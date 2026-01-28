code = """import pandas as pd
import json
from dateutil import parser
# var_call_BihVrs4EnrbSm1UKMwjsS0WB is available
records = var_call_BihVrs4EnrbSm1UKMwjsS0WB

df = pd.DataFrame(records)
# Clean Ids: remove leading # and trim whitespace
for col in ['OpportunityId','OwnerId','ContractId']:
    if col in df.columns:
        df[col] = df[col].astype(str).str.replace('#','', regex=False).str.strip()

# Parse dates robustly
# CreatedDate includes timezone; CompanySignedDate is date-only

def parse_dt(x):
    if pd.isna(x):
        return pd.NaT
    s = str(x).strip()
    try:
        return pd.to_datetime(s)
    except Exception:
        try:
            return pd.to_datetime(parser.parse(s))
        except Exception:
            return pd.NaT


df['CreatedDate'] = df['CreatedDate'].apply(parse_dt)
# Normalize CreatedDate to date (remove tz) by converting to UTC then date
# But simpler: cast to datetime.date by using dt.normalize then convert to date
# First, convert to UTC if timezone-aware

def to_naive_date(dt):
    if pd.isna(dt):
        return pd.NaT
    if dt.tzinfo is not None:
        # convert to UTC then remove tz
        return dt.tz_convert('UTC').tz_localize(None).date()
    else:
        return dt.date()

# However pandas Timestamp.tzinfo handling: use tz_convert only if tz-aware

# Use pandas ways

df['CreatedDate'] = pd.to_datetime(df['CreatedDate'])
# If tz-aware, convert to UTC then remove tz
if df['CreatedDate'].dt.tz is not None:
    df['CreatedDate'] = df['CreatedDate'].dt.tz_convert('UTC').dt.tz_localize(None)

# Now CompanySignedDate
df['CompanySignedDate'] = pd.to_datetime(df['CompanySignedDate'])
if df['CompanySignedDate'].dt.tz is not None:
    df['CompanySignedDate'] = df['CompanySignedDate'].dt.tz_convert('UTC').dt.tz_localize(None)

# Now compute days
# Use floor for CreatedDate to date
created_dates = df['CreatedDate'].dt.normalize()
company_dates = df['CompanySignedDate'].dt.normalize()

df['SalesCycleDays'] = (company_dates - created_dates).dt.days

# Group by OwnerId
agg = df.groupby('OwnerId', as_index=False)['SalesCycleDays'].mean()
agg['SalesCycleDays'] = agg['SalesCycleDays'].round(6)

min_row = agg.loc[agg['SalesCycleDays'].idxmin()]
result = {"AgentId": min_row['OwnerId']}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_BihVrs4EnrbSm1UKMwjsS0WB': [{'OpportunityId': '#006Wt000007BChmIAG', 'OwnerId': '005Wt000003NJgAIAW', 'CreatedDate': '2023-04-25T10:45:30.000+0000', 'ContractId': '#800Wt00000DE9FFIA1', 'CompanySignedDate': '2023-06-13'}, {'OpportunityId': '006Wt000007BDApIAO', 'OwnerId': '005Wt000003NISMIA4', 'CreatedDate': '2023-04-10T10:15:30.000+0000', 'ContractId': '800Wt00000DE8sgIAD', 'CompanySignedDate': '2023-10-13'}, {'OpportunityId': '006Wt000007BHPhIAO', 'OwnerId': '#005Wt000003NEa3IAG', 'CreatedDate': '2023-04-15T09:12:34.000+0000', 'ContractId': '800Wt00000DE9ryIAD', 'CompanySignedDate': '2023-09-30'}]}

exec(code, env_args)
