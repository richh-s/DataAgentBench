code = """import json, pandas as pd

qlis = pd.DataFrame(var_call_YblFnMeVLY3fELc092MxhNtG)
# pricebook entries
pbe = pd.DataFrame(var_call_yqk1fO5Kt80JO0QoEXKeZAy9)

# knowledge articles (load full)
ka_src = var_call_MwPPEt6xUScaMdySelGBpXDW
if isinstance(ka_src, str) and ka_src.endswith('.json'):
    with open(ka_src, 'r', encoding='utf-8') as f:
        ka = pd.DataFrame(json.load(f))
else:
    ka = pd.DataFrame(ka_src)

# Normalize ids for joins
for col in ['PricebookEntryId','Product2Id']:
    if col in qlis.columns:
        qlis[col+'_norm'] = qlis[col].astype(str).str.replace('#','', regex=False).str.strip()
for col in ['PricebookEntryId','Product2Id']:
    if col in pbe.columns:
        pbe[col+'_norm'] = pbe[col].astype(str).str.replace('#','', regex=False).str.strip()

# Join to list prices
m = qlis.merge(pbe, left_on='PricebookEntryId_norm', right_on='PricebookEntryId_norm', how='left', suffixes=('','_pbe'))

# Determine violations
violations = []
# Rule: unit price should match list price unless discount used appropriately.
# Here Discount is percent; expected UnitPrice = ListUnitPrice*(1-Discount/100)
# Also check TotalPrice = Quantity*UnitPrice*(1-Discount/100) ? but TotalPrice already includes discount sometimes.

def to_float(x):
    try:
        return float(str(x).strip())
    except:
        return None

for _, r in m.iterrows():
    qty = to_float(r.get('Quantity'))
    unit = to_float(r.get('UnitPrice'))
    disc = to_float(r.get('Discount')) or 0.0
    listp = to_float(r.get('ListUnitPrice'))
    total = to_float(r.get('TotalPrice'))
    # invalid quantities
    if qty is None or qty <= 0 or (abs(qty - round(qty))>1e-9):
        violations.append('quantity')
        continue
    # price checks
    if listp is not None and unit is not None:
        expected_unit = listp
        # if discount should be applied to list, unit should still be list (common sf) and total reflects discount,
        # but sometimes unit adjusted. We'll accept either: (unit==list and total==qty*list*(1-disc/100)) OR (unit==list*(1-disc/100) and total==qty*unit)
        ok1 = total is not None and abs(unit-expected_unit) < 0.01 and abs(total - qty*expected_unit*(1-disc/100.0)) < 0.05
        ok2 = total is not None and abs(unit-expected_unit*(1-disc/100.0)) < 0.01 and abs(total - qty*unit) < 0.05
        # if discount present, also require 0<=disc<=100
        if disc < 0 or disc > 100:
            violations.append('discount_range')
        elif not (ok1 or ok2):
            violations.append('pricing')

# Map violation to knowledge article: search relevant policy articles
# We'll look for titles/summaries containing pricing/discount/quote line/quantity rules.
text = (ka['title'].fillna('') + ' ' + ka['summary'].fillna('') + ' ' + ka['faq_answer__c'].fillna('')).str.lower()

article_id = None
if 'pricing' in violations or 'discount_range' in violations:
    # search best match for discount/pricing policy
    keywords = ['discount', 'pricing', 'price', 'unit price', 'quote line', 'list price']
elif 'quantity' in violations:
    keywords = ['quantity', 'minimum', 'maximum', 'quote line']
else:
    keywords = ['quote', 'configuration', 'product setup']

scores = []
for i, t in enumerate(text):
    s = sum(t.count(k) for k in keywords)
    if s>0:
        scores.append((s, ka.iloc[i]['id']))
if scores:
    scores.sort(reverse=True)
    article_id = scores[0][1]

# If no match, return null
out = article_id if article_id is not None else ''
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_YblFnMeVLY3fELc092MxhNtG': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_xIM4yFKEG8OyMD5mPsIN2jQt': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_call_yqk1fO5Kt80JO0QoEXKeZAy9': [{'PricebookEntryId': '01uWt0000027P3lIAE', 'Product2Id': '01tWt000006hV57IAE', 'ListUnitPrice': '499.99', 'ProductName': 'PulseSim Pro'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'Product2Id': '#01tWt000006hV58IAE', 'ListUnitPrice': '599.99', 'ProductName': 'SecureFlow Suite'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'Product2Id': '01tWt000006hTUkIAM', 'ListUnitPrice': '399.99', 'ProductName': 'CloudLink Designer'}, {'PricebookEntryId': '#01uWt0000027P8bIAE', 'Product2Id': '01tWt000006hV6jIAE', 'ListUnitPrice': '349.99', 'ProductName': 'EcoPCB Creator   '}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'Product2Id': '01tWt000006hV8LIAU', 'ListUnitPrice': '529.99', 'ProductName': 'AI Cirku-Tech'}, {'PricebookEntryId': '01uWt0000027PADIA2', 'Product2Id': '01tWt000006hPffIAE', 'ListUnitPrice': '299.99', 'ProductName': 'DevVision IDE'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'Product2Id': '01tWt000006hVBZIA2', 'ListUnitPrice': '399.99', 'ProductName': 'EduTech Lab'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'Product2Id': '01tWt000006hVI1IAM', 'ListUnitPrice': '529.99', 'ProductName': 'AIOptics Vision'}, {'PricebookEntryId': '01uWt0000027PIJIA2', 'Product2Id': '01tWt000006hVptIAE', 'ListUnitPrice': '459.99', 'ProductName': 'DesignEdge Pro'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'Product2Id': '01tWt000006hPfgIAE', 'ListUnitPrice': '399.99', 'ProductName': 'EcoPower Convert'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'Product2Id': '01tWt000006hVMrIAM', 'ListUnitPrice': '299.99', 'ProductName': 'TrainEDU Suite'}, {'PricebookEntryId': '01uWt0000027PTZIA2', 'Product2Id': '01tWt000006hV0IIAU', 'ListUnitPrice': '449.99', 'ProductName': 'NextGen IDE'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'Product2Id': '01tWt000006hVUvIAM', 'ListUnitPrice': '459.99', 'ProductName': 'OptiEnergy Suite'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'Product2Id': '01tWt000006hVQ5IAM', 'ListUnitPrice': '339.99', 'ProductName': 'CircuitSync Pro'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'Product2Id': '01tWt000006hVQ6IAM', 'ListUnitPrice': '429.99', 'ProductName': 'VeriSim Express  '}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'Product2Id': '01tWt000006hVTJIA2', 'ListUnitPrice': '529.99', 'ProductName': 'IntegrGuard Secure'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'Product2Id': '01tWt000006hVZlIAM', 'ListUnitPrice': '559.99', 'ProductName': 'SecuManage Pro  '}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'Product2Id': '01tWt000006hVbNIAU', 'ListUnitPrice': '349.99', 'ProductName': 'EnergyReduce Pro'}, {'PricebookEntryId': '01uWt0000027PgUIAU', 'Product2Id': '01tWt000006hVt7IAE', 'ListUnitPrice': '379.99', 'ProductName': 'PCB EcoModel  '}, {'PricebookEntryId': '01uWt0000027Pi5IAE', 'Product2Id': '01tWt000006hVczIAE', 'ListUnitPrice': '399.99', 'ProductName': 'CollabDesign Studio'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'Product2Id': '01tWt000006hVebIAE', 'ListUnitPrice': '549.99', 'ProductName': 'CircuitAI Innovator'}, {'PricebookEntryId': '01uWt0000027PlJIAU', 'Product2Id': '01tWt000006hUsEIAU', 'ListUnitPrice': '499.99', 'ProductName': 'SimuCheck Ultra'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'Product2Id': '01tWt000006hVjRIAU', 'ListUnitPrice': '429.99', 'ProductName': 'Workflow Genius'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'Product2Id': '01tWt000006hVmfIAE', 'ListUnitPrice': '399.99', 'ProductName': 'EduTech Advance'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'Product2Id': '01tWt000006hVwLIAU', 'ListUnitPrice': '529.99', 'ProductName': 'SimulateX Edge'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'Product2Id': '01tWt000006hVujIAE', 'ListUnitPrice': '579.99', 'ProductName': 'CyberShield Core'}, {'PricebookEntryId': '#01uWt0000027Q33IAE', 'Product2Id': '01tWt000006hOd8IAE', 'ListUnitPrice': '499.99', 'ProductName': 'AutoLayout Master'}, {'PricebookEntryId': '#01uWt0000027Q34IAE', 'Product2Id': '01tWt000006hUgwIAE', 'ListUnitPrice': '599.99', 'ProductName': 'AI DesignShift'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'Product2Id': '01tWt000006hVjSIAU', 'ListUnitPrice': '299.99', 'ProductName': 'InnoTrain Hub'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'Product2Id': '01tWt000006hUtqIAE', 'ListUnitPrice': '619.99', 'ProductName': 'SecureTrack Pro '}], 'var_call_MwPPEt6xUScaMdySelGBpXDW': 'file_storage/call_MwPPEt6xUScaMdySelGBpXDW.json', 'var_call_8tqErFdJPYmLZ4p8N8JMMKbn': 'file_storage/call_8tqErFdJPYmLZ4p8N8JMMKbn.json'}

exec(code, env_args)
