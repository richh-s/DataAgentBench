code = """import json
# load the large knowledge articles result from previous query
path = var_call_8P4KS4JhjE0bTleGQs4ItcTe
with open(path, 'r') as f:
    ka = json.load(f)

# also load quote and quote line items
quote = var_call_CixNNtyUNnGlz1woqXSQtuD9[0]
qlis = var_call_Owp5zChdcZtk2NVTIOAYofJT
products = var_call_khXhpaRiw1YXHbxileX5oaDI
pbe = var_call_f2tuB7UDTl0VgfMwEqIz6vOO

# compute totals
import decimal
total = decimal.Decimal('0')
for q in qlis:
    total += decimal.Decimal(str(q['TotalPrice']))

# find knowledge articles that mention discount, volume, installation, price, setup
keywords = ['discount','volume','installation','install','price','pricing','setup','cost']
matches = []
for item in ka:
    txt = (item.get('title','') + ' ' + item.get('summary','') + ' ' + item.get('faq_answer__c','') if item.get('faq_answer__c') else '')
    txtlow = txt.lower()
    for kw in keywords:
        if kw in txtlow:
            matches.append({'id': item.get('id'), 'title': item.get('title'), 'summary': item.get('summary')})
            break

result = {
    'quote_id': quote['Id'],
    'quote_total': float(total),
    'quote_lines_count': len(qlis),
    'products_found': products,
    'pricebook_entries': pbe,
    'matching_knowledge_articles': matches
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_v8g0XtE5dGQ8ODABW2lWgceM': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_Owp5zChdcZtk2NVTIOAYofJT': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_khXhpaRiw1YXHbxileX5oaDI': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1'}], 'var_call_f2tuB7UDTl0VgfMwEqIz6vOO': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_CixNNtyUNnGlz1woqXSQtuD9': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_8P4KS4JhjE0bTleGQs4ItcTe': 'file_storage/call_8P4KS4JhjE0bTleGQs4ItcTe.json'}

exec(code, env_args)
