code = """import json, pandas as pd, re

quote = pd.DataFrame(var_call_5Ei7udqMx9IOYzCxzY7dO5kZ)
qli = pd.DataFrame(var_call_ydYbAlqaPVSsFA5GX8CKrIsu)
products = pd.read_json(var_call_sDEdlxPs2xyvMxyGwRNLBeCn)
kn = pd.read_json(var_call_ZRURw4pLqtMoJ7anESgXu4xK)

def norm_series(x):
    return pd.Series(x, dtype='string').astype(str).str.replace('#','', regex=False).str.strip()

quote['Id_norm'] = norm_series(quote['Id'])
qli['QuoteId_norm'] = norm_series(qli['QuoteId'])
qli['Product2Id_norm'] = norm_series(qli['Product2Id'])
products['Id_norm'] = norm_series(products['Id'])
kn['id_norm'] = norm_series(kn['id'])

setup_kw = ['setup','implementation','onboarding','integration','install','deployment']
pattern = '(' + '|'.join(setup_kw) + ')'
products['is_setup'] = (
    products['Name'].astype(str).str.contains(pattern, case=False, na=False) |
    products['Description'].astype(str).str.contains(pattern, case=False, na=False)
)

qli = qli.merge(products[['Id_norm','Name','Description','is_setup']], how='left', left_on='Product2Id_norm', right_on='Id_norm')

for c in ['Discount','UnitPrice','Quantity','TotalPrice']:
    qli[c] = pd.to_numeric(qli[c], errors='coerce')

setup_present = bool((qli['is_setup'] == True).any())
max_discount = qli['Discount'].max(skipna=True)

text = (kn['title'].fillna('') + '\\n' + kn['summary'].fillna('') + '\\n' + kn['faq_answer__c'].fillna('')).str.lower()

cand_mask = (
    text.str.contains('discount') |
    text.str.contains('setup') |
    text.str.contains('implementation') |
    text.str.contains('onboarding') |
    text.str.contains('integration') |
    text.str.contains('professional service') |
    text.str.contains('pricing')
)
kn_cand = kn[cand_mask].copy()

violation_id = None

def extract_threshold(s):
    m = re.search(r'(max(?:imum)?[^\\n]{0,80}discount[^\\n]{0,40}?)(\\d{1,2})\\s*%', s)
    if m:
        return int(m.group(2))
    m = re.search(r'(discount[^\\n]{0,80}max(?:imum)?[^\\n]{0,40}?)(\\d{1,2})\\s*%', s)
    if m:
        return int(m.group(2))
    return None

thresholds = []
for _, row in kn_cand.iterrows():
    s = (str(row.get('title','')) + '\\n' + str(row.get('summary','')) + '\\n' + str(row.get('faq_answer__c',''))).lower()
    th = extract_threshold(s)
    if th is not None:
        thresholds.append((row['id_norm'], th))

if pd.notna(max_discount) and len(thresholds) > 0:
    strict_id, strict_th = sorted(thresholds, key=lambda x: x[1])[0]
    if float(max_discount) > float(strict_th):
        violation_id = strict_id

if violation_id is None:
    qdesc = quote.loc[0,'Description'] if len(quote) > 0 else ''
    if isinstance(qdesc, str) and (('integration' in qdesc.lower()) or ('implementation' in qdesc.lower())) and (not setup_present):
        req_mask = text.str.contains('integration') & (text.str.contains('setup') | text.str.contains('implementation') | text.str.contains('onboarding')) & (text.str.contains('required') | text.str.contains('must'))
        req = kn[req_mask]
        if len(req) > 0:
            violation_id = req.iloc[0]['id_norm']

print('__RESULT__:')
print(json.dumps(violation_id))"""

env_args = {'var_call_5Ei7udqMx9IOYzCxzY7dO5kZ': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_ydYbAlqaPVSsFA5GX8CKrIsu': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_sDEdlxPs2xyvMxyGwRNLBeCn': 'file_storage/call_sDEdlxPs2xyvMxyGwRNLBeCn.json', 'var_call_ZRURw4pLqtMoJ7anESgXu4xK': 'file_storage/call_ZRURw4pLqtMoJ7anESgXu4xK.json'}

exec(code, env_args)
