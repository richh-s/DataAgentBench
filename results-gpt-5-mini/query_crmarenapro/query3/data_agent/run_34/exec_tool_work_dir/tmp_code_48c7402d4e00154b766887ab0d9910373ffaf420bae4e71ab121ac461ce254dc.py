code = """import json
# Access variables from previous tool calls
op = var_call_bliqVRpixDj7qnfJoqcLhIIt
tasks = var_call_QmvOqAkdaIYfLpuF1ysRVFMi
quotes1 = var_call_hFtDuRKW01HnZMIcgDOnA7Zf
quotes2 = var_call_g359e96jtr4f7amjAap7sxPs

# Normalize strings and prepare checks
stage = None
if op and len(op) > 0:
    stage = op[0].get('StageName')

# Collect text from tasks
task_texts = []
for t in tasks:
    for field in ('Subject','Description','Status','Priority'):
        val = t.get(field)
        if val:
            task_texts.append(str(val).lower().strip())

# Collect quote existence
has_quote = False
if (quotes1 and len(quotes1) > 0) or (quotes2 and len(quotes2) > 0):
    has_quote = True

# Heuristic rules to determine correct stage
label = None
# If there are explicit negotiation-related tasks -> Negotiation
neg_keywords = ['negotiat','negotiate','finalize pricing','finalize','pricing','proposal','quote','follow up on proposal','hold negotiation']
if any(any(k in txt for k in neg_keywords) for txt in task_texts):
    label = 'Negotiation'
# If there is a quote and tasks about acceptance -> Quote or Negotiation
elif has_quote:
    label = 'Quote'
# If stage is closed or probability is 100% -> Closed
elif op and len(op) > 0:
    prob = op[0].get('Probability')
    try:
        prob_val = float(prob)
    except:
        prob_val = None
    if prob_val is not None and prob_val >= 100:
        label = 'Closed'
    else:
        # Keep existing stage if it matches allowed labels
        existing = op[0].get('StageName')
        if existing in ('Qualification','Discovery','Quote','Negotiation','Closed'):
            label = existing
        else:
            label = 'Discovery'
else:
    label = 'Discovery'

# Finalize output
result = json.dumps(label)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_bliqVRpixDj7qnfJoqcLhIIt': [{'Id': '006Wt000007BGGjIAO', 'StageName': 'Discovery', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", 'OwnerId': '005Wt000003NIs9IAG', 'Probability': '85.0', 'Amount': '61666.225', 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'CloseDate': '2022-02-20'}], 'var_call_hFtDuRKW01HnZMIcgDOnA7Zf': [], 'var_call_QmvOqAkdaIYfLpuF1ysRVFMi': [{'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIovIAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client'}], 'var_call_g359e96jtr4f7amjAap7sxPs': []}

exec(code, env_args)
