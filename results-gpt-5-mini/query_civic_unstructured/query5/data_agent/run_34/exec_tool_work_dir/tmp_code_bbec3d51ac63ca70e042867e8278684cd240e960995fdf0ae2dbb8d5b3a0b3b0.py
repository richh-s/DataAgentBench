code = """import json
import re
# Load data from storage file paths
with open(var_call_qXyWeXbxZIaUrwEYTixM3McF, 'r') as f:
    funding = json.load(f)
with open(var_call_FKzVcJnzJFUqI8UYDj0rNXAV, 'r') as f:
    civic_docs = json.load(f)

# Normalize funding amounts
for r in funding:
    try:
        r['Amount'] = int(r['Amount'])
    except:
        try:
            r['Amount'] = int(float(r['Amount']))
        except:
            r['Amount'] = 0

start_indicators = ['begin construction', 'begin', 'start', 'start:', 'begin:', 'advertise', 'project schedule', 'project schedule:']
disaster_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'fire', 'recovery', 'woolsey']

matches = []

for fr in funding:
    pname = fr['Project_Name']
    pname_l = pname.lower()
    # derive base name without parenthetical suffix
    base = re.sub(r"\s*\(.*?\)\s*$", '', pname).strip().lower()
    found_flag = False
    started_2022 = False
    disaster_related = False
    # if project name itself contains disaster keywords, mark disaster_related
    if any(k in pname_l for k in disaster_keywords):
        disaster_related = True
    # search documents
    for doc in civic_docs:
        text = doc.get('text','')
        text_l = text.lower()
        # search for base or full name
        idx = text_l.find(base) if base else -1
        if idx == -1:
            idx = text_l.find(pname_l)
        if idx != -1:
            found_flag = True
            # window
            start = max(0, idx-500)
            end = min(len(text_l), idx+500)
            window = text_l[start:end]
            # check disaster keywords in window
            if any(k in window for k in disaster_keywords):
                disaster_related = True
            # check for start indicators near and presence of 2022
            if '2022' in window and any(ind in window for ind in start_indicators):
                started_2022 = True
            # also check patterns like 'begin construction:.*2022' in full doc
            if re.search(r'begin construction:.*?2022', text_l):
                # ensure related to this project by proximity: find nearest 'begin construction' index
                for m in re.finditer(r'begin construction:.*?2022', text_l):
                    mi = m.start()
                    if abs(mi - idx) < 1000:
                        started_2022 = True
            # check lines like 'construction was completed, november 2022' (end in 2022) - not start
            # check lines like 'begin construction: fall 2022' or 'advertise: fall 2022'
            if re.search(r'(advertise:|advertise).*?2022', window):
                # treat advertise in 2022 as starting in 2022
                started_2022 = True
            # other explicit start patterns
            if re.search(r'(start(ed)?|begin(ned)?).*?2022', window):
                started_2022 = True
        # if found and started and disaster, we can stop scanning docs
        if found_flag and started_2022 and disaster_related:
            break
    # Additional heuristic: if not found in docs but pname contains disaster keywords and amount and maybe known 2022 projects in funding names
    # For this task, require started_2022 True and disaster_related True
    if started_2022 and disaster_related:
        matches.append({'Project_Name': pname, 'Amount': fr['Amount']})

# Sum amounts
total = sum(m['Amount'] for m in matches)

# Prepare output
out = {'total_funding': total, 'matched_projects': matches}

import json
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_FKzVcJnzJFUqI8UYDj0rNXAV': 'file_storage/call_FKzVcJnzJFUqI8UYDj0rNXAV.json', 'var_call_qXyWeXbxZIaUrwEYTixM3McF': 'file_storage/call_qXyWeXbxZIaUrwEYTixM3McF.json'}

exec(code, env_args)
