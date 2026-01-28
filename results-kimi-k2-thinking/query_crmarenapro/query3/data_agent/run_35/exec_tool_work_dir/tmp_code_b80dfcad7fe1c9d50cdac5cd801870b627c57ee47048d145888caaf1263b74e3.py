code = """import json

# Read and analyze the data
opportunity = locals()['var_functions.query_db:0'][0]
opportunity_line_items = locals()['var_functions.query_db:2']
tasks = locals()['var_functions.query_db:3']
events = locals()['var_functions.query_db:4']

# Analyze the opportunity
contract_id = opportunity['ContractID__c']
has_contract = contract_id is not None and contract_id != 'None'
has_line_items = len(opportunity_line_items) > 0
has_tasks = len(tasks) > 0

# Check tasks for negotiation indicators
negotiation_keywords = ['negotiation', 'pricing', 'terms', 'proposal', 'contract']
negotiation_activities = []
for task in tasks:
    if 'Subject' in task and task['Subject']:
        subject = task['Subject'].lower()
        description = task.get('Description', '').lower()
        if any(keyword in subject or keyword in description for keyword in negotiation_keywords):
            negotiation_activities.append(task)

has_negotiation_activities = len(negotiation_activities) > 0

# Based on CRM best practices, determine the correct stage
if has_contract:
    correct_stage = 'Closed'
elif has_negotiation_activities:
    correct_stage = 'Negotiation'
elif len(opportunity_line_items) > 0:
    # Line items exist (Quote stage), but negotiation activities suggest moving to Negotiation
    if any('negotiation' in task.get('Subject', '').lower() or 
           'Negotiation' in task.get('Subject', '') for task in tasks):
        correct_stage = 'Negotiation'
    else:
        correct_stage = 'Quote'
else:
    # Default to Qualification if insufficient activity data
    correct_stage = 'Qualification'

# Check the specific activities for this opportunity
# The tasks show: product demo, negotiation meeting, follow up on proposal
# This strongly indicates Negotiation stage
for task in tasks:
    if 'negotiation' in task.get('Subject', '').lower() or 'Negotiation' in task.get('Subject', ''):
        correct_stage = 'Negotiation'
        break
    elif 'proposal' in task.get('Subject', '').lower() or 'Proposal' in task.get('Subject', ''):
        correct_stage = 'Negotiation'  # Following up on proposal = negotiation
        break

# Return the result in the required JSON format
result_data = {"correct_stage": correct_stage}
print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.query_db:0': [{'Id': '006Wt000007BGGjIAO', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'OwnerId': '005Wt000003NIs9IAG', 'Probability': '85.0', 'Amount': '61666.225', 'StageName': 'Discovery', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'CloseDate': '2022-02-20'}], 'var_functions.query_db:2': [], 'var_functions.query_db:3': [{'Id': '00kWt000002HJTPIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hV58IAE', 'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '50.0', 'TotalPrice': '25499.575'}, {'Id': '00kWt000002HOEWIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hTUkIAM', 'PricebookEntryId': '01uWt0000027P6zIAE', 'Quantity': '30.0', 'TotalPrice': '10199.745'}, {'Id': '00kWt000002HUdKIAW', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVhpIAE', 'PricebookEntryId': '01uWt0000027P3mIAE', 'Quantity': '45.0', 'TotalPrice': '18742.1175'}], 'var_functions.query_db:4': [{'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIovIAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms'}], 'var_functions.query_db:5': []}

exec(code, env_args)
