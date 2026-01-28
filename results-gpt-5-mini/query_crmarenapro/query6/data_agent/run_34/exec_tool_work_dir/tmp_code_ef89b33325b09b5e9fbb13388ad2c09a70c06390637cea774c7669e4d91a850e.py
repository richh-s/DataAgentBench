code = """import json
# Load previous tool results from storage variables
# var_call_bISDgmdoR491RFKb3moXuCKm is a filepath to the full knowledge articles JSON
kb_path = var_call_bISDgmdoR491RFKb3moXuCKm
with open(kb_path, 'r') as f:
    kb = json.load(f)
# Quote Line Items and Quote
qli = var_call_HqsfgO1d4uDswh7njswmSKep
quote = var_call_fHdLtBLH91kWvAE7VmaPVmfR

# Find articles that mention 'discount' or 'volume'
matches = []
for a in kb:
    title = (a.get('title') or '').lower()
    summary = (a.get('summary') or '').lower()
    if 'discount' in title or 'discount' in summary or 'volume' in title or 'volume' in summary:
        matches.append(a)

# Prefer title containing both 'volume' and 'discount', else title containing 'volume' else 'discount'
chosen = None
for a in matches:
    t = (a.get('title') or '').lower()
    if 'volume' in t and 'discount' in t:
        chosen = a
        break
if not chosen:
    for a in matches:
        t = (a.get('title') or '').lower()
        if 'volume' in t:
            chosen = a
            break
if not chosen:
    for a in matches:
        t = (a.get('title') or '').lower()
        if 'discount' in t:
            chosen = a
            break

# Fallback: if no match, choose first match
if not chosen and matches:
    chosen = matches[0]

# Prepare result id or empty
result_id = chosen.get('id') if chosen else None

print("__RESULT__:")
print(json.dumps(result_id))"""

env_args = {'var_call_vwIiy9N46UmYAMD3agD7355S': [], 'var_call_fHdLtBLH91kWvAE7VmaPVmfR': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review'}], 'var_call_HqsfgO1d4uDswh7njswmSKep': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_bISDgmdoR491RFKb3moXuCKm': 'file_storage/call_bISDgmdoR491RFKb3moXuCKm.json'}

exec(code, env_args)
