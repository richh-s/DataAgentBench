code = """import json, pandas as pd

qli = pd.DataFrame(var_call_ko8ET9g8CIx1eKbQGGtesz8h)
pbe = pd.DataFrame(var_call_BCa2reFVfJ8ChvYQaLWJx8kr)

def norm_id(x):
    if x is None:
        return None
    s = str(x).strip()
    return s[1:] if s.startswith('#') else s

for c in ['Product2Id','PricebookEntryId']:
    qli[c+'_n'] = qli[c].map(norm_id)
    pbe[c+'_n'] = pbe[c].map(norm_id)

qli['Quantity'] = qli['Quantity'].astype(float)
qli['UnitPrice'] = qli['UnitPrice'].astype(float)
qli['Discount'] = qli['Discount'].astype(float)
pbe['ListUnitPrice'] = pbe['ListUnitPrice'].astype(float)

m = qli.merge(pbe, left_on='PricebookEntryId_n', right_on='PricebookEntryId_n', how='left', suffixes=('','_pbe'))

m['unit_price_mismatch'] = (m['ListUnitPrice'].notna()) & ((m['UnitPrice'] - m['ListUnitPrice']).abs() > 1e-6)
m['discount_over_10pct'] = m['Discount'] > 10.0

signals = {
    'unit_price_mismatch': bool(m['unit_price_mismatch'].any()),
    'discount_over_10pct': bool(m['discount_over_10pct'].any()),
    'max_discount': float(m['Discount'].max()) if len(m) else None,
    'rows_with_discount_over_10pct': int(m['discount_over_10pct'].sum()) if len(m) else 0,
}

path = var_call_8rWqdNYVrPjT2MEPus9dNykV
with open(path,'r',encoding='utf-8') as f:
    kav = json.load(f)

kdf = pd.DataFrame(kav)
for col in ['title','summary','faq_answer__c']:
    if col in kdf.columns:
        kdf[col] = kdf[col].fillna('')

text = (kdf['title'] + '\n' + kdf['summary'] + '\n' + kdf['faq_answer__c']).str.lower()

candidates = pd.DataFrame([])
if signals['discount_over_10pct']:
    mask = text.str.contains('discount') & (text.str.contains('10%') | text.str.contains('ten percent') | text.str.contains('maximum'))
    candidates = kdf[mask]
elif signals['unit_price_mismatch']:
    mask = text.str.contains('price') & (text.str.contains('pricebook') | text.str.contains('list price') | text.str.contains('unit price'))
    candidates = kdf[mask]

article_id = None
if len(candidates):
    candidates = candidates.copy()
    candidates['score'] = candidates['title'].str.len()
    article_id = candidates.sort_values('score').iloc[0]['id']

print('__RESULT__:')
print(json.dumps({'article_id': article_id, 'signals': signals}))"""

env_args = {'var_call_ko8ET9g8CIx1eKbQGGtesz8h': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_8rWqdNYVrPjT2MEPus9dNykV': 'file_storage/call_8rWqdNYVrPjT2MEPus9dNykV.json', 'var_call_BCa2reFVfJ8ChvYQaLWJx8kr': [{'PricebookEntryId': '01uWt0000027P3mIAE', 'Product2Id': '01tWt000006hVhpIAE', 'ListUnitPrice': '489.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'Product2Id': '#01tWt000006hV58IAE', 'ListUnitPrice': '599.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'Product2Id': '01tWt000006hTUkIAM', 'ListUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'Product2Id': '01tWt000006hV8LIAU', 'ListUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PBpIAM', 'Product2Id': '01tWt000006hV9xIAE', 'ListUnitPrice': '449.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'Product2Id': '01tWt000006hVBZIA2', 'ListUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PGfIAM', 'Product2Id': '01tWt000006hVEnIAM', 'ListUnitPrice': '479.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PIHIA2', 'Product2Id': '#01tWt000006hVGPIA2', 'ListUnitPrice': '599.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'Product2Id': '01tWt000006hVI1IAM', 'ListUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PLVIA2', 'Product2Id': '#01tWt000006hVLFIA2', 'ListUnitPrice': '459.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'Product2Id': '01tWt000006hPfgIAE', 'ListUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'Product2Id': '01tWt000006hVMrIAM', 'ListUnitPrice': '299.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027POkIAM', 'Product2Id': '#01tWt000006hRfqIAE', 'ListUnitPrice': '349.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PRxIAM', 'Product2Id': '#01tWt000006hVOTIA2', 'ListUnitPrice': '559.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'Product2Id': '01tWt000006hVUvIAM', 'ListUnitPrice': '459.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'Product2Id': '01tWt000006hVQ5IAM', 'ListUnitPrice': '339.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'Product2Id': '01tWt000006hVQ6IAM', 'ListUnitPrice': '429.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PYPIA2', 'Product2Id': '#01tWt000006hVRhIAM', 'ListUnitPrice': '319.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'Product2Id': '01tWt000006hVTJIA2', 'ListUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'Product2Id': '01tWt000006hVZlIAM', 'ListUnitPrice': '559.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'Product2Id': '01tWt000006hVbNIAU', 'ListUnitPrice': '349.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'Product2Id': '01tWt000006hVebIAE', 'ListUnitPrice': '549.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PmvIAE', 'Product2Id': '01tWt000006hVJeIAM', 'ListUnitPrice': '599.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PoXIAU', 'Product2Id': '#01tWt000006hVgDIAU', 'ListUnitPrice': '459.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'Product2Id': '01tWt000006hVjRIAU', 'ListUnitPrice': '429.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PrlIAE', 'Product2Id': '01tWt000006hVl3IAE', 'ListUnitPrice': '369.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'Product2Id': '01tWt000006hVmfIAE', 'ListUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'Product2Id': '01tWt000006hVwLIAU', 'ListUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PuzIAE', 'Product2Id': '01tWt000006hVoHIAU', 'ListUnitPrice': '629.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PyDIAU', 'Product2Id': '01tWt000006hVrVIAU', 'ListUnitPrice': '649.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'Product2Id': '01tWt000006hVujIAE', 'ListUnitPrice': '579.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'Product2Id': '01tWt000006hVjSIAU', 'ListUnitPrice': '299.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'Product2Id': '01tWt000006hUtqIAE', 'ListUnitPrice': '619.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}], 'var_call_rVQHettWoaUhgQwHLRsSAp6g': []}

exec(code, env_args)
