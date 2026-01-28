code = """import json, pandas as pd
opps = var_call_Af1LEn20xYdn5lTi85d8oWwx
tasks = var_call_a0N2tqzPKdwNLF50Ww9NLhbY
quotes = var_call_164lpGG76DbIQ3X4WD26XQqE
contracts = var_call_CaYjgHdiwzj6Pauu44jz1g6t

stage = (opps[0].get('StageName') or '').strip() if opps else ''

# Determine appropriate stage based on artifacts/tasks
has_quote = len(quotes) > 0
has_contract = len(contracts) > 0

def norm(s):
    return (s or '').strip().lower()

subjects = ' | '.join([norm(t.get('Subject')) for t in tasks])

action_negotiation = any(k in subjects for k in ['negotiat', 'proposal', 'contract', 'approval', 'terms', 'pricing'])
action_discovery = any(k in subjects for k in ['demo', 'discovery', 'requirements', 'needs'])

# Heuristic mapping to requested labels
if has_contract:
    recommended = 'Closed'
elif has_quote:
    recommended = 'Quote'
elif action_negotiation:
    recommended = 'Negotiation'
elif action_discovery:
    recommended = 'Discovery'
else:
    recommended = 'Qualification'

# If stage already later than recommended? we just output correct stage representing tasks
result = recommended

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Af1LEn20xYdn5lTi85d8oWwx': [{'Id': '006Wt000007BGGjIAO', 'StageName': 'Discovery', 'Probability': '85.0', 'Amount': '61666.225', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'CloseDate': '2022-02-20', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'OwnerId': '005Wt000003NIs9IAG', 'ContractID__c': 'None'}], 'var_call_a0N2tqzPKdwNLF50Ww9NLhbY': [{'Id': '#00TWt000002yqGuMAI', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started', 'ActivityDate': '2022-02-20', 'Subject': 'Prepare contract for approval   ', 'Description': 'Draft the final contract for review and signature'}, {'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIovIAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '00TWt000002yytCMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NIx1IAG', 'Priority': 'Low', 'Status': 'Not Started', 'ActivityDate': '2022-01-18', 'Subject': 'Send case studies', 'Description': 'Provide case studies and testimonials to reinforce the value proposition'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client'}, {'Id': '#00TWt000002z8sLMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'Normal', 'Status': 'In Progress', 'ActivityDate': '2022-01-10', 'Subject': 'Prepare tailored proposal', 'Description': "Draft a proposal that aligns with the client's specific needs and objectives"}], 'var_call_gm935saiohGXjIW7EUGASG0x': [], 'var_call_164lpGG76DbIQ3X4WD26XQqE': [], 'var_call_wtF5EiW6FjO93hVa4Onj5uYG': [{'Id': '00kWt000002HJTPIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hV58IAE', 'Quantity': '50.0', 'TotalPrice': '25499.575'}, {'Id': '00kWt000002HOEWIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hTUkIAM', 'Quantity': '30.0', 'TotalPrice': '10199.745'}, {'Id': '00kWt000002HQ3OIAW', 'OpportunityId': '#006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVQ5IAM', 'Quantity': '25.0', 'TotalPrice': '7224.7875'}, {'Id': '00kWt000002HUdKIAW', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVhpIAE', 'Quantity': '45.0', 'TotalPrice': '18742.1175'}], 'var_call_CaYjgHdiwzj6Pauu44jz1g6t': []}

exec(code, env_args)
