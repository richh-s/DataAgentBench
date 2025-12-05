code = """import json
from datetime import datetime

rows = var_call_24YCegF5vIdKCUncH11LcEsF

for r in rows:
    r['case_count'] = int(r['case_count'])

if not rows:
    result = None
else:
    max_count = max(r['case_count'] for r in rows)
    threshold = max_count * 0.5
    top_months = [r for r in rows if r['case_count'] == max_count]
    second_max = max((r['case_count'] for r in rows if r['case_count'] < max_count), default=None)
    if second_max is None or max_count >= second_max + 2:
        target = top_months[0]
    else:
        target = top_months[0]

    month_date = datetime.strptime(target['month'], '%Y-%m-%d')
    month_name = month_date.strftime('%B')
    result = month_name

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_WAILh39kQbSNzRuRy4CKSSbB': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_call_24YCegF5vIdKCUncH11LcEsF': [{'month': '2020-07-01', 'case_count': '2'}, {'month': '2020-09-01', 'case_count': '4'}, {'month': '2020-10-01', 'case_count': '2'}, {'month': '2020-11-01', 'case_count': '4'}, {'month': '2020-12-01', 'case_count': '1'}, {'month': '2021-01-01', 'case_count': '3'}, {'month': '2021-02-01', 'case_count': '2'}, {'month': '2021-03-01', 'case_count': '5'}]}

exec(code, env_args)
