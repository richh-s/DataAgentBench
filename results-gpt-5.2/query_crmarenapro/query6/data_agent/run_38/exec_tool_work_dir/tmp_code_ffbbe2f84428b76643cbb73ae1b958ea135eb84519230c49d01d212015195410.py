code = """import json, pandas as pd

qli = pd.DataFrame(var_call_50TUjmOMuDnIKSNdi4wh1EzL)
# invalid config appears to be a very large quantity (35) with a discount (15%) and non-integer total price suggests discount applied.
# We'll search knowledge articles for rules about max quantity, discount limits, approval requirements.

path = var_call_g1pwyk3tiyekNlmkvnFjIjm1
with open(path,'r',encoding='utf-8') as f:
    kav = json.load(f)

dfk = pd.DataFrame(kav)
for c in ['id','title','faq_answer__c','summary','urlname']:
    if c in dfk.columns:
        dfk[c] = dfk[c].astype(str)

txt = (dfk['title'].str.lower().fillna('') + ' ' + dfk['summary'].str.lower().fillna('') + ' ' + dfk['faq_answer__c'].str.lower().fillna(''))
keywords = ['discount','approval','quote','quantity','bulk','minimum','maximum','pricing','price','unit price','sales policy','policy','regulation','limit','threshold']
mask = txt.apply(lambda s: any(k in s for k in keywords))
sub = dfk[mask].copy()
# further rank by presence of likely terms around discount limits
rank_terms = ['discount','max','maximum','limit','approval','threshold','bulk','quantity']
sub['score'] = txt[mask].apply(lambda s: sum(s.count(t) for t in rank_terms))
sub = sub.sort_values(['score'], ascending=False)

# pick top candidates and then choose one that clearly is about discount limit; if none, just top scored.
# We'll return the top id.
ans = None
if len(sub):
    ans = sub.iloc[0]['id']

print('__RESULT__:')
print(json.dumps({'article_id': ans, 'top5': sub[['id','title','score']].head(5).to_dict(orient='records')}))"""

env_args = {'var_call_50TUjmOMuDnIKSNdi4wh1EzL': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_g1pwyk3tiyekNlmkvnFjIjm1': 'file_storage/call_g1pwyk3tiyekNlmkvnFjIjm1.json'}

exec(code, env_args)
