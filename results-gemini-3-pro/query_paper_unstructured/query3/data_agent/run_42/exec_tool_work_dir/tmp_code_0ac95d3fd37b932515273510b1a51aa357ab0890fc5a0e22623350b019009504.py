code = """import json
import re

file_path = locals()['var_function-call-2666164887420722559']
with open(file_path, 'r') as f:
    papers = json.load(f)

debug_info = []

for paper in papers[:10]:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    has_empirical = 'empirical' in text.lower()
    
    header = text[:2000]
    years = re.findall(r'\b(20\d{2})\b', header)
    valid_years = [int(y) for y in years if 2000 <= int(y) <= 2025]
    first_year = valid_years[0] if valid_years else None
    
    debug_info.append({
        "title": title,
        "has_empirical": has_empirical,
        "years_found": valid_years,
        "first_year": first_year,
        "snippet": text[:200]
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-12623071366451944695': 'file_storage/function-call-12623071366451944695.json', 'var_function-call-15611850361610481914': 'file_storage/function-call-15611850361610481914.json', 'var_function-call-2666164887420722559': 'file_storage/function-call-2666164887420722559.json', 'var_function-call-8989207208311259725': []}

exec(code, env_args)
