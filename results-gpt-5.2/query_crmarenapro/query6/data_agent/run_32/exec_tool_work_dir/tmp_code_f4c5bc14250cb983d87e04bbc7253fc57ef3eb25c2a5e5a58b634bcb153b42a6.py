code = """import json, pandas as pd

qlis = pd.DataFrame(var_call_oGtSKHebx5RnAUc6FeNMXPye)
pbe = pd.DataFrame(var_call_98czYflzn2BH3HdiU4RI2ZRT)

# normalize ids
for col in ['PricebookEntryId','Product2Id']:
    if col in qlis.columns:
        qlis[col+'_norm'] = qlis[col].astype(str).str.replace('#','', regex=False).str.strip()
for col in ['PricebookEntryId','Product2Id']:
    pbe[col+'_norm'] = pbe[col].astype(str).str.replace('#','', regex=False).str.strip()

# numeric
for c in ['Quantity','UnitPrice','Discount','TotalPrice']:
    qlis[c] = pd.to_numeric(qlis[c], errors='coerce')

pbe['CatalogUnitPrice'] = pd.to_numeric(pbe['CatalogUnitPrice'], errors='coerce')

m = qlis.merge(pbe, left_on='PricebookEntryId_norm', right_on='PricebookEntryId_norm', how='left', suffixes=('','_pbe'))

# Determine volume discount rule: based on purchase total amount (TotalPrice before discount?) Here Discount field seems percent.
# We'll flag any line where Discount > 0 AND Discount not in {5,10,15} OR where Discount>0 but Quantity*UnitPrice doesn't meet thresholds (>=5/10/20).
allowed_discounts = {5,10,15}
# assume discount tiers based on line subtotal before discount
m['LineSubtotal'] = m['Quantity'] * m['UnitPrice']

def violates(row):
    d = row['Discount']
    if pd.isna(d) or d==0:
        return False
    if d not in allowed_discounts:
        return True
    if d==5 and row['LineSubtotal'] < 5:
        return True
    if d==10 and row['LineSubtotal'] < 10:
        return True
    if d==15 and row['LineSubtotal'] < 20:
        return True
    return False

m['violates_volume_discount'] = m.apply(violates, axis=1)

# Also flag unit price not equal to catalog unit price when no discount (possible regulation)
# but we don't have article; focus on volume discount since we have KA.

viol = m[m['violates_volume_discount']]

ka_path = var_call_cBIpd3wJwu5gZwqWccn6CIR4
if isinstance(ka_path, str) and ka_path.endswith('.json'):
    with open(ka_path,'r',encoding='utf-8') as f:
        kas = json.load(f)
else:
    kas = var_call_cBIpd3wJwu5gZwqWccn6CIR4

# find the KA for Volume-Based Discounts
ka_id = None
for r in kas:
    if isinstance(r.get('title',''), str) and 'volume-based discounts' in r.get('title','').lower():
        ka_id = r['id']
        break

# If no violation found, return null
result = {'knowledge_article_id': ka_id if (ka_id and len(viol)>0) else None, 'violations_found': int(len(viol))}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_oGtSKHebx5RnAUc6FeNMXPye': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_XZzyiz0SN8A00BKepSqWXmz5': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_call_98czYflzn2BH3HdiU4RI2ZRT': [{'PricebookEntryId': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'CatalogUnitPrice': '499.99', 'PricebookName': 'None'}, {'PricebookEntryId': '01uWt0000027P3mIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVhpIAE', 'CatalogUnitPrice': '489.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027P5NIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hV58IAE', 'CatalogUnitPrice': '599.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hTUkIAM', 'CatalogUnitPrice': '399.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027P8bIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV6jIAE', 'CatalogUnitPrice': '349.99', 'PricebookName': 'None'}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'CatalogUnitPrice': '529.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PADIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'CatalogUnitPrice': '299.99', 'PricebookName': 'None'}, {'PricebookEntryId': '01uWt0000027PBpIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV9xIAE', 'CatalogUnitPrice': '449.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVBZIA2', 'CatalogUnitPrice': '399.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PF3IAM', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVDBIA2', 'CatalogUnitPrice': '549.99', 'PricebookName': 'None'}, {'PricebookEntryId': '#01uWt0000027PGfIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVEnIAM', 'CatalogUnitPrice': '479.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PIHIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVGPIA2', 'CatalogUnitPrice': '599.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVI1IAM', 'CatalogUnitPrice': '529.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PIJIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVptIAE', 'CatalogUnitPrice': '459.99', 'PricebookName': 'None'}, {'PricebookEntryId': '01uWt0000027PJtIAM', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVJdIAM', 'CatalogUnitPrice': '649.99', 'PricebookName': 'None'}, {'PricebookEntryId': '01uWt0000027PLVIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVLFIA2', 'CatalogUnitPrice': '459.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPfgIAE', 'CatalogUnitPrice': '399.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVMrIAM', 'CatalogUnitPrice': '299.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027POkIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hRfqIAE', 'CatalogUnitPrice': '349.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PQLIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hUKMIA2', 'CatalogUnitPrice': '489.99', 'PricebookName': 'None'}, {'PricebookEntryId': '#01uWt0000027PRxIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVOTIA2', 'CatalogUnitPrice': '559.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PTZIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV0IIAU', 'CatalogUnitPrice': '449.99', 'PricebookName': 'None'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVUvIAM', 'CatalogUnitPrice': '459.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'CatalogUnitPrice': '339.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ6IAM', 'CatalogUnitPrice': '429.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PYPIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVRhIAM', 'CatalogUnitPrice': '319.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVTJIA2', 'CatalogUnitPrice': '529.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PbdIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVWXIA2', 'CatalogUnitPrice': '389.99', 'PricebookName': 'None'}, {'PricebookEntryId': '01uWt0000027PdFIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVY9IAM', 'CatalogUnitPrice': '299.99', 'PricebookName': 'None'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVZlIAM', 'CatalogUnitPrice': '559.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVbNIAU', 'CatalogUnitPrice': '349.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PgUIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVt7IAE', 'CatalogUnitPrice': '379.99', 'PricebookName': 'None'}, {'PricebookEntryId': '01uWt0000027Pi5IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'CatalogUnitPrice': '399.99', 'PricebookName': 'None'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVebIAE', 'CatalogUnitPrice': '549.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PlJIAU', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUsEIAU', 'CatalogUnitPrice': '499.99', 'PricebookName': 'None'}, {'PricebookEntryId': '#01uWt0000027PmvIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVJeIAM', 'CatalogUnitPrice': '599.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PoXIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '#01tWt000006hVgDIAU', 'CatalogUnitPrice': '459.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjRIAU', 'CatalogUnitPrice': '429.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PrlIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVl3IAE', 'CatalogUnitPrice': '369.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVmfIAE', 'CatalogUnitPrice': '399.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVwLIAU', 'CatalogUnitPrice': '529.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PuzIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVoHIAU', 'CatalogUnitPrice': '629.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027PwbIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUUwIAM', 'CatalogUnitPrice': '559.99', 'PricebookName': 'None'}, {'PricebookEntryId': '#01uWt0000027PyDIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVrVIAU', 'CatalogUnitPrice': '649.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027PzpIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVrWIAU', 'CatalogUnitPrice': '429.99', 'PricebookName': 'None'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVujIAE', 'CatalogUnitPrice': '579.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '#01uWt0000027Q33IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hOd8IAE', 'CatalogUnitPrice': '499.99', 'PricebookName': 'None'}, {'PricebookEntryId': '#01uWt0000027Q34IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUgwIAE', 'CatalogUnitPrice': '599.99', 'PricebookName': 'None'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVjSIAU', 'CatalogUnitPrice': '299.99', 'PricebookName': 'Standard Price Book'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hUtqIAE', 'CatalogUnitPrice': '619.99', 'PricebookName': 'Standard Price Book'}], 'var_call_ZC6tEuGz84Rxyza4xLc53Zv0': 'file_storage/call_ZC6tEuGz84Rxyza4xLc53Zv0.json', 'var_call_cBIpd3wJwu5gZwqWccn6CIR4': 'file_storage/call_cBIpd3wJwu5gZwqWccn6CIR4.json'}

exec(code, env_args)
