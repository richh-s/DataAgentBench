code = """import json, re, pandas as pd

fund_fema = pd.DataFrame(var_call_Hf3GJRocvs50lXlGrBoTVMz9)
fund_fema['Amount'] = pd.to_numeric(fund_fema['Amount'], errors='coerce')

# load civic docs containing FEMA/emergency
path = var_call_trgAL8YZx921epxsqdHOUFma
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# compile set of funded project names we care about (FEMA/emergency related from funding)
proj_names = sorted(set(fund_fema['Project_Name'].dropna().tolist()))

# find status for each project by scanning docs for a line containing the project name, then looking ahead for an Updates: line
status_map = {}
for doc in docs:
    text = doc.get('text','')
    # normalize line endings
    lines = text.splitlines()
    # build index of lines lower for matching
    low_lines = [ln.lower() for ln in lines]
    for pn in proj_names:
        if pn in status_map:
            continue
        pn_low = pn.lower()
        # find any line that contains pn_low
        try:
            idxs = [i for i,ln in enumerate(low_lines) if pn_low in ln]
        except Exception:
            idxs = []
        if not idxs:
            continue
        i0 = idxs[0]
        window = lines[i0:i0+40]
        window_low = [w.lower() for w in window]
        status = None
        # heuristics
        if any('construction was completed' in w or 'notice of completion' in w for w in window_low):
            status = 'completed'
        elif any('currently under construction' in w or 'begin construction' in w for w in window_low):
            status = 'construction'
        elif any('finalizing the design' in w or 'complete design' in w or 'plans and specifications' in w or 'under review' in w for w in window_low):
            status = 'design'
        elif any('not started' in w for w in window_low):
            status = 'not started'
        else:
            # look for 'Updates:' line and take it
            for w in window:
                if re.search(r'^\s*(?:\(cid:\d+\))?\s*updates\s*:', w, flags=re.I):
                    status = 'updates provided'
                    break
        if status:
            status_map[pn] = status

# assemble result table: group fund records per project, keep multiple sources/amounts
fund_grouped = (fund_fema.groupby('Project_Name', as_index=False)
                .agg(Funding_Details=('Funding_Source', lambda s: list(s)),
                     Amounts=('Amount', lambda s: list(s))) )

rows = []
for _, r in fund_grouped.iterrows():
    pn = r['Project_Name']
    details = []
    for src, amt in zip(r['Funding_Details'], r['Amounts']):
        details.append({'Funding_Source': src, 'Amount': None if pd.isna(amt) else int(amt)})
    rows.append({
        'Project_Name': pn,
        'Status': status_map.get(pn, 'status not found in sampled civic docs'),
        'Funding': details
    })

out = json.dumps(rows, ensure_ascii=False)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_Hf3GJRocvs50lXlGrBoTVMz9': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_trgAL8YZx921epxsqdHOUFma': 'file_storage/call_trgAL8YZx921epxsqdHOUFma.json', 'var_call_eGLKxqhFFLNkxawOII9cp4WA': 'file_storage/call_eGLKxqhFFLNkxawOII9cp4WA.json', 'var_call_dFaSliyDwMY08hYsT00hNOyQ': 'file_storage/call_dFaSliyDwMY08hYsT00hNOyQ.json', 'var_call_Fw94F7mkoU8N05krCORzPU54': [{'filename': 'malibucity_agenda_03222023-2060.txt'}, {'filename': 'malibucity_agenda__01262022-1835.txt'}, {'filename': 'malibucity_agenda__01272021-1626.txt'}, {'filename': 'malibucity_agenda__03022021-1648.txt'}, {'filename': 'malibucity_agenda__03232022-1869.txt'}, {'filename': 'malibucity_agenda__03242021-1665.txt'}, {'filename': 'malibucity_agenda__04282021-1687.txt'}, {'filename': 'malibucity_agenda__05262021-1701.txt'}, {'filename': 'malibucity_agenda__06222022-1919.txt'}, {'filename': 'malibucity_agenda__06232021-1714.txt'}, {'filename': 'malibucity_agenda__06282023-2116.txt'}, {'filename': 'malibucity_agenda__07272022-1939.txt'}, {'filename': 'malibucity_agenda__07282021-1732.txt'}, {'filename': 'malibucity_agenda__08252021-1746.txt'}, {'filename': 'malibucity_agenda__09222021-1765.txt'}, {'filename': 'malibucity_agenda__09272023-2155.txt'}, {'filename': 'malibucity_agenda__10272021-1779.txt'}, {'filename': 'malibucity_agenda__11102022-1995.txt'}, {'filename': 'malibucity_agenda__12142021-1808.txt'}]}

exec(code, env_args)
