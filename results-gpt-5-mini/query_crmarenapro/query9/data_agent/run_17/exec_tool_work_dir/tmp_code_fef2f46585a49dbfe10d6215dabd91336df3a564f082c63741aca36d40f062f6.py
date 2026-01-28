code = """import pandas as pd
import json

# load variables from previous tool calls
cases = var_call_1CVHBQnnn4RhfB7gZA29Q3Qs
accounts = var_call_rsqPWX7O938wdg4qxnxq8fTR

df_cases = pd.DataFrame(cases)
df_accounts = pd.DataFrame(accounts)

# Clean ID fields: remove leading '#' and whitespace
if 'accountid' in df_cases.columns:
    df_cases['accountid_clean'] = df_cases['accountid'].astype(str).str.replace('#', '', regex=False).str.strip()
else:
    df_cases['accountid_clean'] = None

if 'Id' in df_accounts.columns:
    df_accounts['Id_clean'] = df_accounts['Id'].astype(str).str.replace('#', '', regex=False).str.strip()
else:
    df_accounts['Id_clean'] = None

# Clean ShippingState
if 'ShippingState' in df_accounts.columns:
    df_accounts['ShippingState_clean'] = df_accounts['ShippingState'].astype(str).str.strip()
else:
    df_accounts['ShippingState_clean'] = None

# Merge
df = df_cases.merge(df_accounts, left_on='accountid_clean', right_on='Id_clean', how='left')

# Parse dates
df['createddate_parsed'] = pd.to_datetime(df['createddate'], errors='coerce', utc=True)
df['closeddate_parsed'] = pd.to_datetime(df['closeddate'], errors='coerce', utc=True)

# Compute closure time in hours
df['closure_hours'] = (df['closeddate_parsed'] - df['createddate_parsed']).dt.total_seconds() / 3600.0

# Filter valid rows
df_valid = df[df['closure_hours'].notnull() & df['ShippingState_clean'].notnull()]

# If no valid rows, return empty
if df_valid.empty:
    result_state = None
else:
    # Remove negative or zero durations
    df_valid = df_valid[df_valid['closure_hours'] >= 0]
    # Group by state
    grp = df_valid.groupby('ShippingState_clean').agg(mean_closure_hours=('closure_hours', 'mean'), case_count=('closure_hours', 'count')).reset_index()
    # Round mean for stability
    grp['mean_closure_hours'] = grp['mean_closure_hours'].astype(float)
    # Find minimum mean
    min_mean = grp['mean_closure_hours'].min()
    candidates = grp[grp['mean_closure_hours'] == min_mean]
    if len(candidates) > 1:
        # tie-breaker: choose state with highest case_count
        max_count = candidates['case_count'].max()
        candidates = candidates[candidates['case_count'] == max_count]
    # If still multiple, pick first alphabetically
    candidates = candidates.sort_values('ShippingState_clean')
    result_state = candidates.iloc[0]['ShippingState_clean']

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(result_state))"""

env_args = {'var_call_1CVHBQnnn4RhfB7gZA29Q3Qs': [{'id': '500Wt00000DDPIsIAP', 'accountid': '#001Wt00000PGRnYIAX', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'status': 'Closed '}, {'id': '#500Wt00000DDTERIA5', 'accountid': '001Wt00000PGzSaIAL', 'createddate': '2022-03-10T09:30:00.000+0000', 'closeddate': '2022-03-13T09:45:27.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDYdwIAH', 'accountid': '001Wt00000PFj4zIAD', 'createddate': '2022-02-03T14:30:00.000+0000', 'closeddate': '2022-02-03T14:46:56.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDYpHIAX', 'accountid': '#001Wt00000PHHXXIA5', 'createddate': '2022-09-05T11:15:00.000+0000', 'closeddate': '2022-09-05T11:42:09.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDet1IAD', 'accountid': '001Wt00000PGzSbIAL', 'createddate': '2021-09-07T23:48:00.000+0000', 'closeddate': '2021-09-08T03:11:32.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDg1yIAD', 'accountid': '#001Wt00000PHVnNIAX', 'createddate': '2022-02-08T06:22:00.000+0000', 'closeddate': '2022-02-08T06:43:35.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDg1zIAD', 'accountid': '001Wt00000PGdzxIAD', 'createddate': '2022-04-17T14:20:00.000+0000', 'closeddate': '2022-04-17T14:37:58.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDg8RIAT', 'accountid': '001Wt00000PGZZoIAP', 'createddate': '2022-05-10T11:30:00.000+0000', 'closeddate': '2022-05-10T17:02:48.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDgLLIA1', 'accountid': '#001Wt00000PGZZoIAP', 'createddate': '2022-05-12T14:45:00.000+0000', 'closeddate': '2022-05-12T14:54:10.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDsKuIAL', 'accountid': '#001Wt00000PHVvRIAX', 'createddate': '2022-07-23T07:37:00.000+0000', 'closeddate': '2022-07-23T07:47:37.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDxVqIAL', 'accountid': '001Wt00000PHVvRIAX', 'createddate': '2021-09-15T09:10:00.000+0000', 'closeddate': '2021-09-15T09:50:35.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDxZ4IAL', 'accountid': '001Wt00000PGtmwIAD', 'createddate': '2021-06-19T21:19:00.000+0000', 'closeddate': '2021-06-19T21:32:46.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzSnIAL', 'accountid': '001Wt00000PGaZCIA1', 'createddate': '2021-10-15T11:15:00.000+0000', 'closeddate': '2021-10-15T20:15:55.000+0000', 'status': 'Closed   '}, {'id': '#500Wt00000DDzSoIAL', 'accountid': '001Wt00000PHR8gIAH', 'createddate': '2022-07-26T12:38:00.000+0000', 'closeddate': '2022-07-26T13:40:22.000+0000', 'status': 'Closed  '}, {'id': '#500Wt00000DDzZFIA1', 'accountid': '001Wt00000PGoAaIAL', 'createddate': '2021-07-15T10:30:00.000+0000', 'closeddate': '2021-07-15T13:32:47.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzarIAD', 'accountid': '#001Wt00000PGoAaIAL', 'createddate': '2021-10-08T08:07:00.000+0000', 'closeddate': '2021-10-08T08:43:11.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzcTIAT', 'accountid': '001Wt00000PGRnYIAX', 'createddate': '2022-08-01T10:15:00.000+0000', 'closeddate': '2022-08-01T14:45:37.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DDzfhIAD', 'accountid': '001Wt00000PGzM9IAL', 'createddate': '2022-03-04T09:45:00.000+0000', 'closeddate': '2022-03-05T10:25:32.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DDzuDIAT', 'accountid': '#001Wt00000PGtmwIAD', 'createddate': '2021-06-17T18:18:00.000+0000', 'closeddate': '2021-06-17T21:37:59.000+0000', 'status': 'Closed '}, {'id': '#500Wt00000DE077IAD', 'accountid': '001Wt00000PGZmfIAH', 'createddate': '2021-07-22T09:45:00.000+0000', 'closeddate': '2021-07-22T10:00:58.000+0000', 'status': 'Closed  '}, {'id': '500Wt00000DE08jIAD', 'accountid': '001Wt00000PGSwYIAX', 'createddate': '2021-09-16T11:00:00.000+0000', 'closeddate': '2021-09-16T11:14:27.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DE0FCIA1', 'accountid': '001Wt00000PHVvRIAX', 'createddate': '2021-09-05T11:15:00.000+0000', 'closeddate': '2021-09-05T11:25:45.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DE0IPIA1', 'accountid': '001Wt00000PHVtpIAH', 'createddate': '2022-08-10T09:30:00.000+0000', 'closeddate': '2022-08-10T13:59:01.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DE0QTIA1', 'accountid': '001Wt00000PFt7TIAT', 'createddate': '2022-02-02T15:30:45.000+0000', 'closeddate': '2022-02-03T10:17:46.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DE0S5IAL', 'accountid': '001Wt00000PFt7TIAT', 'createddate': '2022-03-05T11:20:30.000+0000', 'closeddate': '2022-03-05T11:34:08.000+0000', 'status': 'Closed'}, {'id': '#500Wt00000DE0ThIAL', 'accountid': '#001Wt00000PGXrLIAX', 'createddate': '2021-10-02T10:30:00.000+0000', 'closeddate': '2021-10-03T13:27:49.000+0000', 'status': 'Closed'}, {'id': '500Wt00000DE0YXIA1', 'accountid': '#001Wt00000PGaZDIA1', 'createddate': '2022-02-24T19:20:00.000+0000', 'closeddate': '2022-02-25T04:35:46.000+0000', 'status': 'Closed'}], 'var_call_rsqPWX7O938wdg4qxnxq8fTR': [{'Id': '001Wt00000PFj4zIAD', 'ShippingState': 'FL'}, {'Id': '001Wt00000PFt7TIAT', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGRnYIAX', 'ShippingState': 'IA'}, {'Id': '001Wt00000PGSwYIAX', 'ShippingState': 'IA'}, {'Id': '#001Wt00000PGXrLIAX', 'ShippingState': 'NY'}, {'Id': '001Wt00000PGZZoIAP', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGZmfIAH', 'ShippingState': 'MI'}, {'Id': '#001Wt00000PGaZCIA1', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGaZDIA1', 'ShippingState': 'CA'}, {'Id': '#001Wt00000PGdzxIAD', 'ShippingState': 'FL'}, {'Id': '001Wt00000PGoAaIAL', 'ShippingState': 'NJ'}, {'Id': '001Wt00000PGtmwIAD', 'ShippingState': 'IL'}, {'Id': '001Wt00000PGzM9IAL', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGzSaIAL', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGzSbIAL', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PHHXXIA5', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PHR8gIAH', 'ShippingState': 'AZ'}, {'Id': '001Wt00000PHVnNIAX', 'ShippingState': 'SC'}, {'Id': '001Wt00000PHVtpIAH', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHVvRIAX', 'ShippingState': 'TX'}]}

exec(code, env_args)
