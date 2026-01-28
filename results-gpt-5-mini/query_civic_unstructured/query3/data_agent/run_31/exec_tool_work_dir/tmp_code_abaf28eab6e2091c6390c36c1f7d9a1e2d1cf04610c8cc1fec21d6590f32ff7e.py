code = """import json
from pathlib import Path
import re

# Load funding results
fund_var = var_call_c1pff0BCcHaDhyZixHzlsOJW
if isinstance(fund_var, str):
    p = Path(fund_var)
    with p.open('r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = fund_var

# Load civic docs results
docs_var = var_call_uegX5YtT5sjI2pkA0DpZVoVm
if isinstance(docs_var, str):
    p = Path(docs_var)
    with p.open('r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_var

# prepare keywords
design_kw = [r'complete design', r'final design', r'preliminary design', r'design phase', r'design will', r'submit to the county for review', r'staff is working with the consultant to finalize the design']
construction_kw = [r'begin construction', r'begin construction:', r'construction was completed', r'complete construction', r'under construction', r'begin construction', r'complete construction:', r'notice of completion', r'award the contract']
not_started_kw = [r'not started', r'identified but not begun', r'project was identified', r'project description']

results = []

for rec in funding:
    pname = rec.get('Project_Name')
    source = rec.get('Funding_Source')
    amount = rec.get('Amount')
    status_found = None
    pname_esc = re.escape(pname)
    # search in each doc
    for doc in docs:
        text = doc.get('text','')
        # case-insensitive search
        for m in re.finditer(re.compile(pname_esc, re.IGNORECASE), text):
            start = max(0, m.start()-300)
            end = min(len(text), m.end()+300)
            window = text[start:end].lower()
            # check design
            matched = False
            for kw in design_kw:
                if re.search(kw, window):
                    status_found = 'design'
                    matched = True
                    break
            if matched:
                break
            for kw in construction_kw:
                if re.search(kw, window):
                    status_found = 'completed'
                    matched = True
                    break
            if matched:
                break
            for kw in not_started_kw:
                if re.search(kw, window):
                    status_found = 'not started'
                    matched = True
                    break
            if matched:
                break
        if status_found:
            break
    # fallback: try to detect 'FEMA' or 'emergency' in project name or funding source
    if not status_found:
        low = (pname or '').lower()
        if 'design' in low or 'design' in (doc.get('text','').lower() if docs else ''):
            # don't set arbitrarily
            status_found = None
    # convert amount to int if possible
    try:
        amount_int = int(amount)
    except Exception:
        try:
            amount_int = int(float(amount))
        except Exception:
            amount_int = amount
    results.append({
        'Project_Name': pname,
        'Funding_Source': source,
        'Amount': amount_int,
        'Status': status_found
    })

# Filter: only include those related to FEMA or emergency by checking project name or funding source for keywords
out_list = []
for r in results:
    if re.search(r'\bfema\b|\bemergency\b|caloes|caljpia', (r['Project_Name'] or '').lower()) or re.search(r'\bfema\b|\bemergency\b', (r['Funding_Source'] or '').lower()):
        out_list.append(r)

# sort by Project_Name
out_list = sorted(out_list, key=lambda x: x['Project_Name'] or '')

print("__RESULT__:")
print(json.dumps(out_list))"""

env_args = {'var_call_uegX5YtT5sjI2pkA0DpZVoVm': 'file_storage/call_uegX5YtT5sjI2pkA0DpZVoVm.json', 'var_call_jMJhMNiDysEXrJXjHk02hCoY': [], 'var_call_dC5Jtf59tQZsle7ueTVzZrRv': 'file_storage/call_dC5Jtf59tQZsle7ueTVzZrRv.json', 'var_call_c1pff0BCcHaDhyZixHzlsOJW': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
