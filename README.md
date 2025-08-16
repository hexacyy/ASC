# 🛡️ MalCommandGuard

**MalCommandGuard** is a lightweight, modular terminal threat detection engine inspired by Windows Defender. Built in Python for academic and prototype purposes, it monitors command-line input and detects suspicious or malicious behavior using **rule-based**, **signature-based**, and **behavior-based** techniques.

---

## 🚀 Features

* 🧠 **Multi-layer Detection Engine**
  Combines regex rules, MD5 signature matching, and keyword scoring for precise threat classification.

* ⚙️ **Flexible Input Modes**
  Supports interactive input, CSV dataset replay, and simulated live log monitoring.

* 📊 **Detection Verdicts**
  Classifies each command as `Legitimate`, `Suspicious`, or `Malicious` with explainable reasoning.

* 🔒 **Secure by Design**
  Implements input validation, file integrity checks, output sanitization, and error handling.

* 🧪 **Tested & Verified**
  Includes automated unit and regression tests with `pytest` — 94.7% accuracy over 599 real-world command samples.

---

## 🗂️ Folder Structure

```
malcommandguard/
├── main.py               # Main CLI entry point
├── detector.py           # Core detection logic
├── logger.py             # Alert and activity logging
├── alerter.py            # Console alert messages
├── monitor.py            # Simulated live command feed
├── evaluate.py           # Evaluation and accuracy scoring
├── utils.py              # Keyword parsing, file helpers
├── launcher.py           # Unified launcher for all modes
├── tests/                # Pytest test suite
├── data/
│   ├── rules.json
│   ├── signatures.json
│   ├── benign_keywords.json
│   └── cmd_huge_known_commented_updated.csv
├── logs/
│   └── alerts.log
```

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/malcommandguard.git
cd malcommandguard
python3 -m venv fypvenv
source fypvenv/bin/activate
pip install -r requirements.txt
```

---

## 🧪 Run Modes

### 1. Manual Input (Interactive)

```bash
python main.py
```

### 2. CSV Dataset Replay

```bash
python main.py csv
```

### 3. Live Monitoring (Simulated)

```bash
python monitor.py
```

### 4. Evaluation & Metrics

```bash
python evaluate.py
```

### 5. Unified Launcher

```bash
python launcher.py
```

---

## ✅ Sample Output

```
>> Command: powershell -enc aGVsbG8=
[VERDICT] MALICIOUS
[REASON] Rule-Based: matched pattern 'powershell.*-enc'

>> Command: ping 8.8.8.8
[VERDICT] LEGITIMATE
[REASON] Behavior-Based: benign or low-risk keywords []
```

---

## 🧠 Detection Logic

1. **Rule-Based:** Regex pattern matching (e.g., obfuscated PowerShell)
2. **Signature-Based:** MD5 hashes of known malicious command strings
3. **Behavior-Based:** Keyword scoring using risk/benign profiles

---

## 📈 Evaluation Metrics

| Metric    | Value |
| --------- | ----- |
| Accuracy  | 94.7% |
| Precision | 94.3% |
| Recall    | 96.3% |
| F1-Score  | 94.9% |

> Evaluated on 599 manually labeled command samples.

---

## 🔐 Secure Coding Practices

* Input validation for JSON and CSV files
* Output sanitization and log safety
* Read-only config enforcement (`chmod 444`)
* Exception handling and graceful failure

---

## 🧪 Testing

```bash
pytest -v -s tests/
```

Includes:

* Unit tests for detection logic
* Regression tests for accuracy
* Input handling edge cases

---

## 📚 License

MIT – free to use, adapt, and share for academic and non-commercial purposes.

---
