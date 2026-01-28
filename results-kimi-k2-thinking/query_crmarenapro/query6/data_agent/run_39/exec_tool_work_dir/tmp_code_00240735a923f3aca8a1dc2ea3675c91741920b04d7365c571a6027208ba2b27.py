code = """import json

# Retrieve the quote details
quote_data = var_functions.query_db:2
quote_line_items = var_functions.query_db:4
opportunity_line_items_data = var_functions.query_db:6

# Check for the invalid condition based on the article rules
invalid_config_found = False
article_violated_id = ""

# Rule 1: Check if total quantity across both products is at least 30
product1 = next((item for item in opportunity_line_items_data if item["Product2Id"] == "01tWt000006hV8LIAU"), None)
product2 = next((item for item in opportunity_line_items_data if item["Product2Id"] == "01tWt000006hPffIAE"), None)

if product1 and product2:
    total_quantity = float(product1.get("Quantity", 0)) + float(product2.get("Quantity", 0))
    if total_quantity < 30.0:
        invalid_config_found = True
        article_violated_id = "ka-02849"

# Rule 2: Check if the combined total amount is less than $5000
total_amount = 0
for item in opportunity_line_items_data:
    total_amount += float(item.get("TotalPrice", 0))

if total_amount < 5000:
    invalid_config_found = True
    article_violated_id = "ka-02849"  # This rule also applies to the same article

# Output the result
print('__RESULT__:')
print(json.dumps(article_violated_id))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_functions.query_db:4': [], 'var_functions.query_db:6': [{'Id': '#00kWt000002HHRkIAO', 'OpportunityId': '006Wt000007BGgXIAW', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'TotalPrice': '1059.98'}, {'Id': '00kWt000002HQJYIA4', 'OpportunityId': '006Wt000007BGgXIAW', 'Product2Id': '01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'TotalPrice': '1199.96'}], 'var_functions.query_db:8': [{'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.', 'IsActive': '1', 'External_ID__c': 'AI-Powered Circuit Design Tools,Customizable Workflow Automation_5'}]}

exec(code, env_args)
