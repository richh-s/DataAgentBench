code = """import json, re, pandas as pd

funding = pd.DataFrame(var_call_F4MSCWxgcIMn6rsfHEkklhvr)
# normalize types
funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

# load mongo docs (may be file path)
raw_docs = var_call_Sg9ckPEwuOmOYfOX3nlJ6ufv
if isinstance(raw_docs, str):
    with open(raw_docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = raw_docs

# Extract project statuses from docs for FEMA/emergency related lines
status_map = {}
for d in docs:
    text = d.get('text','')
    # focus around disaster recovery section
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if not ln:
            continue
        # candidate project line (title-ish)
        if re.search(r'\bFEMA\b', ln, flags=re.I) or re.search(r'emergency', ln, flags=re.I):
            # Clean title
            title = re.sub(r'^[\-\u2022\(\)\[\]cid:;,. ]+', '', ln).strip()
            # Look ahead for Updates / status info within next 8 lines
            window = " ".join(lines[i:i+10])
            st = None
            if re.search(r'completed', window, flags=re.I):
                st = 'completed'
            elif re.search(r'not started', window, flags=re.I):
                st = 'not started'
            elif re.search(r'under construction|currently under construction|begin construction|construction', window, flags=re.I):
                # not in provided status taxonomy; map to design unless completed
                st = 'design'
            elif re.search(r'design|finalize plans|plans.*completed|awaiting.*approval|under review', window, flags=re.I):
                st = 'design'
            # store if found
            if st:
                status_map[title] = st

# helper to find best status match for project name
keys = list(status_map.keys())

def best_status(pname):
    # direct contains match ignoring case
    p = pname.lower()
    for k in keys:
        if k.lower() in p or p in k.lower():
            return status_map[k]
    # token overlap heuristic
    ptoks = set(re.findall(r'[a-z0-9]+', p))
    best = (0,None)
    for k in keys:
        ktoks = set(re.findall(r'[a-z0-9]+', k.lower()))
        score = len(ptoks & ktoks)
        if score > best[0] and score >= 3:
            best = (score, status_map[k])
    return best[1]

funding['Status'] = funding['Project_Name'].apply(best_status)

# also treat all as FEMA/emergency related already filtered
funding = funding[['Project_Name','Funding_Source','Amount','Status']].sort_values(['Project_Name','Funding_Source']).reset_index(drop=True)

result = funding.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_F4MSCWxgcIMn6rsfHEkklhvr': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_Sg9ckPEwuOmOYfOX3nlJ6ufv': 'file_storage/call_Sg9ckPEwuOmOYfOX3nlJ6ufv.json'}

exec(code, env_args)
