code = """import json, re

# Load the funding records that contain FEMA/emergency from previous query result
with open(var_call_KBiq7j3PwLDI11CUJwjDUwuL, 'r') as f:
    funding_hits = json.load(f)

# Load the civic docs subset
with open(var_call_9EeqpAkBu1yKdzj5uhUK8YP5, 'r') as f:
    civic_docs = json.load(f)

# Combine civic texts
full_text = '\n'.join(d.get('text','') for d in civic_docs)
full_low = full_text.lower()

# Helper to infer status by searching nearby text
def infer_status_by_name(name):
    name_low = name.lower()
    # remove parentheticals for searching
    base = re.sub(r"\s*\(.*?\)", "", name_low)
    base = re.sub(r"[^a-z0-9 ]+", " ", base).strip()
    idx = full_low.find(base)
    snippet = ''
    if idx != -1:
        snippet = full_low[max(0, idx-200): idx+800]
    else:
        # try partial words
        for w in base.split():
            if len(w) > 4:
                i = full_low.find(w)
                if i!=-1:
                    snippet = full_low[max(0, i-200): i+800]
                    break
    s = 'unknown'
    if snippet:
        if 'construction was completed' in snippet or 'notice of completion' in snippet or 'complete construction' in snippet or 'construction was completed' in snippet:
            s = 'completed'
        elif 'complete design' in snippet or 'preliminary design' in snippet or 'final design' in snippet or 'project is in the preliminary design phase' in snippet or 'working with the consultant' in snippet:
            s = 'design'
        elif 'not started' in snippet or 'identified' in snippet or 'awaiting' in snippet or 'waiting for' in snippet or 'advertise:' in snippet or 'begin construction' in snippet:
            s = 'not started'
        elif 'under construction' in snippet or 'currently under construction' in snippet:
            s = 'not started'
    return s

# Build final list with inferred statuses
results = []
for r in funding_hits:
    pname = r.get('Project_Name')
    fsrc = r.get('Funding_Source')
    amt = r.get('Amount')
    try:
        amt_val = int(amt)
    except:
        try:
            amt_val = int(float(amt))
        except:
            amt_val = None
    status = infer_status_by_name(pname)
    results.append({'Project_Name': pname, 'Funding_Source': fsrc, 'Amount': amt_val, 'Status': status})

# sort
results_sorted = sorted(results, key=lambda x: x['Project_Name'].lower())

print('__RESULT__:')
print(json.dumps(results_sorted))"""

env_args = {'var_call_OTsZFSddYbanLEHhV1oqAEar': 'file_storage/call_OTsZFSddYbanLEHhV1oqAEar.json', 'var_call_RpKhjqFTVlsT3xmU5phuCvLx': 'file_storage/call_RpKhjqFTVlsT3xmU5phuCvLx.json', 'var_call_KBiq7j3PwLDI11CUJwjDUwuL': [{'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_9EeqpAkBu1yKdzj5uhUK8YP5': 'file_storage/call_9EeqpAkBu1yKdzj5uhUK8YP5.json'}

exec(code, env_args)
