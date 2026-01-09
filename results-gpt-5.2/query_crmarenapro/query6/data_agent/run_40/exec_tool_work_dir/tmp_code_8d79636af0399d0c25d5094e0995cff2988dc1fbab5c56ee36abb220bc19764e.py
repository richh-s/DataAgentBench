code = """import json, pandas as pd
from pathlib import Path

qli = pd.DataFrame(var_call_4roXg3seCmciju3mSud9BU62)
cat = pd.DataFrame(var_call_Dt7h5zJhTHd1Glyqlpl1bs4w)

# normalize ids by stripping leading '#'
def norm(s):
    if s is None:
        return None
    s = str(s).strip()
    return s[1:] if s.startswith('#') else s

for c in ['Product2Id','PricebookEntryId']:
    qli[c+'_n'] = qli[c].map(norm)
for c in ['Product2Id','PricebookEntryId']:
    cat[c+'_n'] = cat[c].map(norm)

# cast numeric
for c in ['Quantity','UnitPrice','Discount','TotalPrice']:
    qli[c] = pd.to_numeric(qli[c], errors='coerce')
cat['CatalogUnitPrice'] = pd.to_numeric(cat['CatalogUnitPrice'], errors='coerce')

m = qli.merge(cat[['PricebookEntryId_n','Product2Id_n','CatalogUnitPrice']], left_on='PricebookEntryId_n', right_on='PricebookEntryId_n', how='left')

# checks: unit price mismatch vs catalog, discount > 10, quantity > 25, negative/zero
violations = []

# price mismatch
price_mismatch = m[(m['CatalogUnitPrice'].notna()) & (m['UnitPrice'].round(2) != m['CatalogUnitPrice'].round(2))]
if len(price_mismatch)>0:
    violations.append('PRICE_MISMATCH')

# discount threshold
if (m['Discount'].fillna(0) > 10).any():
    violations.append('DISCOUNT_GT_10')

# quantity threshold
if (m['Quantity'].fillna(0) > 25).any():
    violations.append('QTY_GT_25')

# We'll map to knowledge articles by keyword search
# Load knowledge articles
p = Path(var_call_y6Ei0iXrauZJyVY8CpmA7k86)
articles = json.loads(p.read_text())
dfa = pd.DataFrame(articles)

def find_article(keywords):
    if dfa.empty:
        return None
    txt = (dfa['title'].fillna('') + ' ' + dfa['summary'].fillna('') + ' ' + dfa['faq_answer__c'].fillna('')).str.lower()
    mask = pd.Series(True, index=dfa.index)
    for kw in keywords:
        mask &= txt.str.contains(kw)
    hits = dfa[mask]
    return None if hits.empty else hits.iloc[0]['id']

article_id = None
# Priority: discount policy, then quantity, then pricing
if 'DISCOUNT_GT_10' in violations:
    article_id = find_article(['discount','quote']) or find_article(['discount'])
if article_id is None and 'QTY_GT_25' in violations:
    article_id = find_article(['quantity','quote']) or find_article(['bulk']) or find_article(['quantity'])
if article_id is None and 'PRICE_MISMATCH' in violations:
    article_id = find_article(['pricebook']) or find_article(['pricing']) or find_article(['unit price'])

# if still none, attempt generic sales policy
if article_id is None and violations:
    article_id = find_article(['quote','policy']) or find_article(['approval'])

print('__RESULT__:')
print(json.dumps({'violations': violations, 'article_id': article_id}))"""

env_args = {'var_call_4roXg3seCmciju3mSud9BU62': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_y6Ei0iXrauZJyVY8CpmA7k86': 'file_storage/call_y6Ei0iXrauZJyVY8CpmA7k86.json', 'var_call_Dt7h5zJhTHd1Glyqlpl1bs4w': [{'PricebookEntryId': '01uWt0000027P3lIAE', 'Product2Id': '01tWt000006hV57IAE', 'CatalogUnitPrice': '499.99', 'ProductName': 'PulseSim Pro'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'Product2Id': '#01tWt000006hV58IAE', 'CatalogUnitPrice': '599.99', 'ProductName': 'SecureFlow Suite'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'Product2Id': '01tWt000006hTUkIAM', 'CatalogUnitPrice': '399.99', 'ProductName': 'CloudLink Designer'}, {'PricebookEntryId': '#01uWt0000027P8bIAE', 'Product2Id': '01tWt000006hV6jIAE', 'CatalogUnitPrice': '349.99', 'ProductName': 'EcoPCB Creator   '}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'Product2Id': '01tWt000006hV8LIAU', 'CatalogUnitPrice': '529.99', 'ProductName': 'AI Cirku-Tech'}, {'PricebookEntryId': '01uWt0000027PADIA2', 'Product2Id': '01tWt000006hPffIAE', 'CatalogUnitPrice': '299.99', 'ProductName': 'DevVision IDE'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'Product2Id': '01tWt000006hVBZIA2', 'CatalogUnitPrice': '399.99', 'ProductName': 'EduTech Lab'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'Product2Id': '01tWt000006hVI1IAM', 'CatalogUnitPrice': '529.99', 'ProductName': 'AIOptics Vision'}, {'PricebookEntryId': '01uWt0000027PIJIA2', 'Product2Id': '01tWt000006hVptIAE', 'CatalogUnitPrice': '459.99', 'ProductName': 'DesignEdge Pro'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'Product2Id': '01tWt000006hPfgIAE', 'CatalogUnitPrice': '399.99', 'ProductName': 'EcoPower Convert'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'Product2Id': '01tWt000006hVMrIAM', 'CatalogUnitPrice': '299.99', 'ProductName': 'TrainEDU Suite'}, {'PricebookEntryId': '01uWt0000027PTZIA2', 'Product2Id': '01tWt000006hV0IIAU', 'CatalogUnitPrice': '449.99', 'ProductName': 'NextGen IDE'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'Product2Id': '01tWt000006hVUvIAM', 'CatalogUnitPrice': '459.99', 'ProductName': 'OptiEnergy Suite'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'Product2Id': '01tWt000006hVQ5IAM', 'CatalogUnitPrice': '339.99', 'ProductName': 'CircuitSync Pro'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'Product2Id': '01tWt000006hVQ6IAM', 'CatalogUnitPrice': '429.99', 'ProductName': 'VeriSim Express  '}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'Product2Id': '01tWt000006hVTJIA2', 'CatalogUnitPrice': '529.99', 'ProductName': 'IntegrGuard Secure'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'Product2Id': '01tWt000006hVZlIAM', 'CatalogUnitPrice': '559.99', 'ProductName': 'SecuManage Pro  '}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'Product2Id': '01tWt000006hVbNIAU', 'CatalogUnitPrice': '349.99', 'ProductName': 'EnergyReduce Pro'}, {'PricebookEntryId': '01uWt0000027PgUIAU', 'Product2Id': '01tWt000006hVt7IAE', 'CatalogUnitPrice': '379.99', 'ProductName': 'PCB EcoModel  '}, {'PricebookEntryId': '01uWt0000027Pi5IAE', 'Product2Id': '01tWt000006hVczIAE', 'CatalogUnitPrice': '399.99', 'ProductName': 'CollabDesign Studio'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'Product2Id': '01tWt000006hVebIAE', 'CatalogUnitPrice': '549.99', 'ProductName': 'CircuitAI Innovator'}, {'PricebookEntryId': '01uWt0000027PlJIAU', 'Product2Id': '01tWt000006hUsEIAU', 'CatalogUnitPrice': '499.99', 'ProductName': 'SimuCheck Ultra'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'Product2Id': '01tWt000006hVjRIAU', 'CatalogUnitPrice': '429.99', 'ProductName': 'Workflow Genius'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'Product2Id': '01tWt000006hVmfIAE', 'CatalogUnitPrice': '399.99', 'ProductName': 'EduTech Advance'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'Product2Id': '01tWt000006hVwLIAU', 'CatalogUnitPrice': '529.99', 'ProductName': 'SimulateX Edge'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'Product2Id': '01tWt000006hVujIAE', 'CatalogUnitPrice': '579.99', 'ProductName': 'CyberShield Core'}, {'PricebookEntryId': '#01uWt0000027Q33IAE', 'Product2Id': '01tWt000006hOd8IAE', 'CatalogUnitPrice': '499.99', 'ProductName': 'AutoLayout Master'}, {'PricebookEntryId': '#01uWt0000027Q34IAE', 'Product2Id': '01tWt000006hUgwIAE', 'CatalogUnitPrice': '599.99', 'ProductName': 'AI DesignShift'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'Product2Id': '01tWt000006hVjSIAU', 'CatalogUnitPrice': '299.99', 'ProductName': 'InnoTrain Hub'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'Product2Id': '01tWt000006hUtqIAE', 'CatalogUnitPrice': '619.99', 'ProductName': 'SecureTrack Pro '}]}

exec(code, env_args)
