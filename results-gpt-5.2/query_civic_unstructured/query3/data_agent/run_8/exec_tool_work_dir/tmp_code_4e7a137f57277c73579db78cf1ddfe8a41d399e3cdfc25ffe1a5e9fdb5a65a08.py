code = """import json, re
import pandas as pd

funding = pd.DataFrame(var_call_xff2ewmuK2iKeSMc6oDwytk4)
if funding.empty:
    out = []
else:
    funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

# load civic docs full
path_or_list = var_call_Ir1oIA0YaesRqUngkfCUVn1G
if isinstance(path_or_list, str):
    with open(path_or_list, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = path_or_list

texts = [d.get('text','') for d in docs]
fulltext = "\n".join(texts)

# Parse project blocks: lines with name, followed by 'Updates:' line containing status hints.
lines = [ln.strip() for ln in fulltext.splitlines()]
name_re = re.compile(r'^(?!Page\s+\d+\s+of\s+\d+)(?!Agenda Item)([A-Z0-9][A-Za-z0-9&/\-\(\)\.,\'\u2019\s]+?)$')
status_map = {}
section = None
for i, ln in enumerate(lines):
    if not ln:
        continue
    msec = re.match(r'^(Capital Improvement Projects|Disaster Recovery Projects)\s*(\((Design|Construction|Not Started)\))?$', ln)
    if msec:
        # track section; if parenthetical indicates status category
        if msec.group(3):
            section = msec.group(3).lower()
        else:
            section = None
        continue
    if ln in ('Design','Construction','Not Started'):
        section = ln.lower()
        continue
    m = name_re.match(ln)
    if m:
        name = m.group(1).strip()
        # exclude common headings
        if len(name) < 4 or name.lower().startswith(('to:', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'subject', 'recommended action', 'discussion')):
            continue
        # lookahead for updates line
        status = None
        for j in range(i+1, min(i+15, len(lines))):
            if 'Updates:' in lines[j]:
                upd = lines[j]
                if 'completed' in upd.lower() or 'was completed' in upd.lower():
                    status = 'completed'
                elif 'under construction' in upd.lower() or 'currently under construction' in upd.lower():
                    status = 'design'
                break
            if re.match(r'^[A-Z][A-Za-z].*Projects', lines[j]):
                break
        if status is None and section in ('design','construction','not started'):
            # map construction section to design (no explicit status category in prompt)
            status = 'design' if section in ('design','construction') else 'not started'
        if status:
            status_map[name] = status

# For our funded FEMA/emergency projects, attempt to find base name in status_map by removing parenthetical tags.

def normalize(n):
    return re.sub(r'\s+', ' ', n).strip().lower()

status_norm = {normalize(k): v for k,v in status_map.items()}

def find_status(project_name):
    candidates = [project_name,
                  re.sub(r'\s*\([^\)]*\)\s*$', '', project_name),
                  project_name.replace('Storm Drain', 'Storm Drainage'),
                  project_name.replace('Storm Drainage', 'Storm Drain')]
    for c in candidates:
        key = normalize(c)
        if key in status_norm:
            return status_norm[key]
    # fuzzy: contains
    base = normalize(re.sub(r'\s*\([^\)]*\)\s*$', '', project_name))
    for k,v in status_norm.items():
        if base and (base in k or k in base):
            return v
    return None

if not funding.empty:
    funding['Status'] = funding['Project_Name'].apply(find_status)
    # If still null and has FEMA/emergency keywords, default to 'design' as active unless known
    funding.loc[funding['Status'].isna(), 'Status'] = 'design'

    # aggregate funding by project & source
    grp = funding.groupby(['Project_Name','Funding_Source','Status'], as_index=False)['Amount'].sum()
    grp = grp.sort_values(['Project_Name','Funding_Source'])
    out = grp.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_xff2ewmuK2iKeSMc6oDwytk4': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_Ir1oIA0YaesRqUngkfCUVn1G': 'file_storage/call_Ir1oIA0YaesRqUngkfCUVn1G.json'}

exec(code, env_args)
