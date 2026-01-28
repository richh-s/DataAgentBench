code = """import json
import re

civic_docs_key = locals()['var_function-call-13888598528909911574']
funding_key = locals()['var_function-call-13888598528909910147']

with open(civic_docs_key, 'r') as f:
    civic_docs = json.load(f)
with open(funding_key, 'r') as f:
    funding_data = json.load(f)

funding_map = {}
for item in funding_data:
    n = item['Project_Name'].strip().lower()
    a = int(item['Amount'])
    if n in funding_map:
        funding_map[n] += a
    else:
        funding_map[n] = a

found = []
for doc in civic_docs:
    text = doc['text']
    # Use chr(10) for newline split to avoid escaping issues
    lines = text.split(chr(10))
    for i, line in enumerate(lines):
        if 'Updates:' in line:
            name = ''
            for k in range(i-1, -1, -1):
                if lines[k].strip():
                    name = lines[k].strip()
                    break
            
            block_lines = []
            for j in range(i, len(lines)):
                if j > i and 'Updates:' in lines[j]:
                    break
                block_lines.append(lines[j])
            block_text = ' '.join(block_lines).lower()
            
            is_park = 'park' in name.lower() or 'playground' in name.lower() or 'recreation' in name.lower() or 'walkway' in name.lower()
            
            completed_2022 = False
            if '2022' in block_text and 'completed' in block_text:
                # regex: completed.{0,30}2022
                if re.search('completed.{0,30}2022', block_text):
                    completed_2022 = True
            
            if is_park and completed_2022:
                found.append(name)

unique_found = list(set(found))
total = 0
matches = []

for p in unique_found:
    p_clean = p.strip().lower()
    matched_amt = 0
    if p_clean in funding_map:
        matched_amt = funding_map[p_clean]
    else:
        for f in funding_map:
            if f in p_clean and len(f) > 5:
                matched_amt = funding_map[f]
                break
            if p_clean in f and len(p_clean) > 5:
                matched_amt = funding_map[f]
                break
    
    if matched_amt > 0:
        total += matched_amt
        matches.append((p, matched_amt))

print('__RESULT__:')
print(json.dumps({'total': total, 'matches': matches}))"""

env_args = {'var_function-call-18388695237617749918': ['civic_docs'], 'var_function-call-18388695237617747301': ['Funding'], 'var_function-call-18388695237617748780': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-18388695237617746163': 'file_storage/function-call-18388695237617746163.json', 'var_function-call-13888598528909911574': 'file_storage/function-call-13888598528909911574.json', 'var_function-call-13888598528909910147': 'file_storage/function-call-13888598528909910147.json'}

exec(code, env_args)
