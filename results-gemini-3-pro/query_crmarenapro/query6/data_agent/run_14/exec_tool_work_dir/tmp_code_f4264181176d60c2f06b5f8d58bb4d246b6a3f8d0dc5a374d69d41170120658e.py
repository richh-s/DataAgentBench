code = """import json

filename = locals()['var_function-call-12916991409043369812']

with open(filename, 'r') as f:
    hits = json.load(f)

# Filter for most relevant
final_hits = []
for h in hits:
    text = (h['title'] + " " + h['content_snippet']).lower()
    if "collabdesign" in text or "discount" in text or "approval" in text or "limit" in text or "bundle" in text or "quantity" in text:
        final_hits.append(h)

print("__RESULT__:")
print(json.dumps(final_hits))"""

env_args = {'var_function-call-5104968504642584560': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_function-call-5104968504642582709': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_function-call-5104968504642580858': 'file_storage/function-call-5104968504642580858.json', 'var_function-call-6280688823787000736': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE', 'Description': 'Integrated development environment with intuitive coding and debugging capabilities.'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   ', 'Description': 'Environmentally-friendly PCB design solution with power utilization analytics.'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio', 'Description': 'Enhanced design collaboration platform offering real-time editing and feedback.'}], 'var_function-call-14795228103549564541': 'file_storage/function-call-14795228103549564541.json', 'var_function-call-12916991409043369812': 'file_storage/function-call-12916991409043369812.json'}

exec(code, env_args)
