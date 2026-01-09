code = """import json, pandas as pd

qlis = pd.DataFrame(var_call_QS7MFbRXM8CMb0vTPWGrW01I)
pbe = pd.DataFrame(var_call_CcFnDutiDeNYzdqnUcYnwmTY)

# normalize ids by stripping leading '#'
for c in ['Product2Id','PricebookEntryId']:
    qlis[c+'_n'] = qlis[c].astype(str).str.lstrip('#').str.strip()
pbe['PricebookEntryId_n'] = pbe['PricebookEntryId'].astype(str).str.lstrip('#').str.strip()

# numeric
for c in ['Quantity','UnitPrice','Discount','TotalPrice','ListUnitPrice']:
    if c in qlis.columns:
        qlis[c] = pd.to_numeric(qlis[c])
    if c in pbe.columns:
        pbe[c] = pd.to_numeric(pbe[c])

m = qlis.merge(pbe, left_on='PricebookEntryId_n', right_on='PricebookEntryId_n', how='left', suffixes=('','_list'))

# find violations: unit price not equal list price when discount is 0, or discount provided but unit price not list
violations = []
for _, r in m.iterrows():
    if pd.notna(r.get('ListUnitPrice')):
        if float(r['Discount'])==0 and abs(float(r['UnitPrice'])-float(r['ListUnitPrice']))>1e-6:
            violations.append('price_mismatch_no_discount')
        # discount in SF often percent; here discount=15 and totalprice not matching typical rule; flag discount >0
        if float(r['Discount'])>0:
            violations.append('discount_present_requires_approval')
    # quantity rule: unusually high quantity > 25
    if float(r['Quantity'])>25:
        violations.append('high_quantity_requires_approval')

# Decide which knowledge article id matches by keyword search
# Load knowledge articles
path = var_call_uETtG7639XeRKy1PRwtReeOd
with open(path,'r',encoding='utf-8') as f:
    kav = json.load(f)

df = pd.DataFrame(kav)
# search for likely policy articles
keywords = ['discount', 'approval', 'pricing', 'price', 'quantity', 'bulk']
pat = '|'.join([k.replace(' ','\\s+') for k in keywords])
df['text'] = (df['title'].fillna('')+' '+df['summary'].fillna('')+' '+df['faq_answer__c'].fillna('')).str.lower()
subset = df[df['text'].str.contains(pat, regex=True, na=False)].copy()

# rank by presence of violation-specific terms
score = pd.Series(0, index=subset.index)
if 'discount_present_requires_approval' in violations:
    score += subset['text'].str.count('discount')*3 + subset['text'].str.count('approval')*2
if 'high_quantity_requires_approval' in violations:
    score += subset['text'].str.count('quantity')*3 + subset['text'].str.count('bulk')*2
if 'price_mismatch_no_discount' in violations:
    score += subset['text'].str.count('price')*2 + subset['text'].str.count('pricing')*2
subset['score'] = score
subset = subset.sort_values(['score','id'], ascending=[False, True])
article_id = None
if len(subset)>0 and subset.iloc[0]['score']>0:
    article_id = subset.iloc[0]['id']

print('__RESULT__:')
print(json.dumps({'violations':sorted(set(violations)), 'article_id': article_id}))"""

env_args = {'var_call_QS7MFbRXM8CMb0vTPWGrW01I': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_uETtG7639XeRKy1PRwtReeOd': 'file_storage/call_uETtG7639XeRKy1PRwtReeOd.json', 'var_call_CcFnDutiDeNYzdqnUcYnwmTY': [{'PricebookEntryId': '01uWt0000027P3mIAE', 'ListUnitPrice': '489.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVhpIAE'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'ListUnitPrice': '599.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '#01tWt000006hV58IAE'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'ListUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hTUkIAM'}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'ListUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hV8LIAU'}, {'PricebookEntryId': '01uWt0000027PBpIAM', 'ListUnitPrice': '449.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hV9xIAE'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'ListUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVBZIA2'}, {'PricebookEntryId': '#01uWt0000027PGfIAM', 'ListUnitPrice': '479.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVEnIAM'}, {'PricebookEntryId': '01uWt0000027PIHIA2', 'ListUnitPrice': '599.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '#01tWt000006hVGPIA2'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'ListUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVI1IAM'}, {'PricebookEntryId': '01uWt0000027PLVIA2', 'ListUnitPrice': '459.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '#01tWt000006hVLFIA2'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'ListUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hPfgIAE'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'ListUnitPrice': '299.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVMrIAM'}, {'PricebookEntryId': '01uWt0000027POkIAM', 'ListUnitPrice': '349.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '#01tWt000006hRfqIAE'}, {'PricebookEntryId': '#01uWt0000027PRxIAM', 'ListUnitPrice': '559.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '#01tWt000006hVOTIA2'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'ListUnitPrice': '459.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVUvIAM'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'ListUnitPrice': '339.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVQ5IAM'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'ListUnitPrice': '429.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVQ6IAM'}, {'PricebookEntryId': '01uWt0000027PYPIA2', 'ListUnitPrice': '319.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '#01tWt000006hVRhIAM'}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'ListUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVTJIA2'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'ListUnitPrice': '559.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVZlIAM'}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'ListUnitPrice': '349.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVbNIAU'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'ListUnitPrice': '549.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVebIAE'}, {'PricebookEntryId': '#01uWt0000027PmvIAE', 'ListUnitPrice': '599.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVJeIAM'}, {'PricebookEntryId': '01uWt0000027PoXIAU', 'ListUnitPrice': '459.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '#01tWt000006hVgDIAU'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'ListUnitPrice': '429.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVjRIAU'}, {'PricebookEntryId': '01uWt0000027PrlIAE', 'ListUnitPrice': '369.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVl3IAE'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'ListUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVmfIAE'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'ListUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVwLIAU'}, {'PricebookEntryId': '01uWt0000027PuzIAE', 'ListUnitPrice': '629.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVoHIAU'}, {'PricebookEntryId': '#01uWt0000027PyDIAU', 'ListUnitPrice': '649.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVrVIAU'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'ListUnitPrice': '579.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVujIAE'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'ListUnitPrice': '299.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVjSIAU'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'ListUnitPrice': '619.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hUtqIAE'}], 'var_call_iAH1F1AEJXL6nbvvO6ZrXgtQ': []}

exec(code, env_args)
