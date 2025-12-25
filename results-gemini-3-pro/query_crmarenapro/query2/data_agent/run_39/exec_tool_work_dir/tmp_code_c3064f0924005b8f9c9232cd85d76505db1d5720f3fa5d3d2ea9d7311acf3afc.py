code = """import json
import pandas as pd

# Load knowledge articles
with open(var_function_call_16658710354531695047, 'r') as f:
    articles = json.load(f)

# Load quote and items
quote = json.loads(var_function_call_16658710354531695693)[0]
items = json.loads(var_function_call_16658710354531695370)

# 1. Calculate Quote Metrics
total_amount = 0
max_discount = 0
items_with_high_discount = []

for item in items:
    total_amount += float(item['TotalPrice'])
    discount = float(item['Discount'])
    if discount > max_discount:
        max_discount = discount
    if discount > 20: # Just a guess, will refine after reading policies
        items_with_high_discount.append(item)

print(f"Total Amount: {total_amount}")
print(f"Max Discount: {max_discount}")

# 2. Find relevant policy articles
policy_articles = []
for art in articles:
    text = (art['title'] + " " + art['faq_answer__c'] + " " + art['summary']).lower()
    if 'policy' in text or 'approval' in text or 'discount' in text or 'quote' in text:
        policy_articles.append(art)

# Print potential policy articles to identify the correct one
print("__RESULT__:")
print(json.dumps(policy_articles, indent=2))"""

env_args = {'var_function-call-16658710354531695693': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_function-call-16658710354531695370': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_function-call-16658710354531695047': 'file_storage/function-call-16658710354531695047.json'}

exec(code, env_args)
