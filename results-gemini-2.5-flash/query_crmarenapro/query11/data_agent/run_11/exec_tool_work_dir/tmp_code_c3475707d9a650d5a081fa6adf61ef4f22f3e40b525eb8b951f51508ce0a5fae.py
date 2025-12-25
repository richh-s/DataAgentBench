code = """import json
opportunity_ids = [opp['Id'] for opp in locals()['var_function-call-16179312338050489977'] if 'Id' in opp]
print('__RESULT__:')
print(json.dumps(opportunity_ids))"""

env_args = {'var_function-call-13894408723187244389': [{'AccountId': '#001Wt00000PGXrNIAX'}], 'var_function-call-15319840143889871148': [], 'var_function-call-16179312338050489977': [{'Id': '006Wt000007B0g2IAC'}, {'Id': '006Wt000007B7TcIAK'}, {'Id': '006Wt000007BBx1IAG'}, {'Id': '006Wt000007BInBIAW'}]}

exec(code, env_args)
