code = """import json

product_details = locals()['var_function-call-3532736014176179921']

ai_product_id = None
for product in product_details:
    if 'AI processing unit' in product['Name'] or 'AI processing unit' in product['Description'] or 'AI' in product['Name'] or 'AI' in product['Description']:
        ai_product_id = product['Id']
        break

print('__RESULT__:')
print(json.dumps(ai_product_id))"""

env_args = {'var_function-call-7075657702392961048': [{'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '#01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hTUkIAM'}, {'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '01tWt000006hV9xIAE'}], 'var_function-call-10356182795575815338': [], 'var_function-call-15493726896386879118': [], 'var_function-call-4145107439049167997': ['01tWt000006hV8LIAU', '01tWt000006hTUkIAM', '01tWt000006hV9xIAE'], 'var_function-call-3532736014176179921': [{'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer', 'Description': 'Cloud-based design collaboration tool enhancing team productivity across global projects.'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.'}]}

exec(code, env_args)
