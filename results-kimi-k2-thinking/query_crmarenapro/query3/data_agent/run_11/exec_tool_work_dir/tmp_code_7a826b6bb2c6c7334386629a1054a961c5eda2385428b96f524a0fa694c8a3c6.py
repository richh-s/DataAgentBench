code = """import json

# Read the stored results from files
results = []
for i in range(4):
    key = 'var_functions.query_db:' + str(i)
    data = locals().get(key, [])
    results.append(data)

opp_data = results[0]
quotes_data = results[1]
contracts_data = results[2]
line_items_data = results[3]

# Print data for debugging
print('Opportunity:', json.dumps(opp_data))
print('Quotes:', json.dumps(quotes_data))
print('Contracts:', json.dumps(contracts_data))
print('Line Items:', json.dumps(line_items_data))

# Analyze the data
if opp_data:
    opp = opp_data[0]
    current_stage = opp['StageName']
    probability = float(opp['Probability'])
    has_quotes = len(quotes_data) > 0
    has_contracts = len(contracts_data) > 0
    
    print('Current Stage:', current_stage)
    print('Probability:', probability)
    print('Has Quotes:', has_quotes)
    print('Has Contracts:', has_contracts)
    
    # Determine correct stage
    # Discovery = Initial qualification, no quotes yet
    # Quote = Quotes created but not sent
    # Negotiation = Quotes sent/proposed, high probability
    # Closed = Won or Lost, contracts signed
    
    if has_contracts:
        correct_stage = 'Closed'
    elif has_quotes and probability >= 70:
        correct_stage = 'Negotiation'
    elif has_quotes:
        correct_stage = 'Quote'
    else:
        correct_stage = 'Discovery'
    
    print('Correct Stage:', correct_stage)
    output = {'correct_stage': correct_stage}
    
    print('__RESULT__:')
    print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': [{'Id': '006Wt000007BGGjIAO', 'StageName': 'Discovery', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Amount': '61666.225', 'Probability': '85.0', 'CloseDate': '2022-02-20'}], 'var_functions.query_db:2': [], 'var_functions.query_db:3': [], 'var_functions.query_db:4': [{'Id': '00kWt000002HJTPIA4', 'Product2Id': '01tWt000006hV58IAE', 'Quantity': '50.0', 'TotalPrice': '25499.575'}, {'Id': '00kWt000002HOEWIA4', 'Product2Id': '01tWt000006hTUkIAM', 'Quantity': '30.0', 'TotalPrice': '10199.745'}, {'Id': '00kWt000002HUdKIAW', 'Product2Id': '01tWt000006hVhpIAE', 'Quantity': '45.0', 'TotalPrice': '18742.1175'}]}

exec(code, env_args)
