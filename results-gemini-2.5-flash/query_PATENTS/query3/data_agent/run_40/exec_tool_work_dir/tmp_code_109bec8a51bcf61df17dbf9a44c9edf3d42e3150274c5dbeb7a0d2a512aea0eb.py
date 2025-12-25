code = """import json
import pandas as pd
import re

with open(locals()['var_function-call-373891586094066339'], 'r') as f:
    publication_data = json.load(f)

df_publications = pd.DataFrame(publication_data)

def extract_assignee(patents_info):
    match = re.search(r'assignee_harmonized: ([^,;.]+)', patents_info)
    if match:
        return match.group(1).strip()
    return None

df_publications['assignee_harmonized'] = df_publications['Patents_info'].apply(extract_assignee)

# Get all unique assignees to check for UNIV CALIFORNIA and its variations
all_assignees = df_publications['assignee_harmonized'].unique().tolist()

print('__RESULT__:')
print(json.dumps(all_assignees))"""

env_args = {'var_function-call-15453717939236819502': [], 'var_function-call-373891586094066339': 'file_storage/function-call-373891586094066339.json', 'var_function-call-2533390639764278579': []}

exec(code, env_args)
