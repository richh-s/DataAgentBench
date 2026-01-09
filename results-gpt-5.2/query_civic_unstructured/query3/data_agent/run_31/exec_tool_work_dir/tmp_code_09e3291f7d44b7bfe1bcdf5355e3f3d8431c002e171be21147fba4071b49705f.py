code = """import json, re
import pandas as pd

# funding rows
funding = pd.DataFrame(var_call_b8SB9DkNpKcVJgcDJkwoQ6yR).copy()
funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

# read full civic docs result (stored in json file)
path = var_call_p0vMzMLXXxYIzNXv8jWNuwEO
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# build set of project names from funding list to look up status in docs
proj_names = sorted(set(funding['Project_Name'].dropna().tolist()))

# helper to extract a likely status line from a doc around a project mention
status_keywords = ['Design', 'Construction', 'Not Started', 'Completed']

def find_status_for_project(text, project):
    # try exact match, else try normalized (strip parenthetical)
    idx = text.lower().find(project.lower())
    if idx == -1:
        base = re.sub(r'\s*\([^)]*\)\s*$', '', project).strip()
        if base and base.lower() != project.lower():
            idx = text.lower().find(base.lower())
    if idx == -1:
        return None
    window = text[max(0, idx-600): idx+600]
    # look for section headings in window
    # prefer 'Capital Improvement Projects (X)' / 'Disaster Recovery Projects (X)'
    m = re.findall(r'(Capital Improvement Projects\s*\(([^)]+)\)|Disaster Recovery Projects\s*\(([^)]+)\))', window, flags=re.I)
    if m:
        # take last match in window as closest preceding section
        last = m[-1]
        sect = (last[1] or last[2] or '').strip()
        return sect.lower()
    # otherwise look for explicit update phrases
    if re.search(r'currently under construction', window, flags=re.I):
        return 'construction'
    if re.search(r'construction was completed|notice of completion', window, flags=re.I):
        return 'completed'
    if re.search(r'preliminary design|finalize the design|complete design|under design', window, flags=re.I):
        return 'design'
    if re.search(r'not started', window, flags=re.I):
        return 'not started'
    return None

# compute status per project by scanning docs until found
proj_status = {}
for p in proj_names:
    st = None
    for d in docs:
        st = find_status_for_project(d.get('text',''), p)
        if st:
            break
    proj_status[p] = st

funding['Status'] = funding['Project_Name'].map(proj_status)

# output records
out = funding.sort_values(['Project_Name','Funding_Source']).to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_b8SB9DkNpKcVJgcDJkwoQ6yR': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_p0vMzMLXXxYIzNXv8jWNuwEO': 'file_storage/call_p0vMzMLXXxYIzNXv8jWNuwEO.json'}

exec(code, env_args)
