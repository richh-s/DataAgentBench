code = """import json, pandas as pd, re

quote = pd.DataFrame(var_call_2KqEbtMz8UWMjLWHeY36HHzd)
qli = pd.DataFrame(var_call_4WpzNpCLt2U0FkNFAwAInSnO)

p_path = var_call_v8XdtLw0DPPMNl25tZJXiebV
with open(p_path, 'r', encoding='utf-8') as f:
    products = json.load(f)
prod = pd.DataFrame(products)

k_path = var_call_eznFFbeE3e23GR8VcPoonQuG
with open(k_path, 'r', encoding='utf-8') as f:
    kav = json.load(f)
ka = pd.DataFrame(kav)

qli['Discount'] = pd.to_numeric(qli['Discount'], errors='coerce')
max_disc = float(qli['Discount'].max()) if len(qli) else 0.0

text_cols = ['title','summary','faq_answer__c']
ka['__text'] = ka[text_cols].fillna('').agg(' '.join, axis=1).str.lower()

keywords = ['discount','maximum discount','max discount','pricing policy','quote approval','setup fee','implementation','onboarding','professional services','setup','cost','margin']
mask = ka['__text'].apply(lambda t: any(k in t for k in keywords))
ka_cand = ka[mask].copy()

threshold_rows = []
pattern = re.compile(r'(discount[^\r\n]{0,60}?)(\d{1,2}(?:\.\d+)?)\s*%?')
for _, row in ka_cand.iterrows():
    t = row['__text']
    for m in pattern.finditer(t):
        num = float(m.group(2))
        threshold_rows.append((row['id'], num))

violation_id = None
if threshold_rows:
    thr_df = pd.DataFrame(threshold_rows, columns=['id','num'])
    min_thr = float(thr_df['num'].min())
    if max_disc > min_thr + 1e-9:
        violation_id = thr_df.sort_values(['num']).iloc[0]['id']

print('__RESULT__:')
print(json.dumps({'violation_knowledge_article_id': violation_id}))"""

env_args = {'var_call_2KqEbtMz8UWMjLWHeY36HHzd': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_4WpzNpCLt2U0FkNFAwAInSnO': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_v8XdtLw0DPPMNl25tZJXiebV': 'file_storage/call_v8XdtLw0DPPMNl25tZJXiebV.json', 'var_call_eznFFbeE3e23GR8VcPoonQuG': 'file_storage/call_eznFFbeE3e23GR8VcPoonQuG.json'}

exec(code, env_args)
