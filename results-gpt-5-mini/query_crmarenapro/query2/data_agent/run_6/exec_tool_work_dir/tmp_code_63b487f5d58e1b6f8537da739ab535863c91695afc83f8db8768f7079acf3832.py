code = """import json
# var_call_qTbXKcII5Y6w6wZnKwWPhdG1 contains path to full JSON file
with open(var_call_qTbXKcII5Y6w6wZnKwWPhdG1, 'r') as f:
    knowledge = json.load(f)

# We'll create a simplified mapping of knowledge ids to titles for quick lookup
kb = {k['id']: {'title': k.get('title',''), 'faq': k.get('faq_answer__c',''), 'summary': k.get('summary','')} for k in knowledge}

# print result as JSON
print('__RESULT__:')
print(json.dumps(kb))"""

env_args = {'var_call_LtvV6QNm6OcSbcFu8sKlqZqE': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_G8theRiwNOA3qE2TtGGOEW0x': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_lS7HCxMmAq6QWYMeq2KTu5TM': [], 'var_call_I5sOXMpuQFvXTv11ONbKEv96': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_UNg7enQnQkxW9cXuXpjvfZMV': [], 'var_call_qTbXKcII5Y6w6wZnKwWPhdG1': 'file_storage/call_qTbXKcII5Y6w6wZnKwWPhdG1.json'}

exec(code, env_args)
