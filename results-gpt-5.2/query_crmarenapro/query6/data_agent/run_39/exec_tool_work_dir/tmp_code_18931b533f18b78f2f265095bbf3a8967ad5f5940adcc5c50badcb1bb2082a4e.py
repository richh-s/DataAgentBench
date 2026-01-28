code = """import json, pandas as pd

qli = pd.DataFrame(var_call_kH5Gkb1nM2WkQrdWZWy3DkQz)
pbe = pd.DataFrame(var_call_UF8FMEGIZ2ID56W8SdxEk1Hg)

# normalize ids (trim + remove leading '#')
def norm(s):
    if pd.isna(s):
        return s
    s = str(s).strip()
    if s.startswith('#'):
        s = s[1:]
    return s

for c in ['PricebookEntryId','Product2Id','Id','QuoteId']:
    if c in qli.columns:
        qli[c+'_n'] = qli[c].map(norm)
for c in ['PricebookEntryId','Product2Id']:
    if c in pbe.columns:
        pbe[c+'_n'] = pbe[c].map(norm)

# join to get list prices
m = qli.merge(pbe, left_on='PricebookEntryId_n', right_on='PricebookEntryId_n', how='left', suffixes=('','_pbe'))

# detect unit price mismatch vs list (allow tiny float diff)
for col in ['UnitPrice','ListUnitPrice','Quantity','Discount','TotalPrice']:
    if col in m.columns:
        m[col] = pd.to_numeric(m[col], errors='coerce')

m['unit_mismatch'] = (m['ListUnitPrice'].notna()) & ((m['UnitPrice'] - m['ListUnitPrice']).abs() > 0.01)

# detect discount violations: assume max 10% unless approved; here no approval info so flag >10
m['discount_violation'] = m['Discount'].fillna(0) > 10

# detect qty violations: assume qty must be integer >=1 and <=10 per line
m['qty_violation'] = (m['Quantity'] % 1 != 0) | (m['Quantity'] < 1) | (m['Quantity'] > 10)

violations = m[m['unit_mismatch'] | m['discount_violation'] | m['qty_violation']].copy()

# load knowledge articles
import os
path = var_call_p1fxBEviVut8tHv31QgGdLNy
with open(path,'r',encoding='utf-8') as f:
    kav = json.load(f)

df_kav = pd.DataFrame(kav)
# heuristic mapping: look for titles/answers containing discount or quantity limits
text = (df_kav['title'].fillna('') + ' ' + df_kav['summary'].fillna('') + ' ' + df_kav['faq_answer__c'].fillna('')).str.lower()

def find_article(keywords):
    mask = pd.Series(True, index=df_kav.index)
    for kw in keywords:
        mask &= text.str.contains(kw)
    hits = df_kav[mask]
    if len(hits):
        return hits.iloc[0]['id']
    return None

article_id = None
# prioritize discount violation article
if (violations['discount_violation'].any()):
    article_id = find_article(['discount'])
if article_id is None and (violations['qty_violation'].any()):
    article_id = find_article(['quantity'])
if article_id is None and (violations['unit_mismatch'].any()):
    article_id = find_article(['price'])

# fallback: pick generic pricing/quote policy article by keywords
if article_id is None:
    article_id = find_article(['quote','pricing'])

print('__RESULT__:')
print(json.dumps({'article_id': article_id, 'violations_found': bool(len(violations))}))"""

env_args = {'var_call_kH5Gkb1nM2WkQrdWZWy3DkQz': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_Mo6Oda4xkBo7E4JpniaINdNo': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_call_UF8FMEGIZ2ID56W8SdxEk1Hg': [{'PricebookEntryId': '01uWt0000027P5NIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hV58IAE', 'ListUnitPrice': '599.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'SecureFlow Suite', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hTUkIAM', 'ListUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'CloudLink Designer', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'ListUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'AI Cirku-Tech', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVBZIA2', 'ListUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'EduTech Lab', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVI1IAM', 'ListUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'AIOptics Vision', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPfgIAE', 'ListUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'EcoPower Convert', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVMrIAM', 'ListUnitPrice': '299.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'TrainEDU Suite', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVUvIAM', 'ListUnitPrice': '459.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'OptiEnergy Suite', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'ListUnitPrice': '339.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'CircuitSync Pro', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ6IAM', 'ListUnitPrice': '429.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'VeriSim Express  ', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVTJIA2', 'ListUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'IntegrGuard Secure', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVZlIAM', 'ListUnitPrice': '559.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'SecuManage Pro  ', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVbNIAU', 'ListUnitPrice': '349.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'EnergyReduce Pro', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVebIAE', 'ListUnitPrice': '549.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'CircuitAI Innovator', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjRIAU', 'ListUnitPrice': '429.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'Workflow Genius', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVmfIAE', 'ListUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'EduTech Advance', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVwLIAU', 'ListUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'SimulateX Edge', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVujIAE', 'ListUnitPrice': '579.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'CyberShield Core', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjSIAU', 'ListUnitPrice': '299.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'InnoTrain Hub', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUtqIAE', 'ListUnitPrice': '619.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'SecureTrack Pro ', 'ProductIsActive': '1'}], 'var_call_p1fxBEviVut8tHv31QgGdLNy': 'file_storage/call_p1fxBEviVut8tHv31QgGdLNy.json'}

exec(code, env_args)
