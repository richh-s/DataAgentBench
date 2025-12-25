code = """import json
import sqlite3

# Load previous results
quote_items = json.loads(locals()['var_function-call-11232404843001699657'])
ka_file_path = locals()['var_function-call-11232404843001699126']

# Extract Product Ids to query
product_ids = [item['Product2Id'] for item in quote_items]
# Clean IDs (remove leading # if present for querying, though DB might have them)
# I will query with both raw and cleaned versions to be safe, or just use the raw ones if I assume consistency.
# The hint says corruption exists.
# Let's generate a list of IDs to query.
clean_ids = [pid.lstrip('#') for pid in product_ids]
raw_ids = product_ids
all_ids_to_query = list(set(clean_ids + raw_ids))

# Prepare SQL query for products
ids_formatted = "', '".join(all_ids_to_query)
product_query = f"SELECT Id, Name FROM Product2 WHERE Id IN ('{ids_formatted}')"

# Read Knowledge Articles
with open(ka_file_path, 'r') as f:
    knowledge_articles = json.load(f)

# Search for relevant policies in Knowledge Articles
relevant_articles = []
for ka in knowledge_articles:
    text = (ka['title'] + " " + ka['summary'] + " " + (ka['faq_answer__c'] or "")).lower()
    if 'discount' in text or 'approval' in text or 'cost' in text or 'setup' in text or 'bundle' in text:
        relevant_articles.append(ka)

print("__RESULT__:")
print(json.dumps({"product_query": product_query, "relevant_articles_count": len(relevant_articles), "relevant_articles_preview": relevant_articles[:5]}))"""

env_args = {'var_function-call-11232404843001700188': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_function-call-11232404843001699657': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_function-call-11232404843001699126': 'file_storage/function-call-11232404843001699126.json'}

exec(code, env_args)
