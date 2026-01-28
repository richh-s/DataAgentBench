code = """import json, pandas as pd

quote = pd.DataFrame(var_call_Q85uU5gkf6VGl0Ay4O46S9z1)
qli = pd.DataFrame(var_call_iXU4ylVrh8OPWrNDfd6b0mDi)
pricebook = pd.DataFrame(var_call_xc2YJbvZUSPFHxTuTdXqVAmb)

# load knowledge articles (may be file)
ka_src = var_call_uhFTwBeIs6Ru260NCHnq3ish
if isinstance(ka_src, str):
    with open(ka_src, 'r', encoding='utf-8') as f:
        ka = json.load(f)
else:
    ka = ka_src
ka_df = pd.DataFrame(ka)

# Normalize ids
for df, col in [(qli,'PricebookEntryId'),(qli,'Product2Id')]:
    if col in df.columns:
        df[col+'_norm'] = df[col].astype(str).str.replace('#','', regex=False).str.strip()
pricebook['Id_norm'] = pricebook['Id'].astype(str).str.replace('#','', regex=False).str.strip()
pricebook['Product2Id_norm'] = pricebook['Product2Id'].astype(str).str.replace('#','', regex=False).str.strip()

# Join to get list price
m = qli.merge(pricebook, left_on='PricebookEntryId_norm', right_on='Id_norm', how='left', suffixes=('','_pb'))

# Compute effective discount percent vs pricebook unit
m['UnitPrice_f'] = m['UnitPrice'].astype(float)
m['ListPrice_f'] = m['UnitPrice_pb'].astype(float)
# If unit price equals list price in our data model, discount in qli is explicit percent; verify within policy
m['Discount_f'] = m['Discount'].astype(float)

max_discount = m['Discount_f'].max() if len(m) else 0.0

# Find relevant policy knowledge articles mentioning discount/setup/implementation
text_cols = ['title','summary','faq_answer__c']
for c in text_cols:
    if c in ka_df.columns:
        ka_df[c] = ka_df[c].fillna('')
ka_df['blob'] = ka_df[[c for c in text_cols if c in ka_df.columns]].agg(' '.join, axis=1).str.lower()

candidates = ka_df[ka_df['blob'].str.contains('discount|setup|implementation|professional services|services|quote approval|approval|pricing', regex=True)]

# Determine violation: assume policy caps discount at 10% unless article says otherwise; look for explicit '10%' in policy articles
# If any article indicates max 10% and our max_discount>10 then violation that article.
policy_10 = candidates[candidates['blob'].str.contains('max|maximum|cap', regex=True) & candidates['blob'].str.contains('10%', regex=False)]

violate_id = None
if max_discount > 10:
    if len(policy_10):
        violate_id = policy_10.iloc[0]['id']

result = json.dumps(violate_id)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_Q85uU5gkf6VGl0Ay4O46S9z1': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_iXU4ylVrh8OPWrNDfd6b0mDi': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_uhFTwBeIs6Ru260NCHnq3ish': 'file_storage/call_uhFTwBeIs6Ru260NCHnq3ish.json', 'var_call_xc2YJbvZUSPFHxTuTdXqVAmb': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99', 'ProductName': 'PulseSim Pro'}, {'Id': '01uWt0000027P5NIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hV58IAE', 'UnitPrice': '599.99', 'ProductName': 'SecureFlow Suite'}, {'Id': '#01uWt0000027P6zIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hTUkIAM', 'UnitPrice': '399.99', 'ProductName': 'CloudLink Designer'}, {'Id': '#01uWt0000027P8bIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV6jIAE', 'UnitPrice': '349.99', 'ProductName': 'EcoPCB Creator   '}, {'Id': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'UnitPrice': '529.99', 'ProductName': 'AI Cirku-Tech'}, {'Id': '01uWt0000027PADIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'UnitPrice': '299.99', 'ProductName': 'DevVision IDE'}, {'Id': '01uWt0000027PDRIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVBZIA2', 'UnitPrice': '399.99', 'ProductName': 'EduTech Lab'}, {'Id': '01uWt0000027PIIIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVI1IAM', 'UnitPrice': '529.99', 'ProductName': 'AIOptics Vision'}, {'Id': '01uWt0000027PIJIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVptIAE', 'UnitPrice': '459.99', 'ProductName': 'DesignEdge Pro'}, {'Id': '#01uWt0000027PN7IAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPfgIAE', 'UnitPrice': '399.99', 'ProductName': 'EcoPower Convert'}, {'Id': '#01uWt0000027POjIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVMrIAM', 'UnitPrice': '299.99', 'ProductName': 'TrainEDU Suite'}, {'Id': '01uWt0000027PTZIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV0IIAU', 'UnitPrice': '449.99', 'ProductName': 'NextGen IDE'}, {'Id': '#01uWt0000027PTaIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVUvIAM', 'UnitPrice': '459.99', 'ProductName': 'OptiEnergy Suite'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99', 'ProductName': 'CircuitSync Pro'}, {'Id': '#01uWt0000027PWnIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ6IAM', 'UnitPrice': '429.99', 'ProductName': 'VeriSim Express  '}, {'Id': '01uWt0000027Pa1IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVTJIA2', 'UnitPrice': '529.99', 'ProductName': 'IntegrGuard Secure'}, {'Id': '01uWt0000027PerIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVZlIAM', 'UnitPrice': '559.99', 'ProductName': 'SecuManage Pro  '}, {'Id': '01uWt0000027PgTIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVbNIAU', 'UnitPrice': '349.99', 'ProductName': 'EnergyReduce Pro'}, {'Id': '01uWt0000027PgUIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVt7IAE', 'UnitPrice': '379.99', 'ProductName': 'PCB EcoModel  '}, {'Id': '01uWt0000027Pi5IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'UnitPrice': '399.99', 'ProductName': 'CollabDesign Studio'}, {'Id': '01uWt0000027PjhIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVebIAE', 'UnitPrice': '549.99', 'ProductName': 'CircuitAI Innovator'}, {'Id': '01uWt0000027PlJIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUsEIAU', 'UnitPrice': '499.99', 'ProductName': 'SimuCheck Ultra'}, {'Id': '#01uWt0000027Pq9IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjRIAU', 'UnitPrice': '429.99', 'ProductName': 'Workflow Genius'}, {'Id': '#01uWt0000027PtNIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVmfIAE', 'UnitPrice': '399.99', 'ProductName': 'EduTech Advance'}, {'Id': '01uWt0000027PtOIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVwLIAU', 'UnitPrice': '529.99', 'ProductName': 'SimulateX Edge'}, {'Id': '01uWt0000027Q1RIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVujIAE', 'UnitPrice': '579.99', 'ProductName': 'CyberShield Core'}, {'Id': '#01uWt0000027Q33IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hOd8IAE', 'UnitPrice': '499.99', 'ProductName': 'AutoLayout Master'}, {'Id': '#01uWt0000027Q34IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUgwIAE', 'UnitPrice': '599.99', 'ProductName': 'AI DesignShift'}, {'Id': '01uWt0000027Q4fIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjSIAU', 'UnitPrice': '299.99', 'ProductName': 'InnoTrain Hub'}, {'Id': '01uWt0000027Q6HIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUtqIAE', 'UnitPrice': '619.99', 'ProductName': 'SecureTrack Pro '}], 'var_call_BN4LW6ztnm40cEThcohkYiuz': []}

exec(code, env_args)
