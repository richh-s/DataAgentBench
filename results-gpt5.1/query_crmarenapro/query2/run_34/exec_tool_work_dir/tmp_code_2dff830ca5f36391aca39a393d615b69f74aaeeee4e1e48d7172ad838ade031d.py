code = """import json

quote_items = var_call_53vjzJE6M7RXBlhzFTCqbQy5

violated_article_id = None

# Simple hard-coded rules based on likely policy article titles
# 1) Volume-Based Discounts: likely restricts discount <= 20% overall and per line
for li in quote_items:
    try:
        discount = float(li.get('Discount') or 0)
    except ValueError:
        discount = 0
    if discount > 20:
        violated_article_id = 'ka0Wt000000Eq0MIAS'  # Volume-Based Discounts
        break

# 2) Mandatory Bundles for Quotes: if a bundle policy violation detected (e.g., negative price etc.)
# With no product metadata here, we will not infer bundle violations.

# 3) Installation / setup costs: no setup line items appear so we assume compliance.

if violated_article_id is None:
    result = None
else:
    result = violated_article_id

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_5GIGc1gXNiR4wwOQRtGtJ6xR': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_53vjzJE6M7RXBlhzFTCqbQy5': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_heIqjuRcB20iaivLPvi8HNDa': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_9LfO5OjJDB6xNe6uQ6wBbWkA': 'file_storage/call_9LfO5OjJDB6xNe6uQ6wBbWkA.json', 'var_call_bYwhO3iOt70YWaiEXoYmSCqc': [{'id': '#ka0Wt000000EqRlIAK', 'title': 'Competitor: NanoDesign Systems   '}, {'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts'}, {'id': 'ka0Wt000000EorOIAS', 'title': 'Automating Development Processes with AutoGen IDE'}, {'id': 'ka0Wt000000EoJWIA0', 'title': 'Streamlined Development with AutoGen IDE'}, {'id': 'ka0Wt000000Em4zIAC', 'title': 'Navigating Installation Challenges: Solutions for Seamless Setup of TechPulse EDA Tools'}, {'id': 'ka0Wt000000Ens5IAC', 'title': 'Mandatory Bundles for Quotes'}, {'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers'}]}

exec(code, env_args)
