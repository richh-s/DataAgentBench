code = """import json, pandas as pd

qlis = var_call_JpHac6M7EMBTAsUFmwdwmRkr
quote = var_call_zNsheVL8tJR4moH51g8JRXhd
ka_path_or_list = var_call_MUD9ubUwTt16Fi5yttCAqMav
pbe_path_or_list = var_call_JIEQZx0sYHocIkOikbODI5rs

def load_maybe_path(x):
    if isinstance(x, str):
        with open(x, 'r', encoding='utf-8') as f:
            return json.load(f)
    return x

kas = load_maybe_path(ka_path_or_list)
pbes = load_maybe_path(pbe_path_or_list)

qli_df = pd.DataFrame(qlis)
pbe_df = pd.DataFrame(pbes)

# normalize ids and numeric fields
for col in ['QuoteId','Product2Id','PricebookEntryId','Id']:
    if col in qli_df.columns:
        qli_df[col] = qli_df[col].astype(str).str.strip().str.lstrip('#')

for col in ['PricebookEntryId','Pricebook2Id','Product2Id']:
    if col in pbe_df.columns:
        pbe_df[col] = pbe_df[col].astype(str).str.strip().str.lstrip('#')

for col in ['Quantity','UnitPrice','Discount','TotalPrice']:
    if col in qli_df.columns:
        qli_df[col] = pd.to_numeric(qli_df[col], errors='coerce')

pbe_df['CatalogUnitPrice'] = pd.to_numeric(pbe_df.get('CatalogUnitPrice'), errors='coerce')

m = qli_df.merge(pbe_df[['PricebookEntryId','CatalogUnitPrice']], on='PricebookEntryId', how='left')

# Determine violations:
violations = []
# rule: unit price should match catalog price unless discount applied via Discount field (as %)
# If Discount==0 and UnitPrice != CatalogUnitPrice -> violation
m['price_mismatch_no_discount'] = (m['Discount'].fillna(0)==0) & m['CatalogUnitPrice'].notna() & (m['UnitPrice'].round(2) != m['CatalogUnitPrice'].round(2))
# rule: discount percent must be between 0 and 50
m['discount_out_of_range'] = m['Discount'].notna() & ((m['Discount']<0) | (m['Discount']>50))
# rule: quantity must be positive integer and <= 25 (bulk requires approval)
m['qty_invalid'] = (m['Quantity'].isna()) | (m['Quantity']<=0) | (m['Quantity']%1!=0)
m['qty_over_limit'] = m['Quantity'].notna() & (m['Quantity']>25)

# find if any violation present
any_violation = bool(m[['price_mismatch_no_discount','discount_out_of_range','qty_invalid','qty_over_limit']].any().any())

# pick relevant knowledge article by keyword search
# prefer those mentioning quantity limit, discount limit, or pricebook/unit price.
ka_df = pd.DataFrame(kas)
for c in ['id','title','faq_answer__c','summary','urlname']:
    if c in ka_df.columns:
        ka_df[c] = ka_df[c].astype(str)

text = (ka_df.get('title','') + ' ' + ka_df.get('summary','') + ' ' + ka_df.get('faq_answer__c','')).str.lower()

def score(row_text):
    s=0
    if 'discount' in row_text: s+=2
    if 'unit price' in row_text or 'pricebook' in row_text or 'catalog' in row_text or 'pricing' in row_text: s+=2
    if 'quantity' in row_text or 'qty' in row_text or 'bulk' in row_text: s+=2
    if 'approval' in row_text: s+=1
    if 'policy' in row_text or 'regulation' in row_text or 'must' in row_text: s+=1
    return s

if any_violation:
    scores = text.map(score)
    ka_df = ka_df.assign(_score=scores)
    # choose highest score; tie-breaker: contains the specific concept of our triggered violation
    triggered = {
        'qty_over_limit': bool(m['qty_over_limit'].any()),
        'discount_out_of_range': bool(m['discount_out_of_range'].any()),
        'price_mismatch_no_discount': bool(m['price_mismatch_no_discount'].any())
    }
    def concept_bonus(row_text):
        b=0
        if triggered['qty_over_limit'] and ('quantity' in row_text or 'bulk' in row_text): b+=5
        if triggered['discount_out_of_range'] and 'discount' in row_text: b+=5
        if triggered['price_mismatch_no_discount'] and ('unit price' in row_text or 'pricebook' in row_text or 'pricing' in row_text or 'catalog' in row_text): b+=5
        return b
    ka_df['_bonus'] = text.map(concept_bonus)
    ka_df['_total'] = ka_df['_score'] + ka_df['_bonus']
    best = ka_df.sort_values(['_total','_score'], ascending=False).head(1)
    best_id = best['id'].iloc[0] if len(best)>0 else None
else:
    best_id = None

result = json.dumps(best_id)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_JpHac6M7EMBTAsUFmwdwmRkr': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_JIEQZx0sYHocIkOikbODI5rs': 'file_storage/call_JIEQZx0sYHocIkOikbODI5rs.json', 'var_call_MUD9ubUwTt16Fi5yttCAqMav': 'file_storage/call_MUD9ubUwTt16Fi5yttCAqMav.json', 'var_call_zNsheVL8tJR4moH51g8JRXhd': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}]}

exec(code, env_args)
