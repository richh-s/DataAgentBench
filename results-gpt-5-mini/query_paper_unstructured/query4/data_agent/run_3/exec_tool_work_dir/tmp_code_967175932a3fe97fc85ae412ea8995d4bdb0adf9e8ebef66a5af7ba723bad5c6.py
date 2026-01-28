code = """import json, re

data_path = var_call_my4cpHWXG9tLcDQhQAOuLRX4
with open(data_path, 'r', encoding='utf-8') as f:
    records = json.load(f)

hits = []
for rec in records:
    filename = rec.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = rec.get('text','')
    if re.search(r'physical activity', text, re.IGNORECASE) and re.search(r'2016', text):
        # find contexts around '2016'
        contexts = []
        for m in re.finditer(r'.{0,40}2016.{0,40}', text):
            contexts.append(m.group(0))
        hits.append({'title': title, 'contexts': contexts[:5]})

print("__RESULT__:")
print(json.dumps(hits))"""

env_args = {'var_call_3GwP5AzT4DdunCaqNOuU9PO6': ['paper_docs'], 'var_call_cemeraGSem194UTTDcmpr7ne': ['Citations', 'sqlite_sequence'], 'var_call_my4cpHWXG9tLcDQhQAOuLRX4': 'file_storage/call_my4cpHWXG9tLcDQhQAOuLRX4.json', 'var_call_wcx4tBKeuw3a6wgVjWKk4E4i': [], 'var_call_JuO8CNjwWTm7g9Dao0RwAxV8': 'file_storage/call_JuO8CNjwWTm7g9Dao0RwAxV8.json', 'var_call_1S46JatRXvJsr3rDP5UD1O7l': 'file_storage/call_1S46JatRXvJsr3rDP5UD1O7l.json', 'var_call_RguK7OioCjDd8wzCO2zpDNMz': []}

exec(code, env_args)
