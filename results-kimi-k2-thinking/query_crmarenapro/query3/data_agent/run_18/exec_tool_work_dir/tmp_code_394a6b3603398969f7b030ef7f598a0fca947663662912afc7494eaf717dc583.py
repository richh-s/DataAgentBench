code = """# Load available data
import json

# Get specific variables
opp_data = locals()['var_functions.query_db:0']

# Check if tasks data exists
tasks_key = 'var_functions.query_db:1' if 'var_functions.query_db:1' in locals() else None
events_key = 'var_functions.query_db:2' if 'var_functions.query_db:2' in locals() else None
quotes_key = 'var_functions.query_db:3' if 'var_functions.query_db:3' in locals() else None
line_items_key = 'var_functions.query_db:4' if 'var_functions.query_db:4' in locals() else None
contract_key = 'var_functions.query_db:5' if 'var_functions.query_db:5' in locals() else None

print("__RESULT__:")
print(json.dumps({
    'opp_data': opp_data,
    'has_tasks': tasks_key is not None,
    'has_events': events_key is not None,
    'has_quotes': quotes_key is not None,
    'has_line_items': line_items_key is not None,
    'has_contract': contract_key is not None
}))"""

env_args = {'var_functions.query_db:0': [{'Id': '006Wt000007BGGjIAO', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'StageName': 'Discovery', 'Amount': '61666.225', 'CloseDate': '2022-02-20', 'Probability': '85.0'}], 'var_functions.query_db:2': [{'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIovIAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client'}], 'var_functions.query_db:3': [], 'var_functions.query_db:4': [], 'var_functions.query_db:5': [{'Id': '00kWt000002HJTPIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hV58IAE', 'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '50.0', 'TotalPrice': '25499.575'}, {'Id': '00kWt000002HOEWIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hTUkIAM', 'PricebookEntryId': '01uWt0000027P6zIAE', 'Quantity': '30.0', 'TotalPrice': '10199.745'}, {'Id': '00kWt000002HUdKIAW', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVhpIAE', 'PricebookEntryId': '01uWt0000027P3mIAE', 'Quantity': '45.0', 'TotalPrice': '18742.1175'}], 'var_functions.query_db:6': []}

exec(code, env_args)
