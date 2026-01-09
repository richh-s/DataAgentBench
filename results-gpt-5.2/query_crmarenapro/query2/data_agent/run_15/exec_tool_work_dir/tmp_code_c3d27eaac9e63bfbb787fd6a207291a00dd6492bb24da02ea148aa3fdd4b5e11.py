code = """import json, pandas as pd

quote = pd.DataFrame(var_call_NCi45jRkjDbB4vUl4iyEPfsB)
qli = pd.DataFrame(var_call_j5vL2hWfCFZACW5a72U2VcqH)

# load knowledge
path_or_list = var_call_b9CnhMHJjmgZ5eceZffUmKyy
if isinstance(path_or_list, str):
    with open(path_or_list, 'r', encoding='utf-8') as f:
        kav = json.load(f)
else:
    kav = path_or_list
kdf = pd.DataFrame(kav)

# Heuristic: look for policy articles related to quote approval, discount thresholds, setup fees.
text_cols = ['title','summary','faq_answer__c','urlname']
for c in text_cols:
    if c not in kdf.columns:
        kdf[c] = ''

def norm(s):
    if s is None:
        return ''
    return str(s).strip().lower()

kdf['_blob'] = kdf[text_cols].fillna('').agg(' '.join, axis=1).map(norm)

keywords = [
    'quote approval','discount','discounts','maximum discount','approval required',
    'setup fee','setup','implementation','services','professional services','onboarding',
    'pricing policy','price book','pricebook','unit price','cost','margin'
]
mask = False
for kw in keywords:
    mask = mask | kdf['_blob'].str.contains(kw)

candidates = kdf[mask].copy()

# Determine if quote has high discounts
qli['Discount'] = pd.to_numeric(qli['Discount'], errors='coerce')
max_disc = float(qli['Discount'].max()) if len(qli) else 0.0

# If max discount >= 15%, likely violation depending on policy; pick most relevant article mentioning discount approval thresholds.
# Score candidates by presence of 'discount' and 'approval' and numbers like '10%' '15%'
import re

def score(blob):
    s=0
    if 'discount' in blob: s+=3
    if 'approval' in blob: s+=2
    if 'quote' in blob: s+=2
    if 'setup' in blob or 'implementation' in blob: s+=1
    # numeric thresholds
    if re.search(r'\b15%\b|\b15 percent\b', blob): s+=3
    if re.search(r'\b10%\b|\b10 percent\b', blob): s+=2
    if re.search(r'\b20%\b|\b20 percent\b', blob): s+=2
    return s

candidates['score'] = candidates['_blob'].map(score)

violation_id = None
if max_disc >= 15:
    # choose top scored candidate; if none, None
    if len(candidates):
        top = candidates.sort_values(['score'], ascending=False).head(1)
        violation_id = top['id'].iloc[0]

out = json.dumps({'violation_id': violation_id})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_NCi45jRkjDbB4vUl4iyEPfsB': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_j5vL2hWfCFZACW5a72U2VcqH': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_b9CnhMHJjmgZ5eceZffUmKyy': 'file_storage/call_b9CnhMHJjmgZ5eceZffUmKyy.json'}

exec(code, env_args)
