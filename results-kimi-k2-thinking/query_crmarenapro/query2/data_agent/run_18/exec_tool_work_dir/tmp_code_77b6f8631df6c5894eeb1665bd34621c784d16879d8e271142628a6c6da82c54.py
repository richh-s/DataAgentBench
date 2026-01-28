code = """import json
import re

# Read the full knowledge articles result
file_path = locals()['var_functions.query_db:26']
with open(file_path, 'r') as f:
    knowledge_articles = json.load(f)

# Quote details
quote_items = locals()['var_functions.query_db:2']
max_discount = max(float(item['Discount']) for item in quote_items)
quote_total = sum(float(item['TotalPrice']) for item in quote_items)

print("Quote Analysis:")
print("- Maximum discount offered: " + str(max_discount) + "%")
print("- Total quote value: $" + str(round(quote_total, 2)))
print("- Number of line items: " + str(len(quote_items)))

approval_policy_keywords = [
    'requires approval', 'approval required', 'manager approval', 'authorization required',
    'discount limit', 'maximum discount allowed', 'discount threshold', 'approval threshold',
    'quote approval', 'sales approval policy', 'discount approval', 'exceeds approval',
    'cannot exceed', 'must be approved'
]

policy_violations = []

for article in knowledge_articles:
    title = (article['title'] or '').lower()
    summary = (article['summary'] or '').lower()
    faq = (article['faq_answer__c'] or '').lower()
    content = title + ' ' + summary + ' ' + faq
    
    is_policy_doc = any(keyword in content for keyword in approval_policy_keywords)
    
    if is_policy_doc:
        print("\n=== Policy Article Found ===")
        print("ID: " + str(article['id']))
        print("Title: " + str(article['title']))
        
        discount_patterns = re.findall(r'(\d+)%|\b(\d+)\s+percent', content)
        
        for pattern in discount_patterns:
            percent = int(pattern[0]) if pattern[0] else int(pattern[1])
            if 'limit' in content or 'maximum' in content or 'cannot exceed' in content or 'approval' in content:
                if max_discount > percent:
                    policy_violations.append(article['id'])
                    print("VIOLATION: Discount exceeds " + str(percent) + "% limit")

# Check the Volume-Based Discounts article
vol_discount_article = locals()['var_functions.query_db:20'][0]
print("\n=== Checking Volume-Based Discounts Article ===")
print("Title: " + str(vol_discount_article['title']))
print("Note: This appears to be about customer promotions, not internal approval policies")

print("\n=== Results ===")
print("Policy violations found: " + str(len(policy_violations)))

result = {
    'violations': policy_violations,
    'violation_count': len(policy_violations),
    'max_discount': max_discount,
    'quote_total': quote_total
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:5': [], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [], 'var_functions.query_db:10': [], 'var_functions.query_db:12': [{'Id': '006Wt000007BHHfIAO', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '#003Wt00000JqkgYIAR', 'OwnerId': '#005Wt000003NIybIAG', 'Probability': '75.0', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Name': 'InnovateX Solutions Technology Integration Opportunity', 'Description': 'TechPulse Solutions offers InnovateX Solutions a suite of tools, including AI-powered CircuitSync Pro and environmentally-focused EcoPCB Creator, to enhance their design capabilities. By incorporating DesignWave Automation, InnovateX can streamline workflows, ensuring faster project completion and higher client satisfaction. Integrating PulseSim Pro will optimize circuit design verification with precision and speed.', 'CreatedDate': '2021-05-20T14:15:30.000+0000', 'CloseDate': '2021-07-15'}], 'var_functions.execute_python:18': {'max_discount_in_quote': 15.0, 'quote_total': 9140.7755, 'violation_article_id': 'ka0Wt000000Eq0MIAS', 'policy_articles_checked': 100}, 'var_functions.query_db:20': [{'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'faq_answer__c': "Volume-based discounts are a strategic tool for fostering customer loyalty and encouraging bulk purchases. At TechPulse Solution, we aim to provide value-added benefits to our customers, and volume-based discounts are integral to this mission. Here is a detailed overview of the volume-based discounts currently available:\n\n1. **5% Discount for Purchases Over $5**: This entry-level discount is designed for customers making modest but regular purchases. If your transaction totals $5 or more, you automatically become eligible for a 5% discount on your total purchase. This incentive is perfect for small businesses or individuals looking to maximize their purchasing power without committing to large upfront investments.\n\n2. **10% Discount for Purchases Over $10**: By increasing your purchase to $10, you can enjoy a more substantial 10% discount. This tier is targeted at growing businesses or tech enthusiasts planning for larger projects. Whether you're a startup needing essential tech solutions or an established entity upgrading current systems, this level of discount allows you to save significant amounts while meeting your needs.\n\n3. **15% Discount for Purchases Over $20**: The highest discount tier is designed for customers planning substantial investments in tech solutions. With a purchase of $20 or more, you can benefit from a generous 15% discount. This is particularly advantageous for businesses engaged in major scaling projects or for those who require extensive tech solutions for operational expansion.\n\nThese volume-based discounts are designed to reward you as you invest more in our innovative solutions, ensuring that you receive the best possible value. They are automatically applied at checkout, simplifying the purchasing process and enabling you to focus on selecting the best technology for your needs.\n\nIncorporating these discounts into your purchasing strategy can significantly reduce costs while allowing access to premium technology and support from TechPulse Solution. Whether you are a small business making selective purchases or a large company procuring extensive solutions, our discount structure provides a tailored approach to meet varying budgetary needs.\n\nOptimize your purchasing strategy and operational efficiency with our volume-based discounts, designed to bring you closer to innovative technology that can drive your success. At TechPulse Solution, your needs are at the forefront, and these carefully crafted discounts provide a pathway to affordable excellence.", 'summary': 'Volume-Based Discounts', 'urlname': '1745269013-mq1zw'}], 'var_functions.list_db:24': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': []}

exec(code, env_args)
