code = """import json, pandas as pd

qli = pd.DataFrame(var_call_UTuHwp2nkrCkemcHPVPaz95M)
cat = pd.DataFrame(var_call_op3t0CnAle6HU06pToiG8DYp)

# normalize id-like fields by stripping leading '#', trimming spaces
for c in ['Product2Id','PricebookEntryId']:
    qli[c+'_norm'] = qli[c].astype(str).str.strip().str.lstrip('#')
cat['Product2Id_norm'] = cat['Product2Id'].astype(str).str.strip().str.lstrip('#')
cat['PricebookEntryId_norm'] = cat['PricebookEntryId'].astype(str).str.strip().str.lstrip('#')

# cast numerics
for c in ['Quantity','UnitPrice','Discount','TotalPrice']:
    qli[c] = qli[c].astype(float)
cat['CatalogUnitPrice'] = cat['CatalogUnitPrice'].astype(float)

m = qli.merge(cat, left_on='PricebookEntryId_norm', right_on='PricebookEntryId_norm', how='left', suffixes=('','_cat'))

# violations:
# A) unit price must match catalog unit price when Discount is 0
m['viol_unitprice_mismatch_no_discount'] = (m['Discount'].fillna(0)==0) & (m['CatalogUnitPrice'].notna()) & (m['UnitPrice'].round(2) != m['CatalogUnitPrice'].round(2))
# B) quantity must be <= 20 (assumed common policy) OR C) discount must be <= 10% (assumed)
# We'll infer policy from knowledge articles by keyword search later; here just flag observed: quantity 35, discount 15
m['viol_quantity_high'] = m['Quantity'] > 20
m['viol_discount_high'] = m['Discount'] > 10

violations = m.loc[m[['viol_unitprice_mismatch_no_discount','viol_quantity_high','viol_discount_high']].any(axis=1), ['Id','ProductName','Quantity','UnitPrice','Discount','CatalogUnitPrice','viol_unitprice_mismatch_no_discount','viol_quantity_high','viol_discount_high']]

# load knowledge articles
path_or_records = var_call_owPcUzSilUnbyAdhJlAdABVy
if isinstance(path_or_records, str) and path_or_records.endswith('.json'):
    with open(path_or_records,'r',encoding='utf-8') as f:
        kav = json.load(f)
else:
    kav = path_or_records
kdf = pd.DataFrame(kav)

# find most relevant article by matching policy-like keywords
text = (kdf.get('title','').fillna('') + ' ' + kdf.get('summary','').fillna('') + ' ' + kdf.get('faq_answer__c','').fillna('')).astype(str)
# keywords related to discount approvals / max discount / bulk quantity / pricing policy / quote line item
keywords = ['discount','maximum discount','max discount','discount approval','pricing policy','unit price','price override','quantity','bulk','maximum quantity','quote','quote line']
score = pd.Series(0, index=kdf.index, dtype=int)
for kw in keywords:
    score += text.str.lower().str.contains(kw).astype(int)

kdf['score'] = score
kdf_sorted = kdf.sort_values(['score'], ascending=False)

result = {
    'violations': violations.to_dict(orient='records'),
    'top_articles': kdf_sorted.head(20)[['id','title','score']].to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_UTuHwp2nkrCkemcHPVPaz95M': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_op3t0CnAle6HU06pToiG8DYp': [{'PricebookEntryId': '01uWt0000027P3lIAE', 'CatalogUnitPrice': '499.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'CatalogUnitPrice': '599.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hV58IAE', 'ProductName': 'SecureFlow Suite'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'CatalogUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'PricebookEntryId': '#01uWt0000027P8bIAE', 'CatalogUnitPrice': '349.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV6jIAE', 'ProductName': 'EcoPCB Creator   '}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'CatalogUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech'}, {'PricebookEntryId': '01uWt0000027PADIA2', 'CatalogUnitPrice': '299.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'ProductName': 'DevVision IDE'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'CatalogUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVBZIA2', 'ProductName': 'EduTech Lab'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'CatalogUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVI1IAM', 'ProductName': 'AIOptics Vision'}, {'PricebookEntryId': '01uWt0000027PIJIA2', 'CatalogUnitPrice': '459.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVptIAE', 'ProductName': 'DesignEdge Pro'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'CatalogUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPfgIAE', 'ProductName': 'EcoPower Convert'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'CatalogUnitPrice': '299.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVMrIAM', 'ProductName': 'TrainEDU Suite'}, {'PricebookEntryId': '01uWt0000027PTZIA2', 'CatalogUnitPrice': '449.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV0IIAU', 'ProductName': 'NextGen IDE'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'CatalogUnitPrice': '459.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVUvIAM', 'ProductName': 'OptiEnergy Suite'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'CatalogUnitPrice': '339.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'ProductName': 'CircuitSync Pro'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'CatalogUnitPrice': '429.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ6IAM', 'ProductName': 'VeriSim Express  '}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'CatalogUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVTJIA2', 'ProductName': 'IntegrGuard Secure'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'CatalogUnitPrice': '559.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVZlIAM', 'ProductName': 'SecuManage Pro  '}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'CatalogUnitPrice': '349.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVbNIAU', 'ProductName': 'EnergyReduce Pro'}, {'PricebookEntryId': '01uWt0000027PgUIAU', 'CatalogUnitPrice': '379.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVt7IAE', 'ProductName': 'PCB EcoModel  '}, {'PricebookEntryId': '01uWt0000027Pi5IAE', 'CatalogUnitPrice': '399.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'ProductName': 'CollabDesign Studio'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'CatalogUnitPrice': '549.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVebIAE', 'ProductName': 'CircuitAI Innovator'}, {'PricebookEntryId': '01uWt0000027PlJIAU', 'CatalogUnitPrice': '499.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUsEIAU', 'ProductName': 'SimuCheck Ultra'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'CatalogUnitPrice': '429.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjRIAU', 'ProductName': 'Workflow Genius'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'CatalogUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVmfIAE', 'ProductName': 'EduTech Advance'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'CatalogUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVwLIAU', 'ProductName': 'SimulateX Edge'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'CatalogUnitPrice': '579.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVujIAE', 'ProductName': 'CyberShield Core'}, {'PricebookEntryId': '#01uWt0000027Q33IAE', 'CatalogUnitPrice': '499.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hOd8IAE', 'ProductName': 'AutoLayout Master'}, {'PricebookEntryId': '#01uWt0000027Q34IAE', 'CatalogUnitPrice': '599.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUgwIAE', 'ProductName': 'AI DesignShift'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'CatalogUnitPrice': '299.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjSIAU', 'ProductName': 'InnoTrain Hub'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'CatalogUnitPrice': '619.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUtqIAE', 'ProductName': 'SecureTrack Pro '}], 'var_call_owPcUzSilUnbyAdhJlAdABVy': 'file_storage/call_owPcUzSilUnbyAdhJlAdABVy.json', 'var_call_DzjVPKCNuL8MoW64hzLDuTeR': []}

exec(code, env_args)
