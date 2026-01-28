code = """import json
# Load full knowledge articles from the stored file
path = var_call_0KpFBuu8a9m6sHLJ4YcmrDzJ
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
# Find relevant articles
ids_of_interest = set(["ka0Wt000000Eq0MIAS", "#ka0Wt000000EnwvIAC", "ka0Wt000000EnthIAC"])
found = [item for item in data if item.get('id') in ids_of_interest]
# Also include any items whose title matches keywords
for item in data:
    title = item.get('title','').lower()
    if 'quantity' in title or 'discount' in title or 'price' in title:
        if item not in found:
            found.append(item)
# Load quote line items
qli = var_call_IaEJz8HUtJGo1Lh7UG4seq3b
# Prepare result
result = {
    'quote_id': '0Q0Wt000001WRAzKAO',
    'quote_line_items': qli,
    'matched_articles': found
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_tSscTaeB6SWFKMMMtlOwelhZ': [], 'var_call_ev1O9Jc9pIF456AK1WPjBspK': 'file_storage/call_ev1O9Jc9pIF456AK1WPjBspK.json', 'var_call_YQb2yfLs2NuiZqneq4ajk2yg': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_call_0KpFBuu8a9m6sHLJ4YcmrDzJ': 'file_storage/call_0KpFBuu8a9m6sHLJ4YcmrDzJ.json', 'var_call_IaEJz8HUtJGo1Lh7UG4seq3b': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_tPvm9F9FRizrHLgSBLhEYe2m': [{'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'summary': 'Volume-Based Discounts'}, {'id': '#ka0Wt000000EnwvIAC', 'title': 'Product Quantity Limits   ', 'summary': 'Product Quantity Limits'}, {'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers', 'summary': 'Policy for price adjustments based on competing offers'}]}

exec(code, env_args)
