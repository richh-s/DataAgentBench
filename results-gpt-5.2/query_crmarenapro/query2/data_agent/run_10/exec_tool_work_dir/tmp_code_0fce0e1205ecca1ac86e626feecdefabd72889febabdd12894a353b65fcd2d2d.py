code = """import json, pandas as pd
from pathlib import Path

# Load knowledge articles
k = var_call_WRYgtPpVm2AMxlKnwDYxQXjU
if isinstance(k, str) and Path(k).exists():
    articles = json.loads(Path(k).read_text())
else:
    articles = k

df = pd.DataFrame(articles)
# Find quote approval / pricing/discount/setup policy article
pattern = r"quote|approval|discount|pricing|setup|implementation|professional services|ps|cost"
mask = df['title'].fillna('').str.contains(pattern, case=False, regex=True) | \
       df['summary'].fillna('').str.contains(pattern, case=False, regex=True) | \
       df['faq_answer__c'].fillna('').str.contains(pattern, case=False, regex=True)
subset = df.loc[mask, ['id','title','summary']].copy()
# Return candidate ids (top 20)
out = subset.head(20).to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_vhXJ943mzgsgRor9kJAK1bZA': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_gYkaPNLZDYvoX3YgyQEMwqSe': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_WRYgtPpVm2AMxlKnwDYxQXjU': 'file_storage/call_WRYgtPpVm2AMxlKnwDYxQXjU.json'}

exec(code, env_args)
