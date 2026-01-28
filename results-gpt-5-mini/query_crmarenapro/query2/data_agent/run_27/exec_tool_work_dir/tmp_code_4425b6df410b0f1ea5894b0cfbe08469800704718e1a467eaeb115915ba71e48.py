code = """import json
# Load the full knowledge articles result stored in var_call_r427tJH2UUG6spraPEx84FUh
path = var_call_r427tJH2UUG6spraPEx84FUh
with open(path, 'r') as f:
    kav = json.load(f)

# Create searchable list of articles with id, title, faq_answer__c, summary
articles = kav

# Search for keywords that indicate pricing/discount/approval policies
keywords = ['discount', 'approval', 'approve', 'approval required', 'requires approval', 'max', 'maximum', 'price', 'pricing', 'setup', 'setup fee', 'approval threshold', 'discounts']
found = []
for a in articles:
    text = (a.get('title','') + '\n' + a.get('faq_answer__c','') + '\n' + a.get('summary','')).lower()
    for kw in keywords:
        if kw in text:
            found.append({'id': a.get('id'), 'title': a.get('title'), 'matched_keyword': kw, 'snippet': text[text.find(kw):text.find(kw)+200]})
            break

# Also print counts and some matches
result = {'num_articles': len(articles), 'matches': found[:50]}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_MRXhSV5cBB5Z87GKEQPWRvyJ': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_2vH5O33YIJIwJ17Ui8IzRKdf': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_r427tJH2UUG6spraPEx84FUh': 'file_storage/call_r427tJH2UUG6spraPEx84FUh.json', 'var_call_OwDZaXsXAZvVZm2mDxHDSHwG': 'file_storage/call_OwDZaXsXAZvVZm2mDxHDSHwG.json', 'var_call_kinMjQe04DwWtELyrMUwvjFH': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}]}

exec(code, env_args)
