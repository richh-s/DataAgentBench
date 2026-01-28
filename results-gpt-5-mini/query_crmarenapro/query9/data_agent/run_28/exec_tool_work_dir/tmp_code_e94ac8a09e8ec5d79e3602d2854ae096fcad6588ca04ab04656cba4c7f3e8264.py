code = """import json
cases = var_call_nuD8IC6UVS6GViAmVqRICbgh
accounts = var_call_gesdmzhtyYPrqgYmgWM2mg1W
# build mapping from cleaned account id to state
acc_map = {}
for a in accounts:
    aid = a.get('Id','')
    clean = aid.strip()
    while clean.startswith('#'):
        clean = clean[1:]
    acc_map[clean] = a.get('ShippingState')

# For each case, compute closure time in hours and assign quarter based on createddate
from datetime import datetime
import math

results = []
for c in cases:
    aid = c.get('accountid')
    if not aid:
        continue
    clean_aid = aid.strip()
    while clean_aid.startswith('#'):
        clean_aid = clean_aid[1:]
    state = acc_map.get(clean_aid)
    if not state:
        continue
    created = c.get('createddate')
    closed = c.get('closeddate')
    try:
        dt_created = datetime.strptime(created[:19], '%Y-%m-%dT%H:%M:%S')
        dt_closed = datetime.strptime(closed[:19], '%Y-%m-%dT%H:%M:%S')
    except Exception as e:
        continue
    diff_hours = (dt_closed - dt_created).total_seconds()/3600.0
    # determine quarter based on created date
    # quarters: Q1=Jan-Mar, Q2=Apr-Jun, Q3=Jul-Sep, Q4=Oct-Dec
    q_year = dt_created.year
    m = dt_created.month
    if m<=3:
        q = 1
    elif m<=6:
        q = 2
    elif m<=9:
        q = 3
    else:
        q = 4
    # Only include past 6 quarters from today's date 2022-10-26
    # Past 6 quarters ending with current quarter containing 2022-10-26 -> current quarter is Q4 2022
    # Past 6 quarters: Q4 2022, Q3 2022, Q2 2022, Q1 2022, Q4 2021, Q3 2021
    valid_quarters = set([(2022,4),(2022,3),(2022,2),(2022,1),(2021,4),(2021,3)])
    if (q_year, q) not in valid_quarters:
        continue
    results.append({'case_id': c.get('id'), 'state': state, 'created': created, 'closed': closed, 'hours': diff_hours, 'year': q_year, 'quarter': q})

# aggregate average closure time per state across the 6 quarters
from collections import defaultdict
agg = defaultdict(list)
for r in results:
    agg[r['state']].append(r['hours'])
avgs = []
for s, vals in agg.items():
    av = sum(vals)/len(vals)
    av = round(av,4)
    avgs.append({'state': s, 'avg_hours': av, 'count': len(vals)})
# find state with minimum avg_hours
if not avgs:
    out = {'error':'no data'}
else:
    avgs.sort(key=lambda x: (x['avg_hours'], -x['count']))
    best = avgs[0]
    out = {'best_state': best['state'], 'avg_hours': best['avg_hours'], 'count': best['count'], 'all': avgs}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_nuD8IC6UVS6GViAmVqRICbgh': [{'id': '500Wt00000DDPIsIAP', 'accountid': '#001Wt00000PGRnYIAX', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000'}, {'id': '#500Wt00000DDTERIA5', 'accountid': '001Wt00000PGzSaIAL', 'createddate': '2022-03-10T09:30:00.000+0000', 'closeddate': '2022-03-13T09:45:27.000+0000'}, {'id': '#500Wt00000DDYdwIAH', 'accountid': '001Wt00000PFj4zIAD', 'createddate': '2022-02-03T14:30:00.000+0000', 'closeddate': '2022-02-03T14:46:56.000+0000'}, {'id': '#500Wt00000DDYpHIAX', 'accountid': '#001Wt00000PHHXXIA5', 'createddate': '2022-09-05T11:15:00.000+0000', 'closeddate': '2022-09-05T11:42:09.000+0000'}, {'id': '#500Wt00000DDet1IAD', 'accountid': '001Wt00000PGzSbIAL', 'createddate': '2021-09-07T23:48:00.000+0000', 'closeddate': '2021-09-08T03:11:32.000+0000'}, {'id': '500Wt00000DDg1yIAD', 'accountid': '#001Wt00000PHVnNIAX', 'createddate': '2022-02-08T06:22:00.000+0000', 'closeddate': '2022-02-08T06:43:35.000+0000'}, {'id': '500Wt00000DDg1zIAD', 'accountid': '001Wt00000PGdzxIAD', 'createddate': '2022-04-17T14:20:00.000+0000', 'closeddate': '2022-04-17T14:37:58.000+0000'}, {'id': '500Wt00000DDg8RIAT', 'accountid': '001Wt00000PGZZoIAP', 'createddate': '2022-05-10T11:30:00.000+0000', 'closeddate': '2022-05-10T17:02:48.000+0000'}, {'id': '500Wt00000DDgLLIA1', 'accountid': '#001Wt00000PGZZoIAP', 'createddate': '2022-05-12T14:45:00.000+0000', 'closeddate': '2022-05-12T14:54:10.000+0000'}, {'id': '500Wt00000DDsKuIAL', 'accountid': '#001Wt00000PHVvRIAX', 'createddate': '2022-07-23T07:37:00.000+0000', 'closeddate': '2022-07-23T07:47:37.000+0000'}, {'id': '500Wt00000DDxVqIAL', 'accountid': '001Wt00000PHVvRIAX', 'createddate': '2021-09-15T09:10:00.000+0000', 'closeddate': '2021-09-15T09:50:35.000+0000'}, {'id': '500Wt00000DDzSnIAL', 'accountid': '001Wt00000PGaZCIA1', 'createddate': '2021-10-15T11:15:00.000+0000', 'closeddate': '2021-10-15T20:15:55.000+0000'}, {'id': '#500Wt00000DDzSoIAL', 'accountid': '001Wt00000PHR8gIAH', 'createddate': '2022-07-26T12:38:00.000+0000', 'closeddate': '2022-07-26T13:40:22.000+0000'}, {'id': '#500Wt00000DDzZFIA1', 'accountid': '001Wt00000PGoAaIAL', 'createddate': '2021-07-15T10:30:00.000+0000', 'closeddate': '2021-07-15T13:32:47.000+0000'}, {'id': '500Wt00000DDzarIAD', 'accountid': '#001Wt00000PGoAaIAL', 'createddate': '2021-10-08T08:07:00.000+0000', 'closeddate': '2021-10-08T08:43:11.000+0000'}, {'id': '500Wt00000DDzcTIAT', 'accountid': '001Wt00000PGRnYIAX', 'createddate': '2022-08-01T10:15:00.000+0000', 'closeddate': '2022-08-01T14:45:37.000+0000'}, {'id': '500Wt00000DDzfhIAD', 'accountid': '001Wt00000PGzM9IAL', 'createddate': '2022-03-04T09:45:00.000+0000', 'closeddate': '2022-03-05T10:25:32.000+0000'}, {'id': '#500Wt00000DE077IAD', 'accountid': '001Wt00000PGZmfIAH', 'createddate': '2021-07-22T09:45:00.000+0000', 'closeddate': '2021-07-22T10:00:58.000+0000'}, {'id': '500Wt00000DE08jIAD', 'accountid': '001Wt00000PGSwYIAX', 'createddate': '2021-09-16T11:00:00.000+0000', 'closeddate': '2021-09-16T11:14:27.000+0000'}, {'id': '#500Wt00000DE0FCIA1', 'accountid': '001Wt00000PHVvRIAX', 'createddate': '2021-09-05T11:15:00.000+0000', 'closeddate': '2021-09-05T11:25:45.000+0000'}, {'id': '500Wt00000DE0IPIA1', 'accountid': '001Wt00000PHVtpIAH', 'createddate': '2022-08-10T09:30:00.000+0000', 'closeddate': '2022-08-10T13:59:01.000+0000'}, {'id': '500Wt00000DE0QTIA1', 'accountid': '001Wt00000PFt7TIAT', 'createddate': '2022-02-02T15:30:45.000+0000', 'closeddate': '2022-02-03T10:17:46.000+0000'}, {'id': '500Wt00000DE0S5IAL', 'accountid': '001Wt00000PFt7TIAT', 'createddate': '2022-03-05T11:20:30.000+0000', 'closeddate': '2022-03-05T11:34:08.000+0000'}, {'id': '#500Wt00000DE0ThIAL', 'accountid': '#001Wt00000PGXrLIAX', 'createddate': '2021-10-02T10:30:00.000+0000', 'closeddate': '2021-10-03T13:27:49.000+0000'}, {'id': '500Wt00000DE0YXIA1', 'accountid': '#001Wt00000PGaZDIA1', 'createddate': '2022-02-24T19:20:00.000+0000', 'closeddate': '2022-02-25T04:35:46.000+0000'}], 'var_call_b5GIxNYtyxWZAYAgER2KCHXW': {'sql': "SELECT Id, ShippingState FROM Account WHERE REPLACE(Id, '#', '') IN ('001Wt00000PFj4zIAD','001Wt00000PFt7TIAT','001Wt00000PGRnYIAX','001Wt00000PGSwYIAX','001Wt00000PGXrLIAX','001Wt00000PGZZoIAP','001Wt00000PGZmfIAH','001Wt00000PGaZCIA1','001Wt00000PGaZDIA1','001Wt00000PGdzxIAD','001Wt00000PGoAaIAL','001Wt00000PGzM9IAL','001Wt00000PGzSaIAL','001Wt00000PGzSbIAL','001Wt00000PHHXXIA5','001Wt00000PHR8gIAH','001Wt00000PHVnNIAX','001Wt00000PHVtpIAH','001Wt00000PHVvRIAX');", 'count_ids': 19, 'ids': ['001Wt00000PFj4zIAD', '001Wt00000PFt7TIAT', '001Wt00000PGRnYIAX', '001Wt00000PGSwYIAX', '001Wt00000PGXrLIAX', '001Wt00000PGZZoIAP', '001Wt00000PGZmfIAH', '001Wt00000PGaZCIA1', '001Wt00000PGaZDIA1', '001Wt00000PGdzxIAD', '001Wt00000PGoAaIAL', '001Wt00000PGzM9IAL', '001Wt00000PGzSaIAL', '001Wt00000PGzSbIAL', '001Wt00000PHHXXIA5', '001Wt00000PHR8gIAH', '001Wt00000PHVnNIAX', '001Wt00000PHVtpIAH', '001Wt00000PHVvRIAX']}, 'var_call_gesdmzhtyYPrqgYmgWM2mg1W': [{'Id': '001Wt00000PFj4zIAD', 'ShippingState': 'FL'}, {'Id': '001Wt00000PFt7TIAT', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGRnYIAX', 'ShippingState': 'IA'}, {'Id': '001Wt00000PGSwYIAX', 'ShippingState': 'IA'}, {'Id': '#001Wt00000PGXrLIAX', 'ShippingState': 'NY'}, {'Id': '001Wt00000PGZZoIAP', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGZmfIAH', 'ShippingState': 'MI'}, {'Id': '#001Wt00000PGaZCIA1', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGaZDIA1', 'ShippingState': 'CA'}, {'Id': '#001Wt00000PGdzxIAD', 'ShippingState': 'FL'}, {'Id': '001Wt00000PGoAaIAL', 'ShippingState': 'NJ'}, {'Id': '001Wt00000PGzM9IAL', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGzSaIAL', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGzSbIAL', 'ShippingState': 'FL'}, {'Id': '#001Wt00000PHHXXIA5', 'ShippingState': 'TX'}, {'Id': '#001Wt00000PHR8gIAH', 'ShippingState': 'AZ'}, {'Id': '001Wt00000PHVnNIAX', 'ShippingState': 'SC'}, {'Id': '001Wt00000PHVtpIAH', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHVvRIAX', 'ShippingState': 'TX'}]}

exec(code, env_args)
