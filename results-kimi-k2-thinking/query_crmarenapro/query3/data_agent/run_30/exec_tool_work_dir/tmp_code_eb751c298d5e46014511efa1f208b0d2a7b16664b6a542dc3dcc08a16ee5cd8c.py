code = """import json

# Access the results from previous queries
opportunity_data = locals().get('var_functions.query_db:0', [])
tasks_data = locals().get('var_functions.query_db:4', [])

if not opportunity_data or not tasks_data:
    result = {'error': 'Missing data'}
else:
    # Extract current stage
    current_stage = opportunity_data[0].get('StageName', '')
    
    # Analyze task subjects and descriptions
    task_texts = []
    for task in tasks_data:
        subject = task.get('Subject', '').strip().lower()
        description = task.get('Description', '').strip().lower()
        task_texts.append(subject + ' ' + description)
    
    # Check for stage indicators
    has_proposal = any('proposal' in text for text in task_texts)
    has_quote = any('quote' in text for text in task_texts)
    has_negotiation = any('negotiation' in text or 'negotiate' in text for text in task_texts)
    has_contract = any('contract' in text for text in task_texts)
    has_demo = any('demo' in text or 'demonstration' in text for text in task_texts)
    
    # Determine appropriate stage
    if has_contract or has_negotiation:
        appropriate_stage = 'Negotiation'
    elif has_proposal or has_quote:
        appropriate_stage = 'Quote'
    elif has_demo:
        appropriate_stage = 'Discovery'
    else:
        appropriate_stage = 'Qualification'
    
    result = {
        'current_stage': current_stage,
        'appropriate_stage': appropriate_stage,
        'indicators': {
            'has_proposal': has_proposal,
            'has_negotiation': has_negotiation,
            'has_contract': has_contract,
            'has_demo': has_demo
        }
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '006Wt000007BGGjIAO', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'OwnerId': '005Wt000003NIs9IAG', 'Probability': '85.0', 'Amount': '61666.225', 'StageName': 'Discovery', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'CloseDate': '2022-02-20'}], 'var_functions.query_db:2': [], 'var_functions.query_db:4': [{'Id': '#00TWt000002yqGuMAI', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started', 'ActivityDate': '2022-02-20', 'Subject': 'Prepare contract for approval   ', 'Description': 'Draft the final contract for review and signature'}, {'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIovIAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '00TWt000002yytCMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NIx1IAG', 'Priority': 'Low', 'Status': 'Not Started', 'ActivityDate': '2022-01-18', 'Subject': 'Send case studies', 'Description': 'Provide case studies and testimonials to reinforce the value proposition'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client'}, {'Id': '#00TWt000002z8sLMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'Normal', 'Status': 'In Progress', 'ActivityDate': '2022-01-10', 'Subject': 'Prepare tailored proposal', 'Description': "Draft a proposal that aligns with the client's specific needs and objectives"}]}

exec(code, env_args)
