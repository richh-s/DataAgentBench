code = """import json, re, pandas as pd

# Load mongo docs (may be file path)
raw = var_call_fk4R50xd0gNmBWBinATL6TjE
if isinstance(raw, str):
    with open(raw, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = raw

funding = pd.DataFrame(var_call_QvoSObM7OjN24O7zZhHPkupX)
if not funding.empty:
    funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

# Helper: extract status for a project name from a document text
status_patterns = [
    (re.compile(r"Capital Improvement Projects \(Design\)", re.I), 'design'),
    (re.compile(r"Capital Improvement Projects \(Construction\)", re.I), 'design'),  # treat as design/active; schema only has design/completed/not started
    (re.compile(r"Capital Improvement Projects \(Not Started\)", re.I), 'not started'),
    (re.compile(r"Disaster Recovery Projects \(Design\)", re.I), 'design'),
    (re.compile(r"Disaster Recovery Projects \(Construction\)", re.I), 'design'),
    (re.compile(r"Disaster Recovery Projects \(Not Started\)", re.I), 'not started'),
]

def normalize_name(n):
    return re.sub(r"\s+", " ", n.strip())

# Build index of documents for quick search
texts = [(d.get('filename'), d.get('text','')) for d in docs]

project_status = {}
for pname in funding['Project_Name'].dropna().unique().tolist():
    pn = normalize_name(pname)
    # search through docs where project occurs
    found = None
    for fn, txt in texts:
        if re.search(re.escape(pn), txt, flags=re.I):
            # determine status by nearest preceding section header within some window
            m = re.search(re.escape(pn), txt, flags=re.I)
            if not m:
                continue
            start = max(0, m.start()-4000)
            context = txt[start:m.start()]
            # last matched header
            last_pos = -1
            last_status = None
            for pat, st in status_patterns:
                for hm in pat.finditer(context):
                    if hm.start() > last_pos:
                        last_pos = hm.start()
                        last_status = st
            # if still none, infer from local 'Construction was completed' etc.
            if last_status is None:
                snippet = txt[m.start():m.start()+800]
                if re.search(r"Construction was completed|Notice of completion|Completed", snippet, re.I):
                    last_status = 'completed'
                elif re.search(r"currently under construction|out to bid|awaiting|working with", snippet, re.I):
                    last_status = 'design'
            found = last_status
            break
    if found is None:
        # heuristic from name
        found = 'design' if re.search(r"design", pn, re.I) else None
    project_status[pname] = found

funding['Status'] = funding['Project_Name'].map(project_status)

# Filter to emergency/FEMA related (already mostly FEMA); keep any with FEMA/emergency in project or funding source
mask = funding['Project_Name'].str.contains('fema|emergency', case=False, na=False) | funding['Funding_Source'].str.contains('fema|emergency', case=False, na=False)
out = funding.loc[mask, ['Project_Name','Funding_Source','Amount','Status']].sort_values(['Project_Name','Funding_Source']).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_fk4R50xd0gNmBWBinATL6TjE': 'file_storage/call_fk4R50xd0gNmBWBinATL6TjE.json', 'var_call_QvoSObM7OjN24O7zZhHPkupX': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
