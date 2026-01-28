code = """import json
import re

# Read the full knowledge articles result from the file using locals()
file_path = locals()['var_functions.query_db:6']
with open(file_path, 'r') as f:
    knowledge_articles = json.load(f)

# Search for policy-related keywords in titles and content
policy_keywords = ['policy', 'discount', 'approval', 'threshold', 'pricing', 'cost', 'setup', 'configuration', 'contract', 'terms', 'limit', 'maximum', 'minimum']
policy_articles = []

for article in knowledge_articles:
    title_lower = article['title'].lower() if article['title'] else ''
    summary_lower = article['summary'].lower() if article['summary'] else ''
    faq_lower = article['faq_answer__c'].lower() if article['faq_answer__c'] else ''
    
    # Check if any keyword appears
    for keyword in policy_keywords:
        if keyword in title_lower or keyword in summary_lower or keyword in faq_lower:
            policy_articles.append(article)
            break

# Check quote details - use locals() to access the variable
quote_items = locals()['var_functions.query_db:2']
discounts = [float(item['Discount']) for item in quote_items]
max_discount = max(discounts)

violation_article_id = None

# Search for discount limits in policy articles
for article in policy_articles:
    title = article['title'] or ''
    summary = article['summary'] or ''
    faq = article['faq_answer__c'] or ''
    content = title + ' ' + summary + ' ' + faq
    
    # Look for discount percentage patterns
    discount_matches = re.findall(r'(\d+)%|\b(\d+)\s+percent|\b(\d+)\s+percent', content, re.IGNORECASE)
    
    for match in discount_matches:
        # Extract the percentage value
        percent_value = None
        for group in match:
            if group:
                percent_value = int(group)
                break
        
        if percent_value is not None:
            # Check if this might be a discount limit (threshold/maximum)
            if 'discount' in content.lower() or 'maximum' in content.lower() or 'limit' in content.lower() or 'threshold' in content.lower() or 'approval' in content.lower():
                if max_discount > percent_value:
                    violation_article_id = article['id']
                    break
    
    if violation_article_id:
        break

# Also check for explicit dollar amount thresholds
if not violation_article_id:
    for article in policy_articles:
        title = article['title'] or ''
        summary = article['summary'] or ''
        faq = article['faq_answer__c'] or ''
        content = title + ' ' + summary + ' ' + faq
        
        # Look for dollar amount patterns
        dollar_matches = re.findall(r'\$(\d+(?:,\d+)*)|\b(\d+(?:,\d+)*)\s+dollars', content, re.IGNORECASE)
        
        for match in dollar_matches:
            # Extract the dollar value
            dollar_value = None
            for group in match:
                if group:
                    dollar_value = int(group.replace(',', ''))
                    break
            
            if dollar_value is not None:
                # Check if this might be an approval threshold
                if 'approval' in content.lower() or 'threshold' in content.lower() or 'limit' in content.lower() or 'maximum' in content.lower():
                    # Compare with quote total
                    quote_total = sum(float(item['TotalPrice']) for item in quote_items)
                    if quote_total > dollar_value:
                        violation_article_id = article['id']
                        break
        
        if violation_article_id:
            break

result = {
    'max_discount_in_quote': max_discount,
    'quote_total': sum(float(item['TotalPrice']) for item in quote_items),
    'violation_article_id': violation_article_id,
    'policy_articles_checked': len(policy_articles)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:5': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [], 'var_functions.query_db:10': [], 'var_functions.query_db:12': [{'Id': '006Wt000007BHHfIAO', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '#003Wt00000JqkgYIAR', 'OwnerId': '#005Wt000003NIybIAG', 'Probability': '75.0', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Name': 'InnovateX Solutions Technology Integration Opportunity', 'Description': 'TechPulse Solutions offers InnovateX Solutions a suite of tools, including AI-powered CircuitSync Pro and environmentally-focused EcoPCB Creator, to enhance their design capabilities. By incorporating DesignWave Automation, InnovateX can streamline workflows, ensuring faster project completion and higher client satisfaction. Integrating PulseSim Pro will optimize circuit design verification with precision and speed.', 'CreatedDate': '2021-05-20T14:15:30.000+0000', 'CloseDate': '2021-07-15'}]}

exec(code, env_args)
