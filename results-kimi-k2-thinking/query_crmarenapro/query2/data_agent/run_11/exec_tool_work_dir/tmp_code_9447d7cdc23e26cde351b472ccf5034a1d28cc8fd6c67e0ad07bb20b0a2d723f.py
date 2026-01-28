code = """import json
import pandas as pd

# Load Quote
quote = pd.DataFrame(locals()['var_functions.query_db:0'])
print("Quote:", quote)

# Load Quote Line Items
quote_line_items = pd.DataFrame(locals()['var_functions.query_db:5'])
print("\nQuote Line Items:")
print(quote_line_items)

# Load Product data
products = pd.DataFrame(locals()['var_functions.query_db:6'])
print("\nProducts:")
print(products)

# Load Knowledge Articles from the file
articles_path = locals()['var_functions.query_db:2']
with open(articles_path, 'r') as f:
    knowledge_articles = json.load(f)
knowledge_df = pd.DataFrame(knowledge_articles)
print("\nKnowledge Articles:")
print(knowledge_df)

# Find mandatory bundles article
mandatory_bundles_article = knowledge_df[
    knowledge_df['title'].str.contains('Mandatory Bundles', case=False, na=False)
]
print("\nMandatory Bundles Article:")
print(mandatory_bundles_article)

# Check for PulseSim Pro in the quote
pulse_sim_quote = quote_line_items[quote_line_items['Product2Id'].str.strip('#') == '01tWt000006hV57IAE']
pulse_sim_present = not pulse_sim_quote.empty
print("\nPulseSim Pro present in quote:", pulse_sim_present)

# Check if mandatory bundle products are also present in quote (looking for CircuitMaster Analyzer and VeriSim Express)
# This is a simplified check - we need to get names of products in the quote
product_ids_in_quote = quote_line_items['Product2Id'].str.strip('#').tolist()
print("Product IDs in quote:", product_ids_in_quote)

# Get all products from the database to find the bundle items
import sqlite3
import os

# Find the correct database file path from the environment
product_db_path = None
for db_var in os.environ:
    if 'products_orders' in db_var.lower() and db_var.endswith('_PATH'):
        product_db_path = os.environ[db_var]
        break

if product_db_path:
    conn = sqlite3.connect(product_db_path)
    all_products = pd.read_sql_query("SELECT Id, Name FROM Product2", conn)
    conn.close()
    print("\nAll Products:")
    print(all_products)
    
    # Check for mandatory bundle products
    circuit_master = all_products[all_products['Name'].str.contains('CircuitMaster Analyzer', case=False, na=False)]
    verisim_express = all_products[all_products['Name'].str.contains('VeriSim Express', case=False, na=False)]
    
    print("\nCircuitMaster Analyzer found:", not circuit_master.empty)
    print("VeriSim Express found:", not verisim_express.empty)
    
    # Check if bundle products are in the quote
    circuit_master_in_quote = any(cid in product_ids_in_quote for cid in circuit_master['Id'].tolist())
    verisim_in_quote = any(vid in product_ids_in_quote for vid in verisim_express['Id'].tolist())
    
    print("CircuitMaster Analyzer in quote:", circuit_master_in_quote)
    print("VeriSim Express in quote:", verisim_in_quote)
    
    # Determine violation
    violation = pulse_sim_present and not (circuit_master_in_quote and verisim_in_quote)
    print("\nPolicy violation detected:", violation)
    
    if violation and not mandatory_bundles_article.empty:
        result_id = mandatory_bundles_article.iloc[0]['id']
    else:
        result_id = None
else:
    print("Could not find product database path")
    result_id = None

print("__RESULT__:")
print(json.dumps(result_id))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:6': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.'}]}

exec(code, env_args)
