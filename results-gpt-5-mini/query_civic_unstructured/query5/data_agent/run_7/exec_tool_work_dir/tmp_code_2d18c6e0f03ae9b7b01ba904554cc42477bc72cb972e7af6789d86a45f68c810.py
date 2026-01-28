code = """import json, re

# Load data from storage-provided file paths
with open(var_call_q7R3xqp8WG9IOZBRlFr8pyIy, 'r') as f:
    funding = json.load(f)
with open(var_call_QzBZclHwTrrUNkhyo5VjgzV8, 'r') as f:
    civic_docs = json.load(f)

# Combine civic texts
all_text = "\n".join([d.get('text','') for d in civic_docs])
all_text_lower = all_text.lower()

# Disaster identifying keywords
disaster_keywords = re.compile(r"fema|caloes|caljpia|disaster|fire|flood|emergency", re.I)
# Other disaster-related project topic words
disaster_topics = re.compile(r"culvert|slope repair|slope repairs|road repair|road repairs|retaining wall|storm drain|drainage|bridge|water quality|flood|stabilization", re.I)

# Helper to get base name before any parenthesis
def base_name(name):
    return re.split(r"\(|-", name)[0].strip()

results = []
for rec in funding:
    pname = rec.get('Project_Name','')
    pname_lower = pname.lower()
    bname = base_name(pname).lower()
    is_disaster_name = bool(disaster_keywords.search(pname))
    is_disaster_topic = bool(disaster_topics.search(pname))

    # consider candidate if name suggests disaster or topic suggests disaster
    if not (is_disaster_name or is_disaster_topic):
        continue

    # search for pname or base name in civic docs
    idx = -1
    if pname_lower and pname_lower in all_text_lower:
        idx = all_text_lower.find(pname_lower)
    elif bname and bname in all_text_lower:
        idx = all_text_lower.find(bname)
    else:
        # try multi-token matches
        tokens = re.findall(r"[a-z]{4,}", bname)
        for i in range(len(tokens)-1):
            seq = tokens[i] + ' ' + tokens[i+1]
            pos = all_text_lower.find(seq)
            if pos != -1:
                idx = pos
                break

    year2022_nearby = False
    if idx != -1:
        start = max(0, idx-400)
        end = min(len(all_text_lower), idx+400)
        context = all_text_lower[start:end]
        if '2022' in context:
            year2022_nearby = True
        else:
            # also look for phrases indicating start in 2022 like 'begin construction: 2022' or 'advertise: fall 2022'
            if re.search(r"begin (construction|construction:)[:\s].{0,30}2022", context) or re.search(r"begin construction[:\s].{0,30}2022", context):
                year2022_nearby = True
            if re.search(r"advertise[:\s].{0,30}2022", context):
                year2022_nearby = True
            if re.search(r"complete (design|construction).{0,40}2022", context):
                year2022_nearby = True

    results.append({'Project_Name': pname, 'Amount': rec.get('Amount'), 'matched_in_docs': idx!=-1, 'year2022_nearby': year2022_nearby})

# Sum amounts for those with year2022_nearby True
total = 0
included = []
for r in results:
    if r['year2022_nearby']:
        amt_raw = r['Amount']
        try:
            amt = int(amt_raw)
        except:
            amt = int(re.sub(r"[^0-9]","", str(amt_raw) or '0') or 0)
        total += amt
        included.append({'Project_Name': r['Project_Name'], 'Amount': amt})

output = {'total_funding_disaster_projects_started_2022': total, 'included_funding_records': included}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_xHNly7z1Fzv5N8jwdK3mtrAL': ['civic_docs'], 'var_call_jRI4KvDQihFoo9gBTqySXjRT': ['Funding'], 'var_call_q7R3xqp8WG9IOZBRlFr8pyIy': 'file_storage/call_q7R3xqp8WG9IOZBRlFr8pyIy.json', 'var_call_QzBZclHwTrrUNkhyo5VjgzV8': 'file_storage/call_QzBZclHwTrrUNkhyo5VjgzV8.json', 'var_call_eSiYVBrswLWMKVR6Vv4seVf5': {'vars': ['var_call_xHNly7z1Fzv5N8jwdK3mtrAL', 'var_call_jRI4KvDQihFoo9gBTqySXjRT', 'var_call_q7R3xqp8WG9IOZBRlFr8pyIy', 'var_call_QzBZclHwTrrUNkhyo5VjgzV8']}}

exec(code, env_args)
