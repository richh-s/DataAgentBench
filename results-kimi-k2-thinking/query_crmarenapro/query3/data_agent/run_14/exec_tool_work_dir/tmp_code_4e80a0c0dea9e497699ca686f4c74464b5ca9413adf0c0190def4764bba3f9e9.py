code = """import json

# Based on the analysis of the opportunity data:
# Current stage: Discovery
# Tasks observed:
# 1. "Organize product demo" - typically Discovery/early stage activity
# 2. "Follow up on proposal" - indicates Quote stage activity  
# 3. "Hold negotiation meeting" - indicates Negotiation stage activity
# Probability: 85% (high, typical for Negotiation stage)
# CloseDate: 2022-02-20 (approaching)
# No actual quotes found in the system

# The presence of negotiation tasks with high probability suggests
# the opportunity is in Negotiation stage, not Discovery.

result = "Negotiation"

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '006Wt000007BGGjIAO', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'StageName': 'Discovery', 'Amount': '61666.225', 'Probability': '85.0', 'CloseDate': '2022-02-20', 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'OwnerId': '005Wt000003NIs9IAG'}], 'var_functions.query_db:2': [{'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIovIAG', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Priority': 'High'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NF9WIAW', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Priority': 'Normal'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Priority': 'High'}], 'var_functions.query_db:6': []}

exec(code, env_args)
