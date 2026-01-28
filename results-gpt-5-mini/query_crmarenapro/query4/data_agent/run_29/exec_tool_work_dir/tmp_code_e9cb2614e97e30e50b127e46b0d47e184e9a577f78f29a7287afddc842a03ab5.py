code = """import json
import pandas as pd
import statistics

# Load data from storage-provided variables
cases = var_call_hWF2EzBmlix9kx2oXzdwc0Y6
orderitems = json.load(open(var_call_FGAcOIH6axnjuFDaq8fUfc3Z, 'r'))

target = '01tWt000006hVJdIAM'

def clean(s):
    if s is None:
        return None
    return s.lstrip('#').strip()

# Map OrderItem Id -> Product2Id (cleaned)
oid_to_pid = {clean(o.get('Id')): clean(o.get('Product2Id')) for o in orderitems}

# Collect created dates for cases linked to the target product
created_dates = []
for c in cases:
    oid_raw = c.get('orderitemid__c')
    oid = clean(oid_raw)
    pid = oid_to_pid.get(oid)
    if pid == target:
        # parse createddate
        try:
            dt = pd.to_datetime(c.get('createddate'))
            # normalize to naive UTC by removing tzinfo
            if dt.tzinfo is not None:
                dt = dt.tz_convert('UTC').tz_localize(None)
            created_dates.append(dt)
        except Exception:
            continue

# Define analysis window (as used in earlier query)
start = pd.to_datetime('2020-06-10')
end = pd.to_datetime('2021-04-10')

# Filter dates within window
created_dates = [d for d in created_dates if (d >= start) and (d <= end)]

# If no cases, result is None
if not created_dates:
    result = None
else:
    s = pd.Series(created_dates)
    # Build inclusive list of months from start to end (YYYY-MM)
    start_month = start.replace(day=1)
    end_month = end.replace(day=1)
    months = []
    cur = start_month
    while cur <= end_month:
        months.append(cur.strftime('%Y-%m'))
        if cur.month == 12:
            cur = cur.replace(year=cur.year+1, month=1)
        else:
            cur = cur.replace(month=cur.month+1)
    # Count cases per month
    month_keys = s.dt.strftime('%Y-%m')
    counts = {m: int((month_keys == m).sum()) for m in months}
    vals = list(counts.values())
    mean = statistics.mean(vals) if vals else 0
    stdev = statistics.pstdev(vals) if len(vals) > 0 else 0
    # Determine max month
    max_month_key, max_count = max(counts.items(), key=lambda x: x[1])
    # Check significance: max > mean + 2*stdev
    if stdev > 0 and max_count > mean + 2 * stdev:
        month_name = pd.to_datetime(max_month_key + '-01').strftime('%B')
        result = month_name
    else:
        result = None

print("__RESULT__:")
print(json.dumps(result if result is not None else "None"))"""

env_args = {'var_call_hWF2EzBmlix9kx2oXzdwc0Y6': [{'id': '500Wt00000DDDtTIAX', 'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDPM6IAP', 'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDRB2IAP', 'createddate': '2021-01-10T09:30:00.000+0000', 'orderitemid__c': '802Wt00000797axIAA'}, {'id': '500Wt00000DDRVzIAP', 'createddate': '2020-09-05T09:15:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDYpGIAX', 'createddate': '2021-03-31T11:41:00.000+0000', 'orderitemid__c': '802Wt00000798OvIAI'}, {'id': '#500Wt00000DDZmsIAH', 'createddate': '2020-07-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000795XwIAI'}, {'id': '500Wt00000DDeoCIAT', 'createddate': '2020-07-01T15:30:00.000+0000', 'orderitemid__c': '802Wt00000794bTIAQ'}, {'id': '#500Wt00000DDfvXIAT', 'createddate': '2021-03-24T18:04:00.000+0000', 'orderitemid__c': '802Wt00000796dGIAQ'}, {'id': '#500Wt00000DDg8QIAT', 'createddate': '2021-03-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDsG4IAL', 'createddate': '2020-11-05T11:00:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDt7HIAT', 'createddate': '2021-02-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}, {'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000', 'orderitemid__c': '802Wt00000799o1IAA'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DDymuIAD', 'createddate': '2020-10-01T14:30:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDz6GIAT', 'createddate': '2020-09-03T14:45:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '#500Wt00000DDzKjIAL', 'createddate': '2020-10-22T03:55:00.000+0000', 'orderitemid__c': '802Wt00000796JtIAI'}, {'id': '500Wt00000DDzmAIAT', 'createddate': '2021-02-20T14:30:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DE05VIAT', 'createddate': '2021-01-03T15:30:00.000+0000', 'orderitemid__c': '802Wt00000799b7IAA'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0DZIA1', 'createddate': '2020-11-10T22:14:00.000+0000', 'orderitemid__c': '802Wt00000799uTIAQ'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0WwIAL', 'createddate': '2021-03-10T15:45:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}], 'var_call_FGAcOIH6axnjuFDaq8fUfc3Z': 'file_storage/call_FGAcOIH6axnjuFDaq8fUfc3Z.json'}

exec(code, env_args)
