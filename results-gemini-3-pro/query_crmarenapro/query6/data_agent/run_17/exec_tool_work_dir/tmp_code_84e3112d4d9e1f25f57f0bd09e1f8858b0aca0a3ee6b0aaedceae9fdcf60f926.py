code = """import json
import pandas as pd

# Load results
quote_line_items = [{"Id": "0QLWt0000022j3GOAQ", "QuoteId": "0Q0Wt000001WRAzKAO", "OpportunityLineItemId": "00kWt000002HUwhIAG", "Product2Id": "#01tWt000006hV6jIAE", "PricebookEntryId": "01uWt0000027P8bIAE", "Quantity": "3.0", "UnitPrice": "349.99", "Discount": "0.0", "TotalPrice": "1049.97"}, {"Id": "0QLWt0000022j81OAA", "QuoteId": "0Q0Wt000001WRAzKAO", "OpportunityLineItemId": "00kWt000002HHRkIAO", "Product2Id": "01tWt000006hV8LIAU", "PricebookEntryId": "01uWt0000027P8cIAE", "Quantity": "2.0", "UnitPrice": "529.99", "Discount": "0.0", "TotalPrice": "1059.98"}, {"Id": "0QLWt0000022n8TOAQ", "QuoteId": "0Q0Wt000001WRAzKAO", "OpportunityLineItemId": "00kWt000002HQJYIA4", "Product2Id": "#01tWt000006hPffIAE", "PricebookEntryId": "01uWt0000027PADIA2", "Quantity": "4.0", "UnitPrice": "299.99", "Discount": "0.0", "TotalPrice": "1199.96"}, {"Id": "#0QLWt0000022oAvOAI", "QuoteId": "0Q0Wt000001WRAzKAO", "OpportunityLineItemId": "00kWt000002HQJZIA4", "Product2Id": "01tWt000006hVczIAE", "PricebookEntryId": "01uWt0000027Pi5IAE", "Quantity": "35.0", "UnitPrice": "399.99", "Discount": "15.0", "TotalPrice": "11899.7025"}]

with open(locals()['var_function-call-3871856346329201203'], 'r') as f:
    products = json.load(f)

with open(locals()['var_function-call-3871856346329201134'], 'r') as f:
    knowledge_articles = json.load(f)

# Clean IDs
def clean_id(i):
    if i.startswith('#'):
        return i[1:]
    return i

product_map = {clean_id(p['Id']): p['Name'].strip() for p in products}

items_info = []
for item in quote_line_items:
    pid = clean_id(item['Product2Id'])
    pname = product_map.get(pid, "Unknown")
    items_info.append({
        "Product": pname,
        "Quantity": float(item['Quantity']),
        "UnitPrice": float(item['UnitPrice']),
        "Discount": float(item['Discount']) if item['Discount'] else 0.0
    })

print("Quote Items:")
print(json.dumps(items_info, indent=2))

# Search Knowledge Articles
keywords = ["CollabDesign Studio", "EcoPCB Creator", "AI Cirku-Tech", "DevVision IDE", "quantity", "limit", "price", "discount", "regulation", "policy", "setup"]
relevant_articles = []

for ka in knowledge_articles:
    text = (ka.get('title', '') + " " + ka.get('faq_answer__c', '') + " " + ka.get('summary', '')).lower()
    
    # Check for specific product mentions combined with policy keywords
    if any(p.lower() in text for p in ["collabdesign studio", "ecopcb creator", "ai cirku-tech", "devvision ide"]):
        relevant_articles.append({
            "Id": ka['id'],
            "Title": ka['title'],
            "Text": ka['faq_answer__c']
        })
    elif "regulation" in text or "invalid config" in text or "policy" in text:
         if "quantity" in text or "price" in text or "discount" in text:
             relevant_articles.append({
                "Id": ka['id'],
                "Title": ka['title'],
                "Text": ka['faq_answer__c']
            })

print("__RESULT__:")
print(json.dumps(relevant_articles))"""

env_args = {'var_function-call-3871856346329201065': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-3871856346329201134': 'file_storage/function-call-3871856346329201134.json', 'var_function-call-3871856346329201203': 'file_storage/function-call-3871856346329201203.json'}

exec(code, env_args)
