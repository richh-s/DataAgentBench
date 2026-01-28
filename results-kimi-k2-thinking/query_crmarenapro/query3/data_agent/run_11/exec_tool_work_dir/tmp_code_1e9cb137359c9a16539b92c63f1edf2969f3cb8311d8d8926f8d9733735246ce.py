code = """import json

# Check quotes data structure
quotes_data = var_functions.query_db:1
print('Full Quotes Data:', json.dumps(quotes_data, indent=2))

# Check if any quotes have final status
if quotes_data:
    for quote in quotes_data:
        print('Quote Status:', quote.get('Status'))
        print('Quote Description:', quote.get('Description'))

result = {'quotes': quotes_data}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '006Wt000007BGGjIAO', 'StageName': 'Discovery', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Amount': '61666.225', 'Probability': '85.0', 'CloseDate': '2022-02-20'}], 'var_functions.query_db:2': [], 'var_functions.query_db:3': [], 'var_functions.query_db:4': [{'Id': '00kWt000002HJTPIA4', 'Product2Id': '01tWt000006hV58IAE', 'Quantity': '50.0', 'TotalPrice': '25499.575'}, {'Id': '00kWt000002HOEWIA4', 'Product2Id': '01tWt000006hTUkIAM', 'Quantity': '30.0', 'TotalPrice': '10199.745'}, {'Id': '00kWt000002HUdKIAW', 'Product2Id': '01tWt000006hVhpIAE', 'Quantity': '45.0', 'TotalPrice': '18742.1175'}], 'var_functions.execute_python:14': {'correct_stage': 'Discovery'}}

exec(code, env_args)
