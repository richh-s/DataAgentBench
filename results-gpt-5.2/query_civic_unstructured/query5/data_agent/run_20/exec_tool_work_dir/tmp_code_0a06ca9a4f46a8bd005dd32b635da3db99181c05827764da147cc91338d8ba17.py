code = """import json, re, pandas as pd

path = var_call_lgQzBPI1GW1CUv0bwkSRuNj2
with open(path, 'r') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])

path2 = var_call_kD0HQUvbN7JFMNHrDSHvWWAr
with open(path2, 'r') as f:
    docs = json.load(f)

project_info = {}

def normalize_space(s):
    return re.sub(r'\s+', ' ', s).strip()

def extract_from_text(text):
    lines = [l.strip() for l in text.splitlines()]
    for i, line in enumerate(lines):
        if not line:
            continue
        if line.startswith('(') or line.lower().startswith('page ') or line.lower().startswith('agenda'):
            continue
        if line.lower() in {'recommended action','discussion','public works commission','agenda report'}:
            continue
        if line.endswith(':'):
            continue
        look = ' '.join([lines[j].lower() for j in range(i+1, min(i+8, len(lines))) if lines[j]])
        if ('updates' in look) and ('schedule' in look or 'begin construction' in look or 'advertise' in look or 'complete design' in look):
            name = normalize_space(line)
            block = "\n".join(lines[i:i+25])
            st = None
            m = re.search(r'(?i)(begin construction|start|advertise|final design|complete design)\s*[:\-]\s*([^\n]{0,60}2022[^\n]{0,60})', block)
            if m:
                st = normalize_space(m.group(2))
            else:
                m2 = re.search(r'(2022[^\n]{0,30})', block)
                if m2:
                    st = normalize_space(m2.group(1))
            is_disaster = bool(re.search(r'(?i)\bdisaster\b|fema|caloes|caljpia', block + ' ' + name))
            typ = 'disaster' if is_disaster else 'capital'
            return name, typ, st
    return None

for d in docs:
    res = extract_from_text(d.get('text',''))
    if res:
        name, typ, st = res
        if name not in project_info:
            project_info[name] = {'type': typ, 'st': st}
        else:
            if project_info[name]['type'] != 'disaster' and typ=='disaster':
                project_info[name]['type'] = 'disaster'
            if (project_info[name].get('st') is None) and st is not None:
                project_info[name]['st'] = st

proj_df = pd.DataFrame([{'Project_Name':k, 'type':v.get('type'), 'st':v.get('st')} for k,v in project_info.items()])

dis_2022 = proj_df[(proj_df['type']=='disaster') & (proj_df['st'].fillna('').str.contains('2022'))]
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
