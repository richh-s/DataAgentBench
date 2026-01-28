code = """import json, pandas as pd

quote = pd.DataFrame(var_call_vkLpCbPyEphHdNQFwv6IBCXT)
qli = pd.DataFrame(var_call_PdYM4oMNCfDsmG4Pm8oTkRf0)
pbe = pd.DataFrame(var_call_Nd4nxtZglD49kQj1xtLwXsOt)

# Load knowledge articles (may be in file)
ka_src = var_call_eX5CHtKa5Pia77xxA8kOa2J3
if isinstance(ka_src, str):
    with open(ka_src, 'r', encoding='utf-8') as f:
        ka = pd.DataFrame(json.load(f))
else:
    ka = pd.DataFrame(ka_src)

# Normalize ids and numeric columns
def norm_id(s):
    if pd.isna(s):
        return None
    return str(s).replace('#','').strip()

for col in ['QuoteId','PricebookEntryId','Product2Id']:
    if col in qli.columns:
        qli[col+'_n'] = qli[col].map(norm_id)

pbe['PricebookEntryId_n'] = pbe['PricebookEntryId'].map(norm_id)
pbe['ListUnitPrice_f'] = pd.to_numeric(pbe['ListUnitPrice'], errors='coerce')

qli['UnitPrice_f'] = pd.to_numeric(qli['UnitPrice'], errors='coerce')
qli['Discount_f'] = pd.to_numeric(qli['Discount'], errors='coerce')

# Join to get list prices
m = qli.merge(pbe[['PricebookEntryId_n','ListUnitPrice_f']], left_on='PricebookEntryId_n', right_on='PricebookEntryId_n', how='left')

# Policy heuristics from knowledge base: look for approval thresholds keywords
ka['text'] = (ka.get('title','').astype(str) + ' ' + ka.get('summary','').astype(str) + ' ' + ka.get('faq_answer__c','').astype(str)).str.lower()

# Determine discount violations: any discount > 10% is often restricted
max_disc = m['Discount_f'].max() if not m.empty else 0
violations = []
if pd.notna(max_disc) and max_disc > 10:
    # find most relevant KA mentioning discount approval/maximum discount
    cand = ka[ka['text'].str.contains('discount') & (ka['text'].str.contains('approval') | ka['text'].str.contains('max') | ka['text'].str.contains('maximum') | ka['text'].str.contains('%'))]
    if len(cand)==0:
        cand = ka[ka['text'].str.contains('discount')]
    if len(cand)>0:
        violations.append(norm_id(cand.iloc[0]['id']))
    else:
        violations.append(None)

# Determine pricing mismatch: if unit price > list price or negative etc
if not m.empty:
    bad_price = m[(m['ListUnitPrice_f'].notna()) & (m['UnitPrice_f'] > m['ListUnitPrice_f']*1.001)]
    if len(bad_price)>0:
        cand = ka[ka['text'].str.contains('price') & (ka['text'].str.contains('list') | ka['text'].str.contains('unit'))]
        if len(cand)>0:
            violations.append(norm_id(cand.iloc[0]['id']))

# Setup fee check: look for any product name containing setup/implementation in quote lines via Product2Id mapping not available; skip.

# Final: if any violation identified with KA id, choose first non-None
ka_id = None
for v in violations:
    if v:
        ka_id = v
        break

result = json.dumps(ka_id)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_vkLpCbPyEphHdNQFwv6IBCXT': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_PdYM4oMNCfDsmG4Pm8oTkRf0': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_eX5CHtKa5Pia77xxA8kOa2J3': 'file_storage/call_eX5CHtKa5Pia77xxA8kOa2J3.json', 'var_call_Nd4nxtZglD49kQj1xtLwXsOt': [{'PricebookEntryId': '01uWt0000027P3lIAE', 'ListUnitPrice': '499.99', 'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'ListUnitPrice': '599.99', 'Product2Id': '#01tWt000006hV58IAE', 'ProductName': 'SecureFlow Suite'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'PricebookEntryId': '#01uWt0000027P8bIAE', 'ListUnitPrice': '349.99', 'Product2Id': '01tWt000006hV6jIAE', 'ProductName': 'EcoPCB Creator   '}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'ListUnitPrice': '529.99', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech'}, {'PricebookEntryId': '01uWt0000027PADIA2', 'ListUnitPrice': '299.99', 'Product2Id': '01tWt000006hPffIAE', 'ProductName': 'DevVision IDE'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hVBZIA2', 'ProductName': 'EduTech Lab'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'ListUnitPrice': '529.99', 'Product2Id': '01tWt000006hVI1IAM', 'ProductName': 'AIOptics Vision'}, {'PricebookEntryId': '01uWt0000027PIJIA2', 'ListUnitPrice': '459.99', 'Product2Id': '01tWt000006hVptIAE', 'ProductName': 'DesignEdge Pro'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hPfgIAE', 'ProductName': 'EcoPower Convert'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'ListUnitPrice': '299.99', 'Product2Id': '01tWt000006hVMrIAM', 'ProductName': 'TrainEDU Suite'}, {'PricebookEntryId': '01uWt0000027PTZIA2', 'ListUnitPrice': '449.99', 'Product2Id': '01tWt000006hV0IIAU', 'ProductName': 'NextGen IDE'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'ListUnitPrice': '459.99', 'Product2Id': '01tWt000006hVUvIAM', 'ProductName': 'OptiEnergy Suite'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'ListUnitPrice': '339.99', 'Product2Id': '01tWt000006hVQ5IAM', 'ProductName': 'CircuitSync Pro'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'ListUnitPrice': '429.99', 'Product2Id': '01tWt000006hVQ6IAM', 'ProductName': 'VeriSim Express  '}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'ListUnitPrice': '529.99', 'Product2Id': '01tWt000006hVTJIA2', 'ProductName': 'IntegrGuard Secure'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'ListUnitPrice': '559.99', 'Product2Id': '01tWt000006hVZlIAM', 'ProductName': 'SecuManage Pro  '}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'ListUnitPrice': '349.99', 'Product2Id': '01tWt000006hVbNIAU', 'ProductName': 'EnergyReduce Pro'}, {'PricebookEntryId': '01uWt0000027PgUIAU', 'ListUnitPrice': '379.99', 'Product2Id': '01tWt000006hVt7IAE', 'ProductName': 'PCB EcoModel  '}, {'PricebookEntryId': '01uWt0000027Pi5IAE', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hVczIAE', 'ProductName': 'CollabDesign Studio'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'ListUnitPrice': '549.99', 'Product2Id': '01tWt000006hVebIAE', 'ProductName': 'CircuitAI Innovator'}, {'PricebookEntryId': '01uWt0000027PlJIAU', 'ListUnitPrice': '499.99', 'Product2Id': '01tWt000006hUsEIAU', 'ProductName': 'SimuCheck Ultra'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'ListUnitPrice': '429.99', 'Product2Id': '01tWt000006hVjRIAU', 'ProductName': 'Workflow Genius'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hVmfIAE', 'ProductName': 'EduTech Advance'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'ListUnitPrice': '529.99', 'Product2Id': '01tWt000006hVwLIAU', 'ProductName': 'SimulateX Edge'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'ListUnitPrice': '579.99', 'Product2Id': '01tWt000006hVujIAE', 'ProductName': 'CyberShield Core'}, {'PricebookEntryId': '#01uWt0000027Q33IAE', 'ListUnitPrice': '499.99', 'Product2Id': '01tWt000006hOd8IAE', 'ProductName': 'AutoLayout Master'}, {'PricebookEntryId': '#01uWt0000027Q34IAE', 'ListUnitPrice': '599.99', 'Product2Id': '01tWt000006hUgwIAE', 'ProductName': 'AI DesignShift'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'ListUnitPrice': '299.99', 'Product2Id': '01tWt000006hVjSIAU', 'ProductName': 'InnoTrain Hub'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'ListUnitPrice': '619.99', 'Product2Id': '01tWt000006hUtqIAE', 'ProductName': 'SecureTrack Pro '}]}

exec(code, env_args)
