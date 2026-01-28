code = """import pandas as pd
import json

# Access query results
opp_data = var_functions.query_db_0
quotes_data = var_functions.query_db_1
contracts_data = var_functions.query_db_2
line_items_data = var_functions.query_db_3

print('Opportunity Data:')
print(json.dumps(opp_data, indent=2))

print('
Quotes Data:')
print(json.dumps(quotes_data, indent=2))

print('
Contracts Data:')
print(json.dumps(contracts_data, indent=2))

print('
Line Items Data:')
print(json.dumps(line_items_data, indent=2))

opp = opp_data[0] if opp_data else None

if opp:
    stage_name = opp.get('StageName')
    probability = float(opp.get('Probability', 0))
    close_date = opp.get('CloseDate')
    
    print(f'
Current Stage: {stage_name}')
    print(f'Probability: {probability}%')
    print(f'Close Date: {close_date}')
    print(f'Has Line Items: {len(line_items_data) > 0}')
    print(f'Has Quotes: {len(quotes_data) > 0}')
    print(f'Has Contracts: {len(contracts_data) > 0}')
    
    has_quotes = len(quotes_data) > 0
    has_contracts = len(contracts_data) > 0
    
    # CRM logic: High probability (85%) with quotes suggests Negotiation stage
    # Presence of contracts would suggest Closed stage
    
    result = {
        'current_stage': stage_name,
        'probability': probability,
        'close_date': close_date,
        'has_quotes': has_quotes,
        'has_contracts': has_contracts,
        'num_line_items': len(line_items_data)
    }
    
    print('__RESULT__:')
    print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '006Wt000007BGGjIAO', 'StageName': 'Discovery', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Amount': '61666.225', 'Probability': '85.0', 'CloseDate': '2022-02-20'}], 'var_functions.query_db:2': [], 'var_functions.query_db:3': [], 'var_functions.query_db:4': [{'Id': '00kWt000002HJTPIA4', 'Product2Id': '01tWt000006hV58IAE', 'Quantity': '50.0', 'TotalPrice': '25499.575'}, {'Id': '00kWt000002HOEWIA4', 'Product2Id': '01tWt000006hTUkIAM', 'Quantity': '30.0', 'TotalPrice': '10199.745'}, {'Id': '00kWt000002HUdKIAW', 'Product2Id': '01tWt000006hVhpIAE', 'Quantity': '45.0', 'TotalPrice': '18742.1175'}]}

exec(code, env_args)
