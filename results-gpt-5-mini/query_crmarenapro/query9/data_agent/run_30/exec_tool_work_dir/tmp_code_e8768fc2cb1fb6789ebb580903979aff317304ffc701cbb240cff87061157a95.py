code = """import json
import pandas as pd
cases = pd.DataFrame(var_call_2RquQAqQx1mH2QRt7PV9XPkB)
accounts = pd.DataFrame(var_call_NR1tWPNgyZ2NJIL79qgHf4Q9)
# normalize account ids in cases and accounts by stripping leading # and whitespace
cases['accountid_clean'] = cases['accountid'].str.strip().str.lstrip('#')
accounts['Id_clean'] = accounts['Id'].str.strip().str.lstrip('#')
# merge
merged = cases.merge(accounts, left_on='accountid_clean', right_on='Id_clean', how='left')
# compute resolution time in hours
from datetime import datetime
merged['created_ts'] = pd.to_datetime(merged['createddate'], utc=True)
merged['closed_ts'] = pd.to_datetime(merged['closeddate'], utc=True)
merged['resolution_hours'] = (merged['closed_ts'] - merged['created_ts']).dt.total_seconds() / 3600.0
# determine quarter bins for createddate; past 6 quarters from today's date 2022-10-26
# generate quarter start cutoff: we want cases created in past 6 quarters ending on 2022-10-26
today = pd.Timestamp('2022-10-26', tz='UTC')
# find current quarter for that date
def quarter_start(ts):
    q = (ts.month-1)//3 + 1
    start_month = 3*(q-1)+1
    return pd.Timestamp(year=ts.year, month=start_month, day=1, tz='UTC')
cur_q_start = quarter_start(today)
# collect 6 quarter starts including current
quarters = [cur_q_start - pd.DateOffset(months=3*i) for i in range(6)]
quarters = sorted(quarters)
quarter_ranges = []
for i in range(len(quarters)):
    qstart = quarters[i]
    qend = qstart + pd.DateOffset(months=3) - pd.Timedelta(seconds=1)
    quarter_ranges.append((qstart, qend))
# filter merged to created_ts within these ranges
mask = False
for (qs,qe) in quarter_ranges:
    mask = mask | ((merged['created_ts'] >= qs) & (merged['created_ts'] <= qe))
filtered = merged[mask].copy()
# group by ShippingState and quarter; compute average resolution hours
# label quarters as YYYY-Qn
def quarter_label(ts):
    q = (ts.month-1)//3 + 1
    return f"{ts.year}-Q{q}"
filtered['quarter'] = filtered['created_ts'].apply(quarter_label)
# ensure ShippingState cleaned
filtered['ShippingState'] = filtered['ShippingState'].str.strip()
# compute avg resolution per state per quarter
grp = filtered.groupby(['ShippingState','quarter']).agg(avg_resolution_hours=('resolution_hours','mean'), count=('resolution_hours','count')).reset_index()
# We need states with quickest case closure time in the past 6 quarters.
# Interpret as states with the lowest average resolution hours across the 6 quarters combined where they have data in most quarters? The user: "Return only the two-letter abbreviation of the most matching state (eg. CA)."
# We'll compute overall average across all cases in the 6-quarter window per state.
overall = filtered.groupby('ShippingState').agg(avg_resolution_hours=('resolution_hours','mean'), case_count=('resolution_hours','count')).reset_index()
# choose state with minimum avg_resolution_hours, require at least 1 case
overall_sorted = overall.sort_values(['avg_resolution_hours','case_count'])
result_state = overall_sorted.iloc[0]['ShippingState'] if not overall_sorted.empty else None
out = {'best_state': result_state, 'overall': overall_sorted.to_dict(orient='records'), 'per_quarter': grp.to_dict(orient='records')}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_2RquQAqQx1mH2QRt7PV9XPkB': [{'id': '500Wt00000DDPIsIAP', 'accountid': '#001Wt00000PGRnYIAX', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000'}, {'id': '#500Wt00000DDTERIA5', 'accountid': '001Wt00000PGzSaIAL', 'createddate': '2022-03-10T09:30:00.000+0000', 'closeddate': '2022-03-13T09:45:27.000+0000'}, {'id': '#500Wt00000DDYdwIAH', 'accountid': '001Wt00000PFj4zIAD', 'createddate': '2022-02-03T14:30:00.000+0000', 'closeddate': '2022-02-03T14:46:56.000+0000'}, {'id': '#500Wt00000DDYpHIAX', 'accountid': '#001Wt00000PHHXXIA5', 'createddate': '2022-09-05T11:15:00.000+0000', 'closeddate': '2022-09-05T11:42:09.000+0000'}, {'id': '#500Wt00000DDet1IAD', 'accountid': '001Wt00000PGzSbIAL', 'createddate': '2021-09-07T23:48:00.000+0000', 'closeddate': '2021-09-08T03:11:32.000+0000'}, {'id': '500Wt00000DDg1yIAD', 'accountid': '#001Wt00000PHVnNIAX', 'createddate': '2022-02-08T06:22:00.000+0000', 'closeddate': '2022-02-08T06:43:35.000+0000'}, {'id': '500Wt00000DDg1zIAD', 'accountid': '001Wt00000PGdzxIAD', 'createddate': '2022-04-17T14:20:00.000+0000', 'closeddate': '2022-04-17T14:37:58.000+0000'}, {'id': '500Wt00000DDg8RIAT', 'accountid': '001Wt00000PGZZoIAP', 'createddate': '2022-05-10T11:30:00.000+0000', 'closeddate': '2022-05-10T17:02:48.000+0000'}, {'id': '500Wt00000DDgLLIA1', 'accountid': '#001Wt00000PGZZoIAP', 'createddate': '2022-05-12T14:45:00.000+0000', 'closeddate': '2022-05-12T14:54:10.000+0000'}, {'id': '500Wt00000DDsKuIAL', 'accountid': '#001Wt00000PHVvRIAX', 'createddate': '2022-07-23T07:37:00.000+0000', 'closeddate': '2022-07-23T07:47:37.000+0000'}, {'id': '500Wt00000DDxVqIAL', 'accountid': '001Wt00000PHVvRIAX', 'createddate': '2021-09-15T09:10:00.000+0000', 'closeddate': '2021-09-15T09:50:35.000+0000'}, {'id': '500Wt00000DDzSnIAL', 'accountid': '001Wt00000PGaZCIA1', 'createddate': '2021-10-15T11:15:00.000+0000', 'closeddate': '2021-10-15T20:15:55.000+0000'}, {'id': '#500Wt00000DDzSoIAL', 'accountid': '001Wt00000PHR8gIAH', 'createddate': '2022-07-26T12:38:00.000+0000', 'closeddate': '2022-07-26T13:40:22.000+0000'}, {'id': '#500Wt00000DDzZFIA1', 'accountid': '001Wt00000PGoAaIAL', 'createddate': '2021-07-15T10:30:00.000+0000', 'closeddate': '2021-07-15T13:32:47.000+0000'}, {'id': '500Wt00000DDzarIAD', 'accountid': '#001Wt00000PGoAaIAL', 'createddate': '2021-10-08T08:07:00.000+0000', 'closeddate': '2021-10-08T08:43:11.000+0000'}, {'id': '500Wt00000DDzcTIAT', 'accountid': '001Wt00000PGRnYIAX', 'createddate': '2022-08-01T10:15:00.000+0000', 'closeddate': '2022-08-01T14:45:37.000+0000'}, {'id': '500Wt00000DDzfhIAD', 'accountid': '001Wt00000PGzM9IAL', 'createddate': '2022-03-04T09:45:00.000+0000', 'closeddate': '2022-03-05T10:25:32.000+0000'}, {'id': '#500Wt00000DE077IAD', 'accountid': '001Wt00000PGZmfIAH', 'createddate': '2021-07-22T09:45:00.000+0000', 'closeddate': '2021-07-22T10:00:58.000+0000'}, {'id': '500Wt00000DE08jIAD', 'accountid': '001Wt00000PGSwYIAX', 'createddate': '2021-09-16T11:00:00.000+0000', 'closeddate': '2021-09-16T11:14:27.000+0000'}, {'id': '#500Wt00000DE0FCIA1', 'accountid': '001Wt00000PHVvRIAX', 'createddate': '2021-09-05T11:15:00.000+0000', 'closeddate': '2021-09-05T11:25:45.000+0000'}, {'id': '500Wt00000DE0IPIA1', 'accountid': '001Wt00000PHVtpIAH', 'createddate': '2022-08-10T09:30:00.000+0000', 'closeddate': '2022-08-10T13:59:01.000+0000'}, {'id': '500Wt00000DE0QTIA1', 'accountid': '001Wt00000PFt7TIAT', 'createddate': '2022-02-02T15:30:45.000+0000', 'closeddate': '2022-02-03T10:17:46.000+0000'}, {'id': '500Wt00000DE0S5IAL', 'accountid': '001Wt00000PFt7TIAT', 'createddate': '2022-03-05T11:20:30.000+0000', 'closeddate': '2022-03-05T11:34:08.000+0000'}, {'id': '#500Wt00000DE0ThIAL', 'accountid': '#001Wt00000PGXrLIAX', 'createddate': '2021-10-02T10:30:00.000+0000', 'closeddate': '2021-10-03T13:27:49.000+0000'}, {'id': '500Wt00000DE0YXIA1', 'accountid': '#001Wt00000PGaZDIA1', 'createddate': '2022-02-24T19:20:00.000+0000', 'closeddate': '2022-02-25T04:35:46.000+0000'}], 'var_call_uynSX4vOjsOu4jzaCxmdTu7v': {'original_ids': ['#001Wt00000PGRnYIAX', '#001Wt00000PGXrLIAX', '#001Wt00000PGZZoIAP', '#001Wt00000PGaZDIA1', '#001Wt00000PGoAaIAL', '#001Wt00000PHHXXIA5', '#001Wt00000PHVnNIAX', '#001Wt00000PHVvRIAX', '001Wt00000PFj4zIAD', '001Wt00000PFt7TIAT', '001Wt00000PGRnYIAX', '001Wt00000PGSwYIAX', '001Wt00000PGZZoIAP', '001Wt00000PGZmfIAH', '001Wt00000PGaZCIA1', '001Wt00000PGdzxIAD', '001Wt00000PGoAaIAL', '001Wt00000PGzM9IAL', '001Wt00000PGzSaIAL', '001Wt00000PGzSbIAL', '001Wt00000PHR8gIAH', '001Wt00000PHVtpIAH', '001Wt00000PHVvRIAX'], 'expanded_ids': ['#001Wt00000PGRnYIAX', '#001Wt00000PGXrLIAX', '#001Wt00000PGZZoIAP', '#001Wt00000PGaZDIA1', '#001Wt00000PGoAaIAL', '#001Wt00000PHHXXIA5', '#001Wt00000PHVnNIAX', '#001Wt00000PHVvRIAX', '001Wt00000PFj4zIAD', '001Wt00000PFt7TIAT', '001Wt00000PGRnYIAX', '001Wt00000PGSwYIAX', '001Wt00000PGXrLIAX', '001Wt00000PGZZoIAP', '001Wt00000PGZmfIAH', '001Wt00000PGaZCIA1', '001Wt00000PGaZDIA1', '001Wt00000PGdzxIAD', '001Wt00000PGoAaIAL', '001Wt00000PGzM9IAL', '001Wt00000PGzSaIAL', '001Wt00000PGzSbIAL', '001Wt00000PHHXXIA5', '001Wt00000PHR8gIAH', '001Wt00000PHVnNIAX', '001Wt00000PHVtpIAH', '001Wt00000PHVvRIAX']}, 'var_call_NR1tWPNgyZ2NJIL79qgHf4Q9': [{'Id': '001Wt00000PFj4zIAD', 'Name': 'NaviCorp Tech ', 'ShippingState': 'FL'}, {'Id': '001Wt00000PFt7TIAT', 'Name': 'TerraForm Engineering  ', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGRnYIAX', 'Name': 'AgroSmart Innovations', 'ShippingState': 'IA'}, {'Id': '001Wt00000PGSwYIAX', 'Name': 'GreenLeaf Engineering  ', 'ShippingState': 'IA'}, {'Id': '001Wt00000PGZZoIAP', 'Name': 'EnviroTech Solutions', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGZmfIAH', 'Name': 'Quantum Dynamics LLC', 'ShippingState': 'MI'}, {'Id': '001Wt00000PGaZDIA1', 'Name': 'Oceanic Innovation Labs  ', 'ShippingState': 'CA'}, {'Id': '001Wt00000PGoAaIAL', 'Name': 'TrueNorth Technologies', 'ShippingState': 'NJ'}, {'Id': '001Wt00000PGzM9IAL', 'Name': 'MediLux Solutions', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGzSaIAL', 'Name': 'TechFusion Inc.', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGzSbIAL', 'Name': 'AquaGuard Solutions   ', 'ShippingState': 'FL'}, {'Id': '001Wt00000PHVnNIAX', 'Name': 'BrightField Ventures', 'ShippingState': 'SC'}, {'Id': '001Wt00000PHVtpIAH', 'Name': 'EnergyNova Corp', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHVvRIAX', 'Name': 'AeroFusion Systems', 'ShippingState': 'TX'}]}

exec(code, env_args)
