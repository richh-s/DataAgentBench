code = """import json, pandas as pd

qli = pd.DataFrame(var_call_qqmGQt8pLuXkWscnT43edsWe)
pbe = pd.DataFrame(var_call_teXaox1CJdwlKzettwk5Mz7b)

# Normalize ids by stripping leading '#'
def norm(s):
    if s is None:
        return None
    s = str(s).strip()
    return s[1:] if s.startswith('#') else s

for c in ['Product2Id','PricebookEntryId']:
    qli[c+'_n'] = qli[c].map(norm)
pbe['PricebookEntryId_n'] = pbe['PricebookEntryId'].map(norm)
pbe['Product2Id_n'] = pbe['Product2Id'].map(norm)

# Join quote line item to pricebook entry by pricebook entry id
m = qli.merge(pbe, left_on='PricebookEntryId_n', right_on='PricebookEntryId_n', how='left', suffixes=('','_pbe'))

# Determine violations: pricebook entry missing OR unit price mismatch OR negative/zero quantity OR discount out of range
m['Quantity_f'] = pd.to_numeric(m['Quantity'], errors='coerce')
m['UnitPrice_f'] = pd.to_numeric(m['UnitPrice'], errors='coerce')
m['Discount_f'] = pd.to_numeric(m['Discount'], errors='coerce')
m['CatalogUnitPrice_f'] = pd.to_numeric(m['CatalogUnitPrice'], errors='coerce')

m['missing_pbe'] = m['PricebookEntryId_n'].notna() & m['CatalogUnitPrice'].isna()
m['qty_invalid'] = (m['Quantity_f'].isna()) | (m['Quantity_f'] <= 0)
m['discount_invalid'] = (m['Discount_f'].isna()) | (m['Discount_f'] < 0) | (m['Discount_f'] > 100)
# mismatch if catalog price known and differs materially
m['price_mismatch'] = (~m['CatalogUnitPrice_f'].isna()) & (~m['UnitPrice_f'].isna()) & ((m['UnitPrice_f'] - m['CatalogUnitPrice_f']).abs() > 0.01)

violations = {
    'missing_pbe': bool(m['missing_pbe'].any()),
    'price_mismatch': bool(m['price_mismatch'].any()),
    'qty_invalid': bool(m['qty_invalid'].any()),
    'discount_invalid': bool(m['discount_invalid'].any()),
}

# Load knowledge articles
path = var_call_ooq4QN73QiW0DjmL57352lvp
with open(path, 'r', encoding='utf-8') as f:
    kav = json.load(f)
ka = pd.DataFrame(kav)

def find_article(keywords):
    # search in title/summary/faq
    pat = '|'.join([k.replace(' ','\\s+') for k in keywords])
    mask = ka['title'].fillna('').str.contains(pat, case=False, regex=True) | \
           ka['summary'].fillna('').str.contains(pat, case=False, regex=True) | \
           ka['faq_answer__c'].fillna('').str.contains(pat, case=False, regex=True)
    hits = ka[mask].copy()
    if hits.empty:
        return None
    # prefer titles mentioning policy/regulation/quote/pricing/discount
    score = (
        hits['title'].fillna('').str.contains('policy|regulation|quote|pricing|discount|pricebook|quantity', case=False, regex=True).astype(int)*2 +
        hits['summary'].fillna('').str.contains('policy|regulation|quote|pricing|discount|pricebook|quantity', case=False, regex=True).astype(int) +
        hits['faq_answer__c'].fillna('').str.contains('policy|regulation|quote|pricing|discount|pricebook|quantity', case=False, regex=True).astype(int)
    )
    hits['_score']=score
    hits = hits.sort_values(['_score','id'], ascending=[False, True])
    return hits.iloc[0]['id']

article_id = None
if violations['missing_pbe']:
    article_id = find_article(['pricebook entry','price book','pricebook'])
if article_id is None and violations['price_mismatch']:
    article_id = find_article(['unit price','catalog price','price mismatch','pricebook'])
if article_id is None and violations['discount_invalid']:
    article_id = find_article(['discount','maximum discount','approval'])
if article_id is None and violations['qty_invalid']:
    article_id = find_article(['quantity','minimum order','qty'])

# Fallback: if any violation but not found, attempt generic pricing policy
if article_id is None and any(violations.values()):
    article_id = find_article(['pricing policy','quote policy','sales policy','discount policy'])

print('__RESULT__:')
print(json.dumps({'violations': violations, 'article_id': article_id}))"""

env_args = {'var_call_qqmGQt8pLuXkWscnT43edsWe': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_teXaox1CJdwlKzettwk5Mz7b': [{'PricebookEntryId': '01uWt0000027P3mIAE', 'Product2Id': '01tWt000006hVhpIAE', 'CatalogUnitPrice': '489.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'Product2Id': '#01tWt000006hV58IAE', 'CatalogUnitPrice': '599.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'Product2Id': '01tWt000006hTUkIAM', 'CatalogUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'Product2Id': '01tWt000006hV8LIAU', 'CatalogUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PBpIAM', 'Product2Id': '01tWt000006hV9xIAE', 'CatalogUnitPrice': '449.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'Product2Id': '01tWt000006hVBZIA2', 'CatalogUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PGfIAM', 'Product2Id': '01tWt000006hVEnIAM', 'CatalogUnitPrice': '479.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PIHIA2', 'Product2Id': '#01tWt000006hVGPIA2', 'CatalogUnitPrice': '599.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'Product2Id': '01tWt000006hVI1IAM', 'CatalogUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PLVIA2', 'Product2Id': '#01tWt000006hVLFIA2', 'CatalogUnitPrice': '459.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'Product2Id': '01tWt000006hPfgIAE', 'CatalogUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'Product2Id': '01tWt000006hVMrIAM', 'CatalogUnitPrice': '299.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027POkIAM', 'Product2Id': '#01tWt000006hRfqIAE', 'CatalogUnitPrice': '349.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PRxIAM', 'Product2Id': '#01tWt000006hVOTIA2', 'CatalogUnitPrice': '559.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'Product2Id': '01tWt000006hVUvIAM', 'CatalogUnitPrice': '459.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'Product2Id': '01tWt000006hVQ5IAM', 'CatalogUnitPrice': '339.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'Product2Id': '01tWt000006hVQ6IAM', 'CatalogUnitPrice': '429.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PYPIA2', 'Product2Id': '#01tWt000006hVRhIAM', 'CatalogUnitPrice': '319.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'Product2Id': '01tWt000006hVTJIA2', 'CatalogUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'Product2Id': '01tWt000006hVZlIAM', 'CatalogUnitPrice': '559.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'Product2Id': '01tWt000006hVbNIAU', 'CatalogUnitPrice': '349.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'Product2Id': '01tWt000006hVebIAE', 'CatalogUnitPrice': '549.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PmvIAE', 'Product2Id': '01tWt000006hVJeIAM', 'CatalogUnitPrice': '599.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PoXIAU', 'Product2Id': '#01tWt000006hVgDIAU', 'CatalogUnitPrice': '459.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'Product2Id': '01tWt000006hVjRIAU', 'CatalogUnitPrice': '429.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PrlIAE', 'Product2Id': '01tWt000006hVl3IAE', 'CatalogUnitPrice': '369.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'Product2Id': '01tWt000006hVmfIAE', 'CatalogUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'Product2Id': '01tWt000006hVwLIAU', 'CatalogUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PuzIAE', 'Product2Id': '01tWt000006hVoHIAU', 'CatalogUnitPrice': '629.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PyDIAU', 'Product2Id': '01tWt000006hVrVIAU', 'CatalogUnitPrice': '649.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'Product2Id': '01tWt000006hVujIAE', 'CatalogUnitPrice': '579.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'Product2Id': '01tWt000006hVjSIAU', 'CatalogUnitPrice': '299.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'Product2Id': '01tWt000006hUtqIAE', 'CatalogUnitPrice': '619.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}], 'var_call_ooq4QN73QiW0DjmL57352lvp': 'file_storage/call_ooq4QN73QiW0DjmL57352lvp.json'}

exec(code, env_args)
