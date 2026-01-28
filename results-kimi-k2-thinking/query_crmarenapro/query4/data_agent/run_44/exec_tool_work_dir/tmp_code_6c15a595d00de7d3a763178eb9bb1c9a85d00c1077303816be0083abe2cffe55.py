code = """import json
from datetime import datetime, timezone

# Load data from previous queries
cases = locals()['var_functions.query_db:2']
orderitems = locals()['var_functions.query_db:9']

# Normalize IDs: remove leading '#' and trailing whitespace
def normalize_id(id_str):
    if id_str is None:
        return None
    # Ensure it's string
    s = str(id_str)
    # Remove leading '#'
    if s.startswith('#'):
        s = s[1:]
    # Remove trailing whitespace
    s = s.rstrip()
    return s

# Build set of normalized orderitem IDs for the product
product_orderitem_ids = set()
for oi in orderitems:
    oid = oi.get('Id')
    norm_oid = normalize_id(oid)
    if norm_oid:
        product_orderitem_ids.add(norm_oid)

# Define date range: from 2020-06-10 to 2021-04-10 inclusive (past 10 months from today 2021-04-10)
# Use timezone-aware datetimes in UTC
start_date = datetime(2020, 6, 10, 0, 0, 0, tzinfo=timezone.utc)
end_date = datetime(2021, 4, 10, 23, 59, 59, tzinfo=timezone.utc)

case_month_counts = {}

for case in cases:
    # Parse createddate (iso format with timezone)
    created_str = case.get('createddate')
    if not created_str:
        continue
    # Replace 'Z' with '+00:00' for fromisoformat compatibility
    created_str_clean = created_str.replace('Z', '+00:00')
    try:
        created_dt = datetime.fromisoformat(created_str_clean)
    except Exception:
        continue
    # Check date range
    if not (start_date <= created_dt <= end_date):
        continue
    # Normalize case orderitemid
    case_oi = case.get('orderitemid__c')
    norm_case_oi = normalize_id(case_oi)
    # Check if matches any product orderitem id
    if norm_case_oi in product_orderitem_ids:
        # Count by month key: YYYY-MM
        month_key = created_dt.strftime('%Y-%m')
        case_month_counts[month_key] = case_month_counts.get(month_key, 0) + 1

# Determine month with max counts
if not case_month_counts:
    result = 'No significant month found'
else:
    # Find month with highest count
    max_month_key = max(case_month_counts, key=case_month_counts.get)
    max_count = case_month_counts[max_month_key]
    # Compute average of other months
    if len(case_month_counts) > 1:
        total_other = sum(v for k, v in case_month_counts.items() if k != max_month_key)
        avg_other = total_other / (len(case_month_counts) - 1)
    else:
        avg_other = 0
    # Check significance: max count > 1.5 * avg of others
    significant = False
    if avg_other > 0:
        if max_count > 1.5 * avg_other:
            significant = True
    else:
        # Only one month with cases
        significant = True
    if significant:
        # Convert month key to month name
        month_name = datetime.strptime(max_month_key, '%Y-%m').strftime('%B')
        result = month_name
    else:
        result = 'No significant month found'

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:2': [{'id': '500Wt00000DDDtTIAX', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2020-12-29T08:36:00.000+0000'}, {'id': '500Wt00000DDPM6IAP', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-01T10:30:00.000+0000'}, {'id': '500Wt00000DDRB2IAP', 'orderitemid__c': '802Wt00000797axIAA', 'createddate': '2021-01-10T09:30:00.000+0000'}, {'id': '500Wt00000DDRVzIAP', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-05T09:15:00.000+0000'}, {'id': '500Wt00000DDYpGIAX', 'orderitemid__c': '802Wt00000798OvIAI', 'createddate': '2021-03-31T11:41:00.000+0000'}, {'id': '#500Wt00000DDZmsIAH', 'orderitemid__c': '802Wt00000795XwIAI', 'createddate': '2020-07-05T09:45:00.000+0000'}, {'id': '500Wt00000DDeoCIAT', 'orderitemid__c': '802Wt00000794bTIAQ', 'createddate': '2020-07-01T15:30:00.000+0000'}, {'id': '#500Wt00000DDfvXIAT', 'orderitemid__c': '802Wt00000796dGIAQ', 'createddate': '2021-03-24T18:04:00.000+0000'}, {'id': '#500Wt00000DDg8QIAT', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2021-03-05T09:45:00.000+0000'}, {'id': '500Wt00000DDsG4IAL', 'orderitemid__c': '802Wt0000079A2ZIAU', 'createddate': '2020-11-05T11:00:00.000+0000'}, {'id': '500Wt00000DDt7HIAT', 'orderitemid__c': '802Wt00000797foIAA', 'createddate': '2021-02-01T10:30:00.000+0000'}, {'id': '#500Wt00000DDxnbIAD', 'orderitemid__c': '802Wt00000799o1IAA', 'createddate': '2021-01-25T09:30:00.000+0000'}, {'id': '500Wt00000DDy8bIAD', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2020-11-05T08:19:00.000+0000'}, {'id': '500Wt00000DDymuIAD', 'orderitemid__c': '802Wt0000079A2ZIAU', 'createddate': '2020-10-01T14:30:00.000+0000'}, {'id': '500Wt00000DDz6GIAT', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-03T14:45:00.000+0000'}, {'id': '#500Wt00000DDzKjIAL', 'orderitemid__c': '802Wt00000796JtIAI', 'createddate': '2020-10-22T03:55:00.000+0000'}, {'id': '500Wt00000DDzmAIAT', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2021-02-20T14:30:00.000+0000'}, {'id': '500Wt00000DE00gIAD', 'orderitemid__c': '802Wt00000796bfIAA', 'createddate': '2020-09-29T01:59:00.000+0000'}, {'id': '500Wt00000DE05VIAT', 'orderitemid__c': '802Wt00000799b7IAA', 'createddate': '2021-01-03T15:30:00.000+0000'}, {'id': '500Wt00000DE0AMIA1', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2021-03-07T11:25:00.000+0000'}, {'id': '500Wt00000DE0DZIA1', 'orderitemid__c': '802Wt00000799uTIAQ', 'createddate': '2020-11-10T22:14:00.000+0000'}, {'id': '500Wt00000DE0NFIA1', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2020-11-09T19:02:00.000+0000'}, {'id': '500Wt00000DE0WwIAL', 'orderitemid__c': '802Wt00000797foIAA', 'createddate': '2021-03-10T15:45:00.000+0000'}], 'var_functions.list_db:5': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_functions.query_db:9': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}]}

exec(code, env_args)
