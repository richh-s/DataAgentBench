code = """import json, pandas as pd

ql = pd.DataFrame(var_call_kLBQeIswlBN2OkAWfecdrrK1)
cat = pd.DataFrame(var_call_DZKCrgawtHy6Fj9ffguZ72n1)

# normalize ids by stripping leading '#'
def norm(s):
    if s is None:
        return None
    s = str(s).strip()
    return s[1:] if s.startswith('#') else s

for c in ['Product2Id','PricebookEntryId']:
    ql[c+'_n'] = ql[c].map(norm)

cat['Product2Id_n'] = cat['Product2Id'].map(norm)
cat['PricebookEntryId_n'] = cat['PricebookEntryId'].map(norm)

# join on PricebookEntryId primarily; fall back to Product2Id if needed
j = ql.merge(cat, left_on='PricebookEntryId_n', right_on='PricebookEntryId_n', how='left', suffixes=('','_cat'))

# determine violations
violations = []

# rule: unit price should match catalog unit price when discount is 0
j['UnitPrice_f'] = j['UnitPrice'].astype(float)
j['CatalogUnitPrice_f'] = pd.to_numeric(j['CatalogUnitPrice'], errors='coerce')
j['Discount_f'] = j['Discount'].astype(float)

price_mismatch = j[(j['Discount_f']==0) & (j['CatalogUnitPrice_f'].notna()) & (abs(j['UnitPrice_f']-j['CatalogUnitPrice_f'])>1e-6)]
if len(price_mismatch)>0:
    violations.append('PRICE_MISMATCH')

# rule: discount percent must be <= 10
if (j['Discount_f']>10).any():
    violations.append('DISCOUNT_GT_10')

# rule: quantity must be integer and <= 30
j['Quantity_f'] = j['Quantity'].astype(float)
qty_bad = j[(j['Quantity_f']%1!=0) | (j['Quantity_f']>30) | (j['Quantity_f']<=0)]
if len(qty_bad)>0:
    violations.append('QTY_BAD')

# load knowledge articles
path = var_call_b62yKm0x8piHrtT0zudMyoET
with open(path,'r',encoding='utf-8') as f:
    kav = json.load(f)

# find best matching article for our violation keywords
text_fields = ['title','summary','faq_answer__c','urlname']

def score_article(a, keywords):
    blob = ' '.join([str(a.get(tf,'') or '') for tf in text_fields]).lower()
    return sum(1 for kw in keywords if kw in blob)

candidates = []
if 'DISCOUNT_GT_10' in violations:
    keywords = ['discount','maximum','max','%','percent','approval']
    for a in kav:
        sc = score_article(a, keywords)
        if sc:
            candidates.append((sc,a['id']))
if not candidates and ('QTY_BAD' in violations):
    keywords = ['quantity','maximum','max','limit','minimum','min']
    for a in kav:
        sc = score_article(a, keywords)
        if sc:
            candidates.append((sc,a['id']))
if not candidates and ('PRICE_MISMATCH' in violations):
    keywords = ['price','pricing','unit price','list price','pricebook']
    for a in kav:
        sc = score_article(a, keywords)
        if sc:
            candidates.append((sc,a['id']))

best_id = None
if candidates:
    candidates.sort(key=lambda x:(-x[0], x[1]))
    best_id = candidates[0][1]

print('__RESULT__:')
print(json.dumps(best_id))"""

env_args = {'var_call_kLBQeIswlBN2OkAWfecdrrK1': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_DZKCrgawtHy6Fj9ffguZ72n1': [{'PricebookEntryId': '01uWt0000027P5NIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hV58IAE', 'CatalogUnitPrice': '599.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'SecureFlow Suite', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hTUkIAM', 'CatalogUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'CloudLink Designer', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'CatalogUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'AI Cirku-Tech', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVBZIA2', 'CatalogUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'EduTech Lab', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVI1IAM', 'CatalogUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'AIOptics Vision', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPfgIAE', 'CatalogUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'EcoPower Convert', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVMrIAM', 'CatalogUnitPrice': '299.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'TrainEDU Suite', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVUvIAM', 'CatalogUnitPrice': '459.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'OptiEnergy Suite', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'CatalogUnitPrice': '339.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'CircuitSync Pro', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ6IAM', 'CatalogUnitPrice': '429.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'VeriSim Express  ', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVTJIA2', 'CatalogUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'IntegrGuard Secure', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVZlIAM', 'CatalogUnitPrice': '559.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'SecuManage Pro  ', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVbNIAU', 'CatalogUnitPrice': '349.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'EnergyReduce Pro', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVebIAE', 'CatalogUnitPrice': '549.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'CircuitAI Innovator', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjRIAU', 'CatalogUnitPrice': '429.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'Workflow Genius', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVmfIAE', 'CatalogUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'EduTech Advance', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVwLIAU', 'CatalogUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'SimulateX Edge', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVujIAE', 'CatalogUnitPrice': '579.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'CyberShield Core', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjSIAU', 'CatalogUnitPrice': '299.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'InnoTrain Hub', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUtqIAE', 'CatalogUnitPrice': '619.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'SecureTrack Pro ', 'ProductIsActive': '1'}], 'var_call_b62yKm0x8piHrtT0zudMyoET': 'file_storage/call_b62yKm0x8piHrtT0zudMyoET.json', 'var_call_iGLR3UFPAzgcOPI6u0RoIwCi': []}

exec(code, env_args)
