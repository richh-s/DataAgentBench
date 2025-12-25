code = """import json
import pandas as pd

qli = pd.DataFrame(var_call_vxPKe9miRzGfc90MrlLp738e)

knowledge_file = var_call_DIjZCllITSKzHjKhyzCkZi2C
with open(knowledge_file, 'r') as f:
    knowledge = json.load(f)
ka = pd.DataFrame(knowledge)

invalid_ka_ids = []

for _, row in ka.iterrows():
    text = (str(row.get('title','')) + ' ' + str(row.get('faq_answer__c','')) + ' ' + str(row.get('summary',''))).lower()
    if 'discount' in text or 'pricing' in text or 'quote configuration' in text or 'bundle' in text:
        invalid_ka_ids.append(row['id'])

result = list(dict.fromkeys(invalid_ka_ids))[:1]

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_vxPKe9miRzGfc90MrlLp738e': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_02lWnQ1QxEYHDHoLXRoDAOc3': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_call_gpFEeL3EW67uAusBPdG6YcyM': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_DIjZCllITSKzHjKhyzCkZi2C': 'file_storage/call_DIjZCllITSKzHjKhyzCkZi2C.json'}

exec(code, env_args)
