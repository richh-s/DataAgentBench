code = """import json, re, pandas as pd

# Load civic docs result (possibly stored as file path)
docs_src = var_call_Gp9ge0OUP5Bi77FG2n444Dtx
if isinstance(docs_src, str) and docs_src.endswith('.json'):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

funding = var_call_gqehXOTzyRnJkMpNAbKviAFC

def parse_projects(text):
    projects = {}
    lines = [ln.rstrip() for ln in text.splitlines()]
    # find headings for status sections
    status = None
    for i, ln in enumerate(lines):
        s = ln.strip()
        s_low = s.lower()
        if re.search(r'capital improvement projects \(design\)', s_low):
            status = 'design'
            continue
        if re.search(r'capital improvement projects \(construction\)', s_low):
            status = 'construction'
            continue
        if re.search(r'capital improvement projects \(not started\)', s_low):
            status = 'not started'
            continue
        if re.search(r'disaster recovery projects', s_low):
            # next projects are disaster; status varies; keep current unless later specified
            status = status or 'unknown'
            continue

        # project name heuristic: non-empty, not bullet, title case-ish, and not too long
        if status and s and len(s) < 120 and not s.startswith('(') and not s.startswith('cid') and not s_low.startswith('page ') and 'updates' not in s_low and 'project schedule' not in s_low and 'estimated schedule' not in s_low and 'project description' not in s_low:
            # require contains a letter and not end with ':'
            if re.search(r'[A-Za-z]', s) and not s.endswith(':'):
                # capture only if subsequent lines contain Updates or Project Description or Schedule soon
                window = "\n".join(lines[i:i+8]).lower()
                if ('updates' in window) or ('project description' in window) or ('project schedule' in window) or ('estimated schedule' in window):
                    if s not in projects:
                        projects[s] = {'Project_Name': s, 'Status': status}
    return list(projects.values())

projects = []
for d in docs:
    projects.extend(parse_projects(d.get('text','')))

proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name'])

fund_df = pd.DataFrame(funding)
if not fund_df.empty:
    fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce')

# filter projects related to emergency/FEMA by name match with funding list OR keyword in name
pat = re.compile(r'(\bemergency\b|\bFEMA\b)', re.I)
proj_df['is_emergency'] = proj_df['Project_Name'].apply(lambda x: bool(pat.search(str(x))))

# Join funding info
out = fund_df.merge(proj_df[['Project_Name','Status']], on='Project_Name', how='left')
# If any emergency projects in docs not in funding, include them with null funding
extra = proj_df[proj_df['is_emergency'] & ~proj_df['Project_Name'].isin(fund_df['Project_Name'] if not fund_df.empty else [])]
if not extra.empty:
    extra_out = extra[['Project_Name','Status']].copy()
    extra_out['Funding_Source'] = None
    extra_out['Amount'] = None
    out = pd.concat([out, extra_out[['Project_Name','Funding_Source','Amount','Status']]], ignore_index=True)

out = out[['Project_Name','Funding_Source','Amount','Status']].sort_values(['Project_Name','Funding_Source'], na_position='last')
result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Gp9ge0OUP5Bi77FG2n444Dtx': 'file_storage/call_Gp9ge0OUP5Bi77FG2n444Dtx.json', 'var_call_gqehXOTzyRnJkMpNAbKviAFC': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
