code = """import json, pandas as pd

def norm(s):
    if s is None:
        return None
    return str(s).strip().lstrip('#')

qli = pd.DataFrame(var_call_iBFOR303smD076WBHzFtLP0C)
pbe = pd.DataFrame(var_call_dTR2X7rFvqBplmhxAJtJu4FF)
prod = pd.DataFrame(var_call_sDsjoadtGYDLtFXmnLJM3Hmt)

# normalized ids
qli['Product2Id_norm'] = qli['Product2Id'].map(norm)
qli['PricebookEntryId_norm'] = qli['PricebookEntryId'].map(norm)

pbe['PricebookEntryId_norm'] = pbe['PricebookEntryId'].map(norm)
pbe['Product2Id_norm_pbe'] = pbe['Product2Id'].map(norm)

prod['Product2Id_norm'] = prod['Id'].map(norm)

# joins
qli = qli.merge(pbe[['PricebookEntryId_norm','Product2Id_norm_pbe','ListUnitPrice']], on='PricebookEntryId_norm', how='left')
qli = qli.merge(prod[['Product2Id_norm','Name']], on='Product2Id_norm', how='left')

for c in ['Quantity','UnitPrice','Discount','TotalPrice','ListUnitPrice']:
    qli[c] = pd.to_numeric(qli[c], errors='coerce')

violations = []
if (qli['Quantity']>=25).any():
    violations.append('bulk_qty')
if (qli['Discount']>10).any():
    violations.append('discount_over_10')
if ((qli['ListUnitPrice'].notna()) & (abs(qli['UnitPrice']-qli['ListUnitPrice'])>1e-6)).any():
    violations.append('unit_price_not_list')

# load knowledge articles
path_or_data = var_call_snPpTLrN2SJbv2YBDrKSo1p5
if isinstance(path_or_data, str) and path_or_data.endswith('.json'):
    with open(path_or_data,'r',encoding='utf-8') as f:
        kav = json.load(f)
else:
    kav = path_or_data
kdf = pd.DataFrame(kav)

text_cols = ['title','summary','faq_answer__c','urlname']

def score_row(row, keywords):
    txt = ' '.join([str(row.get(c,'')) for c in text_cols]).lower()
    return sum(1 for kw in keywords if kw in txt)

kw_map = {
    'discount_over_10': ['discount','approval','more than 10','over 10','10%','deal desk'],
    'bulk_qty': ['quantity','bulk','large order','over 25','25','approval'],
    'unit_price_not_list': ['list price','unit price','pricebook','must match','pricing'],
}

best_id = None
best_score = -1
for v in violations:
    kws = kw_map.get(v, [])
    if not kws or len(kdf)==0:
        continue
    scores = kdf.apply(lambda r: score_row(r, kws), axis=1)
    sc = int(scores.max())
    idx = int(scores.idxmax())
    if sc > best_score:
        best_score = sc
        best_id = kdf.loc[idx,'id']

if best_id is None:
    best_id = kdf.iloc[0]['id'] if len(kdf)>0 else None

print('__RESULT__:')
print(json.dumps({'knowledge_article_id': best_id, 'violations': violations, 'best_score': best_score}))"""

env_args = {'var_call_iBFOR303smD076WBHzFtLP0C': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_snPpTLrN2SJbv2YBDrKSo1p5': 'file_storage/call_snPpTLrN2SJbv2YBDrKSo1p5.json', 'var_call_dTR2X7rFvqBplmhxAJtJu4FF': [{'PricebookEntryId': '01uWt0000027P3mIAE', 'Product2Id': '01tWt000006hVhpIAE', 'ListUnitPrice': '489.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'Product2Id': '#01tWt000006hV58IAE', 'ListUnitPrice': '599.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'Product2Id': '01tWt000006hTUkIAM', 'ListUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'Product2Id': '01tWt000006hV8LIAU', 'ListUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PBpIAM', 'Product2Id': '01tWt000006hV9xIAE', 'ListUnitPrice': '449.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'Product2Id': '01tWt000006hVBZIA2', 'ListUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027PGfIAM', 'Product2Id': '01tWt000006hVEnIAM', 'ListUnitPrice': '479.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PIHIA2', 'Product2Id': '#01tWt000006hVGPIA2', 'ListUnitPrice': '599.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'Product2Id': '01tWt000006hVI1IAM', 'ListUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PLVIA2', 'Product2Id': '#01tWt000006hVLFIA2', 'ListUnitPrice': '459.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'Product2Id': '01tWt000006hPfgIAE', 'ListUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'Product2Id': '01tWt000006hVMrIAM', 'ListUnitPrice': '299.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027POkIAM', 'Product2Id': '#01tWt000006hRfqIAE', 'ListUnitPrice': '349.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027PRxIAM', 'Product2Id': '#01tWt000006hVOTIA2', 'ListUnitPrice': '559.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'Product2Id': '01tWt000006hVUvIAM', 'ListUnitPrice': '459.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'Product2Id': '01tWt000006hVQ5IAM', 'ListUnitPrice': '339.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'Product2Id': '01tWt000006hVQ6IAM', 'ListUnitPrice': '429.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PYPIA2', 'Product2Id': '#01tWt000006hVRhIAM', 'ListUnitPrice': '319.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'Product2Id': '01tWt000006hVTJIA2', 'ListUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'Product2Id': '01tWt000006hVZlIAM', 'ListUnitPrice': '559.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'Product2Id': '01tWt000006hVbNIAU', 'ListUnitPrice': '349.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'Product2Id': '01tWt000006hVebIAE', 'ListUnitPrice': '549.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027PmvIAE', 'Product2Id': '01tWt000006hVJeIAM', 'ListUnitPrice': '599.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PoXIAU', 'Product2Id': '#01tWt000006hVgDIAU', 'ListUnitPrice': '459.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'Product2Id': '01tWt000006hVjRIAU', 'ListUnitPrice': '429.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PrlIAE', 'Product2Id': '01tWt000006hVl3IAE', 'ListUnitPrice': '369.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'Product2Id': '01tWt000006hVmfIAE', 'ListUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'Product2Id': '01tWt000006hVwLIAU', 'ListUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PuzIAE', 'Product2Id': '01tWt000006hVoHIAU', 'ListUnitPrice': '629.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027PyDIAU', 'Product2Id': '01tWt000006hVrVIAU', 'ListUnitPrice': '649.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'Product2Id': '01tWt000006hVujIAE', 'ListUnitPrice': '579.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'Product2Id': '01tWt000006hVjSIAU', 'ListUnitPrice': '299.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'Product2Id': '01tWt000006hUtqIAE', 'ListUnitPrice': '619.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}], 'var_call_sDsjoadtGYDLtFXmnLJM3Hmt': [{'Id': '01tWt000006hOd8IAE', 'Name': 'AutoLayout Master'}, {'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE'}, {'Id': '01tWt000006hPfgIAE', 'Name': 'EcoPower Convert'}, {'Id': '01tWt000006hRfqIAE', 'Name': 'FlexiDesign Pro'}, {'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer'}, {'Id': '01tWt000006hUKMIA2', 'Name': 'CryptGuard Module'}, {'Id': '#01tWt000006hUUwIAM', 'Name': 'SimuFlow Xtreme'}, {'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hUsEIAU', 'Name': 'SimuCheck Ultra'}, {'Id': '01tWt000006hUtqIAE', 'Name': 'SecureTrack Pro '}, {'Id': '01tWt000006hV0IIAU', 'Name': 'NextGen IDE'}, {'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro'}, {'Id': '#01tWt000006hV58IAE', 'Name': 'SecureFlow Suite'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager'}, {'Id': '01tWt000006hVBZIA2', 'Name': 'EduTech Lab'}, {'Id': '#01tWt000006hVDBIA2', 'Name': 'CircuitMaster Analyzer'}, {'Id': '#01tWt000006hVEnIAM', 'Name': 'DesignWave Automation  '}, {'Id': '01tWt000006hVGPIA2', 'Name': 'QuantumPCB Modeler  '}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}, {'Id': '#01tWt000006hVJeIAM', 'Name': 'SecureData Nexus'}, {'Id': '01tWt000006hVLFIA2', 'Name': 'CollabCircuit Hub'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVOTIA2', 'Name': 'UnitySim Essentials   '}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro'}, {'Id': '01tWt000006hVQ6IAM', 'Name': 'VeriSim Express  '}, {'Id': '01tWt000006hVRhIAM', 'Name': 'PCBProto Wizard'}, {'Id': '01tWt000006hVTJIA2', 'Name': 'IntegrGuard Secure'}, {'Id': '01tWt000006hVUvIAM', 'Name': 'OptiEnergy Suite'}, {'Id': '#01tWt000006hVWXIA2', 'Name': 'AutoGen IDE   '}, {'Id': '#01tWt000006hVY9IAM', 'Name': 'EduFlow Academy'}, {'Id': '01tWt000006hVZlIAM', 'Name': 'SecuManage Pro  '}, {'Id': '01tWt000006hVbNIAU', 'Name': 'EnergyReduce Pro'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVgDIAU', 'Name': 'CloudInnovate Space '}, {'Id': '#01tWt000006hVhpIAE', 'Name': 'OptiPower Max'}, {'Id': '01tWt000006hVjRIAU', 'Name': 'Workflow Genius'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}, {'Id': '#01tWt000006hVl3IAE', 'Name': 'PCB QuickMaker'}, {'Id': '01tWt000006hVmfIAE', 'Name': 'EduTech Advance'}, {'Id': '#01tWt000006hVoHIAU', 'Name': 'CryptSecure Core'}, {'Id': '01tWt000006hVptIAE', 'Name': 'DesignEdge Pro'}, {'Id': '#01tWt000006hVrVIAU', 'Name': 'VerifySim Elite'}, {'Id': '#01tWt000006hVrWIAU', 'Name': 'PowerPro Optimize   '}, {'Id': '01tWt000006hVt7IAE', 'Name': 'PCB EcoModel  '}, {'Id': '01tWt000006hVujIAE', 'Name': 'CyberShield Core'}, {'Id': '01tWt000006hVwLIAU', 'Name': 'SimulateX Edge'}, {'Id': '#01tWt0000072LsLIAU', 'Name': 'Shipping Charge Product'}], 'var_call_lW54ShAzYRtJ2HTSvmapKMu7': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}]}

exec(code, env_args)
