code = """oppty = var_functions.query_db:0
tasks = var_functions.query_db:2
quotes = var_functions.query_db:5

print(f"Opportunity: {oppty[0]['Name']}")
print(f"Current Stage: {oppty[0]['StageName']}")
print(f"Probability: {oppty[0]['Probability']}")
print()

print("TASKS:")
for task in tasks:
    print(f"- {task['Subject']} ({task['Status']})")

print()
print("QUOTES:")
print(f"Number of quotes found: {len(quotes)}")
print()

proposal_prep = False
negotiation = False
contract_prep = False

for task in tasks:
    subject = task['Subject'].lower()
    status = task['Status'].lower()
    
    if 'proposal' in subject and status == 'in progress':
        proposal_prep = True
    if 'negotiation' in subject:
        negotiation = True
    if 'contract' in subject:
        contract_prep = True

print("ANALYSIS:")
print(f"Proposal being prepared (In Progress): {proposal_prep}")
print(f"Negotiation meeting scheduled: {negotiation}")
print(f"Contract preparation mentioned: {contract_prep}")
print(f"Quotes in system: {len(quotes) > 0}")
print()

print("STAGE ASSESSMENT:")
print("Current stage 'Discovery' is NOT accurate.")
print("Tasks indicate proposal preparation is underway and negotiations have begun.")
print("No quotes in system, but negotiation activities present.")
print()

result = "Negotiation"
print("__RESULT__:")
print(result)"""

env_args = {'var_functions.query_db:0': [{'Id': '006Wt000007BGGjIAO', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'OwnerId': '005Wt000003NIs9IAG', 'Probability': '85.0', 'Amount': '61666.225', 'StageName': 'Discovery', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'CloseDate': '2022-02-20'}], 'var_functions.query_db:2': [{'Id': '#00TWt000002yqGuMAI', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started', 'ActivityDate': '2022-02-20', 'Subject': 'Prepare contract for approval   ', 'Description': 'Draft the final contract for review and signature'}, {'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIovIAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '00TWt000002yytCMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NIx1IAG', 'Priority': 'Low', 'Status': 'Not Started', 'ActivityDate': '2022-01-18', 'Subject': 'Send case studies', 'Description': 'Provide case studies and testimonials to reinforce the value proposition'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client'}, {'Id': '#00TWt000002z8sLMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'Normal', 'Status': 'In Progress', 'ActivityDate': '2022-01-10', 'Subject': 'Prepare tailored proposal', 'Description': "Draft a proposal that aligns with the client's specific needs and objectives"}], 'var_functions.query_db:5': []}

exec(code, env_args)
