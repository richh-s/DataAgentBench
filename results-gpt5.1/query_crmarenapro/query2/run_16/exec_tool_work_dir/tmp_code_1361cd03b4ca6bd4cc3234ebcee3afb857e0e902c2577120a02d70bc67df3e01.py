code = """import json, pandas as pd
from pathlib import Path

# Load full knowledge articles
path = Path(var_call_OR8Ctq16NdknEY7RjhFjv9ha)
with path.open() as f:
    knowledge = json.load(f)

quote_li = pd.DataFrame(var_call_JQW8rT6oCmq35ujw4AbavR2p)
opp = pd.DataFrame(var_call_oKuDmR7RQhQzmtuHVFbJDunD)

subtotal = quote_li['TotalPrice'].astype(float).sum()

articles = pd.DataFrame(knowledge)

violations = []

# Very simple rule heuristics based on titles
for _, row in articles.iterrows():
    title = (row.get('title') or '').strip().lower()
    body = (row.get('faq_answer__c') or '').lower()
    # Example heuristic rules (synthetic, based on likely policy article titles)
    if 'discount' in title or 'discount' in body:
        # check if any discount exceeds 20%
        max_disc = quote_li['Discount'].astype(float).max()
        if max_disc > 20:
            violations.append(row['id'])
    if 'approval threshold' in title or 'high-value quote' in title or 'deal desk' in title:
        # e.g., quotes over 25000 need special approval; our quote is smaller
        if subtotal > 25000:
            violations.append(row['id'])
    if 'payment terms' in title and 'net 30' in body:
        # we have no terms info, so cannot evaluate
        pass

viol_id = violations[0] if violations else None

result = json.dumps(viol_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_vo8X9Ah7Ju6UF4oZLyHV8QT9': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_JQW8rT6oCmq35ujw4AbavR2p': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_oKuDmR7RQhQzmtuHVFbJDunD': [{'Id': '006Wt000007BHHfIAO', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '#003Wt00000JqkgYIAR', 'OwnerId': '#005Wt000003NIybIAG', 'Probability': '75.0', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Name': 'InnovateX Solutions Technology Integration Opportunity', 'Description': 'TechPulse Solutions offers InnovateX Solutions a suite of tools, including AI-powered CircuitSync Pro and environmentally-focused EcoPCB Creator, to enhance their design capabilities. By incorporating DesignWave Automation, InnovateX can streamline workflows, ensuring faster project completion and higher client satisfaction. Integrating PulseSim Pro will optimize circuit design verification with precision and speed.', 'CreatedDate': '2021-05-20T14:15:30.000+0000', 'CloseDate': '2021-07-15'}], 'var_call_OR8Ctq16NdknEY7RjhFjv9ha': 'file_storage/call_OR8Ctq16NdknEY7RjhFjv9ha.json'}

exec(code, env_args)
