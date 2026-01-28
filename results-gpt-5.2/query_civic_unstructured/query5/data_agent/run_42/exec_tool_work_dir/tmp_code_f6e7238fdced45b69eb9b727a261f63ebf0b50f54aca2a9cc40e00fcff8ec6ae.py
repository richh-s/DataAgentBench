code = """import json, re, pandas as pd

def load(v):
    if isinstance(v,str) and v.endswith('.json'):
        with open(v,'r',encoding='utf-8') as f:
            return json.load(f)
    return v

docs = load(var_call_RbRJ8B3zhalu7ZZLemeKNatP)
fund = load(var_call_RJmqRBDb3cvzpVjDNrgMt7U5)

begin_re = re.compile(r'Begin\s+Construction\s*:\s*(.+)$', re.I)

started_2022=set()

for d in docs:
    text=d.get('text','') or ''
    lines=text.splitlines()
    in_disaster=False
    current=None
    for ln in lines:
        ls=ln.strip()
        if re.match(r'^Disaster Projects', ls, re.I) or re.match(r'^Disaster Recovery Projects', ls, re.I):
            in_disaster=True
            current=None
            continue
        if in_disaster and re.match(r'^Capital Improvement Projects', ls, re.I):
            in_disaster=False
            current=None
            continue
        if not in_disaster or not ls:
            continue
        if ls.lower().startswith('page ') or ls.lower().startswith('agenda item'):
            continue
        if (not ls.endswith(':')) and (not ls.startswith('(cid:')):
            if len(ls)<=180 and ls not in ['Discussion','Recommended Action','RECOMMENDED ACTION']:
                if re.search(r'(Project|Repairs|Repair|Improvements|Improvement|Slope|Culvert|Bridge|Drain|Storm|Warning|Fire|FEMA|CalOES|CalJPIA)', ls, re.I):
                    current=re.sub(r'\s+',' ',ls).strip()
                    continue
        if ls.startswith('(cid:') and current:
            m=begin_re.search(ls)
            if m and '2022' in m.group(1):
                started_2022.add(current)

fund_df=pd.DataFrame(fund)
fund_df['total_amount']=pd.to_numeric(fund_df['total_amount'])
matched=fund_df[fund_df['Project_Name'].isin(started_2022)]

out={'started_2022_projects':sorted(started_2022),'num_projects':int(matched.shape[0]),'total_funding':int(matched['total_amount'].sum()),'matched_projects':matched.sort_values('Project_Name').to_dict(orient='records')}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_mImfOvDqjEWwtbOEFHa6RwO8': ['Funding'], 'var_call_zek2GZ6YL608W3ghopgfCLDJ': ['civic_docs'], 'var_call_gzsZiU7wXQyH4mWQvV7OHFPc': 'file_storage/call_gzsZiU7wXQyH4mWQvV7OHFPc.json', 'var_call_RJmqRBDb3cvzpVjDNrgMt7U5': 'file_storage/call_RJmqRBDb3cvzpVjDNrgMt7U5.json', 'var_call_qceswyg6XTHns5RKII4iNCGr': {'total_funding': 0, 'num_projects': 0, 'projects': [], 'started_2022_projects': []}, 'var_call_n3fmCyRhoVAGCf9wMSQmOlQO': 'file_storage/call_n3fmCyRhoVAGCf9wMSQmOlQO.json', 'var_call_MxNYKUBIYTrnSbirgumg29F9': [{'line_index': 27, 'context': ['', 'Subject:', '', 'Capital Improvement Projects and Disaster Recovery Projects Status', 'Report', '', 'RECOMMENDED ACTION: Receive and file report on the status of the City’s current and', 'upcoming Capital Improvement Projects and Disaster Recovery Projects.', '', 'DISCUSSION: Staff will provide a status update on the following active projects in the', 'Fiscal Year 2022-2023 Capital Improvement Program:']}, {'line_index': 31, 'context': ['Report', '', 'RECOMMENDED ACTION: Receive and file report on the status of the City’s current and', 'upcoming Capital Improvement Projects and Disaster Recovery Projects.', '', 'DISCUSSION: Staff will provide a status update on the following active projects in the', 'Fiscal Year 2022-2023 Capital Improvement Program:', '', 'Capital Improvement Projects (Design)', '', '2022 Morning View Resurfacing & Storm Drain Improvements']}], 'var_call_n8mdHkfFU40mkjnRdAjCbC5G': 'file_storage/call_n8mdHkfFU40mkjnRdAjCbC5G.json', 'var_call_UUzUq0TekANQfvjxqk2E19vq': {'started_2022_projects': [], 'total_funding': 0, 'num_projects': 0}, 'var_call_RbRJ8B3zhalu7ZZLemeKNatP': 'file_storage/call_RbRJ8B3zhalu7ZZLemeKNatP.json'}

exec(code, env_args)
