code = """import json, pandas as pd, re
qli = pd.DataFrame(var_call_AmJkPllkP0QgiOyjGaCwnPjf)
pbe = pd.DataFrame(var_call_PBRwPSeWxUE98U45Oj9XSC6A)
# normalize ids
for col in ['Product2Id','PricebookEntryId','QuoteId','Id']:
    if col in qli.columns:
        qli[col] = qli[col].astype(str).str.replace('#','', regex=False).str.strip()
for col in ['Id','Product2Id','Pricebook2Id']:
    pbe[col] = pbe[col].astype(str).str.replace('#','', regex=False).str.strip()
# cast numeric
for col in ['Quantity','UnitPrice','Discount','TotalPrice']:
    qli[col] = pd.to_numeric(qli[col], errors='coerce')
pbe['UnitPrice'] = pd.to_numeric(pbe['UnitPrice'], errors='coerce')
# join to validate unit price matches pricebook entry
m = qli.merge(pbe[['Id','UnitPrice']], left_on='PricebookEntryId', right_on='Id', how='left', suffixes=('','_pbe'))
# determine violations
violations = []
# discount as percent between 0 and 100
if (m['Discount'].fillna(0) < 0).any() or (m['Discount'].fillna(0) > 100).any():
    violations.append('discount_range')
# quantity positive integer
if (m['Quantity'].isna() | (m['Quantity']<=0) | (m['Quantity']%1!=0)).any():
    violations.append('quantity_positive_integer')
# unit price matches pricebook entry (when available)
if ((~m['UnitPrice_pbe'].isna()) & (abs(m['UnitPrice']-m['UnitPrice_pbe'])>1e-6)).any():
    violations.append('unitprice_must_match_pricebook')
# total price matches formula: qty*unitprice*(1-discount/100)
calc = m['Quantity']*m['UnitPrice']*(1-m['Discount'].fillna(0)/100.0)
if (abs(m['TotalPrice']-calc)>0.01).any():
    violations.append('totalprice_calculation')
# detect the specific issue: one line has 35 qty and 15 discount, totalprice 11899.7025 looks like discount treated as 15x not 15%? expected 35*399.99*0.85=11899.7025 actually matches, so no violation.
# So likely no violations in numeric consistency. Need check regulation like max quantity per line (e.g., <= 30). We'll infer from knowledge articles text.
# load knowledge articles
import pathlib
path = var_call_hSaxaBR4pa2RaGOpSDLKf10U
if isinstance(path,str) and path.endswith('.json'):
    arts = json.load(open(path,'r'))
else:
    arts = var_call_hSaxaBR4pa2RaGOpSDLKf10U
# find articles mentioning quantity limits, discount limits, pricebook, approval thresholds
candidates=[]
pattern = re.compile(r"(quantity|qty|discount|unit price|pricebook|pricing|approval|limit|max|minimum|bundle)", re.I)
for a in arts:
    text = (str(a.get('title',''))+' '+str(a.get('summary',''))+' '+str(a.get('faq_answer__c','')))
    if pattern.search(text):
        candidates.append(a)
# now search for max quantity per line; use 35 as potential violation
maxqty_candidates=[]
for a in candidates:
    txt = (a.get('title','') or '')+' '+(a.get('summary','') or '')+' '+(a.get('faq_answer__c','') or '')
    if re.search(r"max(imum)?\s+(order\s+)?(quantity|qty).{0,30}(\d+)", txt, re.I) or re.search(r"quantity\s+(must|should)\s+be\s+(less\s+than|under|<=)\s*(\d+)", txt, re.I):
        maxqty_candidates.append(a)
# heuristic: if any article mentions 30 and quantity 35 exists -> violation
viol_id=None
qty_max=None
for a in maxqty_candidates:
    txt = a.get('faq_answer__c','') or ''
    nums = [int(x) for x in re.findall(r"\b(\d{1,3})\b", txt)]
    if nums:
        # choose smallest plausible limit between 5 and 200
        lims=[n for n in nums if 5<=n<=200]
        if lims:
            lim=min(lims)
            if qty_max is None or lim<qty_max:
                qty_max=lim; viol_id=a['id'].replace('#','').strip()
# if no maxqty found, look for any article about needing approval for quantity > 30 or discounts > 10 etc.
if viol_id is None:
    for a in candidates:
        txt=(a.get('faq_answer__c','') or '')
        if 'quantity' in txt.lower() and re.search(r">\s*30|over\s*30|more\s+than\s*30", txt, re.I):
            viol_id=a['id'].replace('#','').strip(); break
# fallback: if no explicit, assume no violation
result = viol_id if viol_id is not None else None
print('__RESULT__:')
print(json.dumps({'knowledge_article_id': result, 'detected_rule_types': violations}))"""

env_args = {'var_call_AmJkPllkP0QgiOyjGaCwnPjf': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97', 'OpportunityLineItemId': '00kWt000002HUwhIAG'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98', 'OpportunityLineItemId': '00kWt000002HHRkIAO'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96', 'OpportunityLineItemId': '00kWt000002HQJYIA4'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025', 'OpportunityLineItemId': '00kWt000002HQJZIA4'}], 'var_call_hSaxaBR4pa2RaGOpSDLKf10U': 'file_storage/call_hSaxaBR4pa2RaGOpSDLKf10U.json', 'var_call_PBRwPSeWxUE98U45Oj9XSC6A': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027P3mIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVhpIAE', 'UnitPrice': '489.99'}, {'Id': '01uWt0000027P5NIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hV58IAE', 'UnitPrice': '599.99'}, {'Id': '#01uWt0000027P6zIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hTUkIAM', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027P8bIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV6jIAE', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027PBpIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV9xIAE', 'UnitPrice': '449.99'}, {'Id': '01uWt0000027PDRIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVBZIA2', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PF3IAM', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVDBIA2', 'UnitPrice': '549.99'}, {'Id': '#01uWt0000027PGfIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVEnIAM', 'UnitPrice': '479.99'}, {'Id': '01uWt0000027PIHIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVGPIA2', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PIIIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVI1IAM', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PIJIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVptIAE', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PJtIAM', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVJdIAM', 'UnitPrice': '649.99'}, {'Id': '01uWt0000027PLVIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVLFIA2', 'UnitPrice': '459.99'}, {'Id': '#01uWt0000027PN7IAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPfgIAE', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027POjIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVMrIAM', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027POkIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hRfqIAE', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027PQLIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hUKMIA2', 'UnitPrice': '489.99'}, {'Id': '#01uWt0000027PRxIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVOTIA2', 'UnitPrice': '559.99'}, {'Id': '01uWt0000027PTZIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV0IIAU', 'UnitPrice': '449.99'}, {'Id': '#01uWt0000027PTaIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVUvIAM', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}, {'Id': '#01uWt0000027PWnIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ6IAM', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027PYPIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVRhIAM', 'UnitPrice': '319.99'}, {'Id': '01uWt0000027Pa1IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVTJIA2', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PbdIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVWXIA2', 'UnitPrice': '389.99'}, {'Id': '01uWt0000027PdFIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVY9IAM', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027PerIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVZlIAM', 'UnitPrice': '559.99'}, {'Id': '01uWt0000027PgTIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVbNIAU', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027PgUIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVt7IAE', 'UnitPrice': '379.99'}, {'Id': '01uWt0000027Pi5IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PjhIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVebIAE', 'UnitPrice': '549.99'}, {'Id': '01uWt0000027PlJIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUsEIAU', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027PmvIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVJeIAM', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PoXIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVgDIAU', 'UnitPrice': '459.99'}, {'Id': '#01uWt0000027Pq9IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjRIAU', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027PrlIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVl3IAE', 'UnitPrice': '369.99'}, {'Id': '#01uWt0000027PtNIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVmfIAE', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PtOIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVwLIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PuzIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVoHIAU', 'UnitPrice': '629.99'}, {'Id': '01uWt0000027PwbIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUUwIAM', 'UnitPrice': '559.99'}, {'Id': '#01uWt0000027PyDIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVrVIAU', 'UnitPrice': '649.99'}, {'Id': '#01uWt0000027PzpIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVrWIAU', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027Q1RIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVujIAE', 'UnitPrice': '579.99'}, {'Id': '#01uWt0000027Q33IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hOd8IAE', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027Q34IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUgwIAE', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027Q4fIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjSIAU', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Q6HIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUtqIAE', 'UnitPrice': '619.99'}], 'var_call_dXMq58QV6T8GHNtRjh1Kkz4F': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}]}

exec(code, env_args)
