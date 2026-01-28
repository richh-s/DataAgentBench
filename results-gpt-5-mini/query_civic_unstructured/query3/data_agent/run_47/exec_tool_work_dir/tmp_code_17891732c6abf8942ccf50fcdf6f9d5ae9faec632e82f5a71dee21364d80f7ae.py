code = """import json

# Access stored variables
funding = var_call_KpVCjvVA5BYe8JcHQVrfIWGC
docs_var = var_call_F7UDdQqOSp06hyXJN6tIfdKY

# Load docs: docs_var may be a filepath string or a list
if isinstance(docs_var, str) and docs_var.endswith('.json'):
    with open(docs_var, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_var

results = []

for rec in funding:
    pname = rec.get('Project_Name','').strip()
    # remove trailing parenthetical suffixes for core matching
    core = pname
    if '(' in pname:
        core = pname.split('(')[0].strip()
    core_lower = core.lower()
    status = None
    # Search for core in docs that mention FEMA or emergency
    for doc in docs:
        text = doc.get('text','')
        if not text:
            continue
        tlower = text.lower()
        if 'fema' not in tlower and 'emergency' not in tlower:
            continue
        idx = tlower.find(core_lower)
        if idx != -1:
            # get context around match
            start = max(0, idx-500)
            context = tlower[start: idx+500]
            # determine status by keywords
            if any(k in context for k in ['not started', 'not begun', 'identified but not begun']):
                status = 'not started'
            elif any(k in context for k in ['complete design', 'preliminary design', 'design phase', 'design is', 'preliminary design phase', 'in the preliminary design']):
                status = 'design'
            elif any(k in context for k in ['construction was completed', 'notice of completion', 'complete construction', 'completed,']):
                status = 'completed'
            elif any(k in context for k in ['under construction', 'begin construction', 'begin construction:', 'construction was']):
                status = 'design'
            elif 'awaiting final fema' in context or 'awaiting fema' in context or 'awaiting final' in context:
                status = 'design'
            else:
                status = None
            break
    # parse amount
    amt = rec.get('Amount')
    try:
        amt_parsed = int(str(amt).replace(',', '').strip())
    except:
        try:
            amt_parsed = int(float(amt))
        except:
            amt_parsed = None
    results.append({'Project_Name': pname, 'Funding_Source': rec.get('Funding_Source'), 'Amount': amt_parsed, 'Status': status})

print("__RESULT__:")
print(json.dumps(results, ensure_ascii=False))"""

env_args = {'var_call_F7UDdQqOSp06hyXJN6tIfdKY': 'file_storage/call_F7UDdQqOSp06hyXJN6tIfdKY.json', 'var_call_PeJpatY4US504BCXETLCFwFV': [], 'var_call_KpVCjvVA5BYe8JcHQVrfIWGC': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
