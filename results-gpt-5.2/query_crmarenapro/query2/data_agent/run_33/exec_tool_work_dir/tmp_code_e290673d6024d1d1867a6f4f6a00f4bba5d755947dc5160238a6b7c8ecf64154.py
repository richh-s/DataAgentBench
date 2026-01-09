code = """import json, pandas as pd

quote = pd.DataFrame(var_call_hwPkOYdHgZs69qO7XciMNKIB)
qli = pd.DataFrame(var_call_dQg0IxNpfCY3DfAtlWcskr5u)

# load knowledge articles (may be file path)
ka_src = var_call_I2uPgZflvZSQD8xOoVGqEsHr
if isinstance(ka_src, str) and ka_src.endswith('.json'):
    with open(ka_src, 'r', encoding='utf-8') as f:
        ka = pd.DataFrame(json.load(f))
else:
    ka = pd.DataFrame(ka_src)

# Heuristic: look for quote approval / discount / setup policy articles
text_cols = ['title','summary','faq_answer__c','urlname']
for c in text_cols:
    if c not in ka.columns:
        ka[c] = ''

pattern_words = ['quote','pricing','discount','approval','setup','implementation','professional services','services','cost','tco']

def score_row(r):
    s = ' '.join([str(r.get(c,'')) for c in text_cols]).lower()
    return sum(1 for w in pattern_words if w in s)

ka['__score'] = ka.apply(score_row, axis=1)
ka_top = ka.sort_values('__score', ascending=False).head(50)

# Determine if quote has any obvious policy violation: discounts > threshold?
# Since policy not explicitly known, infer from articles mentioning max discount.
# Find candidate policy articles mentioning 'discount' and '%' and 'max'
import re
candidates = []
for _, r in ka.iterrows():
    blob = (' '.join([str(r.get(c,'')) for c in text_cols])).lower()
    if 'discount' in blob and ('%' in blob or 'percent' in blob) and ('max' in blob or 'maximum' in blob or 'cannot exceed' in blob or 'not exceed' in blob):
        candidates.append(r)

cand_df = pd.DataFrame(candidates)

# Extract first max discount percent from candidates
max_rules = []
for _, r in cand_df.iterrows():
    blob = (' '.join([str(r.get(c,'')) for c in text_cols])).lower()
    # find patterns like 'max 10%' or 'not exceed 15%'
    m = re.search(r'(max(?:imum)?|not exceed|cannot exceed)[^0-9]{0,20}(\d{1,2}(?:\.\d+)?)\s*%?', blob)
    if m:
        max_rules.append((r['id'], float(m.group(2))))

# compute max discount on quote line items
max_discount = None
if not qli.empty and 'Discount' in qli.columns:
    qli['Discount'] = pd.to_numeric(qli['Discount'], errors='coerce')
    max_discount = float(qli['Discount'].max())

violation_id = None
if max_discount is not None and len(max_rules)>0:
    # pick the strictest rule (lowest max)
    rule_id, rule_max = sorted(max_rules, key=lambda x: x[1])[0]
    if max_discount > rule_max + 1e-9:
        violation_id = rule_id

# If no explicit discount rule found, check for setup fees requirement articles
if violation_id is None:
    # look for articles that mention setup fee must be included / waived policy
    # assume if quote description lacks setup and there is article requiring setup line item.
    setup_articles = []
    for _, r in ka.iterrows():
        blob = (' '.join([str(r.get(c,'')) for c in text_cols])).lower()
        if 'setup' in blob and ('must' in blob or 'required' in blob) and ('fee' in blob or 'cost' in blob):
            setup_articles.append(r)
    setup_df = pd.DataFrame(setup_articles)
    # if such policy exists and no product seems like setup/service in line items
    if not setup_df.empty:
        prod_names = []
        # pricebook entries
        pbe = pd.DataFrame(var_call_USZU8fmSBTINaWf3RVzs68zl)
        if not pbe.empty:
            pbe_map = {str(x).replace('#','').strip(): y for x,y in zip(pbe['Id'], pbe['ProductName'])}
            for pid in qli.get('PricebookEntryId', []):
                key = str(pid).replace('#','').strip()
                prod_names.append(pbe_map.get(key,''))
        prod_blob = ' '.join(prod_names).lower()
        if 'setup' not in prod_blob and 'implementation' not in prod_blob and 'services' not in prod_blob:
            # pick most relevant setup policy article
            setup_df['__s'] = setup_df.apply(score_row, axis=1)
            violation_id = setup_df.sort_values('__s', ascending=False).iloc[0]['id']

result = violation_id if violation_id is not None else None
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_hwPkOYdHgZs69qO7XciMNKIB': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_dQg0IxNpfCY3DfAtlWcskr5u': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_I2uPgZflvZSQD8xOoVGqEsHr': 'file_storage/call_I2uPgZflvZSQD8xOoVGqEsHr.json', 'var_call_USZU8fmSBTINaWf3RVzs68zl': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99', 'ProductName': 'PulseSim Pro'}, {'Id': '01uWt0000027P5NIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hV58IAE', 'UnitPrice': '599.99', 'ProductName': 'SecureFlow Suite'}, {'Id': '#01uWt0000027P6zIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hTUkIAM', 'UnitPrice': '399.99', 'ProductName': 'CloudLink Designer'}, {'Id': '#01uWt0000027P8bIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV6jIAE', 'UnitPrice': '349.99', 'ProductName': 'EcoPCB Creator   '}, {'Id': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'UnitPrice': '529.99', 'ProductName': 'AI Cirku-Tech'}, {'Id': '01uWt0000027PADIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'UnitPrice': '299.99', 'ProductName': 'DevVision IDE'}, {'Id': '01uWt0000027PDRIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVBZIA2', 'UnitPrice': '399.99', 'ProductName': 'EduTech Lab'}, {'Id': '01uWt0000027PIIIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVI1IAM', 'UnitPrice': '529.99', 'ProductName': 'AIOptics Vision'}, {'Id': '01uWt0000027PIJIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVptIAE', 'UnitPrice': '459.99', 'ProductName': 'DesignEdge Pro'}, {'Id': '#01uWt0000027PN7IAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPfgIAE', 'UnitPrice': '399.99', 'ProductName': 'EcoPower Convert'}, {'Id': '#01uWt0000027POjIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVMrIAM', 'UnitPrice': '299.99', 'ProductName': 'TrainEDU Suite'}, {'Id': '01uWt0000027PTZIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV0IIAU', 'UnitPrice': '449.99', 'ProductName': 'NextGen IDE'}, {'Id': '#01uWt0000027PTaIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVUvIAM', 'UnitPrice': '459.99', 'ProductName': 'OptiEnergy Suite'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99', 'ProductName': 'CircuitSync Pro'}, {'Id': '#01uWt0000027PWnIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ6IAM', 'UnitPrice': '429.99', 'ProductName': 'VeriSim Express  '}, {'Id': '01uWt0000027Pa1IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVTJIA2', 'UnitPrice': '529.99', 'ProductName': 'IntegrGuard Secure'}, {'Id': '01uWt0000027PerIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVZlIAM', 'UnitPrice': '559.99', 'ProductName': 'SecuManage Pro  '}, {'Id': '01uWt0000027PgTIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVbNIAU', 'UnitPrice': '349.99', 'ProductName': 'EnergyReduce Pro'}, {'Id': '01uWt0000027PgUIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVt7IAE', 'UnitPrice': '379.99', 'ProductName': 'PCB EcoModel  '}, {'Id': '01uWt0000027Pi5IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'UnitPrice': '399.99', 'ProductName': 'CollabDesign Studio'}, {'Id': '01uWt0000027PjhIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVebIAE', 'UnitPrice': '549.99', 'ProductName': 'CircuitAI Innovator'}, {'Id': '01uWt0000027PlJIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUsEIAU', 'UnitPrice': '499.99', 'ProductName': 'SimuCheck Ultra'}, {'Id': '#01uWt0000027Pq9IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjRIAU', 'UnitPrice': '429.99', 'ProductName': 'Workflow Genius'}, {'Id': '#01uWt0000027PtNIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVmfIAE', 'UnitPrice': '399.99', 'ProductName': 'EduTech Advance'}, {'Id': '01uWt0000027PtOIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVwLIAU', 'UnitPrice': '529.99', 'ProductName': 'SimulateX Edge'}, {'Id': '01uWt0000027Q1RIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVujIAE', 'UnitPrice': '579.99', 'ProductName': 'CyberShield Core'}, {'Id': '#01uWt0000027Q33IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hOd8IAE', 'UnitPrice': '499.99', 'ProductName': 'AutoLayout Master'}, {'Id': '#01uWt0000027Q34IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUgwIAE', 'UnitPrice': '599.99', 'ProductName': 'AI DesignShift'}, {'Id': '01uWt0000027Q4fIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjSIAU', 'UnitPrice': '299.99', 'ProductName': 'InnoTrain Hub'}, {'Id': '01uWt0000027Q6HIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUtqIAE', 'UnitPrice': '619.99', 'ProductName': 'SecureTrack Pro '}], 'var_call_gnmW9FeYuIx6nh1XeJrENVee': [{'Id': '006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '#003Wt00000JqkgYIAR', 'OwnerId': '#005Wt000003NIybIAG', 'Probability': '75.0', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Name': 'InnovateX Solutions Technology Integration Opportunity', 'Description': 'TechPulse Solutions offers InnovateX Solutions a suite of tools, including AI-powered CircuitSync Pro and environmentally-focused EcoPCB Creator, to enhance their design capabilities. By incorporating DesignWave Automation, InnovateX can streamline workflows, ensuring faster project completion and higher client satisfaction. Integrating PulseSim Pro will optimize circuit design verification with precision and speed.', 'CreatedDate': '2021-05-20T14:15:30.000+0000', 'CloseDate': '2021-07-15'}], 'var_call_KtXtEBACZe6uMhWUyYE8ReW0': 'file_storage/call_KtXtEBACZe6uMhWUyYE8ReW0.json'}

exec(code, env_args)
