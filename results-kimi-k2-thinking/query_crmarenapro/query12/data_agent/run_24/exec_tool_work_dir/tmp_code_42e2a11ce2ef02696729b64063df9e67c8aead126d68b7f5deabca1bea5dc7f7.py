code = """import json
import pandas as pd
from datetime import datetime

# Read the full result from file
result_file = locals()['var_functions.query_db:2']
with open(result_file, 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Clean ID fields (remove leading #)
columns_to_clean = ['OpportunityId', 'OwnerId']
for col in columns_to_clean:
    df[col] = df[col].str.replace(r'^#', '', regex=True)

# Convert dates
df['CreatedDate'] = pd.to_datetime(df['CreatedDate'])
df['CompanySignedDate'] = pd.to_datetime(df['CompanySignedDate'])

# Filter for opportunities closed in April 2023
april_2023_start = datetime(2023, 4, 1)
april_2023_end = datetime(2023, 4, 30, 23, 59, 59)

april_2023_df = df[(df['CompanySignedDate'] >= april_2023_start) & 
                   (df['CompanySignedDate'] <= april_2023_end)]

print('__RESULT__:')
print(json.dumps({
    'total_april_2023_records': len(april_2023_df),
    'april_2023_data': april_2023_df.to_dict('records') if len(april_2023_df) > 0 else []
}))"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_records': 122, 'columns': ['ContractId', 'CompanySignedDate', 'OpportunityId', 'CreatedDate', 'OwnerId'], 'sample_data': [{'ContractId': '800Wt00000DE9DdIAL', 'CompanySignedDate': '2023-11-23', 'OpportunityId': '006Wt000007AyaBIAS', 'CreatedDate': '2023-08-14T10:30:00.000+0000', 'OwnerId': '005Wt000003NErnIAG'}, {'ContractId': '800Wt00000DDxHMIA1', 'CompanySignedDate': '2023-09-13', 'OpportunityId': '006Wt000007AzvqIAC', 'CreatedDate': '2023-07-28T10:30:45.000+0000', 'OwnerId': '005Wt000003NIx1IAG'}, {'ContractId': '800Wt00000DDQ6vIAH', 'CompanySignedDate': '2022-03-18', 'OpportunityId': '#006Wt000007B1koIAC', 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'OwnerId': '005Wt000003NEGjIAO'}, {'ContractId': '800Wt00000DDsBEIA1', 'CompanySignedDate': '2024-07-01', 'OpportunityId': '006Wt000007B49SIAS', 'CreatedDate': '2024-05-13T10:15:23.000+0000', 'OwnerId': '005Wt000003NJRdIAO'}, {'ContractId': '800Wt00000DDxdvIAD', 'CompanySignedDate': '2023-01-28', 'OpportunityId': '006Wt000007B4ViIAK', 'CreatedDate': '2022-09-04T10:22:47.000+0000', 'OwnerId': '005Wt000003NJmbIAG'}], 'sample_dates': [{'CompanySignedDate': '2023-11-23', 'CreatedDate': '2023-08-14T10:30:00.000+0000'}, {'CompanySignedDate': '2023-09-13', 'CreatedDate': '2023-07-28T10:30:45.000+0000'}, {'CompanySignedDate': '2022-03-18', 'CreatedDate': '2021-11-15T10:25:30.000+0000'}, {'CompanySignedDate': '2024-07-01', 'CreatedDate': '2024-05-13T10:15:23.000+0000'}, {'CompanySignedDate': '2023-01-28', 'CreatedDate': '2022-09-04T10:22:47.000+0000'}]}}

exec(code, env_args)
