code = """import json, pandas as pd

qli = pd.DataFrame(var_call_7Rm2YVxJ9CXg0QrC7G3Ysfki)
pbe = pd.DataFrame(var_call_ANXk5GVm5FKccaOUn0leqFqU)

# normalize ids by stripping leading '#'
def norm(s):
    if s is None:
        return None
    s = str(s).strip()
    return s[1:] if s.startswith('#') else s

for c in ['PricebookEntryId','Product2Id']:
    qli[c+'_n'] = qli[c].map(norm)

pbe['PricebookEntryId_n'] = pbe['PricebookEntryId'].map(norm)

# join to get catalog unit price
m = qli.merge(pbe[['PricebookEntryId_n','CatalogUnitPrice']], left_on='PricebookEntryId_n', right_on='PricebookEntryId_n', how='left')

# numeric
for col in ['Quantity','UnitPrice','Discount','TotalPrice','CatalogUnitPrice']:
    if col in m.columns:
        m[col] = pd.to_numeric(m[col], errors='coerce')

# identify possible violations: unit price differs from catalog, discount >10%, quantity unusually high (>25)
violations = []
if (m['CatalogUnitPrice'].notna() & (m['UnitPrice'].round(2) != m['CatalogUnitPrice'].round(2))).any():
    violations.append('price_mismatch')
if (m['Discount'] > 10).any():
    violations.append('discount_gt_10')
if (m['Quantity'] > 25).any():
    violations.append('qty_gt_25')

# load knowledge
ka = var_call_Re2ArPRPcDFxvQBny0eu9WE4
if isinstance(ka, str):
    with open(ka, 'r', encoding='utf-8') as f:
        ka_records = json.load(f)
else:
    ka_records = ka
kdf = pd.DataFrame(ka_records)

# search for relevant article based on detected violation keywords
text_cols = ['title','summary','faq_answer__c']
for c in text_cols:
    if c in kdf.columns:
        kdf[c] = kdf[c].fillna('').astype(str)

kdf['blob'] = (kdf.get('title','') + ' ' + kdf.get('summary','') + ' ' + kdf.get('faq_answer__c','')).str.lower()

candidates = pd.Series([False]*len(kdf))
if 'discount_gt_10' in violations:
    candidates = candidates | kdf['blob'].str.contains('discount') | kdf['blob'].str.contains('approval')
if 'qty_gt_25' in violations:
    candidates = candidates | kdf['blob'].str.contains('quantity') | kdf['blob'].str.contains('bulk') | kdf['blob'].str.contains('volume')
if 'price_mismatch' in violations:
    candidates = candidates | kdf['blob'].str.contains('pricebook') | kdf['blob'].str.contains('unit price') | kdf['blob'].str.contains('pricing')

cand_df = kdf[candidates].copy()
# If no candidates found, broaden with common compliance terms
if cand_df.empty:
    broad = kdf['blob'].str.contains('quote') & (kdf['blob'].str.contains('pricing') | kdf['blob'].str.contains('discount') | kdf['blob'].str.contains('pricebook'))
    cand_df = kdf[broad].copy()

# pick best match by simple scoring
terms = []
if 'discount_gt_10' in violations:
    terms += ['discount','approval','maximum','percent','%']
if 'qty_gt_25' in violations:
    terms += ['quantity','bulk','volume','limit','maximum']
if 'price_mismatch' in violations:
    terms += ['pricebook','unit price','pricing','catalog']

if terms:
    def score(blob):
        s = 0
        for t in terms:
            s += blob.count(t)
        return s
    cand_df['score'] = cand_df['blob'].map(score)
    cand_df = cand_df.sort_values(['score'], ascending=False)

article_id = None
if not cand_df.empty:
    article_id = cand_df.iloc[0]['id']

print('__RESULT__:')
print(json.dumps({'violations': violations, 'article_id': article_id}))"""

env_args = {'var_call_7Rm2YVxJ9CXg0QrC7G3Ysfki': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_ANXk5GVm5FKccaOUn0leqFqU': [{'PricebookEntryId': '01uWt0000027P3mIAE', 'CatalogUnitPrice': '489.99', 'Product2Id': '01tWt000006hVhpIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'CatalogUnitPrice': '599.99', 'Product2Id': '#01tWt000006hV58IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'CatalogUnitPrice': '399.99', 'Product2Id': '01tWt000006hTUkIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'CatalogUnitPrice': '529.99', 'Product2Id': '01tWt000006hV8LIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PBpIAM', 'CatalogUnitPrice': '449.99', 'Product2Id': '01tWt000006hV9xIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'CatalogUnitPrice': '399.99', 'Product2Id': '01tWt000006hVBZIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PGfIAM', 'CatalogUnitPrice': '479.99', 'Product2Id': '01tWt000006hVEnIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PIHIA2', 'CatalogUnitPrice': '599.99', 'Product2Id': '#01tWt000006hVGPIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'CatalogUnitPrice': '529.99', 'Product2Id': '01tWt000006hVI1IAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PLVIA2', 'CatalogUnitPrice': '459.99', 'Product2Id': '#01tWt000006hVLFIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'CatalogUnitPrice': '399.99', 'Product2Id': '01tWt000006hPfgIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'CatalogUnitPrice': '299.99', 'Product2Id': '01tWt000006hVMrIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027POkIAM', 'CatalogUnitPrice': '349.99', 'Product2Id': '#01tWt000006hRfqIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PRxIAM', 'CatalogUnitPrice': '559.99', 'Product2Id': '#01tWt000006hVOTIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'CatalogUnitPrice': '459.99', 'Product2Id': '01tWt000006hVUvIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'CatalogUnitPrice': '339.99', 'Product2Id': '01tWt000006hVQ5IAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'CatalogUnitPrice': '429.99', 'Product2Id': '01tWt000006hVQ6IAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PYPIA2', 'CatalogUnitPrice': '319.99', 'Product2Id': '#01tWt000006hVRhIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'CatalogUnitPrice': '529.99', 'Product2Id': '01tWt000006hVTJIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'CatalogUnitPrice': '559.99', 'Product2Id': '01tWt000006hVZlIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'CatalogUnitPrice': '349.99', 'Product2Id': '01tWt000006hVbNIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'CatalogUnitPrice': '549.99', 'Product2Id': '01tWt000006hVebIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PmvIAE', 'CatalogUnitPrice': '599.99', 'Product2Id': '01tWt000006hVJeIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PoXIAU', 'CatalogUnitPrice': '459.99', 'Product2Id': '#01tWt000006hVgDIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'CatalogUnitPrice': '429.99', 'Product2Id': '01tWt000006hVjRIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PrlIAE', 'CatalogUnitPrice': '369.99', 'Product2Id': '01tWt000006hVl3IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'CatalogUnitPrice': '399.99', 'Product2Id': '01tWt000006hVmfIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'CatalogUnitPrice': '529.99', 'Product2Id': '01tWt000006hVwLIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027PuzIAE', 'CatalogUnitPrice': '629.99', 'Product2Id': '01tWt000006hVoHIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '#01uWt0000027PyDIAU', 'CatalogUnitPrice': '649.99', 'Product2Id': '01tWt000006hVrVIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'CatalogUnitPrice': '579.99', 'Product2Id': '01tWt000006hVujIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'CatalogUnitPrice': '299.99', 'Product2Id': '01tWt000006hVjSIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'CatalogUnitPrice': '619.99', 'Product2Id': '01tWt000006hUtqIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}], 'var_call_Re2ArPRPcDFxvQBny0eu9WE4': 'file_storage/call_Re2ArPRPcDFxvQBny0eu9WE4.json', 'var_call_OBnM0GltaAoxWkXeeQt3f4t0': []}

exec(code, env_args)
