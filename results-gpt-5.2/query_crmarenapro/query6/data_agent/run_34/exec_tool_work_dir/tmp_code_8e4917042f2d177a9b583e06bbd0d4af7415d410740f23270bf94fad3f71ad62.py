code = """import json, pandas as pd, re

qli = pd.DataFrame(var_call_auBbeRtkSbWVftqp774qx7sD)
pbe = pd.DataFrame(var_call_QEwqOveOAkG3T6IZsVdZRTa2)

# normalize ids by stripping leading # and whitespace
for col in ['Product2Id','PricebookEntryId']:
    qli[col+'_norm'] = qli[col].astype(str).str.strip().str.lstrip('#')
    pbe[col+'_norm'] = pbe[col].astype(str).str.strip().str.lstrip('#')

qli['Quantity'] = qli['Quantity'].astype(float)
qli['UnitPrice'] = qli['UnitPrice'].astype(float)
qli['Discount'] = qli['Discount'].astype(float)

# join to list price
pbe_map = pbe[['PricebookEntryId','ListUnitPrice','ProductName']].copy()
pbe_map['PricebookEntryId_norm'] = pbe_map['PricebookEntryId'].astype(str).str.strip().str.lstrip('#')
pbe_map['ListUnitPrice'] = pbe_map['ListUnitPrice'].astype(float)

m = qli.merge(pbe_map, on='PricebookEntryId_norm', how='left')

# detect violations: unit price different from list by > 0.01 without discount, or very high qty with discount >0 etc.
viol = []
for _, r in m.iterrows():
    if pd.notna(r['ListUnitPrice']):
        if abs(r['UnitPrice'] - r['ListUnitPrice']) > 0.01 and r['Discount'] == 0:
            viol.append('unit_price_not_list')
    if r['Discount'] > 0 and r['Discount'] >= 15 and r['Quantity'] >= 25:
        viol.append('bulk_discount_threshold')

# load knowledge articles
import pathlib
path = var_call_Dtu3Uu5Pmc0XntSSBLsIkjt6
arts = json.load(open(path,'r'))
ka = pd.DataFrame(arts)

# pick article matching bulk discount policy keywords
text = (ka['title'].fillna('') + ' ' + ka['summary'].fillna('') + ' ' + ka['faq_answer__c'].fillna('')).str.lower()
patterns = [r'bulk\s+discount', r'discount\s+policy', r'max(imum)?\s+discount', r'pricing\s+policy', r'quantity\s+discount', r'approval.*discount']
score = pd.Series(0, index=ka.index)
for pat in patterns:
    score += text.str.count(pat)

# if bulk discount violation present, choose top scored; else choose top for unit price policy
if 'bulk_discount_threshold' in viol:
    idx = score.sort_values(ascending=False).index[0]
else:
    # fallback: look for list price adherence policy
    score2 = text.str.count(r'list\s+price|unit\s+price|price\s+book|pricebook')
    idx = score2.sort_values(ascending=False).index[0]

ans = ka.loc[idx, 'id']

print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_auBbeRtkSbWVftqp774qx7sD': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_Dtu3Uu5Pmc0XntSSBLsIkjt6': 'file_storage/call_Dtu3Uu5Pmc0XntSSBLsIkjt6.json', 'var_call_QEwqOveOAkG3T6IZsVdZRTa2': [{'PricebookEntryId': '01uWt0000027P3lIAE', 'ListUnitPrice': '499.99', 'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'ListUnitPrice': '599.99', 'Product2Id': '#01tWt000006hV58IAE', 'ProductName': 'SecureFlow Suite'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'PricebookEntryId': '#01uWt0000027P8bIAE', 'ListUnitPrice': '349.99', 'Product2Id': '01tWt000006hV6jIAE', 'ProductName': 'EcoPCB Creator   '}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'ListUnitPrice': '529.99', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech'}, {'PricebookEntryId': '01uWt0000027PADIA2', 'ListUnitPrice': '299.99', 'Product2Id': '01tWt000006hPffIAE', 'ProductName': 'DevVision IDE'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hVBZIA2', 'ProductName': 'EduTech Lab'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'ListUnitPrice': '529.99', 'Product2Id': '01tWt000006hVI1IAM', 'ProductName': 'AIOptics Vision'}, {'PricebookEntryId': '01uWt0000027PIJIA2', 'ListUnitPrice': '459.99', 'Product2Id': '01tWt000006hVptIAE', 'ProductName': 'DesignEdge Pro'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hPfgIAE', 'ProductName': 'EcoPower Convert'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'ListUnitPrice': '299.99', 'Product2Id': '01tWt000006hVMrIAM', 'ProductName': 'TrainEDU Suite'}, {'PricebookEntryId': '01uWt0000027PTZIA2', 'ListUnitPrice': '449.99', 'Product2Id': '01tWt000006hV0IIAU', 'ProductName': 'NextGen IDE'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'ListUnitPrice': '459.99', 'Product2Id': '01tWt000006hVUvIAM', 'ProductName': 'OptiEnergy Suite'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'ListUnitPrice': '339.99', 'Product2Id': '01tWt000006hVQ5IAM', 'ProductName': 'CircuitSync Pro'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'ListUnitPrice': '429.99', 'Product2Id': '01tWt000006hVQ6IAM', 'ProductName': 'VeriSim Express  '}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'ListUnitPrice': '529.99', 'Product2Id': '01tWt000006hVTJIA2', 'ProductName': 'IntegrGuard Secure'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'ListUnitPrice': '559.99', 'Product2Id': '01tWt000006hVZlIAM', 'ProductName': 'SecuManage Pro  '}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'ListUnitPrice': '349.99', 'Product2Id': '01tWt000006hVbNIAU', 'ProductName': 'EnergyReduce Pro'}, {'PricebookEntryId': '01uWt0000027PgUIAU', 'ListUnitPrice': '379.99', 'Product2Id': '01tWt000006hVt7IAE', 'ProductName': 'PCB EcoModel  '}, {'PricebookEntryId': '01uWt0000027Pi5IAE', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hVczIAE', 'ProductName': 'CollabDesign Studio'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'ListUnitPrice': '549.99', 'Product2Id': '01tWt000006hVebIAE', 'ProductName': 'CircuitAI Innovator'}, {'PricebookEntryId': '01uWt0000027PlJIAU', 'ListUnitPrice': '499.99', 'Product2Id': '01tWt000006hUsEIAU', 'ProductName': 'SimuCheck Ultra'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'ListUnitPrice': '429.99', 'Product2Id': '01tWt000006hVjRIAU', 'ProductName': 'Workflow Genius'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hVmfIAE', 'ProductName': 'EduTech Advance'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'ListUnitPrice': '529.99', 'Product2Id': '01tWt000006hVwLIAU', 'ProductName': 'SimulateX Edge'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'ListUnitPrice': '579.99', 'Product2Id': '01tWt000006hVujIAE', 'ProductName': 'CyberShield Core'}, {'PricebookEntryId': '#01uWt0000027Q33IAE', 'ListUnitPrice': '499.99', 'Product2Id': '01tWt000006hOd8IAE', 'ProductName': 'AutoLayout Master'}, {'PricebookEntryId': '#01uWt0000027Q34IAE', 'ListUnitPrice': '599.99', 'Product2Id': '01tWt000006hUgwIAE', 'ProductName': 'AI DesignShift'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'ListUnitPrice': '299.99', 'Product2Id': '01tWt000006hVjSIAU', 'ProductName': 'InnoTrain Hub'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'ListUnitPrice': '619.99', 'Product2Id': '01tWt000006hUtqIAE', 'ProductName': 'SecureTrack Pro '}]}

exec(code, env_args)
