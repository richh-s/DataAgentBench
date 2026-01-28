code = """import json
path = var_call_EG9Xv2lgZSnUJmJKFPPPhnbD
with open(path, 'r', encoding='utf-8') as f:
    ka = json.load(f)

results = []
for r in ka:
    text = (r.get('faq_answer__c') or '') + ' ' + (r.get('summary') or '') + ' ' + (r.get('title') or '')
    t = text.lower()
    if 'discount' in t:
        # check for approval language or percent limits
        if 'approval' in t or 'approve' in t or 'requires' in t or '%' in t or 'percent' in t or 'max' in t or 'greater than' in t or 'exceed' in t:
            results.append({'id': r.get('id'), 'title': r.get('title'), 'summary': r.get('summary'), 'faq': r.get('faq_answer__c')})

# print count and ids
out = {'count': len(results), 'ids': [r['id'] for r in results][:50]}
import json
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_3x6fvjosYmwFsztyTYDDvWBn': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_EG9Xv2lgZSnUJmJKFPPPhnbD': 'file_storage/call_EG9Xv2lgZSnUJmJKFPPPhnbD.json', 'var_call_QPUtR5ZLbBZBJZ7190wIjMFv': {'suspicious_line_items': [{'Id': '#0QLWt0000022oAvOAI', 'Quantity': 35.0, 'UnitPrice': 399.99, 'Discount': 15.0, 'TotalPrice': 11899.7025, 'calc_total': 11899.7025, 'mismatch': False, 'high_discount': True, 'high_quantity': True}], 'keyword_matched_articles_count': 91, 'matched_articles_sample': [{'id': 'ka0Wt000000EowFIAS', 'title': 'Competitor: Adaptive Design Solutions', 'keyword': 'pricing'}, {'id': '#ka0Wt000000EqRlIAK', 'title': 'Competitor: NanoDesign Systems   ', 'keyword': 'pricing'}, {'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'keyword': 'discount'}, {'id': '#ka0Wt000000EpSUIA0', 'title': 'TechPulse Solution Volume-Based Installation Timeline Policy', 'keyword': 'quantity'}, {'id': '#ka0Wt000000Eo8HIAS', 'title': "TechPulse's Commitment to Exceptional Customer Service", 'keyword': 'max'}, {'id': '#ka0Wt000000EqLJIA0', 'title': 'Training Excellence with TrainEDU Suite', 'keyword': 'max'}, {'id': 'ka0Wt000000EqI7IAK', 'title': 'Advanced EDA Education with InnoTrain Hub', 'keyword': 'max'}, {'id': 'ka0Wt000000Eq8QIAS', 'title': 'Revolutionizing Integrated Development Environments with AI', 'keyword': 'max'}, {'id': 'ka0Wt000000EpXMIA0', 'title': 'Advanced Workflow Automation with PCB EcoModel', 'keyword': 'max'}, {'id': 'ka0Wt000000EoBSIA0', 'title': 'Efficiency Boost with AutoLayout Master', 'keyword': 'max'}], 'pattern_matched_articles': [{'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts'}, {'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers'}]}}

exec(code, env_args)
