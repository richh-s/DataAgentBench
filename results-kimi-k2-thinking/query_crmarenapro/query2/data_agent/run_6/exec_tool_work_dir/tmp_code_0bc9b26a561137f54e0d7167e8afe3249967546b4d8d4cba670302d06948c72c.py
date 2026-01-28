code = """import json
import os

# Read the knowledge articles from the file path stored in the variable
knowledge_file_path = var_functions.query_db:2

# The variable contains a string with the file path
if isinstance(knowledge_file_path, str):
    with open(knowledge_file_path, 'r') as f:
        knowledge_articles = json.load(f)
else:
    knowledge_articles = knowledge_file_path

# Find the Mandatory Bundles article
bundles_article = None
for article in knowledge_articles:
    if "Mandatory Bundles" in article.get("title", ""):
        bundles_article = article
        break

# Get quote line items and products
quote_items = var_functions.query_db:5
products_from_db = var_functions.query_db:6

# Check which products are in the quote
product_ids_in_quote = [item['Product2Id'] for item in quote_items]
product_names_in_quote = []

for prod in products_from_db:
    # Handle the # prefix issue
    prod_id_clean = prod['Id'].replace('#', '')
    for quote_prod_id in product_ids_in_quote:
        quote_prod_id_clean = quote_prod_id.replace('#', '')
        if prod_id_clean == quote_prod_id_clean:
            product_names_in_quote.append(prod['Name'])

# Extract mandatory bundle requirements
if bundles_article:
    article_text = bundles_article.get('faq_answer__c', '')
    
    # Find PulseSim Pro requirements
    pulsesim_requirements = []
    if 'PulseSim Pro' in article_text:
        lines = article_text.split('\n')
        capture = False
        for line in lines:
            if 'PulseSim Pro' in line:
                capture = True
            if capture:
                if line.strip() and (line.startswith('2.') or line.startswith('3.') or line.startswith('4.') or line.startswith('5.')):
                    break
                if 'must also include' in line or 'must also' in line or 'CircuitMaster Analyzer' in line or 'VeriSim Express' in line:
                    pulsesim_requirements.append(line.strip())
    
    result = {
        'article_id': bundles_article['id'],
        'article_title': bundles_article['title'],
        'pulsesim_requirements': pulsesim_requirements,
        'products_in_quote': product_names_in_quote,
        'product_ids': product_ids_in_quote
    }
else:
    result = {'article_id': None, 'error': 'No bundles article found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:6': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1'}]}

exec(code, env_args)
