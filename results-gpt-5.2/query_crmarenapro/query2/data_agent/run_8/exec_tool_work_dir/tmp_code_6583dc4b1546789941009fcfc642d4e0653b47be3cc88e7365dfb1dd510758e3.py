code = """import json, pandas as pd, pathlib

quote = var_call_DIoFWRe8GhAgwuMGLoFZyMqx[0]
qlis = var_call_HrOK70Q1xxYQAyyKiW2JoxBe

ka_src = var_call_K2bN9aObZHDAgEopXUjyB5bt
if isinstance(ka_src, str):
    ka = json.loads(pathlib.Path(ka_src).read_text())
else:
    ka = ka_src

pbe = pd.DataFrame(var_call_2sDaV2GlFtr83T5hcYBkaAjT)

def norm(x):
    if x is None:
        return None
    return str(x).replace('#','').strip()

pbe['Id_n'] = pbe['Id'].map(norm)
pbe['UnitPrice'] = pbe['UnitPrice'].astype(float)

violations = []
for li in qlis:
    disc = float(li['Discount']) if li.get('Discount') is not None else 0.0
    if disc < 0 or disc > 20:
        violations.append(('discount', disc, norm(li.get('Id'))))
    pbeid = norm(li.get('PricebookEntryId'))
    up = float(li['UnitPrice'])
    row = pbe[pbe['Id_n'] == pbeid]
    if len(row) == 1:
        listp = float(row.iloc[0]['UnitPrice'])
        if abs(up - listp) > 1e-6:
            violations.append(('unitprice_mismatch', (up, listp), norm(li.get('Id'))))

violated_id = None
if violations:
    # Heuristic search for a relevant policy knowledge article.
    for r in ka:
        blob = (str(r.get('title','')) + ' ' + str(r.get('summary','')) + ' ' + str(r.get('faq_answer__c',''))).lower()
        if ('discount' in blob and ('max' in blob or 'maximum' in blob or 'approval' in blob or 'percent' in blob or '%' in blob)) or ('pricebook' in blob and 'unit price' in blob):
            violated_id = norm(r.get('id'))
            break

result = violated_id if violated_id is not None else None
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_DIoFWRe8GhAgwuMGLoFZyMqx': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_HrOK70Q1xxYQAyyKiW2JoxBe': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_K2bN9aObZHDAgEopXUjyB5bt': 'file_storage/call_K2bN9aObZHDAgEopXUjyB5bt.json', 'var_call_2sDaV2GlFtr83T5hcYBkaAjT': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027P3mIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVhpIAE', 'UnitPrice': '489.99'}, {'Id': '01uWt0000027P5NIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hV58IAE', 'UnitPrice': '599.99'}, {'Id': '#01uWt0000027P6zIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hTUkIAM', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027P8bIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV6jIAE', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027PBpIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV9xIAE', 'UnitPrice': '449.99'}, {'Id': '01uWt0000027PDRIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVBZIA2', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PF3IAM', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVDBIA2', 'UnitPrice': '549.99'}, {'Id': '#01uWt0000027PGfIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVEnIAM', 'UnitPrice': '479.99'}, {'Id': '01uWt0000027PIHIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVGPIA2', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PIIIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVI1IAM', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PIJIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVptIAE', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PJtIAM', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVJdIAM', 'UnitPrice': '649.99'}, {'Id': '01uWt0000027PLVIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVLFIA2', 'UnitPrice': '459.99'}, {'Id': '#01uWt0000027PN7IAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPfgIAE', 'UnitPrice': '399.99'}, {'Id': '#01uWt0000027POjIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVMrIAM', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027POkIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hRfqIAE', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027PQLIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hUKMIA2', 'UnitPrice': '489.99'}, {'Id': '#01uWt0000027PRxIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVOTIA2', 'UnitPrice': '559.99'}, {'Id': '01uWt0000027PTZIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV0IIAU', 'UnitPrice': '449.99'}, {'Id': '#01uWt0000027PTaIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVUvIAM', 'UnitPrice': '459.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}, {'Id': '#01uWt0000027PWnIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ6IAM', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027PYPIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVRhIAM', 'UnitPrice': '319.99'}, {'Id': '01uWt0000027Pa1IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVTJIA2', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PbdIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVWXIA2', 'UnitPrice': '389.99'}, {'Id': '01uWt0000027PdFIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVY9IAM', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027PerIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVZlIAM', 'UnitPrice': '559.99'}, {'Id': '01uWt0000027PgTIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVbNIAU', 'UnitPrice': '349.99'}, {'Id': '01uWt0000027PgUIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVt7IAE', 'UnitPrice': '379.99'}, {'Id': '01uWt0000027Pi5IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PjhIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVebIAE', 'UnitPrice': '549.99'}, {'Id': '01uWt0000027PlJIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUsEIAU', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027PmvIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVJeIAM', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027PoXIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVgDIAU', 'UnitPrice': '459.99'}, {'Id': '#01uWt0000027Pq9IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjRIAU', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027PrlIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVl3IAE', 'UnitPrice': '369.99'}, {'Id': '#01uWt0000027PtNIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVmfIAE', 'UnitPrice': '399.99'}, {'Id': '01uWt0000027PtOIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVwLIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PuzIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVoHIAU', 'UnitPrice': '629.99'}, {'Id': '01uWt0000027PwbIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUUwIAM', 'UnitPrice': '559.99'}, {'Id': '#01uWt0000027PyDIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVrVIAU', 'UnitPrice': '649.99'}, {'Id': '#01uWt0000027PzpIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVrWIAU', 'UnitPrice': '429.99'}, {'Id': '01uWt0000027Q1RIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVujIAE', 'UnitPrice': '579.99'}, {'Id': '#01uWt0000027Q33IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hOd8IAE', 'UnitPrice': '499.99'}, {'Id': '#01uWt0000027Q34IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUgwIAE', 'UnitPrice': '599.99'}, {'Id': '01uWt0000027Q4fIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjSIAU', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Q6HIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUtqIAE', 'UnitPrice': '619.99'}], 'var_call_kKqpZXRTUi37sE5qrhIrsgXR': 'file_storage/call_kKqpZXRTUi37sE5qrhIrsgXR.json'}

exec(code, env_args)
