code = """import json, re
import pandas as pd

# Load data from previous tool results (file paths provided in variables)
with open(var_call_wlY2mHtpBD98Uutf9sIYifjA, 'r') as f:
    funding_records = json.load(f)
with open(var_call_4S2HlYk8zlzZAvhNJDENa2BX, 'r') as f:
    civic_docs = json.load(f)

# Convert funding to DataFrame
df = pd.DataFrame(funding_records)
# Ensure Amount is integer
def parse_amount(x):
    try:
        return int(float(x))
    except:
        return 0

if 'Amount' in df.columns:
    df['Amount'] = df['Amount'].apply(parse_amount)
else:
    df['Amount'] = 0

# Precompute civic docs text concatenation
all_texts = [d.get('text','') for d in civic_docs]
all_text_lower = [t.lower() for t in all_texts]

# Disaster keywords
disaster_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'fire', 'woolsey', 'flood']

def is_disaster_name(name):
    nl = name.lower()
    return any(k in nl for k in disaster_keywords)

results = []
total = 0

for _, row in df.iterrows():
    pname = str(row.get('Project_Name','')).strip()
    amount = int(row.get('Amount',0))
    core = re.sub(r"\s*\(.*?\)", '', pname).strip().lower()
    found_disaster = False
    found_2022 = False

    # Quick check on name
    if is_disaster_name(pname):
        found_disaster = True

    # Search in civic docs
    for text in all_text_lower:
        # look for core name or full name
        idx = -1
        if core and core in text:
            idx = text.find(core)
        elif pname.lower() in text:
            idx = text.find(pname.lower())
        if idx >= 0:
            window = text[max(0, idx-300): idx+300]
            if any(k in window for k in disaster_keywords):
                found_disaster = True
            if '2022' in window:
                found_2022 = True
            # also check lines nearby for 'Begin' or 'Begin Construction' with 2022
            # look a bit further
            window2 = text[max(0, idx-600): idx+600]
            # find patterns like 'Begin Construction:' or 'Begin Construction' or 'Begin' near and '2022'
            if 'begin' in window2 and '2022' in window2:
                found_2022 = True
            if ('construction was completed' in window2 or 'complete construction' in window2 or 'completed,' in window2) and '2022' in window2:
                found_2022 = True
            # early exit if both true
            if found_disaster and found_2022:
                break

    # Additional heuristic: if not found_2022, check entire documents for project name + '2022' anywhere
    if not found_2022 and (core in ''.join(all_text_lower) or pname.lower() in ''.join(all_text_lower)):
        bigtext = ' '.join(all_text_lower)
        # find index of core
        idxb = bigtext.find(core) if core in bigtext else bigtext.find(pname.lower())
        if idxb >=0:
            windowb = bigtext[max(0, idxb-500): idxb+500]
            if '2022' in windowb:
                found_2022 = True

    if found_disaster and found_2022:
        total += amount
        results.append({'Project_Name': pname, 'Amount': amount})

# Prepare output
out = {'total_funding': total, 'matching_projects': results}

import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_4S2HlYk8zlzZAvhNJDENa2BX': 'file_storage/call_4S2HlYk8zlzZAvhNJDENa2BX.json', 'var_call_qi2a3nmPwTUl0tMFS3ZnEXNW': ['Funding'], 'var_call_wlY2mHtpBD98Uutf9sIYifjA': 'file_storage/call_wlY2mHtpBD98Uutf9sIYifjA.json'}

exec(code, env_args)
