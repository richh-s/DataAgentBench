code = """import json

# Load knowledge articles (File path)
with open(locals()['var_function-call-16658710354531695047'], 'r') as f:
    articles = json.load(f)

# Load quote and items (Direct list objects)
quote_list = locals()['var_function-call-16658710354531695693']
quote = quote_list[0]
items = locals()['var_function-call-16658710354531695370']

# 1. Calculate Quote Metrics
total_amount = 0
max_discount = 0

for item in items:
    # Ensure values are floats
    total_price = float(item['TotalPrice']) if item['TotalPrice'] else 0.0
    discount = float(item['Discount']) if item['Discount'] else 0.0
    
    total_amount += total_price
    if discount > max_discount:
        max_discount = discount

metrics = {
    "total_amount": total_amount,
    "max_discount": max_discount
}

# 2. Find relevant policy articles
# Looking for "Approval" "Policy" "Discount" related articles
policy_articles = []
for art in articles:
    title = art.get('title', '') or ''
    body = art.get('faq_answer__c', '') or ''
    summary = art.get('summary', '') or ''
    
    text = (title + " " + body + " " + summary).lower()
    
    # Filter for relevant keywords
    if ('policy' in text or 'guideline' in text or 'standard' in text) and \
       ('approval' in text or 'discount' in text or 'margin' in text):
        policy_articles.append({
            "Id": art['id'],
            "Title": art['title'],
            "Body": art['faq_answer__c']
        })

print("__RESULT__:")
print(json.dumps({"metrics": metrics, "policy_articles": policy_articles}, indent=2))"""

env_args = {'var_function-call-16658710354531695693': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_function-call-16658710354531695370': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_function-call-16658710354531695047': 'file_storage/function-call-16658710354531695047.json'}

exec(code, env_args)
