code = """import json, pandas as pd
opp = var_call_qarLmEOqCabJsKKBZmSHPQ3H[0]
tasks = pd.DataFrame(var_call_g1CaPLQMDtL4ggBIoADm16VE)
quotes = var_call_EDXvZxlkCP24jDdaOksmc9Om
contracts = var_call_dEb7mEGHqYdwl0nPJuRLCEQ0

def norm(s):
    return (str(s) if s is not None else '').strip().lower()

# Determine stage from evidence:
# Closed if contract signed OR tasks indicate closed-won (none here)
closed = False
if contracts:
    closed = True

# Negotiation if negotiation/contract preparation tasks exist and not closed
subjects = tasks['Subject'].astype(str).tolist() if not tasks.empty else []
descs = tasks['Description'].astype(str).tolist() if not tasks.empty else []
text = ' '.join(subjects + descs).lower()
neg = any(k in text for k in ['negotiat', 'contract', 'approval', 'finalize pricing', 'terms'])
quote_present = len(quotes) > 0 or ('proposal' in text)

def inferred_stage():
    if closed:
        return 'Closed'
    if neg and quote_present:
        return 'Negotiation'
    if quote_present:
        return 'Quote'
    if any(k in text for k in ['demo', 'discovery', 'needs', 'requirement', 'case studies']):
        return 'Discovery'
    return 'Qualification'

stage = inferred_stage()
print('__RESULT__:')
print(json.dumps({'current_stage': opp['StageName'], 'inferred_stage': stage, 'evidence_text': text[:500]}))"""

env_args = {'var_call_qarLmEOqCabJsKKBZmSHPQ3H': [{'Id': '006Wt000007BGGjIAO', 'StageName': 'Discovery', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", 'Probability': '85.0', 'Amount': '61666.225', 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'CloseDate': '2022-02-20', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'OwnerId': '005Wt000003NIs9IAG', 'ContractID__c': 'None'}], 'var_call_g1CaPLQMDtL4ggBIoADm16VE': [{'Id': '#00TWt000002yqGuMAI', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started', 'ActivityDate': '2022-02-20', 'Subject': 'Prepare contract for approval   ', 'Description': 'Draft the final contract for review and signature'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client'}, {'Id': '00TWt000002yytCMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NIx1IAG', 'Priority': 'Low', 'Status': 'Not Started', 'ActivityDate': '2022-01-18', 'Subject': 'Send case studies', 'Description': 'Provide case studies and testimonials to reinforce the value proposition'}, {'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIovIAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '#00TWt000002z8sLMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'Normal', 'Status': 'In Progress', 'ActivityDate': '2022-01-10', 'Subject': 'Prepare tailored proposal', 'Description': "Draft a proposal that aligns with the client's specific needs and objectives"}], 'var_call_z6hxJjPqfxvjA1HydFKZburL': [], 'var_call_EDXvZxlkCP24jDdaOksmc9Om': [], 'var_call_ck0Efy0QKmdEJNMfA3a72EWl': [{'Id': '00kWt000002HJTPIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hV58IAE', 'Quantity': '50.0', 'TotalPrice': '25499.575'}, {'Id': '00kWt000002HOEWIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hTUkIAM', 'Quantity': '30.0', 'TotalPrice': '10199.745'}, {'Id': '00kWt000002HQ3OIAW', 'OpportunityId': '#006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVQ5IAM', 'Quantity': '25.0', 'TotalPrice': '7224.7875'}, {'Id': '00kWt000002HUdKIAW', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVhpIAE', 'Quantity': '45.0', 'TotalPrice': '18742.1175'}], 'var_call_dEb7mEGHqYdwl0nPJuRLCEQ0': []}

exec(code, env_args)
