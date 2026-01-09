code = """import json, re, pandas as pd

def load_tool_result(x):
    if isinstance(x, str) and x.endswith('.json'):
        with open(x,'r',encoding='utf-8') as f:
            return json.load(f)
    return x

docs = load_tool_result(var_call_UCJq4gDEzfiZVQPH44VuWTPI)
fund = load_tool_result(var_call_QZtCO6cQtvO8QTD4wdb2dF3L)

def extract(text):
    lines=[ln.strip() for ln in text.splitlines()]
    projects=set()
    for i,ln in enumerate(lines):
        if re.search(r'construction was completed', ln, re.I) and re.search(r'2022', ln):
            # back to project title
            j=i-1
            while j>=0 and (not lines[j] or re.search(r'\(cid:|^Updates|^Project Schedule|^Estimated Schedule|^Capital Improvement Projects|^Disaster Recovery Projects|^Page \d+|^Agenda Item', lines[j], re.I)):
                j-=1
            if j>=0:
                name=lines[j]
                window=' '.join(lines[max(0,j-3):min(len(lines), i+3)])
                if re.search(r'\bpark\b', window, re.I):
                    projects.add(name)
    return projects

park_completed_2022=set()
for d in docs:
    park_completed_2022 |= extract(d.get('text',''))

fund_df=pd.DataFrame(fund)
fund_df['total_amount']=pd.to_numeric(fund_df['total_amount'])
matched=fund_df[fund_df['Project_Name'].isin(sorted(park_completed_2022))]

total=int(matched['total_amount'].sum())
res={'projects':sorted(park_completed_2022),'total_funding':total,'matched':matched.to_dict(orient='records')}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_hXf50YBfCrrwm4VISQMICNsZ': ['Funding'], 'var_call_SxtnxuThncsmTRlN1JT8h0Dx': ['civic_docs'], 'var_call_UCJq4gDEzfiZVQPH44VuWTPI': 'file_storage/call_UCJq4gDEzfiZVQPH44VuWTPI.json', 'var_call_QZtCO6cQtvO8QTD4wdb2dF3L': 'file_storage/call_QZtCO6cQtvO8QTD4wdb2dF3L.json', 'var_call_daScurDCWm3lCH5Z7VUW1soU': {'projects_completed_2022_park': [], 'matched_projects': [], 'total_funding': 0}, 'var_call_jx825yvGj5t1RO9j1r5BxfCm': [{'i': 137, 'line': '(cid:131) Plans and specifications have been completed', 'context': ['(cid:190) Updates:', '', '(cid:131) Plans and specifications have been completed', '(cid:131) Awaiting final FEMA/CalOES approval for scope modification', '']}, {'i': 149, 'line': '(cid:131) Field data collection has been completed and storm drain inventory has', 'context': ['(cid:190) Updates:', '', '(cid:131) Field data collection has been completed and storm drain inventory has', '', 'been finalized and incorporated into GIS.']}, {'i': 314, 'line': '(cid:190) Updates: Construction was completed November 2022. Notice of completion', 'context': ['Bluffs Park Shade Structure', '', '(cid:190) Updates: Construction was completed November 2022. Notice of completion', '', 'filed January 2023']}, {'i': 335, 'line': '(cid:131) Construction was completed, January 2023', 'context': ['(cid:190) Updates:', '', '(cid:131) Construction was completed, January 2023', '(cid:131) Scheduled for Council acceptance on April 24, 2023', '']}, {'i': 342, 'line': '(cid:131) Construction was completed, November 2022', 'context': ['(cid:190) Updates:', '', '(cid:131) Construction was completed, November 2022', '(cid:131) Notice of completion filed January 2023', '']}, {'i': 348, 'line': '(cid:131) Construction was completed, November 2022', 'context': ['(cid:190) Updates:', '', '(cid:131) Construction was completed, November 2022', '(cid:131) Notice of completion filed January 2023', '']}]}

exec(code, env_args)
