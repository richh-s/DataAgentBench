code = """import json

# Get QuoteLineItem data  
quote_data = locals()['var_functions.query_db:2']

print('Quote Line Items')
for item in quote_data:
    print(json.dumps(item))
    print('---')

# Check for violations
violations = []
for item in quote_data:
    # Check for malformed Product2Id (leading # sign)
    if item['Product2Id'].startswith('#'):
        violations.append({
            'type': 'malformed_product_id',
            'product_id': item['Product2Id'],
            'message': 'Product ID has invalid format with leading # symbol'
        })
    
    # Check quantity > 30 units
    if float(item['Quantity']) > 30:
        violations.append({
            'type': 'quantity_exceeds_limit',
            'quantity': float(item['Quantity']),
            'message': 'Quantity exceeds maximum allowed limit'
        })
    
    # Check discount > 10 percent
    if float(item['Discount']) > 10:
        violations.append({
            'type': 'discount_exceeds_limit',
            'discount': float(item['Discount']),
            'message': 'Discount exceeds maximum allowed limit'
        })

print('Violations found: ' + str(len(violations)))
for v in violations:
    print(v['type'] + ' : ' + v['message'])

# Based on analysis, we have violations including malformed product IDs with leading #
# This relates to data corruption and ID format policies
# The knowledge article about ID validation and data corruption is relevant here

result = 'ka0Wt000000EpXNIA0'

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:20': [], 'var_functions.query_db:22': []}

exec(code, env_args)
