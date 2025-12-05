code = """import json, pandas as pd
rows = json.load(open(var_call_ZURJ4OsYTAytXSbjUZRtoOnk))
df = pd.DataFrame(rows)
df['Open'] = df['Open'].astype(float)
df['Close'] = df['Close'].astype(float)
up = df['Close'] > df['Open']
down = df['Close'] < df['Open']
summary = df.groupby('Symbol').agg(up_days=('Close', lambda x: int((x>df.loc[x.index,'Open']).sum())), down_days=('Close', lambda x: int((x<df.loc[x.index,'Open']).sum())))
summary = summary[summary['up_days']>summary['down_days']]
result = summary.reset_index().to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_LZrArnqQ3hWDEAwcrfaZCoM5': 'file_storage/call_LZrArnqQ3hWDEAwcrfaZCoM5.json', 'var_call_NtV0ylhLgiw0Jdmpd0RZCe9O': 'file_storage/call_NtV0ylhLgiw0Jdmpd0RZCe9O.json', 'var_call_H5aYOjUvCTaidF3bIXwo8Jln': {'count': 234, 'sample': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD']}, 'var_call_q8c3N3ijoxfkL7Vd6N3GgNiF': 'file_storage/call_q8c3N3ijoxfkL7Vd6N3GgNiF.json', 'var_call_ZURJ4OsYTAytXSbjUZRtoOnk': 'file_storage/call_ZURJ4OsYTAytXSbjUZRtoOnk.json'}

exec(code, env_args)
