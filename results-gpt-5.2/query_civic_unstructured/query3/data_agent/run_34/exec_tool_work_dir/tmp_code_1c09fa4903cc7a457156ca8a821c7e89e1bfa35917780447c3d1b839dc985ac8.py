code = """import json, re, pandas as pd

# Load civic docs results (may be a JSON file path)
docs_obj = var_call_F71sEBFB8UaoSqHczyr6A7Wl
if isinstance(docs_obj, str):
    with open(docs_obj, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_obj

funding = var_call_AaC1DfsxpMM2NAKLa5RfwE3X

# Heuristic extraction: find project lines that contain FEMA or emergency and infer status from section headers.
status_map = {
    'design': re.compile(r'\bCapital Improvement Projects\s*\(Design\)|\(Design\)', re.I),
    'construction': re.compile(r'\bCapital Improvement Projects\s*\(Construction\)|\bConstruction\b', re.I),
    'not started': re.compile(r'\bCapital Improvement Projects\s*\(Not Started\)|\bNot Started\b', re.I),
    'disaster': re.compile(r'\bDisaster Recovery Projects\b', re.I),
}

# We'll parse by scanning lines; when we hit a header, set current_status bucket.
projects_status = {}

proj_line_re = re.compile(r'^[A-Za-z0-9][A-Za-z0-9\-\&\,\./\(\)\s]+(?:FEMA|emergency)[A-Za-z0-9\-\&\,\./\(\)\s]*$', re.I)

for d in docs:
    text = d.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    current = None
    for ln in lines:
        if not ln:
            continue
        # update current section
        for k,pat in status_map.items():
            if pat.search(ln):
                current = k
                break
        # capture project lines containing FEMA/emergency
        if ('fema' in ln.lower()) or ('emergency' in ln.lower()):
            if proj_line_re.match(ln) and len(ln) <= 140:
                name = re.sub(r'\s{2,}', ' ', ln)
                # Normalize some known header-like lines out
                if any(x in name.lower() for x in ['report', 'projects status', 'warning signs']):
                    pass
                else:
                    if name not in projects_status:
                        projects_status[name] = set()
                    if current:
                        # map disaster to design/other? keep as-is
                        projects_status[name].add(current)

# Also include key project from preview: Outdoor Warning Signs (emergency-related). We'll map to 'design' if present.
# But it doesn't include word emergency; ignore.

# Build funding dataframe and join with extracted statuses.
fdf = pd.DataFrame(funding)
if not fdf.empty:
    fdf['Amount'] = pd.to_numeric(fdf['Amount'], errors='coerce')

# Attach status by matching exact Project_Name to extracted keys, else infer from name (FEMA => disaster)
status_list = []
for pn in fdf['Project_Name'].tolist() if not fdf.empty else []:
    st = None
    if pn in projects_status and projects_status[pn]:
        # prefer design/not started/construction over disaster
        order = ['design','construction','not started','disaster']
        sts = list(projects_status[pn])
        sts_sorted = sorted(sts, key=lambda x: order.index(x) if x in order else 99)
        st = sts_sorted[0]
    else:
        # if FEMA in name, call it 'disaster recovery (FEMA)'; if emergency, 'emergency'
        if 'fema' in pn.lower():
            st = 'disaster recovery'
        elif 'emergency' in pn.lower():
            st = 'emergency'
    status_list.append(st)

if not fdf.empty:
    fdf['Status'] = status_list

# Prepare final records
records = fdf[['Project_Name','Funding_Source','Amount','Status']].sort_values(['Project_Name','Funding_Source']).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(records))"""

env_args = {'var_call_F71sEBFB8UaoSqHczyr6A7Wl': 'file_storage/call_F71sEBFB8UaoSqHczyr6A7Wl.json', 'var_call_AaC1DfsxpMM2NAKLa5RfwE3X': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
