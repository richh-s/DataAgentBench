code = """import pandas as pd
import json

# Load data from tool results
ops = var_call_xpCWB6wmX2IkdMZCPMrqnIT7
contracts = var_call_EdEdFXinBiHSXmOGbLu2mRFm

# Create DataFrames
df_ops = pd.DataFrame(ops)
df_contracts = pd.DataFrame(contracts)

# Clean function to strip leading '#' and whitespace
def clean_id(x):
    if pd.isna(x):
        return None
    if isinstance(x, str):
        x = x.strip()
        if x == '' or x.lower() == 'none':
            return None
        # strip leading '#'
        if x.startswith('#'):
            return x[1:]
        return x
    return x

# Apply cleaning
if 'ContractID__c' in df_ops.columns:
    df_ops['clean_contract_id'] = df_ops['ContractID__c'].apply(clean_id)
else:
    df_ops['clean_contract_id'] = None

if 'OwnerId' in df_ops.columns:
    df_ops['clean_owner_id'] = df_ops['OwnerId'].apply(clean_id)
else:
    df_ops['clean_owner_id'] = None

# Parse dates
# CreatedDate may include timezone; convert to datetime
df_ops['created_dt'] = pd.to_datetime(df_ops['CreatedDate'], utc=True, errors='coerce')
# keep only date (normalize to date)
df_ops['created_date'] = df_ops['created_dt'].dt.date

# Clean contracts df
if 'Id' in df_contracts.columns:
    df_contracts['clean_id'] = df_contracts['Id'].apply(clean_id)
else:
    df_contracts['clean_id'] = None

# CompanySignedDate may be null or missing
if 'CompanySignedDate' in df_contracts.columns:
    df_contracts['company_signed_date'] = pd.to_datetime(df_contracts['CompanySignedDate'], errors='coerce').dt.date
else:
    df_contracts['company_signed_date'] = pd.NaT

# Merge ops with contracts on cleaned id
merged = pd.merge(df_ops, df_contracts, left_on='clean_contract_id', right_on='clean_id', how='left', suffixes=('_op','_ctr'))

# Keep only rows with a valid company_signed_date
merged_valid = merged[merged['company_signed_date'].notna()].copy()

# Compute sales cycle days = company_signed_date - created_date
# Ensure created_date not null
merged_valid = merged_valid[merged_valid['created_date'].notna()].copy()
merged_valid['sales_cycle_days'] = merged_valid.apply(lambda r: (r['company_signed_date'] - r['created_date']).days, axis=1)

# Group by clean_owner_id and compute average
group = merged_valid.groupby('clean_owner_id', dropna=True)['sales_cycle_days'].mean().reset_index()

# If no data, result is None
if group.empty:
    result = None
else:
    # Find owner with minimum average days
    min_avg = group['sales_cycle_days'].min()
    candidates = group[group['sales_cycle_days'] == min_avg].copy()
    # Sort candidates to pick a deterministic single id (lexicographically)
    candidates['clean_owner_id'] = candidates['clean_owner_id'].astype(str)
    chosen = sorted(candidates['clean_owner_id'].tolist())[0]
    result = chosen

# Print result in required format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_xpCWB6wmX2IkdMZCPMrqnIT7': [{'Id': '#006Wt000007B1klIAC', 'OwnerId': '#005Wt000003NBylIAG', 'CreatedDate': '2023-04-15T09:00:34.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007B49NIAS', 'OwnerId': '005Wt000003NIs9IAG', 'CreatedDate': '2023-04-25T14:32:51.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007B62sIAC', 'OwnerId': '005Wt000003NJZhIAO', 'CreatedDate': '2023-04-04T10:15:30.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007B6itIAC', 'OwnerId': '#005Wt000003NJMnIAO', 'CreatedDate': '2023-04-25T09:45:30.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007B7tQIAS', 'OwnerId': '005Wt000003NIfGIAW', 'CreatedDate': '2023-04-15T10:20:30.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007B7yJIAS', 'OwnerId': '#005Wt000003NEdJIAW', 'CreatedDate': '2023-04-15T10:30:45.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007B8CqIAK', 'OwnerId': '005Wt000003NInKIAW', 'CreatedDate': '2023-04-15T09:30:45.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007B8FyIAK', 'OwnerId': '005Wt000003NIovIAG', 'CreatedDate': '2023-04-15T10:30:15.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007BA3JIAW', 'OwnerId': '005Wt000003NF9WIAW', 'CreatedDate': '2023-04-02T10:15:30.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BABLIA4', 'OwnerId': '005Wt000003NDEBIA4', 'CreatedDate': '2023-04-01T14:47:23.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BAHlIAO', 'OwnerId': '#005Wt000003NFhPIAW', 'CreatedDate': '2023-04-19T15:30:45.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BAPrIAO', 'OwnerId': '005Wt000003NJxtIAG', 'CreatedDate': '2023-04-15T10:15:32.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BBDrIAO', 'OwnerId': '005Wt000003NJ1pIAG', 'CreatedDate': '2023-04-10T10:30:15.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BBc1IAG', 'OwnerId': '005Wt000003NEtPIAW', 'CreatedDate': '2023-04-15T10:14:32.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BCLEIA4', 'OwnerId': '005Wt000003NJBVIA4', 'CreatedDate': '2023-04-27T11:22:30.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BCTFIA4', 'OwnerId': '#005Wt000003NBcBIAW', 'CreatedDate': '2023-04-20T11:15:33.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007BChmIAG', 'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2023-04-25T10:45:30.000+0000', 'ContractID__c': '800Wt00000DE9FFIA1'}, {'Id': '006Wt000007BDApIAO', 'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'ContractID__c': '800Wt00000DE8sgIAD'}, {'Id': '#006Wt000007BDXPIA4', 'OwnerId': '005Wt000003NJ0EIAW', 'CreatedDate': '2023-04-15T10:45:00.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BDcEIAW', 'OwnerId': '005Wt000003NIAbIAO', 'CreatedDate': '2023-04-15T10:32:45.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BDpAIAW', 'OwnerId': '005Wt000003NEtPIAW', 'CreatedDate': '2023-04-15T10:30:15.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BETVIA4', 'OwnerId': '#005Wt000003NJjNIAW', 'CreatedDate': '2023-04-20T11:34:22.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007BEV4IAO', 'OwnerId': '005Wt000003NFRKIA4', 'CreatedDate': '2023-04-05T14:23:45.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BFUOIA4', 'OwnerId': '005Wt000003NHpdIAG', 'CreatedDate': '2023-04-05T10:15:30.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BGAIIA4', 'OwnerId': '005Wt000003NIdeIAG', 'CreatedDate': '2023-04-11T12:45:33.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007BGDVIA4', 'OwnerId': '005Wt000003NBcBIAW', 'CreatedDate': '2023-04-10T11:20:45.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BHPhIAO', 'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'ContractID__c': '800Wt00000DE9ryIAD'}, {'Id': '#006Wt000007BHZNIA4', 'OwnerId': '005Wt000003NIaPIAW', 'CreatedDate': '2023-04-10T14:25:30.000+0000', 'ContractID__c': 'None'}, {'Id': '#006Wt000007BHfpIAG', 'OwnerId': '005Wt000003NIqXIAW', 'CreatedDate': '2023-04-17T14:37:45.000+0000', 'ContractID__c': 'None'}, {'Id': '006Wt000007BHr7IAG', 'OwnerId': '005Wt000003NIfGIAW', 'CreatedDate': '2023-04-01T09:45:23.000+0000', 'ContractID__c': 'None'}], 'var_call_EdEdFXinBiHSXmOGbLu2mRFm': [{'Id': '800Wt00000DE8sgIAD', 'CompanySignedDate': '2023-10-13'}, {'Id': '800Wt00000DE9ryIAD', 'CompanySignedDate': '2023-09-30'}]}

exec(code, env_args)
