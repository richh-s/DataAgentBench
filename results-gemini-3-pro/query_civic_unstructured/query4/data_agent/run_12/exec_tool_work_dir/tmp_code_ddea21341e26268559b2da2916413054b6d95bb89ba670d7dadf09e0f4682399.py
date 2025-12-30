code = """import json
import re

c_path = locals()['var_function-call-2424790631309893722']
f_path = locals()['var_function-call-2424790631309895007']

with open(c_path, 'r') as f:
    docs = json.load(f)
with open(f_path, 'r') as f:
    funds = json.load(f)

projs = []
# Regex to find project blocks.
# Using the bullet point as a delimiter.
# We split by unicode char 190.
b = chr(190)

for d in docs:
    txt = d['text']
    chunks = txt.split(b)
    # chunk[0] is header.
    # chunk[i] starts with Details. Name is at end of chunk[i-1].
    
    for i in range(1, len(chunks)):
        chunk_prev = chunks[i-1].strip()
        chunk_curr = chunks[i]
        
        # Get Name
        if not chunk_prev: continue
        lines = chunk_prev.split('\n')
        name = None
        # Go backwards
        for l in lines[::-1]:
            l = l.strip()
            if not l: continue
            # Check ignored headers
            if 'Capital' in l or 'Agenda' in l or 'Page' in l: continue
            name = l
            break
            
        if not name: continue
        
        # Get Date
        # Look for "Begin Construction: ..."
        # regex: Begin Construction:\s*(.*)
        # We need to escape \s for python string
        m = re.search('Begin Construction:\\s*(.*)', chunk_curr, re.IGNORECASE)
        if m:
            date_val = m.group(1).strip()
            projs.append({'n': name, 'd': date_val})

# Filter
matched_names = []
target_string = '2022'
spring_months = ['March', 'April', 'May', 'Spring']

for p in projs:
    d_str = p['d']
    if target_string in d_str:
        is_sp = False
        for mon in spring_months:
            if mon.lower() in d_str.lower():
                is_sp = True
        if is_sp:
            matched_names.append(p['n'])

matched_names = list(set(matched_names))

# Sum Funding
total = 0
cnt = 0
f_map = {}
for x in funds:
    n = x['Project_Name'].strip()
    a = int(x['Amount'])
    f_map[n] = f_map.get(n, 0) + a

found_list = []
for n in matched_names:
    if n in f_map:
        total += f_map[n]
        cnt += 1
        found_list.append(n)

print('__RESULT__:')
print(json.dumps({'c': cnt, 't': total, 'l': found_list}))"""

env_args = {'var_function-call-16991084151717076996': ['civic_docs'], 'var_function-call-16991084151717078539': ['Funding'], 'var_function-call-14749918171882353165': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_function-call-14749918171882355006': 'file_storage/function-call-14749918171882355006.json', 'var_function-call-2424790631309893722': 'file_storage/function-call-2424790631309893722.json', 'var_function-call-2424790631309895007': 'file_storage/function-call-2424790631309895007.json'}

exec(code, env_args)
