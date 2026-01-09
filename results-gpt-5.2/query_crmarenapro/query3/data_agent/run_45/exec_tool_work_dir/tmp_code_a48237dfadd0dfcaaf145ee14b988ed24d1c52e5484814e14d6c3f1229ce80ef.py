code = """import json
opp = var_call_lZTqRPx3x7nKSxZPktuVZ00o[0]
tasks = var_call_0Jz104Up9vgm6gdGoi9rZ3HJ
quotes = var_call_QIsJ1j3TFNE3hGOvA6eVP8To
contract_rows = var_call_XXeutxarwuxCl0RohQ3DTyD5
# Heuristic stage mapping based on evidence of process
# Closed if contract signed or opp stage closed; Negotiation if negotiation/contract-prep tasks; Quote if quotes exist or proposal sent; Discovery if demo/case studies; Qualification otherwise.
stage = opp.get('StageName','')
texts = ' '.join([(t.get('Subject') or '') + ' ' + (t.get('Description') or '') for t in tasks]).lower()
if any(k in (stage or '').lower() for k in ['closed']):
    rec = 'Closed'
elif (contract_rows and any((r.get('CustomerSignedDate') or r.get('CompanySignedDate')) for r in contract_rows)):
    rec = 'Closed'
elif ('negotiation' in texts) or ('contract' in texts) or ('approval' in texts):
    rec = 'Negotiation'
elif quotes and len(quotes)>0:
    rec = 'Quote'
elif ('proposal' in texts) or ('pricing' in texts):
    rec = 'Quote'
elif ('demo' in texts) or ('case studies' in texts) or ('requirements' in texts) or ('discovery' in texts):
    rec = 'Discovery'
else:
    rec = 'Qualification'
print('__RESULT__:')
print(json.dumps({'recommended_stage': rec, 'current_stage': stage}))"""

env_args = {'var_call_lZTqRPx3x7nKSxZPktuVZ00o': [{'Id': '006Wt000007BGGjIAO', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'StageName': 'Discovery', 'Probability': '85.0', 'Amount': '61666.225', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'CloseDate': '2022-02-20', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'ContractID__c': 'None'}], 'var_call_QIsJ1j3TFNE3hGOvA6eVP8To': [], 'var_call_0Jz104Up9vgm6gdGoi9rZ3HJ': [{'Id': '#00TWt000002yqGuMAI', 'WhatId': '#006Wt000007BGGjIAO', 'Status': 'Not Started', 'ActivityDate': '2022-02-20', 'Subject': 'Prepare contract for approval   ', 'Description': 'Draft the final contract for review and signature', 'Priority': 'Normal', 'OwnerId': '#005Wt000003NF9WIAW'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms', 'Priority': 'Normal', 'OwnerId': '005Wt000003NF9WIAW'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client', 'Priority': 'High', 'OwnerId': '#005Wt000003NIc1IAG'}, {'Id': '00TWt000002yytCMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'Status': 'Not Started', 'ActivityDate': '2022-01-18', 'Subject': 'Send case studies', 'Description': 'Provide case studies and testimonials to reinforce the value proposition', 'Priority': 'Low', 'OwnerId': '005Wt000003NIx1IAG'}, {'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions', 'Priority': 'High', 'OwnerId': '#005Wt000003NIovIAG'}, {'Id': '#00TWt000002z8sLMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'Status': 'In Progress', 'ActivityDate': '2022-01-10', 'Subject': 'Prepare tailored proposal', 'Description': "Draft a proposal that aligns with the client's specific needs and objectives", 'Priority': 'Normal', 'OwnerId': '#005Wt000003NIc1IAG'}], 'var_call_jVbNU9QbS3ZwoJ4rIR7VeI0F': [], 'var_call_cRTDaUerSU3hStnK8C4A61UL': [{'Id': '00kWt000002HJTPIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Quantity': '50.0', 'TotalPrice': '25499.575', 'Product2Id': '01tWt000006hV58IAE', 'PricebookEntryId': '01uWt0000027P5NIAU'}, {'Id': '00kWt000002HOEWIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Quantity': '30.0', 'TotalPrice': '10199.745', 'Product2Id': '01tWt000006hTUkIAM', 'PricebookEntryId': '01uWt0000027P6zIAE'}, {'Id': '00kWt000002HQ3OIAW', 'OpportunityId': '#006Wt000007BGGjIAO', 'Quantity': '25.0', 'TotalPrice': '7224.7875', 'Product2Id': '01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2'}, {'Id': '00kWt000002HUdKIAW', 'OpportunityId': '006Wt000007BGGjIAO', 'Quantity': '45.0', 'TotalPrice': '18742.1175', 'Product2Id': '01tWt000006hVhpIAE', 'PricebookEntryId': '01uWt0000027P3mIAE'}], 'var_call_0vk9AD2V6lqxsXMMJTBnA6eQ': [], 'var_call_XXeutxarwuxCl0RohQ3DTyD5': []}

exec(code, env_args)
