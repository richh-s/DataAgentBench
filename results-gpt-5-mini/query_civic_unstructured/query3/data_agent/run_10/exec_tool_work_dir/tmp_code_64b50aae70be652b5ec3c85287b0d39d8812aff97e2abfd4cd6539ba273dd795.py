code = """import json, re

# Load files from storage variables
with open(var_call_lzuql9XO4mip4vcz5jSfIR6d, 'r') as f:
    funding_data = json.load(f)
with open(var_call_OTWLMZF2U2vjKkDgiSiAfRbv, 'r') as f:
    civic_docs = json.load(f)

civic_texts = [doc.get('text','').lower() for doc in civic_docs]
combined_text = "\n".join(civic_texts)

def normalize_name(name):
    if not name:
        return ''
    # remove parenthetical parts and non-alphanumeric sequences at ends
    n = re.sub(r"\(.*?\)", "", name)
    return re.sub(r"\s+", " ", n).strip().lower()

key_terms = ['fema', 'emergency', 'outdoor warning', 'sirens', 'backup power', 'disaster']

results = []
seen = set()
for row in funding_data:
    pname = row.get('Project_Name','')
    psource = row.get('Funding_Source','')
    amt_raw = row.get('Amount')
    try:
        amount = int(amt_raw)
    except:
        try:
            amount = int(float(amt_raw))
        except:
            amount = None

    pname_lower = (pname or '').lower()
    pname_norm = normalize_name(pname)

    related = False
    for kt in key_terms:
        if kt in pname_lower:
            related = True
            break
    if not related and pname_norm:
        for t in civic_texts:
            if pname_norm in t:
                related = True
                break
    if not related:
        continue

    # determine status
    status = None
    for t in civic_texts:
        if (pname_norm and pname_norm in t) or (pname_lower and pname_lower in t):
            # find index
            idx = t.find(pname_norm) if pname_norm in t else t.find(pname_lower)
            if idx == -1:
                idx = 0
            start = max(0, idx-250)
            end = min(len(t), idx+250)
            window = t[start:end]
            # completed indicators
            completed_indicators = ['construction was completed', 'notice of completion', 'complete construction', 'completed', 'completion filed', 'filed']
            if any(ci in window for ci in completed_indicators):
                status = 'completed'
                break
            design_indicators = ['design', 'complete design', 'preliminary design', 'working with the consultant', 'finalize the design', 'advertise', 'begin construction', 'awaiting final fema', 'awaiting final caloes', 'awaiting final', 'awaiting approval']
            if any(di in window for di in design_indicators):
                status = 'design'
                break
            not_started_indicators = ['not started', 'identified', 'waiting for the agreement', 'waiting for agreement', 'will be issuing a rfq', 'schedule for council', 'to be discussed']
            if any(ni in window for ni in not_started_indicators):
                status = 'not started'
                break
    if status is None:
        if 'fema' in pname_lower or 'emergency' in pname_lower or 'awaiting' in combined_text:
            status = 'design'

    if pname not in seen:
        seen.add(pname)
        results.append({'Project_Name': pname, 'Funding_Source': psource, 'Amount': amount, 'Status': status})

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_OTWLMZF2U2vjKkDgiSiAfRbv': 'file_storage/call_OTWLMZF2U2vjKkDgiSiAfRbv.json', 'var_call_lzuql9XO4mip4vcz5jSfIR6d': 'file_storage/call_lzuql9XO4mip4vcz5jSfIR6d.json', 'var_call_kpbSuqMp0pn6b3LPb8E1hlgz': {'var1_type': 'str', 'var2_type': 'str'}, 'var_call_IYe14sR0kxs7mSnFvSfNNoBv': {'funding_count': 500, 'civic_docs_count': 5}}

exec(code, env_args)
