code = """import json, pandas as pd

ql = pd.DataFrame(var_call_8nTqno0BwqFwFvIOjq2vYXE2)
pbe = pd.DataFrame(var_call_JZPPaxGNa8OBw0DbOg6HkjZu)

# normalize ids by stripping leading '#'
for c in ['Product2Id','PricebookEntryId','QuoteId','Id']:
    if c in ql.columns:
        ql[c] = ql[c].astype(str).str.replace('#','', regex=False).str.strip()
for c in ['Product2Id','PricebookEntryId']:
    if c in pbe.columns:
        pbe[c] = pbe[c].astype(str).str.replace('#','', regex=False).str.strip()

# cast numeric
for c in ['Quantity','UnitPrice','Discount','TotalPrice']:
    ql[c] = pd.to_numeric(ql[c], errors='coerce')

pbe['CatalogUnitPrice'] = pd.to_numeric(pbe['CatalogUnitPrice'], errors='coerce')

m = ql.merge(pbe[['PricebookEntryId','Product2Id','CatalogUnitPrice']], on='PricebookEntryId', how='left', suffixes=('','_cat'))

# invalid if PBE missing or product mismatch or unit price differs from catalog when discount=0
m['invalid'] = False
m.loc[m['CatalogUnitPrice'].isna(), 'invalid'] = True
m.loc[(~m['CatalogUnitPrice'].isna()) & (m['Product2Id'] != m['Product2Id_cat']), 'invalid'] = True
m.loc[(~m['CatalogUnitPrice'].isna()) & (m['Discount'].fillna(0)==0) & (abs(m['UnitPrice']-m['CatalogUnitPrice'])>1e-6), 'invalid'] = True

invalid_rows = m[m['invalid']]

# load knowledge articles (may be in file)
ka = var_call_ar8uLeHP34lSoNfg909eZeHD
if isinstance(ka, str):
    with open(ka, 'r', encoding='utf-8') as f:
        ka = json.load(f)
ka_df = pd.DataFrame(ka)
ka_df['title_l'] = ka_df['title'].astype(str).str.lower()
ka_df['summary_l'] = ka_df['summary'].astype(str).str.lower()
ka_df['faq_l'] = ka_df['faq_answer__c'].astype(str).str.lower()

# heuristically find pricing/discount policy article
keywords = ['discount','unit price','pricebook','pricing','quote line','minimum','max','approval','needs review']
pat = '|'.join([k.replace(' ','\\s+') for k in keywords])
score = (
    ka_df['title_l'].str.contains('discount|pricing|pricebook|quote', regex=True).astype(int)*3 +
    ka_df['summary_l'].str.contains(pat, regex=True).astype(int) +
    ka_df['faq_l'].str.contains(pat, regex=True).astype(int)
)
ka_df['score'] = score
ka_df = ka_df.sort_values(['score','id'], ascending=[False, True])

article_id = None
if len(invalid_rows)>0:
    # pick top scoring article if any score>0 else None
    top = ka_df.iloc[0]
    if int(top['score'])>0:
        article_id = str(top['id']).replace('#','').strip()

print('__RESULT__:')
print(json.dumps({'article_id': article_id}))"""

env_args = {'var_call_8nTqno0BwqFwFvIOjq2vYXE2': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_ar8uLeHP34lSoNfg909eZeHD': 'file_storage/call_ar8uLeHP34lSoNfg909eZeHD.json', 'var_call_JZPPaxGNa8OBw0DbOg6HkjZu': [{'PricebookEntryId': '01uWt0000027P5NIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hV58IAE', 'CatalogUnitPrice': '599.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'SecureFlow Suite', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hTUkIAM', 'CatalogUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'CloudLink Designer', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'CatalogUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'AI Cirku-Tech', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVBZIA2', 'CatalogUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'EduTech Lab', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVI1IAM', 'CatalogUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'AIOptics Vision', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPfgIAE', 'CatalogUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'EcoPower Convert', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVMrIAM', 'CatalogUnitPrice': '299.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'TrainEDU Suite', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVUvIAM', 'CatalogUnitPrice': '459.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'OptiEnergy Suite', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'CatalogUnitPrice': '339.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'CircuitSync Pro', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ6IAM', 'CatalogUnitPrice': '429.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'VeriSim Express  ', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVTJIA2', 'CatalogUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'IntegrGuard Secure', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVZlIAM', 'CatalogUnitPrice': '559.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'SecuManage Pro  ', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVbNIAU', 'CatalogUnitPrice': '349.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'EnergyReduce Pro', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVebIAE', 'CatalogUnitPrice': '549.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'CircuitAI Innovator', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjRIAU', 'CatalogUnitPrice': '429.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'Workflow Genius', 'ProductIsActive': '1'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVmfIAE', 'CatalogUnitPrice': '399.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'EduTech Advance', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVwLIAU', 'CatalogUnitPrice': '529.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'SimulateX Edge', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVujIAE', 'CatalogUnitPrice': '579.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'CyberShield Core', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjSIAU', 'CatalogUnitPrice': '299.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'InnoTrain Hub', 'ProductIsActive': '1'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUtqIAE', 'CatalogUnitPrice': '619.99', 'PricebookName': 'Standard Price Book', 'PricebookIsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None', 'ProductName': 'SecureTrack Pro ', 'ProductIsActive': '1'}], 'var_call_W6Q8GRa9iGsae1xA4LCoZNpf': [{'Id': '#0Q0Wt000001WRAzKAO', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.'}]}

exec(code, env_args)
