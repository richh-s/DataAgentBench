code = """import json

o = var_call_aC3uqeEpJ64A98VOh6FVeuXo[0] if var_call_aC3uqeEpJ64A98VOh6FVeuXo else {}
tasks = var_call_dOQD2sSVNhn9zPfWXOwcAici
quotes = var_call_PIDpG5ULOGOQvtUpNLzpIDyY
contract = var_call_vlBa2mZ4plniDCX09ihDlseP

stage = (o.get('StageName') or '').strip()

# Heuristic: if negotiation/contract-prep tasks exist and close date matches, stage should be Negotiation unless contract signed.
subjects = ' '.join([(t.get('Subject') or '').lower() for t in tasks])
descs = ' '.join([(t.get('Description') or '').lower() for t in tasks])
text = subjects + ' ' + descs

has_negotiation = ('negotiat' in text) or ('contract' in text) or ('finalize pricing' in text) or ('approval' in text)
has_quote = len(quotes) > 0 or ('proposal' in text)
has_discovery = ('discovery' in text) or ('requirements' in text) or ('needs' in text)

if contract and any((c.get('CustomerSignedDate') or c.get('CompanySignedDate')) for c in contract):
    rec = 'Closed'
elif has_negotiation:
    rec = 'Negotiation'
elif has_quote:
    rec = 'Quote'
elif has_discovery:
    rec = 'Discovery'
else:
    rec = 'Qualification'

print('__RESULT__:')
print(json.dumps({'current_stage': stage, 'recommended_stage': rec}))"""

env_args = {'var_call_aC3uqeEpJ64A98VOh6FVeuXo': [{'Id': '006Wt000007BGGjIAO', 'StageName': 'Discovery', 'Probability': '85.0', 'Amount': '61666.225', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'CloseDate': '2022-02-20', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'ContractID__c': 'None'}], 'var_call_dOQD2sSVNhn9zPfWXOwcAici': [{'Id': '#00TWt000002yqGuMAI', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started', 'ActivityDate': '2022-02-20', 'Subject': 'Prepare contract for approval   ', 'Description': 'Draft the final contract for review and signature'}, {'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIovIAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '00TWt000002yytCMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NIx1IAG', 'Priority': 'Low', 'Status': 'Not Started', 'ActivityDate': '2022-01-18', 'Subject': 'Send case studies', 'Description': 'Provide case studies and testimonials to reinforce the value proposition'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client'}, {'Id': '#00TWt000002z8sLMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'Normal', 'Status': 'In Progress', 'ActivityDate': '2022-01-10', 'Subject': 'Prepare tailored proposal', 'Description': "Draft a proposal that aligns with the client's specific needs and objectives"}], 'var_call_yFeH6ReEMzvClACzi3QJoyIU': [], 'var_call_PIDpG5ULOGOQvtUpNLzpIDyY': [], 'var_call_Rowgm370PNkIB5KDmN9j5FSo': [{'Id': '00kWt000002HJTPIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hV58IAE', 'Quantity': '50.0', 'TotalPrice': '25499.575'}, {'Id': '00kWt000002HOEWIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hTUkIAM', 'Quantity': '30.0', 'TotalPrice': '10199.745'}, {'Id': '00kWt000002HQ3OIAW', 'OpportunityId': '#006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVQ5IAM', 'Quantity': '25.0', 'TotalPrice': '7224.7875'}, {'Id': '00kWt000002HUdKIAW', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVhpIAE', 'Quantity': '45.0', 'TotalPrice': '18742.1175'}], 'var_call_vlBa2mZ4plniDCX09ihDlseP': []}

exec(code, env_args)
