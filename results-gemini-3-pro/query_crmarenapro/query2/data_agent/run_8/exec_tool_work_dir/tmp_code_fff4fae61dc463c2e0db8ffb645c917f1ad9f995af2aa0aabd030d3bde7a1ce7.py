code = """import json
import pandas as pd

# Load knowledge articles
with open(locals()['var_function-call-15791899697117307092'], 'r') as f:
    articles = json.load(f)

# Filter relevant articles
keywords = ['policy', 'approval', 'discount', 'quote', 'limit', 'compliance', 'threshold']
relevant_articles = []
for art in articles:
    text = (str(art.get('title', '')) + " " + str(art.get('summary', '')) + " " + str(art.get('faq_answer__c', ''))).lower()
    if any(k in text for k in keywords):
        relevant_articles.append(art)

# Load Quote Line Items
qli = locals()['var_function-call-15791899697117309243']
quote_items = pd.DataFrame(qli)
if not quote_items.empty:
    quote_items['TotalPrice'] = pd.to_numeric(quote_items['TotalPrice'])
    quote_items['Discount'] = pd.to_numeric(quote_items['Discount'])
    total_amount = quote_items['TotalPrice'].sum()
    max_discount = quote_items['Discount'].max()
else:
    total_amount = 0
    max_discount = 0

print("__RESULT__:")
print(json.dumps({
    "total_quote_amount": total_amount,
    "max_discount": max_discount,
    "relevant_articles_count": len(relevant_articles),
    "relevant_articles_preview": relevant_articles[:5] # Limit to avoid huge output, I'll iterate if needed
}))"""

env_args = {'var_function-call-15791899697117307298': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_function-call-15791899697117309243': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_function-call-15791899697117307092': 'file_storage/function-call-15791899697117307092.json', 'var_function-call-371342213410534164': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '#01tWt000006hVEnIAM', 'Name': 'DesignWave Automation  '}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro'}]}

exec(code, env_args)
