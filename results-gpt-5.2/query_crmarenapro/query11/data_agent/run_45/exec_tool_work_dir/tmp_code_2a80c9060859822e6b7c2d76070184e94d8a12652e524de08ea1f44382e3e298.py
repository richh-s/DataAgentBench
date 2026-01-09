code = """import json, pandas as pd
opp = pd.DataFrame(var_call_UrnYSRbkKRk7SoYQsj4nfnEB)
orders = pd.DataFrame(var_call_WcM6m6I3kEIhmHiaHG8Doj9D)
for df in (opp, orders):
    for c in df.columns:
        if df[c].dtype == 'object':
            df[c] = df[c].astype(str).str.strip()
            if c.lower().endswith('id') or c in ['OrderId','Product2Id','AccountId','ContactId','Id']:
                df[c+'_clean'] = df[c].str.replace('#','', regex=False)

# join on AccountId and date
opp['CloseDate'] = pd.to_datetime(opp['CloseDate']).dt.date
orders['EffectiveDate'] = pd.to_datetime(orders['EffectiveDate']).dt.date
merged = opp.merge(orders, left_on=['AccountId_clean','CloseDate'], right_on=['AccountId_clean','EffectiveDate'], how='inner')
# filter product name contains AI
merged_ai = merged[merged['ProductName'].str.contains('AI', case=False, na=False)].copy()
# pick most recent (and if multiple, first)
merged_ai = merged_ai.sort_values(['CloseDate','OrderId'], ascending=[False, True])
product_id = merged_ai['Product2Id_clean'].iloc[0] if len(merged_ai) else None
print('__RESULT__:')
print(json.dumps({'Product2Id': product_id}))"""

env_args = {'var_call_WcM6m6I3kEIhmHiaHG8Doj9D': [{'OrderId': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro'}], 'var_call_UrnYSRbkKRk7SoYQsj4nfnEB': [{'Id': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}, {'Id': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}]}

exec(code, env_args)
