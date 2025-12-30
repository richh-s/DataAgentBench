code = """import re, json, pandas as pd

path_docs = var_call_dzAmbL820r2mzYlvgOcJfIOQ
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

path_fund = var_call_v3lEntZgSJ801nDZAVOpAoi4
with open(path_fund, 'r') as f:
    funding = json.load(f)

park_keywords = ['park']

park_projects_2022 = set()

for doc in civic_docs:
    lines = doc.get('text','').split('\n')
    for i, line in enumerate(lines):
        if 'Construction was completed' in line and '2022' in line:
            j = i-1
            while j >= 0 and not lines[j].strip():
                j -= 1
            if j >= 0:
                pname = lines[j].strip()
                if any(k in pname.lower() for k in park_keywords):
                    park_projects_2022.add(pname)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

fund_total = 0
matched_projects = []

for pname in park_projects_2022:
    pname_low = pname.lower()
    matches = fund_df[fund_df['Project_Name'].str.lower() == pname_low]
    if matches.empty:
        matches = fund_df[fund_df['Project_Name'].str.lower().str.contains(pname_low)]
    if matches.empty:
        matches = fund_df[fund_df['Project_Name'].str.lower().apply(lambda x: pname_low in x or x in pname_low)]
    if not matches.empty:
        amt = matches['Amount'].sum()
        fund_total += int(amt)
        matched_projects.extend(matches['Project_Name'].tolist())

result = {
    'park_projects_completed_2022': sorted(list(park_projects_2022)),
    'matched_funding_projects': sorted(list(set(matched_projects))),
    'total_funding': int(fund_total)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_dzAmbL820r2mzYlvgOcJfIOQ': 'file_storage/call_dzAmbL820r2mzYlvgOcJfIOQ.json', 'var_call_v3lEntZgSJ801nDZAVOpAoi4': 'file_storage/call_v3lEntZgSJ801nDZAVOpAoi4.json'}

exec(code, env_args)
