code = """import json
import re

f_key = 'var_function-call-9396770381544518491'
d_key = 'var_function-call-9396770381544517930'
f_path = locals()[f_key]
d_path = locals()[d_key]

with open(f_path, 'r') as f:
    f_data = json.load(f)

with open(d_path, 'r') as f:
    d_data = json.load(f)

projects = []
for d in d_data:
    txt = d['text']
    lns = txt.splitlines()
    
    for i, ln in enumerate(lns):
        sln = ln.strip()
        if 'Updates:' in sln:
            # Find name backwards
            k = i - 1
            name = 'Unknown'
            while k >= 0:
                p = lns[k].strip()
                if p and 'Page' not in p and 'Agenda' not in p and 'Status Report' not in p:
                    name = p
                    break
                k -= 1
            
            # Read forward for content
            content = sln
            m = i + 1
            while m < len(lns):
                nln = lns[m].strip()
                if 'Updates:' in nln:
                    break
                content += ' ' + nln
                m += 1
            
            projects.append({'name': name, 'text': content})

res = []
for p in projects:
    nm = p['name']
    tx = p['text']
    
    is_dis = False
    if 'FEMA' in nm or 'CalOES' in nm or 'Disaster' in nm:
        is_dis = True
        
    st_2022 = False
    # Check Begin Construction ... 2022
    # We use a simple regex with dotall equivalent
    if re.search(r'Begin Construction.*?2022', tx):
        st_2022 = True
    if re.search(r'Advertise.*?2022', tx):
        st_2022 = True
    
    # Also check if status matches "Not Started" but "Identified"? No, we want "started in 2022".
    # What if "Construction was completed November 2022"?
    # That means it started BEFORE 2022 (likely). 
    # But if it says "Construction started: Jan 2022", that counts.
    # The text usually says "Updates: ...".
    # Let's see if we capture that.
    
    res.append({'n': nm, 'd': is_dis, 's': st_2022, 'snippet': tx[:100]})

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_function-call-9396770381544518491': 'file_storage/function-call-9396770381544518491.json', 'var_function-call-9396770381544517930': 'file_storage/function-call-9396770381544517930.json'}

exec(code, env_args)
