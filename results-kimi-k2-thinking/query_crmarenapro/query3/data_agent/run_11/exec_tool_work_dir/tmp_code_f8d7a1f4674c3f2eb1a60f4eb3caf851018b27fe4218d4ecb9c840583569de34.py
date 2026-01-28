code = """import json

# Load the data
opp_data = var_functions.query_db:0
quotes_data = var_functions.query_db:1
contracts_data = var_functions.query_db:2
line_items_data = var_functions.query_db:3

print('Opportunity Data:', json.dumps(opp_data))
print('Quotes Data:', json.dumps(quotes_data))
print('Contracts Data:', json.dumps(contracts_data))
print('Line Items Data:', json.dumps(line_items_data))

# Analysis
opp = opp_data[0]
current_stage = opp['StageName']
probability = float(opp['Probability'])
close_date = opp['CloseDate']
has_quotes = len(quotes_data) > 0
has_contracts = len(contracts_data) > 0
has_line_items = len(line_items_data) > 0

print('Current Stage:', current_stage)
print('Probability:', probability)
print('Close Date:', close_date)
print('Has Quotes:', has_quotes)
print('Has Contracts:', has_contracts)
print('Has Line Items:', has_line_items)

result = {
    'current_stage': current_stage,
    'probability': probability,
    'has_quotes': has_quotes,
    'has_contracts': has_contracts,
    'has_line_items': has_line_items
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '006Wt000007BGGjIAO', 'StageName': 'Discovery', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Amount': '61666.225', 'Probability': '85.0', 'CloseDate': '2022-02-20'}], 'var_functions.query_db:2': [], 'var_functions.query_db:3': [], 'var_functions.query_db:4': [{'Id': '00kWt000002HJTPIA4', 'Product2Id': '01tWt000006hV58IAE', 'Quantity': '50.0', 'TotalPrice': '25499.575'}, {'Id': '00kWt000002HOEWIA4', 'Product2Id': '01tWt000006hTUkIAM', 'Quantity': '30.0', 'TotalPrice': '10199.745'}, {'Id': '00kWt000002HUdKIAW', 'Product2Id': '01tWt000006hVhpIAE', 'Quantity': '45.0', 'TotalPrice': '18742.1175'}]}

exec(code, env_args)
