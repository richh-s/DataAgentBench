code = """import pandas as pd
import json

# Load Data
# pb_entries is a list, not a file path
pb_entries = locals()['var_function-call-15490005194197934706']

# oi_prod was a file
with open(locals()['var_function-call-15112027591336911943'], 'r') as f:
    oi_prod = json.load(f) # Id, Product2Id

# oi_pb was a file
with open(locals()['var_function-call-15490005194197936487'], 'r') as f:
    oi_pb = json.load(f) # Id, PriceBookEntryId

# cases was a file
with open(locals()['var_function-call-1629989200070721134'], 'r') as f:
    cases = json.load(f)

# Helper
def clean(x):
    if x is None: return ""
    return str(x).replace('#', '').strip()

target_prod_id = "01tWt000006hVJdIAM"

# 1. Identify relevant PricebookEntries
df_pbe = pd.DataFrame(pb_entries)
df_pbe['clean_prod_id'] = df_pbe['Product2Id'].apply(clean)
df_pbe['clean_id'] = df_pbe['Id'].apply(clean)

target_pbe_ids = set(df_pbe[df_pbe['clean_prod_id'] == target_prod_id]['clean_id'])
print(f"DEBUG: Relevant PricebookEntry IDs: {len(target_pbe_ids)}")

# 2. Identify relevant OrderItems
# Path A: Direct Product2Id
df_oi_prod = pd.DataFrame(oi_prod)
df_oi_prod['clean_prod_id'] = df_oi_prod['Product2Id'].apply(clean)
df_oi_prod['clean_id'] = df_oi_prod['Id'].apply(clean)
ids_from_prod = set(df_oi_prod[df_oi_prod['clean_prod_id'] == target_prod_id]['clean_id'])

# Path B: Via PricebookEntryId
df_oi_pb = pd.DataFrame(oi_pb)
df_oi_pb['clean_pbe_id'] = df_oi_pb['PriceBookEntryId'].apply(clean)
df_oi_pb['clean_id'] = df_oi_pb['Id'].apply(clean)
ids_from_pbe = set(df_oi_pb[df_oi_pb['clean_pbe_id'].isin(target_pbe_ids)]['clean_id'])

target_oi_ids = ids_from_prod.union(ids_from_pbe)
print(f"DEBUG: Relevant OrderItem IDs: {len(target_oi_ids)}")

# 3. Filter Cases
df_cases = pd.DataFrame(cases)
df_cases['clean_oi_id'] = df_cases['orderitemid__c'].apply(clean)
df_cases['createddate'] = pd.to_datetime(df_cases['createddate'], errors='coerce')

matched_cases = df_cases[df_cases['clean_oi_id'].isin(target_oi_ids)].copy()
print(f"DEBUG: Matched Cases (All Time): {len(matched_cases)}")

# 4. Filter Date
ref_date = pd.Timestamp("2021-04-10").tz_localize('UTC')
start_date = ref_date - pd.DateOffset(months=10)
# Start date approx 2020-06-10

matched_cases = matched_cases[(matched_cases['createddate'] <= ref_date) & (matched_cases['createddate'] >= start_date)]
print(f"DEBUG: Matched Cases (Past 10 Months): {len(matched_cases)}")

# 5. Group
matched_cases['month'] = matched_cases['createddate'].dt.strftime('%B')
matched_cases['year_month'] = matched_cases['createddate'].dt.strftime('%Y-%m')

counts = matched_cases['year_month'].value_counts().sort_index()

print("__RESULT__:")
print(json.dumps(counts.to_dict()))"""

env_args = {'var_function-call-15112027591336911943': 'file_storage/function-call-15112027591336911943.json', 'var_function-call-1629989200070721134': 'file_storage/function-call-1629989200070721134.json', 'var_function-call-3934149717266984374': {'2020-09': 1, '2020-11': 2, '2021-01': 1, '2021-03': 1}, 'var_function-call-7611884811353004601': [{'Name': 'SecureAnalytics Pro', 'Id': '#01tWt000006hVJdIAM'}], 'var_function-call-17609888728764763847': {'2020-09': 1, '2020-11': 2, '2021-01': 1, '2021-03': 1, '2023-06': 1}, 'var_function-call-15490005194197934706': [{'Id': '01uWt0000027P3lIAE', 'Product2Id': '01tWt000006hV57IAE'}, {'Id': '01uWt0000027P3mIAE', 'Product2Id': '01tWt000006hVhpIAE'}, {'Id': '01uWt0000027P5NIAU', 'Product2Id': '#01tWt000006hV58IAE'}, {'Id': '#01uWt0000027P6zIAE', 'Product2Id': '01tWt000006hTUkIAM'}, {'Id': '#01uWt0000027P8bIAE', 'Product2Id': '01tWt000006hV6jIAE'}, {'Id': '01uWt0000027P8cIAE', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '01uWt0000027PADIA2', 'Product2Id': '01tWt000006hPffIAE'}, {'Id': '01uWt0000027PBpIAM', 'Product2Id': '01tWt000006hV9xIAE'}, {'Id': '01uWt0000027PDRIA2', 'Product2Id': '01tWt000006hVBZIA2'}, {'Id': '01uWt0000027PF3IAM', 'Product2Id': '01tWt000006hVDBIA2'}, {'Id': '#01uWt0000027PGfIAM', 'Product2Id': '01tWt000006hVEnIAM'}, {'Id': '01uWt0000027PIHIA2', 'Product2Id': '#01tWt000006hVGPIA2'}, {'Id': '01uWt0000027PIIIA2', 'Product2Id': '01tWt000006hVI1IAM'}, {'Id': '01uWt0000027PIJIA2', 'Product2Id': '01tWt000006hVptIAE'}, {'Id': '01uWt0000027PJtIAM', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '01uWt0000027PLVIA2', 'Product2Id': '#01tWt000006hVLFIA2'}, {'Id': '#01uWt0000027PN7IAM', 'Product2Id': '01tWt000006hPfgIAE'}, {'Id': '#01uWt0000027POjIAM', 'Product2Id': '01tWt000006hVMrIAM'}, {'Id': '01uWt0000027POkIAM', 'Product2Id': '#01tWt000006hRfqIAE'}, {'Id': '01uWt0000027PQLIA2', 'Product2Id': '#01tWt000006hUKMIA2'}, {'Id': '#01uWt0000027PRxIAM', 'Product2Id': '#01tWt000006hVOTIA2'}, {'Id': '01uWt0000027PTZIA2', 'Product2Id': '01tWt000006hV0IIAU'}, {'Id': '#01uWt0000027PTaIAM', 'Product2Id': '01tWt000006hVUvIAM'}, {'Id': '01uWt0000027PVBIA2', 'Product2Id': '01tWt000006hVQ5IAM'}, {'Id': '#01uWt0000027PWnIAM', 'Product2Id': '01tWt000006hVQ6IAM'}, {'Id': '01uWt0000027PYPIA2', 'Product2Id': '#01tWt000006hVRhIAM'}, {'Id': '01uWt0000027Pa1IAE', 'Product2Id': '01tWt000006hVTJIA2'}, {'Id': '01uWt0000027PbdIAE', 'Product2Id': '01tWt000006hVWXIA2'}, {'Id': '01uWt0000027PdFIAU', 'Product2Id': '01tWt000006hVY9IAM'}, {'Id': '01uWt0000027PerIAE', 'Product2Id': '01tWt000006hVZlIAM'}, {'Id': '01uWt0000027PgTIAU', 'Product2Id': '01tWt000006hVbNIAU'}, {'Id': '01uWt0000027PgUIAU', 'Product2Id': '01tWt000006hVt7IAE'}, {'Id': '01uWt0000027Pi5IAE', 'Product2Id': '01tWt000006hVczIAE'}, {'Id': '01uWt0000027PjhIAE', 'Product2Id': '01tWt000006hVebIAE'}, {'Id': '01uWt0000027PlJIAU', 'Product2Id': '01tWt000006hUsEIAU'}, {'Id': '#01uWt0000027PmvIAE', 'Product2Id': '01tWt000006hVJeIAM'}, {'Id': '01uWt0000027PoXIAU', 'Product2Id': '#01tWt000006hVgDIAU'}, {'Id': '#01uWt0000027Pq9IAE', 'Product2Id': '01tWt000006hVjRIAU'}, {'Id': '01uWt0000027PrlIAE', 'Product2Id': '01tWt000006hVl3IAE'}, {'Id': '#01uWt0000027PtNIAU', 'Product2Id': '01tWt000006hVmfIAE'}, {'Id': '01uWt0000027PtOIAU', 'Product2Id': '01tWt000006hVwLIAU'}, {'Id': '01uWt0000027PuzIAE', 'Product2Id': '01tWt000006hVoHIAU'}, {'Id': '01uWt0000027PwbIAE', 'Product2Id': '01tWt000006hUUwIAM'}, {'Id': '#01uWt0000027PyDIAU', 'Product2Id': '01tWt000006hVrVIAU'}, {'Id': '#01uWt0000027PzpIAE', 'Product2Id': '01tWt000006hVrWIAU'}, {'Id': '01uWt0000027Q1RIAU', 'Product2Id': '01tWt000006hVujIAE'}, {'Id': '#01uWt0000027Q33IAE', 'Product2Id': '01tWt000006hOd8IAE'}, {'Id': '#01uWt0000027Q34IAE', 'Product2Id': '01tWt000006hUgwIAE'}, {'Id': '01uWt0000027Q4fIAE', 'Product2Id': '01tWt000006hVjSIAU'}, {'Id': '01uWt0000027Q6HIAU', 'Product2Id': '01tWt000006hUtqIAE'}], 'var_function-call-15490005194197936487': 'file_storage/function-call-15490005194197936487.json'}

exec(code, env_args)
