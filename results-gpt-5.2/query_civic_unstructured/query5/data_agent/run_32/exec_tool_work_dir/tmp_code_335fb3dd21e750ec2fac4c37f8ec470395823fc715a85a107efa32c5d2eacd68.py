code = """import json, re, pandas as pd

# funding map
with open(var_call_zUvUXYQoyPETIUUBoSSsfNcu,'r') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])
fund_map = dict(zip(fund_df['Project_Name'], fund_df['total_amount']))

# docs containing disaster section
with open(var_call_ldUkElZpP0kKzd5Ng24ipOpP,'r') as f:
    docs = json.load(f)

project_starts_2022 = set()

# parse disaster projects blocks: look for '(FEMA'/'CalOES'/'CalJPIA' or in disaster section, and within next lines find begin construction in 2022

def parse_disaster_section(text):
    low = text.lower()
    if 'disaster recovery projects' not in low:
        return
    sub = text[low.find('disaster recovery projects'):]
    lines = [re.sub(r'\s+',' ', ln.strip()) for ln in sub.splitlines()]
    # find candidate project names: lines that are Title Case-ish and match known funding projects by exact match if possible
    for i, ln in enumerate(lines):
        if not ln:
            continue
        # exact funding name match and contains disaster hints
        if ln in fund_map and (('fema' in ln.lower()) or ('caloes' in ln.lower()) or ('caljpia' in ln.lower()) or ('project' in ln.lower())):
            window = ' '.join(lines[i+1:i+20]).lower()
            if re.search(r'begin\s+construction\s*:\s*[^.]{0,40}2022', window) or re.search(r'begin\s*:\s*[^.]{0,40}2022', window) or re.search(r'begin\s+construction[^.]{0,40}2022', window):
                project_starts_2022.add(ln)

for d in docs:
    parse_disaster_section(d.get('text',''))

matched = {p: int(fund_map[p]) for p in sorted(project_starts_2022)}
total = int(sum(matched.values()))

print('__RESULT__:')
print(json.dumps({'total_funding': total, 'projects': matched}))"""

env_args = {'var_call_mH4Vxmvq3ReMcbXlZLykb20w': ['Funding'], 'var_call_gbjPHSa1Y6wa84bGMdSamFGX': ['civic_docs'], 'var_call_zUvUXYQoyPETIUUBoSSsfNcu': 'file_storage/call_zUvUXYQoyPETIUUBoSSsfNcu.json', 'var_call_g2qskuSxRxcFvL6Yz5EArSjM': 'file_storage/call_g2qskuSxRxcFvL6Yz5EArSjM.json', 'var_call_axAjxNHqNVE4ARWsDt9BKXyS': 'file_storage/call_axAjxNHqNVE4ARWsDt9BKXyS.json', 'var_call_ldUkElZpP0kKzd5Ng24ipOpP': 'file_storage/call_ldUkElZpP0kKzd5Ng24ipOpP.json'}

exec(code, env_args)
