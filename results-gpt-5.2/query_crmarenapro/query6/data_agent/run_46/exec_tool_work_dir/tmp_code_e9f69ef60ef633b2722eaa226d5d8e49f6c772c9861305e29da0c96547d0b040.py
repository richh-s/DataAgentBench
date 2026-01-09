code = """import json, pandas as pd

qli = pd.DataFrame(var_call_8lKYrCUqe4Tf1dYq4qV1TYif)
cat = pd.DataFrame(var_call_dIje4Z4YSZLGqffDvAJbMHC5)

# normalize id-like fields by stripping leading '#'
def norm(s):
    if pd.isna(s):
        return s
    s = str(s).strip()
    return s[1:] if s.startswith('#') else s

for c in ['Product2Id','PricebookEntryId','Id','QuoteId']:
    if c in qli.columns:
        qli[c+'_n'] = qli[c].map(norm)
for c in ['Product2Id','PricebookEntryId']:
    cat[c+'_n'] = cat[c].map(norm)

# cast numerics
for c in ['Quantity','UnitPrice','Discount','TotalPrice']:
    qli[c] = pd.to_numeric(qli[c], errors='coerce')
cat['CatalogUnitPrice'] = pd.to_numeric(cat['CatalogUnitPrice'], errors='coerce')

m = qli.merge(cat, left_on='PricebookEntryId_n', right_on='PricebookEntryId_n', how='left', suffixes=('','_cat'))

# detect price mismatches vs pricebook entry
m['price_mismatch'] = (m['CatalogUnitPrice'].notna()) & (m['UnitPrice'].round(2) != m['CatalogUnitPrice'].round(2))

# detect unusually high discount (>10%)
m['high_discount'] = m['Discount'].fillna(0) > 10

# detect unusually high quantity (>25)
m['high_qty'] = m['Quantity'].fillna(0) > 25

violations = {
    'price_mismatch': bool(m['price_mismatch'].any()),
    'high_discount': bool(m['high_discount'].any()),
    'high_qty': bool(m['high_qty'].any())
}

# load knowledge articles
import pathlib
ka_path = var_call_dPXO5StbV0VMO5L5cmlhSIwk
if isinstance(ka_path, str) and ka_path.endswith('.json'):
    with open(ka_path, 'r', encoding='utf-8') as f:
        kas = json.load(f)
else:
    kas = var_call_dPXO5StbV0VMO5L5cmlhSIwk

dfka = pd.DataFrame(kas)
for col in ['title','summary','faq_answer__c','urlname','id']:
    if col in dfka.columns:
        dfka[col] = dfka[col].astype(str)

text = (dfka.get('title','') + ' ' + dfka.get('summary','') + ' ' + dfka.get('faq_answer__c','')).str.lower()

# find best matching article for the triggered violation
# priority: discount policy, then quantity limits, then price integrity
queries = []
if violations['high_discount']:
    queries.append(['discount','maximum discount','approval','discount policy'])
if violations['high_qty']:
    queries.append(['quantity','maximum quantity','bulk','order limit','quote line quantity'])
if violations['price_mismatch']:
    queries.append(['unit price','pricebook','standard price','pricing policy','price mismatch'])

best_id = None
best_score = -1
for terms in queries:
    termset = [t.lower() for t in terms]
    scores = text.apply(lambda t: sum(1 for term in termset if term in t))
    idx = int(scores.idxmax()) if len(scores) else None
    score = int(scores.max()) if len(scores) else -1
    if score > best_score:
        best_score = score
        best_id = dfka.loc[idx,'id'] if idx is not None else None

# fallback: if no meaningful match, return null
if best_score <= 0:
    best_id = None

print('__RESULT__:')
print(json.dumps({'knowledge_article_id': best_id, 'violations': violations}))"""

env_args = {'var_call_8lKYrCUqe4Tf1dYq4qV1TYif': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_dPXO5StbV0VMO5L5cmlhSIwk': 'file_storage/call_dPXO5StbV0VMO5L5cmlhSIwk.json', 'var_call_dIje4Z4YSZLGqffDvAJbMHC5': [{'PricebookEntryId': '01uWt0000027P5NIAU', 'CatalogUnitPrice': '599.99', 'PricebookName': 'Standard Price Book', 'ValidFrom': 'None', 'ValidTo': 'None', 'Product2Id': '#01tWt000006hV58IAE', 'ProductName': 'SecureFlow Suite', 'IsActive': '1'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'CatalogUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'ValidFrom': 'None', 'ValidTo': 'None', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer', 'IsActive': '1'}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'CatalogUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'ValidFrom': 'None', 'ValidTo': 'None', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech', 'IsActive': '1'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'CatalogUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'ValidFrom': 'None', 'ValidTo': 'None', 'Product2Id': '01tWt000006hVBZIA2', 'ProductName': 'EduTech Lab', 'IsActive': '1'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'CatalogUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'ValidFrom': 'None', 'ValidTo': 'None', 'Product2Id': '01tWt000006hVI1IAM', 'ProductName': 'AIOptics Vision', 'IsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'CatalogUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'ValidFrom': 'None', 'ValidTo': 'None', 'Product2Id': '01tWt000006hPfgIAE', 'ProductName': 'EcoPower Convert', 'IsActive': '1'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'CatalogUnitPrice': '299.99', 'PricebookName': 'Standard Price Book', 'ValidFrom': 'None', 'ValidTo': 'None', 'Product2Id': '01tWt000006hVMrIAM', 'ProductName': 'TrainEDU Suite', 'IsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'CatalogUnitPrice': '459.99', 'PricebookName': 'Standard Price Book', 'ValidFrom': 'None', 'ValidTo': 'None', 'Product2Id': '01tWt000006hVUvIAM', 'ProductName': 'OptiEnergy Suite', 'IsActive': '1'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'CatalogUnitPrice': '339.99', 'PricebookName': 'Standard Price Book', 'ValidFrom': 'None', 'ValidTo': 'None', 'Product2Id': '01tWt000006hVQ5IAM', 'ProductName': 'CircuitSync Pro', 'IsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'CatalogUnitPrice': '429.99', 'PricebookName': 'Standard Price Book', 'ValidFrom': 'None', 'ValidTo': 'None', 'Product2Id': '01tWt000006hVQ6IAM', 'ProductName': 'VeriSim Express  ', 'IsActive': '1'}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'CatalogUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'ValidFrom': 'None', 'ValidTo': 'None', 'Product2Id': '01tWt000006hVTJIA2', 'ProductName': 'IntegrGuard Secure', 'IsActive': '1'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'CatalogUnitPrice': '559.99', 'PricebookName': 'Standard Price Book', 'ValidFrom': 'None', 'ValidTo': 'None', 'Product2Id': '01tWt000006hVZlIAM', 'ProductName': 'SecuManage Pro  ', 'IsActive': '1'}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'CatalogUnitPrice': '349.99', 'PricebookName': 'Standard Price Book', 'ValidFrom': 'None', 'ValidTo': 'None', 'Product2Id': '01tWt000006hVbNIAU', 'ProductName': 'EnergyReduce Pro', 'IsActive': '1'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'CatalogUnitPrice': '549.99', 'PricebookName': 'Standard Price Book', 'ValidFrom': 'None', 'ValidTo': 'None', 'Product2Id': '01tWt000006hVebIAE', 'ProductName': 'CircuitAI Innovator', 'IsActive': '1'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'CatalogUnitPrice': '429.99', 'PricebookName': 'Standard Price Book', 'ValidFrom': 'None', 'ValidTo': 'None', 'Product2Id': '01tWt000006hVjRIAU', 'ProductName': 'Workflow Genius', 'IsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'CatalogUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'ValidFrom': 'None', 'ValidTo': 'None', 'Product2Id': '01tWt000006hVmfIAE', 'ProductName': 'EduTech Advance', 'IsActive': '1'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'CatalogUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'ValidFrom': 'None', 'ValidTo': 'None', 'Product2Id': '01tWt000006hVwLIAU', 'ProductName': 'SimulateX Edge', 'IsActive': '1'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'CatalogUnitPrice': '579.99', 'PricebookName': 'Standard Price Book', 'ValidFrom': 'None', 'ValidTo': 'None', 'Product2Id': '01tWt000006hVujIAE', 'ProductName': 'CyberShield Core', 'IsActive': '1'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'CatalogUnitPrice': '299.99', 'PricebookName': 'Standard Price Book', 'ValidFrom': 'None', 'ValidTo': 'None', 'Product2Id': '01tWt000006hVjSIAU', 'ProductName': 'InnoTrain Hub', 'IsActive': '1'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'CatalogUnitPrice': '619.99', 'PricebookName': 'Standard Price Book', 'ValidFrom': 'None', 'ValidTo': 'None', 'Product2Id': '01tWt000006hUtqIAE', 'ProductName': 'SecureTrack Pro ', 'IsActive': '1'}]}

exec(code, env_args)
