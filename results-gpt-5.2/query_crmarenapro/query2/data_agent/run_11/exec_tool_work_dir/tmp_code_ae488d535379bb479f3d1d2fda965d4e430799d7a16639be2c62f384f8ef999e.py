code = """import json, pandas as pd, re

quote = pd.DataFrame(var_call_tHIKc7FwdGsnxxiNbLnVlDLK)
qli = pd.DataFrame(var_call_5kvfnLhb9aHZaga0aOfbV9Af)

ka_src = var_call_FX3MbLyiSHz7IZkFT7KYUOP5
if isinstance(ka_src, str) and ka_src.endswith('.json'):
    with open(ka_src, 'r', encoding='utf-8') as f:
        kas = json.load(f)
else:
    kas = ka_src
ka = pd.DataFrame(kas)

for col in ['title','summary','faq_answer__c','urlname','id']:
    if col in ka.columns:
        ka[col] = ka[col].astype(str)

pattern = r"quote\s+approval|approval\s+guide|discount|setup|implementation|pricing|quote\s+policy"
text_cols = [c for c in ['title','summary','faq_answer__c'] if c in ka.columns]
mask = False
for c in text_cols:
    mask = mask | ka[c].str.contains(pattern, regex=True, na=False, case=False)
relevant = ka[mask].copy()

if not qli.empty and 'Discount' in qli.columns:
    qli['Discount'] = pd.to_numeric(qli['Discount'], errors='coerce')
    max_disc = float(qli['Discount'].max()) if qli['Discount'].notna().any() else None
else:
    max_disc = None

violating_article_id = None
if max_disc is not None and max_disc > 10:
    patt2 = r"discount\s*(over|above|greater\s+than|>)\s*10%|>\s*10%\s*discount|discount\s+over\s+10%"
    cand = relevant.copy()
    m2 = False
    for c in text_cols:
        m2 = m2 | cand[c].str.contains(patt2, regex=True, na=False, case=False)
    cand2 = cand[m2]
    if not cand2.empty:
        violating_article_id = cand2.iloc[0]['id']

out = violating_article_id if violating_article_id is not None else None
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_tHIKc7FwdGsnxxiNbLnVlDLK': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_5kvfnLhb9aHZaga0aOfbV9Af': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_FX3MbLyiSHz7IZkFT7KYUOP5': 'file_storage/call_FX3MbLyiSHz7IZkFT7KYUOP5.json', 'var_call_YvZAN56koq97ObEUNR6HKgkR': [{'Id': '006Wt000007BHHfIAO', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Probability': '75.0', 'Name': 'InnovateX Solutions Technology Integration Opportunity', 'Description': 'TechPulse Solutions offers InnovateX Solutions a suite of tools, including AI-powered CircuitSync Pro and environmentally-focused EcoPCB Creator, to enhance their design capabilities. By incorporating DesignWave Automation, InnovateX can streamline workflows, ensuring faster project completion and higher client satisfaction. Integrating PulseSim Pro will optimize circuit design verification with precision and speed.', 'CreatedDate': '2021-05-20T14:15:30.000+0000', 'CloseDate': '2021-07-15', 'OwnerId': '#005Wt000003NIybIAG'}]}

exec(code, env_args)
