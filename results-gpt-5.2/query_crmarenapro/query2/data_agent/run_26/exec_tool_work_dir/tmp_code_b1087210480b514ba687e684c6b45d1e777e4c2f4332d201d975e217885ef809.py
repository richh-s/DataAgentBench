code = """import json, pandas as pd

quote = pd.DataFrame(var_call_d6h1R9Ws1RG4KMW57XD2seSP)
qli = pd.DataFrame(var_call_fUjjkUODXPv11oy7tkKUQcZM)
pbe = pd.DataFrame(var_call_tDZi9pn3bv7zaOcT4VdE7YEZ)

# load large knowledge + products if needed

def load_if_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

knowledge = load_if_path(var_call_vyXXHO1WaKRLvHk18pBPLQMK)
products = load_if_path(var_call_ExukIiEv3zQVvIfZgzJqBWYr)

kdf = pd.DataFrame(knowledge)

# compute effective discount percent per line
for col in ['Quantity','UnitPrice','Discount','TotalPrice']:
    if col in qli.columns:
        qli[col] = pd.to_numeric(qli[col], errors='coerce')

qli['list_total'] = qli['Quantity'] * qli['UnitPrice']
qli['effective_discount_pct'] = (1 - (qli['TotalPrice'] / qli['list_total']))*100

max_disc = float(qli['effective_discount_pct'].max())

# find policy-like knowledge articles about discounts/approval/setup
# heuristic keyword search
text = (kdf['title'].fillna('') + ' ' + kdf['summary'].fillna('') + ' ' + kdf['faq_answer__c'].fillna('')).str.lower()
keywords = ['discount', 'quote', 'approval', 'setup', 'implementation', 'professional services', 'pricing', 'cost', 'waiver']
mask = text.apply(lambda s: any(k in s for k in keywords))
policy_kdf = kdf[mask].copy()

# look specifically for discount thresholds if present
# We'll pick article that mentions a max discount lower than observed
violating_id = None
threshold_found = None
for _, r in policy_kdf.iterrows():
    s = (str(r.get('faq_answer__c',''))+' '+str(r.get('summary',''))+' '+str(r.get('title',''))).lower()
    # simple parse for patterns like 'over 10%' or 'greater than 15%'
    import re
    for m in re.finditer(r'(?:over|greater than|more than|above)\s*(\d{1,2})\s*%|(?:max(?:imum)?\s*discount\s*[:is]*\s*)(\d{1,2})\s*%|(?:discounts?\s*up to\s*)(\d{1,2})\s*%', s):
        nums = [g for g in m.groups() if g is not None]
        if not nums:
            continue
        thr = int(nums[0])
        threshold_found = thr
        if max_disc > thr + 1e-9:
            violating_id = r['id']
            break
    if violating_id:
        break

# If no explicit threshold found, we can't assert violation from knowledge.
res = violating_id if violating_id else None
print('__RESULT__:')
print(json.dumps({'violating_knowledge_article_id': res, 'max_effective_discount_pct': max_disc, 'policy_articles_considered': int(policy_kdf.shape[0])}))"""

env_args = {'var_call_d6h1R9Ws1RG4KMW57XD2seSP': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_fUjjkUODXPv11oy7tkKUQcZM': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVEnIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hV6jIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '01tWt000006hV57IAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVQ5IAM', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_vyXXHO1WaKRLvHk18pBPLQMK': 'file_storage/call_vyXXHO1WaKRLvHk18pBPLQMK.json', 'var_call_ExukIiEv3zQVvIfZgzJqBWYr': 'file_storage/call_ExukIiEv3zQVvIfZgzJqBWYr.json', 'var_call_tDZi9pn3bv7zaOcT4VdE7YEZ': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027P3mIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVhpIAE', 'UnitPrice': '489.99'}, {'Id': '01uWt0000027P5NIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hV58IAE', 'UnitPrice': '599.99'}, {'Id': '#01uWt0000027P6zIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hTUkIAM', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027P8bIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV6jIAE', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027PBpIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV9xIAE', 'UnitPrice': '449.99'}, {'Id': '01uWt0000027PDRIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVBZIA2', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PF3IAM', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVDBIA2', 'UnitPrice': '549.99'}, {'Id': '#01uWt0000027PGfIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVEnIAM', 'UnitPrice': '479.99'}, {'Id': '01uWt0000027PIHIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVGPIA2', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PIIIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVI1IAM', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PIJIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVptIAE', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PJtIAM', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVJdIAM', 'UnitPrice': '649.99'}, {'Id': '01uWt0000027PLVIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVLFIA2', 'UnitPrice': '459.99'}, {'Id': '#01uWt0000027PN7IAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPfgIAE', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027POjIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVMrIAM', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027POkIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hRfqIAE', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027PQLIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hUKMIA2', 'UnitPrice': '489.99'}, {'Id': '#01uWt0000027PRxIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVOTIA2', 'UnitPrice': '559.99'}, {'Id': '01uWt0000027PTZIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV0IIAU', 'UnitPrice': '449.99'}, {'Id': '#01uWt0000027PTaIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVUvIAM', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}, {'Id': '#01uWt0000027PWnIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ6IAM', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027PYPIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVRhIAM', 'UnitPrice': '319.99'}, {'Id': '01uWt0000027Pa1IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVTJIA2', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PbdIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVWXIA2', 'UnitPrice': '389.99'}, {'Id': '01uWt0000027PdFIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVY9IAM', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027PerIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVZlIAM', 'UnitPrice': '559.99'}, {'Id': '01uWt0000027PgTIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVbNIAU', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027PgUIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVt7IAE', 'UnitPrice': '379.99'}, {'Id': '01uWt0000027Pi5IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PjhIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVebIAE', 'UnitPrice': '549.99'}, {'Id': '01uWt0000027PlJIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUsEIAU', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027PmvIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVJeIAM', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PoXIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVgDIAU', 'UnitPrice': '459.99'}, {'Id': '#01uWt0000027Pq9IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjRIAU', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027PrlIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVl3IAE', 'UnitPrice': '369.99'}, {'Id': '#01uWt0000027PtNIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVmfIAE', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PtOIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVwLIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PuzIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVoHIAU', 'UnitPrice': '629.99'}, {'Id': '01uWt0000027PwbIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUUwIAM', 'UnitPrice': '559.99'}, {'Id': '#01uWt0000027PyDIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVrVIAU', 'UnitPrice': '649.99'}, {'Id': '#01uWt0000027PzpIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVrWIAU', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027Q1RIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVujIAE', 'UnitPrice': '579.99'}, {'Id': '#01uWt0000027Q33IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hOd8IAE', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027Q34IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUgwIAE', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027Q4fIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjSIAU', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Q6HIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUtqIAE', 'UnitPrice': '619.99'}], 'var_call_qwwdy9MMFxJIVaUx1eECiVar': [{'Id': '006Wt000007BHHfIAO', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Name': 'InnovateX Solutions Technology Integration Opportunity', 'Description': 'TechPulse Solutions offers InnovateX Solutions a suite of tools, including AI-powered CircuitSync Pro and environmentally-focused EcoPCB Creator, to enhance their design capabilities. By incorporating DesignWave Automation, InnovateX can streamline workflows, ensuring faster project completion and higher client satisfaction. Integrating PulseSim Pro will optimize circuit design verification with precision and speed.', 'Probability': '75.0', 'CreatedDate': '2021-05-20T14:15:30.000+0000', 'CloseDate': '2021-07-15'}]}

exec(code, env_args)
