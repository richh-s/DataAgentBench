code = """import json
import pandas as pd

# Load previous results
quote_info = locals()['var_function-call-13399224158723443727']
quote_lines = locals()['var_function-call-13399224158723444252']
products = locals()['var_function-call-16265987100578663445']
ka_file_path = locals()['var_function-call-13399224158723440681']

# Read Knowledge Articles
with open(ka_file_path, 'r') as f:
    knowledge_articles = json.load(f)

# Calculate Quote Metrics
total_amount = sum(float(item['TotalPrice']) for item in quote_lines)
max_discount = max(float(item['Discount']) for item in quote_lines)
line_items_data = []

# Map Product Names
product_map = {p['Id'].strip('#').strip(): p['Name'].strip() for p in products}
# Also handle original IDs if needed, but stripping # helps normalize.

for item in quote_lines:
    pid = item['Product2Id'].strip('#').strip()
    pname = product_map.get(pid, "Unknown Product")
    line_items_data.append({
        'Product': pname,
        'Quantity': float(item['Quantity']),
        'TotalPrice': float(item['TotalPrice']),
        'Discount': float(item['Discount'])
    })

print(f"Quote Total: {total_amount}")
print(f"Max Discount: {max_discount}")
print("Line Items:", line_items_data)

# Search Knowledge Articles for relevant keywords
keywords = ['policy', 'approval', 'discount', 'setup', 'cost', 'fee', 'limit']
relevant_articles = []

for ka in knowledge_articles:
    text = (ka['title'] + " " + ka['summary'] + " " + ka.get('faq_answer__c', '')).lower()
    if any(k in text for k in keywords):
        relevant_articles.append({
            'id': ka['id'],
            'title': ka['title'],
            'summary': ka['summary'],
            'faq_answer': ka.get('faq_answer__c', '')
        })

print("__RESULT__:")
print(json.dumps(relevant_articles))"""

env_args = {'var_function-call-13399224158723443727': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_function-call-13399224158723444252': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_function-call-13399224158723440681': 'file_storage/function-call-13399224158723440681.json', 'var_function-call-16265987100578663445': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   ', 'Description': 'Environmentally-friendly PCB design solution with power utilization analytics.'}, {'Id': '#01tWt000006hVEnIAM', 'Name': 'DesignWave Automation  ', 'Description': 'Customizable workflow automation tool enhancing process efficiency.'}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro', 'Description': 'AI-enhanced design tool for seamless circuit synchronization and development.'}]}

exec(code, env_args)
