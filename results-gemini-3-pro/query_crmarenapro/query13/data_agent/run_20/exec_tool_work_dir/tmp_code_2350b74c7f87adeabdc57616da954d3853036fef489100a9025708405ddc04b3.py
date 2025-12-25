code = """import json
import pandas as pd

def clean_id(val):
    if val is None:
        return None
    s = str(val).strip()
    if s.lower() == 'none' or s == '':
        return None
    return s.lstrip('#')

# Load data
with open(locals()['var_function-call-12316333429301558190'], 'r') as f:
    contracts = json.load(f)
with open(locals()['var_function-call-12316333429301555633'], 'r') as f:
    opportunities = json.load(f)
with open(locals()['var_function-call-12316333429301557172'], 'r') as f:
    line_items = json.load(f)
price_entries = locals()['var_function-call-12316333429301558711']

# Convert to DataFrames
df_contracts = pd.DataFrame(contracts)
df_opps = pd.DataFrame(opportunities)
df_items = pd.DataFrame(line_items)
df_prices = pd.DataFrame(price_entries)

# Clean IDs for Joining
df_contracts['clean_id'] = df_contracts['Id'].apply(clean_id)
df_opps['clean_contract_id'] = df_opps['ContractID__c'].apply(clean_id)
df_opps['clean_id'] = df_opps['Id'].apply(clean_id)
df_items['clean_opp_id'] = df_items['OpportunityId'].apply(clean_id)
df_items['clean_pbe_id'] = df_items['PricebookEntryId'].apply(clean_id)
df_prices['clean_id'] = df_prices['Id'].apply(clean_id)

# Filter Contracts
start_date = '2022-06-25'
end_date = '2022-11-25'
df_contracts['CompanySignedDate'] = df_contracts['CompanySignedDate'].astype(str).str.strip()
valid_contracts = df_contracts[
    (df_contracts['CompanySignedDate'] >= start_date) & 
    (df_contracts['CompanySignedDate'] <= end_date)
]

# Join
eligible_opps = pd.merge(
    df_opps, 
    valid_contracts[['clean_id']], 
    left_on='clean_contract_id', 
    right_on='clean_id', 
    how='inner',
    suffixes=('_opp', '_con')
)

opp_items = pd.merge(
    eligible_opps[['clean_id_opp', 'OwnerId']], 
    df_items, 
    left_on='clean_id_opp', 
    right_on='clean_opp_id', 
    how='inner'
)

final_df = pd.merge(
    opp_items,
    df_prices[['clean_id', 'UnitPrice']],
    left_on='clean_pbe_id',
    right_on='clean_id',
    how='inner'
)

# Clean OwnerId before grouping
final_df['clean_owner_id'] = final_df['OwnerId'].apply(clean_id)

# Calculate Amount
final_df['Quantity'] = pd.to_numeric(final_df['Quantity'], errors='coerce').fillna(0)
final_df['UnitPrice'] = pd.to_numeric(final_df['UnitPrice'], errors='coerce').fillna(0)
final_df['SalesAmount'] = final_df['Quantity'] * final_df['UnitPrice']

# Sum by Clean OwnerId
agent_sales = final_df.groupby('clean_owner_id')['SalesAmount'].sum().reset_index()

# Find Top Agent
top_agent = agent_sales.sort_values(by='SalesAmount', ascending=False).head(1)

result = top_agent['clean_owner_id'].values[0] if not top_agent.empty else "No agent found"

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-4075165971736892499': [{'Id': '801Wt00000PFsjPIAT', 'AccountId': '001Wt00000PFttwIAD', 'Status': 'Activated', 'EffectiveDate': '2023-06-25', 'Pricebook2Id': '01sWt000000imiTIAQ', 'OwnerId': '005Wt000003NJ0EIAW'}], 'var_function-call-4075165971736891420': [{'Id': '006Wt000007AvVeIAK', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGeJIIA1', 'ContactId': '003Wt00000JqvQiIAJ', 'OwnerId': '005Wt000003NIqXIAW', 'Probability': '75.0', 'Amount': '182448.4965', 'StageName': 'Qualification', 'Name': 'InnoSphere Labs - EDA Innovation Expansion', 'Description': 'InnoSphere Labs is exploring advanced EDA solutions to enhance their R&D capabilities. They are particularly interested in the AI Cirku-Tech for rapid circuit prototyping, and the EcoPCB Creator for environmentally-friendly design processes. Additionally, CloudLink Designer could improve their team collaboration across global projects.', 'CreatedDate': '2023-09-05T11:32:46.000+0000', 'CloseDate': '2024-02-15'}], 'var_function-call-4075165971736894437': [{'Id': '#800Wt00000DD0SZIA1', 'AccountId': '001Wt00000PGZmfIAH', 'Status': 'Activated  ', 'StartDate': '2021-07-20', 'CustomerSignedDate': '2021-07-15', 'CompanySignedDate': '2021-07-16', 'Description': 'This contract solidifies the expanded partnership with Quantum Dynamics LLC for the provision of advanced AI-powered EDA tools, focusing on enhancing their quantum computing technology developments.', 'ContractTerm': '24'}], 'var_function-call-8931113486703717912': [{'cid': '0', 'name': 'Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'AccountId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Status', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'EffectiveDate', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'Pricebook2Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'OwnerId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-8931113486703717975': [{'column_name': 'Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OpportunityId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Product2Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'PricebookEntryId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Quantity', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'TotalPrice', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-8931113486703718038': [{'column_name': 'Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'QuoteId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'OpportunityLineItemId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Product2Id', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'PricebookEntryId', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Quantity', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'UnitPrice', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'Discount', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}, {'column_name': 'TotalPrice', 'column_type': 'VARCHAR', 'null': 'YES', 'key': 'None', 'default': 'None', 'extra': 'None'}], 'var_function-call-12316333429301558190': 'file_storage/function-call-12316333429301558190.json', 'var_function-call-12316333429301555633': 'file_storage/function-call-12316333429301555633.json', 'var_function-call-12316333429301557172': 'file_storage/function-call-12316333429301557172.json', 'var_function-call-12316333429301558711': [{'Id': '01uWt0000027P3lIAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027P3mIAE', 'UnitPrice': '489.99'}, {'Id': '01uWt0000027P5NIAU', 'UnitPrice': '599.99'}, {'Id': '#01uWt0000027P6zIAE', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027P8bIAE', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027P8cIAE', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027PBpIAM', 'UnitPrice': '449.99'}, {'Id': '01uWt0000027PDRIA2', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PF3IAM', 'UnitPrice': '549.99'}, {'Id': '#01uWt0000027PGfIAM', 'UnitPrice': '479.99'}, {'Id': '01uWt0000027PIHIA2', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PIIIA2', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PIJIA2', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PJtIAM', 'UnitPrice': '649.99'}, {'Id': '01uWt0000027PLVIA2', 'UnitPrice': '459.99'}, {'Id': '#01uWt0000027PN7IAM', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027POjIAM', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027POkIAM', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027PQLIA2', 'UnitPrice': '489.99'}, {'Id': '#01uWt0000027PRxIAM', 'UnitPrice': '559.99'}, {'Id': '01uWt0000027PTZIA2', 'UnitPrice': '449.99'}, {'Id': '#01uWt0000027PTaIAM', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PVBIA2', 'UnitPrice': '339.99'}, {'Id': '#01uWt0000027PWnIAM', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027PYPIA2', 'UnitPrice': '319.99'}, {'Id': '01uWt0000027Pa1IAE', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PbdIAE', 'UnitPrice': '389.99'}, {'Id': '01uWt0000027PdFIAU', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027PerIAE', 'UnitPrice': '559.99'}, {'Id': '01uWt0000027PgTIAU', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027PgUIAU', 'UnitPrice': '379.99'}, {'Id': '01uWt0000027Pi5IAE', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PjhIAE', 'UnitPrice': '549.99'}, {'Id': '01uWt0000027PlJIAU', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027PmvIAE', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PoXIAU', 'UnitPrice': '459.99'}, {'Id': '#01uWt0000027Pq9IAE', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027PrlIAE', 'UnitPrice': '369.99'}, {'Id': '#01uWt0000027PtNIAU', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PtOIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PuzIAE', 'UnitPrice': '629.99'}, {'Id': '01uWt0000027PwbIAE', 'UnitPrice': '559.99'}, {'Id': '#01uWt0000027PyDIAU', 'UnitPrice': '649.99'}, {'Id': '#01uWt0000027PzpIAE', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027Q1RIAU', 'UnitPrice': '579.99'}, {'Id': '#01uWt0000027Q33IAE', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027Q34IAE', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027Q4fIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Q6HIAU', 'UnitPrice': '619.99'}], 'var_function-call-2066718297333535417': '005Wt000003NEa3IAG'}

exec(code, env_args)
