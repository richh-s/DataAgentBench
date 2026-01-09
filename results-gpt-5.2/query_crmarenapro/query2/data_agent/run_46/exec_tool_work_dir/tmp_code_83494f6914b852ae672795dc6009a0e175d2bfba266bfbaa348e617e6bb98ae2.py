code = """import json, pandas as pd
from pathlib import Path

quote = pd.DataFrame(var_call_c3VyQVcAbyhqzJqUcGLYYYAF)
qli = pd.DataFrame(var_call_NukDwwDwmszngfRoHxiyBZyD)

# load full knowledge articles
p = Path(var_call_rkjGUID8XECPAr8euiOXhswk)
articles = json.loads(p.read_text())
art_df = pd.DataFrame(articles)

# simple keyword search for quote approval policy around discount/setup/cost
text_cols = ['title','summary','faq_answer__c']
art_df['blob'] = art_df[text_cols].fillna('').agg(' '.join, axis=1).str.lower()
keywords = ['quote approval','approval','discount','discounts','setup fee','setup','implementation','professional services','ps','pricing','cost','margin','waiver','exception']
mask = art_df['blob'].apply(lambda s: any(k in s for k in keywords))
relevant = art_df[mask].copy()

# Determine if quote has discounts beyond a typical threshold by inferring max discount
qli['Discount'] = pd.to_numeric(qli['Discount'])
max_disc = float(qli['Discount'].max()) if not qli.empty else 0.0

# Heuristic: if any relevant article mentions a numeric discount cap and our max exceeds it, flag violation.
# Extract possible caps like '10%' '15%' '20%' etc.
import re
caps = []
for _, r in relevant.iterrows():
    nums = re.findall(r'(?:up to|max(?:imum)?|cap(?:ped)? at)\s*(\d{1,2})\s*%|\b(\d{1,2})\s*%\s*(?:discount cap|cap|maximum)', r['blob'])
    for a,b in nums:
        n = int(a or b)
        if 0 < n <= 90:
            caps.append((r['id'], n))

# choose smallest cap as strictest
violated_id = None
if caps:
    strict_id, strict_cap = sorted(caps, key=lambda x: x[1])[0]
    if max_disc > strict_cap:
        violated_id = strict_id

# If no caps found, attempt direct match for known policy title
if violated_id is None:
    # look for titles containing 'quote approval guide' or 'discount policy'
    tmask = art_df['title'].fillna('').str.lower().str.contains('quote') & art_df['title'].fillna('').str.lower().str.contains('approval')
    if tmask.any() and max_disc>0:
        violated_id = art_df[tmask].iloc[0]['id']

print('__RESULT__:')
print(json.dumps({'violated_id': violated_id}))"""

env_args = {'var_call_c3VyQVcAbyhqzJqUcGLYYYAF': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_NukDwwDwmszngfRoHxiyBZyD': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_rkjGUID8XECPAr8euiOXhswk': 'file_storage/call_rkjGUID8XECPAr8euiOXhswk.json'}

exec(code, env_args)
