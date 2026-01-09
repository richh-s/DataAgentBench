code = """import json, pandas as pd

def norm(x):
    if x is None:
        return None
    return str(x).replace('#','').strip()

contact = var_call_xHKni3bPNsnTEtPN0JtjAr1w[0]
contact_acct = norm(contact['AccountId'])

orders = pd.DataFrame(var_call_lazpg2Z8w3TJodBdVmPKrS9l)
if not orders.empty:
    orders['AccountId_n'] = orders['AccountId'].map(norm)
    orders['Product2Id_n'] = orders['Product2Id'].map(norm)

# Only orders for this contact's account
orders_c = orders[orders['AccountId_n'] == contact_acct].copy()

# Identify AI processing unit product: best effort via name containing 'AI' (from provided product subset)
prods = pd.DataFrame(var_call_aF8ifUG42nI2iQ0ybs3DnQFw)
prods['Id_n'] = prods['Id'].map(norm)
prods['Name_n'] = prods['Name'].astype(str).str.strip().str.lower()

# Choose AI-related products; if multiple, select the one appearing in last month's orders
ai_prod_ids = set(prods[prods['Name_n'].str.contains('ai')]['Id_n'].tolist())

orders_ai = orders_c[orders_c['Product2Id_n'].isin(ai_prod_ids)].copy()
# last month relative to 2021-07-15 -> 2021-06-01..2021-07-01 already filtered; choose latest effective date, then first
if orders_ai.empty:
    product_id = None
else:
    orders_ai['EffectiveDate'] = pd.to_datetime(orders_ai['EffectiveDate'])
    orders_ai = orders_ai.sort_values(['EffectiveDate','OrderId'], ascending=[False, False])
    product_id = orders_ai.iloc[0]['Product2Id_n']

print('__RESULT__:')
print(json.dumps(product_id))"""

env_args = {'var_call_kKAbnGtayTYk8woST2s8bFmk': [{'Id': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}, {'Id': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}], 'var_call_lazpg2Z8w3TJodBdVmPKrS9l': [{'OrderId': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU'}, {'OrderId': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-06-15', 'Product2Id': '01tWt000006hTUkIAM'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV57IAE'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hTUkIAM'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '#01tWt000006hTUkIAM'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV57IAE'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV8LIAU'}], 'var_call_aF8ifUG42nI2iQ0ybs3DnQFw': [{'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}], 'var_call_xHKni3bPNsnTEtPN0JtjAr1w': [{'Id': '003Wt00000Jqy8SIAR', 'AccountId': '#001Wt00000PGXrNIAX'}], 'var_call_V2pVW4bUKijFtOJST4lAptJC': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem']}

exec(code, env_args)
