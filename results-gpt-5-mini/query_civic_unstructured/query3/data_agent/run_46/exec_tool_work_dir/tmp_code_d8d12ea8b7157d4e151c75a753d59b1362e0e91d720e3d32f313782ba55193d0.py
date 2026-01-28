code = """import json

# Load data from previous tool calls available in storage
civic_docs_path = var_call_QMqljVvuhK67qBr9fNixxMoe
funding_records = var_call_6Bj66qSlAIifpECww67AhOpW

# Read the civic docs JSON file
with open(civic_docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Prepare lowercase text contents for faster search
docs_texts = [doc.get('text','').lower() for doc in civic_docs]

# Keywords for status
completed_kw = ['construction was completed', 'was completed', 'notice of completion', 'complete construction', 'completed', 'notice of completion filed']
design_kw = ['complete design', 'final design', 'finalizing the design', 'finalizing plans', 'design plans', 'design phase', 'preliminary design', 'working with the consultant', 'submitted plans', 'staff is working with the consultant', 'finalizing plans and specifications']
not_started_kw = ['not started', 'identified but not begun', 'not begun', 'project was identified', 'waiting for the agreement', 'was identified in the']
under_construction_kw = ['project is currently under construction', 'begin construction']

results = []

for rec in funding_records:
    pname = rec.get('Project_Name')
    fs = rec.get('Funding_Source')
    amt_raw = rec.get('Amount')

    # Normalize amount
    try:
        amt = int(amt_raw)
    except:
        try:
            amt = int(float(amt_raw))
        except:
            amt = amt_raw

    # Simplify base name: remove parenthetical suffixes and trailing design labels
    base = pname.split('(')[0]
    if ' - ' in base:
        base = base.split(' - ')[0]
    base = base.strip().lower()

    status = 'unknown'
    matched = False

    # Search for exact base substring in any document
    for text in docs_texts:
        if base and base in text:
            matched = True
            # check priority: completed > not started > design > under construction
            if any(k in text for k in completed_kw):
                status = 'completed'
            elif any(k in text for k in not_started_kw):
                status = 'not started'
            elif any(k in text for k in design_kw):
                status = 'design'
            elif any(k in text for k in under_construction_kw):
                status = 'design'
            else:
                status = 'unknown'
            break

    if not matched:
        # try token match: use words longer than 4 chars
        import re
        tokens = [t for t in re.split('\W+', base) if len(t) > 4]
        for text in docs_texts:
            if tokens and all(tok in text for tok in tokens[:3]):
                if any(k in text for k in completed_kw):
                    status = 'completed'
                elif any(k in text for k in not_started_kw):
                    status = 'not started'
                elif any(k in text for k in design_kw):
                    status = 'design'
                elif any(k in text for k in under_construction_kw):
                    status = 'design'
                else:
                    status = 'unknown'
                matched = True
                break

    results.append({
        'Project_Name': pname,
        'Funding_Source': fs,
        'Amount': amt,
        'Status': status
    })

# Build plain-text answer
lines = []
for r in results:
    lines.append(f"Project: {r['Project_Name']}")
    lines.append(f"  Funding Source: {r['Funding_Source']}")
    lines.append(f"  Amount: ${r['Amount']}")
    lines.append(f"  Status: {r['Status']}")
    lines.append("")
final_text = '\n'.join(lines).strip()

print('__RESULT__:')
print(json.dumps(final_text))"""

env_args = {'var_call_o1BWtTd1tSx4vPqmWXNGZDBX': ['civic_docs'], 'var_call_QMqljVvuhK67qBr9fNixxMoe': 'file_storage/call_QMqljVvuhK67qBr9fNixxMoe.json', 'var_call_QGnkg9EbqJE14q5U5ShRskU0': ['Funding'], 'var_call_6Bj66qSlAIifpECww67AhOpW': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
