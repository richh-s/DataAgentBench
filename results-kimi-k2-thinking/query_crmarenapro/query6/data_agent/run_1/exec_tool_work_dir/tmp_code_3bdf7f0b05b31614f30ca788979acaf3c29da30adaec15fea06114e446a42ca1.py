code = """import json
import re
# Get the result from previous tool call
# The key is stored in locals()
rl1 = locals()['var_functions.query_db_0']
# Clean up IDs to remove leading #
def clean_id(id_val):
    if id_val and isinstance(id_val, str):
        return id_val.lstrip('#').strip()
    return id_val
# Check each quote line item for potential violations
violations = []
# Rules to check:
# 1. Quantity limits
# 2. Discount limits
# 3. Price limits
for item in rl1:
    quantity = float(item.get('Quantity', 0))
    unit_price = float(item.get('UnitPrice', 0))
    discount = float(item.get('Discount', 0))
    total_price = float(item.get('TotalPrice', 0))
    
    item_id = clean_id(item.get('Id', ''))
    product_id = clean_id(item.get('Product2Id', ''))
    
    # Check quantity limits
    if quantity > 30:
        violations.append({'type': 'quantity_limit', 'item_id': item_id, 'product_id': product_id, 'quantity': quantity})
    
    # Check discount limits
    if discount > 10:
        violations.append({'type': 'discount_limit', 'item_id': item_id, 'product_id': product_id, 'discount': discount})
    
    # Check price limits
    if unit_price > 500 and discount == 0:
        violations.append({'type': 'price_discount_required', 'item_id': item_id, 'product_id': product_id, 'unit_price': unit_price})

print('__RESULT__:')
print(json.dumps(violations))"""

env_args = {'var_functions.query_db:0': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
