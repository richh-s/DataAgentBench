code = """import json

opp = var_call_YIn3t1QfwHwBoxRBsqGZa1re[0]
tasks = var_call_25Nzer0HDDKfw2sb9lB0TiAk
quotes = var_call_ZNsSRhoVJQ4Krhb4kbntuGDh
contracts = var_call_EwYoB1vA6EjkPZ8MxFe1iBPh

# Determine stage from evidence
stage = None
if opp.get('StageName'):
    pass

# If any contract signed => Closed
if contracts:
    stage = 'Closed'
else:
    # If tasks indicate negotiation/contract prep and close date imminent => Negotiation
    txt = ' '.join([(t.get('Subject') or '') + ' ' + (t.get('Description') or '') for t in tasks]).lower()
    if ('negotiat' in txt) or ('contract' in txt) or ('proposal' in txt and 'follow up' in txt):
        stage = 'Negotiation'
    elif quotes:
        stage = 'Quote'
    elif tasks:
        # demo/proposal => Discovery
        stage = 'Discovery'
    else:
        stage = 'Qualification'

print('__RESULT__:')
print(json.dumps({'current_stage': opp.get('StageName'), 'recommended_stage': stage}))"""

env_args = {'var_call_YIn3t1QfwHwBoxRBsqGZa1re': [{'Id': '006Wt000007BGGjIAO', 'StageName': 'Discovery', 'Probability': '85.0', 'Amount': '61666.225', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'CloseDate': '2022-02-20', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'ContractID__c': 'None'}], 'var_call_25Nzer0HDDKfw2sb9lB0TiAk': [{'Id': '#00TWt000002yqGuMAI', 'WhatId': '#006Wt000007BGGjIAO', 'Status': 'Not Started', 'ActivityDate': '2022-02-20', 'Subject': 'Prepare contract for approval   ', 'Description': 'Draft the final contract for review and signature'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client'}, {'Id': '00TWt000002yytCMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'Status': 'Not Started', 'ActivityDate': '2022-01-18', 'Subject': 'Send case studies', 'Description': 'Provide case studies and testimonials to reinforce the value proposition'}, {'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '#00TWt000002z8sLMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'Status': 'In Progress', 'ActivityDate': '2022-01-10', 'Subject': 'Prepare tailored proposal', 'Description': "Draft a proposal that aligns with the client's specific needs and objectives"}], 'var_call_X6WugZsJvzJ9YPHtuXzMQhqy': [], 'var_call_ZNsSRhoVJQ4Krhb4kbntuGDh': [], 'var_call_EwYoB1vA6EjkPZ8MxFe1iBPh': [], 'var_call_CTmeKcuSjYhYO4zoWkDHM2Rm': [{'Id': '00kWt000002HJTPIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hV58IAE', 'Quantity': '50.0', 'TotalPrice': '25499.575'}, {'Id': '00kWt000002HOEWIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hTUkIAM', 'Quantity': '30.0', 'TotalPrice': '10199.745'}, {'Id': '00kWt000002HQ3OIAW', 'OpportunityId': '#006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVQ5IAM', 'Quantity': '25.0', 'TotalPrice': '7224.7875'}, {'Id': '00kWt000002HUdKIAW', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVhpIAE', 'Quantity': '45.0', 'TotalPrice': '18742.1175'}]}

exec(code, env_args)
