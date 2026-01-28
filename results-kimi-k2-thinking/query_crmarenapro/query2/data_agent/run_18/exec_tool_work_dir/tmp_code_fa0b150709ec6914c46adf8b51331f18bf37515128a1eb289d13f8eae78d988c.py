code = """import json
import re

# Read the full knowledge articles result from the file
file_path = var_functions.query_db:6
with open(file_path, 'r') as f:
    knowledge_articles = json.load(f)

# Print the titles to see what we have
print("Available knowledge article titles:")
for article in knowledge_articles:
    print(f"- {article['id']}: {article['title']}")

# Search for policy-related keywords in titles and content
policy_keywords = ['policy', 'discount', 'approval', 'threshold', 'pricing', 'cost', 'setup', 'configuration', 'contract', 'terms', 'limit']
policy_articles = []

for article in knowledge_articles:
    title_lower = article['title'].lower()
    summary_lower = article['summary'].lower() if article['summary'] else ''
    
    # Check if any keyword appears
    for keyword in policy_keywords:
        if keyword in title_lower or keyword in summary_lower:
            policy_articles.append(article)
            break

print(f"\nFound {len(policy_articles)} potentially relevant policy articles:")
for article in policy_articles:
    print(f"- {article['id']}: {article['title']}")

# Let's also search for numeric patterns that might indicate discount limits or approval thresholds
numeric_policy_articles = []
for article in knowledge_articles:
    content = (article['title'] or '') + ' ' + (article['summary'] or '') + ' ' + (article['faq_answer__c'] or '')
    # Look for patterns like "X%", "X percent", "$X", "X dollars", numbers
    if re.search(r'\d+%|\d+ percent|\$\d+|\d+\s*dollars|\b\d+\b.*(discount|approval|limit|threshold)', content, re.IGNORECASE):
        numeric_policy_articles.append(article)

print(f"\nFound {len(numeric_policy_articles)} articles with numeric values:")
for article in numeric_policy_articles:
    print(f"- {article['id']}: {article['title']}")

# Check quote details
quote_items = var_functions.query_db:2
discounts = [float(item['Discount']) for item in quote_items]
print(f"\nQuote discounts: {discounts}")

# Prepare result
result = {
    'policy_articles_count': len(policy_articles),
    'numeric_articles_count': len(numeric_policy_articles),
    'discounts_in_quote': discounts
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:5': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [], 'var_functions.query_db:10': [], 'var_functions.query_db:12': [{'Id': '006Wt000007BHHfIAO', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '#003Wt00000JqkgYIAR', 'OwnerId': '#005Wt000003NIybIAG', 'Probability': '75.0', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Name': 'InnovateX Solutions Technology Integration Opportunity', 'Description': 'TechPulse Solutions offers InnovateX Solutions a suite of tools, including AI-powered CircuitSync Pro and environmentally-focused EcoPCB Creator, to enhance their design capabilities. By incorporating DesignWave Automation, InnovateX can streamline workflows, ensuring faster project completion and higher client satisfaction. Integrating PulseSim Pro will optimize circuit design verification with precision and speed.', 'CreatedDate': '2021-05-20T14:15:30.000+0000', 'CloseDate': '2021-07-15'}]}

exec(code, env_args)
