code = """import json
# Load articles from previous call
kp2 = var_call_tdK5bpWo1LvEgouGn3bIUucc
with open(kp2, 'r') as f:
    articles = json.load(f)

# Find explicit Volume-Based Discounts article
article = next((a for a in articles if a.get('title','').strip().lower()=='volume-based discounts'), None)
article_id = article.get('id') if article else None

print('__RESULT__:')
import json
print(json.dumps(article_id))"""

env_args = {'var_call_Ys6o1gSM3k3IhVeExqTiKtLT': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_81bgoWj3L9aL5Ze2cO91vQWg': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_5zV1FMtWQx7gzTiWEyeoHw6t': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1', 'PricebookEntryId': '01uWt0000027P3lIAE', 'UnitPrice': '499.99', 'PricebookId': 'None', 'PricebookName': 'None'}], 'var_call_v2b01xTPbYREqOFGwQTj5eki': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_o0biAM7YsGTPQndoiKNefW2i': [], 'var_call_XPefcYW9zrwvRYGcx1KENl29': 'file_storage/call_XPefcYW9zrwvRYGcx1KENl29.json', 'var_call_YWPyhbekt4rWZM2PCmF1EIZF': None, 'var_call_tdK5bpWo1LvEgouGn3bIUucc': 'file_storage/call_tdK5bpWo1LvEgouGn3bIUucc.json'}

exec(code, env_args)
