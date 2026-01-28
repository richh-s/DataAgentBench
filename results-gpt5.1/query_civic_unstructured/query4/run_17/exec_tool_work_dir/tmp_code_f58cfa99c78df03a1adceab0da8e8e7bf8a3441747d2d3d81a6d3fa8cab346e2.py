code = """import re, json, pandas as pd

# Load full civic docs
path_civic = var_call_jpf3PNBU9WgTuB2XYBFLAOXk
with open(path_civic, 'r') as f:
    civic_docs = json.load(f)
texts = [d['text'] for d in civic_docs]
full_text = '\n'.join(texts)

# Very simple heuristic: project lines are those that look like titles followed by 'Project' or capitalized phrases
lines = [l.strip() for l in full_text.split('\n') if l.strip()]
project_names = set()
for i,l in enumerate(lines):
    if re.search(r'2022-?Spring', l, re.IGNORECASE) or 'Spring 2022' in l:
        # look around line for project name (previous non-empty line that contains 'Project' or looks like a name)
        for j in range(max(0,i-5), i+1):
            cand = lines[j]
            if len(cand.split())<=2:
                continue
            if any(word in cand for word in ['Project','Improvements','Repairs','Study','Facility','Park','Road','Bridge','Drain']):
                project_names.add(cand.strip(':'))

# also search for patterns 'Begin Construction: Spring 2022' etc and backtrack one line
for i,l in enumerate(lines):
    if re.search(r'(Begin|Complete) (Design|Construction): Spring 2022', l, re.IGNORECASE):
        for j in range(max(0,i-5), i):
            cand = lines[j]
            if any(word in cand for word in ['Project','Improvements','Repairs','Study','Facility','Park','Road','Bridge','Drain']):
                project_names.add(cand.strip(':'))

proj_list = sorted(project_names)

# Build dataframe of funding
path_fund = var_call_TXFhWC6M4jU9LJiIwYE4PvjS
with open(path_fund,'r') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

# fuzzy match by exact containment either way
matched = fund_df[fund_df['Project_Name'].apply(lambda x: any(x in p or p in x for p in proj_list))]

result = {
  'projects_started_spring_2022': len(matched),
  'total_funding': int(matched['Amount'].sum()),
  'matched_projects': matched[['Project_Name','Amount']].to_dict(orient='records')
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_jpf3PNBU9WgTuB2XYBFLAOXk': 'file_storage/call_jpf3PNBU9WgTuB2XYBFLAOXk.json', 'var_call_TXFhWC6M4jU9LJiIwYE4PvjS': 'file_storage/call_TXFhWC6M4jU9LJiIwYE4PvjS.json'}

exec(code, env_args)
