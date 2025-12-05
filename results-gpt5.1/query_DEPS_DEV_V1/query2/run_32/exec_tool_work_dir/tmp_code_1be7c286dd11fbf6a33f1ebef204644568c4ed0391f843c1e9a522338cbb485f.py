code = """import json, pandas as pd
from pathlib import Path

file_path = var_call_uR08p5mkTqrbVPrBijEQ2YVS
rows = json.loads(Path(file_path).read_text())
df = pd.DataFrame(rows)

# Get distinct NPM package versions
uniq = df.drop_duplicates(subset=['System','Name','Version']).head(10000)

# Build an IN clause list
values = []
for _, r in uniq.iterrows():
    values.append(f"('{r['System'].replace("'","''")}', '{r['Name'].replace("'","''")}', '{r['Version'].replace("'","''")}')")

in_clause = ', '.join(values)

query = f"SELECT System, Name, Version, ProjectType, ProjectName FROM project_packageversion WHERE ProjectType = 'GITHUB' AND (System, Name, Version) IN ({in_clause});"

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_call_uR08p5mkTqrbVPrBijEQ2YVS': 'file_storage/call_uR08p5mkTqrbVPrBijEQ2YVS.json', 'var_call_IFv6RF1yZibhiikNWBcOuHNT': ['project_info', 'project_packageversion'], 'var_call_UQWKVGzWS7wSzPvf8tWqUXbr': []}

exec(code, env_args)
