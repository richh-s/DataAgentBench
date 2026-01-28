code = """import json
from datetime import datetime, timezone
cases = var_call_NN7zqpYmHCgFHsqYwXqj6y1A
acct_states = {r['Id'].strip(): r['ShippingState'].strip() for r in var_call_pdoXelaOscMCvcbKH8x2t7W5}
# parse dates manually

def parse_dt(s):
    # s like 2022-08-05T14:30:00.000+0000
    # convert +0000 to +00:00
    if s is None:
        return None
    s2 = s
    if s2.endswith('+0000'):
        s2 = s2[:-5]+'+00:00'
    try:
        return datetime.fromisoformat(s2)
    except Exception:
        # fallback
        try:
            # remove timezone and parse as naive then set tzinfo=UTC
            if '+' in s2:
                s3 = s2.split('+')[0]
                dt = datetime.fromisoformat(s3)
                return dt.replace(tzinfo=timezone.utc)
        except:
            return None

case_list = []
for r in cases:
    aid = r.get('accountid')
    if not aid:
        continue
    nid = aid.strip().lstrip('#').strip()
    state = acct_states.get(nid)
    if not state:
        continue
    cd = r.get('createddate')
    cld = r.get('closeddate')
    created = parse_dt(cd)
    closed = parse_dt(cld)
    if not created or not closed:
        continue
    # ensure both are timezone-aware
    if created.tzinfo is None:
        created = created.replace(tzinfo=timezone.utc)
    if closed.tzinfo is None:
        closed = closed.replace(tzinfo=timezone.utc)
    duration_hours = (closed - created).total_seconds()/3600.0
    case_list.append({'id': r.get('id'), 'state': state, 'duration_hours': duration_hours, 'createddate': cd})

# Filter to last 6 quarters from 2022-10-26
end_date = datetime(2022,10,26, tzinfo=timezone.utc)
from dateutil.relativedelta import relativedelta
start_date = end_date - relativedelta(months=18)
filtered = [c for c in case_list if parse_dt(c['createddate']) >= start_date and parse_dt(c['createddate']) <= end_date]

# Compute average duration per state
from collections import defaultdict
state_sums = defaultdict(list)
for c in filtered:
    state_sums[c['state']].append(c['duration_hours'])
state_avgs = {s: sum(v)/len(v) for s,v in state_sums.items() if len(v)>0}
# find state with minimal avg duration
if not state_avgs:
    result = None
else:
    best_state = min(state_avgs.items(), key=lambda x: x[1])[0]
    result = best_state

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NN7zqpYmHCgFHsqYwXqj6y1A': [{'id': '500Wt00000DDPIsIAP', 'accountid': '#001Wt00000PGRnYIAX', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000'}, {'id': '#500Wt00000DDTERIA5', 'accountid': '001Wt00000PGzSaIAL', 'createddate': '2022-03-10T09:30:00.000+0000', 'closeddate': '2022-03-13T09:45:27.000+0000'}, {'id': '#500Wt00000DDYdwIAH', 'accountid': '001Wt00000PFj4zIAD', 'createddate': '2022-02-03T14:30:00.000+0000', 'closeddate': '2022-02-03T14:46:56.000+0000'}, {'id': '#500Wt00000DDYpHIAX', 'accountid': '#001Wt00000PHHXXIA5', 'createddate': '2022-09-05T11:15:00.000+0000', 'closeddate': '2022-09-05T11:42:09.000+0000'}, {'id': '#500Wt00000DDet1IAD', 'accountid': '001Wt00000PGzSbIAL', 'createddate': '2021-09-07T23:48:00.000+0000', 'closeddate': '2021-09-08T03:11:32.000+0000'}, {'id': '500Wt00000DDg1yIAD', 'accountid': '#001Wt00000PHVnNIAX', 'createddate': '2022-02-08T06:22:00.000+0000', 'closeddate': '2022-02-08T06:43:35.000+0000'}, {'id': '500Wt00000DDg1zIAD', 'accountid': '001Wt00000PGdzxIAD', 'createddate': '2022-04-17T14:20:00.000+0000', 'closeddate': '2022-04-17T14:37:58.000+0000'}, {'id': '500Wt00000DDg8RIAT', 'accountid': '001Wt00000PGZZoIAP', 'createddate': '2022-05-10T11:30:00.000+0000', 'closeddate': '2022-05-10T17:02:48.000+0000'}, {'id': '500Wt00000DDgLLIA1', 'accountid': '#001Wt00000PGZZoIAP', 'createddate': '2022-05-12T14:45:00.000+0000', 'closeddate': '2022-05-12T14:54:10.000+0000'}, {'id': '500Wt00000DDsKuIAL', 'accountid': '#001Wt00000PHVvRIAX', 'createddate': '2022-07-23T07:37:00.000+0000', 'closeddate': '2022-07-23T07:47:37.000+0000'}, {'id': '500Wt00000DDxVqIAL', 'accountid': '001Wt00000PHVvRIAX', 'createddate': '2021-09-15T09:10:00.000+0000', 'closeddate': '2021-09-15T09:50:35.000+0000'}, {'id': '500Wt00000DDzSnIAL', 'accountid': '001Wt00000PGaZCIA1', 'createddate': '2021-10-15T11:15:00.000+0000', 'closeddate': '2021-10-15T20:15:55.000+0000'}, {'id': '#500Wt00000DDzSoIAL', 'accountid': '001Wt00000PHR8gIAH', 'createddate': '2022-07-26T12:38:00.000+0000', 'closeddate': '2022-07-26T13:40:22.000+0000'}, {'id': '#500Wt00000DDzZFIA1', 'accountid': '001Wt00000PGoAaIAL', 'createddate': '2021-07-15T10:30:00.000+0000', 'closeddate': '2021-07-15T13:32:47.000+0000'}, {'id': '500Wt00000DDzarIAD', 'accountid': '#001Wt00000PGoAaIAL', 'createddate': '2021-10-08T08:07:00.000+0000', 'closeddate': '2021-10-08T08:43:11.000+0000'}, {'id': '500Wt00000DDzcTIAT', 'accountid': '001Wt00000PGRnYIAX', 'createddate': '2022-08-01T10:15:00.000+0000', 'closeddate': '2022-08-01T14:45:37.000+0000'}, {'id': '500Wt00000DDzfhIAD', 'accountid': '001Wt00000PGzM9IAL', 'createddate': '2022-03-04T09:45:00.000+0000', 'closeddate': '2022-03-05T10:25:32.000+0000'}, {'id': '#500Wt00000DE077IAD', 'accountid': '001Wt00000PGZmfIAH', 'createddate': '2021-07-22T09:45:00.000+0000', 'closeddate': '2021-07-22T10:00:58.000+0000'}, {'id': '500Wt00000DE08jIAD', 'accountid': '001Wt00000PGSwYIAX', 'createddate': '2021-09-16T11:00:00.000+0000', 'closeddate': '2021-09-16T11:14:27.000+0000'}, {'id': '#500Wt00000DE0FCIA1', 'accountid': '001Wt00000PHVvRIAX', 'createddate': '2021-09-05T11:15:00.000+0000', 'closeddate': '2021-09-05T11:25:45.000+0000'}, {'id': '500Wt00000DE0IPIA1', 'accountid': '001Wt00000PHVtpIAH', 'createddate': '2022-08-10T09:30:00.000+0000', 'closeddate': '2022-08-10T13:59:01.000+0000'}, {'id': '500Wt00000DE0QTIA1', 'accountid': '001Wt00000PFt7TIAT', 'createddate': '2022-02-02T15:30:45.000+0000', 'closeddate': '2022-02-03T10:17:46.000+0000'}, {'id': '500Wt00000DE0S5IAL', 'accountid': '001Wt00000PFt7TIAT', 'createddate': '2022-03-05T11:20:30.000+0000', 'closeddate': '2022-03-05T11:34:08.000+0000'}, {'id': '#500Wt00000DE0ThIAL', 'accountid': '#001Wt00000PGXrLIAX', 'createddate': '2021-10-02T10:30:00.000+0000', 'closeddate': '2021-10-03T13:27:49.000+0000'}, {'id': '500Wt00000DE0YXIA1', 'accountid': '#001Wt00000PGaZDIA1', 'createddate': '2022-02-24T19:20:00.000+0000', 'closeddate': '2022-02-25T04:35:46.000+0000'}], 'var_call_bN5KFhiyy7YG6nJAM7B3Bu1U': ['001Wt00000PFj4zIAD', '001Wt00000PFt7TIAT', '001Wt00000PGRnYIAX', '001Wt00000PGSwYIAX', '001Wt00000PGXrLIAX', '001Wt00000PGZZoIAP', '001Wt00000PGZmfIAH', '001Wt00000PGaZCIA1', '001Wt00000PGaZDIA1', '001Wt00000PGdzxIAD', '001Wt00000PGoAaIAL', '001Wt00000PGzM9IAL', '001Wt00000PGzSaIAL', '001Wt00000PGzSbIAL', '001Wt00000PHHXXIA5', '001Wt00000PHR8gIAH', '001Wt00000PHVnNIAX', '001Wt00000PHVtpIAH', '001Wt00000PHVvRIAX'], 'var_call_pdoXelaOscMCvcbKH8x2t7W5': [{'Id': '001Wt00000PFj4zIAD', 'ShippingState': 'FL'}, {'Id': '001Wt00000PFt7TIAT', 'ShippingState': 'CO'}, {'Id': '001Wt00000PGRnYIAX', 'ShippingState': 'IA'}, {'Id': '001Wt00000PGSwYIAX', 'ShippingState': 'IA'}, {'Id': '001Wt00000PGZZoIAP', 'ShippingState': 'OR'}, {'Id': '001Wt00000PGZmfIAH', 'ShippingState': 'MI'}, {'Id': '001Wt00000PGaZDIA1', 'ShippingState': 'CA'}, {'Id': '001Wt00000PGoAaIAL', 'ShippingState': 'NJ'}, {'Id': '001Wt00000PGzM9IAL', 'ShippingState': 'GA'}, {'Id': '001Wt00000PGzSaIAL', 'ShippingState': 'WA'}, {'Id': '001Wt00000PGzSbIAL', 'ShippingState': 'FL'}, {'Id': '001Wt00000PHVnNIAX', 'ShippingState': 'SC'}, {'Id': '001Wt00000PHVtpIAH', 'ShippingState': 'TX'}, {'Id': '001Wt00000PHVvRIAX', 'ShippingState': 'TX'}]}

exec(code, env_args)
