code = """import json, pandas as pd
from pathlib import Path

quote = var_call_zYhvqvx6BNqnBwrFQm6qi37M
qli = var_call_fBhyIkCBEoRAbgQumk20EvaD

# load knowledge articles (may be large)
ka_src = var_call_PXMUPIZ0r0q4AlXM3397k7Y4
if isinstance(ka_src, str) and Path(ka_src).exists():
    kas = json.loads(Path(ka_src).read_text())
else:
    kas = ka_src

text = ''
if quote:
    q=quote[0]
    text += ' '.join([str(q.get(k,'')) for k in ['Name','Description','Status']])+' '
# add inferred pricing/setup signals
try:
    df = pd.DataFrame(qli)
    for col in ['UnitPrice','Discount','TotalPrice','Quantity']:
        if col in df.columns:
            df[col]=pd.to_numeric(df[col], errors='coerce')
    total = float(df['TotalPrice'].sum()) if 'TotalPrice' in df.columns else None
    max_disc = float(df['Discount'].max()) if 'Discount' in df.columns else None
    text += f"totalprice {total} maxdiscount {max_disc} "
except Exception:
    pass

# find likely policy/approval articles by keyword
kw = ['quote','approval','discount','pricing','setup','implementation','professional services','onboarding','installation','cost']

candidates=[]
for a in kas:
    blob = ' '.join([str(a.get('title','')), str(a.get('summary','')), str(a.get('faq_answer__c',''))]).lower()
    score = sum(blob.count(k) for k in kw)
    if score>0:
        candidates.append((score, a.get('id')))

candidates = sorted(candidates, reverse=True)[:50]
result = {'top_candidate_ids':[cid for _,cid in candidates[:10]], 'found_candidates':len(candidates)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_zYhvqvx6BNqnBwrFQm6qi37M': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_fBhyIkCBEoRAbgQumk20EvaD': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_PXMUPIZ0r0q4AlXM3397k7Y4': 'file_storage/call_PXMUPIZ0r0q4AlXM3397k7Y4.json'}

exec(code, env_args)
