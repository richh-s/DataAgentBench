code = """import json

# Load data
with open(var_call_Rzijr1ISlDUOM9pATv8LIjjx, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_Ux2JQYUAZi3uGCxmtmShczUi, 'r') as f:
    funding_records = json.load(f)

# normalize helper: remove parenthetical and non-alphanum except spaces
import re

def normalize(name):
    if not name:
        return ''
    # remove parenthetical content
    name = name.split('(')[0]
    s = name.lower()
    s = re.sub(r'[^a-z0-9 ]+', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

# ensure Amount int
for r in funding_records:
    try:
        r['Amount'] = int(r.get('Amount', 0))
    except:
        r['Amount'] = int(re.sub(r'[^0-9]', '', str(r.get('Amount','0'))))

# disaster keywords
disaster_kw = ['fema', 'caloes', 'caljpia', 'fema/', 'fire', 'disaster', 'disaster recovery', 'woolsey']

# prepare normalized civic docs text
civic_texts = []
for doc in civic_docs:
    text = doc.get('text','')
    norm_text = re.sub(r'[^a-z0-9 ]+', ' ', text.lower())
    civic_texts.append({'orig': text, 'norm': norm_text})

included = []

for r in funding_records:
    pname = r.get('Project_Name','')
    norm_p = normalize(pname)
    is_disaster_name = any(kw in norm_p for kw in disaster_kw)
    found_match = False
    # check occurrences in civic docs
    for doc in civic_texts:
        if norm_p and norm_p in doc['norm']:
            # check if doc mentions 2022
            if '2022' in doc['orig']:
                # extract window around first occurrence in original text
                idx = doc['orig'].lower().find(norm_p)
                # compute window
                start = max(0, idx-200)
                end = min(len(doc['orig']), idx+200)
                window = doc['orig'][start:end].lower()
                # if window or doc contains disaster keywords or project name indicates disaster
                if is_disaster_name or any(kw in window for kw in disaster_kw) or any(kw in doc['orig'].lower() for kw in disaster_kw):
                    included.append({'funding_id': r.get('Funding_ID'), 'project_name': pname, 'amount': r['Amount']})
                    found_match = True
                    break
        else:
            # even if project name doesn't appear, if name itself indicates disaster and doc mentions 2022 and contains parts of project name words
            if is_disaster_name and '2022' in doc['orig']:
                # check if major words in project name appear in doc
                words = [w for w in norm_p.split() if len(w)>3]
                if words and all(any(w in doc['norm'] for doc in [doc]) for w in words[:2]):
                    included.append({'funding_id': r.get('Funding_ID'), 'project_name': pname, 'amount': r['Amount']})
                    found_match = True
                    break
    # also if project name itself indicates disaster and we didn't find doc match, try to match by base name presence in any doc when doc has 2022 and disaster kw
    if not found_match and is_disaster_name:
        for doc in civic_texts:
            if '2022' in doc['orig'] and any(kw in doc['orig'].lower() for kw in disaster_kw):
                # include as precaution
                included.append({'funding_id': r.get('Funding_ID'), 'project_name': pname, 'amount': r['Amount']})
                found_match = True
                break

# remove duplicates by funding_id
seen = set()
unique_included = []
for it in included:
    fid = it['funding_id']
    if fid not in seen:
        seen.add(fid)
        unique_included.append(it)

total = sum(it['amount'] for it in unique_included)

output = {
    'total_funding': total,
    'projects_count': len(unique_included),
    'projects': unique_included
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_Rzijr1ISlDUOM9pATv8LIjjx': 'file_storage/call_Rzijr1ISlDUOM9pATv8LIjjx.json', 'var_call_Ux2JQYUAZi3uGCxmtmShczUi': 'file_storage/call_Ux2JQYUAZi3uGCxmtmShczUi.json'}

exec(code, env_args)
