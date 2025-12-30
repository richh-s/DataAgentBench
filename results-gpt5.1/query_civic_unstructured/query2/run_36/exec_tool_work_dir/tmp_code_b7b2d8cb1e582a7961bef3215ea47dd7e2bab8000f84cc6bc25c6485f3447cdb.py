code = """import re, json, pandas as pd, os, textwrap

# Load full civic docs
path_docs = var_call_iWi9L0pIyW3kzTvnOuzFx6oY
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Load funding
funding_records = var_call_lCrjo2F1ooN20zovS4hUkEzP
funding_df = pd.DataFrame(funding_records)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Very heuristic extraction: find project lines and possible status/completion year
projects = []
for doc in docs:
    text = doc.get('text','')
    # Split into lines
    lines = text.split('\n')
    for line in lines:
        clean = line.strip()
        if not clean:
            continue
        # consider lines that look like project titles (no colon, some keywords)
        if len(clean) > 200:
            continue
        # Simple heuristic: Title case-ish and contains keywords like Park
        if 'park' in clean.lower():
            projects.append(clean)

unique_projects = sorted(set(projects))

# Now, for each project name, try to find completion info with year 2022 in the nearby text
completed_2022_projects = set()
for doc in docs:
    text = doc.get('text','')
    lower = text.lower()
    for pname in unique_projects:
        if pname.lower() in lower:
            # find occurrences
            for m in re.finditer(re.escape(pname.lower()), lower):
                start = max(0, m.start()-300)
                end = min(len(text), m.end()+300)
                context = text[start:end]
                if 'completed' in context.lower() and '2022' in context:
                    completed_2022_projects.add(pname)

# Match these to funding by exact project name matches or substring matches
matched_funding = funding_df[funding_df['Project_Name'].apply(lambda n: any(p in n for p in completed_2022_projects))]

total_funding = int(matched_funding['Amount'].sum())

result = {
    'completed_2022_park_projects': sorted(list(completed_2022_projects)),
    'matched_funding_records': matched_funding.to_dict(orient='records'),
    'total_funding': total_funding
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_iWi9L0pIyW3kzTvnOuzFx6oY': 'file_storage/call_iWi9L0pIyW3kzTvnOuzFx6oY.json', 'var_call_lCrjo2F1ooN20zovS4hUkEzP': 'file_storage/call_lCrjo2F1ooN20zovS4hUkEzP.json', 'var_call_Cbe41LeF08wqZq0Z9ZrtLh8D': ['civic_docs'], 'var_call_HN7nfpLdkxIBXEJO8OZDf9Q2': ['Funding']}

exec(code, env_args)
