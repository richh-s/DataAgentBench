code = """import json
# load the knowledge list from the stored file var_call_5nuDdUebIcJtApALNM8tcWfz
with open(var_call_5nuDdUebIcJtApALNM8tcWfz, 'r') as f:
    knowledge = json.load(f)

# create a simple mapping of titles to ids, trimming whitespace and lowercasing for matching
knowledge_map = {k['title'].strip().lower(): k['id'] for k in knowledge}

# print the map size and a sample of titles we might search for
result = {'count': len(knowledge_map), 'sample_titles': list(knowledge_map.keys())[:10]}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_v2XJIJEFaewXKyS8gYQzUR96': [], 'var_call_OFE2RIXXiLv5DO28Jp0A4eei': [{'Id': '#0Q0Wt000001WRAzKAO', 'AccountId': '001Wt00000PHVsDIAX', 'OpportunityId': '006Wt000007BGgXIAW', 'Name': 'NeoGreen EDA Expansion Quote', 'Status': 'Needs Review'}], 'var_call_Zwzto2MGXKJBNITZidH0bIar': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_3iCJeFLMty4HA1lXLg9a13Sq': [{'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'IsActive': '1', 'PricebookEntryId': '01uWt0000027P8cIAE', 'UnitPrice': '529.99', 'PricebookId': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book'}], 'var_call_y4VwR1LPR0EqcYaomRCsXWuz': [{'Id': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Pi5IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'UnitPrice': '399.99'}], 'var_call_O9YWJV8sjegnW3711kfYHcfP': [{'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.', 'IsActive': '1', 'External_ID__c': 'AI-Powered Circuit Design Tools,Customizable Workflow Automation_5'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio', 'Description': 'Enhanced design collaboration platform offering real-time editing and feedback.', 'IsActive': '1', 'External_ID__c': 'Cloud-Based Design Collaboration,Integrated Development Environments_30'}], 'var_call_5nuDdUebIcJtApALNM8tcWfz': 'file_storage/call_5nuDdUebIcJtApALNM8tcWfz.json'}

exec(code, env_args)
