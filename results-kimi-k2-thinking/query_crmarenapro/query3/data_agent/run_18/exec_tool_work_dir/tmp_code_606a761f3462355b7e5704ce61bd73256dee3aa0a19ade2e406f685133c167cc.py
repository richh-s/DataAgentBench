code = """# Load all query results from storage
opportunity_data = locals()['var_functions.query_db:0']
tasks_data = locals()['var_functions.query_db:1']
events_data = locals()['var_functions.query_db:2']
quotes_data = locals()['var_functions.query_db:3']
line_items_data = locals()['var_functions.query_db:4']
contracts_data = locals()['var_functions.query_db:5']
contracts_by_opportunity_data = locals()['var_functions.query_db:6']

# Analyze the opportunity details
opp = opportunity_data[0] if opportunity_data else {}

# Check for key indicators of each stage
has_product_demo = any('demo' in str(task.get('Subject', '')).lower() for task in tasks_data)
has_proposal_followup = any('proposal' in str(task.get('Subject', '')).lower() for task in tasks_data)
has_negotiation = any('negotiation' in str(task.get('Subject', '')).lower() for task in tasks_data)
has_line_items = len(line_items_data) > 0
has_quotes = len(quotes_data) > 0
has_contract = len(contracts_data) > 0 or len(contracts_by_opportunity_data) > 0

# Current stage info
current_stage = opp.get('StageName', '')
probability = float(opp.get('Probability', 0))

# Analyze what stage this should be
stage_analysis = {
    'current_stage': current_stage,
    'probability': probability,
    'has_line_items': has_line_items,
    'has_quotes': has_quotes,
    'has_contract': has_contract,
    'has_product_demo': has_product_demo,
    'has_proposal_followup': has_proposal_followup,
    'has_negotiation': has_negotiation,
    'recommended_stage': ''
}

# Determine appropriate stage based on CRM best practices
if has_contract:
    stage_analysis['recommended_stage'] = 'Closed'
elif has_negotiation:
    stage_analysis['recommended_stage'] = 'Negotiation'
elif has_quotes or has_proposal_followup:
    stage_analysis['recommended_stage'] = 'Quote'
elif has_product_demo or has_line_items:
    stage_analysis['recommended_stage'] = 'Discovery'
else:
    stage_analysis['recommended_stage'] = 'Qualification'

import json
print("__RESULT__:")
print(json.dumps(stage_analysis))"""

env_args = {'var_functions.query_db:0': [{'Id': '006Wt000007BGGjIAO', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'StageName': 'Discovery', 'Amount': '61666.225', 'CloseDate': '2022-02-20', 'Probability': '85.0'}], 'var_functions.query_db:2': [{'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIovIAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client'}], 'var_functions.query_db:3': [], 'var_functions.query_db:4': [], 'var_functions.query_db:5': [{'Id': '00kWt000002HJTPIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hV58IAE', 'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '50.0', 'TotalPrice': '25499.575'}, {'Id': '00kWt000002HOEWIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hTUkIAM', 'PricebookEntryId': '01uWt0000027P6zIAE', 'Quantity': '30.0', 'TotalPrice': '10199.745'}, {'Id': '00kWt000002HUdKIAW', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVhpIAE', 'PricebookEntryId': '01uWt0000027P3mIAE', 'Quantity': '45.0', 'TotalPrice': '18742.1175'}], 'var_functions.query_db:6': []}

exec(code, env_args)
