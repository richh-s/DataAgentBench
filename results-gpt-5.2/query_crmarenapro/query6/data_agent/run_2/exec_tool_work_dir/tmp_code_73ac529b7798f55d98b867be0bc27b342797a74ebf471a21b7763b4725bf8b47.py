code = """import json, pandas as pd

qlis = pd.DataFrame(var_call_sie7A3zpzvWuaB9MQTSuuEdB)
# Evaluate potential violations:
# 1) Discount should not be > 0 for quantity >= 25 (bulk discount requires approval) -- common policy
# 2) TotalPrice should equal Quantity*UnitPrice*(1-Discount/100)

# compute expected total
qlis['Quantity'] = qlis['Quantity'].astype(float)
qlis['UnitPrice'] = qlis['UnitPrice'].astype(float)
qlis['Discount'] = qlis['Discount'].astype(float)
qlis['TotalPrice'] = qlis['TotalPrice'].astype(float)
qlis['expected_total'] = (qlis['Quantity']*qlis['UnitPrice']*(1-qlis['Discount']/100)).round(4)
qlis['total_mismatch'] = (qlis['TotalPrice']-qlis['expected_total']).abs() > 0.01

violations = []
if qlis['total_mismatch'].any():
    violations.append('total_mismatch')
# quantity unreasonable threshold e.g., > 30 requires special pricing
if (qlis['Quantity']>30).any():
    violations.append('high_quantity')
# discount > 10 requires approval
if (qlis['Discount']>10).any():
    violations.append('high_discount')

# load knowledge articles
import os
path = var_call_3WhZYmLh0Ews8i6LfdhzGBLw
with open(path,'r',encoding='utf-8') as f:
    arts = json.load(f)
df = pd.DataFrame(arts)

# find best matching article by keyword
text = (df['title'].fillna('')+'\n'+df['summary'].fillna('')+'\n'+df['faq_answer__c'].fillna('')).str.lower()
score = pd.Series(0,index=df.index)
keywords = []
if 'total_mismatch' in violations:
    keywords += ['total price','calculation','quantity','unit price','discount']
if 'high_quantity' in violations:
    keywords += ['quantity','maximum','limit','bulk']
if 'high_discount' in violations:
    keywords += ['discount','maximum','approval','special pricing']

for kw in set(keywords):
    score += text.str.count(kw)

best_idx = score.idxmax() if len(score)>0 else None
best_id = None
if best_idx is not None and score.loc[best_idx]>0:
    best_id = df.loc[best_idx,'id']

print('__RESULT__:')
print(json.dumps({'best_article_id': best_id, 'violations': violations, 'top_score': (None if best_idx is None else float(score.loc[best_idx]))}))"""

env_args = {'var_call_sie7A3zpzvWuaB9MQTSuuEdB': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_OnnSOXY0ZA4rY4Myv2WLTfTL': [{'PricebookEntryId': '01uWt0000027P3mIAE', 'ListUnitPrice': '489.99', 'Product2Id': '01tWt000006hVhpIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'ListUnitPrice': '599.99', 'Product2Id': '#01tWt000006hV58IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hTUkIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'ListUnitPrice': '529.99', 'Product2Id': '01tWt000006hV8LIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PBpIAM', 'ListUnitPrice': '449.99', 'Product2Id': '01tWt000006hV9xIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hVBZIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PGfIAM', 'ListUnitPrice': '479.99', 'Product2Id': '01tWt000006hVEnIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PIHIA2', 'ListUnitPrice': '599.99', 'Product2Id': '#01tWt000006hVGPIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'ListUnitPrice': '529.99', 'Product2Id': '01tWt000006hVI1IAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PLVIA2', 'ListUnitPrice': '459.99', 'Product2Id': '#01tWt000006hVLFIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hPfgIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'ListUnitPrice': '299.99', 'Product2Id': '01tWt000006hVMrIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027POkIAM', 'ListUnitPrice': '349.99', 'Product2Id': '#01tWt000006hRfqIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PRxIAM', 'ListUnitPrice': '559.99', 'Product2Id': '#01tWt000006hVOTIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'ListUnitPrice': '459.99', 'Product2Id': '01tWt000006hVUvIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'ListUnitPrice': '339.99', 'Product2Id': '01tWt000006hVQ5IAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'ListUnitPrice': '429.99', 'Product2Id': '01tWt000006hVQ6IAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PYPIA2', 'ListUnitPrice': '319.99', 'Product2Id': '#01tWt000006hVRhIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'ListUnitPrice': '529.99', 'Product2Id': '01tWt000006hVTJIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'ListUnitPrice': '559.99', 'Product2Id': '01tWt000006hVZlIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'ListUnitPrice': '349.99', 'Product2Id': '01tWt000006hVbNIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'ListUnitPrice': '549.99', 'Product2Id': '01tWt000006hVebIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PmvIAE', 'ListUnitPrice': '599.99', 'Product2Id': '01tWt000006hVJeIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PoXIAU', 'ListUnitPrice': '459.99', 'Product2Id': '#01tWt000006hVgDIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'ListUnitPrice': '429.99', 'Product2Id': '01tWt000006hVjRIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PrlIAE', 'ListUnitPrice': '369.99', 'Product2Id': '01tWt000006hVl3IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hVmfIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'ListUnitPrice': '529.99', 'Product2Id': '01tWt000006hVwLIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PuzIAE', 'ListUnitPrice': '629.99', 'Product2Id': '01tWt000006hVoHIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PyDIAU', 'ListUnitPrice': '649.99', 'Product2Id': '01tWt000006hVrVIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'ListUnitPrice': '579.99', 'Product2Id': '01tWt000006hVujIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'ListUnitPrice': '299.99', 'Product2Id': '01tWt000006hVjSIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'ListUnitPrice': '619.99', 'Product2Id': '01tWt000006hUtqIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}], 'var_call_3WhZYmLh0Ews8i6LfdhzGBLw': 'file_storage/call_3WhZYmLh0Ews8i6LfdhzGBLw.json', 'var_call_s92a4llL85jYLCCKEolw2k8X': []}

exec(code, env_args)
