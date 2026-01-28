code = """import json, pandas as pd

qlis = pd.DataFrame(var_call_IukQY47NY2QXPDMUCldiHrPX)

# Load knowledge articles from file if needed
ka_src = var_call_uCZlAnc2ALtOIQ5bhelebBVs
if isinstance(ka_src, str):
    with open(ka_src, 'r', encoding='utf-8') as f:
        kas = json.load(f)
else:
    kas = ka_src
ka = pd.DataFrame(kas)

# Heuristic checks for invalid config based on common policy patterns
issues = []
# quantity unusually high
qlis['Quantity'] = pd.to_numeric(qlis['Quantity'])
qlis['UnitPrice'] = pd.to_numeric(qlis['UnitPrice'])
qlis['Discount'] = pd.to_numeric(qlis['Discount'])

if (qlis['Discount'] > 0).any():
    issues.append('discount')
if (qlis['Quantity'] >= 25).any():
    issues.append('high_quantity')

text_cols = []
for c in ['title','summary','faq_answer__c','urlname']:
    if c in ka.columns:
        text_cols.append(c)

# Score articles by keyword overlap
keywords_map = {
    'discount': ['discount','approval','maximum discount','pricing exception','discounts','price override'],
    'high_quantity': ['quantity','maximum order','bulk','cap','limit','large order','volume'],
}

scores = []
for _, row in ka.iterrows():
    text = ' '.join([str(row.get(c,'')) for c in text_cols]).lower()
    score = 0
    for iss in issues:
        for kw in keywords_map.get(iss, []):
            if kw in text:
                score += 1
    if score>0:
        scores.append((row.get('id'), score))

# If no matches, try broader search for pricing/discount policy
if not scores and issues:
    broad = ['discount','pricing','price','quote','quantity','volume','approval','policy','regulation','minimum','maximum']
    for _, row in ka.iterrows():
        text = ' '.join([str(row.get(c,'')) for c in text_cols]).lower()
        score = sum(1 for kw in broad if kw in text)
        if score>0:
            scores.append((row.get('id'), score))

# pick top scoring id; if still none, null
best_id = None
if scores:
    best_id = sorted(scores, key=lambda x: (-x[1], str(x[0])))[0][0]

print('__RESULT__:')
print(json.dumps({'knowledge_article_id': best_id}))"""

env_args = {'var_call_IukQY47NY2QXPDMUCldiHrPX': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_uCZlAnc2ALtOIQ5bhelebBVs': 'file_storage/call_uCZlAnc2ALtOIQ5bhelebBVs.json'}

exec(code, env_args)
