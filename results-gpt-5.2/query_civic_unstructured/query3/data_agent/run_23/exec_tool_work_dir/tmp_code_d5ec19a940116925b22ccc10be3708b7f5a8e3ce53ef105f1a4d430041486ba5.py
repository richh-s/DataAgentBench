code = """import json, re
import pandas as pd

funding = pd.DataFrame(var_call_V2de3mRN0503qVuT7j4zmNA3)
funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

# Load civic docs (may be a filepath)
docs_obj = var_call_0DkRL7ynJ2rqb55FvOTcvUhq
if isinstance(docs_obj, str) and docs_obj.endswith('.json'):
    with open(docs_obj, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_obj

# Prepare set of candidate projects from funding that match emergency/FEMA
cand = funding['Project_Name'].dropna().unique().tolist()

# Function: find status by searching near project name
status_terms = [
    ('design', re.compile(r'(?i)\bdesign\b')),
    ('completed', re.compile(r'(?i)\b(completed|notice of completion|construction was completed|complete construction)\b')),
    ('not started', re.compile(r'(?i)\bnot started\b')),
    ('construction', re.compile(r'(?i)\bunder construction\b')),
]

def extract_status(text, proj):
    # locate occurrences of a simplified key
    key = re.escape(proj)
    m = re.search(key, text)
    if not m:
        # try without parenthetical suffix
        base = re.sub(r'\s*\([^)]*\)\s*','', proj).strip()
        if base and base != proj:
            m = re.search(re.escape(base), text)
            if not m:
                return None
        else:
            return None
    start = max(0, m.start()-400)
    end = min(len(text), m.end()+400)
    window = text[start:end]
    for label, rx in status_terms:
        if rx.search(window):
            # normalize construction as design/completed/not started? keep 'construction'
            return label
    return None

# Map project -> best status found across docs (prefer completed > construction > design > not started)
priority = {'completed':3, 'construction':2, 'design':1, 'not started':0}
proj_status = {p: None for p in cand}
proj_pri = {p: -1 for p in cand}
for d in docs:
    text = d.get('text','')
    for p in cand:
        st = extract_status(text, p)
        if st is None:
            continue
        pri = priority.get(st, -1)
        if pri > proj_pri[p]:
            proj_pri[p] = pri
            proj_status[p] = st

funding['Status'] = funding['Project_Name'].map(proj_status)

# Aggregate by project + source + status (sum amounts if multiple)
out = (funding
       .groupby(['Project_Name','Funding_Source','Status'], dropna=False, as_index=False)['Amount'].sum())
out = out.sort_values(['Project_Name','Funding_Source'])

records = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(records))"""

env_args = {'var_call_V2de3mRN0503qVuT7j4zmNA3': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_0DkRL7ynJ2rqb55FvOTcvUhq': 'file_storage/call_0DkRL7ynJ2rqb55FvOTcvUhq.json'}

exec(code, env_args)
