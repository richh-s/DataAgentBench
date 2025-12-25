code = """import json
import pandas as pd

# Load knowledge articles file path
path = var_call_YcOyTtnEgfC4yl0mwUOuPGGk

with open(path, 'r') as f:
    articles = json.load(f)

# Put into DataFrame for filtering/search
df = pd.DataFrame(articles)

# Look for pricing/discount/approval policy related articles
mask = df['title'].str.contains('Discount', case=False, na=False) | df['summary'].str.contains('discount', case=False, na=False) | df['title'].str.contains('Pricing', case=False, na=False) | df['summary'].str.contains('pricing', case=False, na=False) | df['title'].str.contains('Approval', case=False, na=False) | df['summary'].str.contains('approval', case=False, na=False)

policy_articles = df[mask]

result = policy_articles[['id','title','summary']].to_dict(orient='records')

result_json = json.dumps(result)

print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_adzQeAxk5UVkVtZahUuRnd5q': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_BVZjb9C3IB9Y9KYWefNezONp': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_YcOyTtnEgfC4yl0mwUOuPGGk': 'file_storage/call_YcOyTtnEgfC4yl0mwUOuPGGk.json', 'var_call_JHnO62ORI6AtzH5MjgvGPePU': [{'Id': '006Wt000007BHHfIAO', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '#003Wt00000JqkgYIAR', 'OwnerId': '#005Wt000003NIybIAG', 'Probability': '75.0', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Name': 'InnovateX Solutions Technology Integration Opportunity', 'Description': 'TechPulse Solutions offers InnovateX Solutions a suite of tools, including AI-powered CircuitSync Pro and environmentally-focused EcoPCB Creator, to enhance their design capabilities. By incorporating DesignWave Automation, InnovateX can streamline workflows, ensuring faster project completion and higher client satisfaction. Integrating PulseSim Pro will optimize circuit design verification with precision and speed.', 'CreatedDate': '2021-05-20T14:15:30.000+0000', 'CloseDate': '2021-07-15'}]}

exec(code, env_args)
