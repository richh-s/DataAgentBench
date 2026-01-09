code = """import json, pandas as pd

def norm(s):
    if s is None:
        return None
    return str(s).replace('#','').strip()

opp = pd.DataFrame(var_call_9JkKHdzE20IulgkZXUVYoXUr)
ordr = pd.DataFrame(var_call_Z3Bm4ZICj4fwjlx0ycKESkyN)

opp['AccountId_n'] = opp['AccountId'].map(norm)
ordr['AccountId_n'] = ordr['AccountId'].map(norm)

# restrict orders to accounts tied to the contact's opps last month
accounts = set(opp['AccountId_n'].dropna().unique().tolist())
ordr2 = ordr[ordr['AccountId_n'].isin(accounts)].copy()

# AI processing unit heuristic: product name contains 'AI'
ordr2['ProductName_n'] = ordr2['ProductName'].astype(str).str.strip()
ai = ordr2[ordr2['ProductName_n'].str.contains(r'\bAI\b|AI', case=False, regex=True)]

product_id = None
if len(ai) > 0:
    # choose most recent effective date then first
    ai['EffectiveDate_dt'] = pd.to_datetime(ai['EffectiveDate'], errors='coerce')
    ai = ai.sort_values(['EffectiveDate_dt','OrderId'], ascending=[False, True])
    product_id = norm(ai.iloc[0]['Product2Id'])

result = json.dumps(product_id)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_Z3Bm4ZICj4fwjlx0ycKESkyN': [{'OrderId': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech'}, {'OrderId': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-06-15', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE', 'ProductName': 'SecureFlow Suite'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE', 'ProductName': 'SecureFlow Suite'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '#01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech'}], 'var_call_9JkKHdzE20IulgkZXUVYoXUr': [{'Id': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'StageName': 'Discovery'}, {'Id': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'StageName': 'Negotiation'}]}

exec(code, env_args)
