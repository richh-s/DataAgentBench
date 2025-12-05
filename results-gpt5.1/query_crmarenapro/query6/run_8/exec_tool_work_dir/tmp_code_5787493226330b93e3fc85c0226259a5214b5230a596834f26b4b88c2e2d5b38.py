code = """import json, pandas as pd
from pathlib import Path

# Load knowledge articles
data_path = Path(var_call_pYjD2ndR2ZBxYhMDKDQN4dpB)
records = json.loads(data_path.read_text())

# For this task, we need to see if any article explicitly mentions invalid configurations, pricing, discount, or quantity rules.
df = pd.DataFrame(records)
mask = df['faq_answer__c'].str.contains('discount|quantity|pricing|price book|pricebook|quote|configuration|config|bundle|over|under', case=False, na=False)
subset = df[mask][['id','title','summary']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(subset))"""

env_args = {'var_call_A0M4zsfxO4NxqiuYMo14xPyE': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_cEhnKQaRElQu7ylwynTr1mJY': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_pYjD2ndR2ZBxYhMDKDQN4dpB': 'file_storage/call_pYjD2ndR2ZBxYhMDKDQN4dpB.json'}

exec(code, env_args)
