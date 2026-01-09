code = """import json, pandas as pd

ql = pd.DataFrame(var_call_5PN2qVN5w66ISJNwlSvA1VVS)
pbe = pd.DataFrame(var_call_mxOBmgURIgZdmW4cjM0hmHHT)

# normalize ids by stripping leading # and whitespace
for df, cols in [(ql, ['Product2Id','PricebookEntryId']), (pbe, ['Product2Id','PricebookEntryId'])]:
    for c in cols:
        if c in df.columns:
            df[c] = df[c].astype(str).str.strip().str.lstrip('#')

# numeric conversions
for c in ['Quantity','UnitPrice','Discount','TotalPrice']:
    ql[c] = pd.to_numeric(ql[c], errors='coerce')

pbe['ListUnitPrice'] = pd.to_numeric(pbe['ListUnitPrice'], errors='coerce')

m = ql.merge(pbe[['PricebookEntryId','ListUnitPrice']], on='PricebookEntryId', how='left')

# detect unit price not equal list price and/or discount rules
m['unit_price_mismatch'] = (m['ListUnitPrice'].notna()) & (m['UnitPrice'].round(2) != m['ListUnitPrice'].round(2))

# detect totalprice mismatch given discount percent
m['expected_total'] = (m['Quantity'] * m['UnitPrice'] * (1 - (m['Discount'].fillna(0)/100.0)))
# allow small floating tolerance
m['total_mismatch'] = (m['TotalPrice'] - m['expected_total']).abs() > 0.01

# detect high quantity with discount maybe violates (assume discount >10% requires approval)
m['high_discount'] = m['Discount'].fillna(0) > 10

issues = {
    'unit_price_mismatch': int(m['unit_price_mismatch'].sum()),
    'total_mismatch': int(m['total_mismatch'].sum()),
    'high_discount': int(m['high_discount'].sum()),
    'any_issue': bool((m['unit_price_mismatch']|m['total_mismatch']|m['high_discount']).any())
}

# load knowledge articles
import os
ka = var_call_eW5hrJX4Amr0TqU9wIuj9uAz
if isinstance(ka, str) and os.path.exists(ka):
    with open(ka,'r',encoding='utf-8') as f:
        ka = json.load(f)
ka_df = pd.DataFrame(ka)
for c in ['title','summary','faq_answer__c']:
    ka_df[c] = ka_df[c].astype(str)

text = (ka_df['title'].fillna('') + ' ' + ka_df['summary'].fillna('') + ' ' + ka_df['faq_answer__c'].fillna('')).str.lower()

# heuristics: find pricing/discount/quantity policy articles
keywords = ['discount','pricing','price','quote','quotation','quantity','approval','list price','unit price','maximum','bulk']
score = sum(text.str.contains(k).astype(int) for k in keywords)
ka_df['score'] = score
cand = ka_df.sort_values(['score'], ascending=False).head(50)

# pick best matching based on which issue occurs
need = []
if issues['high_discount']:
    need += ['discount','approval']
if issues['unit_price_mismatch']:
    need += ['list price','unit price','pricing']
if issues['total_mismatch']:
    need += ['total','calculation']

if need:
    cand['need_score'] = sum((cand['title'].str.lower()+ ' '+cand['faq_answer__c'].str.lower()).str.contains(k).astype(int) for k in need)
else:
    cand['need_score'] = 0
best = cand.sort_values(['need_score','score'], ascending=False).head(1)

best_id = None
if issues['any_issue'] and len(best):
    best_id = best.iloc[0]['id']

print('__RESULT__:')
print(json.dumps({'best_article_id': best_id, 'issues': issues}))"""

env_args = {'var_call_5PN2qVN5w66ISJNwlSvA1VVS': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_eW5hrJX4Amr0TqU9wIuj9uAz': 'file_storage/call_eW5hrJX4Amr0TqU9wIuj9uAz.json', 'var_call_mxOBmgURIgZdmW4cjM0hmHHT': [{'PricebookEntryId': '01uWt0000027P5NIAU', 'ListUnitPrice': '599.99', 'Product2Id': '#01tWt000006hV58IAE', 'ProductName': 'SecureFlow Suite', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'ListUnitPrice': '529.99', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hVBZIA2', 'ProductName': 'EduTech Lab', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'ListUnitPrice': '529.99', 'Product2Id': '01tWt000006hVI1IAM', 'ProductName': 'AIOptics Vision', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hPfgIAE', 'ProductName': 'EcoPower Convert', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'ListUnitPrice': '299.99', 'Product2Id': '01tWt000006hVMrIAM', 'ProductName': 'TrainEDU Suite', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'ListUnitPrice': '459.99', 'Product2Id': '01tWt000006hVUvIAM', 'ProductName': 'OptiEnergy Suite', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'ListUnitPrice': '339.99', 'Product2Id': '01tWt000006hVQ5IAM', 'ProductName': 'CircuitSync Pro', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'ListUnitPrice': '429.99', 'Product2Id': '01tWt000006hVQ6IAM', 'ProductName': 'VeriSim Express  ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'ListUnitPrice': '529.99', 'Product2Id': '01tWt000006hVTJIA2', 'ProductName': 'IntegrGuard Secure', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'ListUnitPrice': '559.99', 'Product2Id': '01tWt000006hVZlIAM', 'ProductName': 'SecuManage Pro  ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'ListUnitPrice': '349.99', 'Product2Id': '01tWt000006hVbNIAU', 'ProductName': 'EnergyReduce Pro', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'ListUnitPrice': '549.99', 'Product2Id': '01tWt000006hVebIAE', 'ProductName': 'CircuitAI Innovator', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'ListUnitPrice': '429.99', 'Product2Id': '01tWt000006hVjRIAU', 'ProductName': 'Workflow Genius', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hVmfIAE', 'ProductName': 'EduTech Advance', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'ListUnitPrice': '529.99', 'Product2Id': '01tWt000006hVwLIAU', 'ProductName': 'SimulateX Edge', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'ListUnitPrice': '579.99', 'Product2Id': '01tWt000006hVujIAE', 'ProductName': 'CyberShield Core', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'ListUnitPrice': '299.99', 'Product2Id': '01tWt000006hVjSIAU', 'ProductName': 'InnoTrain Hub', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'ListUnitPrice': '619.99', 'Product2Id': '01tWt000006hUtqIAE', 'ProductName': 'SecureTrack Pro ', 'PricebookName': 'Standard Price Book'}], 'var_call_1D8EFqt0r2GzeOOHLmIT5L54': []}

exec(code, env_args)
