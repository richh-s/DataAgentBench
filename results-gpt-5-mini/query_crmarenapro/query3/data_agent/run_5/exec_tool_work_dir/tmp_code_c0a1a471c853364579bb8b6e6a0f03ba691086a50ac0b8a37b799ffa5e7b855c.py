code = """import json
import pandas as pd
# Access the stored query results
opportunity = pd.DataFrame(var_call_Pa11nXHUF9WTEqzONjxmDWTG)
tasks = pd.DataFrame(var_call_NIZj4FMPjpGETuTb4qujlu8e)

# Normalize text fields to handle trailing whitespace and leading #
if not opportunity.empty:
    opportunity['StageName_norm'] = opportunity['StageName'].astype(str).str.strip()
else:
    opportunity['StageName_norm'] = []

# Combine task subjects and descriptions
tasks_text = []
if not tasks.empty:
    for _, row in tasks.iterrows():
        subj = (row.get('Subject') or '')
        desc = (row.get('Description') or '')
        combined = f"{str(subj).strip()} {str(desc).strip()}".lower()
        tasks_text.append(combined)

# Define keyword mapping to stages
stage_keywords = {
    'Qualification': ['qualif', 'lead', 'identify', 'discovery call', 'initial contact'],
    'Discovery': ['demo', 'discover', 'discovery', 'send case studies', 'requirements', 'evaluate', 'product demo'],
    'Quote': ['proposal', 'quote', 'prepare proposal', 'tailored proposal', 'pricing', 'price quote', 'provide quote', 'proposal'],
    'Negotiation': ['negotiat', 'contract', 'finalize', 'hold negotiation', 'approve', 'approval', 'follow up on proposal', 'sign', 'contract for approval'],
    'Closed': ['closed', 'won', 'lost', 'cancelled', 'signed']
}

# Scoring
scores = {k: 0 for k in stage_keywords}
for text in tasks_text:
    for stage, keywords in stage_keywords.items():
        for kw in keywords:
            if kw in text:
                scores[stage] += 1

# Also consider current stage
current_stage = None
if not opportunity.empty:
    current_stage = opportunity.loc[0, 'StageName_norm']

# Decide stage: prefer highest score; tie-breaker use current stage if present
predicted_stage = None
if any(v > 0 for v in scores.values()):
    # pick stage with max score
    predicted_stage = max(scores.items(), key=lambda x: (x[1], x[0]))[0]
else:
    # fallback to current stage or Discovery
    predicted_stage = current_stage if current_stage in stage_keywords else 'Discovery'

# Ensure predicted stage is one of allowed labels
allowed = ['Qualification', 'Discovery', 'Quote', 'Negotiation', 'Closed']
if predicted_stage not in allowed:
    # map possible matches
    if predicted_stage == 'Quote':
        pass
    else:
        predicted_stage = 'Discovery'

# Print result in required format as JSON string
print("__RESULT__:")
print(json.dumps(predicted_stage))"""

env_args = {'var_call_Pa11nXHUF9WTEqzONjxmDWTG': [{'Id': '006Wt000007BGGjIAO', 'StageName': 'Discovery', 'Name': 'DataWave Analytics AI-Driven Enhancement ', 'Description': "DataWave Analytics seeks to enhance its data science services with TechPulse's AI-driven tools. By integrating CloudLink Designer, OptiPower Max, and CircuitSync Pro, they aim to boost efficiency and innovation in data processing. TechPulse's SecureFlow Suite offers them state-of-the-art security and compliance capabilities.", 'Amount': '61666.225', 'Probability': '85.0', 'AccountId': '001Wt00000PGRqjIAH', 'ContactId': '#003Wt00000JqczHIAR', 'OwnerId': '005Wt000003NIs9IAG', 'CreatedDate': '2021-11-15T10:25:30.000+0000', 'CloseDate': '2022-02-20'}], 'var_call_NIZj4FMPjpGETuTb4qujlu8e': [{'Id': '#00TWt000002yqGuMAI', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started', 'ActivityDate': '2022-02-20', 'Subject': 'Prepare contract for approval   ', 'Description': 'Draft the final contract for review and signature'}, {'Id': '00TWt000002ysm8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIovIAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-01-15', 'Subject': 'Organize product demo', 'Description': 'Set up a product demonstration to showcase the relevant solutions'}, {'Id': '00TWt000002yytCMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NIx1IAG', 'Priority': 'Low', 'Status': 'Not Started', 'ActivityDate': '2022-01-18', 'Subject': 'Send case studies', 'Description': 'Provide case studies and testimonials to reinforce the value proposition'}, {'Id': '00TWt000002yzp8MAA', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '005Wt000003NF9WIAW', 'Priority': 'Normal', 'Status': 'Not Started ', 'ActivityDate': '2022-02-15', 'Subject': 'Follow up on proposal', 'Description': 'Reach out to the client to address any questions and negotiate terms'}, {'Id': '00TWt000002z4fFMAQ', 'WhatId': '006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'High', 'Status': 'Not Started', 'ActivityDate': '2022-02-10', 'Subject': 'Hold negotiation meeting', 'Description': 'Discuss terms and finalize pricing with the client'}, {'Id': '#00TWt000002z8sLMAQ', 'WhatId': '#006Wt000007BGGjIAO', 'OwnerId': '#005Wt000003NIc1IAG', 'Priority': 'Normal', 'Status': 'In Progress', 'ActivityDate': '2022-01-10', 'Subject': 'Prepare tailored proposal', 'Description': "Draft a proposal that aligns with the client's specific needs and objectives"}]}

exec(code, env_args)
