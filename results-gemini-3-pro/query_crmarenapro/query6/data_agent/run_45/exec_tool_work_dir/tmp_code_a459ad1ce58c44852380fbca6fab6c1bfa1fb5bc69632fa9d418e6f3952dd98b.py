code = """import json
import pandas as pd

# Load the knowledge articles from the file
file_path = locals()['var_function-call-26332781657081690']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Convert to DataFrame for easier filtering
df_articles = pd.DataFrame(articles)

# Keywords to search for
keywords = [
    "EcoPCB Creator", "AI Cirku-Tech", "DevVision IDE", "CollabDesign Studio",
    "regulation", "policy", "limit", "quantity", "price", "discount", "invalid config", "quotation", "bundle"
]

# Filter function
def is_relevant(row):
    text = (str(row['title']) + " " + str(row['summary']) + " " + str(row['faq_answer__c'])).lower()
    for kw in keywords:
        if kw.lower() in text:
            return True
    return False

# Apply filter
relevant_articles = df_articles[df_articles.apply(is_relevant, axis=1)]

# Print result
print("__RESULT__:")
print(relevant_articles.to_json(orient='records'))"""

env_args = {'var_function-call-26332781657083847': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-26332781657081690': 'file_storage/function-call-26332781657081690.json', 'var_function-call-7879702838541740368': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}]}

exec(code, env_args)
