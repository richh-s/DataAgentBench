code = """import json

# Read the QuoteLineItem data from the previous query
qli_data = locals()['var_functions.query_db:2']

print('=== Quote Line Items Analysis ===')
for item in qli_data:
    print('ID: ' + str(item['Id']) + ', Product2Id: ' + str(item['Product2Id']) + ', Quantity: ' + str(item['Quantity']) + ', UnitPrice: $' + str(item['UnitPrice']) + ', Discount: ' + str(item['Discount']) + '%, Total: $' + str(item['TotalPrice']))

# Check for potential violations
violations = []

# 1. Check for malformed IDs (leading #)
for item in qli_data:
    if item['Id'].startswith('#') or item['Product2Id'].startswith('#'):
        violations.append({
            'type': 'malformed_id',
            'message': 'Line item has malformed ID: QuoteLineItemId=' + str(item['Id']) + ', Product2Id=' + str(item['Product2Id'])
        })

# 2. Check quantity limits (>30 might be a violation)
for item in qli_data:
    quantity = float(item['Quantity'])
    if quantity > 30:
        violations.append({
            'type': 'quantity_limit',
            'message': 'Quantity exceeds limit: ' + str(quantity) + ' units for product ' + str(item['Product2Id'])
        })

# 3. Check discount limits (>10% might be a violation)
for item in qli_data:
    discount = float(item['Discount'])
    if discount > 10:
        violations.append({
            'type': 'discount_limit',
            'message': 'Discount exceeds limit: ' + str(discount) + '% for product ' + str(item['Product2Id'])
        })

print('\n=== Found ' + str(len(violations)) + ' potential violations ===')
for v in violations:
    print('Type: ' + v['type'] + ', Message: ' + v['message'])

# Check knowledge articles for violations
# For malformed IDs
print('\n=== Knowledge Article Analysis ===')
print('Malformed ID violations would relate to data corruption/ID format policies')
print('Quantity limit violations would relate to maximum order quantity policies')
print('Discount limit violations would relate to discount approval policies')

# Find the specific knowledge article IDs
# Based on violations found:
# malfored_id: look for ID format/validation policies
# quantity_limit: look for quantity limit policies  
# discount_limit: look for discount limit policies

result = {
    'violations': violations,
    'total_violations': len(violations),
    'malformed_ids': [item for item in qli_data if item['Id'].startswith('#') or item['Product2Id'].startswith('#')],
    'quantity_exceeded': [item for item in qli_data if float(item['Quantity']) > 30],
    'discount_exceeded': [item for item in qli_data if float(item['Discount']) > 10]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
