code = """import json

# Load stored JSON files
with open(var_call_90dmcYwBxTb7vQatqrbc7U4G, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_7E8sUjkgBqwcx0vACQAqhl9z, 'r') as f:
    funding = json.load(f)

# Prepare lower-cased civic doc texts
lower_texts = [doc.get('text','').lower() for doc in civic_docs]

# Disaster keywords
disaster_kw = ['fema', 'caloes', 'caljpia', 'fire', 'disaster', 'woolsey', 'recovery']

total = 0
matched = {}

for rec in funding:
    pname = rec.get('Project_Name','')
    if not pname:
        continue
    try:
        amt = int(float(rec.get('Amount', 0)))
    except:
        amt = 0
    pname_low = pname.lower()
    matched_flag = False
    # Check if project name appears in any civic doc that also contains '2022' and disaster keywords either in name or in doc
    for doc_text in lower_texts:
        if '2022' in doc_text and pname_low in doc_text:
            if any(d in pname_low for d in disaster_kw) or any(d in doc_text for d in disaster_kw):
                matched_flag = True
                break
    # If not matched yet, but project name itself contains disaster keyword and any civic doc mentions 2022, match it
    if not matched_flag and any(d in pname_low for d in disaster_kw):
        if any('2022' in dt for dt in lower_texts):
            matched_flag = True
    if matched_flag:
        total += amt
        matched[pname] = amt

result = {'total_funding': total, 'matched_projects': matched}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_FbCAMFAZTL2Ih3VWgvwFzEcF': ['civic_docs'], 'var_call_90dmcYwBxTb7vQatqrbc7U4G': 'file_storage/call_90dmcYwBxTb7vQatqrbc7U4G.json', 'var_call_aId1Wornd25qzPfcbmiNPMM9': ['Funding'], 'var_call_7E8sUjkgBqwcx0vACQAqhl9z': 'file_storage/call_7E8sUjkgBqwcx0vACQAqhl9z.json'}

exec(code, env_args)
