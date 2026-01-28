code = """import json
import re

try:
    with open(locals()['var_function-call-5276622005229675102'], 'r') as f:
        papers = json.load(f)
except:
    papers = []

debug_info = []
debug_info.append(f"Total papers: {len(papers)}")

count = 0
for p in papers:
    if count > 5: break
    text = p.get('text', '')
    header = text[:500]
    info = {
        "filename": p.get('filename'),
        "header_snippet": header,
        "has_physical_activity": 'physical activity' in text.lower(),
        "has_2016_header": '2016' in header
    }
    debug_info.append(info)
    count += 1

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-13566097313952112574': 'file_storage/function-call-13566097313952112574.json', 'var_function-call-5276622005229675102': 'file_storage/function-call-5276622005229675102.json', 'var_function-call-15838140455159973064': [], 'var_function-call-16252018297350116542': 'Debug info printed'}

exec(code, env_args)
