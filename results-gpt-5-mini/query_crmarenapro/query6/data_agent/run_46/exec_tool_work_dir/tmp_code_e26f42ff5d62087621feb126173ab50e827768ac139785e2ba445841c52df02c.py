code = """import json
# load the knowledge articles result from var_call_mo4R0OOuWr34mvRux0hRahOA
path = var_call_mo4R0OOuWr34mvRux0hRahOA
with open(path, 'r') as f:
    ka = json.load(f)

# filter articles likely relevant to invalid config: look for titles about discounts, pricing, volume, pricebook, discount policy, quantity limits
keywords = ['discount','price','volume','pricebook','quantity','discounts','pricing','pricebook','UnitPrice','discount policy','minimum quantity']
relevant = []
for a in ka:
    title = (a.get('title') or '').lower()
    summary = (a.get('summary') or '').lower()
    if any(k in title or k in summary for k in keywords):
        relevant.append({'id':a.get('id'),'title':a.get('title'),'summary':a.get('summary')})

# print results
print("__RESULT__:")
print(json.dumps(relevant))"""

env_args = {'var_call_bzH9wjEFTS6ii2hhuYzXD1KS': [], 'var_call_SI3ERZc6ParkU17Bt2Xy70Eo': [{'Id': '#0Q0Wt000001WRAzKAO', 'Name': 'NeoGreen EDA Expansion Quote', 'AccountId': '001Wt00000PHVsDIAX', 'Status': 'Needs Review'}], 'var_call_jfEUkoH7QckUOwDxFeNKpfWL': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_PjPsiOaXcoz7OxsjVyAzp894': [{'Product2Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'IsActive': '1', 'PricebookEntryId': '01uWt0000027P8cIAE', 'UnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ'}, {'Product2Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio', 'IsActive': '1', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'UnitPrice': '399.99', 'Pricebook2Id': '#01sWt000000imiTIAQ'}], 'var_call_vO6Fz2Rj4JtZLdPSU55JiZ1b': [], 'var_call_QImgvfgioj3lI2H7TFTTVFtz': [{'Id': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Pi5IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'UnitPrice': '399.99'}], 'var_call_mo4R0OOuWr34mvRux0hRahOA': 'file_storage/call_mo4R0OOuWr34mvRux0hRahOA.json'}

exec(code, env_args)
