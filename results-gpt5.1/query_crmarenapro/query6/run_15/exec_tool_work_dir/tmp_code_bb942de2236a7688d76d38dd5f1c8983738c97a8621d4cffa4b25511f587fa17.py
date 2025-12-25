code = """import json
import pandas as pd

qli = pd.DataFrame(var_call_UARSo6TTbjFCy195wUL8HkW2)

# Business rule guess: large quantity with discount might trigger volume/installation policy
max_qty = qli['Quantity'].astype(float).max()
max_disc = qli['Discount'].astype(float).max()

# Load full knowledge articles
with open(var_call_F71i9DmrYXj3OjOCCvv3hK7J, 'r') as f:
    kav = pd.DataFrame(json.load(f))

# Look for policies about volume, discount, or pricing
candidates = kav[kav['title'].str.contains('Volume', case=False, na=False) |
                 kav['summary'].str.contains('Volume', case=False, na=False) |
                 kav['title'].str.contains('Discount', case=False, na=False) |
                 kav['summary'].str.contains('Discount', case=False, na=False)]

# Also look for installation timeline policy which might tie to quantity
candidates2 = kav[kav['title'].str.contains('Installation Timeline', case=False, na=False) |
                  kav['summary'].str.contains('Installation Timeline', case=False, na=False)]

cands = pd.concat([candidates, candidates2]).drop_duplicates(subset=['id'])

result_id = None
# If very high quantity and discount, assume volume-based policy violation
if max_qty >= 30 and max_disc > 0 and not cands.empty:
    # Prefer installation timeline specific policy if present
    inst = cands[cands['title'].str.contains('Installation Timeline', case=False, na=False)]
    if not inst.empty:
        result_id = inst.iloc[0]['id']
    else:
        # Otherwise volume-based discounts
        vol = cands[cands['title'].str.contains('Volume-Based Discounts', case=False, na=False)]
        if not vol.empty:
            result_id = vol.iloc[0]['id']
        else:
            result_id = cands.iloc[0]['id']

if result_id is None and not cands.empty:
    result_id = cands.iloc[0]['id']

result = json.dumps(result_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_UARSo6TTbjFCy195wUL8HkW2': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_F71i9DmrYXj3OjOCCvv3hK7J': 'file_storage/call_F71i9DmrYXj3OjOCCvv3hK7J.json', 'var_call_AEuV65qSRxk9iotOKMToi8uv': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_call_DIho4XUxkke62zn4itK4Whnn': 'file_storage/call_DIho4XUxkke62zn4itK4Whnn.json'}

exec(code, env_args)
