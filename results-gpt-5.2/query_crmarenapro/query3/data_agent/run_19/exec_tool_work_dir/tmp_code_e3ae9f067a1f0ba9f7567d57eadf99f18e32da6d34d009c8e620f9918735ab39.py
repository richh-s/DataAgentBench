code = """import json
import pandas as pd

o = pd.DataFrame(var_call_mBvakiktaRwRFCdKIBR0pytK)
tasks = pd.DataFrame(var_call_P5skYH0zJ8QIjcwTMzLMKOyK)
quotes = pd.DataFrame(var_call_TDggOPskPjQqffWKtB0uFykK)
contracts = pd.DataFrame(var_call_ZndyESPG4B1F3kfAAn13xxlB)

stage = (o['StageName'].iloc[0] if len(o) else '').strip()

# Infer appropriate stage from evidence
has_quote = len(quotes) > 0
has_contract = len(contracts) > 0

subjects = ' '.join(tasks['Subject'].fillna('') + ' ' + tasks['Description'].fillna('')) if len(tasks) else ''
subjects_l = subjects.lower()

in_negotiation = any(k in subjects_l for k in ['negot', 'proposal', 'finalize pricing', 'terms'])
in_quote = any(k in subjects_l for k in ['quote', 'proposal'])
in_discovery = any(k in subjects_l for k in ['demo', 'case studies', 'needs', 'discovery'])

if has_contract:
    inferred = 'Closed'
elif 'contract' in subjects_l and 'approval' in subjects_l:
    inferred = 'Negotiation'
elif in_negotiation:
    inferred = 'Negotiation'
elif has_quote or in_quote:
    inferred = 'Quote'
elif in_discovery:
    inferred = 'Discovery'
else:
    inferred = 'Qualification'

print('__RESULT__:')
print(json.dumps({'current_stage': stage, 'inferred_stage': inferred}))"""

env_args = {'var_call_mBvakiktaRwRFCdKIBR0pytK': [{'Id': '006Wt000007BGGjIAO', 'StageName': 'Discovery', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", 'Amount': '61666.225', 'Probability': '85.0', 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'CloseDate': '2022-02-20', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'OwnerId': '005Wt000003NIs9IAG'}], 'var_call_P5skYH0zJ8QIjcwTMzLMKOyK': [{'Id': '#00TWt000002yqGuMAI', 'WhatId': '#006Wt000007BGGjIAO', 'Status': 'Not Started', 'ActivityDate': '2022-02-20', 'Subject': 'Prepare contract for approval   ', 'Description': 'Draft the final contract for review and signature', 'Priority': 'Normal', 'OwnerId': '#005Wt000003NF9WIAW'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms', 'Priority': 'Normal', 'OwnerId': '005Wt000003NF9WIAW'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client', 'Priority': 'High', 'OwnerId': '#005Wt000003NIc1IAG'}, {'Id': '00TWt000002yytCMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'Status': 'Not Started', 'ActivityDate': '2022-01-18', 'Subject': 'Send case studies', 'Description': 'Provide case studies and testimonials to reinforce the value proposition', 'Priority': 'Low', 'OwnerId': '005Wt000003NIx1IAG'}, {'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions', 'Priority': 'High', 'OwnerId': '#005Wt000003NIovIAG'}, {'Id': '#00TWt000002z8sLMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'Status': 'In Progress', 'ActivityDate': '2022-01-10', 'Subject': 'Prepare tailored proposal', 'Description': "Draft a proposal that aligns with the client's specific needs and objectives", 'Priority': 'Normal', 'OwnerId': '#005Wt000003NIc1IAG'}], 'var_call_8LdXAjEelaqh5CKQyWSqUDA3': [], 'var_call_TDggOPskPjQqffWKtB0uFykK': [], 'var_call_6fesjKY4SXxzpy7dQlG2CM2F': [{'Id': '00kWt000002HJTPIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hV58IAE', 'Quantity': '50.0', 'TotalPrice': '25499.575'}, {'Id': '00kWt000002HOEWIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hTUkIAM', 'Quantity': '30.0', 'TotalPrice': '10199.745'}, {'Id': '00kWt000002HQ3OIAW', 'OpportunityId': '#006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVQ5IAM', 'Quantity': '25.0', 'TotalPrice': '7224.7875'}, {'Id': '00kWt000002HUdKIAW', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVhpIAE', 'Quantity': '45.0', 'TotalPrice': '18742.1175'}], 'var_call_ZndyESPG4B1F3kfAAn13xxlB': []}

exec(code, env_args)
