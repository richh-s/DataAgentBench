code = """import json
import pandas as pd

contracts = locals()['var_function-call-13943309715018504219']
prices = locals()['var_function-call-2296219134182922374']
opp_path = locals()['var_function-call-6142991520220664462']
line_items_path = locals()['var_function-call-7004261383623681178']

with open(opp_path, 'r') as f:
    opportunities = json.load(f)

with open(line_items_path, 'r') as f:
    line_items = json.load(f)

# Convert to DataFrames
df_contracts = pd.DataFrame(contracts)
df_opps = pd.DataFrame(opportunities)
df_lines = pd.DataFrame(line_items)
df_prices = pd.DataFrame(prices)

# Ensure numeric types
df_lines['Quantity'] = pd.to_numeric(df_lines['Quantity'], errors='coerce')
df_prices['UnitPrice'] = pd.to_numeric(df_prices['UnitPrice'], errors='coerce')

# Filter Opportunities by eligible Contracts
eligible_contract_ids = set(df_contracts['Id'])
df_opps_filtered = df_opps[df_opps['ContractID__c'].isin(eligible_contract_ids)]

# Filter Line Items by filtered Opportunities
eligible_opp_ids = set(df_opps_filtered['Id'])
df_lines_filtered = df_lines[df_lines['OpportunityId'].isin(eligible_opp_ids)]

# Join Line Items with Prices
# PricebookEntryId in line items -> Id in prices
# Merge df_lines_filtered with df_prices
df_merged = pd.merge(df_lines_filtered, df_prices, left_on='PricebookEntryId', right_on='Id', how='left')

# Calculate Sales Amount per line
df_merged['SalesAmount'] = df_merged['Quantity'] * df_merged['UnitPrice']

# Join with Opportunity to get OwnerId
# Merge df_merged with df_opps_filtered
df_final = pd.merge(df_merged, df_opps_filtered, left_on='OpportunityId', right_on='Id', how='left')

# Group by OwnerId and sum SalesAmount
sales_by_agent = df_final.groupby('OwnerId')['SalesAmount'].sum().reset_index()

# Find top agent
if not sales_by_agent.empty:
    top_agent = sales_by_agent.sort_values(by='SalesAmount', ascending=False).iloc[0]
    result = top_agent['OwnerId']
else:
    result = "No eligible sales found"

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-10860268760905877449': [{'cid': '0', 'name': 'Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '1', 'name': 'AccountId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'Status', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'EffectiveDate', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '4', 'name': 'Pricebook2Id', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}, {'cid': '5', 'name': 'OwnerId', 'type': 'TEXT', 'notnull': '0', 'dflt_value': 'None', 'pk': '0'}], 'var_function-call-1722603450479975372': [{'cid': '0', 'name': 'Id', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'AccountId', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'Status', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'StartDate', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'CustomerSignedDate', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '5', 'name': 'CompanySignedDate', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '6', 'name': 'Description', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '7', 'name': 'ContractTerm', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_function-call-10981760422748443157': [{'cid': '0', 'name': 'Id', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'ContractID__c', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'AccountId', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'ContactId', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'OwnerId', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '5', 'name': 'Probability', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '6', 'name': 'Amount', 'type': 'DOUBLE', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '7', 'name': 'StageName', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '8', 'name': 'Name', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '9', 'name': 'Description', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '10', 'name': 'CreatedDate', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '11', 'name': 'CloseDate', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_function-call-13673227326269800194': [{'cid': '0', 'name': 'Id', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '1', 'name': 'OpportunityId', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '2', 'name': 'Product2Id', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '3', 'name': 'PricebookEntryId', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '4', 'name': 'Quantity', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}, {'cid': '5', 'name': 'TotalPrice', 'type': 'VARCHAR', 'notnull': 'False', 'dflt_value': 'None', 'pk': 'False'}], 'var_function-call-13943309715018504219': [{'Id': '800Wt00000DDNlnIAH', 'CompanySignedDate': '2022-09-02'}, {'Id': '800Wt00000DDe3OIAT', 'CompanySignedDate': '2022-09-20'}, {'Id': '800Wt00000DDeg6IAD', 'CompanySignedDate': '2022-07-18'}, {'Id': '800Wt00000DDzZLIA1', 'CompanySignedDate': '2022-10-26'}, {'Id': '#800Wt00000DDzvrIAD', 'CompanySignedDate': '2022-08-30'}, {'Id': '800Wt00000DE0FHIA1', 'CompanySignedDate': '2022-08-02'}, {'Id': '800Wt00000DE0TiIAL', 'CompanySignedDate': '2022-09-10'}, {'Id': '800Wt00000DE2vLIAT', 'CompanySignedDate': '2022-06-29'}, {'Id': '800Wt00000DE98oIAD', 'CompanySignedDate': '2022-11-10'}, {'Id': '800Wt00000DE9GrIAL', 'CompanySignedDate': '2022-06-30'}, {'Id': '#800Wt00000DE9ITIA1', 'CompanySignedDate': '2022-09-11'}, {'Id': '#800Wt00000DE9SAIA1', 'CompanySignedDate': '2022-09-30'}, {'Id': '800Wt00000DE9YbIAL', 'CompanySignedDate': '2022-11-22'}, {'Id': '#800Wt00000DE9lVIAT', 'CompanySignedDate': '2022-06-26'}, {'Id': '800Wt00000DE9qLIAT', 'CompanySignedDate': '2022-09-01'}, {'Id': '800Wt00000DE9rxIAD', 'CompanySignedDate': '2022-09-19'}], 'var_function-call-6142991520220664462': 'file_storage/function-call-6142991520220664462.json', 'var_function-call-7004261383623681178': 'file_storage/function-call-7004261383623681178.json', 'var_function-call-2296219134182922374': [{'Id': '01uWt0000027P3lIAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027P3mIAE', 'UnitPrice': '489.99'}, {'Id': '01uWt0000027P5NIAU', 'UnitPrice': '599.99'}, {'Id': '#01uWt0000027P6zIAE', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027P8bIAE', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027P8cIAE', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027PBpIAM', 'UnitPrice': '449.99'}, {'Id': '01uWt0000027PDRIA2', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PF3IAM', 'UnitPrice': '549.99'}, {'Id': '#01uWt0000027PGfIAM', 'UnitPrice': '479.99'}, {'Id': '01uWt0000027PIHIA2', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PIIIA2', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PIJIA2', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PJtIAM', 'UnitPrice': '649.99'}, {'Id': '01uWt0000027PLVIA2', 'UnitPrice': '459.99'}, {'Id': '#01uWt0000027PN7IAM', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027POjIAM', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027POkIAM', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027PQLIA2', 'UnitPrice': '489.99'}, {'Id': '#01uWt0000027PRxIAM', 'UnitPrice': '559.99'}, {'Id': '01uWt0000027PTZIA2', 'UnitPrice': '449.99'}, {'Id': '#01uWt0000027PTaIAM', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PVBIA2', 'UnitPrice': '339.99'}, {'Id': '#01uWt0000027PWnIAM', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027PYPIA2', 'UnitPrice': '319.99'}, {'Id': '01uWt0000027Pa1IAE', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PbdIAE', 'UnitPrice': '389.99'}, {'Id': '01uWt0000027PdFIAU', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027PerIAE', 'UnitPrice': '559.99'}, {'Id': '01uWt0000027PgTIAU', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027PgUIAU', 'UnitPrice': '379.99'}, {'Id': '01uWt0000027Pi5IAE', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PjhIAE', 'UnitPrice': '549.99'}, {'Id': '01uWt0000027PlJIAU', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027PmvIAE', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PoXIAU', 'UnitPrice': '459.99'}, {'Id': '#01uWt0000027Pq9IAE', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027PrlIAE', 'UnitPrice': '369.99'}, {'Id': '#01uWt0000027PtNIAU', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PtOIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PuzIAE', 'UnitPrice': '629.99'}, {'Id': '01uWt0000027PwbIAE', 'UnitPrice': '559.99'}, {'Id': '#01uWt0000027PyDIAU', 'UnitPrice': '649.99'}, {'Id': '#01uWt0000027PzpIAE', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027Q1RIAU', 'UnitPrice': '579.99'}, {'Id': '#01uWt0000027Q33IAE', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027Q34IAE', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027Q4fIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Q6HIAU', 'UnitPrice': '619.99'}]}

exec(code, env_args)
