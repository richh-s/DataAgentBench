code = """import json, re, pandas as pd

# Load data from previous tool outputs (file paths)
with open(var_call_0HuYbdpOwkEqEt8U0wuAk4eE, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_a4GjQBiaExe6srUpfqxdvBxP, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Gather completed project candidate names from civic_docs where completion in 2022 is mentioned
completed_names = set()
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        low = line.lower()
        if 'completed' in low and '2022' in low:
            # look backwards for a plausible project title line
            for j in range(i-1, max(i-8, -1), -1):
                cand = lines[j].strip()
                if not cand:
                    continue
                clow = cand.lower()
                # skip common header/footer or labels
                if any(x in clow for x in ['updates', 'project schedule', 'project description', 'agenda item', 'page', 'recommended action', 'date prepared', 'subject', 'approved by', 'meeting date']):
                    continue
                if cand.startswith('(cid:') or cand.startswith('('):
                    continue
                # reasonable length
                if 3 <= len(cand) <= 200:
                    completed_names.add(cand)
                    break

# Normalize completed names
completed_list = sorted(list(completed_names))

# Define park-related keywords
park_keywords = ['park', 'playground', 'walkway', 'bluff', 'bluffs', 'benches', 'paver', 'shade', 'recreation', 'play area']

# Function to check if a name is park-related
def is_park_related(name):
    ln = name.lower()
    return any(k in ln for k in park_keywords)

# Match funding records to completed park projects
matched_records = []
for rec in funding:
    pname = rec.get('Project_Name', '')
    lam = pname.lower()
    amount = rec.get('Amount')
    try:
        amt = int(amount)
    except:
        try:
            amt = int(float(amount))
        except:
            amt = 0
    matched = False
    # Check match by substring with any extracted completed name
    for cname in completed_list:
        c_low = cname.lower()
        if c_low in lam or lam in c_low:
            # ensure park-related
            if is_park_related(cname) or is_park_related(pname):
                matched = True
                break
    # Also consider records where funding project name itself mentions completed 2022 keywords and park keywords
    # (in case civic doc extraction missed the exact title)
    if not matched:
        # if funding project name is park-related and contains a year token maybe 2022 in funding name? unlikely
        if is_park_related(pname):
            # check if any civic doc text mentions this funding project name with completed and 2022
            pname_low = pname.lower()
            for doc in civic_docs:
                if pname_low in doc.get('text','').lower():
                    # find occurrence and check nearby for completed and 2022
                    idx = doc.get('text','').lower().find(pname_low)
                    window = doc.get('text','').lower()[max(0, idx-200): idx+400]
                    if 'completed' in window and '2022' in window:
                        matched = True
                        break
    if matched:
        matched_records.append({"Project_Name": pname, "Amount": amt})

# Sum amounts
total = sum(r['Amount'] for r in matched_records)

# Prepare result
result = {
    "total_funding": total,
    "matched_records": matched_records,
    "completed_project_names": completed_list
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_WDQsRTE2s47oajSWFaHpCyVp': ['civic_docs'], 'var_call_zQtw7CGGxmsHqHlAGXMxR1T6': ['Funding'], 'var_call_0HuYbdpOwkEqEt8U0wuAk4eE': 'file_storage/call_0HuYbdpOwkEqEt8U0wuAk4eE.json', 'var_call_a4GjQBiaExe6srUpfqxdvBxP': 'file_storage/call_a4GjQBiaExe6srUpfqxdvBxP.json'}

exec(code, env_args)
