code = """import json

# Get the order results
order_results = var_functions.query_db:7

# Filter for AI-related products
ai_products = []
if order_results:
    for item in order_results:
        product_name = item.get('ProductName', '').lower()
        description = item.get('Description', '').lower()
        # Check if it's AI-related
        if 'ai' in product_name or 'ai' in description or 'artificial' in product_name or 'artificial' in description:
            ai_products.append(item)

# Print the results
result_json = json.dumps(ai_products)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': [{'Id': '003Wt00000Jqy8SIAR', 'AccountId': '#001Wt00000PGXrNIAX'}], 'var_functions.query_db:2': [], 'var_functions.query_db:4': [], 'var_functions.query_db:7': [{'OrderId': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-06-15', 'OrderItemId': '802Wt0000079AU1IAM', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.'}]}

exec(code, env_args)
