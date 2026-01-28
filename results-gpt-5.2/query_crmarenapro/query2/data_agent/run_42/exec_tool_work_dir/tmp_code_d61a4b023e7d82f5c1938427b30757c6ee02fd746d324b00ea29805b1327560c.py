code = """import json, pandas as pd

quote = pd.DataFrame(var_call_5Ei7udqMx9IOYzCxzY7dO5kZ)
qli = pd.DataFrame(var_call_ydYbAlqaPVSsFA5GX8CKrIsu)

# load large files
import pathlib
prod_path = var_call_sDEdlxPs2xyvMxyGwRNLBeCn
kn_path = var_call_ZRURw4pLqtMoJ7anESgXu4xK
products = pd.read_json(prod_path)
kn = pd.read_json(kn_path)

# normalize ids
for df, col in [(quote,'Id'),(qli,'Product2Id'),(qli,'QuoteId'),(products,'Id'),(kn,'id')]:
    if col in df.columns:
        df[col+'_norm'] = df[col].astype(str).str.replace('#','', regex=False).str.strip()

# identify setup-related products by name/description keywords
setup_kw = ['setup','implementation','onboarding','integration','install','deployment']
pattern = '|'.join(setup_kw)
products['is_setup'] = products['Name'].astype(str).str.contains(pattern, case=False, na=False) | products['Description'].astype(str).str.contains(pattern, case=False, na=False)

qli = qli.merge(products[['Id_norm','Name','Description','is_setup']], how='left', left_on='Product2Id_norm', right_on='Id_norm')

# compute discounts numeric
for c in ['Discount','UnitPrice','Quantity','TotalPrice']:
    qli[c] = pd.to_numeric(qli[c], errors='coerce')

setup_lines = qli[qli['is_setup']==True]
max_discount = qli['Discount'].max(skipna=True)
setup_present = len(setup_lines)>0

# search knowledge for policy on discounts or setup fees
text = (kn['title'].fillna('')+'\n'+kn['summary'].fillna('')+'\n'+kn['faq_answer__c'].fillna('')).str.lower()
# find candidate articles mentioning quote/discount/setup
cand_mask = text.str.contains('discount') | text.str.contains('setup') | text.str.contains('implementation') | text.str.contains('onboarding') | text.str.contains('integration') | text.str.contains('professional service') | text.str.contains('ps ') | text.str.contains('pricing')
kn_cand = kn[cand_mask].copy()

violation_id = None

# Heuristic checks if any policy states max discount threshold or setup fee requirement.
# Look for max discount percent patterns like '10%' '15%' and 'must' etc.
import re

def extract_threshold(s):
    # return minimum found percent near words 'max' or 'maximum' and 'discount'
    m = re.search(r'(max(?:imum)?[^\n]{0,80}discount[^\n]{0,40}?)(\d{1,2})\s*%', s)
    if m:
        return int(m.group(2))
    m = re.search(r'(discount[^\n]{0,80}max(?:imum)?[^\n]{0,40}?)(\d{1,2})\s*%', s)
    if m:
        return int(m.group(2))
    return None

thresholds = []
for _, row in kn_cand.iterrows():
    s = (str(row.get('title',''))+'\n'+str(row.get('summary',''))+'\n'+str(row.get('faq_answer__c',''))).lower()
    th = extract_threshold(s)
    if th is not None:
        thresholds.append((row['id_norm'], th, s))

# determine violation based on any extracted max discount rule
if pd.notna(max_discount) and thresholds:
    # choose strictest (lowest) threshold
    strict_id, strict_th, _ = sorted(thresholds, key=lambda x: x[1])[0]
    if max_discount > strict_th:
        violation_id = strict_id

# setup compliance: look for rule requiring setup line item when integration mentioned
if violation_id is None:
    # if quote description mentions integration and no setup item, find article with such requirement
    qdesc = quote.loc[0,'Description'] if len(quote)>0 else ''
    if isinstance(qdesc,str) and ('integration' in qdesc.lower() or 'implementation' in qdesc.lower()) and not setup_present:
        # find article mentioning setup required for integration
        req_mask = text.str.contains('integration') & (text.str.contains('setup') | text.str.contains('implementation') | text.str.contains('onboarding')) & (text.str.contains('required') | text.str.contains('must'))
        req = kn[req_mask]
        if len(req)>0:
            violation_id = req.iloc[0]['id_norm']

out = json.dumps(violation_id)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_5Ei7udqMx9IOYzCxzY7dO5kZ': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_ydYbAlqaPVSsFA5GX8CKrIsu': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_sDEdlxPs2xyvMxyGwRNLBeCn': 'file_storage/call_sDEdlxPs2xyvMxyGwRNLBeCn.json', 'var_call_ZRURw4pLqtMoJ7anESgXu4xK': 'file_storage/call_ZRURw4pLqtMoJ7anESgXu4xK.json'}

exec(code, env_args)
