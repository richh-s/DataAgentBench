code = """import json, pandas as pd
quote = pd.DataFrame(var_call_eafFoscM1uhkJI4i20ugcube)[0:1].to_dict(orient='records')[0]
# Load full knowledge base
import os
with open(var_call_ZcheX1BPQunVEpmHT66WQXYY, 'r') as f:
    knowledge = json.load(f)

# Simple heuristic: look for policy-related articles mentioning quotes, pricing, discount, approval, TCO, ROI, implementation, deployment, cost.
policy_keywords = ['quote', 'pricing', 'discount', 'approval', 'cost', 'tco', 'total cost of ownership', 'roi', 'implementation', 'deployment', 'setup']

violations = []
for art in knowledge:
    text = ' '.join(str(art.get(col, '') or '') for col in ['title','faq_answer__c','summary']).lower()
    if any(k in text for k in policy_keywords):
        violations.append(art)

# We don't actually have explicit company policy texts; based on the preview, only some articles discuss cost/tco/implementation.
# Choose the most relevant policy-like one focusing on TCO/ROI/implementation complexity, as setup/cost concern.

best = None
for art in violations:
    t = (art.get('title','') or '').lower()
    if 'adaptive design solutions' in t or 'total cost of ownership' in t or 'tco' in (art.get('faq_answer__c','') or '').lower():
        best = art
        break

result = None
if best is not None:
    # Clean id leading '#'
    art_id = (best.get('id') or '').lstrip('#') or None
    result = art_id

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_eafFoscM1uhkJI4i20ugcube': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_ZcheX1BPQunVEpmHT66WQXYY': 'file_storage/call_ZcheX1BPQunVEpmHT66WQXYY.json', 'var_call_sKKjUPvwuwDL6OAwmDNF1WU2': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript']}

exec(code, env_args)
