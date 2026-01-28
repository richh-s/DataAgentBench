code = """import json
import re

file_path = locals()['var_function-call-4290533744407008086']
with open(file_path, 'r') as f:
    docs = json.load(f)

print(f"Total docs: {len(docs)}")

debug_info = []

for doc in docs[:20]:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    header = text[:1000]
    years = re.findall(r'\b(20\d{2})\b', header)
    pub_year = None
    if years:
        years = [int(y) for y in years]
        valid_years = [y for y in years if 2000 <= y <= 2025]
        if valid_years:
            pub_year = valid_years[0]
            
    is_empirical = 'empirical' in text.lower()
    
    debug_info.append({"title": title, "year": pub_year, "empirical": is_empirical})

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-1070528273488687685': ['paper_docs'], 'var_function-call-1070528273488689510': ['Citations', 'sqlite_sequence'], 'var_function-call-3440707792195880886': 'file_storage/function-call-3440707792195880886.json', 'var_function-call-4290533744407008086': 'file_storage/function-call-4290533744407008086.json', 'var_function-call-9474119233572840717': []}

exec(code, env_args)
