code = """import json, re, pandas as pd

# Load full civic docs
path_docs = var_call_bNQRBmlUwsQjWCBZfQ9yWF7Z
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Load full funding table
path_fund = var_call_LDgAkJdsFt2igiV1IQ9snBgj
with open(path_fund, 'r') as f:
    funding = json.load(f)

# Extract project lines and infer minimal structured info
projects = []
for d in docs:
    text = d.get('text','')
    # heuristic: project lines end with 'Project' or 'Park' or 'Playground' etc., or contain 'Park'
    for line in text.split('\n'):
        line_stripped = line.strip()
        if not line_stripped:
            continue
        # consider as potential project name if it contains 'Park' or 'Playground'
        if 'Park' in line_stripped or 'Playground' in line_stripped:
            projects.append({
                'Project_Name': line_stripped,
                'topic': 'park',
                'status': 'unknown',
                'st': None,
                'et': None,
            })

# Deduplicate by Project_Name
proj_df = pd.DataFrame(projects).drop_duplicates(subset=['Project_Name'])

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Join on exact Project_Name matches
merged = fund_df.merge(proj_df, on='Project_Name', how='inner')

# Now, we must determine which of these park-related projects were completed in 2022.
# Look back into docs to find phrases like 'Construction was completed, <Month> 2022' near project names.

completed_2022_projects = set()
for d in docs:
    text = d.get('text','')
    for pname in merged['Project_Name'].unique():
        if pname in text:
            # find completion sentences near project name
            pattern = re.escape(pname) + r"[\s\S]{0,300}?Construction was completed,? ([A-Za-z]+ )?2022"
            if re.search(pattern, text):
                completed_2022_projects.add(pname)

# Filter merged to these projects
completed_2022_df = merged[merged['Project_Name'].isin(completed_2022_projects)]

total_funding = int(completed_2022_df['Amount'].sum())

result = {
    'completed_2022_park_projects': completed_2022_df[['Project_Name','Amount']].to_dict(orient='records'),
    'total_funding': total_funding
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_bNQRBmlUwsQjWCBZfQ9yWF7Z': 'file_storage/call_bNQRBmlUwsQjWCBZfQ9yWF7Z.json', 'var_call_LDgAkJdsFt2igiV1IQ9snBgj': 'file_storage/call_LDgAkJdsFt2igiV1IQ9snBgj.json'}

exec(code, env_args)
