code = """import json

funding_path = var_call_q7R3xqp8WG9IOZBRlFr8pyIy
civic_path = var_call_QzBZclHwTrrUNkhyo5VjgzV8

with open(funding_path, 'r') as f:
    funding = json.load(f)
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# combine civic texts
newline = chr(10)
all_text = newline.join([d.get('text','') for d in civic_docs])
all_text_lower = all_text.lower()

# keywords
disaster_keywords = ['fema', 'caloes', 'caljpia', 'disaster', 'fire', 'flood', 'emergency']
disaster_topics = ['culvert', 'slope repair', 'slope repairs', 'road repair', 'road repairs', 'retaining wall', 'storm drain', 'drainage', 'bridge', 'water quality', 'stabilization']

# helper to get base name
def base_name(name):
    if '(' in name:
        return name.split('(')[0].strip()
    if '-' in name:
        return name.split('-')[0].strip()
    return name.strip()

results = []
for rec in funding:
    pname = rec.get('Project_Name','')
    pname_lower = pname.lower()
    bname = base_name(pname).lower()

    is_disaster_name = any(k in pname_lower for k in disaster_keywords)
    is_disaster_topic = any(t in pname_lower for t in disaster_topics)
    if not (is_disaster_name or is_disaster_topic):
        continue

    idx = -1
    if pname_lower and pname_lower in all_text_lower:
        idx = all_text_lower.find(pname_lower)
    elif bname and bname in all_text_lower:
        idx = all_text_lower.find(bname)
    else:
        # try consecutive word pairs from base name
        tokens = [tok for tok in bname.split() if len(tok) >= 4]
        for i in range(len(tokens)-1):
            seq = tokens[i] + ' ' + tokens[i+1]
            pos = all_text_lower.find(seq)
            if pos != -1:
                idx = pos
                break

    year2022_nearby = False
    if idx != -1:
        start = idx - 400
        if start < 0:
            start = 0
        end = idx + 400
        if end > len(all_text_lower):
            end = len(all_text_lower)
        context = all_text_lower[start:end]
        if '2022' in context:
            year2022_nearby = True
        else:
            # broader check
            start = idx - 1000
            if start < 0:
                start = 0
            end = idx + 1000
            if end > len(all_text_lower):
                end = len(all_text_lower)
            broader = all_text_lower[start:end]
            if '2022' in broader:
                year2022_nearby = True

    results.append({'Project_Name': rec.get('Project_Name'), 'Amount': rec.get('Amount'), 'matched_in_docs': idx != -1, 'year2022_nearby': year2022_nearby})

# sum amounts
total = 0
included = []
for r in results:
    if r['year2022_nearby']:
        amt_raw = r['Amount']
        s = ''.join(ch for ch in str(amt_raw) if ch.isdigit())
        amt = int(s) if s else 0
        total += amt
        included.append({'Project_Name': r['Project_Name'], 'Amount': amt})

output = {'total_funding_disaster_projects_started_2022': total, 'included_funding_records': included}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_xHNly7z1Fzv5N8jwdK3mtrAL': ['civic_docs'], 'var_call_jRI4KvDQihFoo9gBTqySXjRT': ['Funding'], 'var_call_q7R3xqp8WG9IOZBRlFr8pyIy': 'file_storage/call_q7R3xqp8WG9IOZBRlFr8pyIy.json', 'var_call_QzBZclHwTrrUNkhyo5VjgzV8': 'file_storage/call_QzBZclHwTrrUNkhyo5VjgzV8.json', 'var_call_eSiYVBrswLWMKVR6Vv4seVf5': {'vars': ['var_call_xHNly7z1Fzv5N8jwdK3mtrAL', 'var_call_jRI4KvDQihFoo9gBTqySXjRT', 'var_call_q7R3xqp8WG9IOZBRlFr8pyIy', 'var_call_QzBZclHwTrrUNkhyo5VjgzV8']}, 'var_call_SmkVtQCSHHMolSQcfBMKrf7e': {'funding_path': 'file_storage/call_q7R3xqp8WG9IOZBRlFr8pyIy.json', 'civic_path': 'file_storage/call_QzBZclHwTrrUNkhyo5VjgzV8.json'}, 'var_call_O0KMI5glxdNFxekcr8fnrOpf': {'funding_count': 500, 'civic_docs_count': 19}}

exec(code, env_args)
