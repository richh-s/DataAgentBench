code = """import json
import re

# Load papers
with open(locals()['var_function-call-603899956623293996'], 'r') as f:
    papers_data = json.load(f)

debug_info = {}
debug_info['count'] = len(papers_data)
debug_info['years'] = []
debug_info['empirical_count'] = 0
debug_info['gt_2016_count'] = 0

def extract_year(text):
    header = text[:1000]
    matches = re.findall(r'\b(20\d{2})\b', header)
    if matches:
        for y in matches:
            if 2000 <= int(y) <= 2025:
                return int(y)
    return None

for p in papers_data[:10]: # Check first 10
    text = p.get('text', '')
    y = extract_year(text)
    debug_info['years'].append(y)

for p in papers_data:
    text = p.get('text', '')
    y = extract_year(text)
    emp = "empirical" in text.lower()
    
    if emp:
        debug_info['empirical_count'] += 1
    if y and y > 2016:
        debug_info['gt_2016_count'] += 1

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-1625983961919980332': 'file_storage/function-call-1625983961919980332.json', 'var_function-call-1625983961919980937': 'file_storage/function-call-1625983961919980937.json', 'var_function-call-603899956623293996': 'file_storage/function-call-603899956623293996.json', 'var_function-call-10661397933404745766': []}

exec(code, env_args)
