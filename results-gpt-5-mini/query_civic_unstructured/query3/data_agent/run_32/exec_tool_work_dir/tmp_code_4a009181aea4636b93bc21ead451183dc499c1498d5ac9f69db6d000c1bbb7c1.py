code = """import json, re
# Access funding records list from storage variable
funding_records = var_call_Z8q40OmBHPrxzHnOIZVWaWWJ
# Load civic docs from file path stored in var_call_c6lEJx4mdV92C2C8eH4Z8cxt
with open(var_call_c6lEJx4mdV92C2C8eH4Z8cxt, 'r') as f:
    civic_docs = json.load(f)

combined = "\n".join(d.get('text','') for d in civic_docs).lower()

def normalize_name(name):
    if not name:
        return ''
    # remove parenthetical suffixes
    return re.sub(r"\s*\([^)]*\)\s*$", "", name).strip()

def find_in_text(name):
    if not name:
        return -1
    name_l = name.lower()
    # direct match
    idx = combined.find(name_l)
    if idx != -1:
        return idx
    # try normalized (strip paren)
    norm = normalize_name(name).lower()
    if norm and norm != name_l:
        idx = combined.find(norm)
        if idx != -1:
            return idx
    # try searching for longest token >4 chars
    tokens = [t for t in re.split(r"[^a-z0-9]+", norm) if len(t) > 4]
    tokens.sort(key=len, reverse=True)
    for t in tokens:
        idx = combined.find(t)
        if idx != -1:
            return idx
    return -1

def determine_status_at_index(idx):
    if idx == -1:
        return 'design'
    start = max(0, idx-300)
    end = min(len(combined), idx+300)
    ctx = combined[start:end]
    if any(p in ctx for p in ['construction was completed', 'complete construction', 'notice of completion', 'notice of completion filed', 'construction was completed,', 'construction was completed']):
        return 'completed'
    if any(p in ctx for p in ['completed,', 'completed\n', '\ncompleted', ' completed ']):
        return 'completed'
    if any(p in ctx for p in ['not started', 'not begun', 'identified but not begun']):
        return 'not started'
    # look for design/planning cues
    if any(p in ctx for p in ['design', 'complete design', 'final design', 'advertise', 'begin construction', 'project schedule', 'updates', 'awaiting', 'awaiting approval']):
        return 'design'
    return 'design'

output = []
for rec in funding_records:
    pname = rec.get('Project_Name')
    src = rec.get('Funding_Source')
    amt_raw = rec.get('Amount')
    # format amount
    try:
        amt = int(amt_raw)
        amt_str = f"${amt:,}"
    except:
        amt_str = None
    idx = find_in_text(pname)
    status = determine_status_at_index(idx)
    output.append({
        'Project_Name': pname,
        'Funding_Source': src,
        'Amount': amt_str,
        'Status': status
    })

# Sort by Project_Name
output = sorted(output, key=lambda x: (x['Project_Name'] or '').lower())

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_IkHKtTihYjPSZo8aZpBDmyFU': 'file_storage/call_IkHKtTihYjPSZo8aZpBDmyFU.json', 'var_call_c6lEJx4mdV92C2C8eH4Z8cxt': 'file_storage/call_c6lEJx4mdV92C2C8eH4Z8cxt.json', 'var_call_Z8q40OmBHPrxzHnOIZVWaWWJ': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '64', 'Project_Name': 'Outdoor Warning Signs', 'Funding_Source': 'Urban Renewal Fund', 'Amount': '92000'}, {'Funding_ID': '65', 'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': '28000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '73', 'Project_Name': 'PCH Overhead Warning Signs', 'Funding_Source': 'International Organization Grant', 'Amount': '73000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
