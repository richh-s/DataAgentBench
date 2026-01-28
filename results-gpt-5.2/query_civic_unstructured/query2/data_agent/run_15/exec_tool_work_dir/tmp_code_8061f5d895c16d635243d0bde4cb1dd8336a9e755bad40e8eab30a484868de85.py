code = """import json
import pandas as pd

# park-related projects completed in 2022 found in the doc preview: Bluffs Park Shade Structure
completed_2022_park_projects = ['Bluffs Park Shade Structure']

path_fund = var_call_7rv7dzdnvLIhF51JyL0Jqu7x
with open(path_fund,'r',encoding='utf-8') as f:
    fund = json.load(f)
fund_df = pd.DataFrame(fund)
fund_df['Total_Amount'] = pd.to_numeric(fund_df['Total_Amount'])

res = fund_df[fund_df['Project_Name'].isin(completed_2022_park_projects)].copy()

total = int(res['Total_Amount'].sum())
print('__RESULT__:')
print(json.dumps({'total_funding': total, 'projects': res.to_dict(orient='records')}))"""

env_args = {'var_call_YtD90rUj03rayH0hWzM7kgCV': 'file_storage/call_YtD90rUj03rayH0hWzM7kgCV.json', 'var_call_7rv7dzdnvLIhF51JyL0Jqu7x': 'file_storage/call_7rv7dzdnvLIhF51JyL0Jqu7x.json', 'var_call_k6GiortEkCkLT38S4OkCuc8D': {'total_funding': 0, 'project_count': 0, 'projects': [], 'matched_project_names': []}, 'var_call_jsPZpC9NR9g5JWMfLvf8owkQ': 'file_storage/call_jsPZpC9NR9g5JWMfLvf8owkQ.json'}

exec(code, env_args)
