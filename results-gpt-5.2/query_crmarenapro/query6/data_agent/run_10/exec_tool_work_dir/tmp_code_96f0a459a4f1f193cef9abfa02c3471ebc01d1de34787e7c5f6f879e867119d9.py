code = """import json, pandas as pd

qli = pd.DataFrame(var_call_aWq7pY9lFoS5g0jNEexF4PLJ)
pbe = pd.DataFrame(var_call_AUTudaTJ9iabAGiEXXHBijTb)

# normalize ids
for df, col in [(qli,'PricebookEntryId'),(qli,'Product2Id'),(pbe,'PricebookEntryId'),(pbe,'Product2Id')]:
    df[col] = df[col].astype(str).str.replace('#','', regex=False).str.strip()

# numeric
for col in ['Quantity','UnitPrice','Discount','TotalPrice']:
    qli[col] = pd.to_numeric(qli[col], errors='coerce')
pbe['CatalogUnitPrice'] = pd.to_numeric(pbe['CatalogUnitPrice'], errors='coerce')

m = qli.merge(pbe[['PricebookEntryId','Product2Id','CatalogUnitPrice']], on='PricebookEntryId', how='left', suffixes=('','_cat'))

# find invalid: unit price differs from catalog for same pricebook entry (beyond tiny tolerance)
invalid_price = m[(m['CatalogUnitPrice'].notna()) & ((m['UnitPrice'] - m['CatalogUnitPrice']).abs() > 0.01)]

# load knowledge articles
path = var_call_A2xoezntwmV3pKJP8ev0Kq0t
with open(path, 'r', encoding='utf-8') as f:
    kav = json.load(f)
ka = pd.DataFrame(kav)
for c in ['id','title','faq_answer__c','summary','urlname']:
    if c in ka.columns:
        ka[c] = ka[c].astype(str)

# If invalid price exists, pick article most related to pricing/discount/unit price policy
kw = ['price','pricing','discount','unit price','override','list price','pricebook']
text = (ka.get('title','') + ' ' + ka.get('summary','') + ' ' + ka.get('faq_answer__c','')).str.lower()
score = sum(text.str.contains(k, regex=False).astype(int) for k in kw)
ka_scored = ka.assign(_score=score)
ka_scored = ka_scored.sort_values(['_score','id'], ascending=[False, True])

result_id = None
if len(invalid_price) > 0:
    # take best scored article with some match
    top = ka_scored.iloc[0]
    result_id = top['id']

print('__RESULT__:')
print(json.dumps({'knowledge_article_id': result_id}))"""

env_args = {'var_call_aWq7pY9lFoS5g0jNEexF4PLJ': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_AUTudaTJ9iabAGiEXXHBijTb': [{'PricebookEntryId': '01uWt0000027P5NIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hV58IAE', 'CatalogUnitPrice': '599.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'SecureFlow Suite', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hTUkIAM', 'CatalogUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'CloudLink Designer', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'CatalogUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'AI Cirku-Tech', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVBZIA2', 'CatalogUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'EduTech Lab', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVI1IAM', 'CatalogUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'AIOptics Vision', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPfgIAE', 'CatalogUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'EcoPower Convert', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVMrIAM', 'CatalogUnitPrice': '299.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'TrainEDU Suite', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVUvIAM', 'CatalogUnitPrice': '459.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'OptiEnergy Suite', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'CatalogUnitPrice': '339.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'CircuitSync Pro', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ6IAM', 'CatalogUnitPrice': '429.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'VeriSim Express  ', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVTJIA2', 'CatalogUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'IntegrGuard Secure', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVZlIAM', 'CatalogUnitPrice': '559.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'SecuManage Pro  ', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVbNIAU', 'CatalogUnitPrice': '349.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'EnergyReduce Pro', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVebIAE', 'CatalogUnitPrice': '549.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'CircuitAI Innovator', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjRIAU', 'CatalogUnitPrice': '429.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'Workflow Genius', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVmfIAE', 'CatalogUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'EduTech Advance', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVwLIAU', 'CatalogUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'SimulateX Edge', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVujIAE', 'CatalogUnitPrice': '579.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'CyberShield Core', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjSIAU', 'CatalogUnitPrice': '299.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'InnoTrain Hub', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUtqIAE', 'CatalogUnitPrice': '619.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'SecureTrack Pro ', 'ProductIsActive': '1'}], 'var_call_A2xoezntwmV3pKJP8ev0Kq0t': 'file_storage/call_A2xoezntwmV3pKJP8ev0Kq0t.json'}

exec(code, env_args)
