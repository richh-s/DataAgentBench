code = """import pandas as pd
import json

product_ids = locals()['var_function-call-5531313012697286268']
df_product_ids = pd.DataFrame(product_ids)

df_product_ids['Product2Id'] = df_product_ids['Product2Id'].str.replace('#', '')

cleaned_product_ids = df_product_ids['Product2Id'].tolist()

print('__RESULT__:')
print(json.dumps(cleaned_product_ids))"""

env_args = {'var_function-call-1041141412135150793': [{'Id': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15'}, {'Id': '006Wt000007B7TcIAK', 'CloseDate': '2021-06-15'}], 'var_function-call-5531313012697286268': [{'Product2Id': '#01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hTUkIAM'}, {'Product2Id': '01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hV9xIAE'}]}

exec(code, env_args)
