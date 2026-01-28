code = """import json

# Consolidate all findings
contact_id = "003Wt00000Jqy8SIAR"
account_id_from_contact = "#001Wt00000PGXrNIAX"
account_id_clean = "001Wt00000PGXrNIAX"

order_id = "801Wt00000PHRYWIA5"
order_effective_date = "2021-06-15"
order_status = "Activated  "

order_item_id = "802Wt0000079AU1IAM"
product2_id = "01tWt000006hV8LIAU"
product_name = "AI Cirku-Tech"
product_description = "AI-driven circuit design platform offering rapid prototyping and innovation support."

# Verify the product is indeed an AI processing unit based on name and description
is_ai_product = "AI" in product_name and ("circuit" in product_description or "tech" in product_description)

result = {
    "contact_id": contact_id,
    "account_id": account_id_clean,
    "order_id": order_id,
    "order_date": order_effective_date,
    "product_id": product2_id,
    "product_name": product_name,
    "is_ai_processing_unit": is_ai_product
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '003Wt00000Jqy8SIAR', 'AccountId': '#001Wt00000PGXrNIAX'}], 'var_functions.query_db:2': [{'Id': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'Status': 'Activated  ', 'EffectiveDate': '2021-06-15'}], 'var_functions.query_db:5': [{'Id': '802Wt0000079AU1IAM', 'OrderId': '801Wt00000PHRYWIA5', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '10.0', 'UnitPrice': '476.991'}], 'var_functions.query_db:6': [{'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.'}], 'var_functions.query_db:8': [{'Id': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'Status': 'Activated  ', 'EffectiveDate': '2021-06-15'}], 'var_functions.query_db:10': [{'Id': '003Wt00000Jqy8SIAR', 'AccountId': '#001Wt00000PGXrNIAX'}], 'var_functions.query_db:12': [{'Id': '003Wt00000Jqy8SIAR', 'AccountId': '#001Wt00000PGXrNIAX'}]}

exec(code, env_args)
