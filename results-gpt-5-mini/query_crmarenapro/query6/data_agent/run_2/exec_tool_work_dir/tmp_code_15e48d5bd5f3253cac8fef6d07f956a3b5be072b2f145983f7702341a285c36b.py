code = """import json
import pandas as pd

# Load large knowledge articles result from file path variable
path = var_call_EG9Xv2lgZSnUJmJKFPPPhnbD
with open(path, 'r', encoding='utf-8') as f:
    ka = json.load(f)

# DataFrame
df = pd.DataFrame(ka)

# Load QuoteLineItem records
qli = pd.DataFrame(var_call_3x6fvjosYmwFsztyTYDDvWBn)

# Normalize types
qli['Quantity'] = qli['Quantity'].astype(float)
qli['UnitPrice'] = qli['UnitPrice'].astype(float)
qli['Discount'] = qli['Discount'].astype(float)
qli['TotalPrice'] = qli['TotalPrice'].astype(float)

# Find suspicious entries: high quantity, high discount (>10%), mismatch total price
suspicious = []
for idx, row in qli.iterrows():
    calc_total = row['Quantity'] * row['UnitPrice'] * (1 - row['Discount']/100)
    mismatch = abs(calc_total - row['TotalPrice']) > 0.01
    high_discount = row['Discount'] > 10
    high_quantity = row['Quantity'] >= 30
    if mismatch or high_discount or high_quantity:
        suspicious.append({
            'Id': row['Id'],
            'Quantity': row['Quantity'],
            'UnitPrice': row['UnitPrice'],
            'Discount': row['Discount'],
            'TotalPrice': row['TotalPrice'],
            'calc_total': calc_total,
            'mismatch': mismatch,
            'high_discount': high_discount,
            'high_quantity': high_quantity
        })

# Search knowledge articles for rules about discounts, approvals, quantities, pricing
keywords = ['discount', 'approval', 'approve', 'pricing', 'price', 'quantity', 'quota', 'max', 'unauthor', 'unauthorized', 'override', 'approval required', 'discount approval', 'pricebook']

matches = []
for i,r in df.iterrows():
    text = ' '.join([str(r.get('title','') or ''), str(r.get('summary','') or ''), str(r.get('faq_answer__c','') or '')]).lower()
    for kw in keywords:
        if kw in text:
            matches.append({'id': r.get('id'), 'title': r.get('title'), 'keyword': kw})
            break

# Also specifically look for articles mentioning "discount > 10%" or similar patterns
pattern_matches = []
for i,r in df.iterrows():
    text = (str(r.get('faq_answer__c','') or '') + ' ' + str(r.get('summary','') or '')).lower()
    if 'discount' in text and ('approval' in text or '%' in text or 'percent' in text or 'approval required' in text):
        pattern_matches.append({'id': r.get('id'), 'title': r.get('title')})

result = {
    'suspicious_line_items': suspicious,
    'keyword_matched_articles_count': len(matches),
    'matched_articles_sample': matches[:10],
    'pattern_matched_articles': pattern_matches
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_3x6fvjosYmwFsztyTYDDvWBn': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_EG9Xv2lgZSnUJmJKFPPPhnbD': 'file_storage/call_EG9Xv2lgZSnUJmJKFPPPhnbD.json'}

exec(code, env_args)
