code = """import json

opp = var_call_G9dDbVfiAEKar6Tij454ualn[0] if var_call_G9dDbVfiAEKar6Tij454ualn else None

tasks = var_call_Z0TJPwlcVb7944PJlEIXq0Q1 or []
quotes = var_call_RBeg9SPPUnuo3JVeSKebjQ6u or []
contracts = var_call_HPpTXreWOfDRTCO85HlMP9yq or []

stage = (opp or {}).get('StageName','')

# Heuristic mapping:
# Closed if contract signed or opp stage indicates closed.
# Negotiation if tasks mention negotiation/contract approval/proposal follow-up and no signed contract.
# Quote if there is at least one quote record.
# Discovery if demo/proposal prep/case studies.
# Qualification otherwise.

text = " ".join([(t.get('Subject','') or '') + ' ' + (t.get('Description','') or '') for t in tasks]).lower()

suggested = 'Qualification'
if contracts:
    suggested = 'Closed'
elif any(k in text for k in ['negotiat', 'contract', 'finalize pricing', 'terms']):
    suggested = 'Negotiation'
elif quotes:
    suggested = 'Quote'
elif any(k in text for k in ['demo', 'proposal', 'case studies', 'tailored']):
    suggested = 'Discovery'

print('__RESULT__:')
print(json.dumps({'current_stage': stage, 'suggested_stage': suggested}))"""

env_args = {'var_call_G9dDbVfiAEKar6Tij454ualn': [{'Id': '006Wt000007BGGjIAO', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'StageName': 'Discovery', 'Probability': '85.0', 'Amount': '61666.225', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'CloseDate': '2022-02-20', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'ContractID__c': 'None'}], 'var_call_Z0TJPwlcVb7944PJlEIXq0Q1': [{'Id': '#00TWt000002yqGuMAI', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started', 'ActivityDate': '2022-02-20', 'Subject': 'Prepare contract for approval   ', 'Description': 'Draft the final contract for review and signature'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client'}, {'Id': '00TWt000002yytCMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NIx1IAG', 'Priority': 'Low', 'Status': 'Not Started', 'ActivityDate': '2022-01-18', 'Subject': 'Send case studies', 'Description': 'Provide case studies and testimonials to reinforce the value proposition'}, {'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIovIAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '#00TWt000002z8sLMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'Normal', 'Status': 'In Progress', 'ActivityDate': '2022-01-10', 'Subject': 'Prepare tailored proposal', 'Description': "Draft a proposal that aligns with the client's specific needs and objectives"}], 'var_call_RBeg9SPPUnuo3JVeSKebjQ6u': [], 'var_call_jkbgpt7GFFB2QLdC5eJJQBMT': [{'OpportunityLineItemId': '00kWt000002HJTPIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Quantity': '50.0', 'TotalPrice': '25499.575', 'QuoteLineItemId': 'None', 'QuoteId': 'None', 'QuoteQty': 'None', 'UnitPrice': 'None', 'Discount': 'None', 'QuoteLineTotal': 'None'}, {'OpportunityLineItemId': '00kWt000002HQ3OIAW', 'OpportunityId': '#006Wt000007BGGjIAO', 'Quantity': '25.0', 'TotalPrice': '7224.7875', 'QuoteLineItemId': 'None', 'QuoteId': 'None', 'QuoteQty': 'None', 'UnitPrice': 'None', 'Discount': 'None', 'QuoteLineTotal': 'None'}, {'OpportunityLineItemId': '00kWt000002HOEWIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Quantity': '30.0', 'TotalPrice': '10199.745', 'QuoteLineItemId': 'None', 'QuoteId': 'None', 'QuoteQty': 'None', 'UnitPrice': 'None', 'Discount': 'None', 'QuoteLineTotal': 'None'}, {'OpportunityLineItemId': '00kWt000002HUdKIAW', 'OpportunityId': '006Wt000007BGGjIAO', 'Quantity': '45.0', 'TotalPrice': '18742.1175', 'QuoteLineItemId': 'None', 'QuoteId': 'None', 'QuoteQty': 'None', 'UnitPrice': 'None', 'Discount': 'None', 'QuoteLineTotal': 'None'}], 'var_call_HPpTXreWOfDRTCO85HlMP9yq': [], 'var_call_DwZ4viAOesFmSc7oufTVCuXO': []}

exec(code, env_args)
