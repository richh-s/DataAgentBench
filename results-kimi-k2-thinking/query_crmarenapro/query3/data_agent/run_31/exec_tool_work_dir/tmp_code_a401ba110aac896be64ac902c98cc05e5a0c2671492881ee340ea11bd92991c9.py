code = """var_functions.query_db:0 = locals()['var_functions.query_db:0']
var_functions.query_db:2 = locals()['var_functions.query_db:2']
var_functions.query_db:5 = locals()['var_functions.query_db:5']
var_functions.query_db:6 = locals()['var_functions.query_db:6']

print('__RESULT__:')
print({'opportunity_stage': var_functions.query_db:0[0]['StageName'] if var_functions.query_db:0 else None, 
        'quotes_exist': len(var_functions.query_db:2) > 0,
        'contracts_exist': len(var_functions.query_db:6) > 0, 
        'negotiation_tasks': len([t for t in var_functions.query_db:5 if 'negotiation' in t['Subject'].lower() or 'negotiate' in t['Description'].lower()])})"""

env_args = {'var_functions.query_db:0': [{'Id': '006Wt000007BGGjIAO', 'ContractID__c': 'None', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'OwnerId': '005Wt000003NIs9IAG', 'Probability': '85.0', 'Amount': '61666.225', 'StageName': 'Discovery', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'CloseDate': '2022-02-20'}], 'var_functions.query_db:2': [], 'var_functions.query_db:5': [{'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIovIAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client'}], 'var_functions.query_db:6': []}

exec(code, env_args)
