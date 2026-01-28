code = """import json, pandas as pd, re
ql = pd.DataFrame(var_call_BW09FK8GxUOB8GLL4SaYRt5h)
pbe = pd.DataFrame(var_call_y1TDDmhv9SNfAccB4JNPpx7f)

# normalize ids by stripping leading # and whitespace
for df,col in [(ql,'Product2Id'),(ql,'PricebookEntryId'),(pbe,'PricebookEntryId'),(pbe,'Product2Id')]:
    df[col]=df[col].astype(str).str.strip().str.lstrip('#')

# numeric
for c in ['Quantity','UnitPrice','Discount','TotalPrice']:
    ql[c]=pd.to_numeric(ql[c], errors='coerce')
pbe['CatalogUnitPrice']=pd.to_numeric(pbe['CatalogUnitPrice'], errors='coerce')

# join to catalog
m = ql.merge(pbe, on='PricebookEntryId', how='left', suffixes=('','_cat'))

# invalid checks: unit price mismatch vs catalog, non-integer quantity, discount out of range
m['price_mismatch'] = (m['CatalogUnitPrice'].notna()) & (abs(m['UnitPrice']-m['CatalogUnitPrice'])>1e-6)
m['non_integer_qty'] = m['Quantity'].notna() & (m['Quantity']%1!=0)
m['discount_invalid'] = m['Discount'].notna() & ((m['Discount']<0) | (m['Discount']>100))

invalid = m[m['price_mismatch'] | m['non_integer_qty'] | m['discount_invalid']]

# load knowledge articles
import pathlib
path = var_call_NDBujmshuOnWA2zrwaL77Z8g
records = json.loads(pathlib.Path(path).read_text())
ka = pd.DataFrame(records)

# find best matching article for discount policy
text = (ka['title'].fillna('') + ' ' + ka['summary'].fillna('') + ' ' + ka['faq_answer__c'].fillna('')).str.lower()

def score(row):
    s=0
    if 'discount' in row: s+=2
    if 'maximum' in row or 'max' in row or 'cap' in row: s+=1
    if '15' in row or '15%' in row: s+=1
    if 'quantity' in row: s+=1
    if 'unit price' in row or 'price' in row: s+=1
    if 'quote' in row or 'quotation' in row: s+=1
    if 'policy' in row or 'regulation' in row or 'compliance' in row: s+=1
    return s

ka['__score__']=text.apply(score)
ka_sorted=ka.sort_values(['__score__','id'], ascending=[False,True])

# If invalid due to discount, look for discount policy article; else price policy article
reason = None
if not invalid.empty:
    if invalid['discount_invalid'].any() or (m['Discount']>0).any():
        reason='discount'
    elif invalid['price_mismatch'].any():
        reason='price'
    elif invalid['non_integer_qty'].any():
        reason='quantity'

# try more targeted search keywords
keywords = {'discount':['discount','%','maximum discount','approval'],
            'price':['unit price','price override','pricebook','catalog'],
            'quantity':['quantity','minimum order','bulk','multiple']}

best = None
if reason:
    kw=keywords[reason]
    mask = text
    # simple contain count
    ka['__kw__']=0
    for k in kw:
        ka['__kw__'] += mask.str.contains(re.escape(k)).astype(int)
    best = ka.sort_values(['__kw__','__score__','id'], ascending=[False,False,True]).head(1)
else:
    best = ka_sorted.head(1)

article_id = None
if best is not None and not best.empty and (best.iloc[0].get('__kw__',0)>0 or best.iloc[0]['__score__']>0):
    article_id = best.iloc[0]['id']

print('__RESULT__:')
print(json.dumps({'invalid_line_items': int(len(invalid)), 'reason': reason, 'article_id': article_id}))"""

env_args = {'var_call_BW09FK8GxUOB8GLL4SaYRt5h': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_NDBujmshuOnWA2zrwaL77Z8g': 'file_storage/call_NDBujmshuOnWA2zrwaL77Z8g.json', 'var_call_y1TDDmhv9SNfAccB4JNPpx7f': [{'PricebookEntryId': '01uWt0000027P3lIAE', 'CatalogUnitPrice': '499.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE'}, {'PricebookEntryId': '01uWt0000027P3mIAE', 'CatalogUnitPrice': '489.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVhpIAE'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'CatalogUnitPrice': '599.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hV58IAE'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'CatalogUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hTUkIAM'}, {'PricebookEntryId': '#01uWt0000027P8bIAE', 'CatalogUnitPrice': '349.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV6jIAE'}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'CatalogUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'PricebookEntryId': '01uWt0000027PADIA2', 'CatalogUnitPrice': '299.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE'}, {'PricebookEntryId': '01uWt0000027PBpIAM', 'CatalogUnitPrice': '449.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV9xIAE'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'CatalogUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVBZIA2'}, {'PricebookEntryId': '01uWt0000027PF3IAM', 'CatalogUnitPrice': '549.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVDBIA2'}, {'PricebookEntryId': '#01uWt0000027PGfIAM', 'CatalogUnitPrice': '479.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVEnIAM'}, {'PricebookEntryId': '01uWt0000027PIHIA2', 'CatalogUnitPrice': '599.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVGPIA2'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'CatalogUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVI1IAM'}, {'PricebookEntryId': '01uWt0000027PIJIA2', 'CatalogUnitPrice': '459.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVptIAE'}, {'PricebookEntryId': '01uWt0000027PJtIAM', 'CatalogUnitPrice': '649.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'PricebookEntryId': '01uWt0000027PLVIA2', 'CatalogUnitPrice': '459.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVLFIA2'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'CatalogUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPfgIAE'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'CatalogUnitPrice': '299.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVMrIAM'}, {'PricebookEntryId': '01uWt0000027POkIAM', 'CatalogUnitPrice': '349.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hRfqIAE'}, {'PricebookEntryId': '01uWt0000027PQLIA2', 'CatalogUnitPrice': '489.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hUKMIA2'}, {'PricebookEntryId': '#01uWt0000027PRxIAM', 'CatalogUnitPrice': '559.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVOTIA2'}, {'PricebookEntryId': '01uWt0000027PTZIA2', 'CatalogUnitPrice': '449.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV0IIAU'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'CatalogUnitPrice': '459.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVUvIAM'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'CatalogUnitPrice': '339.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'CatalogUnitPrice': '429.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ6IAM'}, {'PricebookEntryId': '01uWt0000027PYPIA2', 'CatalogUnitPrice': '319.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVRhIAM'}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'CatalogUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVTJIA2'}, {'PricebookEntryId': '01uWt0000027PbdIAE', 'CatalogUnitPrice': '389.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVWXIA2'}, {'PricebookEntryId': '01uWt0000027PdFIAU', 'CatalogUnitPrice': '299.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVY9IAM'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'CatalogUnitPrice': '559.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVZlIAM'}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'CatalogUnitPrice': '349.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVbNIAU'}, {'PricebookEntryId': '01uWt0000027PgUIAU', 'CatalogUnitPrice': '379.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVt7IAE'}, {'PricebookEntryId': '01uWt0000027Pi5IAE', 'CatalogUnitPrice': '399.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'CatalogUnitPrice': '549.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVebIAE'}, {'PricebookEntryId': '01uWt0000027PlJIAU', 'CatalogUnitPrice': '499.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUsEIAU'}, {'PricebookEntryId': '#01uWt0000027PmvIAE', 'CatalogUnitPrice': '599.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVJeIAM'}, {'PricebookEntryId': '01uWt0000027PoXIAU', 'CatalogUnitPrice': '459.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVgDIAU'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'CatalogUnitPrice': '429.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjRIAU'}, {'PricebookEntryId': '01uWt0000027PrlIAE', 'CatalogUnitPrice': '369.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVl3IAE'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'CatalogUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVmfIAE'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'CatalogUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVwLIAU'}, {'PricebookEntryId': '01uWt0000027PuzIAE', 'CatalogUnitPrice': '629.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVoHIAU'}, {'PricebookEntryId': '01uWt0000027PwbIAE', 'CatalogUnitPrice': '559.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUUwIAM'}, {'PricebookEntryId': '#01uWt0000027PyDIAU', 'CatalogUnitPrice': '649.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVrVIAU'}, {'PricebookEntryId': '#01uWt0000027PzpIAE', 'CatalogUnitPrice': '429.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVrWIAU'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'CatalogUnitPrice': '579.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVujIAE'}, {'PricebookEntryId': '#01uWt0000027Q33IAE', 'CatalogUnitPrice': '499.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hOd8IAE'}, {'PricebookEntryId': '#01uWt0000027Q34IAE', 'CatalogUnitPrice': '599.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUgwIAE'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'CatalogUnitPrice': '299.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjSIAU'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'CatalogUnitPrice': '619.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUtqIAE'}], 'var_call_8lMZIhsA2YaYo0F7wVrWg3DR': []}

exec(code, env_args)
