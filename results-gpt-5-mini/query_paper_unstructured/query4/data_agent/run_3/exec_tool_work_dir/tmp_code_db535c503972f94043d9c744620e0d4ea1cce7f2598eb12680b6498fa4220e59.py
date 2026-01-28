code = """import json, re
# Read the stored result file from previous execute_python call
data_path = var_call_ANOcjC5DiYAkCduXkdPgLPwj
with open(data_path, 'r', encoding='utf-8') as f:
    records = json.load(f)

titles_2016 = []
for rec in records:
    title = rec.get('title')
    contexts = rec.get('contexts', [])
    for c in contexts:
        if re.search(r'2016', c):
            titles_2016.append(title)
            break

# deduplicate and sort
titles_2016 = sorted(list(dict.fromkeys(titles_2016)))

import json
print("__RESULT__:")
print(json.dumps(titles_2016))"""

env_args = {'var_call_3GwP5AzT4DdunCaqNOuU9PO6': ['paper_docs'], 'var_call_cemeraGSem194UTTDcmpr7ne': ['Citations', 'sqlite_sequence'], 'var_call_my4cpHWXG9tLcDQhQAOuLRX4': 'file_storage/call_my4cpHWXG9tLcDQhQAOuLRX4.json', 'var_call_wcx4tBKeuw3a6wgVjWKk4E4i': [], 'var_call_JuO8CNjwWTm7g9Dao0RwAxV8': 'file_storage/call_JuO8CNjwWTm7g9Dao0RwAxV8.json', 'var_call_1S46JatRXvJsr3rDP5UD1O7l': 'file_storage/call_1S46JatRXvJsr3rDP5UD1O7l.json', 'var_call_RguK7OioCjDd8wzCO2zpDNMz': [], 'var_call_ANOcjC5DiYAkCduXkdPgLPwj': 'file_storage/call_ANOcjC5DiYAkCduXkdPgLPwj.json', 'var_call_p7gvj2nBXuaZTqs6MrVQ3qUg': []}

exec(code, env_args)
