code = """import json, pandas as pd

opp = pd.DataFrame(var_call_8vOTKbv64faYw947zPisxBhi)
tasks = pd.DataFrame(var_call_txl6g1JkjAxkA4cQmT1AwYPV)
quotes = pd.DataFrame(var_call_NGzWM426Gf2ARkwclLxqXt2T)
contracts = pd.DataFrame(var_call_7PqrDSjp74aomzm5WSrcomkP)

stage = opp.loc[0,'StageName'] if len(opp) else None

# Determine appropriate stage from evidence
has_quote = len(quotes) > 0
has_contract = len(contracts) > 0

# task subject/description cues
text = ''
if len(tasks):
    text = ' '.join((tasks.get('Subject',pd.Series(dtype=str)).fillna('') + ' ' + tasks.get('Description',pd.Series(dtype=str)).fillna('')).astype(str).tolist()).lower()

has_negotiation = ('negot' in text) or ('finalize pricing' in text) or ('proposal' in text) or ('contract' in text)
# More granular
has_contract_prep = 'contract' in text
has_demo_discovery = ('demo' in text) or ('discovery' in text)

# map to label
if has_contract:
    proposed = 'Closed'
elif has_quote:
    proposed = 'Quote'
elif ('negot' in text) or ('negotiation meeting' in text) or ('finalize pricing' in text):
    proposed = 'Negotiation'
elif ('proposal' in text) or ('follow up on proposal' in text):
    # without explicit negotiation, treat as Quote stage typically; but no quote records -> Negotiation/Quote? choose Negotiation if proposal follow-up and negotiation tasks exist
    proposed = 'Negotiation' if ('negot' in text) else 'Discovery'
elif has_demo_discovery:
    proposed = 'Discovery'
else:
    proposed = 'Qualification'

# If current stage matches proposed, keep; else output proposed
out = proposed
print('__RESULT__:')
print(json.dumps({'current_stage': stage, 'proposed_stage': out}))"""

env_args = {'var_call_8vOTKbv64faYw947zPisxBhi': [{'Id': '006Wt000007BGGjIAO', 'StageName': 'Discovery', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", 'Probability': '85.0', 'Amount': '61666.225', 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'CloseDate': '2022-02-20', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'OwnerId': '005Wt000003NIs9IAG', 'ContractID__c': 'None'}], 'var_call_txl6g1JkjAxkA4cQmT1AwYPV': [{'Id': '#00TWt000002yqGuMAI', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started', 'ActivityDate': '2022-02-20', 'Subject': 'Prepare contract for approval   ', 'Description': 'Draft the final contract for review and signature'}, {'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIovIAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '00TWt000002yytCMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NIx1IAG', 'Priority': 'Low', 'Status': 'Not Started', 'ActivityDate': '2022-01-18', 'Subject': 'Send case studies', 'Description': 'Provide case studies and testimonials to reinforce the value proposition'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client'}, {'Id': '#00TWt000002z8sLMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'Normal', 'Status': 'In Progress', 'ActivityDate': '2022-01-10', 'Subject': 'Prepare tailored proposal', 'Description': "Draft a proposal that aligns with the client's specific needs and objectives"}], 'var_call_VxnfQqsBg0iF5XK7IwVOcEKc': [], 'var_call_NGzWM426Gf2ARkwclLxqXt2T': [], 'var_call_I5p1daMbMaxHSNxMWBfVYLz4': [{'Id': '00kWt000002HJTPIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hV58IAE', 'Quantity': '50.0', 'TotalPrice': '25499.575'}, {'Id': '00kWt000002HOEWIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hTUkIAM', 'Quantity': '30.0', 'TotalPrice': '10199.745'}, {'Id': '00kWt000002HQ3OIAW', 'OpportunityId': '#006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVQ5IAM', 'Quantity': '25.0', 'TotalPrice': '7224.7875'}, {'Id': '00kWt000002HUdKIAW', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVhpIAE', 'Quantity': '45.0', 'TotalPrice': '18742.1175'}], 'var_call_7PqrDSjp74aomzm5WSrcomkP': []}

exec(code, env_args)
