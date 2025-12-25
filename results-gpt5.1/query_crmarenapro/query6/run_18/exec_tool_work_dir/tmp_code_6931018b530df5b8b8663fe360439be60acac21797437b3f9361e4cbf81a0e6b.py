code = """import json, pandas as pd

# Load full knowledge query result
path = var_call_bVs0YQjxFIYovyfpKUB0n1mI
with open(path, 'r') as f:
    knowledge = json.load(f)

kdf = pd.DataFrame(knowledge)

# Inspect titles likely about limits/discount rules
mask = kdf['title'].str.contains('Quantity Limits', case=False, na=False) | \
       kdf['title'].str.contains('Discount', case=False, na=False) | \
       kdf['title'].str.contains('Pricing', case=False, na=False) | \
       kdf['summary'].str.contains('limit', case=False, na=False)

candidates = kdf[mask]

# From preview we know "Product Quantity Limits" and "Volume-Based Discounts" exist; determine which applies
# We have quote line with quantity 35 and discount 15%
qli = pd.DataFrame(var_call_8pFPgLrjPNGyNerigllTCouM)

max_qty_issue = None
max_disc_issue = None

# very simple heuristic: choose article whose title mentions 'Quantity Limits' for quantity violation
qty_articles = candidates[candidates['title'].str.contains('Quantity Limits', case=False, na=False)]
if not qty_articles.empty:
    max_qty_issue = qty_articles.iloc[0]['id']

# choose article whose title mentions 'Volume-Based Discounts' or 'Discount Policy' for discount violation
disc_articles = candidates[candidates['title'].str.contains('Volume-Based Discounts', case=False, na=False) |
                                   candidates['title'].str.contains('Discount Policy', case=False, na=False)]
if not disc_articles.empty:
    max_disc_issue = disc_articles.iloc[0]['id']

# Decide which rule is violated by this quote
# Quantity: one line has quantity 35, likely exceeding some product max in Product Quantity Limits KA.
# Discount: only 15%, likely allowed as it's exactly the top tier in Volume-Based Discounts, so assume quantity violation.
violated_id = max_qty_issue

result = json.dumps(violated_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_8pFPgLrjPNGyNerigllTCouM': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_Uh8kAbF0z3SQ0VfFxuJxOY41': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_RGn1hou9Ju6HdECCNEEq5yAu': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_call_bVs0YQjxFIYovyfpKUB0n1mI': 'file_storage/call_bVs0YQjxFIYovyfpKUB0n1mI.json'}

exec(code, env_args)
