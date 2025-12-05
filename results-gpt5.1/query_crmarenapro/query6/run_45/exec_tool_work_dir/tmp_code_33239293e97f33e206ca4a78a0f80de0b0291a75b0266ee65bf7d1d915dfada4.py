code = """import json, pandas as pd
from pathlib import Path

# Load knowledge articles
path = Path(var_call_pNbrVyBZdmUOAejYW7uR2p8a)
articles = json.loads(path.read_text())

q_items = pd.DataFrame(var_call_ogDcKq1PV6QDVBLNhJMpYstk)

# Basic rule-of-thumb: large quantity with discount might violate pricing/volume rules.
# Search for knowledge articles mentioning "discount", "volume", "quantity", or "pricing".
text_hits = []
for art in articles:
    text = (art.get('title','') + ' ' + art.get('faq_answer__c','') + ' ' + art.get('summary','')).lower()
    if any(k in text for k in ['discount', 'volume', 'quantity', 'pricing', 'price break', 'bulk']):
        text_hits.append(art)

# If multiple, prefer ones explicitly about pricing/discount policies
priority = []
for art in text_hits:
    t = art.get('title','').lower()
    if any(k in t for k in ['discount', 'pricing', 'price', 'quote configuration', 'deal desk', 'approval']):
        priority.append(art)

chosen = None
if priority:
    chosen = priority[0]
elif text_hits:
    chosen = text_hits[0]

result = chosen['id'] if chosen else None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ogDcKq1PV6QDVBLNhJMpYstk': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_3FPszyivkh9vcrzlXjqtZ0Bd': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_call_reFThp7rNsuNzqg369mal5hk': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_lYVPpvtCAsbOHQVOleak0UBR': [{'id': 'a03Wt00000JqhItIAJ', 'name': 'Software Installation Error', 'description__c': 'Users report encountering errors during the initial installation process, which hinders the setup of TechPulse solutions.'}, {'id': '#a03Wt00000JqmLvIAJ', 'name': 'Billing Discrepancy', 'description__c': 'Some clients encounter unexpected charges on their billing statements, leading to confusion and dissatisfaction.'}, {'id': 'a03Wt00000JqmX6IAJ', 'name': 'Customizability Limitation   ', 'description__c': 'Despite customization options, some users find it challenging to tailor solutions to fit extremely niche industry needs.'}, {'id': 'a03Wt00000JqnHwIAJ', 'name': 'User Interface Bug', 'description__c': "A segment of users face occasional glitches in the software's user interface, affecting their overall usability experience."}, {'id': '#a03Wt00000JqtOtIAJ', 'name': 'Support Response Delay', 'description__c': 'Some users face delays in getting timely responses from the TechPulse support team during peak times.'}, {'id': 'a03Wt00000JqvLsIAJ', 'name': 'License Renewal Confusion', 'description__c': 'Clients find the license renewal process unclear, causing unexpected service disruptions.'}, {'id': '#a03Wt00000JqvNUIAZ', 'name': 'Training Module Access   ', 'description__c': 'Customers report occasional technical difficulties accessing online training modules crucial for product adoption.'}, {'id': 'a03Wt00000JqvvOIAR', 'name': 'Data Loss Incident', 'description__c': 'In rare cases, clients experience unanticipated data loss during software updates, causing significant operational setbacks.'}, {'id': '#a03Wt00000JqxVjIAJ', 'name': 'AI Feature Malfunction', 'description__c': 'Some AI-powered features intermittently fail to operate, resulting in reduced efficiency and user frustration.'}, {'id': '#a03Wt00000JqxtvIAB', 'name': 'Scalability Issue', 'description__c': 'Some enterprises report difficulties in scaling TechPulse solutions to meet increasing demands, impacting their expansion efforts.'}, {'id': 'a03Wt00000JqzKcIAJ', 'name': 'Data Integration Error', 'description__c': 'Users experience challenges when integrating TechPulse solutions with specific third-party software, leading to workflow disruptions.'}, {'id': 'a03Wt00000JqzPSIAZ', 'name': 'Security Compliance Query', 'description__c': 'Clients have concerns about understanding and adhering to the evolving security compliance standards set by TechPulse Solutions.'}, {'id': 'a03Wt00000JqzR3IAJ', 'name': 'Workflow Integration Lag', 'description__c': 'Certain clients experience latency issues when deploying TechPulse solutions within complex existing workflows.'}, {'id': 'a03Wt00000JqzSfIAJ', 'name': 'Feature Update Notification', 'description__c': "Customers are not consistently notified of new feature updates, leading to underutilization of the software's full capabilities."}, {'id': '#a03Wt00000JqzUHIAZ', 'name': 'ROI Assessment Discrepancy', 'description__c': 'A few customers need assistance reconciling their expected ROI with performance metrics delivered by the solutions.'}], 'var_call_pNbrVyBZdmUOAejYW7uR2p8a': 'file_storage/call_pNbrVyBZdmUOAejYW7uR2p8a.json'}

exec(code, env_args)
