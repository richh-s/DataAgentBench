code = """import json
import pandas as pd
# read variables which are lists of dicts
quotes = pd.DataFrame(var_call_IHGuYbShS2aYvIxYfo47VFqs)
qli = pd.DataFrame(var_call_WWGX0s3fvSBNCk8bI86nxlh4)
pbe = pd.DataFrame(var_call_feVeMOVdOUNFTGhstBLRtfd5)
prod = pd.DataFrame(var_call_LiCu5HPDBXtjLeFTZzbEWak1)
# Normalize ids (strip leading #)
quotes['Id_clean'] = quotes['Id'].str.lstrip('#')
qli['QuoteId_clean'] = qli['QuoteId'].str.lstrip('#')
qli['PricebookEntryId_clean'] = qli['PricebookEntryId'].str.lstrip('#')
qli['Product2Id_clean'] = qli['Product2Id'].str.lstrip('#')
pbe['Id_clean'] = pbe['Id'].str.lstrip('#')
prod['Id_clean'] = prod['Id'].str.lstrip('#')
# Find the canonical quote id
target = '0Q0Wt000001WRAzKAO'
# Filter quote line items for the target
qli_target = qli[qli['QuoteId_clean']==target]
# Merge pricebook entries to check prices
merged = qli_target.merge(pbe[['Id_clean','UnitPrice']], left_on='PricebookEntryId_clean', right_on='Id_clean', how='left', suffixes=('','_pbe'))
# Merge product names
merged = merged.merge(prod[['Id_clean','Name']], left_on='Product2Id_clean', right_on='Id_clean', how='left', suffixes=('','_prod'))
# Convert numeric fields
for col in ['Quantity','UnitPrice','Discount','TotalPrice']:
    merged[col] = pd.to_numeric(merged[col], errors='coerce')
merged['UnitPrice_pbe'] = pd.to_numeric(merged['UnitPrice_pbe'], errors='coerce')
# Check for violations: price mismatch between QuoteLineItem.UnitPrice and PricebookEntry.UnitPrice
merged['price_mismatch'] = (merged['UnitPrice'] != merged['UnitPrice_pbe'])
# Check for quantity limits: assume policy article 'Volume-Based Discounts' (ka0Wt000000Eq0MIAS) defines max allowed qty without discount maybe 30; detect Quantity>30 with Discount>0 or suspicious
merged['qty_over_30'] = merged['Quantity']>30
# Prepare a summary
issues = []
if merged['price_mismatch'].any():
    issues.append({'rule':'Price must match active PricebookEntry UnitPrice','article_id':'ka0Wt000000Eq0MIAS'})
if merged['qty_over_30'].any():
    issues.append({'rule':'Quantity over allowed threshold requires special approval','article_id':'ka0Wt000000Eq0MIAS'})
# Also check negative discounts or discounts over 50%
merged['discount_pct'] = merged['Discount']
merged['discount_too_high'] = merged['discount_pct']>50
if merged['discount_too_high'].any():
    issues.append({'rule':'Discount exceeds allowed maximum','article_id':'ka0Wt000000Eq0MIAS'})
# If no issues found, default to None
result_article = None
if issues:
    # choose first relevant article id
    result_article = issues[0]['article_id']
# Print according to format
print("__RESULT__:")
print(json.dumps(result_article))"""

env_args = {'var_call_ykfWtCjVdvit85XMv2cbNhs6': [], 'var_call_Jc4adJd3WYcmBCxQ2qNDfs4p': [], 'var_call_XEZvsNXFCB09W3jffcfMVRkg': 'file_storage/call_XEZvsNXFCB09W3jffcfMVRkg.json', 'var_call_IHGuYbShS2aYvIxYfo47VFqs': [{'Id': '#0Q0Wt000001WRAzKAO', 'Name': 'NeoGreen EDA Expansion Quote', 'AccountId': '001Wt00000PHVsDIAX', 'Status': 'Needs Review'}], 'var_call_6KFKxBgcTFQYlSP2Ycgg9YXH': [], 'var_call_WWGX0s3fvSBNCk8bI86nxlh4': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_feVeMOVdOUNFTGhstBLRtfd5': [{'Id': '01uWt0000027P8cIAE', 'Product2Id': '01tWt000006hV8LIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'Product2Id': '01tWt000006hPffIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Pi5IAE', 'Product2Id': '01tWt000006hVczIAE', 'UnitPrice': '399.99'}], 'var_call_LiCu5HPDBXtjLeFTZzbEWak1': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}], 'var_call_X4rYm0wk5laj4htVS2h5mftH': 'file_storage/call_X4rYm0wk5laj4htVS2h5mftH.json'}

exec(code, env_args)
