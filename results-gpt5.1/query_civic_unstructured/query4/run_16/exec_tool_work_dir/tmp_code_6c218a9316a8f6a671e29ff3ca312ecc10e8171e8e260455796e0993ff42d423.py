code = """import re, json, pandas as pd

# Load full civic docs
path_docs = var_call_NuwTnjF3ibIif745EQUDgfad
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

texts = [d['text'] for d in civic_docs]

project_pattern = re.compile(r"^(?P<name>[A-Z0-9].+?)(?:\n|\r)\s*(?:\(cid:[0-9]+\) )?Updates:", re.MULTILINE)
start_pattern = re.compile(r"Begin Construction:\s*(?P<date>.+)")

projects = []
for text in texts:
    for m in project_pattern.finditer(text):
        name = m.group('name').strip()
        start_search_region = text[m.end(): m.end()+400]
        m_start = start_pattern.search(start_search_region)
        st = m_start.group('date').strip() if m_start else None
        projects.append({'Project_Name': name, 'st': st})

# Filter for Spring 2022
spring_2022_projects = [p for p in projects if p['st'] and ('2022' in p['st']) and any(season in p['st'] for season in ['Spring','March','April','May'])]

# Load funding table
funding = var_call_eCXn3nARxLYho5ZxXj5x5D7i

# Join by exact Project_Name
funding_df = pd.DataFrame(funding)
funding_df['Amount'] = funding_df['Amount'].astype(int)
proj_df = pd.DataFrame(spring_2022_projects)
merged = proj_df.merge(funding_df, on='Project_Name', how='inner')

result = {
    'project_count': int(merged['Project_Name'].nunique()),
    'total_funding': int(merged['Amount'].sum())
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_NuwTnjF3ibIif745EQUDgfad': 'file_storage/call_NuwTnjF3ibIif745EQUDgfad.json', 'var_call_eCXn3nARxLYho5ZxXj5x5D7i': 'file_storage/call_eCXn3nARxLYho5ZxXj5x5D7i.json'}

exec(code, env_args)
