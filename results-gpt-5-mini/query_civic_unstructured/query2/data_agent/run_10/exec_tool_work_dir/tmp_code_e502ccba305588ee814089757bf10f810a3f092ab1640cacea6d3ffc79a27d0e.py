code = """import json
import re

# Load query results from storage-provided file paths
with open(var_call_twkje1XB9wItR2bODeZFtWzA, 'r') as f:
    funding = json.load(f)
with open(var_call_mmDfgxQsjfGR7MR2se4d5CBB, 'r') as f:
    civic_docs = json.load(f)

# Normalize funding amounts and build list
for r in funding:
    # convert Amount to int
    try:
        r['Amount'] = int(r['Amount'])
    except:
        r['Amount'] = 0

# Identify park-related funding records (project name contains 'park' or 'playground')
park_funding = [r for r in funding if re.search(r"\bpark\b|playground", r['Project_Name'], flags=re.I)]

# For each park funding record, check civic docs for a completion in 2022
matched = []
for pf in park_funding:
    pname = pf['Project_Name']
    pname_low = pname.lower()
    found = False
    for doc in civic_docs:
        text = doc.get('text','')
        text_low = text.lower()
        if pname_low in text_low:
            # Check if 'completed' and '2022' appear near the project name
            idx_p = text_low.find(pname_low)
            # find occurrences of 'completed' and '2022'
            idx_completed = text_low.find('completed')
            idx_2022 = text_low.find('2022')
            # consider match if completed and 2022 exist and within 600 chars of project name
            if idx_completed!=-1 and idx_2022!=-1:
                if abs(idx_completed - idx_p) < 600 or abs(idx_2022 - idx_p) < 600:
                    found = True
                    break
            # Alternatively, check sentence-level: find sentences containing project name and check for 2022 and completed
            # split into sentences
            sentences = re.split(r'[\n\.]', text)
            for s in sentences:
                s_low = s.lower()
                if pname_low in s_low and 'completed' in s_low and '2022' in s_low:
                    found = True
                    break
            if found:
                break
    if found:
        matched.append({'Project_Name': pf['Project_Name'], 'Amount': pf['Amount']})

# Additionally, some projects might be referred with slightly different names in funding DB vs docs
# We'll also perform a heuristic: look for any civic doc sentences that mention 'park' and 'completed' and '2022',
# and try to match funded project names that share key tokens.
if not matched:
    # find park-related sentences with completed and 2022
    park_sentences = []
    for doc in civic_docs:
        text = doc.get('text','')
        sentences = re.split(r'[\n\.]', text)
        for s in sentences:
            s_low = s.lower()
            if 'park' in s_low and 'completed' in s_low and '2022' in s_low:
                park_sentences.append(s.strip())
    # try to match funding project names by token overlap
    for s in park_sentences:
        for pf in park_funding:
            # compare tokens
            tokens = re.findall(r"\w+", s.lower())
            pname_tokens = re.findall(r"\w+", pf['Project_Name'].lower())
            # if any significant token overlap
            overlap = set(tokens) & set(pname_tokens)
            if len(overlap) >= 2:
                matched.append({'Project_Name': pf['Project_Name'], 'Amount': pf['Amount']})

# Also, from manual inspection known matches: 'Bluffs Park Shade Structure' and 'Malibu Bluffs Park South Walkway Repairs' maybe
# Check for 'Bluffs Park Shade Structure' specifically if present in funding and civic docs indicate completed Nov 2022
for pf in park_funding:
    if 'bluffs park shade' in pf['Project_Name'].lower():
        # search docs
        for doc in civic_docs:
            if 'bluffs park' in doc.get('text','').lower() and 'completed' in doc.get('text','').lower() and '2022' in doc.get('text','').lower():
                if not any(m['Project_Name']==pf['Project_Name'] for m in matched):
                    matched.append({'Project_Name': pf['Project_Name'], 'Amount': pf['Amount']})

# Remove duplicates
unique = {}
for m in matched:
    unique[m['Project_Name']] = unique.get(m['Project_Name'], 0) + m['Amount']

matched_list = [{'Project_Name': k, 'Amount': v} for k,v in unique.items()]

total = sum(v for v in unique.values())

import json
out = {'matched_projects': matched_list, 'total_funding': total}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_mmDfgxQsjfGR7MR2se4d5CBB': 'file_storage/call_mmDfgxQsjfGR7MR2se4d5CBB.json', 'var_call_twkje1XB9wItR2bODeZFtWzA': 'file_storage/call_twkje1XB9wItR2bODeZFtWzA.json'}

exec(code, env_args)
