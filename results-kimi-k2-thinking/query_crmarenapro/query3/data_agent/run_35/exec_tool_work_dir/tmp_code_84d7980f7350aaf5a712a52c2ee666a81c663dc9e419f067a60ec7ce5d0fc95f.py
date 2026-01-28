code = """# Analyze Opportunity details
opportunity = var_functions.query_db:0[0]
line_items = var_functions.query_db:2
tasks = var_functions.query_db:3
quotes = var_functions.query_db:4
events = var_functions.query_db:5

# Clean and analyze data
clean_amount = float(opportunity['Amount'].replace(',', ''))
clean_probability = float(opportunity['Probability'].replace(',', ''))
has_line_items = len(line_items) > 0
has_quotes = len(quotes) > 0
num_tasks = len(tasks)
contract_id = opportunity['ContractID__c']

# Print analysis results for debugging
print("__RESULT__:")
print("Current Stage: " + opportunity['StageName'])
print("Amount: $" + str(round(clean_amount, 2)))
print("Probability: " + str(clean_probability) + "%")
print("Close Date: " + opportunity['CloseDate'])
print("Has Line Items: " + str(has_line_items))
print("Has Quotes: " + str(has_quotes))
print("Number of Activities: " + str(num_tasks))
print("Contract ID: " + contract_id)

# Check for negotiation-related activities
negotiation_keywords = ['negotiation', 'pricing', 'terms', 'proposal', 'contract']
negotiation_activities = []
for task in tasks:
    subject = task['Subject'].lower()
    description = task.get('Description', '').lower()
    if any(keyword in subject or keyword in description for keyword in negotiation_keywords):
        negotiation_activities.append(task)

print("Negotiation Activities: " + str(len(negotiation_activities)))
for activity in negotiation_activities:
    print("  - " + activity['Subject'] + " (" + activity['ActivityDate'] + ") - " + activity['Status'])"""

env_args = {'var_functions.query_db:0': [{'Id': '006Wt000007BGGjIAO', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'OwnerId': '005Wt000003NIs9IAG', 'Probability': '85.0', 'Amount': '61666.225', 'StageName': 'Discovery', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'CloseDate': '2022-02-20'}], 'var_functions.query_db:2': [], 'var_functions.query_db:3': [{'Id': '00kWt000002HJTPIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hV58IAE', 'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '50.0', 'TotalPrice': '25499.575'}, {'Id': '00kWt000002HOEWIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hTUkIAM', 'PricebookEntryId': '01uWt0000027P6zIAE', 'Quantity': '30.0', 'TotalPrice': '10199.745'}, {'Id': '00kWt000002HUdKIAW', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVhpIAE', 'PricebookEntryId': '01uWt0000027P3mIAE', 'Quantity': '45.0', 'TotalPrice': '18742.1175'}], 'var_functions.query_db:4': [{'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIovIAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms'}], 'var_functions.query_db:5': []}

exec(code, env_args)
