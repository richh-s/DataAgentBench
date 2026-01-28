code = """import json, re

funding = var_call_KpVCjvVA5BYe8JcHQVrfIWGC
docs_path = var_call_F7UDdQqOSp06hyXJN6tIfdKY

with open(docs_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

results = []

for rec in funding:
    pname = rec.get('Project_Name','').strip()
    core = re.sub(r"\s*\(.*?\)", '', pname).strip()
    status = None
    found = False
    for doc in docs:
        text = doc.get('text','')
        if not text:
            continue
        # search for core name words sequence
        if re.search(re.escape(core), text, re.I):
            found = True
            m = re.search(re.escape(core), text, re.I)
            start = m.start()
            # get surrounding context
            before = text[:start].splitlines()[-8:]
            after = text[start:start+800].splitlines()[:12]
            block = '\n'.join(before + after)
            bl = block.lower()
            if re.search(r'not started|not begun|identified but not begun', bl):
                status = 'not started'
            elif re.search(r'complete design|preliminary design|design phase|design is|in the preliminary design', bl):
                status = 'design'
            elif re.search(r'construction was completed|notice of completion|complete construction|complete construction:', bl):
                status = 'completed'
            elif re.search(r'under construction|begin construction|begin construction:|begin construction\b|construction was', bl):
                # map to design (pre-construction/ construction in progress -> not completed)
                status = 'design'
            elif re.search(r'awaiting final fema|awaiting fema|awaiting final', bl):
                status = 'design'
            else:
                status = None
            break
    # convert amount to int if possible
    amt = rec.get('Amount')
    try:
        amt = int(str(amt).replace(',', '').strip())
    except:
        try:
            amt = int(float(amt))
        except:
            amt = None
    results.append({
        'Project_Name': pname,
        'Funding_Source': rec.get('Funding_Source'),
        'Amount': amt,
        'Status': status
    })

print("__RESULT__:")
print(json.dumps(results, ensure_ascii=False))"""

env_args = {'var_call_F7UDdQqOSp06hyXJN6tIfdKY': 'file_storage/call_F7UDdQqOSp06hyXJN6tIfdKY.json', 'var_call_PeJpatY4US504BCXETLCFwFV': [], 'var_call_KpVCjvVA5BYe8JcHQVrfIWGC': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
