code = """# Reading the opportunity data
import json

# These are the actual results from the queries
opportunity = [{"Id": "006Wt000007BGGjIAO", "Name": "DataWave Analytics AI-Driven Enhancement ", "StageName": "Discovery", "Probability": "85.0", "Amount": "61666.225", "CloseDate": "2022-02-20", "Description": "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", "AccountId": "001Wt00000PGRqjIAH", "ContactId": "#003Wt00000JqczHIAR", "OwnerId": "005Wt000003NIs9IAG"}]

tasks = [{"Id": "00TWt000002ysm8MAA", "WhatId": "006Wt000007BGGjIAO", "Subject": "Organize product demo", "Status": "Not Started", "Priority": "High", "ActivityDate": "2022-01-15", "Description": "Set up a product demonstration to showcase the relevant solutions"}, 
         {"Id": "00TWt000002yzp8MAA", "WhatId": "006Wt000007BGGjIAO", "Subject": "Follow up on proposal", "Status": "Not Started ", "Priority": "Normal", "ActivityDate": "2022-02-15", "Description": "Reach out to the client to address any questions and negotiate terms"}, 
         {"Id": "00TWt000002z4fFMAQ", "WhatId": "006Wt000007BGGjIAO", "Subject": "Hold negotiation meeting", "Status": "Not Started", "Priority": "High", "ActivityDate": "2022-02-10", "Description": "Discuss terms and finalize pricing with the client"}]

# Check for quotes
quotes = []
quotes_corrupted = []

# Analyze the situation
has_quotes = len(quotes) > 0 or len(quotes_corrupted) > 0
has_tasks = len(tasks) > 0

# Check task subjects for indicators
proposal_related = any('proposal' in task['Subject'].lower() for task in tasks)
negotiation_related = any('negotiat' in task['Subject'].lower() for task in tasks)
demo_related = any('demo' in task['Subject'].lower() for task in tasks)

# Get probability
probability = float(opportunity[0]['Probability'])
current_stage = opportunity[0]['StageName']

analysis = {
    'opportunity_id': opportunity[0]['Id'],
    'current_stage': current_stage,
    'probability': probability,
    'has_quotes': has_quotes,
    'has_tasks': has_tasks,
    'proposal_task_exists': proposal_related,
    'negotiation_task_exists': negotiation_related,
    'demo_task_exists': demo_related,
    'close_date': opportunity[0]['CloseDate']
}

print('__RESULT__:')
print(json.dumps(analysis))"""

env_args = {'var_functions.query_db:0': [{'Id': '006Wt000007BGGjIAO', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'StageName': 'Discovery', 'Probability': '85.0', 'Amount': '61666.225', 'CloseDate': '2022-02-20', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'OwnerId': '005Wt000003NIs9IAG'}], 'var_functions.query_db:2': [], 'var_functions.query_db:4': [], 'var_functions.query_db:8': [{'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'Subject': 'Organize product demo', 'Status': 'Not Started', 'Priority': 'High', 'ActivityDate': '2022-01-15', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'Subject': 'Follow up on proposal', 'Status': 'Not Started ', 'Priority': 'Normal', 'ActivityDate': '2022-02-15', 'Description': 'Reach out to the client to address any questions and negotiate terms'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'Subject': 'Hold negotiation meeting', 'Status': 'Not Started', 'Priority': 'High', 'ActivityDate': '2022-02-10', 'Description': 'Discuss terms and finalize pricing with the client'}]}

exec(code, env_args)
