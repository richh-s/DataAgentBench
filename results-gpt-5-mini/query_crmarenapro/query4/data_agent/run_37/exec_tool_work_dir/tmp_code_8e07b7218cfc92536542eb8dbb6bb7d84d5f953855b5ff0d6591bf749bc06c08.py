code = """import json
import pandas as pd

# Load variables from previous tool calls
cases = var_call_9Xu1Cva1Sn8sW41edv8QQZ7o
orderitem_file = var_call_HvTv1L5Vup8BGIK9i9KVkbh9

# Read the large OrderItem result from the JSON file
with open(orderitem_file, 'r') as f:
    orderitems = json.load(f)

# Normalization function for IDs (strip whitespace and leading #)
def norm_id(x):
    if x is None:
        return None
    s = str(x).strip()
    if s.startswith('#'):
        s = s[1:]
    return s

# Target product id normalized
target = norm_id('01tWt000006hVJdIAM')

# Build set of OrderItem Ids whose Product2Id matches target
matching_order_ids = set()
for oi in orderitems:
    pid = norm_id(oi.get('Product2Id'))
    oid = norm_id(oi.get('Id'))
    if pid == target:
        matching_order_ids.add(oid)

# Filter cases by those that reference matching order items
matched_cases = []
for c in cases:
    oid = norm_id(c.get('orderitemid__c'))
    if oid in matching_order_ids:
        # parse createddate
        cd = c.get('createddate')
        try:
            dt = pd.to_datetime(cd)
            month_name = dt.strftime('%B')
        except Exception:
            month_name = None
        matched_cases.append({'id': c.get('id'), 'createddate': c.get('createddate'), 'month': month_name})

# Count by month
counts = {}
for c in matched_cases:
    m = c['month']
    if m:
        counts[m] = counts.get(m, 0) + 1

# Determine if any month significantly exceeds others (threshold: > mean + 2*std)
result_month = None
if counts:
    import math
    vals = list(counts.values())
    mean = sum(vals)/len(vals)
    # population std
    var = sum((v-mean)**2 for v in vals)/len(vals)
    std = math.sqrt(var)
    # find month with max count
    max_month = max(counts, key=lambda k: counts[k])
    max_count = counts[max_month]
    if max_count > mean + 2*std:
        result_month = max_month
    else:
        result_month = None
else:
    result_month = None

# Prepare final output: month name or null
out = result_month if result_month is not None else None

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_pbccw64g6sRYg2fEFXhy9qBQ': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_9Xu1Cva1Sn8sW41edv8QQZ7o': [{'id': '500Wt00000DDDtTIAX', 'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDPM6IAP', 'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDRB2IAP', 'createddate': '2021-01-10T09:30:00.000+0000', 'orderitemid__c': '802Wt00000797axIAA'}, {'id': '500Wt00000DDRVzIAP', 'createddate': '2020-09-05T09:15:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDYpGIAX', 'createddate': '2021-03-31T11:41:00.000+0000', 'orderitemid__c': '802Wt00000798OvIAI'}, {'id': '#500Wt00000DDZmsIAH', 'createddate': '2020-07-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000795XwIAI'}, {'id': '500Wt00000DDeoCIAT', 'createddate': '2020-07-01T15:30:00.000+0000', 'orderitemid__c': '802Wt00000794bTIAQ'}, {'id': '#500Wt00000DDfvXIAT', 'createddate': '2021-03-24T18:04:00.000+0000', 'orderitemid__c': '802Wt00000796dGIAQ'}, {'id': '#500Wt00000DDg8QIAT', 'createddate': '2021-03-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDsG4IAL', 'createddate': '2020-11-05T11:00:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDt7HIAT', 'createddate': '2021-02-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}, {'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000', 'orderitemid__c': '802Wt00000799o1IAA'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DDymuIAD', 'createddate': '2020-10-01T14:30:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDz6GIAT', 'createddate': '2020-09-03T14:45:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '#500Wt00000DDzKjIAL', 'createddate': '2020-10-22T03:55:00.000+0000', 'orderitemid__c': '802Wt00000796JtIAI'}, {'id': '500Wt00000DDzmAIAT', 'createddate': '2021-02-20T14:30:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DE05VIAT', 'createddate': '2021-01-03T15:30:00.000+0000', 'orderitemid__c': '802Wt00000799b7IAA'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0DZIA1', 'createddate': '2020-11-10T22:14:00.000+0000', 'orderitemid__c': '802Wt00000799uTIAQ'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0WwIAL', 'createddate': '2021-03-10T15:45:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}], 'var_call_HOwWLFkhZOuTEI1DAs7Nug5I': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_call_HvTv1L5Vup8BGIK9i9KVkbh9': 'file_storage/call_HvTv1L5Vup8BGIK9i9KVkbh9.json'}

exec(code, env_args)
