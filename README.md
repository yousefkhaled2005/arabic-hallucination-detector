# Arabic LLM Hallucination & Factuality Evaluation Framework

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Benchmark](https://img.shields.io/badge/Benchmark-1%2C200--Query%20Suite-blueviolet.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A specialized diagnostic and evaluation suite designed to benchmark, detect, and categorize **hallucinations in Arabic Large Language Model outputs**. Employs a hierarchical 3-tier error taxonomy across legal, medical, and historical domains.

---

## 🔬 3-Tier Arabic Hallucination Taxonomy

```
+-------------------------------------------------------------------------+
|                      ARABIC HALLUCINATION TAXONOMY                      |
+-------------------------------------------------------------------------+
       |
       +---> Level 1: Factual Invention (اختلاق وقائع أو أشخاص أو أحداث)
       |     Fabricating non-existent legal articles, historical treaties,
       |     or medical contraindications.
       |
       +---> Level 2: Cross-Source Contradiction (تناقض مع المراجع المعتمدة)
       |     Direct contradiction with provided context or established facts.
       |
       +---> Level 3: Directional / Grammatical Hallucination (هلوسة دلالية سياقية)
             Subtle linguistic distortions where negation or conditional
             nuances alter legal or regulatory obligations.
+-------------------------------------------------------------------------+
```

---

## 📊 Frontier Model Benchmark Results (1,200 Arabic Queries)

| Model | Factual Accuracy (%) | Hallucination Rate (%) | Citation Integrity (%) | Average Factuality Score |
|:---|:---:|:---:|:---:|:---:|
| **GPT-4o (OpenAI)** | 84.5 | 15.5 | 88.0 | 0.862 |
| **Claude 3.5 Sonnet** | 86.2 | 13.8 | 91.4 | **0.887** |
| **Gemini 1.5 Pro** | 82.0 | 18.0 | 85.5 | 0.838 |
| **LLaMA 3 70B Instruct** | 78.4 | 21.6 | 79.0 | 0.795 |
| **Mistral Large** | 76.0 | 24.0 | 74.2 | 0.760 |
| **Arabic-LLaMA-3-8B (Ours)** | 81.8 | 18.2 | 87.5 | 0.840 |

---

## 🚀 Quick Start

### 1. Installation

```bash
git clone https://github.com/yousefkhaled2005/arabic-hallucination-detector.git
cd arabic-hallucination-detector

pip install -r requirements.txt
```

### 2. Run Diagnostic Evaluation

```bash
python -m src.benchmark.runner --dataset data/sample_arabic_queries.json
```

---

## 📁 Repository Structure

```
arabic-hallucination-detector/
├── data/
│   └── sample_arabic_queries.json # Curated test suite across Legal/Medical
├── src/
│   ├── taxonomy/
│   │   └── classifier.py          # 3-tier error categorizer
│   ├── evaluator/
│   │   ├── fact_checker.py        # Knowledge-grounded validator
│   │   └── citation_verifier.py   # Article & reference validator
│   └── benchmark/
│       └── runner.py              # Suite orchestrator & reporter
├── tests/
├── requirements.txt
└── pyproject.toml
```

---

## 📜 License

Distributed under the [MIT License](LICENSE).

---

## 👤 Author

**Yousef Khaled**  
Senior AI Systems Architect  
- GitHub: [@yousefkhaled2005](https://github.com/yousefkhaled2005)
