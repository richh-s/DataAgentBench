code = """import json
import re

with open(locals()['var_function-call-1188879216130437550'], 'r') as f:
    papers = json.load(f)

debug_info = []
for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    header_text = text[:2000]
    years = re.findall(r'\b(20[0-2][0-9])\b', header_text)
    
    pub_year = int(years[0]) if years else None
    
    has_empirical = "empirical" in text.lower()
    
    debug_info.append({
        "title": title,
        "extracted_year": pub_year,
        "has_empirical": has_empirical
    })

print("__RESULT__:")
print(json.dumps(debug_info, indent=2))"""

env_args = {'var_function-call-563988683724796528': 'file_storage/function-call-563988683724796528.json', 'var_function-call-1188879216130437550': 'file_storage/function-call-1188879216130437550.json', 'var_function-call-6926115911538441459': 'file_storage/function-call-6926115911538441459.json', 'var_function-call-11700601508177380664': []}

exec(code, env_args)
