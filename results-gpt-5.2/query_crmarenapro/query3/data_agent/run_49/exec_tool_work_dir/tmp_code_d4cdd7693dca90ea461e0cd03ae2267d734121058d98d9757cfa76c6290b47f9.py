code = """import json, pandas as pd
opp = pd.DataFrame(var_call_FwBAOMKt01VVOER2ftSFDW8l)
tasks = pd.DataFrame(var_call_ssGz62HICF6nBRcScLx8Cvmz)
quotes = pd.DataFrame(var_call_EQl7FopYS2EcodhxDRIk0B3o)
olis = pd.DataFrame(var_call_Ydx4m018AhMVZzsN5tk1ZaFr)

stage = (opp.loc[0,'StageName'] if len(opp) else None)

def norm(s):
    if s is None: return ''
    return str(s).strip().lower()

# Determine implied stage from artifacts
has_quote = len(quotes) > 0
has_line_items = len(olis) > 0
subjects = (tasks['Subject'].map(norm).tolist() if len(tasks) else [])
descriptions = (tasks['Description'].map(norm).tolist() if len(tasks) else [])
text = ' '.join(subjects + descriptions)

implied = None
if any(k in text for k in ['contract','signature','sign','approval']):
    implied = 'Negotiation'
elif any(k in text for k in ['negotia','proposal','terms','finalize pricing']):
    implied = 'Negotiation'
elif has_quote or 'quote' in text or 'pricing' in text or 'proposal' in text or has_line_items:
    implied = 'Quote'
elif any(k in text for k in ['demo','discovery','requirements','needs','workshop']):
    implied = 'Discovery'
else:
    implied = 'Qualification'

# If close date is past and would indicate closed, but no contract/status info; keep implied.
allowed = {'Qualification','Discovery','Quote','Negotiation','Closed'}
if implied not in allowed:
    implied = stage if stage in allowed else 'Discovery'

print('__RESULT__:')
print(json.dumps({'current_stage': stage, 'implied_stage': implied}))"""

env_args = {'var_call_FwBAOMKt01VVOER2ftSFDW8l': [{'Id': '006Wt000007BGGjIAO', 'StageName': 'Discovery', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", 'Amount': '61666.225', 'Probability': '85.0', 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'CloseDate': '2022-02-20', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'OwnerId': '005Wt000003NIs9IAG', 'ContractID__c': 'None'}], 'var_call_ssGz62HICF6nBRcScLx8Cvmz': [{'Id': '#00TWt000002yqGuMAI', 'WhatId': '#006Wt000007BGGjIAO', 'Subject': 'Prepare contract for approval   ', 'Status': 'Not Started', 'Priority': 'Normal', 'ActivityDate': '2022-02-20', 'Description': 'Draft the final contract for review and signature'}, {'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'Subject': 'Organize product demo', 'Status': 'Not Started', 'Priority': 'High', 'ActivityDate': '2022-01-15', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '00TWt000002yytCMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'Subject': 'Send case studies', 'Status': 'Not Started', 'Priority': 'Low', 'ActivityDate': '2022-01-18', 'Description': 'Provide case studies and testimonials to reinforce the value proposition'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'Subject': 'Follow up on proposal', 'Status': 'Not Started ', 'Priority': 'Normal', 'ActivityDate': '2022-02-15', 'Description': 'Reach out to the client to address any questions and negotiate terms'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'Subject': 'Hold negotiation meeting', 'Status': 'Not Started', 'Priority': 'High', 'ActivityDate': '2022-02-10', 'Description': 'Discuss terms and finalize pricing with the client'}, {'Id': '#00TWt000002z8sLMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'Subject': 'Prepare tailored proposal', 'Status': 'In Progress', 'Priority': 'Normal', 'ActivityDate': '2022-01-10', 'Description': "Draft a proposal that aligns with the client's specific needs and objectives"}], 'var_call_5eU3ZamOtenYWEKrTlaULL5F': [], 'var_call_EQl7FopYS2EcodhxDRIk0B3o': [], 'var_call_Ydx4m018AhMVZzsN5tk1ZaFr': [{'Id': '00kWt000002HJTPIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hV58IAE', 'Quantity': '50.0', 'TotalPrice': '25499.575'}, {'Id': '00kWt000002HOEWIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hTUkIAM', 'Quantity': '30.0', 'TotalPrice': '10199.745'}, {'Id': '00kWt000002HQ3OIAW', 'OpportunityId': '#006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVQ5IAM', 'Quantity': '25.0', 'TotalPrice': '7224.7875'}, {'Id': '00kWt000002HUdKIAW', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVhpIAE', 'Quantity': '45.0', 'TotalPrice': '18742.1175'}], 'var_call_c6pGR5uhE1q6ZfF5YRRhWGIr': []}

exec(code, env_args)
