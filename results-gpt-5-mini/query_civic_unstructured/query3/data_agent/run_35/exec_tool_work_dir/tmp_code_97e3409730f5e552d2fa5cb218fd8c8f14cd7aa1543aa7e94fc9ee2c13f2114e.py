code = """import json
# funding matches variable from SQL query
funding_matches = var_call_hGkmJSAS5AEkDRyZcXmjdl7D
# civic docs file path
civic_docs_path = var_call_RRCtw1M6xV7FbcQ20yHrrUFn
with open(civic_docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
all_text = '\n'.join(doc.get('text','') for doc in civic_docs).lower()

def detect_status(name):
    if not name:
        return 'unknown'
    base = name.split('(')[0].strip().lower()
    idx = all_text.find(base)
    if idx == -1:
        idx = all_text.find(name.lower())
    if idx == -1:
        return 'unknown'
    start = max(0, idx-200)
    end = min(len(all_text), idx+200)
    window = all_text[start:end]
    if 'not started' in window:
        return 'not started'
    completed_phrases = ['construction was completed', 'notice of completion', 'was completed', 'completed']
    for ph in completed_phrases:
        if ph in window:
            return 'completed'
    if 'design' in window or 'preliminary design' in window or 'final design' in window:
        return 'design'
    return 'unknown'

results = []
for r in funding_matches:
    pname = r.get('Project_Name')
    fsrc = r.get('Funding_Source')
    amt_raw = r.get('Amount')
    try:
        amt = int(amt_raw)
    except:
        try:
            amt = int(float(amt_raw))
        except:
            amt = None
    status = detect_status(pname)
    results.append({'Project_Name': pname, 'Funding_Source': fsrc, 'Amount': amt, 'Status': status})

# sort
results = sorted(results, key=lambda x: (x['Project_Name'] or '').lower())
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_RRCtw1M6xV7FbcQ20yHrrUFn': 'file_storage/call_RRCtw1M6xV7FbcQ20yHrrUFn.json', 'var_call_t41ybTqD9rfuGcYnHnPfELh2': 'file_storage/call_t41ybTqD9rfuGcYnHnPfELh2.json', 'var_call_dfvnjNQ8s8EXwWJE9zFV1gmc': {'funding_records': 500, 'civic_docs': 5}, 'var_call_hGkmJSAS5AEkDRyZcXmjdl7D': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Signs', 'Funding_Source': 'Urban Renewal Fund', 'Amount': '92000'}, {'Project_Name': 'Outdoor Warning Sirens', 'Funding_Source': 'Social Impact Investment', 'Amount': '28000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_vabMOb9b32SBYyka7yZWTZdr': {'count': 22}}

exec(code, env_args)
