code = """import json
import pandas as pd
opportunities_data = locals()['var_function-call-13876130167442136310']

df = pd.DataFrame(opportunities_data)
df['CloseDate'] = pd.to_datetime(df['CloseDate'])
filtered_opportunities = df[(df['CloseDate'].dt.month == 6) & (df['CloseDate'].dt.year == 2021)]
opportunity_ids_last_month = filtered_opportunities['Id'].tolist()

print('__RESULT__:')
print(json.dumps(opportunity_ids_last_month))"""

env_args = {'var_function-call-13894408723187244389': [{'AccountId': '#001Wt00000PGXrNIAX'}], 'var_function-call-15319840143889871148': [], 'var_function-call-16179312338050489977': [{'Id': '006Wt000007B0g2IAC'}, {'Id': '006Wt000007B7TcIAK'}, {'Id': '006Wt000007BBx1IAG'}, {'Id': '006Wt000007BInBIAW'}], 'var_function-call-8166341117310542865': ['006Wt000007B0g2IAC', '006Wt000007B7TcIAK', '006Wt000007BBx1IAG', '006Wt000007BInBIAW'], 'var_function-call-13876130167442136310': [{'Id': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15'}, {'Id': '006Wt000007B7TcIAK', 'CloseDate': '2021-06-15'}, {'Id': '006Wt000007BBx1IAG', 'CloseDate': '2021-11-01'}, {'Id': '006Wt000007BInBIAW', 'CloseDate': '2022-06-20'}]}

exec(code, env_args)
