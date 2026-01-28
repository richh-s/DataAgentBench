code = """import json
kb_path = var_call_Qagsj7BZPrVVYCytPMLb3W6z
with open(kb_path,'r') as f:
    kb = json.load(f)

search_phrases = [
    'maximum discount', 'max discount', 'approval required', 'requires approval', 'requires manager approval',
    'discount above', 'discounts over', 'discount >', 'discount greater', 'quantity limit', 'maximum quantity', 'max quantity', 'order quantity limit', 'bulk order limit', 'approval for discounts'
]

matches = []
for art in kb:
    text = ' '.join(str(art.get(k,'')).lower() for k in ['title','summary','faq_answer__c'])
    for ph in search_phrases:
        if ph in text:
            matches.append({'id': art.get('id'), 'title': art.get('title'), 'phrase': ph, 'excerpt': text[text.find(ph)-100:text.find(ph)+200]})
            break

# Also include articles with 'volume-based discounts' or 'discount' and 'approval'
for art in kb:
    text = ' '.join(str(art.get(k,'')).lower() for k in ['title','summary','faq_answer__c'])
    if 'volume-based discounts' in text and not any(m['id']==art.get('id') for m in matches):
        matches.append({'id': art.get('id'), 'title': art.get('title'), 'phrase': 'volume-based discounts', 'excerpt': text[:300]})
    if 'discount' in text and 'approval' in text and not any(m['id']==art.get('id') for m in matches):
        matches.append({'id': art.get('id'), 'title': art.get('title'), 'phrase': 'discount and approval', 'excerpt': text[:300]})

print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_call_ZPlTSscSb35pEnCVNehnayD4': [], 'var_call_2NBOYHDx7TuKQDxVRJoYDmsz': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_lWAqjbNBcjJBlOQi6vyyUwZM': [{'Id': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Pi5IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'UnitPrice': '399.99'}], 'var_call_ouhpeyf9oxAFoUYfLENmUPN0': [{'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}], 'var_call_Qagsj7BZPrVVYCytPMLb3W6z': 'file_storage/call_Qagsj7BZPrVVYCytPMLb3W6z.json', 'var_call_jZUPT2WtT8EogMbpZIgUmXAh': {'matches_found': 27, 'kb_discount_candidates': [{'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'matched_with': 'discount', 'excerpt': 'volume-based discounts volume-based discounts volume-based discounts are a strategic tool for fostering customer loyalty and encouraging bulk purchases. at techpulse solution, we aim to provide value-added benefits to our customers, and volume-based discounts are integral to this mission. here is a '}, {'id': '#ka0Wt000000Eo6cIAC', 'title': 'Maximizing Software Potential: Ensuring Timely Feature Update Notifications at TechPulse Solutions', 'matched_with': 'limit', 'excerpt': 'maximizing software potential: ensuring timely feature update notifications at techpulse solutions at techpulse solutions, customer feedback has revealed a recurring issue with inconsistent notifications of feature updates, which hinders the full utilization of the software. this knowledge article e'}, {'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers', 'matched_with': 'discount', 'excerpt': 'competing offers policy for price adjustments based on competing offers in a competitive marketplace, flexibility and responsiveness to customer needs are critical to maintaining a successful business operation. techpulse solution recognizes that potential clients may be considering multiple vendors'}], 'violations_detected': [{'type': 'discount_exceeds_threshold', 'threshold': 10.0, 'line_item_id': '#0QLWt0000022oAvOAI', 'discount': 15.0, 'quote_id': '0Q0Wt000001WRAzKAO'}, {'type': 'quantity_exceeds_threshold', 'threshold': 30.0, 'line_item_id': '#0QLWt0000022oAvOAI', 'quantity': 35.0, 'quote_id': '0Q0Wt000001WRAzKAO'}]}}

exec(code, env_args)
