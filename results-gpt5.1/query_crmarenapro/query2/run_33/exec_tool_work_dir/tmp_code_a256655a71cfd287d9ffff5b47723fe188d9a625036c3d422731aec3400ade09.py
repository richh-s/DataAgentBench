code = """import json, pandas as pd, os, textwrap

path = var_call_mF8c1caKSRxLw4pNzvOnFKat
with open(path, 'r') as f:
    articles = json.load(f)

df = pd.DataFrame(articles)
text_cols = ['title','faq_answer__c','summary']
mask = pd.Series([False]*len(df))
for col in text_cols:
    col_mask = df[col].fillna('').str.contains('quote approval|discount|maximum discount|pricing policy|implementation cost|setup fee|one-time setup|Needs Review|approval threshold|deal desk', case=False, regex=True)
    mask |= col_mask

candidates = df[mask]

result_id = None
if not candidates.empty:
    result_id = candidates.iloc[0]['id'].strip()

out = json.dumps(result_id)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_jnCsA1fAXKNi1ABg2euWV61U': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_C4arjvIydB7cwxJJ85D9nQok': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_T70jS7bCofmyna7tekXAPru0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_mF8c1caKSRxLw4pNzvOnFKat': 'file_storage/call_mF8c1caKSRxLw4pNzvOnFKat.json'}

exec(code, env_args)
