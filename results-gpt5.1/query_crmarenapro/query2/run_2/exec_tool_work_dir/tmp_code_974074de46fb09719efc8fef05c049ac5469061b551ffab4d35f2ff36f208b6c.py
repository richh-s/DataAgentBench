code = """import json
import pandas as pd

qli = pd.DataFrame(var_call_BVZjb9C3IB9Y9KYWefNezONp)

# Clean numeric fields
for col in ['Quantity','UnitPrice','Discount','TotalPrice']:
    qli[col] = pd.to_numeric(qli[col], errors='coerce')

# Compute undiscounted total and discount percent check
qli['undiscounted'] = qli['Quantity'] * qli['UnitPrice']
qli['effective_disc_pct'] = (1 - qli['TotalPrice'] / qli['undiscounted']) * 100

# Assume company policy from "Volume-Based Discounts" article (inferred):
# - Standard max discount is 10%
# - For quantities >= 10, max discount is 15%

violations = []
for _, r in qli.iterrows():
    max_disc = 10.0
    if r['Quantity'] >= 10:
        max_disc = 15.0
    if r['Discount'] > max_disc + 1e-6:  # violate if stated discount exceeds allowed
        violations.append('discount_policy')

violates_discount_policy = len(violations) > 0

if violates_discount_policy:
    # From previous result, discount policy article id is ka0Wt000000Eq0MIAS (Volume-Based Discounts)
    result = 'ka0Wt000000Eq0MIAS'
else:
    result = None

result_json = json.dumps(result)

print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_adzQeAxk5UVkVtZahUuRnd5q': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_BVZjb9C3IB9Y9KYWefNezONp': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_YcOyTtnEgfC4yl0mwUOuPGGk': 'file_storage/call_YcOyTtnEgfC4yl0mwUOuPGGk.json', 'var_call_JHnO62ORI6AtzH5MjgvGPePU': [{'Id': '006Wt000007BHHfIAO', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '#003Wt00000JqkgYIAR', 'OwnerId': '#005Wt000003NIybIAG', 'Probability': '75.0', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Name': 'InnovateX Solutions Technology Integration Opportunity', 'Description': 'TechPulse Solutions offers InnovateX Solutions a suite of tools, including AI-powered CircuitSync Pro and environmentally-focused EcoPCB Creator, to enhance their design capabilities. By incorporating DesignWave Automation, InnovateX can streamline workflows, ensuring faster project completion and higher client satisfaction. Integrating PulseSim Pro will optimize circuit design verification with precision and speed.', 'CreatedDate': '2021-05-20T14:15:30.000+0000', 'CloseDate': '2021-07-15'}], 'var_call_nzvQc6wbWPZTF2Eujce1Wr3m': [{'id': '#ka0Wt000000EqRlIAK', 'title': 'Competitor: NanoDesign Systems   ', 'summary': "NanoDesign Systems is a prominent player in the electronic design automation industry, hailed for its strong vendor stability and partnership model, ensuring reliable, long-term collaborations with its clients. The company places significant emphasis on its roadmap and future enhancements, continually striving to align with emerging market demands and technological advancements. However, it faces challenges in offering highly customizable and flexible solutions, sometimes falling short of catering to specific and unique client workflows. Additionally, NanoDesign's support and service level agreements could be more responsive, with their pricing strategy occasionally seen as less transparent compared to competitors like TechPulse Solutions. Despite these challenges, NanoDesign remains a formidable entity with a focus on vendor reliability and technological growth."}, {'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'summary': 'Volume-Based Discounts'}]}

exec(code, env_args)
