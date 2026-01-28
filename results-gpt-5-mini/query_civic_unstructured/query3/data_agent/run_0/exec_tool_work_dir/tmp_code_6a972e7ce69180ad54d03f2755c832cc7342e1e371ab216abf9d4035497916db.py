code = """import json
fema = var_call_MbOJriWAo1Uq2qwdRFaqxT9f
civic = var_call_RDTPadJ0MEdOGRSFv71OoRd6
# load civic docs if it's a file path
if isinstance(civic, str):
    with open(civic, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic
# load fema funding if file path
if isinstance(fema, str):
    with open(fema, 'r') as f:
        fema_funding = json.load(f)
else:
    fema_funding = fema

all_text = ''
for d in civic_docs:
    all_text += d.get('text', '') + ' '
all_text_l = all_text.lower()

def status(name):
    n = (name or '').lower()
    base = n.split('(')[0].strip()
    idx = all_text_l.find(n)
    if idx == -1 and base:
        idx = all_text_l.find(base)
    if idx == -1:
        return 'Unknown'
    window = all_text_l[max(0, idx-300): idx+300]
    if any(k in window for k in ['preliminary design', 'complete design', 'final design', 'in the preliminary design phase']):
        return 'Design'
    if any(k in window for k in ['complete construction', 'construction was completed', 'notice of completion', 'was completed']):
        return 'Completed'
    if any(k in window for k in ['not started', 'identified but not begun', 'not begun']):
        return 'Not Started'
    if any(k in window for k in ['begin construction', 'begin construction:', 'currently under construction']):
        return 'Construction'
    # check nearby headers
    pre = all_text_l[max(0, idx-1000): idx]
    if 'capital improvement projects' in pre:
        seg = pre.split('capital improvement projects')[-1][:200]
        if 'design' in seg:
            return 'Design'
        if 'construction' in seg:
            return 'Construction'
        if 'not started' in seg:
            return 'Not Started'
    return 'Unknown'

output = []
for r in fema_funding:
    pname = r.get('Project_Name')
    psource = r.get('Funding_Source')
    amount_raw = r.get('Amount')
    try:
        amount = int(amount_raw)
    except:
        amount = amount_raw
    st = status(pname)
    output.append({'Project_Name': pname, 'Funding_Source': psource, 'Amount': amount, 'Status': st})

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_RDTPadJ0MEdOGRSFv71OoRd6': 'file_storage/call_RDTPadJ0MEdOGRSFv71OoRd6.json', 'var_call_HpgQvXmAaa9rS2LPuJKiZVjk': ['Funding'], 'var_call_O8fNiGy0hYX2JWmSnRw9hiIg': 'file_storage/call_O8fNiGy0hYX2JWmSnRw9hiIg.json', 'var_call_MbOJriWAo1Uq2qwdRFaqxT9f': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
