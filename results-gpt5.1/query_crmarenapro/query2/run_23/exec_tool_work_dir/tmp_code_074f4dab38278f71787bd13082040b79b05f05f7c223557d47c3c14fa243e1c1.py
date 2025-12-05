code = """import json, re, pandas as pd, os

# Load knowledge articles from file
path = var_call_QoUyg2rjlqkPSPHKtmpb4cTD
with open(path, 'r') as f:
    knowledge = json.load(f)

quote = pd.DataFrame(var_call_IJHGVw2EFX8Y0p0tUxU95Mgw)[0:1].to_dict(orient='records')[0]
qli = pd.DataFrame(var_call_4weVJ6zxUoEemvtlrx2O5RH1)
opp = pd.DataFrame(var_call_hFZibI8248TFZ5BKm5SRtMSv)[0:1].to_dict(orient='records')[0]

# Compute total quote amount
qli['TotalPrice'] = pd.to_numeric(qli['TotalPrice'], errors='coerce')
quote_total = float(qli['TotalPrice'].sum()) if not qli['TotalPrice'].isna().all() else None

violations = []

# Very simple policy inference from knowledge: look for mention of "implementation", "deployment", "setup" tied to cost / pricing / TCO
for art in knowledge:
    text = (art.get('title','') + ' ' + art.get('faq_answer__c','') + ' ' + art.get('summary','')).lower()
    # Heuristic: if article talks about cost/price/TCO and implementation/setup/deployment complexity, assume a policy that setup costs must be transparent / reasonable.
    if any(w in text for w in ['total cost of ownership', 'tco', 'pricing', 'total cost', 'cost of ownership']) and any(w in text for w in ['implementation', 'deployment', 'setup']):
        # If quote status is Needs Review and discount is high or amount > opportunity amount by >20%, flag
        opp_amount = float(opp.get('Amount') or 0)
        if quote_total and opp_amount and quote_total > 1.2 * opp_amount:
            violations.append(art['id'])
        else:
            # Or if any discount > 20%
            qli['Discount'] = pd.to_numeric(qli['Discount'], errors='coerce')
            if (qli['Discount'] > 20).any():
                violations.append(art['id'])

result = None
if violations:
    # deduplicate and pick first normalized id without leading '#'
    vid = str(violations[0]).lstrip('#')
    result = vid

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_IJHGVw2EFX8Y0p0tUxU95Mgw': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_4weVJ6zxUoEemvtlrx2O5RH1': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_QoUyg2rjlqkPSPHKtmpb4cTD': 'file_storage/call_QoUyg2rjlqkPSPHKtmpb4cTD.json', 'var_call_hFZibI8248TFZ5BKm5SRtMSv': [{'Id': '006Wt000007BHHfIAO', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '#003Wt00000JqkgYIAR', 'OwnerId': '#005Wt000003NIybIAG', 'Probability': '75.0', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Name': 'InnovateX Solutions Technology Integration Opportunity', 'Description': 'TechPulse Solutions offers InnovateX Solutions a suite of tools, including AI-powered CircuitSync Pro and environmentally-focused EcoPCB Creator, to enhance their design capabilities. By incorporating DesignWave Automation, InnovateX can streamline workflows, ensuring faster project completion and higher client satisfaction. Integrating PulseSim Pro will optimize circuit design verification with precision and speed.', 'CreatedDate': '2021-05-20T14:15:30.000+0000', 'CloseDate': '2021-07-15'}]}

exec(code, env_args)
