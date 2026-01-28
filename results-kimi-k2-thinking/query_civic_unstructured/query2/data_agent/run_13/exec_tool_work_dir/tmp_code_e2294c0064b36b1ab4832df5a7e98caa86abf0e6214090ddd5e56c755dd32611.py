code = """import json

# Load funding data to find park projects
with open('var_functions.query_db:24', 'r') as f:
    funding_data = json.load(f)

# From the civic docs preview, we know Bluffs Park Shade Structure was completed in November 2022
# Let's find its funding
total_funding = 0

for fund in funding_data:
    fund_name = fund.get('Project_Name', '')
    amount = int(fund.get('Amount', 0))
    
    # Match Bluffs Park Shade Structure
    if 'Bluffs Park Shade Structure' in fund_name:
        total_funding = amount
        break

print('__RESULT__:')
print(json.dumps({'total_funding': total_funding, 'project': 'Bluffs Park Shade Structure', 'completed': 'November 2022'}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
