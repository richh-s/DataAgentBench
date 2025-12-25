code = """import json

# Load the knowledge articles
with open(locals()['var_function-call-9314318229804425950'], 'r') as f:
    articles = json.load(f)

relevant_articles_details = []
target_titles = ["Volume-Based Discounts", "TechPulse Solution Volume-Based Installation Timeline Policy"]
keywords = ["quantity", "price", "discount", "limit", "config", "setup", "regulation", "policy", "invalid", "violate"]

for art in articles:
    # Check specific titles first
    if art.get('title', '').strip() in target_titles:
         relevant_articles_details.append(art)
         continue
    
    # Or check keywords in title/summary
    text = (art.get('title', '') + " " + art.get('summary', '')).lower()
    if "discount" in text or "volume" in text or "quantity" in text or "policy" in text or "invalid" in text:
         relevant_articles_details.append(art)

print("__RESULT__:")
print(json.dumps(relevant_articles_details))"""

env_args = {'var_function-call-5453371388796272722': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-8297393543246110417': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE', 'Description': 'Integrated development environment with intuitive coding and debugging capabilities.'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   ', 'Description': 'Environmentally-friendly PCB design solution with power utilization analytics.'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio', 'Description': 'Enhanced design collaboration platform offering real-time editing and feedback.'}], 'var_function-call-9314318229804425950': 'file_storage/function-call-9314318229804425950.json', 'var_function-call-18085625660988873062': 'file_storage/function-call-18085625660988873062.json'}

exec(code, env_args)
