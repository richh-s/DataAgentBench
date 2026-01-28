code = """import json
from datetime import datetime
import math

cases = var_call_GluC9u81D8MrVWff2nLwS12h
orderitems = var_call_zXtBcMtvFe98YFAP8d6Vm3lL

def clean_id(s):
    if s is None:
        return s
    return s.strip().lstrip('#').strip()

target = '01tWt000006hVJdIAM'

# Build mapping from OrderItem Id -> Product2Id (cleaned)
oi_map = {}
for oi in orderitems:
    oid = clean_id(oi.get('Id'))
    pid = clean_id(oi.get('Product2Id'))
    if oid:
        oi_map[oid] = pid

# find orderitem ids that map to target product id (cleaned)
target_clean = clean_id(target)
matching_oi_ids = {oid for oid,pid in oi_map.items() if pid and pid == target_clean}

# filter cases whose orderitemid__c maps to target
from collections import Counter
counts = Counter()

for c in cases:
    oi = clean_id(c.get('orderitemid__c'))
    if oi in matching_oi_ids:
        cd = c.get('createddate')
        if not cd:
            continue
        # strip timezone part like +0000
        if '+' in cd:
            cd = cd.split('+')[0]
        if 'Z' in cd:
            cd = cd.replace('Z','')
        # Some timestamps may not have milliseconds
        fmt = None
        try:
            dt = datetime.strptime(cd, '%Y-%m-%dT%H:%M:%S.%f')
        except Exception:
            try:
                dt = datetime.strptime(cd, '%Y-%m-%dT%H:%M:%S')
            except Exception:
                # fallback: parse date part only
                try:
                    dt = datetime.strptime(cd.split('T')[0], '%Y-%m-%d')
                except Exception:
                    continue
        month_name = dt.strftime('%B')
        counts[month_name] += 1

# decide if a month significantly exceeds others
result = None
if counts:
    items = counts.most_common()
    max_month, max_count = items[0]
    next_count = items[1][1] if len(items) > 1 else 0
    vals = list(counts.values())
    mean = sum(vals)/len(vals)
    # population std
    var = sum((x-mean)**2 for x in vals)/len(vals)
    std = math.sqrt(var)
    # significance rule: max >= 1.5 * next_max AND max >= mean + std
    if (next_count == 0 and max_count > 0) or (max_count >= next_count * 1.5 and max_count >= mean + std):
        result = max_month
    else:
        result = None
else:
    result = None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_GluC9u81D8MrVWff2nLwS12h': [{'id': '500Wt00000DDDtTIAX', 'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDPM6IAP', 'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDRB2IAP', 'createddate': '2021-01-10T09:30:00.000+0000', 'orderitemid__c': '802Wt00000797axIAA'}, {'id': '500Wt00000DDRVzIAP', 'createddate': '2020-09-05T09:15:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDYpGIAX', 'createddate': '2021-03-31T11:41:00.000+0000', 'orderitemid__c': '802Wt00000798OvIAI'}, {'id': '#500Wt00000DDZmsIAH', 'createddate': '2020-07-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000795XwIAI'}, {'id': '500Wt00000DDeoCIAT', 'createddate': '2020-07-01T15:30:00.000+0000', 'orderitemid__c': '802Wt00000794bTIAQ'}, {'id': '#500Wt00000DDfvXIAT', 'createddate': '2021-03-24T18:04:00.000+0000', 'orderitemid__c': '802Wt00000796dGIAQ'}, {'id': '#500Wt00000DDg8QIAT', 'createddate': '2021-03-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDsG4IAL', 'createddate': '2020-11-05T11:00:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDt7HIAT', 'createddate': '2021-02-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}, {'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000', 'orderitemid__c': '802Wt00000799o1IAA'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DDymuIAD', 'createddate': '2020-10-01T14:30:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDz6GIAT', 'createddate': '2020-09-03T14:45:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '#500Wt00000DDzKjIAL', 'createddate': '2020-10-22T03:55:00.000+0000', 'orderitemid__c': '802Wt00000796JtIAI'}, {'id': '500Wt00000DDzmAIAT', 'createddate': '2021-02-20T14:30:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DE05VIAT', 'createddate': '2021-01-03T15:30:00.000+0000', 'orderitemid__c': '802Wt00000799b7IAA'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0DZIA1', 'createddate': '2020-11-10T22:14:00.000+0000', 'orderitemid__c': '802Wt00000799uTIAQ'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0WwIAL', 'createddate': '2021-03-10T15:45:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}], 'var_call_zXtBcMtvFe98YFAP8d6Vm3lL': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794bTIAQ', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '802Wt00000795XwIAI', 'Product2Id': '01tWt000006hVEnIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796JtIAI', 'Product2Id': '01tWt000006hTUkIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797r5IAA', 'Product2Id': '#01tWt000006hV58IAE'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798OvIAI', 'Product2Id': '01tWt000006hV9xIAE'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798aDIAQ', 'Product2Id': '01tWt000006hV58IAE'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000799uTIAQ', 'Product2Id': '01tWt000006hVEnIAM'}, {'Id': '802Wt0000079A2ZIAU', 'Product2Id': '01tWt000006hV57IAE'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}]}

exec(code, env_args)
