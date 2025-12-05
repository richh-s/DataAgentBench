code = """import json, pandas as pd

quote_lines = pd.DataFrame(var_call_tJFQdNEnpVVI3PERihtCbkbT)

arts_path = var_call_1xuw9Ee9IvK4z3dybosqa1Z5
with open(arts_path, 'r') as f:
    arts = json.load(f)
arts_df = pd.DataFrame(arts)

viol_id = None

max_disc_art = arts_df[arts_df['title'].str.contains('Volume-Based Discounts', case=False, na=False)].iloc[0]

quote_lines['Discount'] = quote_lines['Discount'].astype(float)
quote_lines['Quantity'] = quote_lines['Quantity'].astype(float)

low_qty_high_disc = quote_lines[(quote_lines['Quantity'] < 10) & (quote_lines['Discount'] > 10)]

if not low_qty_high_disc.empty:
    viol_id = max_disc_art['id']

if isinstance(viol_id, str):
    viol_id_clean = viol_id.replace('#','')
else:
    viol_id_clean = None

result = json.dumps(viol_id_clean)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_Jr5TIWP7u0S1xVP8VQJ9IfgM': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_tqWYCdyY0WL6YfcH3lFdJpH7': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_1xuw9Ee9IvK4z3dybosqa1Z5': 'file_storage/call_1xuw9Ee9IvK4z3dybosqa1Z5.json', 'var_call_tJFQdNEnpVVI3PERihtCbkbT': [{'QuoteId': '0Q0Wt000001WSDVKA4', 'QuoteStatus': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01', 'OpportunityId': '#006Wt000007BHHfIAO', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Probability': '75.0', 'LineTotal': '2279.9525', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'QuoteLineTotal': '2279.9525'}, {'QuoteId': '0Q0Wt000001WSDVKA4', 'QuoteStatus': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01', 'OpportunityId': '#006Wt000007BHHfIAO', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Probability': '75.0', 'LineTotal': '2260.9335', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'QuoteLineTotal': '2260.9335'}, {'QuoteId': '0Q0Wt000001WSDVKA4', 'QuoteStatus': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01', 'OpportunityId': '#006Wt000007BHHfIAO', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Probability': '75.0', 'LineTotal': '4499.91', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'QuoteLineTotal': '4499.91'}, {'QuoteId': '0Q0Wt000001WSDVKA4', 'QuoteStatus': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01', 'OpportunityId': '#006Wt000007BHHfIAO', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Probability': '75.0', 'LineTotal': '2379.932', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'QuoteLineTotal': '2379.932'}]}

exec(code, env_args)
