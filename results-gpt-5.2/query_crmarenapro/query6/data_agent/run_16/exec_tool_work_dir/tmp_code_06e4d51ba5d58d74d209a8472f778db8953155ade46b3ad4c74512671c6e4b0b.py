code = """import json, pandas as pd, re
qlis = pd.DataFrame(var_call_5lyQ67b9Jg2JuyXWFKhCObax)
# normalize numeric fields
for c in ['Quantity','UnitPrice','Discount','TotalPrice']:
    qlis[c] = pd.to_numeric(qlis[c], errors='coerce')
# rule checks: quantity must be positive integer; discount between 0 and 1 (as fraction) (assumption) or 0-100? We'll detect discount=15 with other lines 0 suggests percent, but stored as 15.0.
# Identify anomalies: non-integer quantity, quantity<=0, discount<0 or discount>1 and discount>100? We'll flag if discount>1 (fraction) and <=100 then percent; if percent > 50? unclear.
qlis['qty_non_int'] = (qlis['Quantity'] % 1 != 0)
qlis['qty_non_pos'] = qlis['Quantity'] <= 0
# discount considered percent if >1; allow 0-30%? We'll flag >10%? but need regulation article.
qlis['disc_percent'] = qlis['Discount']
qlis['disc_flag'] = qlis['Discount'] > 10  # flag high discount >10%
# also validate totalprice equals qty*unitprice*(1-discount/100)
qlis['calc_total'] = qlis['Quantity'] * qlis['UnitPrice'] * (1 - (qlis['Discount']/100.0))
qlis['total_mismatch'] = (qlis['calc_total'] - qlis['TotalPrice']).abs() > 0.01
anoms = qlis[ qlis['qty_non_int'] | qlis['qty_non_pos'] | qlis['disc_flag'] | qlis['total_mismatch'] ]
# load knowledge articles
import os
path = var_call_PRw1zYaMW8wErLqSwrT7Q7tj
with open(path,'r',encoding='utf-8') as f:
    kav = json.load(f)
kdf = pd.DataFrame(kav)
# find candidate article matching discount policy keywords
text = (kdf['title'].fillna('')+'\n'+kdf['summary'].fillna('')+'\n'+kdf['faq_answer__c'].fillna('')).str.lower()
# keywords for discount/quote/price/quantity regulations
kw = ['discount','pricing','price','quote line','quotation','quantity','unit price','approval','maximum discount','min quantity']
mask = text.apply(lambda t: any(k in t for k in kw))
cands = kdf[mask].copy()
# prefer ones mentioning discount thresholds like 10% or 15%
pattern = re.compile(r'(\b10\%\b|\b15\%\b|maximum discount|max discount|discount approval|discounts over)')
if len(cands):
    cands['score'] = text[mask].apply(lambda t: len(pattern.findall(t)))
    cands = cands.sort_values(['score'], ascending=False)
art_id = None
if len(anoms) and len(cands):
    art_id = cands.iloc[0]['id']
elif len(anoms):
    # fallback: take highest scoring overall
    kdf2 = kdf.copy()
    text2 = (kdf2['title'].fillna('')+'\n'+kdf2['summary'].fillna('')+'\n'+kdf2['faq_answer__c'].fillna('')).str.lower()
    kdf2['score'] = text2.apply(lambda t: sum(t.count(k) for k in kw))
    art_id = kdf2.sort_values('score', ascending=False).iloc[0]['id']
else:
    art_id = None
print('__RESULT__:')
print(json.dumps({'anomaly_rows': anoms.to_dict(orient='records'), 'chosen_article_id': art_id}))"""

env_args = {'var_call_5lyQ67b9Jg2JuyXWFKhCObax': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_lgQbasu95OvfaR0l7MIgFbHV': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_call_PRw1zYaMW8wErLqSwrT7Q7tj': 'file_storage/call_PRw1zYaMW8wErLqSwrT7Q7tj.json', 'var_call_ADbfsB1djC0YIUaxmS42O3sF': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE', 'Description': 'Integrated development environment with intuitive coding and debugging capabilities.', 'IsActive': '1', 'External_ID__c': 'Integrated Development Environments,Educational and Training Platforms_6'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   ', 'Description': 'Environmentally-friendly PCB design solution with power utilization analytics.', 'IsActive': '1', 'External_ID__c': 'PCB Design Solutions,Power Optimization Tools_4'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.', 'IsActive': '1', 'External_ID__c': 'AI-Powered Circuit Design Tools,Customizable Workflow Automation_5'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio', 'Description': 'Enhanced design collaboration platform offering real-time editing and feedback.', 'IsActive': '1', 'External_ID__c': 'Cloud-Based Design Collaboration,Integrated Development Environments_30'}], 'var_call_JXfsFlvIxyRiiNDHkKPgkRop': [{'Id': '#01uWt0000027P8bIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV6jIAE', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Pi5IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'UnitPrice': '399.99'}], 'var_call_kY8MtvDllYnjQvmZbZ1g25r7': [{'Id': '01sWt000000imiTIAQ', 'Name': 'Standard Price Book', 'Description': 'None', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}], 'var_call_2dC1KZiHgYmFnYLcnqxNOT3h': [{'QuoteId': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15', 'StageName': 'Quote', 'Amount': '15209.6125'}]}

exec(code, env_args)
