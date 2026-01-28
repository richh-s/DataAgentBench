code = """import json
# load quote line items from storage
qli = var_call_W4Un3dnKY44yTBweUPoCaifK
# load pricebook entries
pbe = var_call_4HZHCRx6d7lDbRRvXnJlEhPM
# load products
prods = var_call_WwP2dNeI5cBA7fhZC3cPDPhA

# convert numeric strings to floats
for item in qli:
    for f in ['Quantity','UnitPrice','Discount','TotalPrice']:
        try:
            item[f] = float(item[f])
        except:
            item[f] = None

# build dicts
pbe_map = {p['Id'].lstrip('#'): p for p in pbe}
prod_map = {p['Id'].lstrip('#'): p for p in prods}

# check for mismatches between unit price in QuoteLineItem and PricebookEntry.UnitPrice
violations = []
for item in qli:
    pbe_id = item['PricebookEntryId'].lstrip('#')
    pbe_rec = pbe_map.get(pbe_id)
    if not pbe_rec:
        violations.append({'QuoteLineItemId': item['Id'], 'issue': 'missing_pricebook_entry'})
        continue
    pbe_price = float(pbe_rec['UnitPrice'])
    # if quote unitprice differs from pricebook by > 0.01
    if abs(item['UnitPrice'] - pbe_price) > 0.01:
        violations.append({'QuoteLineItemId': item['Id'], 'issue': 'unitprice_mismatch', 'quote_price': item['UnitPrice'], 'pricebook_price': pbe_price})
    # check discount limits: suppose company policy max discount is 10% unless volume-based discount applies
    if item['Discount'] > 10.0:
        # check if 'volume-based discounts' article exists
        violations.append({'QuoteLineItemId': item['Id'], 'issue': 'discount_over_limit', 'discount': item['Discount']})
    # check quantity limits (assume max quantity per line is 100)
    if item['Quantity'] > 100:
        violations.append({'QuoteLineItemId': item['Id'], 'issue': 'quantity_exceeds_limit', 'quantity': item['Quantity']})

# also check large bulk discount scenario: one item has 15% discount and quantity 35 -> maybe needs volume-based discount policy

result = {'violations': violations, 'count': len(violations)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_W4Un3dnKY44yTBweUPoCaifK': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_moQKSYWtL2Ow94xUUfZGTgrd': 'file_storage/call_moQKSYWtL2Ow94xUUfZGTgrd.json', 'var_call_4HZHCRx6d7lDbRRvXnJlEhPM': [{'Id': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Pi5IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'UnitPrice': '399.99'}], 'var_call_WwP2dNeI5cBA7fhZC3cPDPhA': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE', 'External_ID__c': 'Integrated Development Environments,Educational and Training Platforms_6'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'External_ID__c': 'AI-Powered Circuit Design Tools,Customizable Workflow Automation_5'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio', 'External_ID__c': 'Cloud-Based Design Collaboration,Integrated Development Environments_30'}], 'var_call_bGkcmza4wYPC9DSN7QkyGrZo': 'file_storage/call_bGkcmza4wYPC9DSN7QkyGrZo.json', 'var_call_H7FK4CTFgp7rgjkuIi5EQQt1': [{'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'keyword': 'volume-based discount', 'excerpt': 'volume-based discounts volume-based discounts are a strategic tool for fostering customer loyalty and encouraging bulk p'}]}

exec(code, env_args)
