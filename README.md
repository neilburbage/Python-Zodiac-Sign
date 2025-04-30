## Quick start

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
python astro.py
               

Enter your name: Ada Lovelace
Enter your date of birth (YYYY-MM-DD): 1815-12-10

Ada Lovelace, 1815-12-10, Sagittarius,
"Today could be filled with…


| Purpose | Library |
|---------|---------|
| HTTP call | `requests` |
| Data collection & CSV export | `pandas` |
| Virtual environment | `venv/` (ignored via `.gitignore`) |

Python-Zodiac-Sign/
│
├── astro.py              # main script (CLI + API client + zodiac helper)
├── zodiac_results.csv    # generated at runtime
├── requirements.txt      # requests, pandas
├── venv/                 # local virtual-env (git-ignored)
└── .gitignore


