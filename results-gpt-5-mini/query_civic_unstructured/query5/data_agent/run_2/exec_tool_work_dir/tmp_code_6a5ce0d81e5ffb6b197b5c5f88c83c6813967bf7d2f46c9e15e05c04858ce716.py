code = """import json, re

# Load data from storage file paths
with open(var_call_XTpGdeOUqBGKrql77n109P0x, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_8iO6IE1pAFY52osRikfHN8xI, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Build funding map: project name -> total amount
funding_map = {}
for rec in funding:
    name = rec.get('Project_Name')
    amt = rec.get('Amount')
    try:
        amt_int = int(amt)
    except:
        try:
            amt_int = int(float(amt))
        except:
            amt_int = 0
    if name in funding_map:
        funding_map[name] += amt_int
    else:
        funding_map[name] = amt_int

# Disaster-identifying tokens
disaster_tokens = ['fema', 'caloes', 'caljpia', 'fema/caloes', 'fema/caloes', 'calo es', 'disaster', 'fire', 'woolsey']

matched_projects = []

for proj_name, amount in funding_map.items():
    name_lower = proj_name.lower()
    is_disaster = any(tok in name_lower for tok in disaster_tokens)
    found_2022 = False

    # Search across civic documents for project name occurrences and nearby '2022'
    for doc in civic_docs:
        text = doc.get('text','')
        text_lower = text.lower()
        # find occurrences of project name
        idx = text_lower.find(name_lower)
        while idx != -1:
            # define window around occurrence
            start = max(0, idx-300)
            end = min(len(text_lower), idx+800)
            window = text_lower[start:end]
            if '2022' in window:
                found_2022 = True
            idx = text_lower.find(name_lower, idx+1)
        # check Disaster Recovery header context
        hdr_idx = text_lower.find('disaster recovery')
        if hdr_idx != -1:
            # look for project name within next 2000 chars of header
            if text_lower.find(name_lower, hdr_idx, hdr_idx+2000) != -1:
                is_disaster = True
                # check for 2022 near that occurrence
                idx2 = text_lower.find(name_lower, hdr_idx, hdr_idx+2000)
                if idx2 != -1:
                    start = max(0, idx2-300)
                    end = min(len(text_lower), idx2+800)
                    if '2022' in text_lower[start:end]:
                        found_2022 = True

    # Also, sometimes project names in funding table are similar but with slight variations
    # Try fuzzy-ish matching: check if key words from proj_name appear in civic text with 2022
    if not found_2022:
        # break proj_name into tokens of length>=4
        tokens = [t for t in re.split(r'[^a-z0-9]+', name_lower) if len(t)>=4]
        if tokens:
            for doc in civic_docs:
                txt = doc.get('text','').lower()
                # require all tokens to be present within 200 chars window
                for m in re.finditer(tokens[0], txt):
                    idx = m.start()
                    window = txt[max(0, idx-200): idx+1200]
                    if all(tok in window for tok in tokens[:3]):
                        if '2022' in window:
                            found_2022 = True
                        # if header indicates disaster
                        if 'disaster recovery' in txt[max(0, idx-500): idx+2000]:
                            is_disaster = True
                        if found_2022:
                            break
                if found_2022:
                    break

    if is_disaster and found_2022:
        matched_projects.append({'Project_Name': proj_name, 'Amount': amount})

# Sum amounts
total = sum(p['Amount'] for p in matched_projects)

# Prepare result
result = {
    'total_funding': total,
    'projects': matched_projects
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_XTpGdeOUqBGKrql77n109P0x': 'file_storage/call_XTpGdeOUqBGKrql77n109P0x.json', 'var_call_8iO6IE1pAFY52osRikfHN8xI': 'file_storage/call_8iO6IE1pAFY52osRikfHN8xI.json'}

exec(code, env_args)
