code = """import json

def norm(s):
    if s is None:
        return ''
    return str(s).replace('#','').strip()

opp = var_call_mz2zhWIrgvtww817iBX6EyD5[0] if var_call_mz2zhWIrgvtww817iBX6EyD5 else {}
stage = (opp.get('StageName') or '').strip()

tasks = var_call_UABb3QZXlYicP9xXMUQ5Tfpw or []
subjects = ' | '.join([(t.get('Subject') or '').strip().lower() for t in tasks])

def infer_stage(stage, subjects, quotes, contracts):
    subs = subjects
    has_neg = any(k in subs for k in ['negotiat', 'follow up on proposal', 'proposal', 'contract'])
    has_quote = any(k in subs for k in ['quote', 'proposal']) or (len(quotes)>0)
    has_contract = any(k in subs for k in ['contract']) or (len(contracts)>0)
    # closed if contract signed/status indicates
    if len(contracts)>0:
        # if any signed dates present or status like Activated/Signed
        for c in contracts:
            st = (c.get('Status') or '').lower().strip()
            if c.get('CustomerSignedDate') or c.get('CompanySignedDate') or 'signed' in st or 'activated' in st:
                return 'Closed'
    # negotiation if negotiation meeting/follow up proposal/contract approval tasks exist and not closed
    if any(k in subs for k in ['negotiation', 'negotiat', 'finalize pricing', 'contract for approval', 'follow up on proposal']):
        return 'Negotiation'
    if has_quote:
        return 'Quote'
    if any(k in subs for k in ['demo', 'case studies', 'discovery']):
        return 'Discovery'
    return 'Qualification'

quotes = var_call_MkQCOFQdmHSDuUuxWTuVzO3j or []
contracts = var_call_TNzuT7vFlb3OrXxmrGIkGS7D or []

label = infer_stage(stage, subjects, quotes, contracts)
print('__RESULT__:')
print(json.dumps({'label': label}))"""

env_args = {'var_call_mz2zhWIrgvtww817iBX6EyD5': [{'Id': '006Wt000007BGGjIAO', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'StageName': 'Discovery', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", 'Probability': '85.0', 'Amount': '61666.225', 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'CloseDate': '2022-02-20', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'ContractID__c': 'None'}], 'var_call_UABb3QZXlYicP9xXMUQ5Tfpw': [{'Id': '#00TWt000002yqGuMAI', 'WhatId': '#006Wt000007BGGjIAO', 'Subject': 'Prepare contract for approval   ', 'Status': 'Not Started', 'ActivityDate': '2022-02-20', 'Description': 'Draft the final contract for review and signature', 'OwnerId': '#005Wt000003NF9WIAW'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'Subject': 'Follow up on proposal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Description': 'Reach out to the client to address any questions and negotiate terms', 'OwnerId': '005Wt000003NF9WIAW'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'Subject': 'Hold negotiation meeting', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Description': 'Discuss terms and finalize pricing with the client', 'OwnerId': '#005Wt000003NIc1IAG'}, {'Id': '00TWt000002yytCMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'Subject': 'Send case studies', 'Status': 'Not Started', 'ActivityDate': '2022-01-18', 'Description': 'Provide case studies and testimonials to reinforce the value proposition', 'OwnerId': '005Wt000003NIx1IAG'}, {'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'Subject': 'Organize product demo', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Description': 'Set up a product demonstration to showcase the relevant solutions', 'OwnerId': '#005Wt000003NIovIAG'}, {'Id': '#00TWt000002z8sLMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'Subject': 'Prepare tailored proposal', 'Status': 'In Progress', 'ActivityDate': '2022-01-10', 'Description': "Draft a proposal that aligns with the client's specific needs and objectives", 'OwnerId': '#005Wt000003NIc1IAG'}], 'var_call_Z24kpkf2MC5GDGeatas3Vy9C': [], 'var_call_MkQCOFQdmHSDuUuxWTuVzO3j': [], 'var_call_TNzuT7vFlb3OrXxmrGIkGS7D': [], 'var_call_yvAkW9m8umtNDepVrgCux7Y8': [{'Id': '00kWt000002HJTPIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hV58IAE', 'Quantity': '50.0', 'TotalPrice': '25499.575'}, {'Id': '00kWt000002HOEWIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hTUkIAM', 'Quantity': '30.0', 'TotalPrice': '10199.745'}, {'Id': '00kWt000002HQ3OIAW', 'OpportunityId': '#006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVQ5IAM', 'Quantity': '25.0', 'TotalPrice': '7224.7875'}, {'Id': '00kWt000002HUdKIAW', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVhpIAE', 'Quantity': '45.0', 'TotalPrice': '18742.1175'}]}

exec(code, env_args)
