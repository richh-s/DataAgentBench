code = """import json
orders = var_call_5CMwjwP2PcGLrFEnxK1Ejf7N
acct = var_call_RwVWINHOuquNvUIPJNi1ugZ7[0]['AccountId']
acct_clean = acct.replace('#','') if acct else None
candidate = None
for row in orders:
    if row['AccountId'].replace('#','') == acct_clean:
        if row['EffectiveDate'] >= '2021-06-15' and row['EffectiveDate'] < '2021-07-15':
            candidate = row['Product2Id']
            break

result = candidate
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_e3R2EleYZq1HsZKwZ6AVFz2i': [], 'var_call_qTLjLIxLFjLoV5Br7aG42tjS': [], 'var_call_5CMwjwP2PcGLrFEnxK1Ejf7N': [{'Product2Id': '#01tWt000006hV9xIAE', 'AccountId': '001Wt00000PHRF9IAP', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hTUkIAM', 'AccountId': '001Wt00000PHRF9IAP', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hV58IAE', 'AccountId': '001Wt00000PHRF9IAP', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hV6jIAE', 'AccountId': '001Wt00000PHRF9IAP', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '#01tWt000006hV6jIAE', 'AccountId': '001Wt00000PGoAaIAL', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hTUkIAM', 'AccountId': '001Wt00000PGoAaIAL', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hV58IAE', 'AccountId': '001Wt00000PGoAaIAL', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hV8LIAU', 'AccountId': '001Wt00000PGoAaIAL', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hV58IAE', 'AccountId': '001Wt00000PHRF9IAP', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hV6jIAE', 'AccountId': '001Wt00000PHRF9IAP', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hV9xIAE', 'AccountId': '001Wt00000PHRF9IAP', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hVBZIA2', 'AccountId': '001Wt00000PHRF9IAP', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hVMrIAM', 'AccountId': '001Wt00000PHRF9IAP', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hV8LIAU', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-06-15'}, {'Product2Id': '01tWt000006hTUkIAM', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01'}, {'Product2Id': '01tWt000006hV58IAE', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01'}, {'Product2Id': '01tWt000006hV57IAE', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01'}, {'Product2Id': '01tWt000006hV58IAE', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01'}], 'var_call_rxPESwOO7MIsLGBa6ewJhaAb': [{'Id': '003Wt00000Jqy8SIAR'}], 'var_call_RwVWINHOuquNvUIPJNi1ugZ7': [{'AccountId': '#001Wt00000PGXrNIAX'}]}

exec(code, env_args)
