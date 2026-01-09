code = """import json, re, pandas as pd

path_docs=var_call_bRlNzZZ72IqhjANul1A5ti3D
with open(path_docs,'r',encoding='utf-8') as f:
    docs=json.load(f)

projects=[]
for d in docs:
    lines=[ln.strip() for ln in d.get('text','').splitlines()]
    current_status=None
    for i,ln in enumerate(lines):
        m=re.search(r'\bCapital Improvement Projects\s*\((Design|Construction|Not Started)\)', ln, re.IGNORECASE)
        if m:
            current_status=m.group(1).strip().lower()
            continue
        if current_status and ln and len(ln)<140:
            low=ln.lower()
            if low.startswith(('(cid:','updates','project schedule','recommended action','discussion','page','agenda item','to:','prepared','approved','date prepared','meeting date','subject')):
                continue
            if re.search(r'\bprojects\b', ln, re.IGNORECASE):
                continue
            window=' '.join(lines[i+1:i+10]).lower()
            if ('updates' in window) or ('project schedule' in window) or ('project description' in window) or ('estimated schedule' in window):
                projects.append({'Project_Name':ln,'status':current_status,'context':' '.join(lines[i:i+25]),'filename':d.get('filename')})

proj_df=pd.DataFrame(projects)

park_mask = proj_df['Project_Name'].str.contains(r'park|playground|bluffs', case=False, na=False) | proj_df['context'].str.contains(r'\bpark\b|playground|bluffs', case=False, na=False)
proj_df=proj_df[park_mask].copy()
completed_2022 = proj_df['context'].str.contains(r'completed[^.]*2022', case=False, na=False)
proj_df=proj_df[completed_2022].copy()

path_fund=var_call_tSW7bYfRh9pqlIqOF2V66jZM
with open(path_fund,'r',encoding='utf-8') as f:
    fund=json.load(f)
fund_df=pd.DataFrame(fund)
fund_df['total_amount']=pd.to_numeric(fund_df['total_amount'])

merged=proj_df.merge(fund_df,on='Project_Name',how='inner')

out={'total_funding': int(merged['total_amount'].sum()),
     'projects': merged[['Project_Name','total_amount']].drop_duplicates().sort_values('Project_Name').to_dict(orient='records')}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_EwJRJJ2BDH1bM1CyPdScGWSH': ['Funding'], 'var_call_y86nrVdqSPdR9vmjn1tZzarh': ['civic_docs'], 'var_call_bRlNzZZ72IqhjANul1A5ti3D': 'file_storage/call_bRlNzZZ72IqhjANul1A5ti3D.json', 'var_call_tSW7bYfRh9pqlIqOF2V66jZM': 'file_storage/call_tSW7bYfRh9pqlIqOF2V66jZM.json', 'var_call_9wzPbJn4pIo9IAPXQeBcNCYw': {'doc_count': 19, 'sample_keys': ['filename', 'text']}, 'var_call_EmngWz2UM1sSupaha8csJxcu': {'rows': 0, 'cols': [], 'head': []}, 'var_call_FZY50vlgyNKOysQy9D5bHi50': {'filename': 'malibucity_agenda_03222023-2060.txt', 'hits': ['Capital Improvement Projects and Disaster Recovery Projects Status', 'upcoming Capital Improvement Projects and Disaster Recovery Projects.', 'Fiscal Year 2022-2023 Capital Improvement Program:', 'Capital Improvement Projects (Design)', 'Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)']}, 'var_call_sI22QuRPBttwk9tYwUBZxNKb': {'filename': 'malibucity_agenda_03222023-2060.txt', 'segment': ['Capital Improvement Projects (Construction)', '', 'Malibu Road Slope Repairs', '', '(cid:190) Updates: Project is currently under construction', '(cid:190) Complete Construction: April 2023', '', 'Encinal Canyon Road Repairs', '', '(cid:190) Updates: Project is currently under construction', '(cid:190) Complete Construction: Summer 2023', '', 'PCH Signal Synchronization System Improvements Project', '', '(cid:190) Updates:', '', '(cid:131) On February 27, 2023, City Council awarded the contract to GMZ', '', 'Engineering, Inc.', '', '(cid:190) Project Schedule:', '', '(cid:131) Begin construction: April 2023', '(cid:131) Complete Construction: Summer 2025', '', 'Storm Drain Trash Screens Phase Two', '', '(cid:190) Updates:', '', '(cid:131) Project is currently out to bid. Bids are due on March 23, 2023.', '', '(cid:190) Project Schedule:', '', '(cid:131) Begin construction: Summer 2023', '(cid:131) Complete Construction: Summer 2023', '', 'Bluffs Park Shade Structure', '', '(cid:190) Updates: Construction was completed November 2022. Notice of completion', '', 'filed January 2023', '', 'Page 4 of 6', '', 'Agenda Item # 4.B.', '', '', '', '', '', '', '', '', '', '', '', 'Marie Canyon Green Streets', '(cid:190) Updates:', '', '(cid:131) Construction was completed, January 2023', '(cid:131) Scheduled for Council acceptance on April 24, 2023', '', 'Broad Beach Road Water Quality Repair', '', '(cid:190) Updates:', '', '(cid:131) Construction was completed, November 2022', '(cid:131) Notice of completion filed January 2023', '', 'Point Dume Walkway Repairs', '(cid:190) Updates:', '', '(cid:131) Construction was completed, November 2022', '(cid:131) Notice of completion filed January 2023', '', 'Capital Improvement Projects (Not Started)', '', 'PCH Median Improvements at Paradise Cove and Zuma Beach', '', '(cid:190) Project Description: This project was identified in the 2015 PCH Safety Study']}}

exec(code, env_args)
