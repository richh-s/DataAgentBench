code = """import json
import pandas as pd
from datetime import datetime

# Load the data from storage using the correct variable names
opportunities_file = var_functions.query_db_0
contracts_file = var_functions.query_db_2

print('Opportunities file path:', opportunities_file)
print('Contracts file path:', contracts_file)

# Read the full data from the JSON files
with open(opportunities_file, 'r') as f:
    opportunities = json.load(f)

with open(contracts_file, 'r') as f:
    contracts = json.load(f)

print('Opportunities loaded, count:', len(opportunities))
print('Contracts loaded, count:', len(contracts))

# Convert to DataFrames
opp_df = pd.DataFrame(opportunities)
contract_df = pd.DataFrame(contracts)

print('DataFrame shapes - Opportunities:', opp_df.shape, 'Contracts:', contract_df.shape)

# Clean the data
# Remove leading '#' from IDs
opp_df['Id'] = opp_df['Id'].str.replace('#', '')
opp_df['OwnerId'] = opp_df['OwnerId'].str.replace('#', '')
opp_df['ContractID__c'] = opp_df['ContractID__c'].str.replace('#', '')

contract_df['Id'] = contract_df['Id'].str.replace('#', '')

# Remove trailing whitespace
opp_df['ContractID__c'] = opp_df['ContractID__c'].str.strip()
contract_df['Id'] = contract_df['Id'].str.strip()

print('Sample cleaned data:')
print(opp_df[['Id', 'OwnerId', 'ContractID__c']].head(3))
print(contract_df[['Id', 'CompanySignedDate']].head(3))

print('__RESULT__:')
print(json.dumps('Data loaded and cleaned successfully'))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
