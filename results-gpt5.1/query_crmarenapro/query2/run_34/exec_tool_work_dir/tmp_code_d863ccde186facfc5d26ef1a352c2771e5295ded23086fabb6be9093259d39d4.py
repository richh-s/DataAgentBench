code = """import json
import pandas as pd

# Load full knowledge articles file
with open(var_call_9LfO5OjJDB6xNe6uQ6wBbWkA, 'r') as f:
    knowledge = json.load(f)

kdf = pd.DataFrame(knowledge)

# Simple heuristic: look for cost / discount / pricing / setup policy articles
mask = kdf['summary'].str.contains('discount', case=False, na=False) | \
       kdf['summary'].str.contains('pricing', case=False, na=False) | \
       kdf['summary'].str.contains('price ', case=False, na=False) | \
       kdf['summary'].str.contains('quote', case=False, na=False) | \
       kdf['summary'].str.contains('setup', case=False, na=False) | \
       kdf['title'].str.contains('discount', case=False, na=False) | \
       kdf['title'].str.contains('pricing', case=False, na=False) | \
       kdf['title'].str.contains('quote', case=False, na=False) | \
       kdf['title'].str.contains('setup', case=False, na=False)

candidates = kdf[mask]

result = candidates[['id','title']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_5GIGc1gXNiR4wwOQRtGtJ6xR': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_53vjzJE6M7RXBlhzFTCqbQy5': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_heIqjuRcB20iaivLPvi8HNDa': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_9LfO5OjJDB6xNe6uQ6wBbWkA': 'file_storage/call_9LfO5OjJDB6xNe6uQ6wBbWkA.json'}

exec(code, env_args)
