code = """import json, re, pandas as pd

funding = pd.DataFrame(var_call_A04s9y1X5sWHPskg0JTF7Ifb)
# normalize amount to int
funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

# load mongo docs
path_or_list = var_call_eLgSetgDF50oiX4FUPjLt3Yn
if isinstance(path_or_list, str):
    with open(path_or_list, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = path_or_list

# extract project statuses from docs
project_status = {}
# patterns for sections and project line formats
status_headers = {
    'design': re.compile(r'Capital Improvement Projects\s*\(Design\)|Disaster Recovery Projects\s*\(Design\)', re.I),
    'construction': re.compile(r'Capital Improvement Projects\s*\(Construction\)|Disaster Recovery Projects\s*\(Construction\)', re.I),
    'not started': re.compile(r'Capital Improvement Projects\s*\(Not Started\)|Disaster Recovery Projects\s*\(Not Started\)', re.I)
}

known_projects = set(funding['Project_Name'].dropna().unique().tolist())

for d in docs:
    text = d.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    current = None
    for ln in lines:
        if not ln:
            continue
        # update section
        for st, pat in status_headers.items():
            if pat.search(ln):
                current = st
                break
        # attempt match project names in line
        if current is None:
            continue
        # direct contains of a known project name
        for pn in known_projects:
            if pn and pn in ln:
                project_status[pn] = current
        # also match by stripping FEMA suffixes in doc names vs funding names

# if no status found for a project, infer as 'design' if contains 'Design' in name, else unknown
funding['Status'] = funding['Project_Name'].map(project_status)
funding.loc[funding['Status'].isna() & funding['Project_Name'].str.contains('design', case=False, na=False), 'Status'] = 'design'
funding['Status'] = funding['Status'].fillna('unknown')

# filter emergency/FEMA related projects based on name/source (already filtered in SQL but keep)
mask = funding['Project_Name'].str.contains('emergency|fema', case=False, na=False) | funding['Funding_Source'].str.contains('emergency|fema', case=False, na=False)
res = funding.loc[mask, ['Project_Name','Funding_Source','Amount','Status']].sort_values(['Project_Name','Funding_Source']).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_A04s9y1X5sWHPskg0JTF7Ifb': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_eLgSetgDF50oiX4FUPjLt3Yn': 'file_storage/call_eLgSetgDF50oiX4FUPjLt3Yn.json', 'var_call_yBwr7e2h5YUOO018G8hQSFDK': ['Funding']}

exec(code, env_args)
