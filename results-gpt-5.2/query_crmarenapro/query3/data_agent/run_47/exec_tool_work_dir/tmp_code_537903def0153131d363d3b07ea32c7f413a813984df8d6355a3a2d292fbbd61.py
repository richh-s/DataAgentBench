code = """import json

opp = var_call_IVlOIAo1zHixshm1916P8VCM[0] if var_call_IVlOIAo1zHixshm1916P8VCM else {}
stage = (opp.get('StageName') or '').strip()

tasks = var_call_6MDhW8NCjGzIGYM3dPygzWTX or []
quotes = var_call_n1v2BPCdYs2puMwrNJofARG1 or []
contract_id = (opp.get('ContractID__c') or '').strip()

# Heuristic mapping based on evidence:
# - If contract exists/signed => Closed
# - If negotiation/contract prep tasks exist => Negotiation
# - If quotes exist or proposal tasks exist => Quote
# - If demo/discovery tasks exist => Discovery
# - Else Qualification

subjects = ' '.join([(t.get('Subject') or '') for t in tasks]).lower()
descs = ' '.join([(t.get('Description') or '') for t in tasks]).lower()
text = subjects + ' ' + descs

has_contract_prep = ('contract' in text) or ('signature' in text) or ('sign' in text)
has_negotiation = ('negotiat' in text) or ('terms' in text) or ('finalize pricing' in text)
has_proposal = ('proposal' in text) or ('quote' in text)
has_demo = ('demo' in text) or ('discovery' in text) or ('case studies' in text)

if contract_id and contract_id.lower() != 'none':
    inferred = 'Closed'
elif has_negotiation or has_contract_prep:
    inferred = 'Negotiation'
elif quotes or has_proposal:
    inferred = 'Quote'
elif has_demo:
    inferred = 'Discovery'
else:
    inferred = 'Qualification'

print('__RESULT__:')
print(json.dumps({'current_stage': stage, 'inferred_stage': inferred}))"""

env_args = {'var_call_IVlOIAo1zHixshm1916P8VCM': [{'Id': '006Wt000007BGGjIAO', 'StageName': 'Discovery', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", 'Probability': '85.0', 'Amount': '61666.225', 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'CloseDate': '2022-02-20', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'OwnerId': '005Wt000003NIs9IAG', 'ContractID__c': 'None'}], 'var_call_6MDhW8NCjGzIGYM3dPygzWTX': [{'Id': '#00TWt000002yqGuMAI', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started', 'ActivityDate': '2022-02-20', 'Subject': 'Prepare contract for approval   ', 'Description': 'Draft the final contract for review and signature'}, {'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIovIAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '00TWt000002yytCMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NIx1IAG', 'Priority': 'Low', 'Status': 'Not Started', 'ActivityDate': '2022-01-18', 'Subject': 'Send case studies', 'Description': 'Provide case studies and testimonials to reinforce the value proposition'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client'}, {'Id': '#00TWt000002z8sLMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'Normal', 'Status': 'In Progress', 'ActivityDate': '2022-01-10', 'Subject': 'Prepare tailored proposal', 'Description': "Draft a proposal that aligns with the client's specific needs and objectives"}], 'var_call_l0YvJnBAxbTmlLb7bzRXjT1E': [], 'var_call_n1v2BPCdYs2puMwrNJofARG1': [], 'var_call_O41T2LKYsxa4uRVK1Yc0iiim': [{'Id': '00kWt000002HJTPIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hV58IAE', 'Quantity': '50.0', 'TotalPrice': '25499.575'}, {'Id': '00kWt000002HOEWIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hTUkIAM', 'Quantity': '30.0', 'TotalPrice': '10199.745'}, {'Id': '00kWt000002HQ3OIAW', 'OpportunityId': '#006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVQ5IAM', 'Quantity': '25.0', 'TotalPrice': '7224.7875'}, {'Id': '00kWt000002HUdKIAW', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVhpIAE', 'Quantity': '45.0', 'TotalPrice': '18742.1175'}], 'var_call_RtB7BBNvIiTc79fRBCFGsl9N': [{'Id': '006Wt000007BGGjIAO', 'ContractID__c': 'None'}]}

exec(code, env_args)
