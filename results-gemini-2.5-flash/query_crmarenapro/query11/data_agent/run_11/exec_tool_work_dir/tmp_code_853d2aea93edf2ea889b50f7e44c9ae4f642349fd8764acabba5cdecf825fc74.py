code = """import json
product_ids = [product['Product2Id'] for product in locals()['var_function-call-12072386742813464785'] if 'Product2Id' in product]
print('__RESULT__:')
print(json.dumps(product_ids))"""

env_args = {'var_function-call-13894408723187244389': [{'AccountId': '#001Wt00000PGXrNIAX'}], 'var_function-call-15319840143889871148': [], 'var_function-call-16179312338050489977': [{'Id': '006Wt000007B0g2IAC'}, {'Id': '006Wt000007B7TcIAK'}, {'Id': '006Wt000007BBx1IAG'}, {'Id': '006Wt000007BInBIAW'}], 'var_function-call-8166341117310542865': ['006Wt000007B0g2IAC', '006Wt000007B7TcIAK', '006Wt000007BBx1IAG', '006Wt000007BInBIAW'], 'var_function-call-13876130167442136310': [{'Id': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15'}, {'Id': '006Wt000007B7TcIAK', 'CloseDate': '2021-06-15'}, {'Id': '006Wt000007BBx1IAG', 'CloseDate': '2021-11-01'}, {'Id': '006Wt000007BInBIAW', 'CloseDate': '2022-06-20'}], 'var_function-call-12752375921248626090': ['006Wt000007B0g2IAC', '006Wt000007B7TcIAK'], 'var_function-call-12072386742813464785': [{'Product2Id': '#01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hTUkIAM'}, {'Product2Id': '01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hV9xIAE'}]}

exec(code, env_args)
