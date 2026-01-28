code = """import json, re

# Load civic docs from file path variable
with open(var_call_c1qEeIcfYV2j9XXcklUAC7jg, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Funding records that matched FEMA/emergency from earlier SQL query are available as var_call_SFPIdfcgExZ2Uz4hYAmGMLRw
funding = var_call_SFPIdfcgExZ2Uz4hYAmGMLRw

# Prepare regex escape for searching project names

def find_status_in_text(text, proj_name):
    # search for proj_name in text
    idx = text.lower().find(proj_name.lower())
    if idx == -1:
        return None
    # take window
    start = max(0, idx-400)
    end = min(len(text), idx+400)
    window = text[start:end].lower()
    # status patterns
    if re.search(r'construction (was )?completed|notice of completion|complete construction|construction was completed', window):
        return 'completed'
    if re.search(r'project is currently under construction|begin construction|begin construction:|begin construction\b', window):
        return 'under construction'
    if re.search(r'complete design|preliminary design|final design|in the preliminary design phase|design plans|estimated schedule:.*complete design', window):
        return 'design'
    if re.search(r'not started|not yet', window):
        return 'not started'
    # other hints
    if 'advertise' in window or 'design' in window:
        return 'design'
    return None

# Priority
priority = {'completed':4, 'under construction':3, 'design':2, 'not started':1, None:0}

results = []
for f in funding:
    proj = f.get('Project_Name')
    fs = f.get('Funding_Source')
    amt = f.get('Amount')
    # try to find status in docs
    best_status = None
    for doc in docs:
        text = doc.get('text','')
        status = find_status_in_text(text, proj)
        if status and priority[status] > priority.get(best_status,0):
            best_status = status
    # if not found, try searching by base name without parentheses (strip suffixes)
    if not best_status:
        base = re.sub(r"\s*\(.*?\)\s*", "", proj).strip()
        for doc in docs:
            status = find_status_in_text(doc.get('text',''), base)
            if status and priority[status] > priority.get(best_status,0):
                best_status = status
    # convert amount to int if possible
    try:
        amount_val = int(amt)
    except:
        try:
            amount_val = int(float(amt))
        except:
            amount_val = None
    results.append({'Project_Name': proj, 'Funding_Source': fs, 'Amount': amount_val, 'Status': best_status})

# Deduplicate exact tuples
seen = set()
final = []
for r in results:
    key = (r['Project_Name'], r['Funding_Source'], r['Amount'], r['Status'])
    if key in seen:
        continue
    seen.add(key)
    final.append(r)

print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_call_c1qEeIcfYV2j9XXcklUAC7jg': 'file_storage/call_c1qEeIcfYV2j9XXcklUAC7jg.json', 'var_call_FH2VjWuOAAWVTxL5LBeROsyI': 'file_storage/call_FH2VjWuOAAWVTxL5LBeROsyI.json', 'var_call_TyLQRS18h4ix11kGbl7qZGZp': [], 'var_call_SFPIdfcgExZ2Uz4hYAmGMLRw': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
