code = """import json
products_info = locals()['var_function-call-3444993487923791947']
ai_product_id = None
for product in products_info:
    if 'AI' in product['Name'] or 'AI' in product['Description']:
        ai_product_id = product['Id']
        break
print("__RESULT__:")
print(json.dumps(ai_product_id))"""

env_args = {'var_function-call-2738486724164434386': [{'Id': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX', 'ContractID__c': 'None'}, {'Id': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX', 'ContractID__c': '800Wt00000DDsO9IAL'}], 'var_function-call-436058163650440965': [{'Product2Id': '#01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hTUkIAM'}, {'Product2Id': '01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hV9xIAE'}], 'var_function-call-15193278915218809025': [{'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer'}], 'var_function-call-6988751579978859680': ['01tWt000006hV8LIAU', '01tWt000006hTUkIAM', '01tWt000006hV9xIAE'], 'var_function-call-3444993487923791947': [{'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer', 'Description': 'Cloud-based design collaboration tool enhancing team productivity across global projects.'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.'}]}

exec(code, env_args)
