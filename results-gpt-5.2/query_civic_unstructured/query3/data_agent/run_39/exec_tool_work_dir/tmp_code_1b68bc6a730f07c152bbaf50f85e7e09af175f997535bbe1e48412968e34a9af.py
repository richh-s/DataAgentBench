code = """import json, re, pandas as pd
from pathlib import Path

# Load civic docs result (may be file path)
raw = var_call_Ul7aPB6gnCbeFj8mTLxgBT0T
if isinstance(raw, str) and raw.endswith('.json'):
    docs = json.loads(Path(raw).read_text())
else:
    docs = raw

funding = pd.DataFrame(var_call_zkHE1IWBtwQ21HCHdoGrOBtX)
# normalize amount
funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

# Extract project statuses from civic docs by parsing common agenda report structure
status_map = {}  # project_name -> status

status_headers = [
    ('Design', 'design'),
    ('Construction', 'construction'),
    ('Not Started', 'not started'),
    ('Completed', 'completed')
]

for d in docs:
    text = d.get('text','')
    # Split into lines for easier parsing
    lines = [ln.strip() for ln in text.splitlines()]
    current_status = None
    for ln in lines:
        # detect section headers like "Capital Improvement Projects (Design)" etc.
        m = re.search(r'\((Design|Construction|Not Started|Completed)\)', ln, flags=re.I)
        if m:
            sec = m.group(1).lower()
            # map to standardized
            for hdr, std in status_headers:
                if hdr.lower() == sec.lower():
                    current_status = std
                    break
            continue
        # project name lines: typically non-empty and not bullet markers
        if current_status in ('design','construction','not started','completed'):
            if not ln:
                continue
            if ln.startswith(('•','(cid:', '-', 'Updates', 'Project', 'RECOMMENDED', 'DISCUSSION', 'To:', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject', 'Page', 'Agenda')):
                continue
            # heuristics: project name line usually contains letters and not too long; avoid sentences
            if len(ln) > 3 and len(ln) < 120 and not ln.endswith((':',)):
                # Exclude obvious narrative lines
                if re.search(r'\b(City|Staff|Consultant|Funding|Agreement|Notice|Bids|Plans)\b', ln) and not re.search(r'\bProject\b', ln):
                    pass
                # accept and store
                status_map.setdefault(ln, current_status)

# Prepare output joined on exact Project_Name match
funding['Status'] = funding['Project_Name'].map(status_map)

# If status not found, try fuzzy match by stripping parenthetical suffix
base_to_status = {}
for k,v in status_map.items():
    base = re.sub(r'\s*\([^\)]*\)\s*','',k).strip().lower()
    if base and base not in base_to_status:
        base_to_status[base]=v

def infer_status(pn, st):
    if pd.notna(st):
        return st
    base = re.sub(r'\s*\([^\)]*\)\s*','',pn).strip().lower()
    return base_to_status.get(base)

funding['Status'] = [infer_status(pn, st) for pn,st in zip(funding['Project_Name'], funding['Status'])]

# Topic filter: projects related to emergency or FEMA already by query; keep all from funding selection
out = funding.sort_values(['Project_Name','Funding_Source']).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Ul7aPB6gnCbeFj8mTLxgBT0T': 'file_storage/call_Ul7aPB6gnCbeFj8mTLxgBT0T.json', 'var_call_zkHE1IWBtwQ21HCHdoGrOBtX': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
