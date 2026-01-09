code = """import json, pandas as pd

o = pd.DataFrame(var_call_bv6X33Tr2W7Td0k9OtpvKZGw)
tasks = pd.DataFrame(var_call_rNKeapzWyug6070PkgZLrkV3)
quotes = pd.DataFrame(var_call_dZH3aL3NBmwisEe4VjYc828W)
olis = pd.DataFrame(var_call_PWlvNjPndUpQqYlhoIo9PCRe)
contracts = pd.DataFrame(var_call_wkTOh45Q4tbksC9o4GV80zgG)

stage = (o.loc[0,'StageName'] if len(o) else None)

has_quote = len(quotes) > 0
has_line_items = len(olis) > 0
has_contract = len(contracts) > 0

# infer from tasks subjects/descriptions
text = ' '.join((tasks.get('Subject',pd.Series(dtype=str)).fillna('') + ' ' + tasks.get('Description',pd.Series(dtype=str)).fillna('')).astype(str).tolist()).lower()

negotiation_signals = any(k in text for k in ['negotiat', 'finalize pricing', 'terms'])
quote_signals = any(k in text for k in ['proposal', 'quote', 'pricing'])
discovery_signals = any(k in text for k in ['demo', 'discovery', 'requirements', 'case studies'])
contract_signals = any(k in text for k in ['contract', 'signature', 'sign'])

# Determine appropriate stage label
if has_contract:
    inferred = 'Closed'
elif contract_signals and (negotiation_signals or quote_signals):
    inferred = 'Negotiation'
elif negotiation_signals:
    inferred = 'Negotiation'
elif has_quote or quote_signals:
    inferred = 'Quote'
elif discovery_signals or has_line_items:
    # line items suggest scoping but could be quote prep; still earlier than quote without quote record
    inferred = 'Discovery'
else:
    inferred = 'Qualification'

print('__RESULT__:')
print(json.dumps({'current_stage': stage, 'inferred_stage': inferred}))"""

env_args = {'var_call_bv6X33Tr2W7Td0k9OtpvKZGw': [{'Id': '006Wt000007BGGjIAO', 'StageName': 'Discovery', 'Probability': '85.0', 'Amount': '61666.225', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'CloseDate': '2022-02-20', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'OwnerId': '005Wt000003NIs9IAG', 'ContractID__c': 'None'}], 'var_call_rNKeapzWyug6070PkgZLrkV3': [{'Id': '#00TWt000002yqGuMAI', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started', 'ActivityDate': '2022-02-20', 'Subject': 'Prepare contract for approval   ', 'Description': 'Draft the final contract for review and signature'}, {'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIovIAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '00TWt000002yytCMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NIx1IAG', 'Priority': 'Low', 'Status': 'Not Started', 'ActivityDate': '2022-01-18', 'Subject': 'Send case studies', 'Description': 'Provide case studies and testimonials to reinforce the value proposition'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client'}, {'Id': '#00TWt000002z8sLMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'Normal', 'Status': 'In Progress', 'ActivityDate': '2022-01-10', 'Subject': 'Prepare tailored proposal', 'Description': "Draft a proposal that aligns with the client's specific needs and objectives"}], 'var_call_dZH3aL3NBmwisEe4VjYc828W': [], 'var_call_PWlvNjPndUpQqYlhoIo9PCRe': [{'Id': '00kWt000002HJTPIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hV58IAE', 'Quantity': '50.0', 'TotalPrice': '25499.575'}, {'Id': '00kWt000002HOEWIA4', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hTUkIAM', 'Quantity': '30.0', 'TotalPrice': '10199.745'}, {'Id': '00kWt000002HQ3OIAW', 'OpportunityId': '#006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVQ5IAM', 'Quantity': '25.0', 'TotalPrice': '7224.7875'}, {'Id': '00kWt000002HUdKIAW', 'OpportunityId': '006Wt000007BGGjIAO', 'Product2Id': '01tWt000006hVhpIAE', 'Quantity': '45.0', 'TotalPrice': '18742.1175'}], 'var_call_wkTOh45Q4tbksC9o4GV80zgG': [], 'var_call_pPoSWTrXkDuppFfFRjXgGqPx': []}

exec(code, env_args)
