# AI-Agent-Challenge

Coding agent that can automatically generate custom parsers for bank statement PDFs.  

---

## How it works
The agent (`agent.py`) follows an **agent loop**:

**Plan → Generate Parser → Run Tests → Self-Fix (≤3 attempts)**  

It uses PDF/CSV pairs from `data/<bank>` to write a parser under `custom_parsers/`.  
The parser must return a `pandas.DataFrame` identical to the provided CSV.  

---

## Steps to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/janhavi-28/ai-agent-challenge.git
   cd ai-agent-challenge
# AI-Agent-Challenge

Coding agent that can automatically generate custom parsers for bank statement PDFs.  

---

## How it works
The agent (`agent.py`) follows an **agent loop**:

**Plan → Generate Parser → Run Tests → Self-Fix (≤3 attempts)**  

It uses PDF/CSV pairs from `data/<bank>` to write a parser under `custom_parsers/`.  
The parser must return a `pandas.DataFrame` identical to the provided CSV.  

---

## Steps to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/janhavi-28/ai-agent-challenge.git
   cd ai-agent-challenge
2. **Create virtual environment**
   bash
   python -m venv .venv
   source .venv/bin/activate     # Mac/Linux
   .venv\Scripts\activate        # Windows
3. **Install dependencies**
   bash
   pip install -r requirements.txt
4. **Run the agent**
   bash
   python agent.py --target icici
This will read:

data/icici/icici_sample.pdf

data/icici/icici_sample.csv

And generate:

custom_parsers/icici_parser.py

5. **Run tests
   pytest -q
   

