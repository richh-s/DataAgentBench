code = """import json

# Load storage files
with open(var_call_xYjxDFVtmV0T7uhUW6fn1MPb, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_saf1zSumCBClpwwtOFQoyZwV, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# disaster indicators
disaster_indicators = ['fema', 'caloes', 'caljpia', 'fema/caloes', 'fire', 'disaster', 'emergency', 'flood']

def is_disaster_name(name):
    if not name:
        return False
    ln = name.lower()
    for kw in disaster_indicators:
        if kw in ln:
            return True
    return False

# normalize document texts
doc_texts = [doc.get('text','').lower() for doc in civic_docs]

total = 0
matched = []

for rec in funding_rows:
    name = rec.get('Project_Name','')
    name_l = name.lower() if name else ''
    try:
        amount = int(rec.get('Amount', 0))
    except:
        try:
            amount = int(float(rec.get('Amount',0)))
        except:
            amount = 0

    disaster_flag = is_disaster_name(name)
    started_2022 = '2022' in name_l

    # If not started flag, search civic docs for occurrence of name and 2022
    if not started_2022 and name_l:
        for dt in doc_texts:
            if name_l in dt and '2022' in dt:
                started_2022 = True
                break
    # If name not found, try token-based presence: require two meaningful tokens appear in same doc and '2022' present
    if not started_2022 and name_l:
        tokens = [t for t in ''.join(ch if ch.isalnum() else ' ' for ch in name_l).split() if len(t)>=4]
        if len(tokens) >= 2:
            for dt in doc_texts:
                if '2022' in dt and all(tok in dt for tok in tokens[:3]):
                    started_2022 = True
                    break
    # If not disaster by name, check civic doc context for disaster keywords near the name occurrence
    if not disaster_flag and name_l:
        for dt in doc_texts:
            if name_l in dt:
                # check window around first occurrence
                idx = dt.find(name_l)
                start = max(0, idx-200)
                end = min(len(dt), idx+200)
                snippet = dt[start:end]
                if any(kw in snippet for kw in disaster_indicators):
                    disaster_flag = True
                    break
    # Also, if project appears in a document that contains 'disaster recovery' and '2022', consider it disaster-started-2022
    if not disaster_flag or not started_2022:
        for dt in doc_texts:
            if 'disaster recovery' in dt and '2022' in dt:
                # if project name appears in same doc, mark both
                if name_l and name_l in dt:
                    disaster_flag = True
                    started_2022 = True
                    break

    if disaster_flag and started_2022:
        total += amount
        matched.append({'Project_Name': name, 'Amount': amount})

result = {'total_disaster_funding_started_2022': total, 'matched_records': matched}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_5UWQMcOPol6UzCwliXq5ldyo': ['civic_docs'], 'var_call_9NLdNOA90UOg67wMOYnq3dvj': ['Funding'], 'var_call_xYjxDFVtmV0T7uhUW6fn1MPb': 'file_storage/call_xYjxDFVtmV0T7uhUW6fn1MPb.json', 'var_call_saf1zSumCBClpwwtOFQoyZwV': 'file_storage/call_saf1zSumCBClpwwtOFQoyZwV.json'}

exec(code, env_args)
