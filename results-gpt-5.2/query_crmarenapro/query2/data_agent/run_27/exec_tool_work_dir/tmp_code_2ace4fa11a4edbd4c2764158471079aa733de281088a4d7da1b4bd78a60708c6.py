code = """import json, pandas as pd

quote = pd.DataFrame(var_call_a01UeEzS1IX4l2aY9eHSYS8L)
qli = pd.DataFrame(var_call_vUVzCfL5ZJd8Q99JpKKsQK02)
pbe = pd.DataFrame(var_call_e3Y5ED06Y4pf5znCqCNcHTf8)

# Load knowledge articles (may be large)
ka_src = var_call_pSbvHimnsXygo5T2hlvnv3KD
if isinstance(ka_src, str) and ka_src.endswith('.json'):
    with open(ka_src, 'r', encoding='utf-8') as f:
        ka = pd.DataFrame(json.load(f))
else:
    ka = pd.DataFrame(ka_src)

# Normalize ids for joins
for df, col in [(qli,'PricebookEntryId'), (pbe,'Id')]:
    if col in df.columns:
        df[col+'_norm'] = df[col].astype(str).str.replace('#','', regex=False).str.strip()

qli['QuoteId_norm'] = qli['QuoteId'].astype(str).str.replace('#','', regex=False).str.strip()

pbe['ProductName_clean'] = pbe.get('ProductName', pd.Series(dtype=str)).astype(str).str.strip()

# Determine discounts vs policy candidates
qli['Discount_num'] = pd.to_numeric(qli['Discount'], errors='coerce')

# Find policy articles likely about quote approval/discount/setup/cost
text_cols = []
for c in ['title','summary','faq_answer__c','urlname']:
    if c in ka.columns:
        text_cols.append(c)

def row_text(r):
    parts=[]
    for c in text_cols:
        v=r.get(c)
        if pd.notna(v):
            parts.append(str(v))
    return ' '.join(parts).lower()

ka['__text'] = ka.apply(row_text, axis=1) if len(ka)>0 else ''
keywords = ['quote', 'approval', 'discount', 'setup', 'implementation', 'professional services', 'pricing', 'cost', 'margin']
ka['__score'] = ka['__text'].apply(lambda t: sum(1 for k in keywords if k in t)) if len(ka)>0 else 0
candidates = ka.sort_values(['__score'], ascending=False).head(50)

violations = []
# simple heuristic: if any line discount > 10%, flag conflict with any article mentioning max discount 10%
max_disc = qli['Discount_num'].max() if len(qli)>0 else None

# Search for explicit discount threshold in articles
import re
threshold_articles=[]
for _,r in candidates.iterrows():
    txt=r['__text']
    m=re.search(r'max(imum)?\s+discount\s*(of)?\s*(\d{1,2})\s*%|discount\s+cap\s*(is)?\s*(\d{1,2})\s*%|no\s+more\s+than\s*(\d{1,2})\s*%\s+discount', txt)
    if m:
        nums=[g for g in m.groups() if g and g.isdigit()]
        if nums:
            threshold_articles.append((r['id'], int(nums[-1])))

violating_article=None
if max_disc is not None and pd.notna(max_disc):
    # if any article provides a threshold and quote exceeds it, pick that article id
    for aid,thr in sorted(threshold_articles, key=lambda x:x[1]):
        if float(max_disc) > thr:
            violating_article=aid
            break

# If no explicit threshold match, try generic: detect if setup fees must be itemized etc (not available)
# With available data, only discount-based compliance is checkable.

result = violating_article if violating_article is not None else None
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_a01UeEzS1IX4l2aY9eHSYS8L': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_vUVzCfL5ZJd8Q99JpKKsQK02': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_e3Y5ED06Y4pf5znCqCNcHTf8': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'ListUnitPrice': '499.99', 'ProductName': 'PulseSim Pro'}, {'Id': '01uWt0000027P5NIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hV58IAE', 'ListUnitPrice': '599.99', 'ProductName': 'SecureFlow Suite'}, {'Id': '#01uWt0000027P6zIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hTUkIAM', 'ListUnitPrice': '399.99', 'ProductName': 'CloudLink Designer'}, {'Id': '#01uWt0000027P8bIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV6jIAE', 'ListUnitPrice': '349.99', 'ProductName': 'EcoPCB Creator   '}, {'Id': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'ListUnitPrice': '529.99', 'ProductName': 'AI Cirku-Tech'}, {'Id': '01uWt0000027PADIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'ListUnitPrice': '299.99', 'ProductName': 'DevVision IDE'}, {'Id': '01uWt0000027PDRIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVBZIA2', 'ListUnitPrice': '399.99', 'ProductName': 'EduTech Lab'}, {'Id': '01uWt0000027PIIIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVI1IAM', 'ListUnitPrice': '529.99', 'ProductName': 'AIOptics Vision'}, {'Id': '01uWt0000027PIJIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVptIAE', 'ListUnitPrice': '459.99', 'ProductName': 'DesignEdge Pro'}, {'Id': '#01uWt0000027PN7IAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPfgIAE', 'ListUnitPrice': '399.99', 'ProductName': 'EcoPower Convert'}, {'Id': '#01uWt0000027POjIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVMrIAM', 'ListUnitPrice': '299.99', 'ProductName': 'TrainEDU Suite'}, {'Id': '01uWt0000027PTZIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV0IIAU', 'ListUnitPrice': '449.99', 'ProductName': 'NextGen IDE'}, {'Id': '#01uWt0000027PTaIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVUvIAM', 'ListUnitPrice': '459.99', 'ProductName': 'OptiEnergy Suite'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'ListUnitPrice': '339.99', 'ProductName': 'CircuitSync Pro'}, {'Id': '#01uWt0000027PWnIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ6IAM', 'ListUnitPrice': '429.99', 'ProductName': 'VeriSim Express  '}, {'Id': '01uWt0000027Pa1IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVTJIA2', 'ListUnitPrice': '529.99', 'ProductName': 'IntegrGuard Secure'}, {'Id': '01uWt0000027PerIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVZlIAM', 'ListUnitPrice': '559.99', 'ProductName': 'SecuManage Pro  '}, {'Id': '01uWt0000027PgTIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVbNIAU', 'ListUnitPrice': '349.99', 'ProductName': 'EnergyReduce Pro'}, {'Id': '01uWt0000027PgUIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVt7IAE', 'ListUnitPrice': '379.99', 'ProductName': 'PCB EcoModel  '}, {'Id': '01uWt0000027Pi5IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'ListUnitPrice': '399.99', 'ProductName': 'CollabDesign Studio'}, {'Id': '01uWt0000027PjhIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVebIAE', 'ListUnitPrice': '549.99', 'ProductName': 'CircuitAI Innovator'}, {'Id': '01uWt0000027PlJIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUsEIAU', 'ListUnitPrice': '499.99', 'ProductName': 'SimuCheck Ultra'}, {'Id': '#01uWt0000027Pq9IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjRIAU', 'ListUnitPrice': '429.99', 'ProductName': 'Workflow Genius'}, {'Id': '#01uWt0000027PtNIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVmfIAE', 'ListUnitPrice': '399.99', 'ProductName': 'EduTech Advance'}, {'Id': '01uWt0000027PtOIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVwLIAU', 'ListUnitPrice': '529.99', 'ProductName': 'SimulateX Edge'}, {'Id': '01uWt0000027Q1RIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVujIAE', 'ListUnitPrice': '579.99', 'ProductName': 'CyberShield Core'}, {'Id': '#01uWt0000027Q33IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hOd8IAE', 'ListUnitPrice': '499.99', 'ProductName': 'AutoLayout Master'}, {'Id': '#01uWt0000027Q34IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUgwIAE', 'ListUnitPrice': '599.99', 'ProductName': 'AI DesignShift'}, {'Id': '01uWt0000027Q4fIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjSIAU', 'ListUnitPrice': '299.99', 'ProductName': 'InnoTrain Hub'}, {'Id': '01uWt0000027Q6HIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUtqIAE', 'ListUnitPrice': '619.99', 'ProductName': 'SecureTrack Pro '}], 'var_call_pSbvHimnsXygo5T2hlvnv3KD': 'file_storage/call_pSbvHimnsXygo5T2hlvnv3KD.json', 'var_call_VgfTrTFZnaBMGXcnJY5uNHip': []}

exec(code, env_args)
