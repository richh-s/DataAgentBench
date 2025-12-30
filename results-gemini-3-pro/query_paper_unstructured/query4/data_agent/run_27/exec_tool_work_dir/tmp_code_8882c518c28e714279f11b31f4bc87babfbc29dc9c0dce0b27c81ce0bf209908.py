code = """import json
import re

with open(locals()['var_function-call-14323313354234643834'], 'r') as f:
    papers = json.load(f)

debug_info = []
for p in papers[:10]:
    filename = p.get('filename', '')
    text = p.get('text', '')
    header = text[:1000]
    years = re.findall(r'\b(20\d{2})\b', header)
    has_pa = 'physical activity' in text[:5000].lower()
    debug_info.append({"title": filename, "years": years, "has_pa": has_pa})

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-8814252410451424238': ['paper_docs'], 'var_function-call-5259206578733669392': 'file_storage/function-call-5259206578733669392.json', 'var_function-call-14323313354234643834': 'file_storage/function-call-14323313354234643834.json', 'var_function-call-12161874527337870347': ['Citations', 'sqlite_sequence'], 'var_function-call-7764328309385985012': 'file_storage/function-call-7764328309385985012.json', 'var_function-call-3369097710081167039': []}

exec(code, env_args)
