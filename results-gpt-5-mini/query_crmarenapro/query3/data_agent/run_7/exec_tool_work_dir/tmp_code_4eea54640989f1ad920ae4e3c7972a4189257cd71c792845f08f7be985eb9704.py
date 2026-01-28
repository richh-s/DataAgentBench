code = """import json
# Access query results from storage variables
opp_records = var_call_L52MAJblIxUaJyUX1qzmlIjU
task_records = var_call_hoWF9ebsfjGVrUmd6GhsBDr5

# Extract stage name
stage = None
if opp_records and isinstance(opp_records, list):
    stage = opp_records[0].get('StageName')

# Simple rule-based decision based on task subjects/descriptions
subjects = [t.get('Subject','').strip().lower() for t in task_records]
descriptions = [t.get('Description','').strip().lower() for t in task_records]
all_text = ' '.join(subjects + descriptions)

# Determine appropriate stage
# If there are negotiation/contract keywords -> Negotiation
# Else if there are proposal/quote keywords -> Quote
# Else if discovery/demonstration keywords -> Discovery
# Else fallback to current stage
stage_decision = None
if any(k in all_text for k in ['negotiation', 'negotiate', 'terms', 'contract', 'finalize pricing', 'prepare contract']):
    stage_decision = 'Negotiation'
elif any(k in all_text for k in ['proposal', 'quote', 'prepare tailored proposal', 'follow up on proposal']):
    stage_decision = 'Quote'
elif any(k in all_text for k in ['demo', 'discover', 'discovery', 'gather', 'send case studies']):
    stage_decision = 'Discovery'
else:
    stage_decision = stage if stage in ['Qualification','Discovery','Quote','Negotiation','Closed'] else 'Discovery'

# For this opportunity, tasks include negotiation and contract preparation -> Negotiation
result_json = json.dumps(stage_decision)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_L52MAJblIxUaJyUX1qzmlIjU': [{'Id': '006Wt000007BGGjIAO', 'StageName': 'Discovery'}], 'var_call_hoWF9ebsfjGVrUmd6GhsBDr5': [{'Id': '#00TWt000002z8sLMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'Subject': 'Prepare tailored proposal', 'Description': "Draft a proposal that aligns with the client's specific needs and objectives", 'Status': 'In Progress', 'Priority': 'Normal', 'ActivityDate': '2022-01-10'}, {'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions', 'Status': 'Not Started', 'Priority': 'High', 'ActivityDate': '2022-01-15'}, {'Id': '00TWt000002yytCMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'Subject': 'Send case studies', 'Description': 'Provide case studies and testimonials to reinforce the value proposition', 'Status': 'Not Started', 'Priority': 'Low', 'ActivityDate': '2022-01-18'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client', 'Status': 'Not Started', 'Priority': 'High', 'ActivityDate': '2022-02-10'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms', 'Status': 'Not Started ', 'Priority': 'Normal', 'ActivityDate': '2022-02-15'}, {'Id': '#00TWt000002yqGuMAI', 'WhatId': '#006Wt000007BGGjIAO', 'Subject': 'Prepare contract for approval   ', 'Description': 'Draft the final contract for review and signature', 'Status': 'Not Started', 'Priority': 'Normal', 'ActivityDate': '2022-02-20'}]}

exec(code, env_args)
