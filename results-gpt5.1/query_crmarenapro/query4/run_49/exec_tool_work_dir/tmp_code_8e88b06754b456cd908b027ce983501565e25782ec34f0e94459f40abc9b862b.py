code = """import json
from datetime import datetime

rows = var_call_UYj2skW6Txcucq9NGr8WVeSa
# convert case_count to int
for r in rows:
    r['case_count'] = int(r['case_count'])

# find month with max cases
max_count = max(r['case_count'] for r in rows)
max_months = [r for r in rows if r['case_count'] == max_count]

# check if it significantly exceeds others: here require it to be strictly greater than every other month
if len(max_months) == 1 and all(max_count > r['case_count'] for r in rows if r is not max_months[0]):
    month_dt = datetime.strptime(max_months[0]['month_start'], '%Y-%m-%d')
    month_name = month_dt.strftime('%B')
else:
    month_name = None

result = json.dumps(month_name)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_nRvhDGf365HHL8DNxfj67hlX': [{'table_name': 'Case'}, {'table_name': 'knowledge__kav'}, {'table_name': 'issue__c'}, {'table_name': 'casehistory__c'}, {'table_name': 'emailmessage'}, {'table_name': 'livechattranscript'}], 'var_call_3iVGoiqOrW0HIQmmyETiR37x': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_call_UYj2skW6Txcucq9NGr8WVeSa': [{'month_start': '2020-09-01', 'case_count': '4'}, {'month_start': '2020-10-01', 'case_count': '2'}, {'month_start': '2020-11-01', 'case_count': '4'}, {'month_start': '2020-12-01', 'case_count': '1'}, {'month_start': '2021-01-01', 'case_count': '3'}, {'month_start': '2021-02-01', 'case_count': '2'}, {'month_start': '2021-03-01', 'case_count': '5'}]}

exec(code, env_args)
