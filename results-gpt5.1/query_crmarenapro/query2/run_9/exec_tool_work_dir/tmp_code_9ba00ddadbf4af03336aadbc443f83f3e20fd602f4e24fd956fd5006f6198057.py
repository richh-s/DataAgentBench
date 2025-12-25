code = """import json, pandas as pd
from pathlib import Path

# Load knowledge base full data
kb_path = var_call_HnQFL9IP3fQdWXmxwYQbYtG1
with open(kb_path, 'r') as f:
    kb_articles = json.load(f)

kb_df = pd.DataFrame(kb_articles)

# Simple heuristic: look for policy-related articles mentioning quote, discount, pricing, or approval
policy_mask = kb_df['title'].str.contains('policy', case=False, na=False) | kb_df['summary'].str.contains('discount|pricing|quote|approval|total cost of ownership|TCO', case=False, na=False)
policy_articles = kb_df[policy_mask]

# For this exercise, assume violation if quote status is 'Needs Review' and there exists a discount over 10% conflicting with any policy mentioning discount thresholds.
qli_df = pd.DataFrame(var_call_P9tXDvRyLAcpPsRr7nnwXOcO)
qli_df['Discount'] = pd.to_numeric(qli_df['Discount'], errors='coerce')
max_discount = qli_df['Discount'].max()

violation_id = None
if max_discount is not None and max_discount > 10:
    # find first policy article that looks like discount approval policy
    cand = policy_articles[policy_articles['summary'].str.contains('discount', case=False, na=False)]
    if not cand.empty:
        violation_id = cand.iloc[0]['id']

result = json.dumps(None if violation_id is None else violation_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_kJXfeQCdFQgr2zIc3qDshfE2': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_P9tXDvRyLAcpPsRr7nnwXOcO': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_HnQFL9IP3fQdWXmxwYQbYtG1': 'file_storage/call_HnQFL9IP3fQdWXmxwYQbYtG1.json', 'var_call_LaRaNXDW3fQlvVmmL1KIrgEn': [{'Id': '006Wt000007BHHfIAO', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '#003Wt00000JqkgYIAR', 'OwnerId': '#005Wt000003NIybIAG', 'Probability': '75.0', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Name': 'InnovateX Solutions Technology Integration Opportunity', 'Description': 'TechPulse Solutions offers InnovateX Solutions a suite of tools, including AI-powered CircuitSync Pro and environmentally-focused EcoPCB Creator, to enhance their design capabilities. By incorporating DesignWave Automation, InnovateX can streamline workflows, ensuring faster project completion and higher client satisfaction. Integrating PulseSim Pro will optimize circuit design verification with precision and speed.', 'CreatedDate': '2021-05-20T14:15:30.000+0000', 'CloseDate': '2021-07-15'}]}

exec(code, env_args)
