code = """import json

# Load the opportunity data
opportunity = [{"Id": "006Wt000007BGGjIAO", "ContractID__c": "None", "AccountId": "001Wt00000PGRqjIAH", "ContactId": "#003Wt00000JqczHIAR", "OwnerId": "005Wt000003NIs9IAG", "Probability": "85.0", "Amount": "61666.225", "StageName": "Discovery", "Name": "DataWave Analytics AI-Driven Enhancement ", "Description": "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", "CreatedDate": "2021-11-15T10:25:30.000+0000", "CloseDate": "2022-02-20"}]

# Load the tasks data
tasks = [{"Id": "00TWt000002ysm8MAA", "WhatId": "006Wt000007BGGjIAO", "OwnerId": "#005Wt000003NIovIAG", "Priority": "High", "Status": "Not Started", "ActivityDate": "2022-01-15", "Subject": "Organize product demo", "Description": "Set up a product demonstration to showcase the relevant solutions"}, {"Id": "00TWt000002yzp8MAA", "WhatId": "006Wt000007BGGjIAO", "OwnerId": "005Wt000003NF9WIAW", "Priority": "Normal", "Status": "Not Started ", "ActivityDate": "2022-02-15", "Subject": "Follow up on proposal", "Description": "Reach out to the client to address any questions and negotiate terms"}, {"Id": "00TWt000002z4fFMAQ", "WhatId": "006Wt000007BGGjIAO", "OwnerId": "#005Wt000003NIc1IAG", "Priority": "High", "Status": "Not Started", "ActivityDate": "2022-02-10", "Subject": "Hold negotiation meeting", "Description": "Discuss terms and finalize pricing with the client"}]

# Analyze tasks to determine appropriate stage
current_stage = opportunity[0]['StageName']
probability = float(opportunity[0]['Probability'])

# Check task types
has_demo = any('demo' in task['Subject'].lower() for task in tasks)
has_proposal = any('proposal' in task['Subject'].lower() for task in tasks)
has_negotiation = any('negotiation' in task['Subject'].lower() for task in tasks)

# Determine appropriate stage based on tasks and probability
if has_negotiation:
    appropriate_stage = 'Negotiation'
elif has_proposal:
    appropriate_stage = 'Quote'
elif has_demo:
    appropriate_stage = 'Discovery'
else:
    appropriate_stage = 'Qualification'

# Also consider probability - 85% is typically negotiation stage
if probability >= 80:
    appropriate_stage = 'Negotiation'

result = appropriate_stage
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '006Wt000007BGGjIAO', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'OwnerId': '005Wt000003NIs9IAG', 'Probability': '85.0', 'Amount': '61666.225', 'StageName': 'Discovery', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'CloseDate': '2022-02-20'}], 'var_functions.query_db:2': [{'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIovIAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client'}], 'var_functions.query_db:4': []}

exec(code, env_args)
