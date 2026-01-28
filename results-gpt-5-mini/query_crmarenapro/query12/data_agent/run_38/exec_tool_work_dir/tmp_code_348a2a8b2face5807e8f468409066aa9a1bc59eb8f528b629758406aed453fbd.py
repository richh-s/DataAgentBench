code = """import pandas as pd
import json

df = pd.DataFrame(var_call_FQpCyWmyKq7JH3CHWVN0gjDe)
if df.empty:
    result = None
else:
    # clean owner id: strip whitespace and leading '#'
    df['owner_clean'] = df['owner_id'].astype(str).str.strip().str.replace(r"^#+", "", regex=True)
    # parse dates
    df['created_dt'] = pd.to_datetime(df['created_date'], utc=True)
    df['company_signed_dt'] = pd.to_datetime(df['company_signed_date'], utc=True)
    # compute days difference (company_signed - created)
    df['days'] = (df['company_signed_dt'] - df['created_dt']).dt.days
    # group by owner and compute average days
    grp = df.groupby('owner_clean', dropna=False)['days'].mean()
    # find owner with minimum average
    min_owner = None
    if not grp.empty:
        min_owner = grp.idxmin()
    result = min_owner

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_FQpCyWmyKq7JH3CHWVN0gjDe': [{'opp_id': '#006Wt000007BChmIAG', 'owner_id': '005Wt000003NJgAIAW', 'created_date': '2023-04-25T10:45:30.000+0000', 'contract_id': '#800Wt00000DE9FFIA1', 'company_signed_date': '2023-06-13'}, {'opp_id': '006Wt000007BDApIAO', 'owner_id': '005Wt000003NISMIA4', 'created_date': '2023-04-10T10:15:30.000+0000', 'contract_id': '800Wt00000DE8sgIAD', 'company_signed_date': '2023-10-13'}, {'opp_id': '006Wt000007BHPhIAO', 'owner_id': '#005Wt000003NEa3IAG', 'created_date': '2023-04-15T09:12:34.000+0000', 'contract_id': '800Wt00000DE9ryIAD', 'company_signed_date': '2023-09-30'}], 'var_call_N1l1Klu560eBKA8LNN2Y0bk4': 'file_storage/call_N1l1Klu560eBKA8LNN2Y0bk4.json'}

exec(code, env_args)
