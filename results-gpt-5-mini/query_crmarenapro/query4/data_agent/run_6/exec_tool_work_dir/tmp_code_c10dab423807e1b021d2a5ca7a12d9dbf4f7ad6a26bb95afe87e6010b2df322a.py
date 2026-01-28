code = """import json
from datetime import datetime

# Load data from previous tool calls
order_items = var_call_HVKXHgc8YHtxtMpBaGyYIqTZ
cases = var_call_TTZmBWCXZqo2RFqzxTU1YguC

# Normalize function
def norm_id(s):
    if s is None:
        return None
    return s.strip().lstrip('#').strip()

order_item_ids = set(norm_id(r.get('Id')) for r in order_items)

# Filter cases linked to these order items
linked_cases = []
for c in cases:
    oid = norm_id(c.get('orderitemid__c'))
    if oid in order_item_ids:
        cd = c.get('createddate')
        if cd:
            try:
                dt = datetime.strptime(cd, "%Y-%m-%dT%H:%M:%S.%f%z")
            except Exception:
                # try without milliseconds
                try:
                    dt = datetime.strptime(cd, "%Y-%m-%dT%H:%M:%S%z")
                except Exception:
                    continue
            linked_cases.append({'id': c.get('id'), 'created': dt})

# Count per month name
from collections import Counter
counts = Counter()
for c in linked_cases:
    counts[c['created'].strftime('%B')] += 1

# Prepare statistics
months = list(counts.keys())
values = [counts[m] for m in months]

import math

def significant_month(counter):
    if not counter:
        return None
    # find max
    items = list(counter.items())
    # compute mean and std
    vals = [v for _, v in items]
    mean = sum(vals)/len(vals)
    var = sum((v-mean)**2 for v in vals)/len(vals)
    std = math.sqrt(var)
    # pick month with highest count
    items.sort(key=lambda x: x[1], reverse=True)
    top_month, top_count = items[0]
    # define significant as top_count > mean + 2*std
    if top_count > mean + 2*std:
        return top_month
    else:
        return None

sig_month = significant_month(counts)

# print result as JSON-serializable string
print("__RESULT__:")
print(json.dumps(sig_month))"""

env_args = {'var_call_4NcZd4IxPZ2WmdtQgaqCONTV': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_call_VfPWqCey3OPmxKbuzlgMG1HQ': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_call_HVKXHgc8YHtxtMpBaGyYIqTZ': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_call_TTZmBWCXZqo2RFqzxTU1YguC': [{'id': '500Wt00000DDDtTIAX', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2020-12-29T08:36:00.000+0000'}, {'id': '500Wt00000DDPM6IAP', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-01T10:30:00.000+0000'}, {'id': '500Wt00000DDRB2IAP', 'orderitemid__c': '802Wt00000797axIAA', 'createddate': '2021-01-10T09:30:00.000+0000'}, {'id': '500Wt00000DDRVzIAP', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-05T09:15:00.000+0000'}, {'id': '500Wt00000DDYpGIAX', 'orderitemid__c': '802Wt00000798OvIAI', 'createddate': '2021-03-31T11:41:00.000+0000'}, {'id': '#500Wt00000DDZmsIAH', 'orderitemid__c': '802Wt00000795XwIAI', 'createddate': '2020-07-05T09:45:00.000+0000'}, {'id': '500Wt00000DDeoCIAT', 'orderitemid__c': '802Wt00000794bTIAQ', 'createddate': '2020-07-01T15:30:00.000+0000'}, {'id': '#500Wt00000DDfvXIAT', 'orderitemid__c': '802Wt00000796dGIAQ', 'createddate': '2021-03-24T18:04:00.000+0000'}, {'id': '#500Wt00000DDg8QIAT', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2021-03-05T09:45:00.000+0000'}, {'id': '500Wt00000DDsG4IAL', 'orderitemid__c': '802Wt0000079A2ZIAU', 'createddate': '2020-11-05T11:00:00.000+0000'}, {'id': '500Wt00000DDt7HIAT', 'orderitemid__c': '802Wt00000797foIAA', 'createddate': '2021-02-01T10:30:00.000+0000'}, {'id': '#500Wt00000DDxnbIAD', 'orderitemid__c': '802Wt00000799o1IAA', 'createddate': '2021-01-25T09:30:00.000+0000'}, {'id': '500Wt00000DDy8bIAD', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2020-11-05T08:19:00.000+0000'}, {'id': '500Wt00000DDymuIAD', 'orderitemid__c': '802Wt0000079A2ZIAU', 'createddate': '2020-10-01T14:30:00.000+0000'}, {'id': '500Wt00000DDz6GIAT', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-03T14:45:00.000+0000'}, {'id': '#500Wt00000DDzKjIAL', 'orderitemid__c': '802Wt00000796JtIAI', 'createddate': '2020-10-22T03:55:00.000+0000'}, {'id': '500Wt00000DDzmAIAT', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2021-02-20T14:30:00.000+0000'}, {'id': '500Wt00000DE00gIAD', 'orderitemid__c': '802Wt00000796bfIAA', 'createddate': '2020-09-29T01:59:00.000+0000'}, {'id': '500Wt00000DE05VIAT', 'orderitemid__c': '802Wt00000799b7IAA', 'createddate': '2021-01-03T15:30:00.000+0000'}, {'id': '500Wt00000DE0AMIA1', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2021-03-07T11:25:00.000+0000'}, {'id': '500Wt00000DE0DZIA1', 'orderitemid__c': '802Wt00000799uTIAQ', 'createddate': '2020-11-10T22:14:00.000+0000'}, {'id': '500Wt00000DE0NFIA1', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2020-11-09T19:02:00.000+0000'}, {'id': '500Wt00000DE0WwIAL', 'orderitemid__c': '802Wt00000797foIAA', 'createddate': '2021-03-10T15:45:00.000+0000'}]}

exec(code, env_args)
