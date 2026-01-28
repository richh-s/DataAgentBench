code = """import json
import re

# Load data from storage files
with open(var_call_mLDS1c7AFshKWRzpb4qcL0oI, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_tvxBDixjkLkzSP6Indag6T4A, 'r') as f:
    funding = json.load(f)

# Prepare list of disaster keywords
disaster_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'fire', 'woolsey', 'fema/caloes', 'caloes/fema']

def is_disaster_related(name, context):
    text = (name + ' ' + context).lower()
    for kw in disaster_keywords:
        if kw in text:
            return True
    return False

# For each funding record, search civic docs for project name and nearby 2022
matched_funding = []
for rec in funding:
    pname = rec.get('Project_Name','')
    amount = rec.get('Amount',0)
    try:
        amt = int(amount)
    except:
        try:
            amt = int(float(amount))
        except:
            amt = 0
    found = False
    disaster_flag = False
    for doc in civic_docs:
        text = doc.get('text','')
        # find all occurrences of pname in text, case-insensitive
        for m in re.finditer(re.escape(pname), text, flags=re.IGNORECASE):
            start = max(0, m.start()-200)
            end = min(len(text), m.end()+200)
            context = text[start:end]
            # check for '2022' in context
            if '2022' in context:
                found = True
                if is_disaster_related(pname, context):
                    disaster_flag = True
                else:
                    # also check if project name itself has FEMA-like suffix
                    if re.search(r'\(.*fema.*\)', pname, flags=re.IGNORECASE) or re.search(r'\(.*caloes.*\)', pname, flags=re.IGNORECASE) or re.search(r'\(.*caljpia.*\)', pname, flags=re.IGNORECASE):
                        disaster_flag = True
                # if found, break
                break
        if found:
            break
    # Additionally, if pname itself contains disaster keywords and funding table only (no civic doc mention), check civic docs globally for 2022 nearby occurrences using just keywords
    if not found:
        # search for project name as partial match: remove parentheses content
        short_name = re.sub(r'\s*\(.*?\)\s*','', pname)
        for doc in civic_docs:
            text = doc.get('text','')
            if re.search(re.escape(short_name), text, flags=re.IGNORECASE):
                start = max(0, m.start()-200)
                end = min(len(text), m.end()+200)
                context = text[start:end]
                if '2022' in context:
                    found = True
                    if is_disaster_related(pname, context):
                        disaster_flag = True
                    break
    # As another heuristic: if pname contains disaster suffix and funding table row exists, and any civic doc contains the plain project name and '2022' anywhere, mark it
    if not found and re.search(r'\(.*fema.*\)|\(.*caloes.*\)|\(.*caljpia.*\)', pname, flags=re.IGNORECASE):
        plain = re.sub(r'\s*\(.*?\)\s*','', pname)
        for doc in civic_docs:
            if plain.lower() in doc.get('text','').lower() and '2022' in doc.get('text',''):
                found = True
                disaster_flag = True
                break

    if found and disaster_flag:
        matched_funding.append({'Project_Name': pname, 'Amount': amt})

# Sum amounts
total = sum(r['Amount'] for r in matched_funding)

# Prepare output
output = {
    'total_funding_disaster_projects_started_2022': total,
    'matched_projects_count': len(matched_funding),
    'matched_projects': matched_funding[:100]
}

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_5AL8taEGIdtt2mrsby6EHuFp': ['civic_docs'], 'var_call_ivAlOzjJ2tN3U0HiIWt3xFuR': ['Funding'], 'var_call_mLDS1c7AFshKWRzpb4qcL0oI': 'file_storage/call_mLDS1c7AFshKWRzpb4qcL0oI.json', 'var_call_tvxBDixjkLkzSP6Indag6T4A': 'file_storage/call_tvxBDixjkLkzSP6Indag6T4A.json'}

exec(code, env_args)
