code = """import json, pandas as pd

qlis = pd.DataFrame(var_call_DQhWjXdhmb4GisIKfXoT5Tde)

# load pricebook entries full
pbe_src = var_call_uEHWcF0MVrBBZRmlyKg32rtW
if isinstance(pbe_src, str) and pbe_src.endswith('.json'):
    with open(pbe_src, 'r') as f:
        pbe = pd.DataFrame(json.load(f))
else:
    pbe = pd.DataFrame(pbe_src)

# normalize ids for join
for df, col in [(qlis,'PricebookEntryId'), (pbe,'PricebookEntryId')]:
    df[col+'_norm'] = df[col].astype(str).str.replace('#','', regex=False).str.strip()

# ensure numeric
for c in ['Quantity','UnitPrice','Discount','TotalPrice']:
    qlis[c] = pd.to_numeric(qlis[c], errors='coerce')

pbe['CatalogUnitPrice'] = pd.to_numeric(pbe['CatalogUnitPrice'], errors='coerce')

m = qlis.merge(pbe, left_on='PricebookEntryId_norm', right_on='PricebookEntryId_norm', how='left', suffixes=('','_pbe'))

# find price mismatches vs catalog, or inactive product/pricebook if available
m['price_mismatch'] = (m['CatalogUnitPrice'].notna()) & (m['UnitPrice'].round(2) != m['CatalogUnitPrice'].round(2))

# discount field seems percent; compute expected total
m['expected_total'] = (m['UnitPrice'] * m['Quantity'] * (1 - (m['Discount'].fillna(0)/100.0)))
m['total_mismatch'] = (m['TotalPrice'].notna()) & (m['expected_total'].notna()) & ((m['TotalPrice'] - m['expected_total']).abs() > 0.01)

# quantity invalid: non-integer or <=0
m['qty_invalid'] = (m['Quantity'].isna()) | (m['Quantity'] <= 0) | ((m['Quantity'] % 1)!=0)

violations = m[(m['price_mismatch']) | (m['total_mismatch']) | (m['qty_invalid'])]

# Determine type of violation present
violation_types = []
if violations['price_mismatch'].any():
    violation_types.append('unit price differs from pricebook')
if violations['total_mismatch'].any():
    violation_types.append('total price inconsistent with qty/unit/discount')
if violations['qty_invalid'].any():
    violation_types.append('invalid quantity')

# Load knowledge articles and select best match by keyword scoring
ka_src = var_call_VehEFXuSyhi701467659fUyS
if isinstance(ka_src, str) and ka_src.endswith('.json'):
    with open(ka_src,'r') as f:
        kas = json.load(f)
else:
    kas = ka_src

query_terms = ['quote','quotation','quote line','quantity','unit price','pricebook','pricing','discount','total price']
# emphasize the likely issue
if 'unit price differs from pricebook' in violation_types:
    query_terms += ['pricebook entry','must match','catalog price']
if 'invalid quantity' in violation_types:
    query_terms += ['minimum','must be whole','integer','positive']

best = None
best_score = -1
for a in kas:
    text = ' '.join([str(a.get('title','')), str(a.get('summary','')), str(a.get('faq_answer__c',''))]).lower()
    score = sum(1 for t in query_terms if t in text)
    if score > best_score:
        best_score = score
        best = a

out = {'violation_types': violation_types, 'best_article_id': (best or {}).get('id'), 'best_score': best_score}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_DQhWjXdhmb4GisIKfXoT5Tde': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_uEHWcF0MVrBBZRmlyKg32rtW': 'file_storage/call_uEHWcF0MVrBBZRmlyKg32rtW.json', 'var_call_VehEFXuSyhi701467659fUyS': 'file_storage/call_VehEFXuSyhi701467659fUyS.json'}

exec(code, env_args)
