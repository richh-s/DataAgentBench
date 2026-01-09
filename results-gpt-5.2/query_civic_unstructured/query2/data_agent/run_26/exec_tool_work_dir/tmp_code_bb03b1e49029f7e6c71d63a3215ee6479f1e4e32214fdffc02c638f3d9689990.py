code = """import json, re, pandas as pd

def load_tool_result(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x,'r',encoding='utf-8') as f:
            return json.load(f)
    return x

docs = load_tool_result(var_call_UCJq4gDEzfiZVQPH44VuWTPI)
fund = load_tool_result(var_call_QZtCO6cQtvO8QTD4wdb2dF3L)

def extract_completed_2022_park_projects(text):
    lines = [ln.strip() for ln in text.splitlines()]
    projects = set()
    for i,ln in enumerate(lines):
        if not ln:
            continue
        # detect completion statements containing 2022
        if re.search(r'completed', ln, re.I) and re.search(r'2022', ln):
            # look back for project name (nearest previous non-empty line, avoid headings)
            j = i-1
            while j>=0 and (not lines[j] or re.search(r'^(Updates|Project Schedule|Estimated Schedule|Capital Improvement Projects|Disaster Recovery Projects|Page \d+|Agenda Item|\(cid:)', lines[j], re.I)):
                j -= 1
            if j>=0:
                name = lines[j]
                # filter obvious non-project phrases
                if len(name) > 3 and not re.search(r'^(To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|RECOMMENDED ACTION|DISCUSSION)', name, re.I):
                    # park-related if name or nearby context has park
                    window = ' '.join(lines[max(0,j-3):min(len(lines), i+3)])
                    if re.search(r'\bpark\b', window, re.I):
                        projects.add(name)
    return projects

park_completed_2022 = set()
for d in docs:
    park_completed_2022 |= extract_completed_2022_park_projects(d.get('text',''))

# Join to funding totals by exact match
fund_df = pd.DataFrame(fund)
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'])
completed_names = sorted(park_completed_2022)
matched = fund_df[fund_df['Project_Name'].isin(completed_names)]

result = {
    'projects_completed_2022_park': completed_names,
    'matched_projects': matched.to_dict(orient='records'),
    'total_funding': int(matched['total_amount'].sum())
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_hXf50YBfCrrwm4VISQMICNsZ': ['Funding'], 'var_call_SxtnxuThncsmTRlN1JT8h0Dx': ['civic_docs'], 'var_call_UCJq4gDEzfiZVQPH44VuWTPI': 'file_storage/call_UCJq4gDEzfiZVQPH44VuWTPI.json', 'var_call_QZtCO6cQtvO8QTD4wdb2dF3L': 'file_storage/call_QZtCO6cQtvO8QTD4wdb2dF3L.json'}

exec(code, env_args)
