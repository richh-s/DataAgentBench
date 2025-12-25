code = """import json

# Load knowledge articles
with open(locals()['var_function-call-5779811584283906500'], 'r') as f:
    articles = json.load(f)

keywords = ["CollabDesign", "quantity", "discount", "price", "approval", "limit", "regulation", "invalid", "config"]

relevant_articles = []

for article in articles:
    text = (article.get('title', '') + ' ' + article.get('summary', '') + ' ' + article.get('faq_answer__c', '')).lower()
    
    # Filter out competitor articles if possible, but keep them if they mention the product
    if "competitor" in text and "collabdesign" not in text:
        continue

    score = 0
    matches = []
    
    if "collabdesign" in text:
        score += 5
        matches.append("CollabDesign")
        
    if "quantity" in text or "limit" in text or "maximum" in text:
        score += 1
        matches.append("Quantity/Limit")
        
    if "discount" in text:
        score += 1
        matches.append("Discount")

    if score > 0:
        relevant_articles.append({
            "id": article['id'],
            "title": article['title'],
            "matches": matches,
            "summary": article['summary'],
            "faq_answer__c": article.get('faq_answer__c', '')[:200] # Preview
        })

print("__RESULT__:")
print(json.dumps(relevant_articles))"""

env_args = {'var_function-call-5779811584283909379': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-5779811584283906500': 'file_storage/function-call-5779811584283906500.json', 'var_function-call-10824156375473959546': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}], 'var_function-call-5191502495806351568': 'file_storage/function-call-5191502495806351568.json'}

exec(code, env_args)
