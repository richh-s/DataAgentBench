code = """import json, pandas as pd, re
from pathlib import Path

qli = pd.DataFrame(var_call_dSa8597cWcc4XVqaLyV1GHqY)
pbe = pd.DataFrame(var_call_cqi2Aa33fqTxZS9ebVUSN0Pz)

# normalize ids
for df, col in [(qli,'PricebookEntryId'),(qli,'Product2Id'),(pbe,'Id'),(pbe,'Product2Id')]:
    if col in df.columns:
        df[col+'_n'] = df[col].astype(str).str.replace('#','', regex=False).str.strip()

# numeric
for col in ['Quantity','UnitPrice','Discount','TotalPrice','UnitPrice']:
    if col in qli.columns:
        qli[col] = pd.to_numeric(qli[col], errors='coerce')

pbe['UnitPrice'] = pd.to_numeric(pbe['UnitPrice'], errors='coerce')

m = qli.merge(pbe, left_on='PricebookEntryId_n', right_on='Id_n', how='left', suffixes=('','_pb'))

# identify violations:
violations = []
# 1) unitprice must match pricebook entry (no arbitrary price overrides)
price_mismatch = m[(m['UnitPrice'].notna()) & (m['UnitPrice_pb'].notna()) & ((m['UnitPrice'] - m['UnitPrice_pb']).abs() > 1e-6)]
if len(price_mismatch)>0:
    violations.append('PRICE_OVERRIDE_NOT_ALLOWED')

# 2) quantity must be integer positive
qty_bad = qli[(qli['Quantity'].isna()) | (qli['Quantity']<=0) | (qli['Quantity']%1!=0)]
if len(qty_bad)>0:
    violations.append('INVALID_QUANTITY')

# 3) discount must be between 0 and 1? or 0-100; unclear. detect >1 and <=100 treat as percent; compute total
# Here discount appears 15.0 and totalprice computed as qty*unit*(1-discount/100) -> ok.

# choose most likely: price mismatch exists?
# check mismatch
price_mismatch_ids = price_mismatch['Id'].tolist() if 'Id' in price_mismatch.columns else []

# Load knowledge articles from file
ka_src = var_call_AobDgGmsKM1J7TkghkOppBWN
if isinstance(ka_src, str) and ka_src.endswith('.json'):
    ka_records = json.loads(Path(ka_src).read_text())
else:
    ka_records = ka_src
ka = pd.DataFrame(ka_records)

# find relevant article by keyword matching
text_cols = ['title','summary','faq_answer__c','urlname']
ka['_text'] = ka[text_cols].fillna('').agg(' '.join, axis=1).str.lower()

# mapping from violation to keywords
violation_keywords = {
    'PRICE_OVERRIDE_NOT_ALLOWED': [
        'price override', 'override unit price', 'must match pricebook', 'pricebook entry', 'unit price must',
        'do not change unit price', 'pricing policy', 'standard pricing'
    ],
    'INVALID_QUANTITY': [
        'quantity', 'minimum order', 'must be whole number', 'integer quantity'
    ]
}

chosen_violation = 'PRICE_OVERRIDE_NOT_ALLOWED' if 'PRICE_OVERRIDE_NOT_ALLOWED' in violations else (violations[0] if violations else None)

best_id = None
if chosen_violation:
    kws = violation_keywords.get(chosen_violation, [])
    scores = []
    for _, row in ka.iterrows():
        t = row['_text']
        score = sum(1 for kw in kws if kw in t)
        # also boost if contains 'quote' 'pricebook'
        if 'pricebook' in t and chosen_violation=='PRICE_OVERRIDE_NOT_ALLOWED':
            score += 1
        scores.append(score)
    ka['score'] = scores
    ka_best = ka.sort_values(['score'], ascending=False).head(20)
    top = ka_best.iloc[0]
    if int(top['score'])>0:
        best_id = top['id']

# If no keyword match, fall back to any article mentioning pricebook/unit price/discount rules
if best_id is None:
    fallback = ka[ka['_text'].str.contains('pricebook|unit price|discount|quote', regex=True, na=False)]
    if len(fallback)>0:
        best_id = fallback.iloc[0]['id']

result = best_id if best_id is not None else ''
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_dSa8597cWcc4XVqaLyV1GHqY': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_AobDgGmsKM1J7TkghkOppBWN': 'file_storage/call_AobDgGmsKM1J7TkghkOppBWN.json', 'var_call_cqi2Aa33fqTxZS9ebVUSN0Pz': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027P3mIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVhpIAE', 'UnitPrice': '489.99'}, {'Id': '01uWt0000027P5NIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hV58IAE', 'UnitPrice': '599.99'}, {'Id': '#01uWt0000027P6zIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hTUkIAM', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027P8bIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV6jIAE', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027PBpIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV9xIAE', 'UnitPrice': '449.99'}, {'Id': '01uWt0000027PDRIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVBZIA2', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PF3IAM', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVDBIA2', 'UnitPrice': '549.99'}, {'Id': '#01uWt0000027PGfIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVEnIAM', 'UnitPrice': '479.99'}, {'Id': '01uWt0000027PIHIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVGPIA2', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PIIIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVI1IAM', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PIJIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVptIAE', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PJtIAM', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVJdIAM', 'UnitPrice': '649.99'}, {'Id': '01uWt0000027PLVIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVLFIA2', 'UnitPrice': '459.99'}, {'Id': '#01uWt0000027PN7IAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPfgIAE', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027POjIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVMrIAM', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027POkIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hRfqIAE', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027PQLIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hUKMIA2', 'UnitPrice': '489.99'}, {'Id': '#01uWt0000027PRxIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVOTIA2', 'UnitPrice': '559.99'}, {'Id': '01uWt0000027PTZIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV0IIAU', 'UnitPrice': '449.99'}, {'Id': '#01uWt0000027PTaIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVUvIAM', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}, {'Id': '#01uWt0000027PWnIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ6IAM', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027PYPIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVRhIAM', 'UnitPrice': '319.99'}, {'Id': '01uWt0000027Pa1IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVTJIA2', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PbdIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVWXIA2', 'UnitPrice': '389.99'}, {'Id': '01uWt0000027PdFIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVY9IAM', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027PerIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVZlIAM', 'UnitPrice': '559.99'}, {'Id': '01uWt0000027PgTIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVbNIAU', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027PgUIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVt7IAE', 'UnitPrice': '379.99'}, {'Id': '01uWt0000027Pi5IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PjhIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVebIAE', 'UnitPrice': '549.99'}, {'Id': '01uWt0000027PlJIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUsEIAU', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027PmvIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVJeIAM', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PoXIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVgDIAU', 'UnitPrice': '459.99'}, {'Id': '#01uWt0000027Pq9IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjRIAU', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027PrlIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVl3IAE', 'UnitPrice': '369.99'}, {'Id': '#01uWt0000027PtNIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVmfIAE', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PtOIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVwLIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PuzIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVoHIAU', 'UnitPrice': '629.99'}, {'Id': '01uWt0000027PwbIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUUwIAM', 'UnitPrice': '559.99'}, {'Id': '#01uWt0000027PyDIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVrVIAU', 'UnitPrice': '649.99'}, {'Id': '#01uWt0000027PzpIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVrWIAU', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027Q1RIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVujIAE', 'UnitPrice': '579.99'}, {'Id': '#01uWt0000027Q33IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hOd8IAE', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027Q34IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUgwIAE', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027Q4fIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjSIAU', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Q6HIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUtqIAE', 'UnitPrice': '619.99'}], 'var_call_QJRxOItv5mQwb5NE7JDlrZVo': [{'Id': '01tWt000006hOd8IAE', 'Name': 'AutoLayout Master', 'IsActive': '1'}, {'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE', 'IsActive': '1'}, {'Id': '01tWt000006hPfgIAE', 'Name': 'EcoPower Convert', 'IsActive': '1'}, {'Id': '01tWt000006hRfqIAE', 'Name': 'FlexiDesign Pro', 'IsActive': '1'}, {'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer', 'IsActive': '1'}, {'Id': '01tWt000006hUKMIA2', 'Name': 'CryptGuard Module', 'IsActive': '1'}, {'Id': '#01tWt000006hUUwIAM', 'Name': 'SimuFlow Xtreme', 'IsActive': '1'}, {'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift', 'IsActive': '1'}, {'Id': '01tWt000006hUsEIAU', 'Name': 'SimuCheck Ultra', 'IsActive': '1'}, {'Id': '01tWt000006hUtqIAE', 'Name': 'SecureTrack Pro ', 'IsActive': '1'}, {'Id': '01tWt000006hV0IIAU', 'Name': 'NextGen IDE', 'IsActive': '1'}, {'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'IsActive': '1'}, {'Id': '#01tWt000006hV58IAE', 'Name': 'SecureFlow Suite', 'IsActive': '1'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   ', 'IsActive': '1'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'IsActive': '1'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager', 'IsActive': '1'}, {'Id': '01tWt000006hVBZIA2', 'Name': 'EduTech Lab', 'IsActive': '1'}, {'Id': '#01tWt000006hVDBIA2', 'Name': 'CircuitMaster Analyzer', 'IsActive': '1'}, {'Id': '#01tWt000006hVEnIAM', 'Name': 'DesignWave Automation  ', 'IsActive': '1'}, {'Id': '01tWt000006hVGPIA2', 'Name': 'QuantumPCB Modeler  ', 'IsActive': '1'}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision', 'IsActive': '1'}, {'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro', 'IsActive': '1'}, {'Id': '#01tWt000006hVJeIAM', 'Name': 'SecureData Nexus', 'IsActive': '1'}, {'Id': '01tWt000006hVLFIA2', 'Name': 'CollabCircuit Hub', 'IsActive': '1'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite', 'IsActive': '1'}, {'Id': '01tWt000006hVOTIA2', 'Name': 'UnitySim Essentials   ', 'IsActive': '1'}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro', 'IsActive': '1'}, {'Id': '01tWt000006hVQ6IAM', 'Name': 'VeriSim Express  ', 'IsActive': '1'}, {'Id': '01tWt000006hVRhIAM', 'Name': 'PCBProto Wizard', 'IsActive': '1'}, {'Id': '01tWt000006hVTJIA2', 'Name': 'IntegrGuard Secure', 'IsActive': '1'}, {'Id': '01tWt000006hVUvIAM', 'Name': 'OptiEnergy Suite', 'IsActive': '1'}, {'Id': '#01tWt000006hVWXIA2', 'Name': 'AutoGen IDE   ', 'IsActive': '1'}, {'Id': '#01tWt000006hVY9IAM', 'Name': 'EduFlow Academy', 'IsActive': '1'}, {'Id': '01tWt000006hVZlIAM', 'Name': 'SecuManage Pro  ', 'IsActive': '1'}, {'Id': '01tWt000006hVbNIAU', 'Name': 'EnergyReduce Pro', 'IsActive': '1'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio', 'IsActive': '1'}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator', 'IsActive': '1'}, {'Id': '01tWt000006hVgDIAU', 'Name': 'CloudInnovate Space ', 'IsActive': '1'}, {'Id': '#01tWt000006hVhpIAE', 'Name': 'OptiPower Max', 'IsActive': '1'}, {'Id': '01tWt000006hVjRIAU', 'Name': 'Workflow Genius', 'IsActive': '1'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub', 'IsActive': '1'}, {'Id': '#01tWt000006hVl3IAE', 'Name': 'PCB QuickMaker', 'IsActive': '1'}, {'Id': '01tWt000006hVmfIAE', 'Name': 'EduTech Advance', 'IsActive': '1'}, {'Id': '#01tWt000006hVoHIAU', 'Name': 'CryptSecure Core', 'IsActive': '1'}, {'Id': '01tWt000006hVptIAE', 'Name': 'DesignEdge Pro', 'IsActive': '1'}, {'Id': '#01tWt000006hVrVIAU', 'Name': 'VerifySim Elite', 'IsActive': '1'}, {'Id': '#01tWt000006hVrWIAU', 'Name': 'PowerPro Optimize   ', 'IsActive': '1'}, {'Id': '01tWt000006hVt7IAE', 'Name': 'PCB EcoModel  ', 'IsActive': '1'}, {'Id': '01tWt000006hVujIAE', 'Name': 'CyberShield Core', 'IsActive': '1'}, {'Id': '01tWt000006hVwLIAU', 'Name': 'SimulateX Edge', 'IsActive': '1'}, {'Id': '#01tWt0000072LsLIAU', 'Name': 'Shipping Charge Product', 'IsActive': '1'}], 'var_call_c2HzEW7MPY6tWvJlJHx1HdIF': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}]}

exec(code, env_args)
