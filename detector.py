import json
import re
import os
from utils import hash_command

# Secure Coding: Ensure all required config files exist before loading
required_files = [
    "data/rules.json",
    "data/signatures.json",
    "data/behavior_scoring.json",
    "data/benign_keywords.json"
]

for path in required_files:
    if not os.path.exists(path):
        raise FileNotFoundError(f"[SECURITY] Required config missing: {path}")

# Load detection rules, signatures, behavior scores, and benign keywords
with open("data/rules.json") as f:
    RULES = json.load(f)

with open("data/signatures.json") as f:
    SIGNATURES = json.load(f)

with open("data/behavior_scoring.json") as f:
    BEHAVIOR_SCORES = json.load(f)

with open("data/benign_keywords.json") as f:
    BENIGN_KEYWORDS = json.load(f)


# Rule-Based Detection: Check if command matches any known attack pattern
def match_rule_patterns(cmd):
    for rule in RULES:
        pattern = rule["pattern"]
        if re.search(pattern, cmd, re.IGNORECASE):
            return {
                "verdict": rule["verdict"],
                "reason": f"Rule-Based: matched '{pattern}'"
            }
    return None


# Signature-Based Detection: Match hash of the command with known malicious/suspicious hashes
def match_signature(cmd):
    # Secure Coding: Use hashing to avoid direct content comparison and tampering
    cmd_hash = hash_command(cmd)
    if cmd_hash in SIGNATURES.get("malicious_hashes", []):
        return {
            "verdict": "malicious",
            "reason": f"Signature-Based: hash match {cmd_hash}"
        }
    if cmd_hash in SIGNATURES.get("suspicious_hashes", []):
        return {
            "verdict": "suspicious",
            "reason": f"Signature-Based: suspicious hash match {cmd_hash}"
        }
    return None


# Behavior-Based Detection: Add risk points based on keyword scoring logic
def behavior_score(cmd):
    score = 0.0
    hits = []

    cmd_lower = cmd.lower()

    # Add score for risky behavior keywords
    for keyword, weight in BEHAVIOR_SCORES.items():
        if keyword in cmd_lower:
            score += weight
            hits.append(keyword)

    # Secure Coding: Reduce score for known benign terms to avoid false positives
    for safe_word in BENIGN_KEYWORDS:
        if safe_word in cmd_lower:
            score -= 0.1
            hits.append(f"-{safe_word}")

    # Verdict based on final score
    if score >= 0.6:
        return {
            "verdict": "malicious",
            "reason": f"Behavior-Based: high-risk keywords {hits}"
        }
    elif score >= 0.3:
        return {
            "verdict": "suspicious",
            "reason": f"Behavior-Based: medium-risk keywords {hits}"
        }
    else:
        return {
            "verdict": "legitimate",
            "reason": f"Behavior-Based: benign or low-risk keywords {hits}"
        }


# Main Detection Engine: Combines all detection methods
def analyze_command(cmd):
    # First try rule-based detection
    result = match_rule_patterns(cmd)
    if result:
        return result

    # Then check against known signatures
    result = match_signature(cmd)
    if result:
        return result

    # Fallback to behavior-based analysis
    return behavior_score(cmd)
