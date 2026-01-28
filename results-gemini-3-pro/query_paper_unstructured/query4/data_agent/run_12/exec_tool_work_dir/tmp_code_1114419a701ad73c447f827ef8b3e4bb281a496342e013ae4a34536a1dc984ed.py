code = """import json
import re

file_path = locals()['var_function-call-5896966146300588964']
with open(file_path, 'r') as f:
    papers = json.load(f)

matches = []
for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    if 'physical activity' not in text.lower():
        continue
        
    header = text[:1000]
    
    is_2016 = False
    
    # Check for 2016 in header, and ensure no later years (2017+) appear in header to avoid newer papers citing old ones or proceedings
    if re.search(r'\b2016\b', header):
        # Look for 2017, 2018, 2019, 2020... in header
        if not re.search(r'\b20(1[7-9]|[2-9][0-9])\b', header):
            is_2016 = True
    elif re.search(r"'\s*16\b", header):
        if not re.search(r"'\s*(1[7-9]|[2-9][0-9])\b", header):
            is_2016 = True
            
    if is_2016:
        matches.append(title)

print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_function-call-2683298839036433804': ['paper_docs'], 'var_function-call-17469928963468779101': 'file_storage/function-call-17469928963468779101.json', 'var_function-call-5896966146300588964': 'file_storage/function-call-5896966146300588964.json'}

exec(code, env_args)
