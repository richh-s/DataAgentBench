code = """import json, re
from pathlib import Path

path = Path(var_call_e4cVh4gvC35fxV9g9KATxYof)
articles = json.loads(path.read_text())

quote = json.loads('[{"Id": "0Q0Wt000001WSDVKA4", "OpportunityId": "#006Wt000007BHHfIAO", "AccountId": "#001Wt00000PGXrKIAX", "ContactId": "003Wt00000JqkgYIAR", "Name": "TechPulse-InnovateX Integration Quote", "Description": "Initial quote for AI-powered EDA solutions integration", "Status": "Needs Review", "CreatedDate": "2021-06-01T10:00:00.000+0000", "ExpirationDate": "2021-07-01"}]')[0]
qli = json.loads('[{"Id": "0QLWt0000022xB1OAI", "QuoteId": "#0Q0Wt000001WSDVKA4", "OpportunityLineItemId": "00kWt000002HHpqIAG", "Product2Id": "#01tWt000006hVEnIAM", "PricebookEntryId": "01uWt0000027PGfIAM", "Quantity": "5.0", "UnitPrice": "479.99", "Discount": "5.0", "TotalPrice": "2279.9525"}, {"Id": "0QLWt0000022yNAOAY", "QuoteId": "0Q0Wt000001WSDVKA4", "OpportunityLineItemId": "00kWt000002HavbIAC", "Product2Id": "#01tWt000006hV6jIAE", "PricebookEntryId": "01uWt0000027P8bIAE", "Quantity": "8.0", "UnitPrice": "349.99", "Discount": "15.0", "TotalPrice": "2379.932"}, {"Id": "0QLWt0000022z7tOAA", "QuoteId": "0Q0Wt000001WSDVKA4", "OpportunityLineItemId": "00kWt000002HXg4IAG", "Product2Id": "01tWt000006hV57IAE", "PricebookEntryId": "01uWt0000027P3lIAE", "Quantity": "10.0", "UnitPrice": "499.99", "Discount": "10.0", "TotalPrice": "4499.91"}, {"Id": "0QLWt0000022z9VOAQ", "QuoteId": "0Q0Wt000001WSDVKA4", "OpportunityLineItemId": "00kWt000002HL76IAG", "Product2Id": "#01tWt000006hVQ5IAM", "PricebookEntryId": "01uWt0000027PVBIA2", "Quantity": "7.0", "UnitPrice": "339.99", "Discount": "5.0", "TotalPrice": "2260.9335"}]')

violating_article_id = None

for art in articles:
    text = (art.get('title','') or '') + ' ' + (art.get('faq_answer__c','') or '') + ' ' + (art.get('summary','') or '')
    lower = text.lower()
    if 'quote approval' in lower or 'discount' in lower or 'pricing policy' in lower or 'setup fee' in lower:
        violating_article_id = art['id']
        break

result = json.dumps(violating_article_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_CJ4BAEMzm2nO7xBfjEzvqSzw': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_De1175omd2KGwqAOSTuZiBP7': [{'Id': '006Wt000007BHHfIAO', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '#003Wt00000JqkgYIAR', 'OwnerId': '#005Wt000003NIybIAG', 'Probability': '75.0', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Name': 'InnovateX Solutions Technology Integration Opportunity', 'Description': 'TechPulse Solutions offers InnovateX Solutions a suite of tools, including AI-powered CircuitSync Pro and environmentally-focused EcoPCB Creator, to enhance their design capabilities. By incorporating DesignWave Automation, InnovateX can streamline workflows, ensuring faster project completion and higher client satisfaction. Integrating PulseSim Pro will optimize circuit design verification with precision and speed.', 'CreatedDate': '2021-05-20T14:15:30.000+0000', 'CloseDate': '2021-07-15'}], 'var_call_ReGB9BTuCT3n4CiwXTkHkGlK': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_FDeW1jh6YecVmyQyqvFsdF7X': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_e4cVh4gvC35fxV9g9KATxYof': 'file_storage/call_e4cVh4gvC35fxV9g9KATxYof.json'}

exec(code, env_args)
