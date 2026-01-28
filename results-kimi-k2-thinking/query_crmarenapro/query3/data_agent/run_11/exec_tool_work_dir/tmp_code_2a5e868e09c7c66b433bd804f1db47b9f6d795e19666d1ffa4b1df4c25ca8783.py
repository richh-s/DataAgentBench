code = """import json

# Get the data from queries
opp = var_functions.query_db:0[0]
quotes = var_functions.query_db:18
tasks = var_functions.query_db:19

probability = float(opp['Probability'])
current_stage = opp['StageName']

# Check for negotiation indicators
has_negotiation_tasks = any('negotiation' in task.get('Subject', '').lower() or 
                           'proposal' in task.get('Subject', '').lower() 
                           for task in tasks)

# Determine correct stage
if probability >= 75 and has_negotiation_tasks:
    correct_stage = 'Negotiation'
elif probability >= 50 and len(quotes) > 0:
    correct_stage = 'Quote'
else:
    correct_stage = 'Discovery'

result = {'correct_stage': correct_stage}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '006Wt000007BGGjIAO', 'StageName': 'Discovery', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Amount': '61666.225', 'Probability': '85.0', 'CloseDate': '2022-02-20'}], 'var_functions.query_db:2': [], 'var_functions.query_db:3': [], 'var_functions.query_db:4': [{'Id': '00kWt000002HJTPIA4', 'Product2Id': '01tWt000006hV58IAE', 'Quantity': '50.0', 'TotalPrice': '25499.575'}, {'Id': '00kWt000002HOEWIA4', 'Product2Id': '01tWt000006hTUkIAM', 'Quantity': '30.0', 'TotalPrice': '10199.745'}, {'Id': '00kWt000002HUdKIAW', 'Product2Id': '01tWt000006hVhpIAE', 'Quantity': '45.0', 'TotalPrice': '18742.1175'}], 'var_functions.execute_python:14': {'correct_stage': 'Discovery'}, 'var_functions.query_db:18': [], 'var_functions.query_db:19': [{'Id': '00TWt000002yzp8MAA', 'Subject': 'Follow up on proposal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15'}, {'Id': '00TWt000002z4fFMAQ', 'Subject': 'Hold negotiation meeting', 'Status': 'Not Started', 'ActivityDate': '2022-02-10'}, {'Id': '00TWt000002ysm8MAA', 'Subject': 'Organize product demo', 'Status': 'Not Started', 'ActivityDate': '2022-01-15'}]}

exec(code, env_args)
