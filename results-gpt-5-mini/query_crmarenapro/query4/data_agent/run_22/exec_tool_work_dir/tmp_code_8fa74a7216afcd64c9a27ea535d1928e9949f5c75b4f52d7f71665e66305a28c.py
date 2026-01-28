code = """import pandas as pd
import json
from datetime import datetime

# Load data from previous tool calls
cases = var_call_VYdBwolJWlYH4m28T0lalTlN
order_items = var_call_PwzhSes8O07E7fEe201jCTv0

# Normalize IDs: remove leading '#' and surrounding whitespace
def norm_id(s):
    if s is None:
        return None
    return s.strip().lstrip('#').strip()

order_ids = set()
for r in order_items:
    if 'Id' in r:
        order_ids.add(norm_id(r['Id']))

# Reference date and months list (past 10 months including reference month)
ref_date = datetime(2021,4,10)
months = []  # list of (year, month) tuples from most recent to older
y = ref_date.year
m = ref_date.month
for i in range(10):
    months.append((y, m))
    # move back one month
    m -= 1
    if m == 0:
        m = 12
        y -= 1
# months currently from most recent to older; reverse to older->recent for chronology
months = list(reversed(months))

# Map (year,month) to month name
ym_to_name = {(y,m): datetime(y,m,1).strftime('%B') for (y,m) in months}

# Initialize counts with zeros for each month
counts = {ym_to_name[(y,m)]: 0 for (y,m) in months}

# Process cases
for c in cases:
    oid = c.get('orderitemid__c')
    if oid is None:
        continue
    if norm_id(oid) not in order_ids:
        continue
    cd = c.get('createddate')
    if cd is None:
        continue
    # parse created date robustly
    try:
        dt = pd.to_datetime(cd)
    except Exception:
        continue
    ymd = (dt.year, dt.month)
    if ymd in ym_to_name:
        counts[ym_to_name[ymd]] += 1

# Prepare list of counts in chronological order (older to recent)
ordered_month_names = [ym_to_name[(y,m)] for (y,m) in months]
ordered_counts = [counts[name] for name in ordered_month_names]

# Compute mean and std using pandas
s = pd.Series(ordered_counts)
mean = float(s.mean())
std = float(s.std(ddof=0))  # population std
threshold = mean + 2 * std

result_month = None
if len(s) > 0:
    max_count = int(s.max())
    # check if a unique month has the max and exceeds threshold
    max_indices = [i for i,v in enumerate(ordered_counts) if v == max_count]
    if len(max_indices) == 1 and max_count > threshold:
        result_month = ordered_month_names[max_indices[0]]

# If no month meets criteria, return "None"
if result_month is None:
    out = "None"
else:
    out = result_month

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_KtCuGsREsGlvbFjJatOjPdUP': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_VYdBwolJWlYH4m28T0lalTlN': [{'id': '500Wt00000DDDtTIAX', 'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDPM6IAP', 'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDRB2IAP', 'createddate': '2021-01-10T09:30:00.000+0000', 'orderitemid__c': '802Wt00000797axIAA'}, {'id': '500Wt00000DDRVzIAP', 'createddate': '2020-09-05T09:15:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDYpGIAX', 'createddate': '2021-03-31T11:41:00.000+0000', 'orderitemid__c': '802Wt00000798OvIAI'}, {'id': '#500Wt00000DDZmsIAH', 'createddate': '2020-07-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000795XwIAI'}, {'id': '500Wt00000DDeoCIAT', 'createddate': '2020-07-01T15:30:00.000+0000', 'orderitemid__c': '802Wt00000794bTIAQ'}, {'id': '#500Wt00000DDfvXIAT', 'createddate': '2021-03-24T18:04:00.000+0000', 'orderitemid__c': '802Wt00000796dGIAQ'}, {'id': '#500Wt00000DDg8QIAT', 'createddate': '2021-03-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDsG4IAL', 'createddate': '2020-11-05T11:00:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDt7HIAT', 'createddate': '2021-02-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}, {'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000', 'orderitemid__c': '802Wt00000799o1IAA'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DDymuIAD', 'createddate': '2020-10-01T14:30:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDz6GIAT', 'createddate': '2020-09-03T14:45:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '#500Wt00000DDzKjIAL', 'createddate': '2020-10-22T03:55:00.000+0000', 'orderitemid__c': '802Wt00000796JtIAI'}, {'id': '500Wt00000DDzmAIAT', 'createddate': '2021-02-20T14:30:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DE05VIAT', 'createddate': '2021-01-03T15:30:00.000+0000', 'orderitemid__c': '802Wt00000799b7IAA'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0DZIA1', 'createddate': '2020-11-10T22:14:00.000+0000', 'orderitemid__c': '802Wt00000799uTIAQ'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0WwIAL', 'createddate': '2021-03-10T15:45:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}], 'var_call_PwzhSes8O07E7fEe201jCTv0': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
