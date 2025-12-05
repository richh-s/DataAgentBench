code = """import json
import pandas as pd

kavs = var_call_F0aAmS5KZZUfCHGAcetFxQlu

if isinstance(kavs, str) and kavs.endswith('.json'):
    with open(kavs, 'r') as f:
        kavs = json.load(f)

kavs_df = pd.DataFrame(kavs)

invalid_keywords = ['discount', 'volume', 'minimum quantity', 'max quantity', 'maximum quantity', 'tiered pricing', 'bulk', 'installation timeline', 'promotion', 'promo', 'bundle', 'bundling', 'up to', 'over ', 'per unit']

text_cols = ['title', 'summary']

mask = False
for col in text_cols:
    if col in kavs_df.columns:
        col_mask = pd.Series([False]*len(kavs_df))
        vals = kavs_df[col].fillna('').str.lower()
        for kw in invalid_keywords:
            col_mask |= vals.str.contains(kw)
        mask |= col_mask

candidates = kavs_df[mask]

result_id = None
if not candidates.empty:
    exact = candidates[candidates['title'].str.contains('volume-based discounts', case=False, na=False)]
    if not exact.empty:
        result_id = exact.iloc[0]['id']
    else:
        result_id = candidates.iloc[0]['id']

result = result_id

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_j28zUQsd8CZh7wvgOgtmhLhs': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_o55JsuqE1WQZlwVdWp4EzEG0': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_F0aAmS5KZZUfCHGAcetFxQlu': 'file_storage/call_F0aAmS5KZZUfCHGAcetFxQlu.json'}

exec(code, env_args)
