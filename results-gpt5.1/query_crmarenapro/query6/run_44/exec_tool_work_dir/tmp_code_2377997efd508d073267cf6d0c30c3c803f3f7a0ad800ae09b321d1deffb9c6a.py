code = """import json
import pandas as pd

qli = pd.DataFrame(var_call_yu6CKPIaC0NsmoBrCLJCziXF)

# Basic rule inference from data patterns; here we assume large discounted quantity may violate some rule
invalid_rows = []
for _, r in qli.iterrows():
    qty = float(r['Quantity']) if r['Quantity'] is not None else 0
    disc = float(r['Discount']) if r['Discount'] is not None else 0
    if qty >= 30 and disc >= 10:
        invalid_rows.append(r.to_dict())

# Map this assumed rule to a specific knowledge article by keyword search in titles
import os, pandas as pd
file_path = var_call_1SXVgnHiZVG4oGBwD5Rd6At0
with open(file_path, 'r') as f:
    articles = json.load(f)

ka_df = pd.DataFrame(articles)

# Naive search for discount / bulk / quantity policy articles
candidates = ka_df[ka_df['summary'].str.contains('discount', case=False, na=False) |
                   ka_df['summary'].str.contains('pricing', case=False, na=False) |
                   ka_df['summary'].str.contains('bulk', case=False, na=False)]

# Pick first candidate id as the violated article, or None
violated_id = candidates.iloc[0]['id'] if not candidates.empty and invalid_rows else None

result = json.dumps(violated_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_yu6CKPIaC0NsmoBrCLJCziXF': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_FjyOOiMXy5T5MIuP7L8aS3kV': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_1SXVgnHiZVG4oGBwD5Rd6At0': 'file_storage/call_1SXVgnHiZVG4oGBwD5Rd6At0.json'}

exec(code, env_args)
