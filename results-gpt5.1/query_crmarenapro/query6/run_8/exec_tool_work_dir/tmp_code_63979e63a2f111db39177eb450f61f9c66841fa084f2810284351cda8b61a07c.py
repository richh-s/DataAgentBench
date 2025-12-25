code = """import json, pandas as pd
from pathlib import Path

qli = pd.DataFrame(var_call_A0M4zsfxO4NxqiuYMo14xPyE)
qli['Quantity'] = qli['Quantity'].astype(float)
qli['UnitPrice'] = qli['UnitPrice'].astype(float)
qli['Discount'] = qli['Discount'].astype(float)

# Determine potential issues: unusually high quantity, high discount, etc.
max_qty = qli['Quantity'].max()
max_discount = qli['Discount'].max()

# Load candidate knowledge subset
subset_path = Path(var_call_Uee91gGQVvy5jPKiuvegF21V)
subset = json.loads(subset_path.read_text())
ks = pd.DataFrame(subset)

# From preview, we know "Volume-Based Discounts" likely covers discount rules.
row = ks[ks['title'].str.contains('Volume-Based Discounts', case=False, na=False)].iloc[0]

print('__RESULT__:')
print(json.dumps(row['id']))"""

env_args = {'var_call_A0M4zsfxO4NxqiuYMo14xPyE': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_cEhnKQaRElQu7ylwynTr1mJY': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_pYjD2ndR2ZBxYhMDKDQN4dpB': 'file_storage/call_pYjD2ndR2ZBxYhMDKDQN4dpB.json', 'var_call_Uee91gGQVvy5jPKiuvegF21V': 'file_storage/call_Uee91gGQVvy5jPKiuvegF21V.json'}

exec(code, env_args)
