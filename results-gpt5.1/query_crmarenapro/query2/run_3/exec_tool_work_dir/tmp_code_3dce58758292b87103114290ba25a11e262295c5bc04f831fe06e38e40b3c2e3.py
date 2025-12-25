code = """import json, pandas as pd
from pathlib import Path

# Load full knowledge articles
path = var_call_MlUbYhsNt4q7PVZGCHwCVY8h
with open(path, 'r') as f:
    knowledge = json.load(f)

# Simple heuristic company quote policy embedded in knowledge articles text
# Look for any article that clearly mentions discount, pricing, or setup/implementation constraints
violating_ids = []

# Aggregate quote info
quote_lines = pd.DataFrame(var_call_wJmEawi3xVo4FU3VjLXm1rnB)
quote_lines['LineTotal'] = quote_lines['LineTotal'].astype(float)
quote_lines['LineDiscount'] = quote_lines['LineDiscount'].astype(float)

max_discount = quote_lines['LineDiscount'].max()

for art in knowledge:
    text = (art.get('faq_answer__c') or '') + ' ' + (art.get('summary') or '') + ' ' + (art.get('title') or '')
    lower = text.lower()
    # Policy patterns
    if 'maximum discount' in lower or 'max discount' in lower or 'discount policy' in lower or 'approval required for discounts above' in lower:
        # Very rough check: if article mentions a max discount below what we used, flag it
        # Try to find a percentage in the text
        import re
        percents = re.findall(r"(\d+)%", lower)
        if percents:
            max_allowed = max(int(p) for p in percents)
            if max_discount > max_allowed:
                violating_ids.append(art['id'])
    if 'implementation fee' in lower or 'setup fee' in lower:
        # If article requires mandatory setup/implementation fee but quote description says initial quote only for integration without fees, flag
        if 'mandatory' in lower or 'required' in lower:
            desc = ' '.join(quote_lines['QuoteDescription'].unique()).lower()
            if 'setup fee' not in desc and 'implementation fee' not in desc:
                violating_ids.append(art['id'])

violating_ids = list(dict.fromkeys(violating_ids))

result = None
if violating_ids:
    # Return just the first violating article Id
    result = violating_ids[0]

result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_Kk0fI4AstxxjgsZ0V0Q6Dir9': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_MlUbYhsNt4q7PVZGCHwCVY8h': 'file_storage/call_MlUbYhsNt4q7PVZGCHwCVY8h.json', 'var_call_wJmEawi3xVo4FU3VjLXm1rnB': [{'QuoteId': '0Q0Wt000001WSDVKA4', 'QuoteStatus': 'Needs Review', 'QuoteDescription': 'Initial quote for AI-powered EDA solutions integration', 'LineTotal': '2379.932', 'LineDiscount': '15.0', 'LineUnitPrice': '349.99', 'LineQuantity': '8.0'}, {'QuoteId': '0Q0Wt000001WSDVKA4', 'QuoteStatus': 'Needs Review', 'QuoteDescription': 'Initial quote for AI-powered EDA solutions integration', 'LineTotal': '4499.91', 'LineDiscount': '10.0', 'LineUnitPrice': '499.99', 'LineQuantity': '10.0'}, {'QuoteId': '0Q0Wt000001WSDVKA4', 'QuoteStatus': 'Needs Review', 'QuoteDescription': 'Initial quote for AI-powered EDA solutions integration', 'LineTotal': '2260.9335', 'LineDiscount': '5.0', 'LineUnitPrice': '339.99', 'LineQuantity': '7.0'}]}

exec(code, env_args)
