code = """import json

# Load data from storage file paths provided by previous tool calls
with open(var_call_lzuql9XO4mip4vcz5jSfIR6d, 'r') as f:
    funding_data = json.load(f)

with open(var_call_OTWLMZF2U2vjKkDgiSiAfRbv, 'r') as f:
    civic_docs = json.load(f)

# Combine civic doc texts
civic_texts = [doc.get('text','').lower() for doc in civic_docs]
combined_text = "\n".join(civic_texts)

# Helper to normalize project name by removing parenthetical suffixes and whitespace
def normalize_name_simple(name):
    if not name:
        return ''
    return name.split('(')[0].strip().lower()

keywords = ['fema', 'emergency', 'outdoor warning', 'sirens', 'backup power', 'disaster']

results = []
seen = set()
for row in funding_data:
    pname = row.get('Project_Name','')
    psource = row.get('Funding_Source','')
    amount_raw = row.get('Amount')
    try:
        amount = int(amount_raw)
    except:
        try:
            amount = int(float(amount_raw))
        except:
            amount = None

    pname_norm = normalize_name_simple(pname)
    lname = pname.lower()

    related = False
    # If project name contains keyword
    for kw in keywords:
        if kw in lname:
            related = True
            break
    # Or if normalized project name appears in any civic doc that contains emergency/FEMA
    if not related and pname_norm:
        for t in civic_texts:
            if pname_norm in t:
                related = True
                break

    if not related:
        continue

    # Determine status from civic docs where the project is mentioned
    status = None
    for t in civic_texts:
        if pname_norm in t or pname.lower() in t:
            # look for completed
            if 'construction was completed' in t or 'notice of completion' in t or 'complete construction' in t or 'completed' in t:
                status = 'completed'
                break
            # design/active
            if 'design' in t or 'complete design' in t or 'preliminary design' in t or 'working with the consultant' in t or 'finalize the design' in t or 'advertise' in t or 'begin construction' in t or 'awaiting final fema' in t or 'awaiting final caloes' in t or 'awaiting final' in t or 'awaiting' in t:
                status = 'design'
                break
            # not started
            if 'not started' in t or 'identified' in t or 'waiting for the agreement' in t or 'waiting for agreement' in t or 'will be issuing a rfq' in t or 'schedule for council' in t:
                status = 'not started'
                break
    # fallback inference
    if status is None:
        if any(kw in lname for kw in keywords):
            status = 'design'

    if pname not in seen:
        seen.add(pname)
        results.append({'Project_Name': pname, 'Funding_Source': psource, 'Amount': amount, 'Status': status})

import json
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_OTWLMZF2U2vjKkDgiSiAfRbv': 'file_storage/call_OTWLMZF2U2vjKkDgiSiAfRbv.json', 'var_call_lzuql9XO4mip4vcz5jSfIR6d': 'file_storage/call_lzuql9XO4mip4vcz5jSfIR6d.json'}

exec(code, env_args)
