code = """import json
# Load previous tool results
quote_line_items = var_call_2NBOYHDx7TuKQDxVRJoYDmsz
kb_path = var_call_Qagsj7BZPrVVYCytPMLb3W6z

with open(kb_path, 'r') as f:
    kb = json.load(f)

# normalize text and search keywords
keywords = ['discount', 'approval', 'approve', 'pricing', 'price', 'maximum discount', 'max discount', 'quantity', 'limit', 'minimum order', 'bulk', 'approval required']
matches = []
for art in kb:
    text = ' '.join(str(art.get(k,'')).lower() for k in ['title','summary','faq_answer__c'])
    for kw in keywords:
        if kw in text:
            matches.append({'id': art.get('id'), 'title': art.get('title'), 'matched_with': kw, 'excerpt': text[:300]})
            break

# Analyze quote for potential violations: check discounts >10% and large quantities >30 (example threshold)
violations = []
for li in quote_line_items:
    try:
        disc = float(li.get('Discount') or 0)
    except:
        disc = 0.0
    try:
        qty = float(li.get('Quantity') or 0)
    except:
        qty = 0.0
    if disc > 10.0:
        violations.append({'type':'discount_exceeds_threshold','threshold':10.0,'line_item_id':li.get('Id'),'discount':disc,'quote_id':li.get('QuoteId')})
    if qty > 30.0:
        violations.append({'type':'quantity_exceeds_threshold','threshold':30.0,'line_item_id':li.get('Id'),'quantity':qty,'quote_id':li.get('QuoteId')})

# Now find KB articles that mention discounts and approvals or quantity limits
kb_discount_articles = [m for m in matches if 'discount' in (m['matched_with'] or '') or 'approval' in (m['matched_with'] or '') or 'approve' in (m['matched_with'] or '') or 'max' in m['title'].lower()]

result = {
    'matches_found': len(matches),
    'kb_discount_candidates': kb_discount_articles,
    'violations_detected': violations
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ZPlTSscSb35pEnCVNehnayD4': [], 'var_call_2NBOYHDx7TuKQDxVRJoYDmsz': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_lWAqjbNBcjJBlOQi6vyyUwZM': [{'Id': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Pi5IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'UnitPrice': '399.99'}], 'var_call_ouhpeyf9oxAFoUYfLENmUPN0': [{'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}], 'var_call_Qagsj7BZPrVVYCytPMLb3W6z': 'file_storage/call_Qagsj7BZPrVVYCytPMLb3W6z.json'}

exec(code, env_args)
