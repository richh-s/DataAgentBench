code = """import json
import re

file_path = locals()['var_function-call-4863138715288248504']
with open(file_path, 'r') as f:
    papers = json.load(f)

candidates = []

for paper in papers:
    text = paper.get('text', '')
    if "physical activity" in text.lower():
        # Find all years in the first 1000 chars
        years = re.findall(r'20\d\d', text[:1000])
        candidates.append({
            "filename": paper['filename'],
            "years_found": years,
            "header_snippet": text[:200]
        })

print("__RESULT__:")
print(json.dumps(candidates))"""

env_args = {'var_function-call-1438467208148862698': 'file_storage/function-call-1438467208148862698.json', 'var_function-call-987307425493553399': 'file_storage/function-call-987307425493553399.json', 'var_function-call-4863138715288248504': 'file_storage/function-call-4863138715288248504.json', 'var_function-call-6286417956079604125': []}

exec(code, env_args)
