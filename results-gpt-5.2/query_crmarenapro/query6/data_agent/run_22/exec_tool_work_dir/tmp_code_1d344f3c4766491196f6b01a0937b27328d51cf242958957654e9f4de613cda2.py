code = """import json, pandas as pd
from pathlib import Path

qli = pd.DataFrame(var_call_2bbJd7RPFRqZoGlMxzwSDFeO)
pbe = pd.DataFrame(var_call_Gme1TuW4y1dEkJyuBghujZQT)

# load knowledge articles (may be a file path)
ka_src = var_call_ew26c4UCMwE0Am5sCVQ1Wbv2
if isinstance(ka_src, str) and Path(ka_src).exists():
    ka = pd.read_json(ka_src)
else:
    ka = pd.DataFrame(ka_src)

# normalize ids by stripping leading '#', trimming
for df, col in [(qli,'PricebookEntryId'),(qli,'Product2Id'),(pbe,'PricebookEntryId'),(pbe,'Product2Id')]:
    if col in df.columns:
        df[col+'_norm'] = df[col].astype(str).str.strip().str.lstrip('#')

# numeric
for c in ['Quantity','UnitPrice','Discount','TotalPrice']:
    qli[c] = pd.to_numeric(qli[c], errors='coerce')

pbe['CatalogUnitPrice'] = pd.to_numeric(pbe['CatalogUnitPrice'], errors='coerce')

# join to catalog unit price
m = qli.merge(pbe[['PricebookEntryId_norm','CatalogUnitPrice']], left_on='PricebookEntryId_norm', right_on='PricebookEntryId_norm', how='left')

# detect price mismatch beyond tiny tolerance OR discount rule violations
# compute expected unit price from catalog (assuming unit price must match catalog before discount)
# discount stored as percent; if discount>0, unitprice should still match catalog and totalprice should be qty*unit*(1-discount/100)

tol = 0.01
m['unit_mismatch'] = (m['CatalogUnitPrice'].notna()) & ((m['UnitPrice'] - m['CatalogUnitPrice']).abs() > tol)

m['expected_total'] = m['Quantity'] * m['UnitPrice'] * (1 - (m['Discount'].fillna(0)/100.0))
m['total_mismatch'] = (m['TotalPrice'] - m['expected_total']).abs() > 0.05

# quantity rules: must be positive integer
m['qty_invalid'] = (m['Quantity']<=0) | (m['Quantity']%1!=0)

invalid = m[m['unit_mismatch'] | m['total_mismatch'] | m['qty_invalid']].copy()

# find best matching knowledge article id by simple keyword search for discount/price/quantity policy
text_cols = ['title','summary','faq_answer__c','urlname']
for c in text_cols:
    if c in ka.columns:
        ka[c] = ka[c].astype(str)

ka['alltext'] = ''
for c in text_cols:
    if c in ka.columns:
        ka['alltext'] += ' ' + ka[c]

keywords = ['quote','quotation','price','pricing','unit price','pricebook','discount','quantity','qty','configuration','invalid']
pattern = '|'.join([k.replace(' ','\\s+') for k in keywords])
ka['score'] = ka['alltext'].str.lower().apply(lambda s: sum(1 for k in keywords if k in s.lower()))

# prefer articles that mention discount/pricebook/quantity explicitly
ka['score'] += ka['alltext'].str.lower().str.contains('pricebook').astype(int)*3
ka['score'] += ka['alltext'].str.lower().str.contains('discount').astype(int)*3
ka['score'] += ka['alltext'].str.lower().str.contains('quantity').astype(int)*3
ka['score'] += ka['alltext'].str.lower().str.contains('unit price').astype(int)*2

best = ka.sort_values(['score'], ascending=False).head(20)

# pick first with nonzero score; else None
best_id = None
if len(best) and best.iloc[0]['score']>0:
    best_id = str(best.iloc[0]['id']).strip()

# if no invalid detected, return empty
out = best_id if (len(invalid)>0 and best_id is not None) else ''
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_2bbJd7RPFRqZoGlMxzwSDFeO': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_Gme1TuW4y1dEkJyuBghujZQT': [{'PricebookEntryId': '01uWt0000027P3mIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVhpIAE', 'CatalogUnitPrice': '489.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hV58IAE', 'CatalogUnitPrice': '599.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hTUkIAM', 'CatalogUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'CatalogUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PBpIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV9xIAE', 'CatalogUnitPrice': '449.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVBZIA2', 'CatalogUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PGfIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVEnIAM', 'CatalogUnitPrice': '479.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PIHIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVGPIA2', 'CatalogUnitPrice': '599.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVI1IAM', 'CatalogUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PLVIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVLFIA2', 'CatalogUnitPrice': '459.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPfgIAE', 'CatalogUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVMrIAM', 'CatalogUnitPrice': '299.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027POkIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hRfqIAE', 'CatalogUnitPrice': '349.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PRxIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVOTIA2', 'CatalogUnitPrice': '559.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVUvIAM', 'CatalogUnitPrice': '459.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'CatalogUnitPrice': '339.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ6IAM', 'CatalogUnitPrice': '429.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PYPIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVRhIAM', 'CatalogUnitPrice': '319.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVTJIA2', 'CatalogUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVZlIAM', 'CatalogUnitPrice': '559.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVbNIAU', 'CatalogUnitPrice': '349.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVebIAE', 'CatalogUnitPrice': '549.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PmvIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVJeIAM', 'CatalogUnitPrice': '599.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PoXIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVgDIAU', 'CatalogUnitPrice': '459.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjRIAU', 'CatalogUnitPrice': '429.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PrlIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVl3IAE', 'CatalogUnitPrice': '369.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVmfIAE', 'CatalogUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVwLIAU', 'CatalogUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PuzIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVoHIAU', 'CatalogUnitPrice': '629.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PyDIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVrVIAU', 'CatalogUnitPrice': '649.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVujIAE', 'CatalogUnitPrice': '579.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjSIAU', 'CatalogUnitPrice': '299.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUtqIAE', 'CatalogUnitPrice': '619.99', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}], 'var_call_ew26c4UCMwE0Am5sCVQ1Wbv2': 'file_storage/call_ew26c4UCMwE0Am5sCVQ1Wbv2.json', 'var_call_TC7HTMsVexk83IWkihRP8qkz': []}

exec(code, env_args)
