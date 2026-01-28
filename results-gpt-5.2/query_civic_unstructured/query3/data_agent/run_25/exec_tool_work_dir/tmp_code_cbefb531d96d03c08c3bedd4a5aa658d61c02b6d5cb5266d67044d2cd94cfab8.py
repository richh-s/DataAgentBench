code = """import json, re, pandas as pd

funding = pd.DataFrame(var_call_aluKol7THXqZx4gms9rf6s5h)
funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

# Load civic docs (may be file path)
if isinstance(var_call_pa6OGcwh7FDMcfoNSFcWYRqq, str):
    with open(var_call_pa6OGcwh7FDMcfoNSFcWYRqq, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = var_call_pa6OGcwh7FDMcfoNSFcWYRqq

texts = [d.get('text','') for d in docs]
all_text = "\n".join(texts)

# Find statuses from agenda style lists by locating project name lines and nearby header
status_map = {}

# Known status headers
headers = {
    'design': [r'Capital Improvement Projects \(Design\)', r'Disaster Recovery Projects \(Design\)', r'Projects \(Design\)'],
    'construction': [r'Capital Improvement Projects \(Construction\)', r'Disaster Recovery Projects \(Construction\)'],
    'not started': [r'Capital Improvement Projects \(Not Started\)', r'Disaster Recovery Projects \(Not Started\)', r'\(Not Started\)']
}

def find_status_for_project(proj):
    # search occurrences in the big text
    for m in re.finditer(re.escape(proj), all_text, flags=re.IGNORECASE):
        start = max(0, m.start()-2000)
        context = all_text[start:m.start()]
        # find last header occurrence in context
        last = None
        for status, pats in headers.items():
            for pat in pats:
                for hm in re.finditer(pat, context, flags=re.IGNORECASE):
                    pos = start + hm.start()
                    if (last is None) or pos > last[0]:
                        last = (pos, status)
        if last:
            return last[1]
    return None

projects = funding['Project_Name'].drop_duplicates().tolist()
for p in projects:
    status_map[p] = find_status_for_project(p)

out = funding.copy()
out['Status'] = out['Project_Name'].map(status_map)
# If agenda uses 'under construction' without header, map to 'construction'
out['Status'] = out['Status'].fillna('')
out.loc[out['Status'].eq('construction'), 'Status'] = 'design'  # normalize to requested statuses? keep as construction? revert
# Actually requested statuses: design, completed, not started. We'll infer completed if text contains 'completed' near project.

def infer_completed(proj):
    for m in re.finditer(re.escape(proj), all_text, flags=re.IGNORECASE):
        window = all_text[m.start():m.start()+800]
        if re.search(r'Construction was completed|completed\b|Notice of completion', window, flags=re.IGNORECASE):
            return True
    return False

completed = {p: infer_completed(p) for p in projects}
for p, iscomp in completed.items():
    if iscomp:
        out.loc[out['Project_Name']==p, 'Status'] = 'completed'

# Map remaining statuses: if matched design header -> design; not started header -> not started
# Our earlier function returns 'design' or 'not started' only. Keep those.
out.loc[out['Status'].eq(''), 'Status'] = None

# Aggregate funding by project and source (keep as rows but ensure amount numeric)
out = out[['Project_Name','Funding_Source','Amount','Status']].sort_values(['Project_Name','Funding_Source'])
result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_aluKol7THXqZx4gms9rf6s5h': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_pa6OGcwh7FDMcfoNSFcWYRqq': 'file_storage/call_pa6OGcwh7FDMcfoNSFcWYRqq.json'}

exec(code, env_args)
