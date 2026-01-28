code = """import json
cases = var_call_h6QGZYCs5FknOrhFeOQAzNht
accounts = var_call_VUjGXwvwupY6M2QKgCF2iPzb
# build dict of account id -> state
acct_state = {a['Id'].strip(): (a.get('ShippingState') or '').strip() for a in accounts}

# prepare list of case records with state and compute closure time in seconds if closed
from datetime import datetime

out = []
for c in cases:
    acct = c.get('accountid')
    if not acct or acct.strip().lower()=='none':
        continue
    acct = acct.strip()
    if acct.startswith('#'):
        acct = acct[1:]
    state = acct_state.get(acct)
    if not state:
        continue
    created = c.get('createddate')
    closed = c.get('closeddate')
    # parse datetimes, closed may be 'None'
    try:
        created_dt = datetime.strptime(created[:19], '%Y-%m-%dT%H:%M:%S')
    except:
        continue
    if not closed or closed.strip().lower()=='none':
        # skip open cases for closure time calc
        continue
    try:
        closed_dt = datetime.strptime(closed[:19], '%Y-%m-%dT%H:%M:%S')
    except:
        continue
    delta = (closed_dt - created_dt).total_seconds()
    if delta < 0:
        # ignore negative
        continue
    out.append({'case_id': c['id'].strip(), 'account_id': acct, 'state': state, 'created': created, 'closed': closed, 'closure_seconds': delta})

# Now filter to past 6 quarters from today's date 2022-10-26 meaning last 6 quarters inclusive of current quarter?
# Past 6 quarters back from 2022-10-26 covers from 2021-01-01? Let's compute quarters: Q4 2021? But typically past 6 quarters from current date includes current Q4 2022 and previous 5 quarters back to Q1 2021? Today's date 2022-10-26 is in Q4 2022; past 6 quarters: Q4 2022, Q3 2022, Q2 2022, Q1 2022, Q4 2021, Q3 2021. So start date is 2021-07-01.
start = datetime(2021,7,1)
end = datetime(2022,10,26,23,59,59)
out2 = [r for r in out if datetime.strptime(r['created'][:19], '%Y-%m-%dT%H:%M:%S')>=start and datetime.strptime(r['created'][:19], '%Y-%m-%dT%H:%M:%S')<=end]

# compute average closure time per state
from collections import defaultdict
sums = defaultdict(float)
counts = defaultdict(int)
for r in out2:
    sums[r['state']] += r['closure_seconds']
    counts[r['state']] += 1

avg = []
for s in sums:
    avg.append({'state': s, 'avg_seconds': sums[s]/counts[s], 'count': counts[s]})

# sort by avg_seconds ascending
avg_sorted = sorted(avg, key=lambda x: x['avg_seconds'])
# get top state (smallest avg)
if avg_sorted:
    top = avg_sorted[0]['state']
else:
    top = None

print('__RESULT__:')
print(json.dumps({'avg_sorted': avg_sorted, 'top_state': top}))"""

env_args = {'var_call_h6QGZYCs5FknOrhFeOQAzNht': [{'id': '500Wt00000DDPIsIAP', 'accountid': '#001Wt00000PGRnYIAX', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000'}, {'id': '500Wt00000DDPZ0IAP', 'accountid': '001Wt00000PGdzxIAD', 'createddate': '2022-04-18T10:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDPsOIAX', 'accountid': '001Wt00000PHRF9IAP', 'createddate': '2021-07-06T14:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDQoUIAX', 'accountid': '#001Wt00000PGzM9IAL', 'createddate': '2021-09-15T10:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDTEQIA5', 'accountid': '001Wt00000PGzM9IAL', 'createddate': '2022-03-02T10:15:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDTERIA5', 'accountid': '001Wt00000PGzSaIAL', 'createddate': '2022-03-10T09:30:00.000+0000', 'closeddate': '2022-03-13T09:45:27.000+0000'}, {'id': '500Wt00000DDTHfIAP', 'accountid': '#001Wt00000PGaZCIA1', 'createddate': '2021-10-05T14:45:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDYdwIAH', 'accountid': '001Wt00000PFj4zIAD', 'createddate': '2022-02-03T14:30:00.000+0000', 'closeddate': '2022-02-03T14:46:56.000+0000'}, {'id': '500Wt00000DDzRCIA1', 'accountid': '#001Wt00000PGzM9IAL', 'createddate': '2021-09-20T15:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDYipIAH', 'accountid': '001Wt00000PGzSaIAL', 'createddate': '2022-03-15T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDYpHIAX', 'accountid': '#001Wt00000PHHXXIA5', 'createddate': '2022-09-05T11:15:00.000+0000', 'closeddate': '2022-09-05T11:42:09.000+0000'}, {'id': '500Wt00000DDZ0VIAX', 'accountid': '#001Wt00000PGSwYIAX', 'createddate': '2021-10-15T13:46:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDZ5LIAX', 'accountid': '001Wt00000PH9ITIA1', 'createddate': '2021-11-11T12:13:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDZtLIAX', 'accountid': '#001Wt00000PFj50IAD', 'createddate': '2022-05-15T14:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDet1IAD', 'accountid': '001Wt00000PGzSbIAL', 'createddate': '2021-09-07T23:48:00.000+0000', 'closeddate': '2021-09-08T03:11:32.000+0000'}, {'id': '500Wt00000DDfHCIA1', 'accountid': '#001Wt00000PGZmfIAH', 'createddate': '2021-07-23T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDfYxIAL', 'accountid': '001Wt00000PFj50IAD', 'createddate': '2022-04-01T10:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDg1yIAD', 'accountid': '#001Wt00000PHVnNIAX', 'createddate': '2022-02-08T06:22:00.000+0000', 'closeddate': '2022-02-08T06:43:35.000+0000'}, {'id': '500Wt00000DDg1zIAD', 'accountid': '001Wt00000PGdzxIAD', 'createddate': '2022-04-17T14:20:00.000+0000', 'closeddate': '2022-04-17T14:37:58.000+0000'}, {'id': '500Wt00000DDg8RIAT', 'accountid': '001Wt00000PGZZoIAP', 'createddate': '2022-05-10T11:30:00.000+0000', 'closeddate': '2022-05-10T17:02:48.000+0000'}, {'id': '500Wt00000DDgLLIA1', 'accountid': '#001Wt00000PGZZoIAP', 'createddate': '2022-05-12T14:45:00.000+0000', 'closeddate': '2022-05-12T14:54:10.000+0000'}, {'id': '500Wt00000DDnt7IAD', 'accountid': '001Wt00000PHVvRIAX', 'createddate': '2021-09-02T10:30:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDsKtIAL', 'accountid': '001Wt00000PHVvRIAX', 'createddate': '2021-08-24T13:25:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDsKuIAL', 'accountid': '#001Wt00000PHVvRIAX', 'createddate': '2022-07-23T07:37:00.000+0000', 'closeddate': '2022-07-23T07:47:37.000+0000'}, {'id': '500Wt00000DDt7GIAT', 'accountid': '001Wt00000PHHXXIA5', 'createddate': '2021-11-01T10:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDxScIAL', 'accountid': '001Wt00000PGtdJIAT', 'createddate': '2022-10-01T14:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDxVqIAL', 'accountid': '001Wt00000PHVvRIAX', 'createddate': '2021-09-15T09:10:00.000+0000', 'closeddate': '2021-09-15T09:50:35.000+0000'}, {'id': '500Wt00000DDxduIAD', 'accountid': '001Wt00000PGtdJIAT', 'createddate': '2022-09-16T09:30:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDyznIAD', 'accountid': '001Wt00000PGaZCIA1', 'createddate': '2022-09-22T19:28:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzJ8IAL', 'accountid': '001Wt00000PHHXXIA5', 'createddate': '2022-09-03T15:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzSnIAL', 'accountid': '001Wt00000PGaZCIA1', 'createddate': '2021-10-15T11:15:00.000+0000', 'closeddate': '2021-10-15T20:15:55.000+0000'}, {'id': '#500Wt00000DDzSoIAL', 'accountid': '001Wt00000PHR8gIAH', 'createddate': '2022-07-26T12:38:00.000+0000', 'closeddate': '2022-07-26T13:40:22.000+0000'}, {'id': '#500Wt00000DDzUQIA1', 'accountid': '001Wt00000PFsmbIAD', 'createddate': '2022-03-04T11:30:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzW3IAL', 'accountid': '001Wt00000PGXrNIAX', 'createddate': '2021-11-02T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzXeIAL', 'accountid': '001Wt00000PHVtpIAH', 'createddate': '2022-09-05T14:45:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzZFIA1', 'accountid': '001Wt00000PGoAaIAL', 'createddate': '2021-07-15T10:30:00.000+0000', 'closeddate': '2021-07-15T13:32:47.000+0000'}, {'id': '500Wt00000DDzarIAD', 'accountid': '#001Wt00000PGoAaIAL', 'createddate': '2021-10-08T08:07:00.000+0000', 'closeddate': '2021-10-08T08:43:11.000+0000'}, {'id': '500Wt00000DDzcTIAT', 'accountid': '001Wt00000PGRnYIAX', 'createddate': '2022-08-01T10:15:00.000+0000', 'closeddate': '2022-08-01T14:45:37.000+0000'}, {'id': '#500Wt00000DDze5IAD', 'accountid': '001Wt00000PHR8gIAH', 'createddate': '2021-10-22T10:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzfhIAD', 'accountid': '001Wt00000PGzM9IAL', 'createddate': '2022-03-04T09:45:00.000+0000', 'closeddate': '2022-03-05T10:25:32.000+0000'}, {'id': '500Wt00000DDzm9IAD', 'accountid': '001Wt00000PFsmbIAD', 'createddate': '2022-03-03T10:00:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DDzmBIAT', 'accountid': '#001Wt00000PGZgHIAX', 'createddate': '2022-01-28T02:41:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzmCIAT', 'accountid': '#001Wt00000PHVvRIAX', 'createddate': '2021-09-10T14:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzr2IAD', 'accountid': '001Wt00000PGXrLIAX', 'createddate': '2022-01-10T11:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DDzxRIAT', 'accountid': '#001Wt00000PGdzxIAD', 'createddate': '2022-04-16T09:45:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DE00hIAD', 'accountid': '001Wt00000PGXrLIAX', 'createddate': '2021-11-15T14:45:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DE077IAD', 'accountid': '001Wt00000PGZmfIAH', 'createddate': '2021-07-22T09:45:00.000+0000', 'closeddate': '2021-07-22T10:00:58.000+0000'}, {'id': '500Wt00000DE079IAD', 'accountid': '001Wt00000PHRF9IAP', 'createddate': '2021-07-05T10:15:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE07AIAT', 'accountid': '001Wt00000PGXrNIAX', 'createddate': '2021-11-02T09:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE08jIAD', 'accountid': '001Wt00000PGSwYIAX', 'createddate': '2021-09-16T11:00:00.000+0000', 'closeddate': '2021-09-16T11:14:27.000+0000'}, {'id': '500Wt00000DE0ALIA1', 'accountid': '#001Wt00000PGSwYIAX', 'createddate': '2021-09-17T09:45:00.000+0000', 'closeddate': 'None'}, {'id': '#500Wt00000DE0FCIA1', 'accountid': '001Wt00000PHVvRIAX', 'createddate': '2021-09-05T11:15:00.000+0000', 'closeddate': '2021-09-05T11:25:45.000+0000'}, {'id': '500Wt00000DE0IPIA1', 'accountid': '001Wt00000PHVtpIAH', 'createddate': '2022-08-10T09:30:00.000+0000', 'closeddate': '2022-08-10T13:59:01.000+0000'}, {'id': '500Wt00000DE0K1IAL', 'accountid': '001Wt00000PHVtpIAH', 'createddate': '2022-10-15T11:00:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE0QTIA1', 'accountid': '001Wt00000PFt7TIAT', 'createddate': '2022-02-02T15:30:45.000+0000', 'closeddate': '2022-02-03T10:17:46.000+0000'}, {'id': '500Wt00000DE0S5IAL', 'accountid': '001Wt00000PFt7TIAT', 'createddate': '2022-03-05T11:20:30.000+0000', 'closeddate': '2022-03-05T11:34:08.000+0000'}, {'id': '#500Wt00000DE0ThIAL', 'accountid': '#001Wt00000PGXrLIAX', 'createddate': '2021-10-02T10:30:00.000+0000', 'closeddate': '2021-10-03T13:27:49.000+0000'}, {'id': '500Wt00000DE0WvIAL', 'accountid': '001Wt00000PHRF9IAP', 'createddate': '2021-07-07T09:45:00.000+0000', 'closeddate': 'None'}, {'id': '500Wt00000DE0YXIA1', 'accountid': '#001Wt00000PGaZDIA1', 'createddate': '2022-02-24T19:20:00.000+0000', 'closeddate': '2022-02-25T04:35:46.000+0000'}], 'var_call_eA6lF2w4rSsYeL1VmUbtMQWx': {'ids': ['001Wt00000PFj4zIAD', '001Wt00000PFj50IAD', '001Wt00000PFsmbIAD', '001Wt00000PFt7TIAT', '001Wt00000PGRnYIAX', '001Wt00000PGSwYIAX', '001Wt00000PGXrLIAX', '001Wt00000PGXrNIAX', '001Wt00000PGZZoIAP', '001Wt00000PGZgHIAX', '001Wt00000PGZmfIAH', '001Wt00000PGaZCIA1', '001Wt00000PGaZDIA1', '001Wt00000PGdzxIAD', '001Wt00000PGoAaIAL', '001Wt00000PGtdJIAT', '001Wt00000PGzM9IAL', '001Wt00000PGzSaIAL', '001Wt00000PGzSbIAL', '001Wt00000PH9ITIA1', '001Wt00000PHHXXIA5', '001Wt00000PHR8gIAH', '001Wt00000PHRF9IAP', '001Wt00000PHVnNIAX', '001Wt00000PHVtpIAH', '001Wt00000PHVvRIAX'], 'in_clause': "'001Wt00000PFj4zIAD','001Wt00000PFj50IAD','001Wt00000PFsmbIAD','001Wt00000PFt7TIAT','001Wt00000PGRnYIAX','001Wt00000PGSwYIAX','001Wt00000PGXrLIAX','001Wt00000PGXrNIAX','001Wt00000PGZZoIAP','001Wt00000PGZgHIAX','001Wt00000PGZmfIAH','001Wt00000PGaZCIA1','001Wt00000PGaZDIA1','001Wt00000PGdzxIAD','001Wt00000PGoAaIAL','001Wt00000PGtdJIAT','001Wt00000PGzM9IAL','001Wt00000PGzSaIAL','001Wt00000PGzSbIAL','001Wt00000PH9ITIA1','001Wt00000PHHXXIA5','001Wt00000PHR8gIAH','001Wt00000PHRF9IAP','001Wt00000PHVnNIAX','001Wt00000PHVtpIAH','001Wt00000PHVvRIAX'"}, 'var_call_VUjGXwvwupY6M2QKgCF2iPzb': [{'Id': '001Wt00000PFj4zIAD', 'Name': 'NaviCorp Tech ', 'ShippingState': 'FL'}, {'Id': '001Wt00000PFj50IAD', 'Name': 'FusionTech Systems', 'ShippingState': 'TX'}, {'Id': '001Wt00000PFsmbIAD', 'Name': 'Innovative Robotics', 'ShippingState': 'NV'}, {'Id': '001Wt00000PFt7TIAT', 'Name': 'TerraForm Engineering  ', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGRnYIAX', 'Name': 'AgroSmart Innovations', 'ShippingState': 'IA'}, {'Id': '001Wt00000PGSwYIAX', 'Name': 'GreenLeaf Engineering  ', 'ShippingState': 'IA'}, {'Id': '001Wt00000PGXrNIAX', 'Name': 'FutureTech Innovations', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGZZoIAP', 'Name': 'EnviroTech Solutions', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGZgHIAX', 'Name': 'TechGrove Systems', 'ShippingState': 'UT'}, {'Id': '001Wt00000PGZmfIAH', 'Name': 'Quantum Dynamics LLC', 'ShippingState': 'MI'}, {'Id': '001Wt00000PGaZDIA1', 'Name': 'Oceanic Innovation Labs  ', 'ShippingState': 'CA'}, {'Id': '001Wt00000PGoAaIAL', 'Name': 'TrueNorth Technologies', 'ShippingState': 'NJ'}, {'Id': '001Wt00000PGtdJIAT', 'Name': 'Quantum Innovations Inc.', 'ShippingState': 'IL'}, {'Id': '001Wt00000PGzM9IAL', 'Name': 'MediLux Solutions', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGzSaIAL', 'Name': 'TechFusion Inc.', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGzSbIAL', 'Name': 'AquaGuard Solutions   ', 'ShippingState': 'FL'}, {'Id': '001Wt00000PHRF9IAP', 'Name': 'Green Circuitry LLC', 'ShippingState': 'WA'}, {'Id': '001Wt00000PHVnNIAX', 'Name': 'BrightField Ventures', 'ShippingState': 'SC'}, {'Id': '001Wt00000PHVtpIAH', 'Name': 'EnergyNova Corp', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHVvRIAX', 'Name': 'AeroFusion Systems', 'ShippingState': 'TX'}]}

exec(code, env_args)
