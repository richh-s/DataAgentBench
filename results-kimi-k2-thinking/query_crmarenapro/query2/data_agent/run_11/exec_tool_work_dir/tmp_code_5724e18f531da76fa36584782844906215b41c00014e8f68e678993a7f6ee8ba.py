code = """import json
import pandas as pd
import sqlite3
import os

# Load data from storage
quote = pd.DataFrame(locals()['var_functions.query_db:0'])
quote_line_items = pd.DataFrame(locals()['var_functions.query_db:5'])
products = pd.DataFrame(locals()['var_functions.query_db:6'])

# Load Knowledge Articles from the file
articles_path = locals()['var_functions.query_db:2']
with open(articles_path, 'r') as f:
    knowledge_articles = json.load(f)
knowledge_df = pd.DataFrame(knowledge_articles)

# Find mandatory bundles article
mandatory_bundles_article = knowledge_df[
    knowledge_df['title'].str.contains('Mandatory Bundles', case=False, na=False)
]

# Check if PulseSim Pro is present in the quote
pulse_sim_present = False
product_ids_in_quote = []

for idx, row in quote_line_items.iterrows():
    product_id = str(row['Product2Id']).replace('#', '')
    product_ids_in_quote.append(product_id)

# Get actual product names from the database
product_db_path = None
for db_var in os.environ:
    if 'products_orders' in db_var.lower() and db_var.endswith('_PATH'):
        product_db_path = os.environ[db_var]
        break

violation = False
result_id = None

if product_db_path:
    conn = sqlite3.connect(product_db_path)
    all_products = pd.read_sql_query("SELECT Id, Name FROM Product2", conn)
    conn.close()
    
    # Check which products are in the quote
    quote_products = all_products[all_products['Id'].isin(product_ids_in_quote)]
    
    # Check for PulseSim Pro
    pulsim_sim = quote_products[quote_products['Name'].str.contains('PulseSim Pro', case=False, na=False)]
    pulse_sim_present = not pulsim_sim.empty
    
    if pulse_sim_present:
        # Check for mandatory bundled products (CircuitMaster Analyzer, VeriSim Express)
        circuit_master = quote_products[quote_products['Name'].str.contains('CircuitMaster Analyzer', case=False, na=False)]
        verisim_express = quote_products[quote_products['Name'].str.contains('VeriSim Express', case=False, na=False)]
        
        circuit_master_in_quote = not circuit_master.empty
        verisim_in_quote = not verisim_express.empty
        
        # Check if policy is violated (PulseSim present but mandatory bundles not present)
        if not (circuit_master_in_quote and verisim_in_quote):
            violation = True
    
    if violation and not mandatory_bundles_article.empty:
        result_id = mandatory_bundles_article.iloc[0]['id']
    else:
        result_id = None
else:
    result_id = None

print("__RESULT__:")
print(json.dumps(result_id))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:6': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.'}]}

exec(code, env_args)
