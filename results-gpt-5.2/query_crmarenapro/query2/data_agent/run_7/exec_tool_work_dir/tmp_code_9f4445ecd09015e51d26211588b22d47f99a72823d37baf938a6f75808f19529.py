code = """import json, pandas as pd

def norm(x):
    if x is None:
        return None
    return str(x).replace('#','').strip()

quote = pd.DataFrame(var_call_e5te0nWLIZ7Fhe3DUrCkLHIz)
qli = pd.DataFrame(var_call_tJwbg3jHETaxtBCJfC5sNxoe)

# load knowledge
kp = var_call_bKwpqQ9tzcOvU4zsQPYT1gDv
if isinstance(kp, str) and kp.endswith('.json'):
    with open(kp,'r',encoding='utf-8') as f:
        knowledge = json.load(f)
else:
    knowledge = kp
kdf = pd.DataFrame(knowledge)

# Evaluate pricing vs list pricebook entry
pbe = pd.DataFrame(var_call_PxtQvGg3ZX1Ab4VSlUjdLidB)
if not qli.empty:
    qli['PricebookEntryId_n'] = qli['PricebookEntryId'].map(norm)
    pbe['PricebookEntryId_n'] = pbe['PricebookEntryId'].map(norm)
    merged = qli.merge(pbe[['PricebookEntryId_n','ListUnitPrice']], on='PricebookEntryId_n', how='left')
    merged['UnitPrice_f'] = merged['UnitPrice'].astype(float)
    merged['Discount_f'] = merged['Discount'].astype(float)
    merged['ListUnitPrice_f'] = merged['ListUnitPrice'].astype(float)
    merged['expected_unit_after_discount'] = merged['ListUnitPrice_f'] * (1- merged['Discount_f']/100.0)
    merged['unit_matches'] = (merged['UnitPrice_f'] - merged['expected_unit_after_discount']).abs() < 1e-6

# find any policy article about max discount thresholds and setup fees etc.
# Heuristic: if any QLI discount > 10% then likely violation.
violation = None
if not qli.empty:
    max_disc = qli['Discount'].astype(float).max()
    if max_disc > 10:
        # find knowledge article mentioning discount limit 10 or approval required
        # search titles/summary/faq for keywords
        text_cols = ['title','summary','faq_answer__c','urlname']
        def row_text(r):
            return ' '.join([str(r.get(c,'') or '') for c in text_cols]).lower()
        kdf['_text'] = kdf.apply(row_text, axis=1)
        cand = kdf[kdf['_text'].str.contains('discount') & (kdf['_text'].str.contains('10%') | kdf['_text'].str.contains('10 percent') | kdf['_text'].str.contains('10\%'))]
        if cand.empty:
            cand = kdf[kdf['_text'].str.contains('discount') & kdf['_text'].str.contains('approval')]
        if not cand.empty:
            violation = cand.iloc[0]['id']

result = violation if violation is not None else None
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_e5te0nWLIZ7Fhe3DUrCkLHIz': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_tJwbg3jHETaxtBCJfC5sNxoe': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_bKwpqQ9tzcOvU4zsQPYT1gDv': 'file_storage/call_bKwpqQ9tzcOvU4zsQPYT1gDv.json', 'var_call_PxtQvGg3ZX1Ab4VSlUjdLidB': [{'PricebookEntryId': '01uWt0000027P3lIAE', 'Product2Id': '01tWt000006hV57IAE', 'ListUnitPrice': '499.99', 'ProductName': 'PulseSim Pro'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'Product2Id': '#01tWt000006hV58IAE', 'ListUnitPrice': '599.99', 'ProductName': 'SecureFlow Suite'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'Product2Id': '01tWt000006hTUkIAM', 'ListUnitPrice': '399.99', 'ProductName': 'CloudLink Designer'}, {'PricebookEntryId': '#01uWt0000027P8bIAE', 'Product2Id': '01tWt000006hV6jIAE', 'ListUnitPrice': '349.99', 'ProductName': 'EcoPCB Creator   '}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'Product2Id': '01tWt000006hV8LIAU', 'ListUnitPrice': '529.99', 'ProductName': 'AI Cirku-Tech'}, {'PricebookEntryId': '01uWt0000027PADIA2', 'Product2Id': '01tWt000006hPffIAE', 'ListUnitPrice': '299.99', 'ProductName': 'DevVision IDE'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'Product2Id': '01tWt000006hVBZIA2', 'ListUnitPrice': '399.99', 'ProductName': 'EduTech Lab'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'Product2Id': '01tWt000006hVI1IAM', 'ListUnitPrice': '529.99', 'ProductName': 'AIOptics Vision'}, {'PricebookEntryId': '01uWt0000027PIJIA2', 'Product2Id': '01tWt000006hVptIAE', 'ListUnitPrice': '459.99', 'ProductName': 'DesignEdge Pro'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'Product2Id': '01tWt000006hPfgIAE', 'ListUnitPrice': '399.99', 'ProductName': 'EcoPower Convert'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'Product2Id': '01tWt000006hVMrIAM', 'ListUnitPrice': '299.99', 'ProductName': 'TrainEDU Suite'}, {'PricebookEntryId': '01uWt0000027PTZIA2', 'Product2Id': '01tWt000006hV0IIAU', 'ListUnitPrice': '449.99', 'ProductName': 'NextGen IDE'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'Product2Id': '01tWt000006hVUvIAM', 'ListUnitPrice': '459.99', 'ProductName': 'OptiEnergy Suite'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'Product2Id': '01tWt000006hVQ5IAM', 'ListUnitPrice': '339.99', 'ProductName': 'CircuitSync Pro'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'Product2Id': '01tWt000006hVQ6IAM', 'ListUnitPrice': '429.99', 'ProductName': 'VeriSim Express  '}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'Product2Id': '01tWt000006hVTJIA2', 'ListUnitPrice': '529.99', 'ProductName': 'IntegrGuard Secure'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'Product2Id': '01tWt000006hVZlIAM', 'ListUnitPrice': '559.99', 'ProductName': 'SecuManage Pro  '}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'Product2Id': '01tWt000006hVbNIAU', 'ListUnitPrice': '349.99', 'ProductName': 'EnergyReduce Pro'}, {'PricebookEntryId': '01uWt0000027PgUIAU', 'Product2Id': '01tWt000006hVt7IAE', 'ListUnitPrice': '379.99', 'ProductName': 'PCB EcoModel  '}, {'PricebookEntryId': '01uWt0000027Pi5IAE', 'Product2Id': '01tWt000006hVczIAE', 'ListUnitPrice': '399.99', 'ProductName': 'CollabDesign Studio'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'Product2Id': '01tWt000006hVebIAE', 'ListUnitPrice': '549.99', 'ProductName': 'CircuitAI Innovator'}, {'PricebookEntryId': '01uWt0000027PlJIAU', 'Product2Id': '01tWt000006hUsEIAU', 'ListUnitPrice': '499.99', 'ProductName': 'SimuCheck Ultra'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'Product2Id': '01tWt000006hVjRIAU', 'ListUnitPrice': '429.99', 'ProductName': 'Workflow Genius'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'Product2Id': '01tWt000006hVmfIAE', 'ListUnitPrice': '399.99', 'ProductName': 'EduTech Advance'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'Product2Id': '01tWt000006hVwLIAU', 'ListUnitPrice': '529.99', 'ProductName': 'SimulateX Edge'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'Product2Id': '01tWt000006hVujIAE', 'ListUnitPrice': '579.99', 'ProductName': 'CyberShield Core'}, {'PricebookEntryId': '#01uWt0000027Q33IAE', 'Product2Id': '01tWt000006hOd8IAE', 'ListUnitPrice': '499.99', 'ProductName': 'AutoLayout Master'}, {'PricebookEntryId': '#01uWt0000027Q34IAE', 'Product2Id': '01tWt000006hUgwIAE', 'ListUnitPrice': '599.99', 'ProductName': 'AI DesignShift'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'Product2Id': '01tWt000006hVjSIAU', 'ListUnitPrice': '299.99', 'ProductName': 'InnoTrain Hub'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'Product2Id': '01tWt000006hUtqIAE', 'ListUnitPrice': '619.99', 'ProductName': 'SecureTrack Pro '}], 'var_call_MJtZ3HejFBFaJGAjFN0BhfJR': 'file_storage/call_MJtZ3HejFBFaJGAjFN0BhfJR.json', 'var_call_zTzVZbhog29B8y2bz0TCRxuF': 'file_storage/call_zTzVZbhog29B8y2bz0TCRxuF.json', 'var_call_nrU2wB8JToMrmqXG4n2ijfsb': [{'Id': '01sWt000000imiTIAQ', 'Name': 'Standard Price Book', 'Description': 'None', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}, {'Id': '01sWt000000iu1hIAA', 'Name': 'Standard Pricebook', 'Description': 'The standard pricebook.', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}], 'var_call_sTyQ6KZjolm3Ihr6wM9j7UJ4': 'file_storage/call_sTyQ6KZjolm3Ihr6wM9j7UJ4.json'}

exec(code, env_args)
