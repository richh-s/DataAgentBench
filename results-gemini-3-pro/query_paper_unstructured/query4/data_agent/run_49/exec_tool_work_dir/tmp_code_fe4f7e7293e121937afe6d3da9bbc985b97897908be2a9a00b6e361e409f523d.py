code = """import json
import re

file_path = locals()['var_function-call-11172061455759427872']
with open(file_path, 'r') as f:
    papers = json.load(f)

debug_results = []
count = 0

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    
    if 'physical activity' in text.lower():
        header = text[:1000] # Increase to 1000
        years_4d = re.findall(r'\b(201[0-9])\b', header)
        years_2d = re.findall(r"['’](1[0-9])\b", header)
        
        candidates = []
        if years_4d:
            candidates.extend([int(y) for y in years_4d])
        if years_2d:
            candidates.extend([int('20' + y) for y in years_2d])
            
        debug_results.append({
            "filename": filename,
            "candidates": candidates,
            "header_snippet": header[:200].replace('\n', ' ')
        })
        count += 1
        if count >= 10:
            break

print("__RESULT__:")
print(json.dumps(debug_results))"""

env_args = {'var_function-call-3489125586506889844': 'file_storage/function-call-3489125586506889844.json', 'var_function-call-3489125586506887483': ['Citations', 'sqlite_sequence'], 'var_function-call-13585702268998000327': 'file_storage/function-call-13585702268998000327.json', 'var_function-call-13585702268998000192': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-11172061455759427872': 'file_storage/function-call-11172061455759427872.json', 'var_function-call-12104304543771652425': []}

exec(code, env_args)
