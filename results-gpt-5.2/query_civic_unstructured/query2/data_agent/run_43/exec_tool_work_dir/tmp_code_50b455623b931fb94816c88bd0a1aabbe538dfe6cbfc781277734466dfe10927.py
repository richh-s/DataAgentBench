code = """import json, re, pandas as pd

# Load civic docs (2022 filenames)
path_docs = var_call_fNGMQN7rsGT753P1DhDoSjRg
if isinstance(path_docs, str):
    with open(path_docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = path_docs

# Load funding totals by project
path_fund = var_call_i24rwJefKrIAwf8WGY46Fd1j
if isinstance(path_fund, str):
    with open(path_fund, 'r', encoding='utf-8') as f:
        fund = json.load(f)
else:
    fund = path_fund
fund_df = pd.DataFrame(fund)
# coerce to numeric
fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

texts = [d.get('text','') for d in docs]
all_text = "\n".join(texts)

# Extract the block of completed capital improvement projects if present
completed_block = ""
m = re.search(r"Capital Improvement Projects \(Completed\)(.*?)(?:Disaster Projects \(|\Z)", all_text, flags=re.S|re.I)
if m:
    completed_block = m.group(1)
else:
    # fallback: use whole text
    completed_block = all_text

# Candidate project names are those in funding table containing park-related keywords
park_keywords = [r"\bpark\b", r"playground", r"skate", r"bluffs", r"legacy park", r"trancas canyon park", r"point dume"]
kw_re = re.compile("|".join(park_keywords), flags=re.I)
park_projects = fund_df[fund_df['Project_Name'].fillna('').str.contains(kw_re, regex=True)].copy()

# Determine which of these are completed in 2022 documents:
# A project is considered completed if its name appears in completed_block.
# (This relies on 2022 agenda docs containing the completed list.)
completed_mask = park_projects['Project_Name'].apply(lambda n: re.search(re.escape(str(n)), completed_block, flags=re.I) is not None)
completed_park_projects = park_projects[completed_mask].copy()

# Additionally ensure completion pertains to 2022: we already filtered to 2022 filenames; the completed section referenced acceptance/complete in 2022 docs.

total_funding = int(completed_park_projects['total_amount'].sum())

result = {
    "total_funding": total_funding,
    "completed_park_projects": completed_park_projects[['Project_Name','total_amount']].sort_values('Project_Name').to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_iY9iEMBFD1F9AEybuTddJbwP': ['Funding'], 'var_call_t17aCCEPYBdI8yfkojzgW6Zc': ['civic_docs'], 'var_call_fNGMQN7rsGT753P1DhDoSjRg': 'file_storage/call_fNGMQN7rsGT753P1DhDoSjRg.json', 'var_call_i24rwJefKrIAwf8WGY46Fd1j': 'file_storage/call_i24rwJefKrIAwf8WGY46Fd1j.json'}

exec(code, env_args)
