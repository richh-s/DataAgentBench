code = """import json

qlis = var_call_2BFatLIeQP2dDuaXYHht4N8h

# Identify any obvious volume-based thresholds from quantities
quantities = [float(r['Quantity']) for r in qlis]

result = {
  'quantities': quantities,
  'total_quantity': sum(quantities)
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_2BFatLIeQP2dDuaXYHht4N8h': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_P7Ec2BpMp1ubbfjWL4mq1OoA': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_call_S7ECBbcS9D5MvJPwQ4rtn1z7': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_zDIqxA40xXAve7E91D2KXYDp': 'file_storage/call_zDIqxA40xXAve7E91D2KXYDp.json', 'var_call_uvjZEMc5soWvLDrGxfhuMF7V': [{'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'summary': 'Volume-Based Discounts'}, {'id': '#ka0Wt000000EpSUIA0', 'title': 'TechPulse Solution Volume-Based Installation Timeline Policy', 'summary': 'TechPulse Solution Volume-Based Installation Timeline Policy'}, {'id': 'ka0Wt000000Em4zIAC', 'title': 'Navigating Installation Challenges: Solutions for Seamless Setup of TechPulse EDA Tools', 'summary': "TechPulse Solutions clients sometimes face software installation errors, which can be an obstacle during the initial setup of the company's powerful electronic design automation tools. This article delves into the two main solutions designed to address these challenges effectively. The 'Priority Support Upgrade' offers customers the advantage of faster response times to installation issues, ensuring minimal disruption and timely resolution. Additionally, 'Comprehensive Training Access' equips users with the necessary skills and confidence to handle potential roadblocks in the installation process, fostering a deeper understanding of the product's intricacies. These strategies, together with TechPulse Solutions' commitment to innovation and customer satisfaction, reinforce the seamless integration of their AI-powered solutions into existing workflows, ensuring clients maximize their investment."}]}

exec(code, env_args)
