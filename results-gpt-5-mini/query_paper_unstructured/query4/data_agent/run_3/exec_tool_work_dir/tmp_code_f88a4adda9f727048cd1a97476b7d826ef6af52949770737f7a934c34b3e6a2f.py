code = """import json, re

# Load Mongo query result file
data_path = var_call_JuO8CNjwWTm7g9Dao0RwAxV8
with open(data_path, 'r', encoding='utf-8') as f:
    records = json.load(f)

titles = []
for rec in records:
    filename = rec.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = rec.get('text','')
    if not (re.search(r'physical', text, re.I) and re.search(r'activity', text, re.I)):
        continue
    header = text[:1000]
    pub2016 = False
    # check explicit 2016
    if re.search(r'\b2016\b', header):
        pub2016 = True
    # check common venue shorthand 'CHI'16', 'UBICOMP '16', 'CSCW '16', 'CHI 2016'
    if re.search(r"\bCHI\s*'?16\b", header, re.I) or re.search(r"\bUBICOMP\s*'?16\b", header, re.I) or re.search(r"\bCSCW\s*'?16\b", header, re.I) or re.search(r"\bWWW\s*'?16\b", header, re.I) or re.search(r"\bIUI\s*'?16\b", header, re.I):
        pub2016 = True
    # check copyright lines
    if re.search(r"\u00a9\s*2016\s*ACM", header) or re.search(r"Copyright\s*2016", header, re.I):
        pub2016 = True
    # check Proceedings of the 2016
    if re.search(r"Proceedings of the 2016", header, re.I):
        pub2016 = True
    if pub2016:
        titles.append(title)

# deduplicate
titles = sorted(list(dict.fromkeys(titles)))
print("__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_call_3GwP5AzT4DdunCaqNOuU9PO6': ['paper_docs'], 'var_call_cemeraGSem194UTTDcmpr7ne': ['Citations', 'sqlite_sequence'], 'var_call_my4cpHWXG9tLcDQhQAOuLRX4': 'file_storage/call_my4cpHWXG9tLcDQhQAOuLRX4.json', 'var_call_wcx4tBKeuw3a6wgVjWKk4E4i': [], 'var_call_JuO8CNjwWTm7g9Dao0RwAxV8': 'file_storage/call_JuO8CNjwWTm7g9Dao0RwAxV8.json', 'var_call_1S46JatRXvJsr3rDP5UD1O7l': 'file_storage/call_1S46JatRXvJsr3rDP5UD1O7l.json', 'var_call_RguK7OioCjDd8wzCO2zpDNMz': [], 'var_call_ANOcjC5DiYAkCduXkdPgLPwj': 'file_storage/call_ANOcjC5DiYAkCduXkdPgLPwj.json'}

exec(code, env_args)
