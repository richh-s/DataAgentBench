code = """import json, re

# Load funding query result variable
fund_var = var_call_PLDT1vX07qomWdThkFZjCF7F
civic_var = var_call_OTWLMZF2U2vjKkDgiSiAfRbv

# fund_var may be list or a filepath string
if isinstance(fund_var, str):
    with open(fund_var, 'r') as f:
        funding = json.load(f)
else:
    funding = fund_var

# civic_var may be filepath
if isinstance(civic_var, str):
    with open(civic_var, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_var

civic_texts = [d.get('text','').lower() for d in civic_docs]
combined = '\n'.join(civic_texts)

# indicators
completed_inds = ['construction was completed', 'notice of completion', 'complete construction', 'completed', 'completion filed', 'filed', 'complete construction:']
design_inds = ['design', 'complete design', 'preliminary design', 'working with the consultant', 'finalize the design', 'advertise', 'begin construction', 'begin construction:', 'awaiting final fema', 'awaiting final caloes', 'awaiting final', 'awaiting approval', 'awaiting']
not_started_inds = ['not started', 'identified', 'waiting for the agreement', 'waiting for agreement', 'will be issuing a rfq', 'schedule for council', 'to be discussed', 'waiting for the agreement']

def normalize(name):
    n = re.sub(r"\(.*?\)", "", name)
    return re.sub(r"\s+", " ", n).strip().lower()

results = []
seen = set()
for row in funding:
    pname = row.get('Project_Name','')
    psource = row.get('Funding_Source')
    amount_raw = row.get('Amount')
    try:
        amount = int(amount_raw)
    except:
        try:
            amount = int(float(amount_raw))
        except:
            amount = None

    pname_norm = normalize(pname)
    pname_low = (pname or '').lower()

    # Determine status by scanning civic texts
    status = None
    found = False
    for t in civic_texts:
        if pname_norm and pname_norm in t or pname_low and pname_low in t:
            found = True
            idx = t.find(pname_norm) if pname_norm in t else t.find(pname_low)
            if idx == -1:
                idx = 0
            start = max(0, idx-250)
            end = min(len(t), idx+250)
            window = t[start:end]
            # check completed
            if any(ci in window for ci in completed_inds):
                status = 'completed'
                break
            if any(ni in window for ni in not_started_inds):
                status = 'not started'
                break
            if any(di in window for di in design_inds):
                status = 'design'
                break
    # Fallbacks
    if not found:
        # if project name explicitly mentions fema/emergency/sirens/outdoor warning -> likely design
        if any(k in pname_low for k in ['fema','emergency','outdoor warning','sirens','warning']):
            status = 'design'
        else:
            status = None

    if pname not in seen:
        seen.add(pname)
        results.append({'Project_Name': pname, 'Funding_Source': psource, 'Amount': amount, 'Status': status})

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_OTWLMZF2U2vjKkDgiSiAfRbv': 'file_storage/call_OTWLMZF2U2vjKkDgiSiAfRbv.json', 'var_call_lzuql9XO4mip4vcz5jSfIR6d': 'file_storage/call_lzuql9XO4mip4vcz5jSfIR6d.json', 'var_call_kpbSuqMp0pn6b3LPb8E1hlgz': {'var1_type': 'str', 'var2_type': 'str'}, 'var_call_IYe14sR0kxs7mSnFvSfNNoBv': {'funding_count': 500, 'civic_docs_count': 5}, 'var_call_PLDT1vX07qomWdThkFZjCF7F': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Signs', 'Funding_Source': 'Urban Renewal Fund', 'Amount': '92000'}, {'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': '28000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
