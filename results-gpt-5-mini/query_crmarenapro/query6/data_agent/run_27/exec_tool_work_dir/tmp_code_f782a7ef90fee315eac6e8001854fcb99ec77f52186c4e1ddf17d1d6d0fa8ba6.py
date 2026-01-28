code = """import json
# Load previous query results from storage variables
kav = var_call_nGygwU6SNc7Y5E4RH0grYgRb
qli = var_call_2YdGIHKZW0bprh7mnpDTqHoP

# Normalize text function
def contains_keywords(text, keywords):
    if not text:
        return False
    txt = text.lower()
    return any(k in txt for k in keywords)

keywords = ['discount', 'pricing', 'price', 'minimum order', 'minimum', 'quantity', 'approval', 'pricebook', 'discounts', 'discount approval', 'max discount', 'order quantity']

matches = []
for art in kav:
    combined = ' '.join([str(art.get('title','')), str(art.get('faq_answer__c','')), str(art.get('summary',''))])
    if contains_keywords(combined, keywords):
        matches.append({'id': art.get('id'), 'title': art.get('title')})

# Print results
print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_call_bMDlLquwdVYFwmVoOvAeV8eE': [], 'var_call_CcS0WbIuEos0jxEIVKL95Dga': 'file_storage/call_CcS0WbIuEos0jxEIVKL95Dga.json', 'var_call_2YdGIHKZW0bprh7mnpDTqHoP': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_nGygwU6SNc7Y5E4RH0grYgRb': 'file_storage/call_nGygwU6SNc7Y5E4RH0grYgRb.json'}

exec(code, env_args)
