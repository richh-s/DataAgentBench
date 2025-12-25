code = """import json, pandas as pd
from pathlib import Path

ppv = json.load(open(var_call_sqUqwZtlldWddjetrSI3Ie4j))
pi = json.load(open(var_call_pQoEG369J9omCPYrvkPedelV))

ppv_df = pd.DataFrame(ppv)
pi_df = pd.DataFrame(pi)

ppv_df = ppv_df[ppv_df['ProjectType'] == 'GITHUB']

pi_df = pi_df.copy()
pi_df['VersionInfo_json'] = pi_df['VersionInfo'].apply(json.loads)
pi_df['IsRelease'] = pi_df['VersionInfo_json'].apply(lambda x: x.get('IsRelease'))
pi_df['Ordinal'] = pi_df['VersionInfo_json'].apply(lambda x: x.get('Ordinal'))

pi_df = pi_df[pi_df['IsRelease'] == True]

pi_latest = pi_df.sort_values('Ordinal', ascending=False).drop_duplicates(['System','Name'])

merged = ppv_df.merge(pi_latest[['System','Name','Version']], on=['System','Name','Version'], how='inner')

result = merged[['System','Name','Version','ProjectName']].to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_sqUqwZtlldWddjetrSI3Ie4j': 'file_storage/call_sqUqwZtlldWddjetrSI3Ie4j.json', 'var_call_pQoEG369J9omCPYrvkPedelV': 'file_storage/call_pQoEG369J9omCPYrvkPedelV.json', 'var_call_Gqr5SsjNQpkZR3CKuvJo1BKr': 'file_storage/call_Gqr5SsjNQpkZR3CKuvJo1BKr.json'}

exec(code, env_args)
