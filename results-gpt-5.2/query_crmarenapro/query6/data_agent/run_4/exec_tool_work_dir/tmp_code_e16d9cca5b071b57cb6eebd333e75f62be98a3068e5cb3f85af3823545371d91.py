code = """import json, pandas as pd

qli = pd.DataFrame(var_call_zzgkIYMS87GKD14toJt1q0Gi)

# load product/pricebook entries full
path = var_call_tNZyhobXRynzKrqRuv2KdDkn
with open(path, 'r', encoding='utf-8') as f:
    prod = json.load(f)
prod_df = pd.DataFrame(prod)

kpath = var_call_1pVbsZih7m0UUismoquEcpBi
with open(kpath, 'r', encoding='utf-8') as f:
    kav = json.load(f)
kav_df = pd.DataFrame(kav)

# normalize ids for joins
for c in ['Product2Id','PricebookEntryId']:
    if c in qli.columns:
        qli[c+'_norm'] = qli[c].astype(str).str.lstrip('#').str.strip()
for c in ['Product2Id','PricebookEntryId']:
    if c in prod_df.columns:
        prod_df[c+'_norm'] = prod_df[c].astype(str).str.lstrip('#').str.strip()

# numeric
for c in ['Quantity','UnitPrice','Discount','TotalPrice']:
    qli[c] = pd.to_numeric(qli[c], errors='coerce')
prod_df['ListUnitPrice'] = pd.to_numeric(prod_df['ListUnitPrice'], errors='coerce')

# join on pricebookentryid first; if missing, on product2id
j = qli.merge(prod_df[['Product2Id_norm','PricebookEntryId_norm','ListUnitPrice']], how='left', left_on='PricebookEntryId_norm', right_on='PricebookEntryId_norm', suffixes=('','_pbe'))
# fill list price via product join where pbe not matched
miss = j['ListUnitPrice'].isna()
if miss.any():
    j2 = qli[miss].merge(prod_df[['Product2Id_norm','ListUnitPrice']], how='left', left_on='Product2Id_norm', right_on='Product2Id_norm')
    j.loc[miss,'ListUnitPrice'] = j2['ListUnitPrice'].values

# Determine invalid: unitprice different from list OR discount outside 0-100 OR quantity not positive int OR total mismatch
invalid = pd.Series(False, index=j.index)
# quantity must be positive whole number
invalid |= (j['Quantity'].isna()) | (j['Quantity']<=0) | (j['Quantity']%1!=0)
# discount 0-100
invalid |= (j['Discount'].isna()) | (j['Discount']<0) | (j['Discount']>100)
# list price compare if available
invalid |= (~j['ListUnitPrice'].isna()) & (abs(j['UnitPrice']-j['ListUnitPrice'])>1e-6)
# total price check: UnitPrice*Quantity*(1-Discount/100)
calc_total = j['UnitPrice']*j['Quantity']*(1-j['Discount']/100.0)
invalid |= (j['TotalPrice'].isna()) | (abs(j['TotalPrice']-calc_total)>0.01)

is_invalid = bool(invalid.any())

# find most relevant knowledge article: look for pricing/discount/quote configuration keywords
text_cols = ['title','summary','faq_answer__c']
for col in text_cols:
    if col in kav_df.columns:
        kav_df[col] = kav_df[col].astype(str)
needle_terms = ['discount','discounts','pricing','price','quote line','quotation','unit price','quantity','configuration','pricebook','list price','total price']
pattern = '|'.join([t.replace(' ','\\s+') for t in needle_terms])
# score by occurrences
import re
regex = re.compile(pattern, flags=re.IGNORECASE)

def score_row(r):
    s = 0
    for col in text_cols:
        if col in r and pd.notna(r[col]):
            s += len(regex.findall(r[col]))
    return s

kav_df['score'] = kav_df.apply(lambda r: score_row(r), axis=1)
# pick top scored
best = kav_df.sort_values(['score','id'], ascending=[False, True]).head(1)
article_id = None
if len(best)>0 and best.iloc[0]['score']>0:
    article_id = str(best.iloc[0]['id']).lstrip('#').strip()

result = {'is_invalid': is_invalid, 'article_id': article_id}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_zzgkIYMS87GKD14toJt1q0Gi': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97', 'OpportunityLineItemId': '00kWt000002HUwhIAG'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98', 'OpportunityLineItemId': '00kWt000002HHRkIAO'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96', 'OpportunityLineItemId': '00kWt000002HQJYIA4'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025', 'OpportunityLineItemId': '00kWt000002HQJZIA4'}], 'var_call_tNZyhobXRynzKrqRuv2KdDkn': 'file_storage/call_tNZyhobXRynzKrqRuv2KdDkn.json', 'var_call_1pVbsZih7m0UUismoquEcpBi': 'file_storage/call_1pVbsZih7m0UUismoquEcpBi.json', 'var_call_qXBbCONtzGLm0xycugIDY35h': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.'}]}

exec(code, env_args)
