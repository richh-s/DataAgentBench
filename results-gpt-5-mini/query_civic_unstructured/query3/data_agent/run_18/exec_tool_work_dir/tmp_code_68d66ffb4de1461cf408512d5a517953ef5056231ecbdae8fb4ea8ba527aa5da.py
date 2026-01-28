code = """import json

funding = var_call_vdX59qe1pTla9sl0WesBpRST
civic_docs_path = var_call_rHRczMIJPO629lmxlTRznRDK

# Load civic docs
with open(civic_docs_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

def core_name(name):
    # remove parentheses content
    import re
    return re.sub(r"\s*\(.*?\)", "", name).strip()

def detect_status_for_project(core, docs):
    core_l = core.lower()
    tokens = [t for t in core_l.split() if len(t)>3]
    for doc in docs:
        text = doc.get('text','').lower()
        if core_l in text or any(t in text for t in tokens):
            # get a snippet around first occurrence
            idx = text.find(core_l) if core_l in text else (text.find(tokens[0]) if tokens else -1)
            start = max(0, idx-200)
            window = text[start:start+400]
            if 'construction was completed' in window or 'complete construction' in window or 'notice of completion' in window or 'completed' in window:
                return 'completed'
            if 'complete design' in window or 'final design' in window or 'preliminary design' in window or 'design' in window or 'advertise' in window:
                return 'design'
            if 'not started' in window or 'not yet started' in window:
                return 'not started'
            if 'under construction' in window or 'begin construction' in window:
                return 'design'
    return None

results = []
for rec in funding:
    proj = rec.get('Project_Name')
    src = rec.get('Funding_Source')
    amt_raw = rec.get('Amount')
    try:
        amt = int(amt_raw)
    except:
        try:
            amt = int(str(amt_raw).replace(',', ''))
        except:
            amt = None
    core = core_name(proj or '')
    status = detect_status_for_project(core, civic_docs)
    results.append({'Project_Name': proj, 'Funding_Source': src, 'Amount': amt, 'Status': status})

# filter for fema or emergency
final = [r for r in results if r['Project_Name'] and (('fema' in r['Project_Name'].lower()) or ('emergency' in r['Project_Name'].lower()) or (r['Funding_Source'] and ('fema' in r['Funding_Source'].lower() or 'emergency' in r['Funding_Source'].lower())))]

print("__RESULT__:")
print(json.dumps(final))"""

env_args = {'var_call_vdX59qe1pTla9sl0WesBpRST': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_rHRczMIJPO629lmxlTRznRDK': 'file_storage/call_rHRczMIJPO629lmxlTRznRDK.json'}

exec(code, env_args)
