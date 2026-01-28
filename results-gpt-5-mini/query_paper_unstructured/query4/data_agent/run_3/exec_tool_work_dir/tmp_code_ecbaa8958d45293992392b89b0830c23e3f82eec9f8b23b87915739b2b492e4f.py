code = """import json, re

data_path = var_call_JuO8CNjwWTm7g9Dao0RwAxV8
with open(data_path, 'r', encoding='utf-8') as f:
    records = json.load(f)

matched = []
for rec in records:
    filename = rec.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = rec.get('text','')
    if re.search(r'physical', text, re.IGNORECASE) and re.search(r'activity', text, re.IGNORECASE):
        # find all years 2000-2026
        years = re.findall(r"\b(20\d{2})\b", text)
        years = [int(y) for y in years]
        # try to infer publication year: look in first 500 chars for 20xx
        head = text[:500]
        m = re.findall(r"\b(20\d{2})\b", head)
        head_years = [int(y) for y in m]
        pub_year = head_years[0] if head_years else (years[0] if years else None)
        if pub_year == 2016:
            matched.append({'title': title, 'pub_year': pub_year})

print("__RESULT__:")
print(json.dumps(matched))"""

env_args = {'var_call_3GwP5AzT4DdunCaqNOuU9PO6': ['paper_docs'], 'var_call_cemeraGSem194UTTDcmpr7ne': ['Citations', 'sqlite_sequence'], 'var_call_my4cpHWXG9tLcDQhQAOuLRX4': 'file_storage/call_my4cpHWXG9tLcDQhQAOuLRX4.json', 'var_call_wcx4tBKeuw3a6wgVjWKk4E4i': [], 'var_call_JuO8CNjwWTm7g9Dao0RwAxV8': 'file_storage/call_JuO8CNjwWTm7g9Dao0RwAxV8.json', 'var_call_1S46JatRXvJsr3rDP5UD1O7l': 'file_storage/call_1S46JatRXvJsr3rDP5UD1O7l.json'}

exec(code, env_args)
