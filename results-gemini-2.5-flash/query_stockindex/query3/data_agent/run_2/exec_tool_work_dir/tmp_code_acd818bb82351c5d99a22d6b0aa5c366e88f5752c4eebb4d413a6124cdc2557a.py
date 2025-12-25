code = """import pandas as pd
df = pd.DataFrame(locals()['var_function-call-15017430552549906343'])
df['first_adj_close'] = pd.to_numeric(df['first_adj_close'])
df['last_adj_close'] = pd.to_numeric(df['last_adj_close'])
df['return'] = (df['last_adj_close'] - df['first_adj_close']) / df['first_adj_close']
top_5_indices = df.sort_values(by='return', ascending=False).head(5)
print("__RESULT__:")
print(top_5_indices.to_json(orient='records'))"""

env_args = {'var_function-call-13143669812427612350': ['index_info'], 'var_function-call-13143669812427613783': ['index_trade'], 'var_function-call-15017430552549906343': [{'Index': 'HSI', 'first_adj_close': '15542.23047', 'last_adj_close': '26092.26953'}, {'Index': 'NYA', 'first_adj_close': '6762.109863', 'last_adj_close': '12701.88965'}, {'Index': 'IXIC', 'first_adj_close': '3727.129883', 'last_adj_close': '4620.160156'}, {'Index': '000001.SS', 'first_adj_close': '1406.370972', 'last_adj_close': '3052.781006'}, {'Index': 'N225', 'first_adj_close': '19002.85938', 'last_adj_close': '23185.11914'}, {'Index': 'N100', 'first_adj_close': '960.219971', 'last_adj_close': '1099.170044'}, {'Index': '399001.SZ', 'first_adj_close': '3486.250977', 'last_adj_close': '9988.138672'}, {'Index': 'GSPTSE', 'first_adj_close': '8119.399902', 'last_adj_close': '14725.90039'}, {'Index': 'NSEI', 'first_adj_close': '4938.850098', 'last_adj_close': '7964.799805'}, {'Index': 'GDAXI', 'first_adj_close': '6502.069824', 'last_adj_close': '10511.01953'}, {'Index': 'SSMI', 'first_adj_close': '7181.299805', 'last_adj_close': '10187.0'}, {'Index': 'TWII', 'first_adj_close': '9315.395508', 'last_adj_close': '12515.61035'}, {'Index': 'J203.JO', 'first_adj_close': '34226.73047', 'last_adj_close': '54824.96875'}]}

exec(code, env_args)
