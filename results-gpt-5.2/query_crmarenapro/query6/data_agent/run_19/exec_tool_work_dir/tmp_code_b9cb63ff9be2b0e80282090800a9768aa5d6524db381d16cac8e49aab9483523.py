code = """import json, pandas as pd

qlis = pd.DataFrame(var_call_HRbjA4e5AG1LazdQwQb1lUMa)
pbes = pd.DataFrame(var_call_GMxuzuDNQ1j0Rq6RAUzqoaNO)

# normalize id-like fields by stripping leading # and whitespace
for c in ['Product2Id','PricebookEntryId']:
    qlis[c] = qlis[c].astype(str).str.strip().str.lstrip('#')
for c in ['Product2Id','PricebookEntryId']:
    pbes[c] = pbes[c].astype(str).str.strip().str.lstrip('#')

# numeric coercion
for c in ['Quantity','UnitPrice','Discount','TotalPrice','ListUnitPrice']:
    if c in qlis.columns:
        qlis[c] = pd.to_numeric(qlis[c], errors='coerce')
    if c in pbes.columns:
        pbes[c] = pd.to_numeric(pbes[c], errors='coerce')

merged = qlis.merge(pbes[['PricebookEntryId','ListUnitPrice']], on='PricebookEntryId', how='left')
merged['unit_price_matches_list'] = (merged['UnitPrice'].round(2) == merged['ListUnitPrice'].round(2))

# Detect suspect config: any unit price not matching list OR very high quantity with discount
suspect = merged[(~merged['unit_price_matches_list']) | ((merged['Quantity']>=10) & (merged['Discount']>0))].copy()

# Load knowledge articles
path_or_data = var_call_CF4PlOrUhGEdY5ozBvcHBrLo
if isinstance(path_or_data, str):
    with open(path_or_data, 'r', encoding='utf-8') as f:
        kav = json.load(f)
else:
    kav = path_or_data
kav_df = pd.DataFrame(kav)

# Find likely policy article by keyword
text = (kav_df['title'].fillna('') + ' ' + kav_df['summary'].fillna('') + ' ' + kav_df['faq_answer__c'].fillna('')).str.lower()
keywords = [
    'discount','discounting','pricing policy','price','unit price','pricebook','list price',
    'quantity','minimum order','bulk','volume','quote line','quotation','quote'
]
score = sum(text.str.contains(k, regex=False).astype(int) for k in keywords)
kav_df = kav_df.assign(score=score)
policy_candidates = kav_df.sort_values(['score'], ascending=False).head(20)

# If no suspect lines, return null
result = {
    'suspect_count': int(suspect.shape[0]),
    'top_candidates': policy_candidates[['id','title','score']].to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_HRbjA4e5AG1LazdQwQb1lUMa': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_GMxuzuDNQ1j0Rq6RAUzqoaNO': [{'PricebookEntryId': '01uWt0000027P5NIAU', 'ListUnitPrice': '599.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '#01tWt000006hV58IAE', 'ProductName': 'SecureFlow Suite'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'ListUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'ListUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'ListUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVBZIA2', 'ProductName': 'EduTech Lab'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'ListUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVI1IAM', 'ProductName': 'AIOptics Vision'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'ListUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hPfgIAE', 'ProductName': 'EcoPower Convert'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'ListUnitPrice': '299.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVMrIAM', 'ProductName': 'TrainEDU Suite'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'ListUnitPrice': '459.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVUvIAM', 'ProductName': 'OptiEnergy Suite'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'ListUnitPrice': '339.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVQ5IAM', 'ProductName': 'CircuitSync Pro'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'ListUnitPrice': '429.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVQ6IAM', 'ProductName': 'VeriSim Express  '}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'ListUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVTJIA2', 'ProductName': 'IntegrGuard Secure'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'ListUnitPrice': '559.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVZlIAM', 'ProductName': 'SecuManage Pro  '}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'ListUnitPrice': '349.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVbNIAU', 'ProductName': 'EnergyReduce Pro'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'ListUnitPrice': '549.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVebIAE', 'ProductName': 'CircuitAI Innovator'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'ListUnitPrice': '429.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVjRIAU', 'ProductName': 'Workflow Genius'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'ListUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVmfIAE', 'ProductName': 'EduTech Advance'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'ListUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVwLIAU', 'ProductName': 'SimulateX Edge'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'ListUnitPrice': '579.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVujIAE', 'ProductName': 'CyberShield Core'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'ListUnitPrice': '299.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVjSIAU', 'ProductName': 'InnoTrain Hub'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'ListUnitPrice': '619.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hUtqIAE', 'ProductName': 'SecureTrack Pro '}], 'var_call_CF4PlOrUhGEdY5ozBvcHBrLo': 'file_storage/call_CF4PlOrUhGEdY5ozBvcHBrLo.json', 'var_call_9opEvtBvhXl1iY1JG2RRpqCr': []}

exec(code, env_args)
