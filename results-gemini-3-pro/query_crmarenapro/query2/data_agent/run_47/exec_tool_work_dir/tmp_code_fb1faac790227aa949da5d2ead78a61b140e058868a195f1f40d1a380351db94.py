code = """import json
import pandas as pd

# Load Line Items
line_items = locals()['var_function-call-4134485673776411407']
if isinstance(line_items, str):
    line_items = json.loads(line_items)

# Calculate Quote Metrics
total_amount = sum(float(item['TotalPrice']) for item in line_items)
max_discount = max(float(item['Discount']) for item in line_items)
items_summary = []
for item in line_items:
    items_summary.append({
        'id': item['Product2Id'],
        'discount': float(item['Discount']),
        'total': float(item['TotalPrice'])
    })

print(f"Total Amount: {total_amount}")
print(f"Max Discount: {max_discount}")

# Load Knowledge Articles
ka_file = locals()['var_function-call-13328938538877257626']
with open(ka_file, 'r') as f:
    articles = json.load(f)

# Search for relevant articles
relevant_articles = []
for art in articles:
    text = (art.get('title') or '') + ' ' + (art.get('summary') or '') + ' ' + (art.get('faq_answer__c') or '')
    if 'approval' in text.lower() and 'quote' in text.lower():
        relevant_articles.append(art)

print(f"Found {len(relevant_articles)} relevant articles.")
for art in relevant_articles:
    print(f"ID: {art['id']}")
    print(f"Title: {art['title']}")
    print(f"Summary: {art['summary']}")
    print("-" * 20)

print("__RESULT__:")
print(json.dumps(relevant_articles))"""

env_args = {'var_function-call-4134485673776413636': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_function-call-4134485673776411407': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_function-call-13328938538877258407': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   ', 'Description': 'Environmentally-friendly PCB design solution with power utilization analytics.'}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro', 'Description': 'AI-enhanced design tool for seamless circuit synchronization and development.'}], 'var_function-call-13328938538877257626': 'file_storage/function-call-13328938538877257626.json', 'var_function-call-1134305191959445827': [], 'var_function-call-14270719026228689260': [{'Id': '#01tWt000006hVEnIAM', 'Name': 'DesignWave Automation  ', 'Description': 'Customizable workflow automation tool enhancing process efficiency.'}]}

exec(code, env_args)
