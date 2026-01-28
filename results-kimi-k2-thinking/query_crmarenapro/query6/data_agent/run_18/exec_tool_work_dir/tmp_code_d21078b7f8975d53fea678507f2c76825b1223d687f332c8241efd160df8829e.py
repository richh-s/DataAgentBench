code = """import json

# QuoteLineItem data
quote_line_items = [
    {"Id": "0QLWt0000022j3GOAQ", "QuoteId": "0Q0Wt000001WRAzKAO", "OpportunityLineItemId": "00kWt000002HUwhIAG", "Product2Id": "#01tWt000006hV6jIAE", "PricebookEntryId": "01uWt0000027P8bIAE", "Quantity": "3.0", "UnitPrice": "349.99", "Discount": "0.0", "TotalPrice": "1049.97"},
    {"Id": "0QLWt0000022j81OAA", "QuoteId": "0Q0Wt000001WRAzKAO", "OpportunityLineItemId": "00kWt000002HHRkIAO", "Product2Id": "01tWt000006hV8LIAU", "PricebookEntryId": "01uWt0000027P8cIAE", "Quantity": "2.0", "UnitPrice": "529.99", "Discount": "0.0", "TotalPrice": "1059.98"},
    {"Id": "0QLWt0000022n8TOAQ", "QuoteId": "0Q0Wt000001WRAzKAO", "OpportunityLineItemId": "00kWt000002HQJYIA4", "Product2Id": "#01tWt000006hPffIAE", "PricebookEntryId": "01uWt0000027PADIA2", "Quantity": "4.0", "UnitPrice": "299.99", "Discount": "0.0", "TotalPrice": "1199.96"},
    {"Id": "#0QLWt0000022oAvOAI", "QuoteId": "0Q0Wt000001WRAzKAO", "OpportunityLineItemId": "00kWt000002HQJZIA4", "Product2Id": "01tWt000006hVczIAE", "PricebookEntryId": "01uWt0000027Pi5IAE", "Quantity": "35.0", "UnitPrice": "399.99", "Discount": "15.0", "TotalPrice": "11899.7025"}
]

# Calculate total price for the quote
total_quote_price = sum(float(item["TotalPrice"]) for item in quote_line_items)
print(f"Total Quote Price: ${total_quote_price:.2f}")

# Check each item's eligibility for discounts based on volume discount policy
for item in quote_line_items:
    total_price = float(item["TotalPrice"])
    discount = float(item["Discount"])
    print(f"\nItem ID: {item['Id']}")
    print(f"  Total Price: ${total_price:.2f}")
    print(f"  Current Discount: {discount}%")
    print(f"  Should have 15% discount (over $20): {total_price >= 20}")
    print(f"  Compliant: {discount == 15.0 if total_price >= 20 else 'N/A - no discount required'}")

# Find violations
violations = []
for item in quote_line_items:
    total_price = float(item["TotalPrice"])
    discount = float(item["Discount"])
    # All items are above $20, so all should have 15% discount according to policy
    if discount != 15.0 and total_price >= 20:
        violations.append(item["Id"])

print(f"\n\nVIOLATIONS FOUND: {len(violations)} items")
for vid in violations:
    print(f"  - {vid}")

if violations:
    print("\n\nThe issue is inconsistent application of volume discounts.")"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_functions.query_db:5': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE', 'Description': 'Integrated development environment with intuitive coding and debugging capabilities.', 'IsActive': '1', 'External_ID__c': 'Integrated Development Environments,Educational and Training Platforms_6', 'UnitPrice': '299.99'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   ', 'Description': 'Environmentally-friendly PCB design solution with power utilization analytics.', 'IsActive': '1', 'External_ID__c': 'PCB Design Solutions,Power Optimization Tools_4', 'UnitPrice': '349.99'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.', 'IsActive': '1', 'External_ID__c': 'AI-Powered Circuit Design Tools,Customizable Workflow Automation_5', 'UnitPrice': '529.99'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio', 'Description': 'Enhanced design collaboration platform offering real-time editing and feedback.', 'IsActive': '1', 'External_ID__c': 'Cloud-Based Design Collaboration,Integrated Development Environments_30', 'UnitPrice': '399.99'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
