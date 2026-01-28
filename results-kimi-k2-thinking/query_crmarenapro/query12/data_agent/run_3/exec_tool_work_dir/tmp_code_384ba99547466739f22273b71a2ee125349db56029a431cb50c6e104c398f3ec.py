code = """import json
import pandas as pd
from datetime import datetime

# Load the data from storage
opp_file = var_functions_query_db_0
contract_file = var_functions_query_db_2

print('Opportunities file:', opp_file)
print('Contracts file:', contract_file)

# Read the full data from the JSON files
with open(opp_file, 'r') as f:
    opportunities = json.load(f)

with open(contract_file, 'r') as f:
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

# Convert date strings to datetime
opp_df['CreatedDate'] = pd.to_datetime(opp_df['CreatedDate'])
contract_df['CompanySignedDate'] = pd.to_datetime(contract_df['CompanySignedDate'])

print('Sample cleaned data:')
print(opp_df[['Id', 'OwnerId', 'ContractID__c', 'CreatedDate']].head(3))
print(contract_df[['Id', 'CompanySignedDate']].head(3))

print('__RESULT__:')
print(json.dumps('Data loaded and cleaned successfully'))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
