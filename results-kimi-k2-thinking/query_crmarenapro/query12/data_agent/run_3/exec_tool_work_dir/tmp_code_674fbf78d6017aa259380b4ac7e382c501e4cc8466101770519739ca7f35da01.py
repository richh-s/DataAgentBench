code = """import json
import pandas as pd
from datetime import datetime

# Load the data from storage using the correct variable names
opportunities = var_functions_query_db_0
contracts = var_functions_query_db_2

print('Type of opportunities:', type(opportunities))
print('Type of contracts:', type(contracts))

# If they're file paths, read them
if isinstance(opportunities, str) and opportunities.endswith('.json'):
    with open(opportunities, 'r') as f:
        opportunities = json.load(f)

if isinstance(contracts, str) and contracts.endswith('.json'):
    with open(contracts, 'r') as f:
        contracts = json.load(f)

print('Opportunities loaded, count:', len(opportunities))
print('Contracts loaded, count:', len(contracts))

# Convert to DataFrames
opp_df = pd.DataFrame(opportunities)
contract_df = pd.DataFrame(contracts)

print('DataFrame shapes - Opportunities:', opp_df.shape, 'Contracts:', contract_df.shape)

print('__RESULT__:')
print(json.dumps('Data loaded successfully'))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
