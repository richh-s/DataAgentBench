code = """import json, pandas as pd

qlis = pd.DataFrame(var_call_on3Od3qO1100P8rqbIS5l9ia)
pbe = pd.DataFrame(var_call_cddtKnttXnTfMrX2gl71xMxI)

# normalize ids by stripping leading '#'
for c in ['Product2Id','PricebookEntryId','QuoteId','Id']:
    if c in qlis.columns:
        qlis[c+'_norm'] = qlis[c].astype(str).str.strip().str.lstrip('#')
for c in ['PricebookEntryId','Product2Id']:
    if c in pbe.columns:
        pbe[c+'_norm'] = pbe[c].astype(str).str.strip().str.lstrip('#')

# numeric conversions
for c in ['Quantity','UnitPrice','Discount','TotalPrice']:
    qlis[c] = pd.to_numeric(qlis[c], errors='coerce')
pbe['CatalogUnitPrice'] = pd.to_numeric(pbe['CatalogUnitPrice'], errors='coerce')

m = qlis.merge(pbe, left_on='PricebookEntryId_norm', right_on='PricebookEntryId_norm', how='left', suffixes=('','_cat'))

# detect unit price mismatch vs catalog (regulation: must match pricebook entry unit price unless discount is used)
# here discount is present but UnitPrice should still equal catalog; discount should be in Discount field.
m['unit_price_mismatch'] = (m['CatalogUnitPrice'].notna()) & ((m['UnitPrice'] - m['CatalogUnitPrice']).abs() > 1e-6)

# detect total price mismatch vs expected total after discount
m['expected_total'] = m['Quantity'] * m['UnitPrice'] * (1 - (m['Discount'].fillna(0)/100.0))
m['total_mismatch'] = (m['TotalPrice'] - m['expected_total']).abs() > 0.01

violations = m[m['unit_price_mismatch'] | m['total_mismatch']]

# load knowledge articles
import pathlib
path = var_call_GiPc72IlHcqO3MNexjN8azi3
arts = pd.DataFrame(json.load(open(path,'r',encoding='utf-8')))
arts['text'] = (arts['title'].fillna('') + ' ' + arts['summary'].fillna('') + ' ' + arts['faq_answer__c'].fillna('')).str.lower()

# pick best matching regulation article based on keywords
keywords = ['discount','unit price','pricebook','pricing','quote line','quantity','total price']
pattern = '|'.join([pd.regex.escape(k) for k in keywords]) if hasattr(pd,'regex') else None
# pandas doesn't have pd.regex; use python re
import re
rx = re.compile('|'.join([re.escape(k) for k in keywords]))
arts['kw_hits'] = arts['text'].apply(lambda t: len(rx.findall(t)))
reg_arts = arts[arts['kw_hits']>0].copy()

# if none found, fallback to empty
chosen_id = None
if len(violations)>0 and len(reg_arts)>0:
    chosen_id = reg_arts.sort_values(['kw_hits'], ascending=False).iloc[0]['id']

result = {'chosen_id': chosen_id, 'violations_count': int(len(violations))}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_on3Od3qO1100P8rqbIS5l9ia': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_cddtKnttXnTfMrX2gl71xMxI': [{'PricebookEntryId': '01uWt0000027P5NIAU', 'CatalogUnitPrice': '599.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hV58IAE', 'ProductName': 'SecureFlow Suite', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'CatalogUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'CatalogUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'CatalogUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVBZIA2', 'ProductName': 'EduTech Lab', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'CatalogUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVI1IAM', 'ProductName': 'AIOptics Vision', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'CatalogUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPfgIAE', 'ProductName': 'EcoPower Convert', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'CatalogUnitPrice': '299.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVMrIAM', 'ProductName': 'TrainEDU Suite', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'CatalogUnitPrice': '459.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVUvIAM', 'ProductName': 'OptiEnergy Suite', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'CatalogUnitPrice': '339.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'ProductName': 'CircuitSync Pro', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'CatalogUnitPrice': '429.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ6IAM', 'ProductName': 'VeriSim Express  ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'CatalogUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVTJIA2', 'ProductName': 'IntegrGuard Secure', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'CatalogUnitPrice': '559.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVZlIAM', 'ProductName': 'SecuManage Pro  ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'CatalogUnitPrice': '349.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVbNIAU', 'ProductName': 'EnergyReduce Pro', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'CatalogUnitPrice': '549.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVebIAE', 'ProductName': 'CircuitAI Innovator', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'CatalogUnitPrice': '429.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjRIAU', 'ProductName': 'Workflow Genius', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'CatalogUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVmfIAE', 'ProductName': 'EduTech Advance', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'CatalogUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVwLIAU', 'ProductName': 'SimulateX Edge', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'CatalogUnitPrice': '579.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVujIAE', 'ProductName': 'CyberShield Core', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'CatalogUnitPrice': '299.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjSIAU', 'ProductName': 'InnoTrain Hub', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'CatalogUnitPrice': '619.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUtqIAE', 'ProductName': 'SecureTrack Pro ', 'PricebookName': 'Standard Price Book'}], 'var_call_GiPc72IlHcqO3MNexjN8azi3': 'file_storage/call_GiPc72IlHcqO3MNexjN8azi3.json', 'var_call_4kAncPhQQeP7h6yx9668xai8': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}]}

exec(code, env_args)
