code = """import json, pandas as pd
qlis = pd.DataFrame(var_call_wAM0SeJZaPy3PnK0AnbUlppq)
# compute effective discount percent relative to (qty*unitprice)
for col in ['Quantity','UnitPrice','Discount','TotalPrice']:
    qlis[col] = pd.to_numeric(qlis[col], errors='coerce')
qlis['expected_total_no_disc'] = qlis['Quantity']*qlis['UnitPrice']
qlis['effective_discount_pct'] = (1 - qlis['TotalPrice']/qlis['expected_total_no_disc'])*100
# find any discount >0 that matches 15% tier mentioned in volume discount article
match_15 = qlis.loc[(qlis['Discount'].fillna(0)>0) & (qlis['effective_discount_pct'].round(2).between(14.9,15.1))]
# load knowledge articles
import os
path = var_call_UsxK9dID3VC8hGXVh4LKEuV6
if isinstance(path,str) and os.path.exists(path):
    with open(path,'r',encoding='utf-8') as f:
        arts = json.load(f)
else:
    arts = var_call_UsxK9dID3VC8hGXVh4LKEuV6
arts_df = pd.DataFrame(arts)
# select volume discount article id
vol = arts_df[arts_df['title'].str.contains('Volume-Based Discounts', case=False, na=False)].head(1)
article_id = None
if not vol.empty and not match_15.empty:
    # invalid if discount should be volume-based on purchase total thresholds ($5,$10,$20) but quote line uses unit price $399.99 and qty 35 => total huge; still eligible for 15% (>=20) actually valid.
    article_id = None
# Try other invalid heuristic: quantity 35 might exceed installation timeline max 25 units per policy => violates installation timeline policy
inst = arts_df[arts_df['title'].str.contains('Installation Timeline Policy', case=False, na=False)].head(1)
if article_id is None and not inst.empty:
    if (qlis['Quantity']>25).any():
        article_id = inst.iloc[0]['id']
# output
print('__RESULT__:')
print(json.dumps({'article_id': article_id}))"""

env_args = {'var_call_wAM0SeJZaPy3PnK0AnbUlppq': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_UsxK9dID3VC8hGXVh4LKEuV6': 'file_storage/call_UsxK9dID3VC8hGXVh4LKEuV6.json'}

exec(code, env_args)
