code = """import json, pandas as pd, re

qlis = pd.DataFrame(var_call_WABGa49eCkujCfTb4SVQmKt8)
cat = pd.DataFrame(var_call_3uv4Sq0tAoitg0zHIBq4Mqwy)

# normalize ids
for df,col in [(qlis,'PricebookEntryId'),(qlis,'Product2Id'),(cat,'PricebookEntryId'),(cat,'Product2Id')]:
    df[col] = df[col].astype(str).str.replace('#','', regex=False).str.strip()

# numeric
for c in ['Quantity','UnitPrice','Discount','TotalPrice']:
    qlis[c] = pd.to_numeric(qlis[c], errors='coerce')
cat['CatalogUnitPrice'] = pd.to_numeric(cat['CatalogUnitPrice'], errors='coerce')

m = qlis.merge(cat[['PricebookEntryId','CatalogUnitPrice','Product2Id','ProductName']], on='PricebookEntryId', how='left', suffixes=('','_cat'))

# detect potential invalid config
issues = []
# 1) Quantity unusually high
if (m['Quantity']>10).any():
    issues.append('high_quantity')
# 2) unit price mismatch vs catalog (tolerance small)
if ((m['CatalogUnitPrice'].notna()) & (abs(m['UnitPrice']-m['CatalogUnitPrice'])>0.01)).any():
    issues.append('unit_price_mismatch')
# 3) discount percent > 0 with nonstandard total (note total seems off for one line)
calc_total = m['Quantity']*m['UnitPrice']*(1 - (m['Discount'].fillna(0)/100.0))
if (abs(calc_total - m['TotalPrice'])>0.02).any():
    issues.append('total_price_incorrect')

# Load knowledge articles
import pathlib
ka_source = var_call_kW54XS8O7KTvhEEfwISPjdTL
if isinstance(ka_source, str) and ka_source.endswith('.json'):
    with open(ka_source,'r',encoding='utf-8') as f:
        kas = json.load(f)
else:
    kas = ka_source
ka_df = pd.DataFrame(kas)
for c in ['id','title','summary','faq_answer__c']:
    if c in ka_df.columns:
        ka_df[c] = ka_df[c].astype(str)

# heuristic match: find first article mentioning max quantity / quantity limit / bulk order / pricing calculation / discount policy
patterns = []
if 'high_quantity' in issues:
    patterns += [r'max(imum)?\s+quantity', r'quantity\s+limit', r'qty\s+limit', r'bulk\s+order', r'orders?\s+over\s+\d+']
if 'unit_price_mismatch' in issues:
    patterns += [r'pricebook', r'unit\s+price', r'catalog\s+price', r'pricing\s+must', r'list\s+price']
if 'total_price_incorrect' in issues:
    patterns += [r'total\s+price', r'pricing\s+calculation', r'calculate', r'discount\s+policy']

text = (ka_df.get('title','') + ' ' + ka_df.get('summary','') + ' ' + ka_df.get('faq_answer__c','')).str.lower()
score = pd.Series(0, index=ka_df.index, dtype=int)
for pat in patterns:
    score += text.str.contains(pat).astype(int)

# prefer highest score >0 else none
best_id = None
if len(score)>0 and score.max()>0:
    best_id = ka_df.loc[score.idxmax(),'id']

print('__RESULT__:')
print(json.dumps({'issues':issues,'best_article_id':best_id}))"""

env_args = {'var_call_WABGa49eCkujCfTb4SVQmKt8': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_kW54XS8O7KTvhEEfwISPjdTL': 'file_storage/call_kW54XS8O7KTvhEEfwISPjdTL.json', 'var_call_3uv4Sq0tAoitg0zHIBq4Mqwy': [{'PricebookEntryId': '01uWt0000027P3lIAE', 'CatalogUnitPrice': '499.99', 'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'CatalogUnitPrice': '599.99', 'Product2Id': '#01tWt000006hV58IAE', 'ProductName': 'SecureFlow Suite'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'CatalogUnitPrice': '399.99', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'PricebookEntryId': '#01uWt0000027P8bIAE', 'CatalogUnitPrice': '349.99', 'Product2Id': '01tWt000006hV6jIAE', 'ProductName': 'EcoPCB Creator   '}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'CatalogUnitPrice': '529.99', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech'}, {'PricebookEntryId': '01uWt0000027PADIA2', 'CatalogUnitPrice': '299.99', 'Product2Id': '01tWt000006hPffIAE', 'ProductName': 'DevVision IDE'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'CatalogUnitPrice': '399.99', 'Product2Id': '01tWt000006hVBZIA2', 'ProductName': 'EduTech Lab'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'CatalogUnitPrice': '529.99', 'Product2Id': '01tWt000006hVI1IAM', 'ProductName': 'AIOptics Vision'}, {'PricebookEntryId': '01uWt0000027PIJIA2', 'CatalogUnitPrice': '459.99', 'Product2Id': '01tWt000006hVptIAE', 'ProductName': 'DesignEdge Pro'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'CatalogUnitPrice': '399.99', 'Product2Id': '01tWt000006hPfgIAE', 'ProductName': 'EcoPower Convert'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'CatalogUnitPrice': '299.99', 'Product2Id': '01tWt000006hVMrIAM', 'ProductName': 'TrainEDU Suite'}, {'PricebookEntryId': '01uWt0000027PTZIA2', 'CatalogUnitPrice': '449.99', 'Product2Id': '01tWt000006hV0IIAU', 'ProductName': 'NextGen IDE'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'CatalogUnitPrice': '459.99', 'Product2Id': '01tWt000006hVUvIAM', 'ProductName': 'OptiEnergy Suite'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'CatalogUnitPrice': '339.99', 'Product2Id': '01tWt000006hVQ5IAM', 'ProductName': 'CircuitSync Pro'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'CatalogUnitPrice': '429.99', 'Product2Id': '01tWt000006hVQ6IAM', 'ProductName': 'VeriSim Express  '}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'CatalogUnitPrice': '529.99', 'Product2Id': '01tWt000006hVTJIA2', 'ProductName': 'IntegrGuard Secure'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'CatalogUnitPrice': '559.99', 'Product2Id': '01tWt000006hVZlIAM', 'ProductName': 'SecuManage Pro  '}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'CatalogUnitPrice': '349.99', 'Product2Id': '01tWt000006hVbNIAU', 'ProductName': 'EnergyReduce Pro'}, {'PricebookEntryId': '01uWt0000027PgUIAU', 'CatalogUnitPrice': '379.99', 'Product2Id': '01tWt000006hVt7IAE', 'ProductName': 'PCB EcoModel  '}, {'PricebookEntryId': '01uWt0000027Pi5IAE', 'CatalogUnitPrice': '399.99', 'Product2Id': '01tWt000006hVczIAE', 'ProductName': 'CollabDesign Studio'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'CatalogUnitPrice': '549.99', 'Product2Id': '01tWt000006hVebIAE', 'ProductName': 'CircuitAI Innovator'}, {'PricebookEntryId': '01uWt0000027PlJIAU', 'CatalogUnitPrice': '499.99', 'Product2Id': '01tWt000006hUsEIAU', 'ProductName': 'SimuCheck Ultra'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'CatalogUnitPrice': '429.99', 'Product2Id': '01tWt000006hVjRIAU', 'ProductName': 'Workflow Genius'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'CatalogUnitPrice': '399.99', 'Product2Id': '01tWt000006hVmfIAE', 'ProductName': 'EduTech Advance'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'CatalogUnitPrice': '529.99', 'Product2Id': '01tWt000006hVwLIAU', 'ProductName': 'SimulateX Edge'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'CatalogUnitPrice': '579.99', 'Product2Id': '01tWt000006hVujIAE', 'ProductName': 'CyberShield Core'}, {'PricebookEntryId': '#01uWt0000027Q33IAE', 'CatalogUnitPrice': '499.99', 'Product2Id': '01tWt000006hOd8IAE', 'ProductName': 'AutoLayout Master'}, {'PricebookEntryId': '#01uWt0000027Q34IAE', 'CatalogUnitPrice': '599.99', 'Product2Id': '01tWt000006hUgwIAE', 'ProductName': 'AI DesignShift'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'CatalogUnitPrice': '299.99', 'Product2Id': '01tWt000006hVjSIAU', 'ProductName': 'InnoTrain Hub'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'CatalogUnitPrice': '619.99', 'Product2Id': '01tWt000006hUtqIAE', 'ProductName': 'SecureTrack Pro '}], 'var_call_qtesGPjtdTWwVspkgzvrlGt5': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}]}

exec(code, env_args)
