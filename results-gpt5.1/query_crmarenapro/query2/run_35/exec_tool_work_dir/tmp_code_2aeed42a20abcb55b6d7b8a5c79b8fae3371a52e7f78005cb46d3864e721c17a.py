code = """import json, pandas as pd

# Load full knowledge articles
import os
with open(var_call_LIHfFbNPLuGuVS6BWATo9Osl, 'r') as f:
    knowledge = json.load(f)

quote = var_call_dLnFnixCR8fpfzgGUCImiSS9[0]
qli = pd.DataFrame(var_call_o6E6je3Y1FzjZFwMy4mrjI0U)

# Compute total quote amount
for col in ['Quantity','UnitPrice','Discount','TotalPrice']:
    qli[col] = qli[col].astype(float)

computed_total = (qli['Quantity'] * qli['UnitPrice'] * (1 - qli['Discount']/100)).sum()
stored_total = qli['TotalPrice'].sum()

violated_id = None

# Simple policy inference from knowledge content
for art in knowledge:
    text = (art.get('title','') + ' ' + art.get('summary','') + ' ' + art.get('faq_answer__c','')).lower()
    if 'quote approval' in text or 'discount policy' in text or 'pricing policy' in text or 'quote' in art.get('title','').lower():
        # Example rule: if total discount > 10% for any line, it's a violation
        if (qli['Discount'] > 10).any():
            violated_id = art['id']
            break

result = violated_id if violated_id is not None else None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_dLnFnixCR8fpfzgGUCImiSS9': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_o6E6je3Y1FzjZFwMy4mrjI0U': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_4uB4vOqFkqUB7JCCZzGuAjwB': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_LIHfFbNPLuGuVS6BWATo9Osl': 'file_storage/call_LIHfFbNPLuGuVS6BWATo9Osl.json'}

exec(code, env_args)
