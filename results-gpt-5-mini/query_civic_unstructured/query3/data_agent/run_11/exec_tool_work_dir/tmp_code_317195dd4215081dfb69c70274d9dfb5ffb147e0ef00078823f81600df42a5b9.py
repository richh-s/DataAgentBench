code = """import json
funding = var_call_xFUYNSWQQe0b7JtiSruERKuM
path = var_call_2ajh9JRnLUZjcgZaBU1zv32y
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)
all_text = ' '.join(d.get('text','') for d in docs).lower()

def norm(name):
    if ' (' in name:
        base = name.split(' (')[0]
    else:
        base = name
    return base.lower().strip()

results = []
for fr in funding:
    pname = fr.get('Project_Name','')
    psource = fr.get('Funding_Source','')
    amount = fr.get('Amount', None)
    base = norm(pname)
    status = 'not found'
    idx = all_text.find(base)
    context = ''
    if idx != -1:
        start = idx - 200
        if start < 0:
            start = 0
        end = idx + 200
        context = all_text[start:end]
    if 'construction was completed' in context or 'notice of completion' in context or 'complete construction' in context or 'completed' in context:
        status = 'completed'
    elif 'awaiting' in context or 'waiting for' in context or 'not started' in context or 'identified' in context:
        status = 'not started'
    elif 'preliminary design' in context or 'working with the consultant' in context or 'finalize the design' in context or 'complete design' in context or 'design phase' in context or 'begin construction' in context or 'currently under construction' in context or 'advertise' in context:
        status = 'design'
    else:
        if context:
            status = 'not started'
        else:
            status = 'not started'
    try:
        amt = int(amount)
    except:
        try:
            amt = int(float(amount))
        except:
            amt = None
    results.append({'Project_Name': pname, 'Funding_Source': psource, 'Amount': amt, 'Status': status})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_2ajh9JRnLUZjcgZaBU1zv32y': 'file_storage/call_2ajh9JRnLUZjcgZaBU1zv32y.json', 'var_call_QLNYso6DCSC7NVUDNVKM3KbR': {'doc_count': 19}, 'var_call_xFUYNSWQQe0b7JtiSruERKuM': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
