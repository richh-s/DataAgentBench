code = """import json, re, pandas as pd

latest_links = json.loads(var_call_PRjLJYbNo7s13uD567KIhUfM)
pi_df = pd.read_json(var_call_Gqr5SsjNQpkZR3CKuvJo1BKr)

pi_df['ProjectName'] = pi_df['Project_Information'].str.extract(r'The project ([^ ]+/[^ ]+)')[0]
pi_df['Stars'] = pi_df['Project_Information'].str.extract(r'(?:has|with) (?:a total of )?([0-9,]+) stars')[0].str.replace(',','').astype('float')

links_df = pd.DataFrame(latest_links)
merged = links_df.merge(pi_df[['ProjectName','Stars']], on='ProjectName', how='left')

merged = merged.dropna(subset=['Stars'])

result_df = merged.sort_values('Stars', ascending=False).drop_duplicates(['System','Name']).head(5)

result = result_df[['Name','Version','ProjectName','Stars']].to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_call_sqUqwZtlldWddjetrSI3Ie4j': 'file_storage/call_sqUqwZtlldWddjetrSI3Ie4j.json', 'var_call_pQoEG369J9omCPYrvkPedelV': 'file_storage/call_pQoEG369J9omCPYrvkPedelV.json', 'var_call_Gqr5SsjNQpkZR3CKuvJo1BKr': 'file_storage/call_Gqr5SsjNQpkZR3CKuvJo1BKr.json', 'var_call_PRjLJYbNo7s13uD567KIhUfM': 'file_storage/call_PRjLJYbNo7s13uD567KIhUfM.json'}

exec(code, env_args)
