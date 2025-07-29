
from detector import analyze_command

def test_rule_based_malicious():
    result = analyze_command("powershell -enc aGVsbG8=")
    assert result['verdict'] == "malicious"

def test_behavior_legitimate():
    result = analyze_command("ping 8.8.8.8")
    assert result['verdict'] == "legitimate"

def test_fallback_behavior():
    result = analyze_command("schtasks /create /tn backup /tr powershell")
    assert result['verdict'] in ["suspicious", "malicious", "legitimate"]
