code = """import json, pandas as pd

quote = pd.DataFrame(var_call_0a5cYhpKHH1RuSLTa9dLA239)
qli = pd.DataFrame(var_call_0InQWawH7CUyvLZbxofq9mYu)

# load knowledge
ka_src = var_call_dIQKyp7o7UKCJuOdScIrC324
if isinstance(ka_src, str) and ka_src.endswith('.json'):
    import pathlib
    ka = pd.read_json(ka_src)
else:
    ka = pd.DataFrame(ka_src)

quote_desc = (quote.loc[0,'Description'] if len(quote)>0 else '') or ''

# identify setup cost and cost issues
# Policy heuristic: Setup costs must be explicitly itemized as a separate line item OR included in description.
# Here we only have product line items; check if any product name includes 'setup'/'implementation'/'onboarding'
# but we don't have product names; infer from description.
has_setup_mentioned = any(k in quote_desc.lower() for k in ['setup','implementation','onboarding','integration fee','professional services','ps'])

# discount policy heuristic: discounts >10% require approval; quote status needs review but that's OK.
# We'll check max discount > 10.
max_discount = None
if len(qli)>0 and 'Discount' in qli.columns:
    disc = pd.to_numeric(qli['Discount'], errors='coerce')
    if disc.notna().any():
        max_discount = float(disc.max())

violation_theme = None
if not has_setup_mentioned:
    violation_theme = 'setup'
elif max_discount is not None and max_discount > 10:
    violation_theme = 'discount'

violated_id = None
if violation_theme is not None and len(ka)>0:
    text = (ka['title'].fillna('') + ' ' + ka['summary'].fillna('') + ' ' + ka['faq_answer__c'].fillna('')).str.lower()
    if violation_theme == 'setup':
        mask = text.str.contains('setup') | text.str.contains('implementation') | text.str.contains('onboarding') | text.str.contains('professional services') | text.str.contains('integration fee')
    else:
        mask = text.str.contains('discount') | text.str.contains('pricing') | text.str.contains('approval')
    cand = ka.loc[mask, ['id','title']]
    if len(cand)>0:
        violated_id = str(cand.iloc[0]['id']).replace(' ','')

out = violated_id if violated_id not in [None,'', 'nan'] else None
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0a5cYhpKHH1RuSLTa9dLA239': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_0InQWawH7CUyvLZbxofq9mYu': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_dIQKyp7o7UKCJuOdScIrC324': 'file_storage/call_dIQKyp7o7UKCJuOdScIrC324.json'}

exec(code, env_args)
