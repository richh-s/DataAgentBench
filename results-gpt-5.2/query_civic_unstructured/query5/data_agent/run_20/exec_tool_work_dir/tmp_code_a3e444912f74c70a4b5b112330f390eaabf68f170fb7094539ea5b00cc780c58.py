code = """import json, re, pandas as pd

# load funding by project
path = var_call_lgQzBPI1GW1CUv0bwkSRuNj2
with open(path, 'r') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])

# load civic docs
path2 = var_call_kD0HQUvbN7JFMNHrDSHvWWAr
with open(path2, 'r') as f:
    docs = json.load(f)

project_info = {}  # name -> {'type':..., 'st':...}

# regex to find project blocks with schedule lines
# We'll extract lines between a project title line and next blank/title.
# Project title heuristics: line with letters and not too long and not bullets, followed by blank or 'Updates' etc.

def normalize_space(s):
    return re.sub(r'\s+', ' ', s).strip()

def extract_from_text(text):
    lines = [l.strip() for l in text.splitlines()]
    # keep non-empty lines for scanning
    for i, line in enumerate(lines):
        if not line:
            continue
        # identify a project name line: not start with '(' or 'cid', not all caps headers, length reasonable
        if line.startswith('(') or line.lower().startswith('page ') or line.lower().startswith('agenda'):
            continue
        if line.lower() in {'recommended action','discussion','public works commission','agenda report'}:
            continue
        if line.endswith(':'):
            continue
        # likely project name if next few lines contain 'Updates' or 'Project Schedule' or 'Estimated Schedule'
        look = ' '.join([lines[j].lower() for j in range(i+1, min(i+8, len(lines))) if lines[j]])
        if ('updates' in look) and ('schedule' in look or 'begin construction' in look or 'advertise' in look or 'complete design' in look):
            name = normalize_space(line)
            # gather a block of next 20 lines
            block = '\n'.join(lines[i:i+25])
            # find start time as first occurrence of a 2022 in schedule lines
            st = None
            m = re.search(r'(?i)(begin construction|start|advertise|final design|complete design)\s*[:\-]\s*([^\n]{0,60}2022[^\n]{0,60})', block)
            if m:
                st = normalize_space(m.group(2))
            else:
                # any 2022 token in block near schedule
                m2 = re.search(r'(2022[^\n]{0,30})', block)
                if m2:
                    st = normalize_space(m2.group(1))
            # determine type disaster if FEMA/CalOES/CalJPIA/disaster mentioned in block or name
            is_disaster = bool(re.search(r'(?i)\bdisaster\b|fema|caloes|caljpia', block + ' ' + name))
            typ = 'disaster' if is_disaster else 'capital'
            return name, typ, st
    return None

for d in docs:
    res = extract_from_text(d.get('text',''))
    if res:
        name, typ, st = res
        # keep first st if exists; prioritize one containing 2022
        if name not in project_info:
            project_info[name] = {'type': typ, 'st': st}
        else:
            # update type to disaster if any mention
            if project_info[name]['type'] != 'disaster' and typ=='disaster':
                project_info[name]['type'] = 'disaster'
            # update st if current missing and new present
            if (project_info[name].get('st') is None) and st is not None:
                project_info[name]['st'] = st

proj_df = pd.DataFrame([{'Project_Name':k, 'type':v.get('type'), 'st':v.get('st')} for k,v in project_info.items()])

# Filter to disaster and started in 2022: st contains '2022'
dis_2022 = proj_df[(proj_df['type']=='disaster') & (proj_df['st'].fillna('').str.contains('2022'))]

# join with funding totals
merged = dis_2022.merge(fund_df, on='Project_Name', how='inner')

total = int(merged['total_amount'].sum())

out = {
    'total_funding_disaster_projects_started_2022': total,
    'matched_projects_count': int(len(merged)),
    'matched_projects': merged[['Project_Name','st','total_amount']].sort_values('Project_Name').to_dict(orient='records')
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_AANdMbvLJ8dHbieBcxTKvsNY': ['Funding'], 'var_call_Th2Urt5XiWHHxMjZkGfStPZG': ['civic_docs'], 'var_call_lgQzBPI1GW1CUv0bwkSRuNj2': 'file_storage/call_lgQzBPI1GW1CUv0bwkSRuNj2.json', 'var_call_kD0HQUvbN7JFMNHrDSHvWWAr': 'file_storage/call_kD0HQUvbN7JFMNHrDSHvWWAr.json'}

exec(code, env_args)
