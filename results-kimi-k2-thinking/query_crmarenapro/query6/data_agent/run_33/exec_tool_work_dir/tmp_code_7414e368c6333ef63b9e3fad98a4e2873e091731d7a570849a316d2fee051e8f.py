code = """import json

# Load the knowledge articles from the file
with open('/tmp/tmp_oxfrr9a.json', 'r') as f:
    knowledge_articles = json.load(f)

print("Total knowledge articles:", len(knowledge_articles))

# Search for articles that might contain regulations about quotes, pricing, or product setup
relevant_articles = []
for article in knowledge_articles:
    content = (article.get('title', '') + ' ' + article.get('summary', '') + ' ' + article.get('faq_answer__c', '')).lower()
    
    # Look for keywords related to regulations
    keywords = ['quote', 'pricing', 'price', 'discount', 'approval', 'review', 'limit', 'regulation', 'policy', 'violation', 'invalid']
    if any(keyword in content for keyword in keywords):
        relevant_articles.append(article)

print("Potentially relevant articles:", len(relevant_articles))
for article in relevant_articles:
    print("\nArticle ID:", article.get('id'))
    print("Title:", article.get('title'))
    print("Summary:", article.get('summary')[:200])

# Check the quote details we have from the previous queries
print("\n\nQuote Analysis:")
print("Quote ID: #0Q0Wt000001WRAzKAO")
print("Status: Needs Review")
print("Opportunity ID: 006Wt000007BGgXIAW")

# Opportunity line items (from previous query)
line_items = [
    {
        "ProductName": "AI Cirku-Tech",
        "Quantity": 2.0,
        "UnitPrice": 529.99,
        "TotalPrice": 1059.98
    },
    {
        "ProductName": "DevVision IDE",
        "Quantity": 4.0,
        "UnitPrice": 299.99,
        "TotalPrice": 1199.96
    }
]

print("\nLine Items:")
for item in line_items:
    print("- " + item['ProductName'] + ": " + str(item['Quantity']) + " units @ $" + str(item['UnitPrice']) + " = $" + str(item['TotalPrice']))

# Check if any articles specifically mention "Needs Review" status or approval processes
for article in knowledge_articles:
    content = (article.get('title', '') + ' ' + article.get('summary', '') + ' ' + article.get('faq_answer__c', '')).lower()
    if 'needs review' in content or 'approval' in content or 'review' in content:
        print("\n\nFound article mentioning approval/review:")
        print("ID:", article.get('id'))
        print("Title:", article.get('title'))

# Let's look more closely at the Product Quantity Limits article
for article in knowledge_articles:
    if 'Product Quantity Limits' in article.get('title', ''):
        print("\n\n=== PRODUCT QUANTITY LIMITS ARTICLE ===")
        print("ID:", article.get('id'))
        print("Title:", article.get('title'))
        print("Summary:", article.get('summary'))
        # Check if our products are in the list
        content = article.get('faq_answer__c', '').lower()
        print("Contains AI Cirku-Tech:", 'ai cirku-tech' in content)
        print("Contains DevVision IDE:", 'devvision' in content or 'devvision ide' in content)
        # Extract quantity limits
        lines = article.get('faq_answer__c', '').split('\n')
        for line in lines:
            if 'unit' in line.lower() and ('ai' in line.lower() or 'cirku' in line.lower() or 'devvision' in line.lower() or 'ide' in line.lower()):
                print("Line:", line.strip())"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_functions.query_db:6': [], 'var_functions.query_db:8': [{'Id': '#00kWt000002HHRkIAO', 'OpportunityId': '006Wt000007BGgXIAW', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'TotalPrice': '1059.98'}, {'Id': '00kWt000002HQJYIA4', 'OpportunityId': '006Wt000007BGgXIAW', 'Product2Id': '01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'TotalPrice': '1199.96'}], 'var_functions.query_db:10': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE', 'Description': 'Integrated development environment with intuitive coding and debugging capabilities.', 'IsActive': '1', 'UnitPrice': '299.99'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.', 'IsActive': '1', 'UnitPrice': '529.99'}], 'var_functions.list_db:12': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
