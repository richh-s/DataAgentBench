code = """import json

o = var_call_yl2TPQSHU3xU3i5D6MxitDtf[0] if var_call_yl2TPQSHU3xU3i5D6MxitDtf else {}
tasks = var_call_3VdhpCeAuh57gt6wEmu07KdN or []
quotes = var_call_Rd8OWqJwJJ6W4MqD0krCRJWf or []
contract = var_call_hiveffTOERh5EQhJMYsvsvFX or []

stage = (o.get('StageName') or '').strip()

# Heuristic stage selection based on artifacts
has_negotiation = any('negotiat' in ((t.get('Subject') or '') + ' ' + (t.get('Description') or '')).lower() for t in tasks)
has_proposal = any('proposal' in ((t.get('Subject') or '') + ' ' + (t.get('Description') or '')).lower() for t in tasks)
has_contract_prep = any('contract' in ((t.get('Subject') or '') + ' ' + (t.get('Description') or '')).lower() for t in tasks)
has_quote = len(quotes) > 0
has_signed_contract = False
if contract:
    c = contract[0]
    # consider signed if either signed date present or status indicates activated/signed
    status = (c.get('Status') or '').lower()
    has_signed_contract = bool(c.get('CustomerSignedDate') or c.get('CompanySignedDate') or ('signed' in status) or ('activated' in status))

# Determine best stage label among given
if has_signed_contract:
    correct = 'Closed'
elif has_contract_prep or has_negotiation:
    correct = 'Negotiation'
elif has_quote or has_proposal:
    correct = 'Quote'
else:
    # default earlier funnel
    correct = 'Discovery' if stage in ('Discovery','Qualification') else 'Discovery'

print('__RESULT__:')
print(json.dumps({'current_stage': stage, 'recommended_stage': correct}))"""

env_args = {'var_call_yl2TPQSHU3xU3i5D6MxitDtf': [{'Id': '006Wt000007BGGjIAO', 'StageName': 'Discovery', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", 'Probability': '85.0', 'Amount': '61666.225', 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'CloseDate': '2022-02-20', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'OwnerId': '005Wt000003NIs9IAG', 'ContractID__c': 'None'}], 'var_call_3VdhpCeAuh57gt6wEmu07KdN': [{'Id': '#00TWt000002yqGuMAI', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started', 'ActivityDate': '2022-02-20', 'Subject': 'Prepare contract for approval   ', 'Description': 'Draft the final contract for review and signature'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client'}, {'Id': '00TWt000002yytCMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NIx1IAG', 'Priority': 'Low', 'Status': 'Not Started', 'ActivityDate': '2022-01-18', 'Subject': 'Send case studies', 'Description': 'Provide case studies and testimonials to reinforce the value proposition'}, {'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIovIAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '#00TWt000002z8sLMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'Normal', 'Status': 'In Progress', 'ActivityDate': '2022-01-10', 'Subject': 'Prepare tailored proposal', 'Description': "Draft a proposal that aligns with the client's specific needs and objectives"}], 'var_call_GdwIHKilVC1QJhWlm8SFLY3d': [], 'var_call_Rd8OWqJwJJ6W4MqD0krCRJWf': [], 'var_call_Up1wuERsnk2LlLDPPQ96nJxY': [{'Id': '00kWt000002HJTPIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hV58IAE', 'Quantity': '50.0', 'TotalPrice': '25499.575'}, {'Id': '00kWt000002HOEWIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hTUkIAM', 'Quantity': '30.0', 'TotalPrice': '10199.745'}, {'Id': '00kWt000002HQ3OIAW', 'OpportunityId': '#006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVQ5IAM', 'Quantity': '25.0', 'TotalPrice': '7224.7875'}, {'Id': '00kWt000002HUdKIAW', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVhpIAE', 'Quantity': '45.0', 'TotalPrice': '18742.1175'}], 'var_call_hiveffTOERh5EQhJMYsvsvFX': []}

exec(code, env_args)
