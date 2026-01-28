code = """import json
import re

# Load data from storage variables created by previous tool calls
# var_call_kOWaSCxi0jLwhcn1WZiaSMhY -> civic docs JSON file path
# var_call_39SGDykNb7ZiqRLRRSwCDSO2 -> funding query JSON file path

with open(var_call_kOWaSCxi0jLwhcn1WZiaSMhY, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

with open(var_call_39SGDykNb7ZiqRLRRSwCDSO2, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)

# Build funding dict list
funding = []
for r in funding_records:
    name = r.get('Project_Name')
    amt = r.get('Total_Amount')
    try:
        amt_int = int(amt)
    except:
        # If amount not parseable, skip
        continue
    funding.append({'Project_Name': name, 'Amount': amt_int})

# Keywords for disaster detection
disaster_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'disaster recovery', 'fire', 'woolsey']

matches = []

for rec in funding:
    pname = rec['Project_Name']
    pname_l = pname.lower() if pname else ''
    amount = rec['Amount']
    found_any = False
    started_2022 = False
    disaster_flag = False
    windows = []

    # If project name itself includes disaster keyword, mark disaster_flag
    for kw in disaster_keywords:
        if kw in pname_l:
            disaster_flag = True
            break

    # Search in civic documents
    for doc in civic_docs:
        text = doc.get('text','')
        text_l = text.lower()
        if pname_l and pname_l in text_l:
            found_any = True
            idx = text_l.find(pname_l)
            start = max(0, idx-500)
            end = min(len(text), idx+500)
            window = text[start:end]
            window_l = window.lower()
            windows.append(window)
            # check for year 2022 in window
            if '2022' in window_l:
                started_2022 = True
            # check for disaster keywords in window
            for kw in disaster_keywords:
                if kw in window_l:
                    disaster_flag = True
    
    # Also, if not found in civic docs but name had disaster keyword, we still may want to check other funding naming variants
    # For safety, require started_2022 to be True (must be found in docs mentioning 2022)
    if disaster_flag and started_2022:
        matches.append({'Project_Name': pname, 'Amount': amount, 'Found_Mentions': len(windows), 'Sample_Window': (windows[0][:200] if windows else '')})

# Sum amounts
total = sum(m['Amount'] for m in matches)

# Prepare result
result = {
    'total_funding': total,
    'currency': 'USD',
    'year': 2022,
    'matching_project_count': len(matches),
    'matching_projects': matches
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_oHeT7iP8Cv30S7YtVEOWgNlX': ['civic_docs'], 'var_call_j7Pu5hCC4g0bVP2dGxAFl638': ['Funding'], 'var_call_kOWaSCxi0jLwhcn1WZiaSMhY': 'file_storage/call_kOWaSCxi0jLwhcn1WZiaSMhY.json', 'var_call_39SGDykNb7ZiqRLRRSwCDSO2': 'file_storage/call_39SGDykNb7ZiqRLRRSwCDSO2.json'}

exec(code, env_args)
