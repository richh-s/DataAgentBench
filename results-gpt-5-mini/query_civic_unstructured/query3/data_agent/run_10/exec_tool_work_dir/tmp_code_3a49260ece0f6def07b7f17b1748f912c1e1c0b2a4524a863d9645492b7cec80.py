code = """import json

# Load data from storage file paths provided by previous tool calls
with open(var_call_lzuql9XO4mip4vcz5jSfIR6d, 'r') as f:
    funding_data = json.load(f)

with open(var_call_OTWLMZF2U2vjKkDgiSiAfRbv, 'r') as f:
    civic_docs = json.load(f)

# Prepare civic texts (these docs were pre-filtered for emergency/FEMA)
civic_texts = [doc.get('text','').lower() for doc in civic_docs]
combined_text = "\n".join(civic_texts)

# Helper to normalize project name by removing parenthetical suffixes and whitespace
def normalize_name(name):
    if not name:
        return ''
    return name.split('(')[0].strip().lower()

# Keywords indicating emergency/FEMA relevance
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

    pname_lower = pname.lower()
    pname_norm = normalize_name(pname)

    related = False
    # If project name contains any key term
    for kt in key_terms:
        if kt in pname_lower:
            related = True
            break
    # Or if the normalized project name appears in any civic doc (these docs are emergency-filtered)
    if not related and pname_norm:
        for t in civic_texts:
            if pname_norm in t:
                related = True
                break

    if not related:
        continue

    # Determine status by searching civic docs for mentions and context
    status = None
    for t in civic_texts:
        if pname_norm in t or pname_lower in t:
            # extract a window around first occurrence
            idx = t.find(pname_norm) if pname_norm in t else t.find(pname_lower)
            start = max(0, idx - 200)
            end = min(len(t), idx + 200)
            window = t[start:end]
            # completed indicators
            if any(kw in window for kw in ['construction was completed', 'notice of completion', 'complete construction', 'completed', 'construction was completed']):
                status = 'completed'
                break
            # design/active indicators
            if any(kw in window for kw in ['design', 'complete design', 'preliminary design', 'working with the consultant', 'finalize the design', 'advertise', 'begin construction', 'awaiting final fema', 'awaiting final caloes', 'awaiting final']):
                status = 'design'
                break
            # not started indicators
            if any(kw in window for kw in ['not started', 'identified', 'waiting for the agreement', 'waiting for agreement', 'will be issuing a rfq', 'schedule for council', 'to be discussed']):
                status = 'not started'
                break
    # fallback
    if status is None:
        # if project name has FEMA, assume design unless doc says completed
        if 'fema' in pname_lower or 'emergency' in pname_lower:
            status = 'design'
        else:
            status = None

    if pname not in seen:
        seen.add(pname)
        results.append({'Project_Name': pname, 'Funding_Source': psource, 'Amount': amount, 'Status': status})

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_OTWLMZF2U2vjKkDgiSiAfRbv': 'file_storage/call_OTWLMZF2U2vjKkDgiSiAfRbv.json', 'var_call_lzuql9XO4mip4vcz5jSfIR6d': 'file_storage/call_lzuql9XO4mip4vcz5jSfIR6d.json', 'var_call_kpbSuqMp0pn6b3LPb8E1hlgz': {'var1_type': 'str', 'var2_type': 'str'}}

exec(code, env_args)
