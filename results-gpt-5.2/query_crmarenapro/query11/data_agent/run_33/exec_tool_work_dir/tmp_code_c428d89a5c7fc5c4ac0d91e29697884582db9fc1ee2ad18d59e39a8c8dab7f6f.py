code = """import json, pandas as pd

contact = pd.DataFrame(var_call_mJyNIiFj5ZqBqVYbeD1hLoCK)
acct_id = contact.loc[0,'AccountId']
acct_id_norm = str(acct_id).replace('#','').strip()

orders = pd.DataFrame(var_call_z1UyCiFOo5Yb5f48oqykDBf3)
orders['AccountId_norm'] = orders['AccountId'].astype(str).str.replace('#','', regex=False).str.strip()
orders_contact = orders[orders['AccountId_norm']==acct_id_norm].copy()

prods_ai = pd.DataFrame(var_call_iDqX8cAdyAg31GIj5J5gC0jS)
prods_ai['Id_norm'] = prods_ai['Id'].astype(str).str.replace('#','', regex=False).str.strip()
ai_set = set(prods_ai['Id_norm'].tolist())

# Combine product ids from orders and opportunity line items for last month
oli = pd.DataFrame(var_call_XFubVNjwh0hjJmo6x2Pndopn)
oli['Product2Id_norm'] = oli['Product2Id'].astype(str).str.replace('#','', regex=False).str.strip()

order_prod_ids = set(orders_contact['Product2Id'].astype(str).str.replace('#','', regex=False).str.strip().tolist())
oli_prod_ids = set(oli['Product2Id_norm'].tolist())

candidate = [pid for pid in (order_prod_ids.union(oli_prod_ids)) if pid in ai_set]
# pick deterministic: if multiple, prefer ones that appear in contact's orders first by date desc
chosen = None
if len(candidate)==1:
    chosen = candidate[0]
else:
    # rank by appearance in orders desc, then in oli
    if not orders_contact.empty:
        orders_contact['Product2Id_norm'] = orders_contact['Product2Id'].astype(str).str.replace('#','', regex=False).str.strip()
        ordered = orders_contact.sort_values('EffectiveDate', ascending=False)['Product2Id_norm'].tolist()
        for pid in ordered:
            if pid in candidate:
                chosen = pid
                break
    if chosen is None:
        for pid in sorted(candidate):
            chosen = pid
            break

result = chosen if chosen is not None else None
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_z1UyCiFOo5Yb5f48oqykDBf3': [{'OrderId': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hTUkIAM'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV57IAE'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE'}], 'var_call_mJyNIiFj5ZqBqVYbeD1hLoCK': [{'Id': '003Wt00000Jqy8SIAR', 'AccountId': '#001Wt00000PGXrNIAX'}], 'var_call_iDqX8cAdyAg31GIj5J5gC0jS': [{'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}], 'var_call_YO2QcUiYpKHrPsCxKBLDTju2': [{'Id': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}, {'Id': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}], 'var_call_XFubVNjwh0hjJmo6x2Pndopn': [{'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '#01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hTUkIAM'}, {'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '01tWt000006hV9xIAE'}]}

exec(code, env_args)
