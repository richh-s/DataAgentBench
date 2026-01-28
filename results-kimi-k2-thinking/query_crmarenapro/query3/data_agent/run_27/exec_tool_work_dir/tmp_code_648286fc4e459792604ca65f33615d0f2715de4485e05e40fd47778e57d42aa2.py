code = """# Get the data from the previous queries
import json

# Load the opportunity data from the previous query result
opportunity_data_str = """[{"Id": "006Wt000007BGGjIAO", "Name": "DataWave Analytics AI-Driven Enhancement ", "StageName": "Discovery", "Amount": "61666.225", "Probability": "85.0", "CloseDate": "2022-02-20", "ContractID__c": "None", "AccountId": "001Wt00000PGRqjIAH", "ContactId": "#003Wt00000JqczHIAR", "OwnerId": "005Wt000003NIs9IAG", "Description": "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities."}]"""

tasks_data_str = """[{"Id": "00TWt000002ysm8MAA", "WhatId": "006Wt000007BGGjIAO", "Subject": "Organize product demo", "Status": "Not Started", "ActivityDate": "2022-01-15", "Description": "Set up a product demonstration to showcase the relevant solutions"}, {"Id": "00TWt000002yzp8MAA", "WhatId": "006Wt000007BGGjIAO", "Subject": "Follow up on proposal", "Status": "Not Started ", "ActivityDate": "2022-02-15", "Description": "Reach out to the client to address any questions and negotiate terms"}, {"Id": "00TWt000002z4fFMAQ", "WhatId": "006Wt000007BGGjIAO", "Subject": "Hold negotiation meeting", "Status": "Not Started", "ActivityDate": "2022-02-10", "Description": "Discuss terms and finalize pricing with the client"}]"""

quotes_data_str = "[]"
contracts_data_str = "[]"

# Parse the JSON strings
opportunity = json.loads(opportunity_data_str)[0]
tasks = json.loads(tasks_data_str)
quotes = json.loads(quotes_data_str)
contracts = json.loads(contracts_data_str)

# Analyze the stage appropriateness
current_stage = opportunity["StageName"]
contract_id = opportunity["ContractID__c"]
probability = float(opportunity["Probability"])
close_date = opportunity["CloseDate"]

# Check for key activities that indicate stage
has_demo_task = any("demo" in task["Subject"].lower() for task in tasks)
has_proposal_task = any("proposal" in task["Subject"].lower() for task in tasks)
has_negotiation_task = any("negotiation" in task["Subject"].lower() for task in tasks)
has_quote = len(quotes) > 0
has_contract = len(contracts) > 0 or contract_id != "None"

# Check task statuses - if key tasks are completed or not
proposal_tasks_completed = all(
    task["Status"].strip().lower() in ["completed", "closed"]
    for task in tasks 
    if "proposal" in task["Subject"].lower()
)

negotiation_tasks_completed = all(
    task["Status"].strip().lower() in ["completed", "closed"]
    for task in tasks 
    if "negotiation" in task["Subject"].lower()
)

# Determine appropriate stage
# Based on CRM best practices and the given tasks:
# - Qualification: Early stage, identifying needs, no proposal
# - Discovery: Understanding requirements, may have demo tasks
# - Quote: Proposal/quote sent, awaiting response
# - Negotiation: Actively negotiating terms, pricing
# - Closed: Final stage, either won or lost

appropriate_stage = current_stage

# If there's no contract and negotiation tasks are pending or in progress,
# the opportunity should be in Negotiation stage
if has_negotiation_task or has_proposal_task:
    if not negotiation_tasks_completed and not proposal_tasks_completed:
        appropriate_stage = "Negotiation"

# Check if we're actually past Discovery based on the tasks
if has_proposal_task and not proposal_tasks_completed:
    appropriate_stage = "Negotiation"
elif has_quote and not has_contract:
    appropriate_stage = "Quote"
elif has_demo_task and not has_proposal_task:
    appropriate_stage = "Discovery"

# Final decision based on the data
result = appropriate_stage if appropriate_stage != current_stage else current_stage

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '006Wt000007BGGjIAO', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'StageName': 'Discovery', 'Amount': '61666.225', 'Probability': '85.0', 'CloseDate': '2022-02-20', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'OwnerId': '005Wt000003NIs9IAG', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities."}], 'var_functions.query_db:2': [{'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'Subject': 'Organize product demo', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'Subject': 'Follow up on proposal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Description': 'Reach out to the client to address any questions and negotiate terms'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'Subject': 'Hold negotiation meeting', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Description': 'Discuss terms and finalize pricing with the client'}], 'var_functions.query_db:3': [], 'var_functions.query_db:4': []}

exec(code, env_args)
