code = """import json

# Read the knowledge articles to get full content
with open('/tmp/tmp3q2j8h1n.json', 'r') as f:
    knowledge_articles = json.load(f)

# Filter for the specific articles we need
relevant_articles = []
for article in knowledge_articles:
    if article['id'] in ['ka0Wt000000Eq0MIAS', '#ka0Wt000000EnwvIAC', 'ka0Wt000000Ens5IAC', 'ka0Wt000000EnvJIAS']:
        relevant_articles.append(article)

# Print the articles for analysis
for article in relevant_articles:
    print(f"ID: {article['id']}")
    print(f"Title: {article['title']}")
    print(f"Content: {article['faq_answer__c'][:500]}...")  # First 500 chars
    print("-" * 80)

print("\nChecking for violations...")

# Check Product Quantity Limits article more carefully
quantity_limits_article = None
for article in relevant_articles:
    if 'Product Quantity Limits' in article['title']:
        quantity_limits_article = article
        break

if quantity_limits_article:
    print("\nProduct Quantity Limits Content:")
    print(quantity_limits_article['faq_answer__c'])
    print("\n" + "="*80)

# Check the quote line items again
quote_items = [
    {"product": "EcoPCB Creator", "quantity": 3.0},
    {"product": "AI Cirku-Tech", "quantity": 2.0},
    {"product": "DevVision IDE", "quantity": 4.0},
    {"product": "CollabDesign Studio", "quantity": 35.0}
]

print("\nQuote Line Items:")
for item in quote_items:
    print(f"- {item['product']}: {item['quantity']} units")

# Check for violations
print("\n" + "="*80)
print("VIOLATION ANALYSIS:")
print("="*80)

if quantity_limits_article:
    content = quantity_limits_article['faq_answer__c']
    if 'CollabDesign Studio' in content:
        # Extract the limit for CollabDesign Studio
        import re
        match = re.search(r'CollabDesign Studio.*?up to (\d+) units', content)
        if match:
            limit = int(match.group(1))
            print(f"CollabDesign Studio limit: {limit} units per order")
            print(f"Quote quantity: 35 units")
            if 35 > limit:
                print(f"❌ VIOLATION: Quantity exceeds limit by {35 - limit} units!")
                print(f"Violated Knowledge Article ID: {quantity_limits_article['id']}")
            else:
                print("✅ No violation")

print("\n" + "="*80)"""

env_args = {'var_functions.query_db:0': [], 'var_functions.list_db:2': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:4': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_functions.query_db:6': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts'}, {'id': '#ka0Wt000000EnwvIAC', 'title': 'Product Quantity Limits   '}, {'id': 'ka0Wt000000Ens5IAC', 'title': 'Mandatory Bundles for Quotes'}, {'id': 'ka0Wt000000EnvJIAS', 'title': 'Product Exclusion Constraints'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}]}

exec(code, env_args)
