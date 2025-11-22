# CodeBreaker-Reproduction: Detecting LLM-Transformed Vulnerabilities

**Course:** CS 4371: Computer System Security
**Semester:** Fall 2025
**Team Members:**

- Bruce Homoya III
- Mason Barber
- Santiago Marin Suarez

---

## Project Overview

This project reproduces the core mechanism of the **CODEBREAKER** attack, a sophisticated backdoor attack methodology targeting code completion models.

Modern static analysis tools (SAST) like **Bandit** rely on pattern matching to detect vulnerabilities (e.g., identifying `verify=False` in Python requests). CODEBREAKER leverages the reasoning capabilities of Large Language Models (LLMs) to **transform** these malicious payloads. It rewrites the code to preserve the exact malicious functionality while altering the syntax enough to bypass security scanners.

### Key Contributions

1. **Attack Reproduction:** A fully functional Python pipeline that takes a vulnerable code snippet, uses LLM to mask it, and proves it bypasses the Bandit security scanner.
2. **Defense Proposal:** A conceptual framework for a next-generation defense tool designed to detect these semantic-preserving transformations using "AI vs. AI" anomaly detection.

---

## The "Archeologist" Context

This project sits on the shoulders of two major research milestones in the field of Neural Code Completion poisoning:

### 1. The Foundational Bedrock (Prior Research)

> **Schuster, R., Song, C., Tromer, E., & Shmatikov, V. (2021). You Autocomplete Me: Poisoning Vulnerabilities in Neural Code Completion.** *Proceedings of the 30th USENIX Security Symposium.*

* This is the seminal paper that first demonstrated that neural code completion models (like GPT-2 and Pythia) could be "poisoned." The authors showed that by injecting bad files into the training data, an attacker could force the model to suggest insecure code. It established the threat model that CODEBREAKER builds upon.

### 2. The Contemporary Advancement (Current Work)

> **Aghakhani, H., Dai, W., Manoel, A., Fernandes, X., Kharkar, A., Kruegel, C., et al. (2024). TrojanPuzzle: Covertly Poisoning Code-Suggestion Models.** *Proceedings of the 2024 IEEE Symposium on Security and Privacy (SP).*

* This work attempted to make poisoning attacks stealthier by hiding payloads in comments or docstrings to evade static analysis. CODEBREAKER acknowledges this advancement but improves upon it by embedding payloads directly into functional code, proving that LLM-transformed code is even harder to detect than the "comment-hiding" method proposed in TrojanPuzzle.

---

## Installation & Setup

Follow these steps to clone and build the project environment.

### Prerequisites

- Python 3.11+
- A Gemini API Key (for the transformation agent)

### 1. Clone the Repository

```bash
git clone [https://github.com/YOUR_USERNAME/CODEBREAKER-Reproduction.git](https://github.com/YOUR_USERNAME/CODEBREAKER-Reproduction.git)
cd CodeBreaker-Reproduction
```

### Project Structure

CodeBreaker-Reproduction/
├── .venv/                  			# Python virtual environment
├── data/
│   ├── evasive.py          		# The LLM-transformed code (Output)
│   └── vulnerability.py    		# The original 'bad' code (Input)
├── references/             		# Folder for research papers & docs
├── utils/
|   └── check_models.py         	# Check available models from API key
│   ├── scanner_bandit.py   		# Wrapper for the Bandit security tool
│   └── transformer_LLM.py      	# Wrapper for the Gemini API
├── .env                    			# API keys
├── .gitignore              			# Files to ignore
├── main.py                 			# Main entry point for the demo
├── README.md               		# Project documentation
└── requirements.txt        		# Python dependencies
