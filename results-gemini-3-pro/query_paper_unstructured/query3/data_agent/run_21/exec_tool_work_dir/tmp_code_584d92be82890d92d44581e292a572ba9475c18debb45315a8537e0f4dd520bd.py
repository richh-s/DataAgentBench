code = """import json
import re

with open(locals()['var_function-call-8978544678357083899'], 'r') as f:
    papers = json.load(f)

def extract_year(text):
    head = text[:1000]
    matches = re.findall(r'\b(20\d{2})\b', head)
    if matches:
        return int(matches[0])
    return None

debug_info = []
for p in papers:
    title = p['filename'].replace('.txt', '')
    year = extract_year(p['text'])
    has_empirical = "empirical" in p['text'].lower()
    debug_info.append({"title": title, "year": year, "has_empirical": has_empirical})

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-15050569047067534700': 'file_storage/function-call-15050569047067534700.json', 'var_function-call-3142892684795704503': 'file_storage/function-call-3142892684795704503.json', 'var_function-call-8978544678357083899': 'file_storage/function-call-8978544678357083899.json', 'var_function-call-9130584372251179173': 'file_storage/function-call-9130584372251179173.json', 'var_function-call-5001071914055655965': []}

exec(code, env_args)
