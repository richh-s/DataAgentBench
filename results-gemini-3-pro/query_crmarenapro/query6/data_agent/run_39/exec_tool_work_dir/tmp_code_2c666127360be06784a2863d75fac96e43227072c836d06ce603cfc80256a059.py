code = """import json
import re

# Load knowledge articles
with open(locals()['var_function-call-13205167140694388168'], 'r') as f:
    articles = json.load(f)

keywords = ['discount', 'quantity', 'limit', 'price', 'bundle', 'maximum', 'minimum', '%']
relevant_articles = []

for article in articles:
    text = (article.get('title', '') + ' ' + article.get('summary', '') + ' ' + article.get('faq_answer__c', '')).lower()
    
    # Check for product names + keywords in same article
    products = ['collabdesign', 'devvision', 'ecopcb', 'cirku-tech']
    
    has_product = any(p in text for p in products)
    has_keyword = any(k in text for k in keywords)
    
    if has_product and has_keyword:
        relevant_articles.append(article)

print("__RESULT__:")
print(json.dumps(relevant_articles))"""

env_args = {'var_function-call-3577143583478871835': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-3577143583478871756': 'file_storage/function-call-3577143583478871756.json', 'var_function-call-4227665644957381308': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}], 'var_function-call-6444435732355192003': [{'id': 'ka0Wt000000EqQ9IAK', 'title': "Understanding TechPulse's Return Policy for Purchased Items", 'summary': "Details of TechPulse Solutions' return policy for purchased items, outlining the process for returns, refunds, and exchanges to ensure transparency and customer satisfaction."}, {'id': '#ka0Wt000000EpSUIA0', 'title': 'TechPulse Solution Volume-Based Installation Timeline Policy', 'summary': 'TechPulse Solution Volume-Based Installation Timeline Policy'}, {'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers', 'summary': 'Policy for price adjustments based on competing offers'}], 'var_function-call-13205167140694388168': 'file_storage/function-call-13205167140694388168.json'}

exec(code, env_args)
