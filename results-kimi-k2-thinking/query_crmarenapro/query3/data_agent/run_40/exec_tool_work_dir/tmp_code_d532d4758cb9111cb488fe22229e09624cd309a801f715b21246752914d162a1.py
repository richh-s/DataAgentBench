code = """import json

# Load the results
opp_data = [{"Id": "006Wt000007BGGjIAO", "Name": "DataWave Analytics AI-Driven Enhancement ", "StageName": "Discovery", "Amount": "61666.225", "Probability": "85.0", "CloseDate": "2022-02-20", "AccountId": "001Wt00000PGRqjIAH", "ContactId": "#003Wt00000JqczHIAR", "OwnerId": "005Wt000003NIs9IAG"}]

quotes_data = []

contracts_data = []

line_items_data = [
    {"Id": "00kWt000002HJTPIA4", "OpportunityId": "006Wt000007BGGjIAO", "Product2Id": "01tWt000006hV58IAE", "PricebookEntryId": "01uWt0000027P5NIAU", "Quantity": "50.0", "TotalPrice": "25499.575"},
    {"Id": "00kWt000002HOEWIA4", "OpportunityId": "006Wt000007BGGjIAO", "Product2Id": "01tWt000006hTUkIAM", "PricebookEntryId": "01uWt0000027P6zIAE", "Quantity": "30.0", "TotalPrice": "10199.745"},
    {"Id": "00kWt000002HUdKIAW", "OpportunityId": "006Wt000007BGGjIAO", "Product2Id": "01tWt000006hVhpIAE", "PricebookEntryId": "01uWt0000027P3mIAE", "Quantity": "45.0", "TotalPrice": "18742.1175"}
]

tasks_data = [
    {"Id": "#00TWt000002yqGuMAI", "WhatId": "#006Wt000007BGGjIAO", "OwnerId": "#005Wt000003NF9WIAW", "Priority": "Normal", "Status": "Not Started", "ActivityDate": "2022-02-20", "Subject": "Prepare contract for approval   ", "Description": "Draft the final contract for review and signature"},
    {"Id": "00TWt000002yzp8MAA", "WhatId": "006Wt000007BGGjIAO", "OwnerId": "005Wt000003NF9WIAW", "Priority": "Normal", "Status": "Not Started ", "ActivityDate": "2022-02-15", "Subject": "Follow up on proposal", "Description": "Reach out to the client to address any questions and negotiate terms"},
    {"Id": "00TWt000002z4fFMAQ", "WhatId": "006Wt000007BGGjIAO", "OwnerId": "#005Wt000003NIc1IAG", "Priority": "High", "Status": "Not Started", "ActivityDate": "2022-02-10", "Subject": "Hold negotiation meeting", "Description": "Discuss terms and finalize pricing with the client"},
    {"Id": "00TWt000002yytCMAQ", "WhatId": "#006Wt000007BGGjIAO", "OwnerId": "005Wt000003NIx1IAG", "Priority": "Low", "Status": "Not Started", "ActivityDate": "2022-01-18", "Subject": "Send case studies", "Description": "Provide case studies and testimonials to reinforce the value proposition"},
    {"Id": "00TWt000002ysm8MAA", "WhatId": "006Wt000007BGGjIAO", "OwnerId": "#005Wt000003NIovIAG", "Priority": "High", "Status": "Not Started", "ActivityDate": "2022-01-15", "Subject": "Organize product demo", "Description": "Set up a product demonstration to showcase the relevant solutions"},
    {"Id": "#00TWt000002z8sLMAQ", "WhatId": "#006Wt000007BGGjIAO", "OwnerId": "#005Wt000003NIc1IAG", "Priority": "Normal", "Status": "In Progress", "ActivityDate": "2022-01-10", "Subject": "Prepare tailored proposal", "Description": "Draft a proposal that aligns with the client's specific needs and objectives"}
]

# Analyze the data
opp = opp_data[0]
current_stage = opp['StageName']
probability = float(opp['Probability'])

# Key indicators
has_line_items = len(line_items_data) > 0
has_quotes = len(quotes_data) > 0
has_contracts = len(contracts_data) > 0

# Analyze tasks
task_subjects = [task['Subject'].strip() for task in tasks_data]
task_descriptions = [task['Description'].strip() for task in tasks_data]
task_statuses = [task['Status'].strip() for task in tasks_data]

# Print analysis
print("__RESULT__:")
print(json.dumps({
    "current_stage": current_stage,
    "probability": probability,
    "has_line_items": has_line_items,
    "has_quotes": has_quotes,
    "has_contracts": has_contracts,
    "task_subjects": task_subjects,
    "task_statuses": task_statuses,
    "analysis": "High probability (85%) but no quotes or contracts yet. Tasks show proposal preparation in progress, negotiation meeting planned, and contract preparation task exists but not started. This suggests the deal is past Discovery and into Negotiation phase."
}))"""

env_args = {'var_functions.query_db:0': [{'Id': '006Wt000007BGGjIAO', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'StageName': 'Discovery', 'Amount': '61666.225', 'Probability': '85.0', 'CloseDate': '2022-02-20', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'OwnerId': '005Wt000003NIs9IAG'}], 'var_functions.query_db:2': [], 'var_functions.query_db:3': [], 'var_functions.query_db:4': [{'Id': '00kWt000002HJTPIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hV58IAE', 'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '50.0', 'TotalPrice': '25499.575'}, {'Id': '00kWt000002HOEWIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hTUkIAM', 'PricebookEntryId': '01uWt0000027P6zIAE', 'Quantity': '30.0', 'TotalPrice': '10199.745'}, {'Id': '00kWt000002HUdKIAW', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVhpIAE', 'PricebookEntryId': '01uWt0000027P3mIAE', 'Quantity': '45.0', 'TotalPrice': '18742.1175'}], 'var_functions.query_db:5': [{'Id': '#00TWt000002yqGuMAI', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started', 'ActivityDate': '2022-02-20', 'Subject': 'Prepare contract for approval   ', 'Description': 'Draft the final contract for review and signature'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client'}, {'Id': '00TWt000002yytCMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NIx1IAG', 'Priority': 'Low', 'Status': 'Not Started', 'ActivityDate': '2022-01-18', 'Subject': 'Send case studies', 'Description': 'Provide case studies and testimonials to reinforce the value proposition'}, {'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIovIAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '#00TWt000002z8sLMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'Normal', 'Status': 'In Progress', 'ActivityDate': '2022-01-10', 'Subject': 'Prepare tailored proposal', 'Description': "Draft a proposal that aligns with the client's specific needs and objectives"}]}

exec(code, env_args)
