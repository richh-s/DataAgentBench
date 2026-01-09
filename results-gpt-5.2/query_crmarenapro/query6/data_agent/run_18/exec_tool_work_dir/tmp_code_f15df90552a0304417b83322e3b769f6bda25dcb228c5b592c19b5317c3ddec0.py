code = """import json, pandas as pd

qlis = pd.DataFrame(var_call_mf28nNpo5QQIRTXUpCb0TFG5)
pbe = pd.DataFrame(var_call_2RBbcgMJ5mcJjspLkXL1j7Sv)

# normalize ids by stripping leading '#'
def norm(s):
    if s is None: return None
    s = str(s)
    return s[1:] if s.startswith('#') else s

for c in ['Product2Id','PricebookEntryId']:
    qlis[c+'_n'] = qlis[c].map(norm)

pbe['PricebookEntryId_n'] = pbe['PricebookEntryId'].map(norm)

m = qlis.merge(pbe, left_on='PricebookEntryId_n', right_on='PricebookEntryId_n', how='left', suffixes=('','_pbe'))

# detect violations: unit price not equal to list unit price when discount=0
m['UnitPrice_f'] = m['UnitPrice'].astype(float)
m['ListUnitPrice_f'] = pd.to_numeric(m['ListUnitPrice'], errors='coerce')
m['Discount_f'] = m['Discount'].astype(float)

viol = m[(m['Discount_f']==0.0) & (m['ListUnitPrice_f'].notna()) & (abs(m['UnitPrice_f']-m['ListUnitPrice_f'])>1e-6)]

# Load knowledge articles
path = var_call_GzAZJOTNmLg3FbwOh0EbCfUt
with open(path,'r',encoding='utf-8') as f:
    kav = json.load(f)

# find best matching article id based on keywords
text_cols = ['title','summary','faq_answer__c']

def score_article(a):
    blob = ' '.join([(a.get(c) or '') for c in text_cols]).lower()
    score = 0
    # pricing/discount compliance cues
    for kw, w in [
        ('unit price',3),('list price',3),('pricebook',3),('standard price book',2),
        ('discount',3),('pricing',2),('must match',4),('not allowed',2),('policy',2),
        ('override',3),('manual price',3),('minimum advertised',2)
    ]:
        if kw in blob:
            score += w
    return score

best = None
best_score = -1
for a in kav:
    sc = score_article(a)
    if sc > best_score:
        best_score = sc
        best = a

# If no violation found, return null
result = {'violation_found': len(viol)>0, 'article_id': (best.get('id') if (len(viol)>0 and best_score>0) else None)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_mf28nNpo5QQIRTXUpCb0TFG5': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_2RBbcgMJ5mcJjspLkXL1j7Sv': [{'PricebookEntryId': '01uWt0000027P5NIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hV58IAE', 'ListUnitPrice': '599.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'SecureFlow Suite', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hTUkIAM', 'ListUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'CloudLink Designer', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'ListUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'AI Cirku-Tech', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVBZIA2', 'ListUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'EduTech Lab', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVI1IAM', 'ListUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'AIOptics Vision', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPfgIAE', 'ListUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'EcoPower Convert', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVMrIAM', 'ListUnitPrice': '299.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'TrainEDU Suite', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVUvIAM', 'ListUnitPrice': '459.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'OptiEnergy Suite', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'ListUnitPrice': '339.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'CircuitSync Pro', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ6IAM', 'ListUnitPrice': '429.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'VeriSim Express  ', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVTJIA2', 'ListUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'IntegrGuard Secure', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVZlIAM', 'ListUnitPrice': '559.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'SecuManage Pro  ', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVbNIAU', 'ListUnitPrice': '349.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'EnergyReduce Pro', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVebIAE', 'ListUnitPrice': '549.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'CircuitAI Innovator', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjRIAU', 'ListUnitPrice': '429.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'Workflow Genius', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVmfIAE', 'ListUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'EduTech Advance', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVwLIAU', 'ListUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'SimulateX Edge', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVujIAE', 'ListUnitPrice': '579.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'CyberShield Core', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjSIAU', 'ListUnitPrice': '299.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'InnoTrain Hub', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUtqIAE', 'ListUnitPrice': '619.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'SecureTrack Pro ', 'ProductIsActive': '1'}], 'var_call_GzAZJOTNmLg3FbwOh0EbCfUt': 'file_storage/call_GzAZJOTNmLg3FbwOh0EbCfUt.json'}

exec(code, env_args)
