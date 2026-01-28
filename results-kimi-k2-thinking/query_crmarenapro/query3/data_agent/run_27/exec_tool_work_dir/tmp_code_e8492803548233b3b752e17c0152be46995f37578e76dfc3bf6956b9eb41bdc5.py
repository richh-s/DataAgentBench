code = """# Analyze the stage appropriateness based on the opportunity data and tasks
import json

try:
    # Get the data from the previous queries
    opportunity = locals()['var_functions.query_db:0'][0]
    tasks = locals()['var_functions.query_db:2']
    quotes = locals()['var_functions.query_db:3']
    contracts = locals()['var_functions.query_db:4']
    
    # Extract key information
    current_stage = opportunity["StageName"]
    contract_id = opportunity["ContractID__c"]
    probability = float(opportunity["Probability"])
    
    # Check for key indicators
    has_proposal = any("proposal" in task.get("Subject", "").lower() for task in tasks)
    has_negotiation = any("negotiation" in task.get("Subject", "").lower() for task in tasks)
    has_quote = len(quotes) > 0
    has_contract = len(contracts) > 0 or contract_id != "None"
    
    # Check if proposal/negotiation tasks are completed
    proposal_completed = all(
        task.get("Status", "").strip().lower() in ["completed", "closed"]
        for task in tasks 
        if "proposal" in task.get("Subject", "").lower()
    )
    negotiation_completed = all(
        task.get("Status", "").strip().lower() in ["completed", "closed"]
        for task in tasks 
        if "negotiation" in task.get("Subject", "").lower()
    )
    
    # Determine appropriate stage based on CRM logic
    if has_contract:
        appropriate_stage = "Closed"
    elif (has_negotiation or has_proposal) and not negotiation_completed:
        appropriate_stage = "Negotiation"
    elif has_quote:
        appropriate_stage = "Quote"
    else:
        appropriate_stage = "Discovery"
    
    print("__RESULT__:")
    print(json.dumps(appropriate_stage))

except Exception as e:
    print("__RESULT__:")
    print(json.dumps(str(e)))"""

env_args = {'var_functions.query_db:0': [{'Id': '006Wt000007BGGjIAO', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'StageName': 'Discovery', 'Amount': '61666.225', 'Probability': '85.0', 'CloseDate': '2022-02-20', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'OwnerId': '005Wt000003NIs9IAG', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities."}], 'var_functions.query_db:2': [{'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'Subject': 'Organize product demo', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'Subject': 'Follow up on proposal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Description': 'Reach out to the client to address any questions and negotiate terms'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'Subject': 'Hold negotiation meeting', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Description': 'Discuss terms and finalize pricing with the client'}], 'var_functions.query_db:3': [], 'var_functions.query_db:4': []}

exec(code, env_args)
