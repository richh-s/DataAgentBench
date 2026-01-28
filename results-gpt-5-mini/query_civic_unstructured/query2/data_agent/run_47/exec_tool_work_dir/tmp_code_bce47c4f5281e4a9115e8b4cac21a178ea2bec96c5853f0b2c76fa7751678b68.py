code = """import json
import re
import pandas as pd

# Load the query results from storage files
with open(var_call_E8QO6jZvQ5TaJuqjapMUgTc1, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_FmdCSvGxyiKxUNfv0qmPCsJd, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Convert funding to DataFrame
fund_df = pd.DataFrame(funding)
# Ensure Amount numeric
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Keywords to consider as park-related
keywords = ['park', 'playground', 'playground', 'play', 'walkway', 'bluffs', 'bench', 'arboretum', 'pavilion', 'shade', 'playground', 'playground']

# Helper to get significant tokens from a project name
def significant_tokens(name):
    toks = re.findall(r"\w+", name.lower())
    return [t for t in toks if len(t) > 3]

# Build list of civic doc texts
texts = [d.get('text','').lower() for d in civic_docs]

matched_rows = []

# Iterate funding rows and identify park-related
for idx, row in fund_df.iterrows():
    pname = row['Project_Name']
    lname = pname.lower()
    if any(k in lname for k in keywords):
        # search in civic docs
        toks = significant_tokens(pname)
        found = False
        for text in texts:
            if lname in text:
                # exact substring found; check completion and 2022 near occurrence
                pos = text.find(lname)
                window = text[max(0,pos-200):pos+200]
                if 'completed' in window and '2022' in window:
                    found = True
                    break
                # also check if 'construction was completed' elsewhere with 2022 in doc
                if 'completed' in text and '2022' in text:
                    found = True
                    break
            else:
                # check if all significant tokens appear in the same vicinity
                if toks:
                    # check if all tokens present in text
                    if all(t in text for t in toks):
                        # find first token pos
                        positions = [text.find(t) for t in toks]
                        minpos = min(positions)
                        maxpos = max(positions)
                        if maxpos - minpos < 300:
                            window = text[max(0,minpos-200):maxpos+200]
                            if 'completed' in window and '2022' in window:
                                found = True
                                break
                            if 'completed' in text and '2022' in text:
                                found = True
                                break
        if found:
            matched_rows.append({'Project_Name': pname, 'Amount': int(row['Amount'])})

# As a fallback, also scan civic docs for any phrases that look like park projects completed in 2022
# Extract sentences containing 'completed' and '2022' and see if they mention 'park' or keywords
extra_matches = []
for d in civic_docs:
    text = d.get('text','')
    # Split into lines for more context
    lines = re.split(r"\n+", text)
    for line in lines:
        low = line.lower()
        if 'completed' in low and '2022' in low:
            if any(k in low for k in ['park','playground','walkway','bluffs','malibu bluffs','play']):
                # try to find matching funding rows by checking project name tokens in the line
                for idx, row in fund_df.iterrows():
                    pname = row['Project_Name']
                    if any(w.lower() in low for w in re.findall(r"\w+", pname) if len(w)>3):
                        entry = {'Project_Name': pname, 'Amount': int(row['Amount'])}
                        if entry not in matched_rows and entry not in extra_matches:
                            extra_matches.append(entry)

# Combine matches
all_matches = matched_rows + extra_matches

# Deduplicate by project name
unique = {}
for m in all_matches:
    unique[m['Project_Name']] = unique.get(m['Project_Name'], 0) + m['Amount']

# Prepare result list
result_list = [{'Project_Name': k, 'Amount': v} for k,v in unique.items()]

total = sum(v for v in unique.values())

# If no matches found, return zero
output = {'total_funding_completed_in_2022_for_park_related_projects': total, 'projects': result_list}

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_XnYVyMzjKWY45aFJ7l2K2SZ6': ['civic_docs'], 'var_call_gFOOFrxGtfA1pqMBT4gj7G4r': ['Funding'], 'var_call_E8QO6jZvQ5TaJuqjapMUgTc1': 'file_storage/call_E8QO6jZvQ5TaJuqjapMUgTc1.json', 'var_call_FmdCSvGxyiKxUNfv0qmPCsJd': 'file_storage/call_FmdCSvGxyiKxUNfv0qmPCsJd.json'}

exec(code, env_args)
