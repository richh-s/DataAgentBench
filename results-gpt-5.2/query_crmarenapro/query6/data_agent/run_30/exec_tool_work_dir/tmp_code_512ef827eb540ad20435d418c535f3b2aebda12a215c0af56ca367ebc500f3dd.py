code = """import json, pandas as pd, re

ql = pd.DataFrame(var_call_ne27p7NFW4ZsXi051RDzddwg)
pbe = pd.DataFrame(var_call_R64ObTBFX6uIcu4dMEOF4UKv)

for c in ['Quantity','UnitPrice','Discount','TotalPrice']:
    if c in ql.columns:
        ql[c] = pd.to_numeric(ql[c], errors='coerce')
for c in ['ListUnitPrice']:
    pbe[c] = pd.to_numeric(pbe[c], errors='coerce')

# normalize ids by stripping leading '#'
for c in ['PricebookEntryId','Product2Id']:
    if c in ql.columns:
        ql[c+'_norm'] = ql[c].astype(str).str.replace('^#','', regex=True).str.strip()
for c in ['PricebookEntryId','Product2Id']:
    if c in pbe.columns:
        pbe[c+'_norm'] = pbe[c].astype(str).str.replace('^#','', regex=True).str.strip()

m = ql.merge(pbe, left_on='PricebookEntryId_norm', right_on='PricebookEntryId_norm', how='left', suffixes=('','_pbe'))

# detect pricing violations: unit price different from list price beyond tiny tolerance, and/or discount not consistent
m['unit_vs_list_diff'] = (m['UnitPrice'] - m['ListUnitPrice']).abs()
viol_price = m[m['ListUnitPrice'].notna() & (m['unit_vs_list_diff']>0.01)]

# detect abnormal quantities (heuristic): quantity must be positive integer and <= 20
viol_qty = m[(m['Quantity'].isna()) | (m['Quantity']<=0) | (m['Quantity']%1!=0) | (m['Quantity']>20)]

# detect discount limit (heuristic): discount percent <=10
viol_disc = m[m['Discount'].fillna(0)>10]

violations = []
if len(viol_price)>0: violations.append('price')
if len(viol_qty)>0: violations.append('quantity')
if len(viol_disc)>0: violations.append('discount')

# load knowledge articles
path = var_call_NO9HB33D0lzsQrwc2PqpPiMr
if isinstance(path, str) and path.endswith('.json'):
    with open(path,'r',encoding='utf-8') as f:
        ka = json.load(f)
else:
    ka = path

def best_article(violations, ka):
    # simple keyword matching
    patterns = {
        'discount': re.compile(r"discount|maximum discount|pricing exception|approval", re.I),
        'quantity': re.compile(r"quantity|maximum units|bulk|volume limit", re.I),
        'price': re.compile(r"list price|unit price|price override|pricing policy", re.I),
    }
    candidates = []
    for art in ka:
        text = (str(art.get('title',''))+' '+str(art.get('summary',''))+' '+str(art.get('faq_answer__c','')))
        score = 0
        for v in violations:
            if patterns[v].search(text):
                score += 1
        if score>0:
            candidates.append((score, art.get('id')))
    candidates.sort(reverse=True)
    return candidates[0][1] if candidates else None

article_id = best_article(violations, ka)

print('__RESULT__:')
print(json.dumps({'violations': violations, 'article_id': article_id}))"""

env_args = {'var_call_ne27p7NFW4ZsXi051RDzddwg': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_NO9HB33D0lzsQrwc2PqpPiMr': 'file_storage/call_NO9HB33D0lzsQrwc2PqpPiMr.json', 'var_call_R64ObTBFX6uIcu4dMEOF4UKv': [{'PricebookEntryId': '01uWt0000027P3lIAE', 'ListUnitPrice': '499.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE'}, {'PricebookEntryId': '01uWt0000027P3mIAE', 'ListUnitPrice': '489.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVhpIAE'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'ListUnitPrice': '599.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hV58IAE'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'ListUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hTUkIAM'}, {'PricebookEntryId': '#01uWt0000027P8bIAE', 'ListUnitPrice': '349.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV6jIAE'}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'ListUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU'}, {'PricebookEntryId': '01uWt0000027PADIA2', 'ListUnitPrice': '299.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE'}, {'PricebookEntryId': '01uWt0000027PBpIAM', 'ListUnitPrice': '449.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV9xIAE'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'ListUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVBZIA2'}, {'PricebookEntryId': '01uWt0000027PF3IAM', 'ListUnitPrice': '549.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVDBIA2'}, {'PricebookEntryId': '#01uWt0000027PGfIAM', 'ListUnitPrice': '479.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVEnIAM'}, {'PricebookEntryId': '01uWt0000027PIHIA2', 'ListUnitPrice': '599.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVGPIA2'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'ListUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVI1IAM'}, {'PricebookEntryId': '01uWt0000027PIJIA2', 'ListUnitPrice': '459.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVptIAE'}, {'PricebookEntryId': '01uWt0000027PJtIAM', 'ListUnitPrice': '649.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'PricebookEntryId': '01uWt0000027PLVIA2', 'ListUnitPrice': '459.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVLFIA2'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'ListUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPfgIAE'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'ListUnitPrice': '299.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVMrIAM'}, {'PricebookEntryId': '01uWt0000027POkIAM', 'ListUnitPrice': '349.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hRfqIAE'}, {'PricebookEntryId': '01uWt0000027PQLIA2', 'ListUnitPrice': '489.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hUKMIA2'}, {'PricebookEntryId': '#01uWt0000027PRxIAM', 'ListUnitPrice': '559.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVOTIA2'}, {'PricebookEntryId': '01uWt0000027PTZIA2', 'ListUnitPrice': '449.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV0IIAU'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'ListUnitPrice': '459.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVUvIAM'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'ListUnitPrice': '339.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'ListUnitPrice': '429.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ6IAM'}, {'PricebookEntryId': '01uWt0000027PYPIA2', 'ListUnitPrice': '319.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVRhIAM'}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'ListUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVTJIA2'}, {'PricebookEntryId': '01uWt0000027PbdIAE', 'ListUnitPrice': '389.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVWXIA2'}, {'PricebookEntryId': '01uWt0000027PdFIAU', 'ListUnitPrice': '299.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVY9IAM'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'ListUnitPrice': '559.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVZlIAM'}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'ListUnitPrice': '349.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVbNIAU'}, {'PricebookEntryId': '01uWt0000027PgUIAU', 'ListUnitPrice': '379.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVt7IAE'}, {'PricebookEntryId': '01uWt0000027Pi5IAE', 'ListUnitPrice': '399.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'ListUnitPrice': '549.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVebIAE'}, {'PricebookEntryId': '01uWt0000027PlJIAU', 'ListUnitPrice': '499.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUsEIAU'}, {'PricebookEntryId': '#01uWt0000027PmvIAE', 'ListUnitPrice': '599.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVJeIAM'}, {'PricebookEntryId': '01uWt0000027PoXIAU', 'ListUnitPrice': '459.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVgDIAU'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'ListUnitPrice': '429.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjRIAU'}, {'PricebookEntryId': '01uWt0000027PrlIAE', 'ListUnitPrice': '369.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVl3IAE'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'ListUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVmfIAE'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'ListUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVwLIAU'}, {'PricebookEntryId': '01uWt0000027PuzIAE', 'ListUnitPrice': '629.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVoHIAU'}, {'PricebookEntryId': '01uWt0000027PwbIAE', 'ListUnitPrice': '559.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUUwIAM'}, {'PricebookEntryId': '#01uWt0000027PyDIAU', 'ListUnitPrice': '649.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVrVIAU'}, {'PricebookEntryId': '#01uWt0000027PzpIAE', 'ListUnitPrice': '429.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVrWIAU'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'ListUnitPrice': '579.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVujIAE'}, {'PricebookEntryId': '#01uWt0000027Q33IAE', 'ListUnitPrice': '499.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hOd8IAE'}, {'PricebookEntryId': '#01uWt0000027Q34IAE', 'ListUnitPrice': '599.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUgwIAE'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'ListUnitPrice': '299.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjSIAU'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'ListUnitPrice': '619.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUtqIAE'}], 'var_call_NtjbNwVJJRyky2MKuG0OYAoY': []}

exec(code, env_args)
