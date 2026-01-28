code = """import json, pandas as pd

opp = pd.DataFrame(var_call_paswVviDha4oWFF9SkOtKTu8)
tasks = pd.DataFrame(var_call_i6c0wRavAGqpBcWsnjizjTps)
quotes = pd.DataFrame(var_call_eVoFBtReXiTXGAcUbTpFbAuj)
contracts = pd.DataFrame(var_call_hZ1NK5ki3O4c5X2Eseb8peK2)

stage = (opp['StageName'].iloc[0] if len(opp) else None)

# Infer stage from artifacts/tasks
has_quote = len(quotes) > 0
has_contract = len(contracts) > 0

# Normalize text
subj = tasks['Subject'].fillna('').astype(str).str.strip().str.lower() if len(tasks) else pd.Series([], dtype=str)

def any_contains(needles):
    if len(subj)==0: return False
    return subj.apply(lambda s: any(n in s for n in needles)).any()

has_demo = any_contains(['demo'])
has_proposal = any_contains(['proposal'])
has_negotiate = any_contains(['negotiation','negotiate'])
has_contract_task = any_contains(['contract'])

# Decision
# Closed only if contract present/signed; Qualification if very early (no demo/proposal/quote); Quote if quote exists; Negotiation if negotiation/contract tasks exist
if has_contract:
    inferred = 'Closed'
elif has_quote:
    inferred = 'Quote'
elif has_negotiate or has_contract_task:
    inferred = 'Negotiation'
elif has_demo or has_proposal:
    inferred = 'Discovery'
else:
    inferred = 'Qualification'

print('__RESULT__:')
print(json.dumps({'current_stage': stage, 'inferred_stage': inferred}))"""

env_args = {'var_call_paswVviDha4oWFF9SkOtKTu8': [{'Id': '006Wt000007BGGjIAO', 'StageName': 'Discovery', 'Probability': '85.0', 'Amount': '61666.225', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'CloseDate': '2022-02-20', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'OwnerId': '005Wt000003NIs9IAG', 'ContractID__c': 'None'}], 'var_call_i6c0wRavAGqpBcWsnjizjTps': [{'Id': '#00TWt000002yqGuMAI', 'WhatId': '#006Wt000007BGGjIAO', 'Status': 'Not Started', 'ActivityDate': '2022-02-20', 'Subject': 'Prepare contract for approval   ', 'Description': 'Draft the final contract for review and signature', 'OwnerId': '#005Wt000003NF9WIAW', 'Priority': 'Normal'}, {'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions', 'OwnerId': '#005Wt000003NIovIAG', 'Priority': 'High'}, {'Id': '00TWt000002yytCMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'Status': 'Not Started', 'ActivityDate': '2022-01-18', 'Subject': 'Send case studies', 'Description': 'Provide case studies and testimonials to reinforce the value proposition', 'OwnerId': '005Wt000003NIx1IAG', 'Priority': 'Low'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms', 'OwnerId': '005Wt000003NF9WIAW', 'Priority': 'Normal'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'High'}, {'Id': '#00TWt000002z8sLMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'Status': 'In Progress', 'ActivityDate': '2022-01-10', 'Subject': 'Prepare tailored proposal', 'Description': "Draft a proposal that aligns with the client's specific needs and objectives", 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'Normal'}], 'var_call_tzjq1K4KLPTJizlrl3vxnEo8': [], 'var_call_eVoFBtReXiTXGAcUbTpFbAuj': [], 'var_call_KVgIewiilTLwSaNuulcRhMD7': [{'Id': '00kWt000002HJTPIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hV58IAE', 'Quantity': '50.0', 'TotalPrice': '25499.575'}, {'Id': '00kWt000002HOEWIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hTUkIAM', 'Quantity': '30.0', 'TotalPrice': '10199.745'}, {'Id': '00kWt000002HQ3OIAW', 'OpportunityId': '#006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVQ5IAM', 'Quantity': '25.0', 'TotalPrice': '7224.7875'}, {'Id': '00kWt000002HUdKIAW', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVhpIAE', 'Quantity': '45.0', 'TotalPrice': '18742.1175'}], 'var_call_hZ1NK5ki3O4c5X2Eseb8peK2': []}

exec(code, env_args)
