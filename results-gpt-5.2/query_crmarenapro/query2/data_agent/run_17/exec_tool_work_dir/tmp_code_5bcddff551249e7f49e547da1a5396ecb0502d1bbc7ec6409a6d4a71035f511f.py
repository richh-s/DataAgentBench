code = """import json, pandas as pd

quote = pd.DataFrame(var_call_zUIEwgPMxzoDstwyh8JlDvgQ)
qli = pd.DataFrame(var_call_HOME5dWy2clXBtoBrBKpJWej)
pricebook = pd.DataFrame(var_call_q982eN3bfcx7kuHhCWdAION6)

# Clean ids
for df, cols in [(qli,['QuoteId','Product2Id','PricebookEntryId']), (pricebook,['PricebookEntryId','Product2Id'])]:
    for c in cols:
        if c in df.columns:
            df[c] = df[c].astype(str).str.replace('#','', regex=False).str.strip()

qli['UnitPrice'] = qli['UnitPrice'].astype(float)
qli['Discount'] = qli['Discount'].astype(float)
qli['Quantity'] = qli['Quantity'].astype(float)

pricebook['ListUnitPrice'] = pricebook['ListUnitPrice'].astype(float)

# join list price
m = qli.merge(pricebook[['PricebookEntryId','ListUnitPrice']], on='PricebookEntryId', how='left')

# compute discount percent vs list (if list available)
m['disc_pct'] = (1 - (m['UnitPrice']/m['ListUnitPrice']))*100

max_disc = m['disc_pct'].max()
# also compare stated Discount field
max_stated = m['Discount'].max()

# Load knowledge articles
path = var_call_GDz6ht1YY50t99Gl1DR6E8jK
if isinstance(path, str) and path.endswith('.json'):
    with open(path,'r',encoding='utf-8') as f:
        kav = json.load(f)
else:
    kav = var_call_GDz6ht1YY50t99Gl1DR6E8jK
kdf = pd.DataFrame(kav)
for c in ['id','title','faq_answer__c','summary','urlname']:
    if c in kdf.columns:
        kdf[c] = kdf[c].astype(str)

# Determine violation: if any discount > 10% (common policy); find article mentioning discount approval thresholds.
violation = None
if (max_disc > 10.0 + 1e-9) or (max_stated > 10.0 + 1e-9):
    # find best matching article
    text = (kdf['title'].str.lower().fillna('') + ' ' + kdf['summary'].str.lower().fillna('') + ' ' + kdf['faq_answer__c'].str.lower().fillna(''))
    candidates = kdf[text.str.contains('discount') & (text.str.contains('approval') | text.str.contains('quote') | text.str.contains('pricing') | text.str.contains('%'))]
    # if none, return None (can't justify)
    if len(candidates)==0:
        violation = None
    else:
        # prefer those with 'discount' and '10' or 'ten'
        cand_text = (candidates['title'].str.lower()+' '+candidates['summary'].str.lower()+' '+candidates['faq_answer__c'].str.lower())
        score = cand_text.str.count('discount')*3 + cand_text.str.contains('10').astype(int)*5 + cand_text.str.contains('ten').astype(int)*5 + cand_text.str.contains('approval').astype(int)*2 + cand_text.str.contains('quote').astype(int)
        best_id = candidates.iloc[score.values.argmax()]['id']
        violation = best_id.replace('#','').strip()

print('__RESULT__:')
print(json.dumps({'violation_article_id': violation}))"""

env_args = {'var_call_zUIEwgPMxzoDstwyh8JlDvgQ': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_HOME5dWy2clXBtoBrBKpJWej': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_GDz6ht1YY50t99Gl1DR6E8jK': 'file_storage/call_GDz6ht1YY50t99Gl1DR6E8jK.json', 'var_call_3vg4BcPlbvo8unCDMNcA06Vq': [{'Id': '00kWt000002HHpqIAG', 'OpportunityId': '006Wt000007BHHfIAO', 'Product2Id': '01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '00kWt000002HL76IAG', 'OpportunityId': '006Wt000007BHHfIAO', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'TotalPrice': '2260.9335'}, {'Id': '#00kWt000002HXg4IAG', 'OpportunityId': '006Wt000007BHHfIAO', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'TotalPrice': '4499.91'}, {'Id': '00kWt000002HavbIAC', 'OpportunityId': '#006Wt000007BHHfIAO', 'Product2Id': '01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'TotalPrice': '2379.932'}], 'var_call_q982eN3bfcx7kuHhCWdAION6': [{'PricebookEntryId': '01uWt0000027P3lIAE', 'ListUnitPrice': '499.99', 'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'ListUnitPrice': '599.99', 'Product2Id': '#01tWt000006hV58IAE', 'ProductName': 'SecureFlow Suite'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'PricebookEntryId': '#01uWt0000027P8bIAE', 'ListUnitPrice': '349.99', 'Product2Id': '01tWt000006hV6jIAE', 'ProductName': 'EcoPCB Creator   '}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'ListUnitPrice': '529.99', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech'}, {'PricebookEntryId': '01uWt0000027PADIA2', 'ListUnitPrice': '299.99', 'Product2Id': '01tWt000006hPffIAE', 'ProductName': 'DevVision IDE'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hVBZIA2', 'ProductName': 'EduTech Lab'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'ListUnitPrice': '529.99', 'Product2Id': '01tWt000006hVI1IAM', 'ProductName': 'AIOptics Vision'}, {'PricebookEntryId': '01uWt0000027PIJIA2', 'ListUnitPrice': '459.99', 'Product2Id': '01tWt000006hVptIAE', 'ProductName': 'DesignEdge Pro'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hPfgIAE', 'ProductName': 'EcoPower Convert'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'ListUnitPrice': '299.99', 'Product2Id': '01tWt000006hVMrIAM', 'ProductName': 'TrainEDU Suite'}, {'PricebookEntryId': '01uWt0000027PTZIA2', 'ListUnitPrice': '449.99', 'Product2Id': '01tWt000006hV0IIAU', 'ProductName': 'NextGen IDE'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'ListUnitPrice': '459.99', 'Product2Id': '01tWt000006hVUvIAM', 'ProductName': 'OptiEnergy Suite'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'ListUnitPrice': '339.99', 'Product2Id': '01tWt000006hVQ5IAM', 'ProductName': 'CircuitSync Pro'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'ListUnitPrice': '429.99', 'Product2Id': '01tWt000006hVQ6IAM', 'ProductName': 'VeriSim Express  '}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'ListUnitPrice': '529.99', 'Product2Id': '01tWt000006hVTJIA2', 'ProductName': 'IntegrGuard Secure'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'ListUnitPrice': '559.99', 'Product2Id': '01tWt000006hVZlIAM', 'ProductName': 'SecuManage Pro  '}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'ListUnitPrice': '349.99', 'Product2Id': '01tWt000006hVbNIAU', 'ProductName': 'EnergyReduce Pro'}, {'PricebookEntryId': '01uWt0000027PgUIAU', 'ListUnitPrice': '379.99', 'Product2Id': '01tWt000006hVt7IAE', 'ProductName': 'PCB EcoModel  '}, {'PricebookEntryId': '01uWt0000027Pi5IAE', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hVczIAE', 'ProductName': 'CollabDesign Studio'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'ListUnitPrice': '549.99', 'Product2Id': '01tWt000006hVebIAE', 'ProductName': 'CircuitAI Innovator'}, {'PricebookEntryId': '01uWt0000027PlJIAU', 'ListUnitPrice': '499.99', 'Product2Id': '01tWt000006hUsEIAU', 'ProductName': 'SimuCheck Ultra'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'ListUnitPrice': '429.99', 'Product2Id': '01tWt000006hVjRIAU', 'ProductName': 'Workflow Genius'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hVmfIAE', 'ProductName': 'EduTech Advance'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'ListUnitPrice': '529.99', 'Product2Id': '01tWt000006hVwLIAU', 'ProductName': 'SimulateX Edge'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'ListUnitPrice': '579.99', 'Product2Id': '01tWt000006hVujIAE', 'ProductName': 'CyberShield Core'}, {'PricebookEntryId': '#01uWt0000027Q33IAE', 'ListUnitPrice': '499.99', 'Product2Id': '01tWt000006hOd8IAE', 'ProductName': 'AutoLayout Master'}, {'PricebookEntryId': '#01uWt0000027Q34IAE', 'ListUnitPrice': '599.99', 'Product2Id': '01tWt000006hUgwIAE', 'ProductName': 'AI DesignShift'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'ListUnitPrice': '299.99', 'Product2Id': '01tWt000006hVjSIAU', 'ProductName': 'InnoTrain Hub'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'ListUnitPrice': '619.99', 'Product2Id': '01tWt000006hUtqIAE', 'ProductName': 'SecureTrack Pro '}]}

exec(code, env_args)
