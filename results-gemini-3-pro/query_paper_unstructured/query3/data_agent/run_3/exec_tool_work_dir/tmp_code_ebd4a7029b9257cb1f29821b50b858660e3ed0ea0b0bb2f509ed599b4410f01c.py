code = """import json
import re

with open(locals()['var_function-call-1637746451261953747'], 'r') as f:
    papers_data = json.load(f)

def get_year(text):
    header = text[:2000]
    matches = re.findall(r'\b(20[0-2][0-9])\b', header)
    valid_years = []
    for m in matches:
        y = int(m)
        if 2000 <= y <= 2025:
            valid_years.append(y)
    if valid_years:
        return valid_years[0]
    return None

debug_list = []
for p in papers_data:
    title = p.get('filename', '').replace('.txt', '')
    text = p.get('text', '')
    year = get_year(text)
    emp = "empirical" in text.lower()
    debug_list.append({"title": title, "year": year, "empirical": emp})

print("__RESULT__:")
print(json.dumps(debug_list))"""

env_args = {'var_function-call-1625983961919980332': 'file_storage/function-call-1625983961919980332.json', 'var_function-call-1625983961919980937': 'file_storage/function-call-1625983961919980937.json', 'var_function-call-603899956623293996': 'file_storage/function-call-603899956623293996.json', 'var_function-call-10661397933404745766': [], 'var_function-call-11800293491939370274': {'count': 5, 'years': [None, None, None, None, None], 'empirical_count': 2, 'gt_2016_count': 0}, 'var_function-call-1637746451261953747': 'file_storage/function-call-1637746451261953747.json', 'var_function-call-14546405968583665070': [{'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'total_citation_count': 278}]}

exec(code, env_args)
