code = """import json, re, pandas as pd

funding = pd.DataFrame(var_call_t9HDXiI7niatscbPSr4fO6h0)
funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

# load civic docs full
path = var_call_TdJLOxdICAuCsOP0Cjk1FyKj
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Build status map from docs for relevant projects
projects = set(funding['Project_Name'].dropna().tolist())
status_map = {p: None for p in projects}

def find_section_status(text, project):
    # locate occurrence and infer status from nearest header above
    idx = text.lower().find(project.lower())
    if idx == -1:
        # try normalized (remove extra spaces)
        norm_text = re.sub(r'\s+', ' ', text.lower())
        norm_proj = re.sub(r'\s+', ' ', project.lower())
        idx = norm_text.find(norm_proj)
        if idx == -1:
            return None
        # map back approx by using norm_text only
        window = norm_text[max(0, idx-800):idx]
        # check for headers in window
        if 'disaster recovery projects' in window:
            # may also have (design)/(construction)/(not started)
            for k,v in [('design','design'),('construction','construction'),('not started','not started'),('completed','completed')]:
                if k in window.split('disaster recovery projects')[-1]:
                    return v
            return None
        for k,v in [('capital improvement projects (design)','design'),('capital improvement projects (construction)','construction'),('capital improvement projects (not started)','not started'),('completed','completed')]:
            if k in window:
                return v
        return None

    window = text[max(0, idx-1200):idx]
    wlow = window.lower()

    # direct cues near project line
    near = text[idx: min(len(text), idx+400)].lower()
    if 'updates:' in near:
        if 'completed' in near or 'construction was completed' in near or 'notice of completion' in near:
            return 'completed'
        if 'currently under construction' in near or 'is currently under construction' in near or 'begin construction' in near:
            return 'construction'
        if 'working with' in near or 'finalize the design' in near or 'plans are under review' in near or 'submit' in near or 'design' in near:
            return 'design'

    # header-based cues
    if 'disaster recovery projects' in wlow:
        tail = wlow.split('disaster recovery projects')[-1]
        if 'not started' in tail:
            return 'not started'
        if 'construction' in tail:
            return 'construction'
        if 'design' in tail:
            return 'design'
    for k,v in [('capital improvement projects (design)','design'),('capital improvement projects (construction)','construction'),('capital improvement projects (not started)','not started')]:
        if k in wlow:
            return v

    return None

for d in docs:
    text = d.get('text','')
    for p in projects:
        if status_map[p] is None:
            st = find_section_status(text, p)
            if st:
                status_map[p] = st

funding['Status'] = funding['Project_Name'].map(status_map).fillna('unknown')

# filter to emergency/FEMA projects (already, but keep safeguard)
mask = funding['Project_Name'].str.contains('fema|emergency', case=False, na=False) | funding['Funding_Source'].str.contains('fema|emergency', case=False, na=False)
out = funding.loc[mask, ['Project_Name','Funding_Source','Amount','Status']].sort_values(['Project_Name','Funding_Source']).to_dict('records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_t9HDXiI7niatscbPSr4fO6h0': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_TdJLOxdICAuCsOP0Cjk1FyKj': 'file_storage/call_TdJLOxdICAuCsOP0Cjk1FyKj.json'}

exec(code, env_args)
