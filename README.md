### Python Zodiac Sign
**Discover your star sign and grab a daily horoscope reading.**   
**Behold... this is the crystal ball that you always wanted.**

---

### Quick start 
**Clone this repo:**  
```git clone git@github.com:neilburbage/Python-Zodiac-Sign.git```  
**Make sure you've added your SSH key first:**   
```https://docs.github.com/en/authentication/connecting-to-github-with-ssh```    
```cd Python-Zodiac-Sign```  
**Create a virtual environment:**     
```python -m venv .venv```  
```# Linux / macOS: source .venv/bin/activate```     
```# Windows (PowerShell): .venv\Scripts\Activate.ps1```  
```# Windows (cmd): .venv\Scripts\activate.bat```  
**Install dependencies:**    
```pip install -r requirements.txt```  

___

### Example astrology reading:               

<small>
<strong><em>Enter your name: Ada Lovelace</em></strong><br>
<strong><em>Enter your date of birth (YYYY-MM-DD): 1815-12-10</em></strong><br><br>
<strong><em>Ada Lovelace, 1815-12-10, Sagittarius,</em></strong><br>
<strong><em>"Today could be filled with…"</em></strong>
</small>

---

### Dependencies guide

| Purpose                     | Library  |
|-----------------------------|----------|
| HTTP requests               | requests |
| Data handling & CSV export  | pandas   |
| Project-local environment   | .venv/   |

---

### Project layout
```
Python-Zodiac-Sign/
│
├── astro.py              # main script (CLI, API client and zodiac helper)
├── zodiac_results.csv    # generated at runtime
├── requirements.txt      # requests, pandas
├── .gitignore            # .venv/, __pycache__/
└── README.md             # you are here
```
---
