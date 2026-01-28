code = """import json

# Get quote line items
quote_items = locals()['var_functions.query_db:5']

# Based on the knowledge article, PulseSim Pro requires CircuitMaster Analyzer and VeriSim Express
# Let's check if we have product matches

# Get product names from products_orders database
product1_data = locals()['var_functions.query_db:10']
product2_data = locals()['var_functions.query_db:12']
product3_data = locals()['var_functions.query_db:16']
product4_data = locals()['var_functions.query_db:18']

all_products = product1_data + product2_data + product3_data + product4_data

print('__RESULT__:')
print(json.dumps(all_products))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.execute_python:8': [{'id': 'ka0Wt000000EqQ9IAK', 'title': "Understanding TechPulse's Return Policy for Purchased Items", 'summary': "Details of TechPulse Solutions' return policy for purchased items, outlining the process for returns, refunds, and exchanges to ensure transparency and customer satisfaction."}, {'id': '#ka0Wt000000EpSUIA0', 'title': 'TechPulse Solution Volume-Based Installation Timeline Policy', 'summary': 'TechPulse Solution Volume-Based Installation Timeline Policy'}, {'id': 'ka0Wt000000Ens5IAC', 'title': 'Mandatory Bundles for Quotes', 'summary': 'Mandatory Bundles for Quotes'}, {'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers', 'summary': 'Policy for price adjustments based on competing offers'}], 'var_functions.query_db:10': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.'}], 'var_functions.query_db:12': [{'Id': '#01tWt000006hVDBIA2', 'Name': 'CircuitMaster Analyzer', 'Description': 'Sophisticated simulation software ensuring precise verification and testing.'}], 'var_functions.execute_python:14': ['#01tWt000006hV6jIAE', '01tWt000006hV57IAE', '#01tWt000006hVQ5IAM'], 'var_functions.query_db:16': [{'Id': '01tWt000006hVQ6IAM', 'Name': 'VeriSim Express  ', 'Description': 'Express verification software focusing on speed and precision for circuit testing.'}], 'var_functions.query_db:18': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.'}]}

exec(code, env_args)
