code = """import json
import re

# Load data from storage file paths provided by previous tool calls
with open(var_call_lzuql9XO4mip4vcz5jSfIR6d, 'r') as f:
    funding_data = json.load(f)

with open(var_call_OTWLMZF2U2vjKkDgiSiAfRbv, 'r') as f:
    civic_docs = json.load(f)

# Normalize funding records to list of dicts
fund_df = funding_data

# Helper to normalize project name by removing parenthetical suffixes and extra whitespace
def normalize_name(name):
    # Remove content in parentheses
    n = re.sub(r"\(.*?\)", "", name)
    return re.sub(r"\s+", " ", n).strip().lower()

# Combine all civic doc texts into one large text as well as keep per-doc
all_texts = [doc.get('text','') for doc in civic_docs]
all_text_combined = "\n".join(all_texts).lower()

# Keywords to directly identify FEMA/emergency-related funding entries
direct_keywords = re.compile(r"fema|emergency|outdoor warning|sirens|backup power|disaster", re.I)

results = []

for row in fund_df:
    pname = row.get('Project_Name','')
    psource = row.get('Funding_Source','')
    amount = row.get('Amount')
    try:
        amount = int(amount)
    except:
        try:
            amount = int(float(amount))
        except:
            amount = None

    pname_norm = normalize_name(pname)

    # Determine if project is related: either project name contains direct keywords OR appears in any civic doc that contained 'emergency'/'FEMA'
    related = False
    if direct_keywords.search(pname):
        related = True
    else:
        # check if normalized name appears in any civic doc text
        for t in all_texts:
            if pname_norm and pname_norm in t.lower():
                related = True
                break

    if not related:
        continue

    # Find status by searching civic docs for occurrences and checking nearby context
    status = None
    # search in all_texts for the project
    for t in all_texts:
        tl = t.lower()
        idx = tl.find(pname_norm)
        if idx == -1:
            # also try without normalization: look for original project name substring
            idx = tl.find(pname.lower())
        if idx == -1:
            continue
        # Extract window around match
        start = max(0, idx-300)
        end = min(len(tl), idx+300)
        window = tl[start:end]
        # Check for completed keywords
        if any(k in window for k in ['construction was completed', 'notice of completion', 'complete construction', 'completed', 'complete construction:']):
            status = 'completed'
            break
        # Check for design-related keywords
        if any(k in window for k in ['design', 'complete design', 'preliminary design', 'working with the consultant', 'finalize the design', 'advertise', 'submit to the county for review', 'awaiting final fema', 'awaiting final caloes', 'awaiting final fema/caloes', 'awaiting approval']):
            status = 'design'
            break
        # Check for not started
        if any(k in window for k in ['not started', 'identified', 'waiting for the agreement', 'waiting for agreement', 'waiting for the agreement', 'will be issuing a rfq', 'schedule for council', 'to be discussed']):
            status = 'not started'
            break
        # Check for under construction -> treat as design (active)
        if 'under construction' in window or 'begin construction' in window or 'begin construction:' in window or 'begin construction' in window:
            status = 'design'
            break
    # If status still None, attempt to infer from project name mentioning FEMA -> assume design if awaiting approval words in combined doc
    if status is None:
        if 'awaiting' in all_text_combined or 'fema' in pname.lower():
            status = 'design'

    results.append({
        'Project_Name': pname,
        'Funding_Source': psource,
        'Amount': amount,
        'Status': status
    })

# Remove duplicates by Project_Name keeping first
seen = set()
unique_results = []
for r in results:
    if r['Project_Name'] not in seen:
        seen.add(r['Project_Name'])
        unique_results.append(r)

import json
print('__RESULT__:')
print(json.dumps(unique_results))"""

env_args = {'var_call_OTWLMZF2U2vjKkDgiSiAfRbv': 'file_storage/call_OTWLMZF2U2vjKkDgiSiAfRbv.json', 'var_call_lzuql9XO4mip4vcz5jSfIR6d': 'file_storage/call_lzuql9XO4mip4vcz5jSfIR6d.json'}

exec(code, env_args)
