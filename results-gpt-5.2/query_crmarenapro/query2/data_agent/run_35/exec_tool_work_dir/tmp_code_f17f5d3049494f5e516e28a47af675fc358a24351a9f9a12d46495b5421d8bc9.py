code = """import json, pandas as pd

quote = pd.DataFrame(var_call_0RdfwClz8CxuVfiCP3dIJRZm)
qli = pd.DataFrame(var_call_S8VU3jed4DqIFIrBQyucn3W5)
pbe = pd.DataFrame(var_call_pajVweDyq5BWBrTog0jqpSMs)

# normalize ids
for df, col in [(qli,'PricebookEntryId'),(qli,'Product2Id')]:
    if col in df.columns:
        df[col+'_norm'] = df[col].astype(str).str.replace('#','', regex=False).str.strip()
for col in ['Id']:
    pbe[col+'_norm'] = pbe[col].astype(str).str.replace('#','', regex=False).str.strip()

# join to get list price
merged = qli.merge(pbe, left_on='PricebookEntryId_norm', right_on='Id_norm', how='left', suffixes=('','_pbe'))
# numeric
for c in ['Quantity','UnitPrice','Discount','TotalPrice','UnitPrice_pbe']:
    if c in merged.columns:
        merged[c] = pd.to_numeric(merged[c], errors='coerce')

merged['discount_pct'] = merged['Discount']
merged['list_unit_price'] = merged['UnitPrice_pbe']
merged['unit_price_matches_list'] = (merged['UnitPrice'].round(2) == merged['list_unit_price'].round(2))

# find max discount
max_disc = float(merged['discount_pct'].max()) if len(merged) else 0.0

# Load knowledge articles
path = var_call_BByJPf12iWXayxwb0ZS0ZzeJ
with open(path,'r',encoding='utf-8') as f:
    kav = json.load(f)

kdf = pd.DataFrame(kav)
for col in ['id','title','faq_answer__c','summary','urlname']:
    if col in kdf.columns:
        kdf[col] = kdf[col].astype(str)

# Heuristic: find policy on discounts/setup; look for 10% cap or discount approval rules.
text = (kdf['title'].fillna('') + ' ' + kdf['summary'].fillna('') + ' ' + kdf['faq_answer__c'].fillna('')).str.lower()
keywords = ['discount','discounts','pricing','price','quote','approval','setup','implementation','onboarding','professional services','tco','roi']
mask = False
for kw in keywords:
    mask = mask | text.str.contains(kw)
policy_candidates = kdf[mask].copy()

# Determine violation: any discount >10% (common policy). If so, pick best matching policy article mentioning discount limit/cap/approval.
violation = max_disc > 10.0
violating_id = None
if violation and len(policy_candidates):
    cand_text = (policy_candidates['title']+' '+policy_candidates['summary']+' '+policy_candidates['faq_answer__c']).str.lower()
    score = (
        cand_text.str.count('discount')*3 +
        cand_text.str.count('quote')*2 +
        cand_text.str.count('approval')*2 +
        cand_text.str.count('setup') +
        cand_text.str.count('implementation')
    )
    # boost if mentions 10% or 'ten percent'
    score = score + cand_text.str.contains('10%').astype(int)*10 + cand_text.str.contains('ten percent').astype(int)*10 + cand_text.str.contains('discount cap').astype(int)*6
    best_idx = score.idxmax()
    violating_id = policy_candidates.loc[best_idx,'id']

out = {'max_discount_pct': max_disc, 'violation': violation, 'violating_article_id': violating_id}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_0RdfwClz8CxuVfiCP3dIJRZm': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_S8VU3jed4DqIFIrBQyucn3W5': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_BByJPf12iWXayxwb0ZS0ZzeJ': 'file_storage/call_BByJPf12iWXayxwb0ZS0ZzeJ.json', 'var_call_pajVweDyq5BWBrTog0jqpSMs': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99', 'ProductName': 'PulseSim Pro'}, {'Id': '01uWt0000027P5NIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hV58IAE', 'UnitPrice': '599.99', 'ProductName': 'SecureFlow Suite'}, {'Id': '#01uWt0000027P6zIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hTUkIAM', 'UnitPrice': '399.99', 'ProductName': 'CloudLink Designer'}, {'Id': '#01uWt0000027P8bIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV6jIAE', 'UnitPrice': '349.99', 'ProductName': 'EcoPCB Creator   '}, {'Id': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'UnitPrice': '529.99', 'ProductName': 'AI Cirku-Tech'}, {'Id': '01uWt0000027PADIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'UnitPrice': '299.99', 'ProductName': 'DevVision IDE'}, {'Id': '01uWt0000027PDRIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVBZIA2', 'UnitPrice': '399.99', 'ProductName': 'EduTech Lab'}, {'Id': '01uWt0000027PIIIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVI1IAM', 'UnitPrice': '529.99', 'ProductName': 'AIOptics Vision'}, {'Id': '01uWt0000027PIJIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVptIAE', 'UnitPrice': '459.99', 'ProductName': 'DesignEdge Pro'}, {'Id': '#01uWt0000027PN7IAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPfgIAE', 'UnitPrice': '399.99', 'ProductName': 'EcoPower Convert'}, {'Id': '#01uWt0000027POjIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVMrIAM', 'UnitPrice': '299.99', 'ProductName': 'TrainEDU Suite'}, {'Id': '01uWt0000027PTZIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV0IIAU', 'UnitPrice': '449.99', 'ProductName': 'NextGen IDE'}, {'Id': '#01uWt0000027PTaIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVUvIAM', 'UnitPrice': '459.99', 'ProductName': 'OptiEnergy Suite'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99', 'ProductName': 'CircuitSync Pro'}, {'Id': '#01uWt0000027PWnIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ6IAM', 'UnitPrice': '429.99', 'ProductName': 'VeriSim Express  '}, {'Id': '01uWt0000027Pa1IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVTJIA2', 'UnitPrice': '529.99', 'ProductName': 'IntegrGuard Secure'}, {'Id': '01uWt0000027PerIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVZlIAM', 'UnitPrice': '559.99', 'ProductName': 'SecuManage Pro  '}, {'Id': '01uWt0000027PgTIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVbNIAU', 'UnitPrice': '349.99', 'ProductName': 'EnergyReduce Pro'}, {'Id': '01uWt0000027PgUIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVt7IAE', 'UnitPrice': '379.99', 'ProductName': 'PCB EcoModel  '}, {'Id': '01uWt0000027Pi5IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'UnitPrice': '399.99', 'ProductName': 'CollabDesign Studio'}, {'Id': '01uWt0000027PjhIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVebIAE', 'UnitPrice': '549.99', 'ProductName': 'CircuitAI Innovator'}, {'Id': '01uWt0000027PlJIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUsEIAU', 'UnitPrice': '499.99', 'ProductName': 'SimuCheck Ultra'}, {'Id': '#01uWt0000027Pq9IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjRIAU', 'UnitPrice': '429.99', 'ProductName': 'Workflow Genius'}, {'Id': '#01uWt0000027PtNIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVmfIAE', 'UnitPrice': '399.99', 'ProductName': 'EduTech Advance'}, {'Id': '01uWt0000027PtOIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVwLIAU', 'UnitPrice': '529.99', 'ProductName': 'SimulateX Edge'}, {'Id': '01uWt0000027Q1RIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVujIAE', 'UnitPrice': '579.99', 'ProductName': 'CyberShield Core'}, {'Id': '#01uWt0000027Q33IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hOd8IAE', 'UnitPrice': '499.99', 'ProductName': 'AutoLayout Master'}, {'Id': '#01uWt0000027Q34IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUgwIAE', 'UnitPrice': '599.99', 'ProductName': 'AI DesignShift'}, {'Id': '01uWt0000027Q4fIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjSIAU', 'UnitPrice': '299.99', 'ProductName': 'InnoTrain Hub'}, {'Id': '01uWt0000027Q6HIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUtqIAE', 'UnitPrice': '619.99', 'ProductName': 'SecureTrack Pro '}]}

exec(code, env_args)
