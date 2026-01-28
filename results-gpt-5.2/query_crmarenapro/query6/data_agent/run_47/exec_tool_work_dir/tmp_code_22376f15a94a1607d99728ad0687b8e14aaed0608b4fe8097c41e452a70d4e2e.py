code = """import json, pandas as pd

qlis = var_call_ioSgHQlSsIxCHiiCz0LaKw8l
pbes = var_call_CtZikFwhAYUvknVAaj60J0Vg

qdf = pd.DataFrame(qlis)
pdf = pd.DataFrame(pbes)

# normalize ids and numeric fields
for col in ['QuoteId','Product2Id','PricebookEntryId','Id']:
    if col in qdf.columns:
        qdf[col] = qdf[col].astype(str).str.replace('#','', regex=False).str.strip()

for col in ['PricebookEntryId','Product2Id','Pricebook2Id']:
    if col in pdf.columns:
        pdf[col] = pdf[col].astype(str).str.replace('#','', regex=False).str.strip()

for col in ['Quantity','UnitPrice','Discount','TotalPrice','ListUnitPrice']:
    if col in qdf.columns:
        qdf[col] = pd.to_numeric(qdf[col], errors='coerce')
    if col in pdf.columns:
        pdf[col] = pd.to_numeric(pdf[col], errors='coerce')

m = qdf.merge(pdf[['PricebookEntryId','ListUnitPrice']], on='PricebookEntryId', how='left')

# detect violations
violations = []
# pricebook entry missing
if m['ListUnitPrice'].isna().any():
    violations.append('missing_pricebook_entry')

# unit price mismatch (expect equals list, assuming discount handled separately)
# if discount present, expected total = qty*unit*(1-discount/100)
# also flag if unit price differs from list by >0.01 without explanation
m['expected_total'] = m['Quantity'] * m['UnitPrice'] * (1 - (m['Discount'].fillna(0)/100.0))

if ((m['TotalPrice'] - m['expected_total']).abs() > 0.02).any():
    violations.append('total_price_mismatch')

if ((m['UnitPrice'] - m['ListUnitPrice']).abs() > 0.02).any():
    violations.append('unit_price_not_list')

# quantity rule heuristic: unusually high quantity (>=25) requires special approval
if (m['Quantity'] >= 25).any():
    violations.append('high_quantity_requires_approval')

# find relevant knowledge article by keyword search in title/summary/faq
import pathlib
path = var_call_Wou0oQOb7YgGvjD8uLPo64aY
arts = json.load(open(path,'r',encoding='utf-8'))
adf = pd.DataFrame(arts)
for c in ['id','title','summary','faq_answer__c']:
    adf[c] = adf[c].astype(str)

kw_map = {
    'missing_pricebook_entry': ['pricebook','price book','pricebook entry','not in pricebook'],
    'unit_price_not_list': ['unit price','list price','pricebook','pricing','must match'],
    'total_price_mismatch': ['total price','calculation','discount'],
    'high_quantity_requires_approval': ['quantity','bulk','volume','approval','maximum']
}

picked_id = None
# prioritize pricing/pricebook violations, then quantity
priority = ['missing_pricebook_entry','unit_price_not_list','total_price_mismatch','high_quantity_requires_approval']

for v in priority:
    if v not in violations:
        continue
    kws = kw_map[v]
    patt = '|'.join([pd.regex.escape(k) if hasattr(pd,'regex') else k for k in kws])
    # simple contains checks
    mask = adf['title'].str.contains('|'.join(kws), case=False, na=False) | adf['summary'].str.contains('|'.join(kws), case=False, na=False) | adf['faq_answer__c'].str.contains('|'.join(kws), case=False, na=False)
    if mask.any():
        picked_id = adf.loc[mask, 'id'].iloc[0]
        break

# fallback: if high quantity violation, pick article that mentions discount approval/volume if any
if picked_id is None and violations:
    # broad search for 'quote' and 'policy'
    mask = adf['title'].str.contains('policy|pricing|discount|quote|approval', case=False, na=False) | adf['summary'].str.contains('policy|pricing|discount|quote|approval', case=False, na=False)
    if mask.any():
        picked_id = adf.loc[mask,'id'].iloc[0]

print('__RESULT__:')
print(json.dumps({'violations': violations, 'article_id': picked_id}))"""

env_args = {'var_call_ioSgHQlSsIxCHiiCz0LaKw8l': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_CtZikFwhAYUvknVAaj60J0Vg': [{'PricebookEntryId': '01uWt0000027P5NIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hV58IAE', 'ListUnitPrice': '599.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'SecureFlow Suite', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hTUkIAM', 'ListUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'CloudLink Designer', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'ListUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'AI Cirku-Tech', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVBZIA2', 'ListUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'EduTech Lab', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVI1IAM', 'ListUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'AIOptics Vision', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPfgIAE', 'ListUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'EcoPower Convert', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVMrIAM', 'ListUnitPrice': '299.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'TrainEDU Suite', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVUvIAM', 'ListUnitPrice': '459.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'OptiEnergy Suite', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'ListUnitPrice': '339.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'CircuitSync Pro', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ6IAM', 'ListUnitPrice': '429.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'VeriSim Express  ', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVTJIA2', 'ListUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'IntegrGuard Secure', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVZlIAM', 'ListUnitPrice': '559.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'SecuManage Pro  ', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVbNIAU', 'ListUnitPrice': '349.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'EnergyReduce Pro', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVebIAE', 'ListUnitPrice': '549.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'CircuitAI Innovator', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjRIAU', 'ListUnitPrice': '429.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'Workflow Genius', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVmfIAE', 'ListUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'EduTech Advance', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVwLIAU', 'ListUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'SimulateX Edge', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVujIAE', 'ListUnitPrice': '579.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'CyberShield Core', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjSIAU', 'ListUnitPrice': '299.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'InnoTrain Hub', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUtqIAE', 'ListUnitPrice': '619.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'SecureTrack Pro ', 'ProductIsActive': '1'}], 'var_call_Wou0oQOb7YgGvjD8uLPo64aY': 'file_storage/call_Wou0oQOb7YgGvjD8uLPo64aY.json', 'var_call_u7GQMzwQZxbrngUn4N9DTEQ2': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.'}]}

exec(code, env_args)
