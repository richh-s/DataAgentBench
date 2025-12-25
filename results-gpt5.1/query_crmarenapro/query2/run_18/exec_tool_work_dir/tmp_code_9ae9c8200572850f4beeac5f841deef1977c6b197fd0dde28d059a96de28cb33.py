code = """import json
import pandas as pd

qli = pd.DataFrame(var_call_UQQXOCH2vw6oh79gnbJuhWVJ)
articles_path = var_call_Ordfkl88qKBtsSqHHURHQ8vC

with open(articles_path, 'r') as f:
    articles = json.load(f)

articles_df = pd.DataFrame(articles)

qli['Quantity'] = qli['Quantity'].astype(float)
qli['UnitPrice'] = qli['UnitPrice'].astype(float)
qli['Discount'] = qli['Discount'].astype(float)
qli['TotalPrice'] = qli['TotalPrice'].astype(float)

qli['calc_total'] = qli['Quantity'] * qli['UnitPrice'] * (1 - qli['Discount'] / 100)

qli['matches'] = (abs(qli['calc_total'] - qli['TotalPrice']) < 0.01)

violated_article_id = None

if not qli['matches'].all():
    mask = articles_df['title'].str.contains('Volume-Based Discounts', case=False, na=False)
    if mask.any():
        violated_article_id = articles_df[mask].iloc[0]['id']

result = violated_article_id

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_eP051dFnjG124VipWc0luAD7': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_UQQXOCH2vw6oh79gnbJuhWVJ': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_Ordfkl88qKBtsSqHHURHQ8vC': 'file_storage/call_Ordfkl88qKBtsSqHHURHQ8vC.json'}

exec(code, env_args)
