code = """import json
import pandas as pd
from datetime import datetime

# Load the data from storage
opportunities_path = var_functions.query_db:0
contracts_path = var_functions.query_db:2

# Read the full data from the JSON files
with open(opportunities_path, 'r') as f:
    opportunities = json.load(f)

with open(contracts_path, 'r') as f:
    contracts = json.load(f)

# Convert to DataFrames
opp_df = pd.DataFrame(opportunities)
contract_df = pd.DataFrame(contracts)

# Data cleaning: Remove leading '#' from IDs
opp_df['Id'] = opp_df['Id'].str.replace('#', '')
opp_df['OwnerId'] = opp_df['OwnerId'].str.replace('#', '')
opp_df['ContractID__c'] = opp_df['ContractID__c'].str.replace('#', '')

contract_df['Id'] = contract_df['Id'].str.replace('#', '')

# Remove trailing whitespace
opp_df['ContractID__c'] = opp_df['ContractID__c'].str.strip()
contract_df['Id'] = contract_df['Id'].str.strip()

print('__RESULT__:')
print(json.dumps({
    'opportunities_count': len(opp_df),
    'contracts_count': len(contract_df),
    'sample_opportunities': opp_df.head(3).to_dict('records'),
    'sample_contracts': contract_df.head(3).to_dict('records')
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
