code = """import json, pandas as pd

qlis = pd.DataFrame(var_call_FiWw8xFBqE0f81ZtukUJiFbg)
cat = pd.DataFrame(var_call_feqnlbSMgQwy7es9pB8gSyPh)

# normalize ids by stripping leading # and whitespace
for c in ['Product2Id','PricebookEntryId']:
    qlis[c+'_norm'] = qlis[c].astype(str).str.strip().str.lstrip('#')
cat['PricebookEntryId_norm'] = cat['PricebookEntryId'].astype(str).str.strip().str.lstrip('#')

# join to catalog unit price
m = qlis.merge(cat[['PricebookEntryId_norm','CatalogUnitPrice']], left_on='PricebookEntryId_norm', right_on='PricebookEntryId_norm', how='left')

# identify mismatches or discount issues (nonzero discount with high qty etc.)
# Here only clear policy-style violation: TotalPrice should equal Quantity*UnitPrice*(1-Discount/100)
# If not, it's invalid configuration.
for col in ['Quantity','UnitPrice','Discount','TotalPrice','CatalogUnitPrice']:
    if col in m.columns:
        m[col] = pd.to_numeric(m[col], errors='coerce')

m['expected_total'] = m['Quantity']*m['UnitPrice']*(1 - (m['Discount'].fillna(0)/100.0))
# tolerance cents
m['total_mismatch'] = (m['TotalPrice'] - m['expected_total']).abs() > 0.01

# also check if UnitPrice deviates from catalog unit price without discount (i.e., unit price must equal catalog, discount field used)
m['unitprice_mismatch_vs_catalog'] = (m['CatalogUnitPrice'].notna()) & ((m['UnitPrice'] - m['CatalogUnitPrice']).abs() > 0.01) & (m['Discount'].fillna(0)==0)

viol = m[m['total_mismatch'] | m['unitprice_mismatch_vs_catalog']]

ka_path = var_call_tQLkW1Oj79bGM01XBGcqsdOe
with open(ka_path,'r',encoding='utf-8') as f:
    kas = json.load(f)
ka_df = pd.DataFrame(kas)

# find knowledge article about quote/line item total price calculation / discount policy
# simple keyword search
text_cols = ['title','summary','faq_answer__c','urlname']
for c in text_cols:
    ka_df[c] = ka_df[c].astype(str)

keywords = ['quote','quotation','discount','unit price','totalprice','total price','pricing','price','quantity','calculation','calc','line item']
pattern = '|'.join([k.replace(' ','\\s+') for k in keywords])
mask = ka_df['title'].str.contains(pattern, case=False, regex=True) | ka_df['summary'].str.contains(pattern, case=False, regex=True) | ka_df['faq_answer__c'].str.contains(pattern, case=False, regex=True)
ka_cand = ka_df[mask].copy()

# If multiple, prioritize those mentioning total price calculation/discount must be applied via Discount field
pattern2 = r'total\\s*price|line\\s*item|unit\\s*price|discount'
ka_cand['score'] = (
    ka_cand['title'].str.count(pattern2, flags=0) +
    ka_cand['summary'].str.count(pattern2, flags=0) +
    ka_cand['faq_answer__c'].str.count(pattern2, flags=0)
)
ka_cand = ka_cand.sort_values('score', ascending=False)

# Determine if config invalid
invalid = len(viol) > 0
article_id = None
if invalid and len(ka_cand)>0:
    article_id = ka_cand.iloc[0]['id']

print('__RESULT__:')
print(json.dumps({'invalid': invalid, 'viol_rows': viol[['Id','Quantity','UnitPrice','Discount','TotalPrice','expected_total','CatalogUnitPrice']].to_dict(orient='records'), 'article_id': article_id}, default=str))"""

env_args = {'var_call_FiWw8xFBqE0f81ZtukUJiFbg': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_tQLkW1Oj79bGM01XBGcqsdOe': 'file_storage/call_tQLkW1Oj79bGM01XBGcqsdOe.json', 'var_call_feqnlbSMgQwy7es9pB8gSyPh': [{'PricebookEntryId': '01uWt0000027P3lIAE', 'CatalogUnitPrice': '499.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'CatalogUnitPrice': '599.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hV58IAE', 'ProductName': 'SecureFlow Suite'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'CatalogUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'PricebookEntryId': '#01uWt0000027P8bIAE', 'CatalogUnitPrice': '349.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV6jIAE', 'ProductName': 'EcoPCB Creator   '}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'CatalogUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech'}, {'PricebookEntryId': '01uWt0000027PADIA2', 'CatalogUnitPrice': '299.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'ProductName': 'DevVision IDE'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'CatalogUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVBZIA2', 'ProductName': 'EduTech Lab'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'CatalogUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVI1IAM', 'ProductName': 'AIOptics Vision'}, {'PricebookEntryId': '01uWt0000027PIJIA2', 'CatalogUnitPrice': '459.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVptIAE', 'ProductName': 'DesignEdge Pro'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'CatalogUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPfgIAE', 'ProductName': 'EcoPower Convert'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'CatalogUnitPrice': '299.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVMrIAM', 'ProductName': 'TrainEDU Suite'}, {'PricebookEntryId': '01uWt0000027PTZIA2', 'CatalogUnitPrice': '449.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV0IIAU', 'ProductName': 'NextGen IDE'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'CatalogUnitPrice': '459.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVUvIAM', 'ProductName': 'OptiEnergy Suite'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'CatalogUnitPrice': '339.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'ProductName': 'CircuitSync Pro'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'CatalogUnitPrice': '429.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ6IAM', 'ProductName': 'VeriSim Express  '}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'CatalogUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVTJIA2', 'ProductName': 'IntegrGuard Secure'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'CatalogUnitPrice': '559.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVZlIAM', 'ProductName': 'SecuManage Pro  '}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'CatalogUnitPrice': '349.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVbNIAU', 'ProductName': 'EnergyReduce Pro'}, {'PricebookEntryId': '01uWt0000027PgUIAU', 'CatalogUnitPrice': '379.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVt7IAE', 'ProductName': 'PCB EcoModel  '}, {'PricebookEntryId': '01uWt0000027Pi5IAE', 'CatalogUnitPrice': '399.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'ProductName': 'CollabDesign Studio'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'CatalogUnitPrice': '549.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVebIAE', 'ProductName': 'CircuitAI Innovator'}, {'PricebookEntryId': '01uWt0000027PlJIAU', 'CatalogUnitPrice': '499.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUsEIAU', 'ProductName': 'SimuCheck Ultra'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'CatalogUnitPrice': '429.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjRIAU', 'ProductName': 'Workflow Genius'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'CatalogUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVmfIAE', 'ProductName': 'EduTech Advance'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'CatalogUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVwLIAU', 'ProductName': 'SimulateX Edge'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'CatalogUnitPrice': '579.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVujIAE', 'ProductName': 'CyberShield Core'}, {'PricebookEntryId': '#01uWt0000027Q33IAE', 'CatalogUnitPrice': '499.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hOd8IAE', 'ProductName': 'AutoLayout Master'}, {'PricebookEntryId': '#01uWt0000027Q34IAE', 'CatalogUnitPrice': '599.99', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUgwIAE', 'ProductName': 'AI DesignShift'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'CatalogUnitPrice': '299.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjSIAU', 'ProductName': 'InnoTrain Hub'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'CatalogUnitPrice': '619.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUtqIAE', 'ProductName': 'SecureTrack Pro '}], 'var_call_RZvw1vsqf4Jr6ebxsQaEw6k9': []}

exec(code, env_args)
