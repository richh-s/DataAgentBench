code = """import json

# Read the results from storage
opp_result = locals()['var_functions.query_db:0']
line_items_result = locals()['var_functions.query_db:2']
tasks_result = locals()['var_functions.query_db:3']
quotes_result = locals()['var_functions.query_db:4']
events_result = locals()['var_functions.query_db:5']

# Parse the opportunity data
opportunity = opp_result[0]
stage_name = opportunity['StageName']
contract_id = opportunity['ContractID__c']
amount = opportunity['Amount']
probability = opportunity['Probability']

# Check for line items and quotes
has_line_items = len(line_items_result) > 0
has_quotes = len(quotes_result) > 0

# Check for contract (if exists means closed)
has_contract = contract_id is not None and contract_id != 'None'

# Print some debugging info to see what we're working with
print('__RESULT__:')
print('Current Stage: ' + stage_name)
print('Has Contract: ' + str(has_contract))
print('Has Line Items: ' + str(has_line_items))
print('Has Quotes: ' + str(has_quotes))
print('Number of Tasks: ' + str(len(tasks_result)))

# Sample task if exists
if len(tasks_result) > 0:
    print('First task keys: ' + str(list(tasks_result[0].keys())))"""

env_args = {'var_functions.query_db:0': [{'Id': '006Wt000007BGGjIAO', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'OwnerId': '005Wt000003NIs9IAG', 'Probability': '85.0', 'Amount': '61666.225', 'StageName': 'Discovery', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'CloseDate': '2022-02-20'}], 'var_functions.query_db:2': [], 'var_functions.query_db:3': [{'Id': '00kWt000002HJTPIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hV58IAE', 'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '50.0', 'TotalPrice': '25499.575'}, {'Id': '00kWt000002HOEWIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hTUkIAM', 'PricebookEntryId': '01uWt0000027P6zIAE', 'Quantity': '30.0', 'TotalPrice': '10199.745'}, {'Id': '00kWt000002HUdKIAW', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVhpIAE', 'PricebookEntryId': '01uWt0000027P3mIAE', 'Quantity': '45.0', 'TotalPrice': '18742.1175'}], 'var_functions.query_db:4': [{'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIovIAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms'}], 'var_functions.query_db:5': []}

exec(code, env_args)
