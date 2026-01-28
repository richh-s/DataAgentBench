code = """import json
import re

file_path = locals()['var_function-call-4863138715288248504']
with open(file_path, 'r') as f:
    papers = json.load(f)

count_2016 = 0
count_domain = 0
samples = []

for i, paper in enumerate(papers):
    text = paper.get('text', '')
    header = text[:500]
    
    # Check for 2016 anywhere in header
    if "2016" in header or "'16" in header:
        count_2016 += 1
        
    if "physical activity" in text.lower():
        count_domain += 1
        
    if i < 5:
        samples.append({
            "filename": paper['filename'],
            "header": header.replace('\n', ' ')[:100]
        })

print("__RESULT__:")
print(json.dumps({"total": len(papers), "with_2016_header": count_2016, "with_domain": count_domain, "samples": samples}))"""

env_args = {'var_function-call-1438467208148862698': 'file_storage/function-call-1438467208148862698.json', 'var_function-call-987307425493553399': 'file_storage/function-call-987307425493553399.json', 'var_function-call-4863138715288248504': 'file_storage/function-call-4863138715288248504.json', 'var_function-call-6286417956079604125': []}

exec(code, env_args)
