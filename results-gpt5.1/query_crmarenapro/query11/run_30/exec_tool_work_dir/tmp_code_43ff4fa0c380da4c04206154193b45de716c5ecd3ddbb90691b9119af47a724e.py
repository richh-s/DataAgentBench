code = """import json
opps = var_call_W6dOHkZTdc5ABX56cWcfTwwo
# assume "AI processing unit" is the product with Id containing 'V8L' based on domain pattern, else fall back to first product
ai_products = [r['Product2Id'] for r in opps if 'V8L' in r['Product2Id']]
product_id = ai_products[0] if ai_products else opps[0]['Product2Id'] if opps else None
result = json.dumps(product_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_W6dOHkZTdc5ABX56cWcfTwwo': [{'OpportunityId': '006Wt000007B0g2IAC', 'ContactId': '003Wt00000Jqy8SIAR', 'Product2Id': '#01tWt000006hV8LIAU', 'CloseDate': '2021-06-15'}, {'OpportunityId': '006Wt000007B7TcIAK', 'ContactId': '003Wt00000Jqy8SIAR', 'Product2Id': '01tWt000006hTUkIAM', 'CloseDate': '2021-06-15'}, {'OpportunityId': '006Wt000007B7TcIAK', 'ContactId': '003Wt00000Jqy8SIAR', 'Product2Id': '01tWt000006hV8LIAU', 'CloseDate': '2021-06-15'}, {'OpportunityId': '006Wt000007B0g2IAC', 'ContactId': '003Wt00000Jqy8SIAR', 'Product2Id': '01tWt000006hV9xIAE', 'CloseDate': '2021-06-15'}], 'var_call_BpfNhGvs8qneCxh96UQM6dyu': [], 'var_call_bpfFyQUI9ZarVxtsTlNVs0w6': []}

exec(code, env_args)
