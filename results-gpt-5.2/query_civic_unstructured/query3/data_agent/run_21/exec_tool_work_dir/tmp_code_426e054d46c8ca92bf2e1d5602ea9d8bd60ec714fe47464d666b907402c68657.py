code = """import re, json
import pandas as pd

# Load docs (may be file path)
docs_src = var_call_SvfsYUiLIq1IhXqQTJ1NzQGF
if isinstance(docs_src, str):
    import pathlib
    p = pathlib.Path(docs_src)
    docs = json.loads(p.read_text())
else:
    docs = docs_src

funding = pd.DataFrame(var_call_7YKPkMpvh0ZmhvrcVVHK5n0d)
if not funding.empty:
    funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

# Extract project statuses from civic docs by locating project name line and nearby text

def norm(s):
    return re.sub(r'\s+', ' ', (s or '').strip()).lower()

status_keywords = [
    ('completed', [r'completed', r'construction was completed', r'notice of completion', r'acceptance']),
    ('design', [r'complete design', r'final design', r'preliminary design', r'design plans', r'under design', r'plans (and|&) specifications', r'plans are under review']),
    ('not started', [r'not started', r'identified', r'waiting for the agreement', r'to request proposal', r'will be issuing', r'will include', r'will be discussed', r'pending']),
    ('construction', [r'currently under construction', r'begin construction', r'out to bid', r'advertise'])
]

# Prepare candidate project names from funding table
project_names = funding['Project_Name'].dropna().unique().tolist()
proj_norm_map = {norm(p): p for p in project_names}

# Initialize status map
status_map = {}

for d in docs:
    text = d.get('text','')
    text_lower = text.lower()
    for pn in project_names:
        pn_l = pn.lower()
        if pn_l in text_lower:
            # find first occurrence and take window around it
            idx = text_lower.find(pn_l)
            window = text_lower[max(0, idx-500): idx+800]
            # infer status
            inferred = None
            for st, pats in status_keywords:
                for pat in pats:
                    if re.search(pat, window):
                        inferred = st
                        break
                if inferred:
                    break
            if inferred is None:
                # fallback: look for 'updates:' in window and if has 'awaiting' treat as design
                if 'awaiting' in window or 'under review' in window:
                    inferred = 'design'
            # store with precedence: completed > construction > design > not started
            if inferred:
                prev = status_map.get(pn)
                precedence = {'completed':4,'construction':3,'design':2,'not started':1,None:0}
                if precedence.get(inferred,0) > precedence.get(prev,0):
                    status_map[pn] = inferred

funding['Status'] = funding['Project_Name'].map(status_map)

# filter related to emergency or fema (already via name); also include any with source text match? keep as is.
res = funding[['Project_Name','Funding_Source','Amount','Status']].sort_values(['Project_Name','Funding_Source']).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_SvfsYUiLIq1IhXqQTJ1NzQGF': 'file_storage/call_SvfsYUiLIq1IhXqQTJ1NzQGF.json', 'var_call_7YKPkMpvh0ZmhvrcVVHK5n0d': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
