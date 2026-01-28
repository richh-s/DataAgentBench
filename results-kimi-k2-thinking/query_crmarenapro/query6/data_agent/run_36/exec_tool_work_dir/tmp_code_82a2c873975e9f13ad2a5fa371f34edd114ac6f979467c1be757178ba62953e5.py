code = """import json

# Read the QuoteLineItem data from the file
file_path = var_functions.query_db:12
with open(file_path, 'r') as f:
    quote_line_items = json.load(f)

print("__RESULT__:")
print(f"Total number of quote line items: {len(quote_line_items)}")

# Find those related to our quote ID
target_quote_ids = ["0Q0Wt000001WRAzKAO", "#0Q0Wt000001WRAzKAO"]
matching_items = [item for item in quote_line_items if item['QuoteId'] in target_quote_ids]
print(f"Number of matching items: {len(matching_items)}")

# Show the matching items
for item in matching_items:
    print(f"Quote ID: {item['QuoteId']}, Product: {item['Product2Id']}, Quantity: {item['Quantity']}, UnitPrice: {item['UnitPrice']}, Discount: {item['Discount']}, TotalPrice: {item['TotalPrice']}")"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:6': [], 'var_functions.query_db:8': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_functions.query_db:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
