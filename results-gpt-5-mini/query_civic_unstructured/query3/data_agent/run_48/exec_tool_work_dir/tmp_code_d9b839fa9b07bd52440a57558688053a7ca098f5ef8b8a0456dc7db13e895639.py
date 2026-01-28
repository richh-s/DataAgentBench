code = """import json

# Load data from stored files
with open(var_call_doKwQqZMvpmPnawdjdbN3n3o, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_s6qdIdS4Yp618zXNPzZHwa0f, 'r') as f:
    funding_fema = json.load(f)

# Combine civic texts
all_text = ' '.join(d.get('text','') for d in civic_docs).lower()

# Helper
def base_name(name):
    if not isinstance(name, str):
        return ''
    return name.split('(')[0].strip().lower()

# Status keywords
design_kws = ['complete design', 'final design', 'preliminary design', 'design plans', 'complete design:']
completed_kws = ['construction was completed', 'project is currently under construction', 'complete construction', 'notice of completion', 'begin construction', 'awarded the contract']
notstarted_kws = ['not started', 'not begun', 'not yet started']

results = []
for rec in funding_fema:
    pname = rec.get('Project_Name','')
    psource = rec.get('Funding_Source','')
    try:
        amount = int(rec.get('Amount',0))
    except:
        try:
            amount = int(float(rec.get('Amount',0)))
        except:
            amount = 0
    b = base_name(pname)
    status = 'unknown'
    if b and b in all_text:
        # find window
        idx = all_text.find(b)
        start = max(0, idx-200)
        end = min(len(all_text), idx+200)
        window = all_text[start:end]
        for kw in design_kws:
            if kw in window:
                status = 'design'
                break
        if status == 'unknown':
            for kw in completed_kws:
                if kw in window:
                    status = 'completed'
                    break
        if status == 'unknown':
            for kw in notstarted_kws:
                if kw in window:
                    status = 'not started'
                    break
    # If not found in civic text, still include (they matched by fema/emergency)
    results.append({'Project_Name': pname, 'Funding_Source': psource, 'Amount': amount, 'Status': status})

# Sort
results = sorted(results, key=lambda x: x['Project_Name'].lower())

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_doKwQqZMvpmPnawdjdbN3n3o': 'file_storage/call_doKwQqZMvpmPnawdjdbN3n3o.json', 'var_call_wBrhbjFYhMnA5OtJjyPFnbnZ': 'file_storage/call_wBrhbjFYhMnA5OtJjyPFnbnZ.json', 'var_call_s6qdIdS4Yp618zXNPzZHwa0f': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
