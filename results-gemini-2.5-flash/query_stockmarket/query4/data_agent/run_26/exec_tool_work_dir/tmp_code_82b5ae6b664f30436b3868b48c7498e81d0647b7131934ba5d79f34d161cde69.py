code = """import json
import pandas as pd

with open(locals()['var_function-call-10858864484969439476'], 'r') as f:
    stockinfo_data = json.load(f)

df_stockinfo = pd.DataFrame(stockinfo_data)

symbols_to_query = df_stockinfo['Symbol'].tolist()
company_descriptions = df_stockinfo.set_index('Symbol')['Company Description'].to_dict()

print('__RESULT__:')
print(json.dumps({'symbols': symbols_to_query, 'descriptions': company_descriptions}))"""

env_args = {'var_function-call-10858864484969439476': 'file_storage/function-call-10858864484969439476.json'}

exec(code, env_args)
