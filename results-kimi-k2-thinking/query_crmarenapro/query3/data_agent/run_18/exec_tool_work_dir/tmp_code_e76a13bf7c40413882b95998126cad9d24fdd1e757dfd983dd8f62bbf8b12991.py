code = """import json

# Parse opportunity data
opp = {"Id": "006Wt000007BGGjIAO", "Name": "DataWave Analytics AI-Driven Enhancement ", "StageName": "Discovery", "Amount": "61666.225", "CloseDate": "2022-02-20", "Probability": "85.0"}

# Key indicators based on the data retrieved
current_stage = opp.get('StageName')
probability = float(opp.get('Probability', 0))

# Based on the query results we saw:
# 1. Tasks include: product demo, proposal follow-up, negotiation meeting
# 2. Line items present (3 items)
# 3. No quotes found
# 4. No contract signed
# 5. Probability is 85% (very high)
# 6. Close date is approaching/has passed (2022-02-20)

# Analyze what stage this should be:
# - Probability 85% suggests late stage
# - Negotiation task exists
# - No quote created yet is unusual for this probability
# - Product demo and proposal follow-up tasks exist

# CRM best practices: Negotiation stage typically has:
# - Terms being discussed
# - Pricing being finalized
# - High probability (70%+)

# Given the negotiation task exists and probability is 85%,
# the appropriate stage should likely be Negotiation, not Discovery

print("__RESULT__:")
print(json.dumps({
    'current_stage': current_stage,
    'probability': probability,
    'has_negotiation_task': True,  # "Hold negotiation meeting" task exists
    'has_line_items': True,  # 3 line items found
    'has_quotes': False,  # No quotes created
    'has_contract': False,  # No contract signed
    'recommended_stage': 'Negotiation'
}))"""

env_args = {'var_functions.query_db:0': [{'Id': '006Wt000007BGGjIAO', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'StageName': 'Discovery', 'Amount': '61666.225', 'CloseDate': '2022-02-20', 'Probability': '85.0'}], 'var_functions.query_db:2': [{'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIovIAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client'}], 'var_functions.query_db:3': [], 'var_functions.query_db:4': [], 'var_functions.query_db:5': [{'Id': '00kWt000002HJTPIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hV58IAE', 'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '50.0', 'TotalPrice': '25499.575'}, {'Id': '00kWt000002HOEWIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hTUkIAM', 'PricebookEntryId': '01uWt0000027P6zIAE', 'Quantity': '30.0', 'TotalPrice': '10199.745'}, {'Id': '00kWt000002HUdKIAW', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVhpIAE', 'PricebookEntryId': '01uWt0000027P3mIAE', 'Quantity': '45.0', 'TotalPrice': '18742.1175'}], 'var_functions.query_db:6': [], 'var_functions.execute_python:16': {'opp_data': [{'Id': '006Wt000007BGGjIAO', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'StageName': 'Discovery', 'Amount': '61666.225', 'CloseDate': '2022-02-20', 'Probability': '85.0'}], 'has_tasks': False, 'has_events': True, 'has_quotes': True, 'has_line_items': True, 'has_contract': True}}

exec(code, env_args)
