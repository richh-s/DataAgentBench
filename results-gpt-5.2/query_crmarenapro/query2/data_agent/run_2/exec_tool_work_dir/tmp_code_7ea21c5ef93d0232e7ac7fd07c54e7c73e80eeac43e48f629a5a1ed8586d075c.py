code = """import json, pandas as pd, re

quote = pd.DataFrame(var_call_bHEeaCvHkytMRduFKmypjmpj)
qli = pd.DataFrame(var_call_dLMVd2fF3SNiQ0fBFHlhMbRZ)

# load knowledge articles
ka_src = var_call_UvEayypfONnBAb7MGORXQQxM
if isinstance(ka_src, str):
    with open(ka_src, 'r', encoding='utf-8') as f:
        ka = pd.DataFrame(json.load(f))
else:
    ka = pd.DataFrame(ka_src)

# pricebook entries
pbe = pd.DataFrame(var_call_gKf1kZBAI0nUByb38qjkoyre)

def norm_id(x):
    if x is None:
        return None
    return str(x).replace('#','').strip()

for c in ['PricebookEntryId','QuoteId','Product2Id']:
    if c in qli.columns:
        qli[c+'_n'] = qli[c].map(norm_id)

pbe['PricebookEntryId_n'] = pbe['PricebookEntryId'].map(norm_id)

# determine discount violations: infer policy from knowledge article text
text_cols = ['title','summary','faq_answer__c','urlname']
ka['__text'] = ka[text_cols].fillna('').agg(' '.join, axis=1)

# Find candidate policy articles mentioning quote approval/discount/setup/cost
pat = re.compile(r"(quote|approval|discount|setup|implementation|pricing|cost)", re.IGNORECASE)
ka_cand = ka[ka['__text'].str.contains(pat, na=False)].copy()

# Extract numeric discount thresholds from candidate articles
thr_re = re.compile(r"(discount)[^\d]{0,40}(\d{1,2})\s*%", re.IGNORECASE)
setup_re = re.compile(r"setup[^\d]{0,40}(\d+(?:\.\d+)?)\s*%", re.IGNORECASE)

cand_thresholds = []
for _, r in ka_cand.iterrows():
    t = r['__text']
    m = thr_re.findall(t)
    # take max mentioned discount percent if any
    disc_perc = max([int(x[1]) for x in m], default=None)
    m2 = setup_re.findall(t)
    setup_perc = max([float(x) for x in m2], default=None)
    cand_thresholds.append((r.get('id'), disc_perc, setup_perc, t))

# Compute max discount on quote line items
if len(qli)==0:
    max_disc = None
else:
    qli['Discount_num'] = pd.to_numeric(qli['Discount'], errors='coerce')
    max_disc = float(qli['Discount_num'].max()) if qli['Discount_num'].notna().any() else None

# Assume policy: discounts > allowed percent violate.
violating_article = None
if max_disc is not None:
    # choose strictest (lowest) discount threshold available
    thresholds = [(cid, disc) for cid, disc, sp, t in cand_thresholds if disc is not None]
    if thresholds:
        lowest = min(thresholds, key=lambda x: x[1])
        allowed = lowest[1]
        if max_disc > allowed:
            violating_article = lowest[0]

# If no extracted thresholds, attempt keyword rules: any mention 'no discount over 10%' etc.
# fallback: look for explicit 'discount over 10% requires VP approval' etc and if max_disc >=15 triggers
if violating_article is None and max_disc is not None:
    for cid, disc, sp, t in cand_thresholds:
        if disc is None:
            m = re.search(r"discounts?\s*(?:above|over|greater\s*than)\s*(\d{1,2})\s*%", t, re.IGNORECASE)
            if m:
                allowed = int(m.group(1))
                if max_disc > allowed:
                    violating_article = cid
                    break

# Setup/cost not present in schema; if any policy article forbids missing setup fee and quote description lacks it, can't infer.

result = violating_article if violating_article is not None else None
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_bHEeaCvHkytMRduFKmypjmpj': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_dLMVd2fF3SNiQ0fBFHlhMbRZ': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_UvEayypfONnBAb7MGORXQQxM': 'file_storage/call_UvEayypfONnBAb7MGORXQQxM.json', 'var_call_gKf1kZBAI0nUByb38qjkoyre': [{'PricebookEntryId': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'ListUnitPrice': '499.99', 'ProductName': 'PulseSim Pro'}, {'PricebookEntryId': '01uWt0000027P3mIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVhpIAE', 'ListUnitPrice': '489.99', 'ProductName': 'None'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hV58IAE', 'ListUnitPrice': '599.99', 'ProductName': 'SecureFlow Suite'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hTUkIAM', 'ListUnitPrice': '399.99', 'ProductName': 'CloudLink Designer'}, {'PricebookEntryId': '#01uWt0000027P8bIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV6jIAE', 'ListUnitPrice': '349.99', 'ProductName': 'EcoPCB Creator   '}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'ListUnitPrice': '529.99', 'ProductName': 'AI Cirku-Tech'}, {'PricebookEntryId': '01uWt0000027PADIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'ListUnitPrice': '299.99', 'ProductName': 'DevVision IDE'}, {'PricebookEntryId': '01uWt0000027PBpIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV9xIAE', 'ListUnitPrice': '449.99', 'ProductName': 'None'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVBZIA2', 'ListUnitPrice': '399.99', 'ProductName': 'EduTech Lab'}, {'PricebookEntryId': '01uWt0000027PF3IAM', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVDBIA2', 'ListUnitPrice': '549.99', 'ProductName': 'None'}, {'PricebookEntryId': '#01uWt0000027PGfIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVEnIAM', 'ListUnitPrice': '479.99', 'ProductName': 'None'}, {'PricebookEntryId': '01uWt0000027PIHIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVGPIA2', 'ListUnitPrice': '599.99', 'ProductName': 'None'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVI1IAM', 'ListUnitPrice': '529.99', 'ProductName': 'AIOptics Vision'}, {'PricebookEntryId': '01uWt0000027PIJIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVptIAE', 'ListUnitPrice': '459.99', 'ProductName': 'DesignEdge Pro'}, {'PricebookEntryId': '01uWt0000027PJtIAM', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVJdIAM', 'ListUnitPrice': '649.99', 'ProductName': 'None'}, {'PricebookEntryId': '01uWt0000027PLVIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVLFIA2', 'ListUnitPrice': '459.99', 'ProductName': 'None'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPfgIAE', 'ListUnitPrice': '399.99', 'ProductName': 'EcoPower Convert'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVMrIAM', 'ListUnitPrice': '299.99', 'ProductName': 'TrainEDU Suite'}, {'PricebookEntryId': '01uWt0000027POkIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hRfqIAE', 'ListUnitPrice': '349.99', 'ProductName': 'None'}, {'PricebookEntryId': '01uWt0000027PQLIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hUKMIA2', 'ListUnitPrice': '489.99', 'ProductName': 'None'}, {'PricebookEntryId': '#01uWt0000027PRxIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVOTIA2', 'ListUnitPrice': '559.99', 'ProductName': 'None'}, {'PricebookEntryId': '01uWt0000027PTZIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV0IIAU', 'ListUnitPrice': '449.99', 'ProductName': 'NextGen IDE'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVUvIAM', 'ListUnitPrice': '459.99', 'ProductName': 'OptiEnergy Suite'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'ListUnitPrice': '339.99', 'ProductName': 'CircuitSync Pro'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ6IAM', 'ListUnitPrice': '429.99', 'ProductName': 'VeriSim Express  '}, {'PricebookEntryId': '01uWt0000027PYPIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVRhIAM', 'ListUnitPrice': '319.99', 'ProductName': 'None'}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVTJIA2', 'ListUnitPrice': '529.99', 'ProductName': 'IntegrGuard Secure'}, {'PricebookEntryId': '01uWt0000027PbdIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVWXIA2', 'ListUnitPrice': '389.99', 'ProductName': 'None'}, {'PricebookEntryId': '01uWt0000027PdFIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVY9IAM', 'ListUnitPrice': '299.99', 'ProductName': 'None'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVZlIAM', 'ListUnitPrice': '559.99', 'ProductName': 'SecuManage Pro  '}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVbNIAU', 'ListUnitPrice': '349.99', 'ProductName': 'EnergyReduce Pro'}, {'PricebookEntryId': '01uWt0000027PgUIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVt7IAE', 'ListUnitPrice': '379.99', 'ProductName': 'PCB EcoModel  '}, {'PricebookEntryId': '01uWt0000027Pi5IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'ListUnitPrice': '399.99', 'ProductName': 'CollabDesign Studio'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVebIAE', 'ListUnitPrice': '549.99', 'ProductName': 'CircuitAI Innovator'}, {'PricebookEntryId': '01uWt0000027PlJIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUsEIAU', 'ListUnitPrice': '499.99', 'ProductName': 'SimuCheck Ultra'}, {'PricebookEntryId': '#01uWt0000027PmvIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVJeIAM', 'ListUnitPrice': '599.99', 'ProductName': 'None'}, {'PricebookEntryId': '01uWt0000027PoXIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVgDIAU', 'ListUnitPrice': '459.99', 'ProductName': 'None'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjRIAU', 'ListUnitPrice': '429.99', 'ProductName': 'Workflow Genius'}, {'PricebookEntryId': '01uWt0000027PrlIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVl3IAE', 'ListUnitPrice': '369.99', 'ProductName': 'None'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVmfIAE', 'ListUnitPrice': '399.99', 'ProductName': 'EduTech Advance'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVwLIAU', 'ListUnitPrice': '529.99', 'ProductName': 'SimulateX Edge'}, {'PricebookEntryId': '01uWt0000027PuzIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVoHIAU', 'ListUnitPrice': '629.99', 'ProductName': 'None'}, {'PricebookEntryId': '01uWt0000027PwbIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUUwIAM', 'ListUnitPrice': '559.99', 'ProductName': 'None'}, {'PricebookEntryId': '#01uWt0000027PyDIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVrVIAU', 'ListUnitPrice': '649.99', 'ProductName': 'None'}, {'PricebookEntryId': '#01uWt0000027PzpIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVrWIAU', 'ListUnitPrice': '429.99', 'ProductName': 'None'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVujIAE', 'ListUnitPrice': '579.99', 'ProductName': 'CyberShield Core'}, {'PricebookEntryId': '#01uWt0000027Q33IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hOd8IAE', 'ListUnitPrice': '499.99', 'ProductName': 'AutoLayout Master'}, {'PricebookEntryId': '#01uWt0000027Q34IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUgwIAE', 'ListUnitPrice': '599.99', 'ProductName': 'AI DesignShift'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjSIAU', 'ListUnitPrice': '299.99', 'ProductName': 'InnoTrain Hub'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUtqIAE', 'ListUnitPrice': '619.99', 'ProductName': 'SecureTrack Pro '}], 'var_call_siEJXcocDZvhqQiGm1e8Ztdm': 'file_storage/call_siEJXcocDZvhqQiGm1e8Ztdm.json', 'var_call_OICPbhojfcMvC2MDD336M571': []}

exec(code, env_args)
