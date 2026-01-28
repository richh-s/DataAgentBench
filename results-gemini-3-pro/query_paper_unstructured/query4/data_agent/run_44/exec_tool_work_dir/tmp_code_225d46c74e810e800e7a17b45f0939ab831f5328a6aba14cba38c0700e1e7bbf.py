code = """import json
import re

file_path = locals()['var_function-call-4863138715288248504']
with open(file_path, 'r') as f:
    papers = json.load(f)

# Debug: Check first 5 papers headers
debug_info = []
count_2016 = 0
count_domain = 0

for paper in papers:
    text = paper.get('text', '')
    header = text[:500]
    
    # Check for 2016 anywhere in header
    has_2016 = "2016" in header or "'16" in header
    if has_2016:
        count_2016 += 1
        
    has_domain = "physical activity" in text.lower()
    if has_domain:
        count_domain += 1
        
    debug_info.append({
        "filename": paper['filename'],
        "header_snippet": header.replace('\n', ' ')[:100],
        "has_2016": has_2016,
        "has_domain": has_domain
    })
    
    if len(debug_info) >= 5:
        break

print("__RESULT__:")
print(json.dumps({"total_papers": len(papers), "count_2016_rough": count_2016, "count_domain": count_domain, "samples": debug_info}))"""

env_args = {'var_function-call-1438467208148862698': 'file_storage/function-call-1438467208148862698.json', 'var_function-call-987307425493553399': 'file_storage/function-call-987307425493553399.json', 'var_function-call-4863138715288248504': 'file_storage/function-call-4863138715288248504.json', 'var_function-call-6286417956079604125': []}

exec(code, env_args)
