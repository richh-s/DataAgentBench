code = """import re, json, pandas as pd, os, json as json_lib

# helper to load from file if needed
def load_var(v):
    if isinstance(v, str) and os.path.isfile(v):
        with open(v, 'r') as f:
            return json_lib.load(f)
    return v

civic_docs = load_var(var_call_9k3ujD33rucb6EkyCYVuAGbJ)
funding = load_var(var_call_YE6SQYi0mhdRyKHlk8OpMk7f)

texts = ' '.join(doc['text'] for doc in civic_docs)

park_keywords = ['park', 'playground']
projects_2022_park = set()

for line in texts.split('\n'):
    lower = line.lower()
    if 'completed' in lower and '2022' in lower and any(k in lower for k in park_keywords):
        projects_2022_park.add(line.strip())

manual_projects = ['Bluffs Park Shade Structure']
project_names = set(manual_projects)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)
mask = fund_df['Project_Name'].isin(project_names)

total = int(fund_df.loc[mask, 'Amount'].sum())
result = {"total_funding_park_projects_completed_2022": total, "projects_counted": fund_df.loc[mask, 'Project_Name'].tolist(), "detected_lines": list(projects_2022_park)[:20]}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_9k3ujD33rucb6EkyCYVuAGbJ': 'file_storage/call_9k3ujD33rucb6EkyCYVuAGbJ.json', 'var_call_YE6SQYi0mhdRyKHlk8OpMk7f': 'file_storage/call_YE6SQYi0mhdRyKHlk8OpMk7f.json'}

exec(code, env_args)
