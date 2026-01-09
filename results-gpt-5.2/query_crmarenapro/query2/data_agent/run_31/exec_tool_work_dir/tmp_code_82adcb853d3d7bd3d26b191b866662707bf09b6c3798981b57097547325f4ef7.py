code = """import json, pandas as pd

quote = pd.DataFrame(var_call_NR21T50Q6f4L46HQwnpczSsI)
qli = pd.DataFrame(var_call_GXTSBW3RUg9zdHkBVlDkfnsX)
pricebook = pd.DataFrame(var_call_qIRN49tUL0opQClMjo6ka63R)

# Load full knowledge articles
path = var_call_bJxnoitOA5XC2aHVxLp1j7qR
with open(path, 'r', encoding='utf-8') as f:
    kav = pd.DataFrame(json.load(f))

# Normalize ids
for df, col in [(quote,'Id'),(quote,'OpportunityId'),(quote,'AccountId'),(quote,'ContactId'),(qli,'QuoteId'),(qli,'PricebookEntryId'),(pricebook,'PricebookEntryId'),(kav,'id')]:
    if col in df.columns:
        df[col+'_norm'] = df[col].astype(str).str.replace('#','', regex=False).str.strip()

# Join QLIs to list price
m = qli.merge(pricebook, left_on='PricebookEntryId_norm', right_on='PricebookEntryId_norm', how='left', suffixes=('','_pb'))

# numeric conversions
for c in ['Quantity','UnitPrice','Discount','TotalPrice','ListUnitPrice']:
    if c in m.columns:
        m[c] = pd.to_numeric(m[c], errors='coerce')

# Compute discount percent vs list
m['disc_pct_vs_list'] = (1 - (m['UnitPrice'] / m['ListUnitPrice'])) * 100

# Policy heuristic: discount must be <=10% without approval; quote status Needs Review implies needs approval. Violation if any line discount >10%.
violation = (m['disc_pct_vs_list'] > 10.0001) | (m['Discount'] > 10.0001)

# Find relevant knowledge article about discount policy by title/summary keywords
keywords = ['discount', 'pricing', 'quote approval', 'approval', 'setup fee', 'implementation', 'cost']
text = (kav['title'].fillna('') + ' ' + kav['summary'].fillna('') + ' ' + kav['faq_answer__c'].fillna('')).str.lower()
mask = False
for kw in keywords:
    mask = mask | text.str.contains(kw)

cand = kav[mask].copy()
# Prefer article mentioning discount thresholds
cand['score'] = 0
for kw in ['discount', 'quote approval', 'pricing', 'approval']:
    cand['score'] += text[mask].str.count(kw)

cand = cand.sort_values(['score','title'], ascending=[False, True])
article_id = None
if violation.any() and len(cand)>0:
    article_id = cand.iloc[0]['id_norm']

result = article_id if article_id is not None else None

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_NR21T50Q6f4L46HQwnpczSsI': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_GXTSBW3RUg9zdHkBVlDkfnsX': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_bJxnoitOA5XC2aHVxLp1j7qR': 'file_storage/call_bJxnoitOA5XC2aHVxLp1j7qR.json', 'var_call_qIRN49tUL0opQClMjo6ka63R': [{'PricebookEntryId': '01uWt0000027P3lIAE', 'ListUnitPrice': '499.99', 'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'ListUnitPrice': '599.99', 'Product2Id': '#01tWt000006hV58IAE', 'ProductName': 'SecureFlow Suite'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'PricebookEntryId': '#01uWt0000027P8bIAE', 'ListUnitPrice': '349.99', 'Product2Id': '01tWt000006hV6jIAE', 'ProductName': 'EcoPCB Creator   '}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'ListUnitPrice': '529.99', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech'}, {'PricebookEntryId': '01uWt0000027PADIA2', 'ListUnitPrice': '299.99', 'Product2Id': '01tWt000006hPffIAE', 'ProductName': 'DevVision IDE'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hVBZIA2', 'ProductName': 'EduTech Lab'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'ListUnitPrice': '529.99', 'Product2Id': '01tWt000006hVI1IAM', 'ProductName': 'AIOptics Vision'}, {'PricebookEntryId': '01uWt0000027PIJIA2', 'ListUnitPrice': '459.99', 'Product2Id': '01tWt000006hVptIAE', 'ProductName': 'DesignEdge Pro'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hPfgIAE', 'ProductName': 'EcoPower Convert'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'ListUnitPrice': '299.99', 'Product2Id': '01tWt000006hVMrIAM', 'ProductName': 'TrainEDU Suite'}, {'PricebookEntryId': '01uWt0000027PTZIA2', 'ListUnitPrice': '449.99', 'Product2Id': '01tWt000006hV0IIAU', 'ProductName': 'NextGen IDE'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'ListUnitPrice': '459.99', 'Product2Id': '01tWt000006hVUvIAM', 'ProductName': 'OptiEnergy Suite'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'ListUnitPrice': '339.99', 'Product2Id': '01tWt000006hVQ5IAM', 'ProductName': 'CircuitSync Pro'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'ListUnitPrice': '429.99', 'Product2Id': '01tWt000006hVQ6IAM', 'ProductName': 'VeriSim Express  '}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'ListUnitPrice': '529.99', 'Product2Id': '01tWt000006hVTJIA2', 'ProductName': 'IntegrGuard Secure'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'ListUnitPrice': '559.99', 'Product2Id': '01tWt000006hVZlIAM', 'ProductName': 'SecuManage Pro  '}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'ListUnitPrice': '349.99', 'Product2Id': '01tWt000006hVbNIAU', 'ProductName': 'EnergyReduce Pro'}, {'PricebookEntryId': '01uWt0000027PgUIAU', 'ListUnitPrice': '379.99', 'Product2Id': '01tWt000006hVt7IAE', 'ProductName': 'PCB EcoModel  '}, {'PricebookEntryId': '01uWt0000027Pi5IAE', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hVczIAE', 'ProductName': 'CollabDesign Studio'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'ListUnitPrice': '549.99', 'Product2Id': '01tWt000006hVebIAE', 'ProductName': 'CircuitAI Innovator'}, {'PricebookEntryId': '01uWt0000027PlJIAU', 'ListUnitPrice': '499.99', 'Product2Id': '01tWt000006hUsEIAU', 'ProductName': 'SimuCheck Ultra'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'ListUnitPrice': '429.99', 'Product2Id': '01tWt000006hVjRIAU', 'ProductName': 'Workflow Genius'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hVmfIAE', 'ProductName': 'EduTech Advance'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'ListUnitPrice': '529.99', 'Product2Id': '01tWt000006hVwLIAU', 'ProductName': 'SimulateX Edge'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'ListUnitPrice': '579.99', 'Product2Id': '01tWt000006hVujIAE', 'ProductName': 'CyberShield Core'}, {'PricebookEntryId': '#01uWt0000027Q33IAE', 'ListUnitPrice': '499.99', 'Product2Id': '01tWt000006hOd8IAE', 'ProductName': 'AutoLayout Master'}, {'PricebookEntryId': '#01uWt0000027Q34IAE', 'ListUnitPrice': '599.99', 'Product2Id': '01tWt000006hUgwIAE', 'ProductName': 'AI DesignShift'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'ListUnitPrice': '299.99', 'Product2Id': '01tWt000006hVjSIAU', 'ProductName': 'InnoTrain Hub'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'ListUnitPrice': '619.99', 'Product2Id': '01tWt000006hUtqIAE', 'ProductName': 'SecureTrack Pro '}]}

exec(code, env_args)
