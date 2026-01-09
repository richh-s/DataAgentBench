code = """import json, pandas as pd

quote = pd.DataFrame(var_call_xda4Pa7OtaOKni9FefKRO337)
qli = pd.DataFrame(var_call_Q0cFxxIjVT0K5rskAFtalcot)
pbe = pd.DataFrame(var_call_WnzWUGo00tWQ2XzWiB9oQjb5)

# normalize ids
for df, cols in [(qli,['PricebookEntryId','Product2Id','QuoteId']), (pbe,['PricebookEntryId','Product2Id'])]:
    for c in cols:
        if c in df.columns:
            df[c+'_norm'] = df[c].astype(str).str.replace('#','', regex=False).str.strip()

# parse numeric
for c in ['Quantity','UnitPrice','Discount','TotalPrice']:
    if c in qli.columns:
        qli[c] = pd.to_numeric(qli[c], errors='coerce')

pbe['ListUnitPrice'] = pd.to_numeric(pbe['ListUnitPrice'], errors='coerce')

# join to get list price per line
merged = qli.merge(pbe, left_on='PricebookEntryId_norm', right_on='PricebookEntryId_norm', how='left', suffixes=('','_pbe'))

# detect discount policy violations: discount > 10% off list price
# compute effective discount vs list if available; else use provided Discount
merged['eff_discount_pct'] = None
mask = merged['ListUnitPrice'].notna() & merged['UnitPrice'].notna() & (merged['ListUnitPrice']!=0)
merged.loc[mask,'eff_discount_pct'] = (1 - (merged.loc[mask,'UnitPrice']/merged.loc[mask,'ListUnitPrice']))*100
merged['eff_discount_pct'] = pd.to_numeric(merged['eff_discount_pct'], errors='coerce')
merged['disc_pct_used'] = merged['eff_discount_pct'].fillna(merged['Discount'])

viol_discount = merged['disc_pct_used'] > 10.0

# load knowledge articles and find matching policy article about discount threshold
import pathlib
ka_path = var_call_J6JmBZuZoz9uVGbbVErseoAY
if isinstance(ka_path, str) and ka_path.endswith('.json'):
    data = json.load(open(ka_path,'r',encoding='utf-8'))
else:
    data = var_call_J6JmBZuZoz9uVGbbVErseoAY
ka = pd.DataFrame(data)

# find candidate article mentioning discount and 10% or approvals
text = (ka['title'].fillna('') + ' ' + ka['summary'].fillna('') + ' ' + ka['faq_answer__c'].fillna('')).str.lower()
cand = ka[text.str.contains('discount') & (text.str.contains('10%') | text.str.contains('10 percent') | text.str.contains('ten percent'))]

violated_article_id = None
if viol_discount.any():
    if len(cand)>0:
        violated_article_id = str(cand.iloc[0]['id'])
    else:
        # fallback: any article that contains 'discount' and 'policy'
        cand2 = ka[text.str.contains('discount') & text.str.contains('policy')]
        if len(cand2)>0:
            violated_article_id = str(cand2.iloc[0]['id'])
        else:
            violated_article_id = None

print('__RESULT__:')
print(json.dumps({'violated_article_id': violated_article_id}))"""

env_args = {'var_call_xda4Pa7OtaOKni9FefKRO337': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_Q0cFxxIjVT0K5rskAFtalcot': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_J6JmBZuZoz9uVGbbVErseoAY': 'file_storage/call_J6JmBZuZoz9uVGbbVErseoAY.json', 'var_call_WnzWUGo00tWQ2XzWiB9oQjb5': [{'PricebookEntryId': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'ListUnitPrice': '499.99', 'ProductName': 'PulseSim Pro'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hV58IAE', 'ListUnitPrice': '599.99', 'ProductName': 'SecureFlow Suite'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hTUkIAM', 'ListUnitPrice': '399.99', 'ProductName': 'CloudLink Designer'}, {'PricebookEntryId': '#01uWt0000027P8bIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV6jIAE', 'ListUnitPrice': '349.99', 'ProductName': 'EcoPCB Creator   '}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'ListUnitPrice': '529.99', 'ProductName': 'AI Cirku-Tech'}, {'PricebookEntryId': '01uWt0000027PADIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'ListUnitPrice': '299.99', 'ProductName': 'DevVision IDE'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVBZIA2', 'ListUnitPrice': '399.99', 'ProductName': 'EduTech Lab'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVI1IAM', 'ListUnitPrice': '529.99', 'ProductName': 'AIOptics Vision'}, {'PricebookEntryId': '01uWt0000027PIJIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVptIAE', 'ListUnitPrice': '459.99', 'ProductName': 'DesignEdge Pro'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPfgIAE', 'ListUnitPrice': '399.99', 'ProductName': 'EcoPower Convert'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVMrIAM', 'ListUnitPrice': '299.99', 'ProductName': 'TrainEDU Suite'}, {'PricebookEntryId': '01uWt0000027PTZIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV0IIAU', 'ListUnitPrice': '449.99', 'ProductName': 'NextGen IDE'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVUvIAM', 'ListUnitPrice': '459.99', 'ProductName': 'OptiEnergy Suite'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'ListUnitPrice': '339.99', 'ProductName': 'CircuitSync Pro'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ6IAM', 'ListUnitPrice': '429.99', 'ProductName': 'VeriSim Express  '}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVTJIA2', 'ListUnitPrice': '529.99', 'ProductName': 'IntegrGuard Secure'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVZlIAM', 'ListUnitPrice': '559.99', 'ProductName': 'SecuManage Pro  '}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVbNIAU', 'ListUnitPrice': '349.99', 'ProductName': 'EnergyReduce Pro'}, {'PricebookEntryId': '01uWt0000027PgUIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVt7IAE', 'ListUnitPrice': '379.99', 'ProductName': 'PCB EcoModel  '}, {'PricebookEntryId': '01uWt0000027Pi5IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'ListUnitPrice': '399.99', 'ProductName': 'CollabDesign Studio'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVebIAE', 'ListUnitPrice': '549.99', 'ProductName': 'CircuitAI Innovator'}, {'PricebookEntryId': '01uWt0000027PlJIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUsEIAU', 'ListUnitPrice': '499.99', 'ProductName': 'SimuCheck Ultra'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjRIAU', 'ListUnitPrice': '429.99', 'ProductName': 'Workflow Genius'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVmfIAE', 'ListUnitPrice': '399.99', 'ProductName': 'EduTech Advance'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVwLIAU', 'ListUnitPrice': '529.99', 'ProductName': 'SimulateX Edge'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVujIAE', 'ListUnitPrice': '579.99', 'ProductName': 'CyberShield Core'}, {'PricebookEntryId': '#01uWt0000027Q33IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hOd8IAE', 'ListUnitPrice': '499.99', 'ProductName': 'AutoLayout Master'}, {'PricebookEntryId': '#01uWt0000027Q34IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUgwIAE', 'ListUnitPrice': '599.99', 'ProductName': 'AI DesignShift'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjSIAU', 'ListUnitPrice': '299.99', 'ProductName': 'InnoTrain Hub'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUtqIAE', 'ListUnitPrice': '619.99', 'ProductName': 'SecureTrack Pro '}]}

exec(code, env_args)
