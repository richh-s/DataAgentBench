code = """import json
from datetime import datetime

orders = var_call_HtVwRK07TlCUOdLCKv4H0Ulg

cutoff = datetime.fromisoformat('2021-07-15')

# Filter orders on or before cutoff (last month relative to 2021-07-15 means June 2021, but we only have 2021-06-15 and 2021-11-01)
valid_orders = []
for r in orders:
    d = datetime.fromisoformat(r['EffectiveDate'])
    if d <= cutoff:
        valid_orders.append(r)

# Pick the most recent valid order
if valid_orders:
    latest = max(valid_orders, key=lambda r: r['EffectiveDate'])
    product_id = latest['Product2Id']
else:
    product_id = None

result = json.dumps(product_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_nPWJAFUs4mf71sY6IhK9fci9': [], 'var_call_c9wJuMlPINJPXjzQnJcpHxIu': [{'Id': '003Wt00000Jqy8SIAR', 'AccountId': '#001Wt00000PGXrNIAX'}], 'var_call_HtVwRK07TlCUOdLCKv4H0Ulg': [{'OrderItemId': '#802Wt00000792tlIAA', 'Product2Id': '#01tWt000006hVmfIAE', 'EffectiveDate': '2021-11-01'}, {'OrderItemId': '#802Wt00000798qNIAQ', 'Product2Id': '01tWt000006hVY9IAM', 'EffectiveDate': '2021-11-01'}, {'OrderItemId': '#802Wt0000079AVbIAM', 'Product2Id': '01tWt000006hV57IAE', 'EffectiveDate': '2021-11-01'}, {'OrderItemId': '#802Wt0000079AsAIAU', 'Product2Id': '01tWt000006hV58IAE', 'EffectiveDate': '2021-11-01'}, {'OrderItemId': '802Wt000007959PIAQ', 'Product2Id': '#01tWt000006hV8LIAU', 'EffectiveDate': '2021-11-01'}, {'OrderItemId': '802Wt0000079986IAA', 'Product2Id': '01tWt000006hV6jIAE', 'EffectiveDate': '2021-11-01'}, {'OrderItemId': '802Wt0000079AU1IAM', 'Product2Id': '01tWt000006hV8LIAU', 'EffectiveDate': '2021-06-15'}], 'var_call_dNyE7QEO5lbZpp8ieyJxwxlK': []}

exec(code, env_args)
