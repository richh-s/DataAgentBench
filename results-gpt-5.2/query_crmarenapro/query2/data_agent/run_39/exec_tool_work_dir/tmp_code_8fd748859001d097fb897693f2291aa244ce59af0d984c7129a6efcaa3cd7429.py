code = """import json, pandas as pd

def load(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

quote = pd.DataFrame(load(var_call_J8U2OHCcltUztFOmG2XbU9y1))
qli = pd.DataFrame(load(var_call_KlMWaXtY8ExTyYz4Tb3fvveh))
kb = pd.DataFrame(load(var_call_5gtnCQaIjB3rBKqRtkMpMZEi))

# If there is no explicit company policy KB about quote discounts/setup, we cannot assert a violation.
# Heuristic: search KB titles/summaries/answers for pricing/discount/setup/quote approval policy keywords.
text_cols = ['title','summary','faq_answer__c','urlname']
for c in text_cols:
    if c in kb.columns:
        kb[c] = kb[c].fillna('').astype(str)

pattern = r"(?i)\b(quote|pricing|price|discount|setup|implementation|professional\s+services|ps\b|approval|margin|list\s+price)\b"
mask = False
for c in ['title','summary','faq_answer__c']:
    if c in kb.columns:
        mask = mask | kb[c].str.contains(pattern, regex=True)

kb_relevant = kb[mask].copy()

# Determine if quote has any unusual setup cost fields (none in schema) or discount levels.
# We'll consider a possible policy violation only if a relevant KB exists AND the quote exceeds constraints stated there.
# Since we cannot parse constraints reliably without a specific KB, default to None.
violation_id = None

# Minimal attempt: if any KB explicitly mentions a max discount like 'maximum discount' and the quote line discounts exceed it.
# Extract max discount percentage if mentioned in KB.
import re
max_discounts = []
for _, row in kb_relevant.iterrows():
    text = ' '.join([row.get('title',''), row.get('summary',''), row.get('faq_answer__c','')])
    m = re.search(r"(?i)(max(?:imum)?\s+discount|discount\s+cap)\s*(?:is|=|:)\s*(\d{1,2}(?:\.\d+)?)\s*%", text)
    if m:
        try:
            max_discounts.append((row['id'], float(m.group(2))))
        except:
            pass

if max_discounts and not qli.empty and 'Discount' in qli.columns:
    qli['Discount'] = pd.to_numeric(qli['Discount'], errors='coerce')
    max_line_disc = float(qli['Discount'].max())
    # choose strictest cap
    cap_id, cap = sorted(max_discounts, key=lambda x: x[1])[0]
    if pd.notna(max_line_disc) and max_line_disc > cap:
        violation_id = cap_id

out = json.dumps(violation_id)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_J8U2OHCcltUztFOmG2XbU9y1': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_KlMWaXtY8ExTyYz4Tb3fvveh': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_5gtnCQaIjB3rBKqRtkMpMZEi': 'file_storage/call_5gtnCQaIjB3rBKqRtkMpMZEi.json', 'var_call_Uv6DfIRFrrnBrO0qz099OOMC': 'file_storage/call_Uv6DfIRFrrnBrO0qz099OOMC.json', 'var_call_Tu3KKzAZWgwAQSgicwW5VBKM': 'file_storage/call_Tu3KKzAZWgwAQSgicwW5VBKM.json', 'var_call_tDUYAydYNVhrhGDApApDQiJ8': 'file_storage/call_tDUYAydYNVhrhGDApApDQiJ8.json', 'var_call_UIGdjfMOTZ3NnJO1PzGYfYeS': 'file_storage/call_UIGdjfMOTZ3NnJO1PzGYfYeS.json'}

exec(code, env_args)
