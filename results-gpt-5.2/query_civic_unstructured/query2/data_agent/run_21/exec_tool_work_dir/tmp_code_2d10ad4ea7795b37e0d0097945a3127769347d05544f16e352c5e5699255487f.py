code = """import json, re
import pandas as pd

# load civic docs
path_docs = var_call_bRlNzZZ72IqhjANul1A5ti3D
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# parse projects from docs: use section headings as status markers
statuses = ["Design","Construction","Not Started"]

def norm_status(s):
    s=s.strip().lower()
    if s=="design": return "design"
    if s=="construction": return "construction"
    if s=="not started": return "not started"
    return s

# Heuristic parse: look for blocks after each heading like "Capital Improvement Projects (Construction)"
projects=[]
for d in docs:
    text=d.get('text','')
    # Split into lines
    lines=[ln.strip() for ln in text.splitlines()]
    current_status=None
    for i,ln in enumerate(lines):
        m=re.search(r'\bCapital Improvement Projects\s*\((Design|Construction|Not Started)\)', ln, re.IGNORECASE)
        if m:
            current_status=norm_status(m.group(1))
            continue
        # project name lines tend to be standalone and followed by bullet "Updates" within next few lines
        if current_status and ln and len(ln)<120 and not ln.lower().startswith(('updates','project schedule','recommended action','discussion','page','agenda item','#','to:','prepared','approved','date prepared','meeting date','subject')):
            # exclude headings
            if re.search(r'\bprojects\b', ln, re.IGNORECASE):
                continue
            # determine if next few lines contain 'Updates' or 'Project Schedule' or 'Project Description'
            window=' '.join(lines[i+1:i+8]).lower()
            if ('updates' in window) or ('project schedule' in window) or ('project description' in window) or ('estimated schedule' in window):
                pname=ln
                # extract completion date if mentioned nearby
                win2=' '.join(lines[i:i+15])
                comp=None
                m2=re.search(r'completed\s+(?:construction\s+)?(?:was\s+)?completed\s*(?:,|:)\s*([A-Za-z]+\s+\d{4}|\w+\s+\d{4}|\w+\s+\d{1,2},\s*\d{4})', win2, re.IGNORECASE)
                if m2:
                    comp=m2.group(1)
                else:
                    m3=re.search(r'Construction was completed\s+([A-Za-z]+\s+\d{4})', win2, re.IGNORECASE)
                    if m3:
                        comp=m3.group(1)
                projects.append({'Project_Name':pname,'status':current_status,'context':win2,'filename':d.get('filename'),'completion_text':comp})

# de-duplicate keeping most informative
proj_df=pd.DataFrame(projects).drop_duplicates(subset=['Project_Name','status'])

# Determine park-related: project name or context contains keyword park/playground/bluffs
park_mask = proj_df['Project_Name'].str.contains(r'park|playground|bluffs', case=False, na=False) | proj_df['context'].str.contains(r'\bpark\b|playground|bluffs', case=False, na=False)
proj_df=proj_df[park_mask].copy()

# Determine completed in 2022: either status is construction and context mentions completed ... 2022, or context has 'November 2022' etc.
completed_2022 = proj_df['context'].str.contains(r'completed[^\n]*2022|Construction was completed[^\n]*2022', case=False, na=False)
proj_df=proj_df[completed_2022].copy()

# load funding per project
path_fund = var_call_tSW7bYfRh9pqlIqOF2V66jZM
with open(path_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)
fund_df=pd.DataFrame(fund)
fund_df['total_amount']=pd.to_numeric(fund_df['total_amount'])

merged=proj_df.merge(fund_df, on='Project_Name', how='inner')

answer_total=int(merged['total_amount'].sum())

out={
    'total_funding': answer_total,
    'projects': merged[['Project_Name','total_amount','filename']].drop_duplicates().sort_values('Project_Name').to_dict(orient='records')
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_EwJRJJ2BDH1bM1CyPdScGWSH': ['Funding'], 'var_call_y86nrVdqSPdR9vmjn1tZzarh': ['civic_docs'], 'var_call_bRlNzZZ72IqhjANul1A5ti3D': 'file_storage/call_bRlNzZZ72IqhjANul1A5ti3D.json', 'var_call_tSW7bYfRh9pqlIqOF2V66jZM': 'file_storage/call_tSW7bYfRh9pqlIqOF2V66jZM.json'}

exec(code, env_args)
