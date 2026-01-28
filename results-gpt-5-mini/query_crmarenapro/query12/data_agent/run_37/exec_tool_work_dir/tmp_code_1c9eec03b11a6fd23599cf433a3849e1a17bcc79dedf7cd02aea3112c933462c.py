code = """import pandas as pd
import json
from dateutil import parser
# Access the previous query result
records = var_call_C2jBAkCa2Xtac1blnQMezMWq

# Load into DataFrame
df = pd.DataFrame(records)

# Normalize owner id: remove leading # and surrounding whitespace
df['owner_id_clean'] = df['owner_id'].astype(str).str.strip().str.lstrip('#').str.strip()

# Parse dates manually to handle timezone differences

def parse_date(s):
    try:
        if s is None:
            return pd.NaT
        s_str = str(s).strip()
        if s_str == '' or s_str.lower() == 'none':
            return pd.NaT
        # Use pandas to parse; if timezone aware, convert to UTC and make naive
        dt = pd.to_datetime(s_str, errors='coerce')
        if pd.isna(dt):
            return pd.NaT
        # If tz-aware, convert to UTC and remove tz info
        if dt.tzinfo is not None:
            dt = dt.tz_convert('UTC').tz_localize(None)
        return dt
    except Exception:
        return pd.NaT

# Apply parsing

df['created_date_parsed'] = df['created_date'].apply(parse_date)
df['company_signed_date_parsed'] = df['company_signed_date'].apply(parse_date)

# For created_date entries that have timezone info in string, pandas may create tz-aware. Another approach: parse with dateutil then make naive in UTC
from datetime import datetime

def parse_make_naive(s):
    try:
        if s is None:
            return pd.NaT
        s_str = str(s).strip()
        if s_str == '' or s_str.lower() == 'none':
            return pd.NaT
        dt = parser.parse(s_str)
        # Convert to UTC
        if dt.tzinfo is not None:
            dt = dt.astimezone(tz=None)
            # make naive in local timezone; better: convert to UTC and drop tz
            dt = dt.replace(tzinfo=None)
        return pd.Timestamp(dt)
    except Exception:
        return pd.NaT

# Use parse_make_naive for both

df['created_date_parsed'] = df['created_date'].apply(parse_make_naive)
df['company_signed_date_parsed'] = df['company_signed_date'].apply(parse_make_naive)

# Compute delta days
df['delta_days'] = (df['company_signed_date_parsed'] - df['created_date_parsed']).dt.total_seconds() / 86400.0

# Filter to valid deltas (non-null and non-negative)
valid = df[df['delta_days'].notna() & (df['delta_days'] >= 0)]

if valid.empty:
    result = None
else:
    avg = valid.groupby('owner_id_clean')['delta_days'].mean()
    fastest_owner = avg.idxmin()
    result = str(fastest_owner)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_C2jBAkCa2Xtac1blnQMezMWq': [{'opp_id': '006Wt000007BDApIAO', 'owner_id': '005Wt000003NISMIA4', 'created_date': '2023-04-10T10:15:30.000+0000', 'contract_id': '800Wt00000DE8sgIAD', 'company_signed_date': '2023-10-13'}, {'opp_id': '006Wt000007BHPhIAO', 'owner_id': '#005Wt000003NEa3IAG', 'created_date': '2023-04-15T09:12:34.000+0000', 'contract_id': '800Wt00000DE9ryIAD', 'company_signed_date': '2023-09-30'}, {'opp_id': '#006Wt000007B1klIAC', 'owner_id': '#005Wt000003NBylIAG', 'created_date': '2023-04-15T09:00:34.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}, {'opp_id': '006Wt000007B49NIAS', 'owner_id': '005Wt000003NIs9IAG', 'created_date': '2023-04-25T14:32:51.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}, {'opp_id': '006Wt000007B62sIAC', 'owner_id': '005Wt000003NJZhIAO', 'created_date': '2023-04-04T10:15:30.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}, {'opp_id': '006Wt000007B6itIAC', 'owner_id': '#005Wt000003NJMnIAO', 'created_date': '2023-04-25T09:45:30.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}, {'opp_id': '#006Wt000007B7tQIAS', 'owner_id': '005Wt000003NIfGIAW', 'created_date': '2023-04-15T10:20:30.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}, {'opp_id': '#006Wt000007B7yJIAS', 'owner_id': '#005Wt000003NEdJIAW', 'created_date': '2023-04-15T10:30:45.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}, {'opp_id': '006Wt000007B8CqIAK', 'owner_id': '005Wt000003NInKIAW', 'created_date': '2023-04-15T09:30:45.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}, {'opp_id': '#006Wt000007B8FyIAK', 'owner_id': '005Wt000003NIovIAG', 'created_date': '2023-04-15T10:30:15.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}, {'opp_id': '#006Wt000007BA3JIAW', 'owner_id': '005Wt000003NF9WIAW', 'created_date': '2023-04-02T10:15:30.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}, {'opp_id': '006Wt000007BABLIA4', 'owner_id': '005Wt000003NDEBIA4', 'created_date': '2023-04-01T14:47:23.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}, {'opp_id': '006Wt000007BAHlIAO', 'owner_id': '#005Wt000003NFhPIAW', 'created_date': '2023-04-19T15:30:45.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}, {'opp_id': '006Wt000007BAPrIAO', 'owner_id': '005Wt000003NJxtIAG', 'created_date': '2023-04-15T10:15:32.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}, {'opp_id': '006Wt000007BBDrIAO', 'owner_id': '005Wt000003NJ1pIAG', 'created_date': '2023-04-10T10:30:15.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}, {'opp_id': '006Wt000007BBc1IAG', 'owner_id': '005Wt000003NEtPIAW', 'created_date': '2023-04-15T10:14:32.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}, {'opp_id': '006Wt000007BCLEIA4', 'owner_id': '005Wt000003NJBVIA4', 'created_date': '2023-04-27T11:22:30.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}, {'opp_id': '006Wt000007BCTFIA4', 'owner_id': '#005Wt000003NBcBIAW', 'created_date': '2023-04-20T11:15:33.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}, {'opp_id': '#006Wt000007BChmIAG', 'owner_id': '005Wt000003NJgAIAW', 'created_date': '2023-04-25T10:45:30.000+0000', 'contract_id': '800Wt00000DE9FFIA1', 'company_signed_date': 'None'}, {'opp_id': '#006Wt000007BDXPIA4', 'owner_id': '005Wt000003NJ0EIAW', 'created_date': '2023-04-15T10:45:00.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}, {'opp_id': '006Wt000007BDcEIAW', 'owner_id': '005Wt000003NIAbIAO', 'created_date': '2023-04-15T10:32:45.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}, {'opp_id': '006Wt000007BDpAIAW', 'owner_id': '005Wt000003NEtPIAW', 'created_date': '2023-04-15T10:30:15.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}, {'opp_id': '006Wt000007BETVIA4', 'owner_id': '#005Wt000003NJjNIAW', 'created_date': '2023-04-20T11:34:22.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}, {'opp_id': '#006Wt000007BEV4IAO', 'owner_id': '005Wt000003NFRKIA4', 'created_date': '2023-04-05T14:23:45.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}, {'opp_id': '006Wt000007BFUOIA4', 'owner_id': '005Wt000003NHpdIAG', 'created_date': '2023-04-05T10:15:30.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}, {'opp_id': '006Wt000007BGAIIA4', 'owner_id': '005Wt000003NIdeIAG', 'created_date': '2023-04-11T12:45:33.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}, {'opp_id': '#006Wt000007BGDVIA4', 'owner_id': '005Wt000003NBcBIAW', 'created_date': '2023-04-10T11:20:45.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}, {'opp_id': '#006Wt000007BHZNIA4', 'owner_id': '005Wt000003NIaPIAW', 'created_date': '2023-04-10T14:25:30.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}, {'opp_id': '#006Wt000007BHfpIAG', 'owner_id': '005Wt000003NIqXIAW', 'created_date': '2023-04-17T14:37:45.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}, {'opp_id': '006Wt000007BHr7IAG', 'owner_id': '005Wt000003NIfGIAW', 'created_date': '2023-04-01T09:45:23.000+0000', 'contract_id': 'None', 'company_signed_date': 'None'}]}

exec(code, env_args)
