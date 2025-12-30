code = """import re, json, pandas as pd

# Load full civic docs
path_docs = var_call_148jrEg3qYEabjivE6d21xun
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Load full funding
path_fund = var_call_btIqmH2tjApBoQdYfKLLGaJX
with open(path_fund, 'r') as f:
    funding = json.load(f)

texts = ' '.join(d['text'] for d in docs)

# Very rough heuristic: assume project names correspond to those in Funding and appear in text near a start date pattern
project_names = [row['Project_Name'] for row in funding]

spring_2022_projects = set()

for name in project_names:
    # search in text
    pattern = re.escape(name)
    for m in re.finditer(pattern, texts):
        window = texts[m.end():m.end()+300]
        # look for Spring 2022 patterns near it
        if re.search(r"2022[-\s]Spring|Spring 2022|March 2022|April 2022|May 2022", window, re.IGNORECASE):
            spring_2022_projects.add(name)
            break

# Sum funding for those projects
spring_projects_funding = [row for row in funding if row['Project_Name'] in spring_2022_projects]

count_projects = len(spring_2022_projects)
 total_funding = sum(int(row['Amount']) for row in spring_projects_funding)

result = {"num_projects_started_spring_2022": count_projects, "total_funding": total_funding}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_148jrEg3qYEabjivE6d21xun': 'file_storage/call_148jrEg3qYEabjivE6d21xun.json', 'var_call_btIqmH2tjApBoQdYfKLLGaJX': 'file_storage/call_btIqmH2tjApBoQdYfKLLGaJX.json'}

exec(code, env_args)
