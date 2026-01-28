code = """import json
# load quote lines
ql = var_call_wNoGlqHGpPYskamILCNILlUJ
# load pricebook entries
pbe = var_call_tYw4T3sIwa9x1hD0T0U30pIQ
# find any mismatches between QuoteLineItem UnitPrice and PricebookEntry UnitPrice
pbe_map = {x['Id']: float(x['UnitPrice']) for x in pbe}
violations = []
for item in ql:
    qid = item['Id']
    pbe_id = item.get('PricebookEntryId')
    q_unit = float(item.get('UnitPrice'))
    if pbe_id in pbe_map:
        pb_unit = pbe_map[pbe_id]
        if abs(q_unit - pb_unit) > 0.01:
            violations.append({'QuoteLineItemId': qid, 'PricebookEntryId': pbe_id, 'QuoteUnitPrice': q_unit, 'PricebookUnitPrice': pb_unit})
    else:
        violations.append({'QuoteLineItemId': qid, 'PricebookEntryId': pbe_id, 'error': 'Pricebook entry not found in PricebookEntry table'})

# check quantity limits rule: find knowledge article for Product Quantity Limits
# from earlier execute_python result we have var_call_0DJ9qdrwZxrwu2GrHvWdCDXs
ka_matches = var_call_0DJ9qdrwZxrwu2GrHvWdCDXs
# find quote lines with large quantities > 100 (example rule) or high discounts
suspicious = []
for item in ql:
    qty = float(item.get('Quantity'))
    disc = float(item.get('Discount'))
    if qty > 100 or disc > 10:
        suspicious.append({'QuoteLineItemId': item['Id'], 'Quantity': qty, 'Discount': disc})

res = {'price_mismatches': violations, 'suspicious_quantity_or_discount': suspicious, 'knowledge_matches': ka_matches}
print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_call_odEBb1mQIHOssKI6xxcwkm7f': [], 'var_call_Gi6ZZyYcAlu58CrF9BxH7cEf': [{'Id': '#0Q0Wt000001WRAzKAO', 'Name': 'NeoGreen EDA Expansion Quote', 'AccountId': '001Wt00000PHVsDIAX', 'OpportunityId': '006Wt000007BGgXIAW', 'Status': 'Needs Review'}], 'var_call_DMLKQx9SHLjUbEysnh5eJVP8': [], 'var_call_wNoGlqHGpPYskamILCNILlUJ': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_X1FZdf2TtYXCdBZ4ncGyCe0j': 'file_storage/call_X1FZdf2TtYXCdBZ4ncGyCe0j.json', 'var_call_0DJ9qdrwZxrwu2GrHvWdCDXs': [{'id': '#ka0Wt000000EqRlIAK', 'title': 'Competitor: NanoDesign Systems   ', 'summary': "NanoDesign Systems is a prominent player in the electronic design automation industry, hailed for its strong vendor stability and partnership model, ensuring reliable, long-term collaborations with its clients. The company places significant emphasis on its roadmap and future enhancements, continually striving to align with emerging market demands and technological advancements. However, it faces challenges in offering highly customizable and flexible solutions, sometimes falling short of catering to specific and unique client workflows. Additionally, NanoDesign's support and service level agreements could be more responsive, with their pricing strategy occasionally seen as less transparent compared to competitors like TechPulse Solutions. Despite these challenges, NanoDesign remains a formidable entity with a focus on vendor reliability and technological growth."}, {'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'summary': 'Volume-Based Discounts'}, {'id': '#ka0Wt000000EpSUIA0', 'title': 'TechPulse Solution Volume-Based Installation Timeline Policy', 'summary': 'TechPulse Solution Volume-Based Installation Timeline Policy'}, {'id': '#ka0Wt000000EnwvIAC', 'title': 'Product Quantity Limits   ', 'summary': 'Product Quantity Limits'}, {'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers', 'summary': 'Policy for price adjustments based on competing offers'}], 'var_call_tYw4T3sIwa9x1hD0T0U30pIQ': [{'Id': '01uWt0000027P8cIAE', 'Product2Id': '01tWt000006hV8LIAU', 'UnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ'}, {'Id': '01uWt0000027PADIA2', 'Product2Id': '01tWt000006hPffIAE', 'UnitPrice': '299.99', 'Pricebook2Id': '#01sWt000000imiTIAQ'}, {'Id': '01uWt0000027Pi5IAE', 'Product2Id': '01tWt000006hVczIAE', 'UnitPrice': '399.99', 'Pricebook2Id': '#01sWt000000imiTIAQ'}], 'var_call_pAt2WSZzS3MGmyga8ItnKppI': [{'Id': '01sWt000000imiTIAQ', 'Name': 'Standard Price Book', 'IsActive': '1'}]}

exec(code, env_args)
