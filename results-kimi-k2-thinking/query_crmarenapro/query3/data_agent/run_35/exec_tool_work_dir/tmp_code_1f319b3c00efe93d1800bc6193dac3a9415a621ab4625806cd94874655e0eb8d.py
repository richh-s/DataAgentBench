code = """import json

# Read and analyze the data
opportunity = locals()['var_functions.query_db:0'][0]
line_items = locals()['var_functions.query_db:2']
quotes = locals()['var_functions.query_db:3']  # Note: this returned the line items, not quotes
# Actually var_functions.query_db:3 returned quotes, var_functions.query_db:2 returned line items

# Let's correct this based on the query order:
# Query 2 (var_functions.query_db:4) was Quote query - but returned []
# Query 3 (var_functions.query_db:2) was OpportunityLineItem - returned 3 items
# Query 4 (var_functions.query_db:3) was Task - returned 3 tasks

opportunity_line_items = locals()['var_functions.query_db:2']
tasks = locals()['var_functions.query_db:3']
quotes = locals()['var_functions.query_db:4']

# Analyze the data
has_line_items = len(opportunity_line_items) > 0
has_tasks = len(tasks) > 0
has_quotes = len(quotes) > 0  # This appears to be empty based on the results

# Check for contract
contract_id = opportunity['ContractID__c']
has_contract = contract_id is not None and contract_id != 'None'

# Check tasks for negotiation indicators
negotiation_keywords = ['negotiation', 'pricing', 'terms', 'proposal', 'contract', 'follow up']
negotiation_activities = []
for task in tasks:
    if 'Subject' in task:
        subject = task['Subject'].lower()
        description = task.get('Description', '').lower()
        if any(keyword in subject or keyword in description for keyword in negotiation_keywords):
            negotiation_activities.append(task)

has_negotiation_activities = len(negotiation_activities) > 0

# Determine correct stage based on CRM best practices
if has_contract:
    correct_stage = 'Closed'
elif has_negotiation_activities:
    correct_stage = 'Negotiation'
elif has_line_items:
    # With line items (products configured) and negotiation activities starting
    correct_stage = 'Negotiation'
elif has_tasks:
    # Some tasks exist but no negotiation yet, likely Discovery or Quote
    if any('demo' in task.get('Subject', '').lower() for task in tasks):
        correct_stage = 'Discovery'
    else:
        correct_stage = 'Qualification'
else:
    correct_stage = 'Qualification'

# Print the final answer
print('__RESULT__:')
print(correct_stage)"""

env_args = {'var_functions.query_db:0': [{'Id': '006Wt000007BGGjIAO', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'OwnerId': '005Wt000003NIs9IAG', 'Probability': '85.0', 'Amount': '61666.225', 'StageName': 'Discovery', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'CloseDate': '2022-02-20'}], 'var_functions.query_db:2': [], 'var_functions.query_db:3': [{'Id': '00kWt000002HJTPIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hV58IAE', 'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '50.0', 'TotalPrice': '25499.575'}, {'Id': '00kWt000002HOEWIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hTUkIAM', 'PricebookEntryId': '01uWt0000027P6zIAE', 'Quantity': '30.0', 'TotalPrice': '10199.745'}, {'Id': '00kWt000002HUdKIAW', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVhpIAE', 'PricebookEntryId': '01uWt0000027P3mIAE', 'Quantity': '45.0', 'TotalPrice': '18742.1175'}], 'var_functions.query_db:4': [{'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIovIAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms'}], 'var_functions.query_db:5': []}

exec(code, env_args)
