code = """import json
# var_call_nGygwU6SNc7Y5E4RH0grYgRb is a file path containing knowledge articles JSON
kav_path = var_call_nGygwU6SNc7Y5E4RH0grYgRb
with open(kav_path, 'r', encoding='utf-8') as f:
    kav = json.load(f)

qli = var_call_2YdGIHKZW0bprh7mnpDTqHoP

# Examine quote line items for potential violations
violations = []
for item in qli:
    # normalize numeric values
    try:
        qty = float(item.get('Quantity') or item.get('quantity') or 0)
        unit = float(item.get('UnitPrice') or item.get('unitprice') or 0)
        disc = float(item.get('Discount') or item.get('discount') or 0)
    except:
        qty = 0
        unit = 0
        disc = 0
    # conditions to flag: discount > 10%, quantity unusually large > 30, unit price higher than typical pricebook? can't check pricebook here
    if disc > 10 or qty > 30:
        violations.append({'Id': item.get('Id'), 'Quantity': qty, 'UnitPrice': unit, 'Discount': disc})

# Search knowledge articles for relevant policies
keywords = ['discount', 'approval', 'pricebook', 'minimum order', 'minimum', 'quantity', 'max discount', 'discount approval', 'pricing', 'price approval']
matches = []
for art in kav:
    text = ' '.join([str(art.get('title','') or ''), str(art.get('faq_answer__c','') or ''), str(art.get('summary','') or '')]).lower()
    for kw in keywords:
        if kw in text:
            matches.append({'id': art.get('id'), 'title': art.get('title'), 'keyword': kw})
            break

result = {'quote_id': '0Q0Wt000001WRAzKAO', 'flagged_line_items': violations, 'matching_knowledge_articles': matches}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_bMDlLquwdVYFwmVoOvAeV8eE': [], 'var_call_CcS0WbIuEos0jxEIVKL95Dga': 'file_storage/call_CcS0WbIuEos0jxEIVKL95Dga.json', 'var_call_2YdGIHKZW0bprh7mnpDTqHoP': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_nGygwU6SNc7Y5E4RH0grYgRb': 'file_storage/call_nGygwU6SNc7Y5E4RH0grYgRb.json'}

exec(code, env_args)
