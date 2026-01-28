code = """import json
# Load files
with open(var_call_eY6MrH3yMduMhdp7Od4wxifW, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_mfhhNhnlDRowwEHz4PEUqpDB, 'r') as f:
    funding = json.load(f)

# normalize amounts
for rec in funding:
    try:
        rec['Amount'] = int(rec.get('Amount') if rec.get('Amount') is not None else 0)
    except:
        s = ''.join(ch for ch in str(rec.get('Amount','')) if ch.isdigit())
        rec['Amount'] = int(s) if s else 0

funding_by_name = {}
for rec in funding:
    name = rec.get('Project_Name','').strip()
    if name:
        funding_by_name[name] = funding_by_name.get(name, 0) + rec.get('Amount', 0)

spring_terms = [
    'spring 2022','2022-spring','2022-march','2022-april','2022-may',
    'march 2022','april 2022','may 2022','2022-03','2022-04','2022-05'
]
start_words = ['begin','begin construction','advertise','start','started','starting','estimated schedule','project schedule','complete design']

matched = set()

for pname, amount in funding_by_name.items():
    pname_lower = pname.lower()
    for doc in civic_docs:
        text = doc.get('text','')
        text_lower = text.lower()
        idx = text_lower.find(pname_lower)
        if idx == -1:
            continue
        # consider multiple occurrences
        found_flag = False
        start = 0
        while True:
            idx = text_lower.find(pname_lower, start)
            if idx == -1:
                break
            window = text_lower[max(0, idx-200): idx+len(pname_lower)+200]
            # check for spring terms
            if any(term in window for term in spring_terms):
                # optionally check for start words
                if any(sw in window for sw in start_words):
                    matched.add(pname)
                    found_flag = True
                    break
                else:
                    # still include if spring term present near
                    matched.add(pname)
                    found_flag = True
                    break
            start = idx + 1
        if found_flag:
            break

matched_list = sorted(list(matched))
count = len(matched_list)
total = sum(funding_by_name.get(n,0) for n in matched_list)

result = {'count': count, 'total_funding': total, 'projects': matched_list}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NxzWWT5KvvxnzaNw09EloWJH': ['civic_docs'], 'var_call_zdTWCxg3xHrmDB2Vw93UB0ER': ['Funding'], 'var_call_kiS82EWlxpy6moSmreVncFDG': [], 'var_call_eY6MrH3yMduMhdp7Od4wxifW': 'file_storage/call_eY6MrH3yMduMhdp7Od4wxifW.json', 'var_call_mfhhNhnlDRowwEHz4PEUqpDB': 'file_storage/call_mfhhNhnlDRowwEHz4PEUqpDB.json'}

exec(code, env_args)
