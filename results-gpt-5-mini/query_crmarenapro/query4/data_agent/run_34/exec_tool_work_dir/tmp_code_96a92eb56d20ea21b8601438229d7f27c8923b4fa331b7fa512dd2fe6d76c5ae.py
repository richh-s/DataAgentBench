code = """import json
from datetime import datetime

# Load data from previous tool calls
cases = var_call_ydVPzDpP7fyIxy538cleplCW
order_items = var_call_qJeN4nxzway9AOg2KTO16bK1

# Normalize order item ids (strip leading '#' and whitespace)
def norm_id(s):
    if s is None:
        return s
    return s.strip().lstrip('#')

order_ids = set([norm_id(r.get('Id') or r.get('id') or '') for r in order_items])

# Filter cases where orderitemid__c matches one of the product's order items
filtered = []
for c in cases:
    oid = norm_id(c.get('orderitemid__c') or c.get('orderitemid__C') or '')
    if oid in order_ids:
        # parse date
        cd = c.get('createddate')
        try:
            dt = datetime.fromisoformat(cd.replace('Z', '+00:00'))
        except Exception:
            # fallback parse
            try:
                dt = datetime.strptime(cd, '%Y-%m-%dT%H:%M:%S.%f%z')
            except Exception:
                continue
        filtered.append({'id': c.get('id'), 'orderitemid__c': oid, 'createddate': dt})

# Define the 10-month window: from 2020-07 to 2021-04 inclusive (based on the initial query range)
months = []
start_year = 2020
start_month = 7
for i in range(10):
    y = start_year + (start_month - 1 + i) // 12
    m = (start_month - 1 + i) % 12 + 1
    months.append((y, m))

# Initialize counts with zeros
from collections import OrderedDict, Counter
month_names = OrderedDict()
for y,m in months:
    name = datetime(y, m, 1).strftime('%B')
    month_names[(y,m)] = name

counts = {name: 0 for name in month_names.values()}
for f in filtered:
    dt = f['createddate']
    key = (dt.year, dt.month)
    if key in month_names:
        counts[month_names[key]] += 1

# Determine if any month significantly exceeds others
vals = list(counts.values())
import math
n = len(vals)
mean = sum(vals)/n
var = sum((v-mean)**2 for v in vals)/n
std = math.sqrt(var)

# Find top and second top
sorted_months = sorted(counts.items(), key=lambda x: x[1], reverse=True)
if sorted_months:
    top_month, top_count = sorted_months[0]
    second_count = sorted_months[1][1] if len(sorted_months) > 1 else 0
else:
    top_month, top_count, second_count = None, 0, 0

significant_month = None
# Criterion 1: greater than mean + 2*std
if top_count > mean + 2*std and top_count > 0:
    significant_month = top_month
# Criterion 2: at least 1.5x the second highest and at least 2 cases
elif second_count == 0 and top_count >= 2:
    significant_month = top_month
elif second_count > 0 and top_count >= 1.5 * second_count and top_count >= 2:
    significant_month = top_month

result = significant_month if significant_month is not None else "None"

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ydVPzDpP7fyIxy538cleplCW': [{'id': '500Wt00000DDDtTIAX', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2020-12-29T08:36:00.000+0000'}, {'id': '500Wt00000DDPM6IAP', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-01T10:30:00.000+0000'}, {'id': '500Wt00000DDRB2IAP', 'orderitemid__c': '802Wt00000797axIAA', 'createddate': '2021-01-10T09:30:00.000+0000'}, {'id': '500Wt00000DDRVzIAP', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-05T09:15:00.000+0000'}, {'id': '500Wt00000DDYpGIAX', 'orderitemid__c': '802Wt00000798OvIAI', 'createddate': '2021-03-31T11:41:00.000+0000'}, {'id': '#500Wt00000DDZmsIAH', 'orderitemid__c': '802Wt00000795XwIAI', 'createddate': '2020-07-05T09:45:00.000+0000'}, {'id': '500Wt00000DDeoCIAT', 'orderitemid__c': '802Wt00000794bTIAQ', 'createddate': '2020-07-01T15:30:00.000+0000'}, {'id': '#500Wt00000DDfvXIAT', 'orderitemid__c': '802Wt00000796dGIAQ', 'createddate': '2021-03-24T18:04:00.000+0000'}, {'id': '#500Wt00000DDg8QIAT', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2021-03-05T09:45:00.000+0000'}, {'id': '500Wt00000DDsG4IAL', 'orderitemid__c': '802Wt0000079A2ZIAU', 'createddate': '2020-11-05T11:00:00.000+0000'}, {'id': '500Wt00000DDt7HIAT', 'orderitemid__c': '802Wt00000797foIAA', 'createddate': '2021-02-01T10:30:00.000+0000'}, {'id': '#500Wt00000DDxnbIAD', 'orderitemid__c': '802Wt00000799o1IAA', 'createddate': '2021-01-25T09:30:00.000+0000'}, {'id': '500Wt00000DDy8bIAD', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2020-11-05T08:19:00.000+0000'}, {'id': '500Wt00000DDymuIAD', 'orderitemid__c': '802Wt0000079A2ZIAU', 'createddate': '2020-10-01T14:30:00.000+0000'}, {'id': '500Wt00000DDz6GIAT', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-03T14:45:00.000+0000'}, {'id': '#500Wt00000DDzKjIAL', 'orderitemid__c': '802Wt00000796JtIAI', 'createddate': '2020-10-22T03:55:00.000+0000'}, {'id': '500Wt00000DDzmAIAT', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2021-02-20T14:30:00.000+0000'}, {'id': '500Wt00000DE00gIAD', 'orderitemid__c': '802Wt00000796bfIAA', 'createddate': '2020-09-29T01:59:00.000+0000'}, {'id': '500Wt00000DE05VIAT', 'orderitemid__c': '802Wt00000799b7IAA', 'createddate': '2021-01-03T15:30:00.000+0000'}, {'id': '500Wt00000DE0AMIA1', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2021-03-07T11:25:00.000+0000'}, {'id': '500Wt00000DE0DZIA1', 'orderitemid__c': '802Wt00000799uTIAQ', 'createddate': '2020-11-10T22:14:00.000+0000'}, {'id': '500Wt00000DE0NFIA1', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2020-11-09T19:02:00.000+0000'}, {'id': '500Wt00000DE0WwIAL', 'orderitemid__c': '802Wt00000797foIAA', 'createddate': '2021-03-10T15:45:00.000+0000'}], 'var_call_qJeN4nxzway9AOg2KTO16bK1': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}]}

exec(code, env_args)
