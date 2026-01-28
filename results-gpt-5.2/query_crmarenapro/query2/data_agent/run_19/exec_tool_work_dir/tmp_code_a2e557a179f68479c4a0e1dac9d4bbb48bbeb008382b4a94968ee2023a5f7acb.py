code = """import json, pandas as pd

quote = pd.DataFrame(var_call_qpBoLFKisGpOUsxv52JLE4Cu)
qli = pd.DataFrame(var_call_ansQXQIeDidpmbmKdnXzgBpS)

# Load knowledge articles (may be large file)
ka_src = var_call_OBzPgsIxvJGkbF2PoRmyLbhr
if isinstance(ka_src, str) and ka_src.endswith('.json'):
    with open(ka_src, 'r', encoding='utf-8') as f:
        ka = pd.DataFrame(json.load(f))
else:
    ka = pd.DataFrame(ka_src)

# Compute effective discount rates per line if possible
for col in ['Quantity','UnitPrice','Discount','TotalPrice']:
    if col in qli.columns:
        qli[col] = pd.to_numeric(qli[col], errors='coerce')

# infer discount percent if TotalPrice looks like discounted extended price
qli['extended'] = qli['Quantity'] * qli['UnitPrice']
qli['disc_frac_inferred'] = 1 - (qli['TotalPrice'] / qli['extended'])

max_disc = float(qli['Discount'].max()) if 'Discount' in qli.columns and len(qli)>0 else None
max_disc_inf = float(qli['disc_frac_inferred'].max()) if len(qli)>0 else None

# Find policy-like knowledge articles by keyword search
text_cols = []
for c in ['title','summary','faq_answer__c','urlname']:
    if c in ka.columns:
        text_cols.append(c)

def row_text(r):
    parts = []
    for c in text_cols:
        v = r.get(c)
        if pd.notna(v):
            parts.append(str(v))
    return ' '.join(parts).lower()

keywords = ['quote', 'pricing', 'discount', 'approval', 'setup', 'implementation', 'professional services', 'ps', 'cost', 'policy', 'compliance']

candidate_rows = []
for _, r in ka.iterrows():
    t = row_text(r)
    score = sum(1 for k in keywords if k in t)
    if score>0:
        candidate_rows.append((r.get('id'), score, r.get('title')))

# if any candidate exists, try to identify one explicitly about discount thresholds or setup fees
# Use extra scoring for discount/setup related terms
focus_terms = ['discount', 'discounts', 'setup', 'implementation', 'professional services', 'onboarding', 'one-time', 'fee', 'fees', 'approval']
refined = []
for _, r in ka.iterrows():
    t = row_text(r)
    base = sum(1 for k in keywords if k in t)
    if base==0:
        continue
    extra = sum(2 for ft in focus_terms if ft in t)
    refined.append((r.get('id'), base+extra, r.get('title'), t))

refined_sorted = sorted(refined, key=lambda x: x[1], reverse=True)

# Determine violation: assume standard policy maximum discount 10% unless article indicates otherwise.
# Since we must return an article id only if conflict is found, require finding an article that mentions max discount 10% or similar.
violation_id = None
if max_disc is not None and max_disc > 10:
    # look for article with '10%' or '10 percent' and 'discount' and 'quote'
    for aid, sc, title, t in refined_sorted[:200]:
        if 'discount' in t and ('10%' in t or '10 percent' in t or 'ten percent' in t):
            violation_id = aid
            break

# Also check for setup fee policy: if quote description/lines lack setup but question asks cost and setup; we can't assess setup fee without product mapping.

print('__RESULT__:')
print(json.dumps({'violation_id': violation_id, 'max_discount': max_disc, 'max_discount_inferred': max_disc_inf}))"""

env_args = {'var_call_qpBoLFKisGpOUsxv52JLE4Cu': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_ansQXQIeDidpmbmKdnXzgBpS': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_OBzPgsIxvJGkbF2PoRmyLbhr': 'file_storage/call_OBzPgsIxvJGkbF2PoRmyLbhr.json', 'var_call_KqVWCSkU6ZYTnyplyuFdEtNR': []}

exec(code, env_args)
