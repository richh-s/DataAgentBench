code = """import json
from pathlib import Path
# Load the knowledge articles result file
kp = Path(var_call_xjrGc45h0QyzaOlZQUClsKeE)
with kp.open('r', encoding='utf-8') as f:
    k_articles = json.load(f)

# Load the quote and quote line items datasets which are available as variables
quotes = var_call_Aw7RtuPc88ZOg87xkD70HTGs
qli = var_call_IqZD5B4iS32EkLOdzIlxjcrp

# Identify the quote and its line items
quote_id = '0Q0Wt000001WRAzKAO'
quote = None
for q in quotes:
    # handle possible leading #
    if q.get('Id') and q.get('Id').lstrip('#') == quote_id.lstrip('#'):
        quote = q
        break

line_items = [l for l in qli if l.get('QuoteId') and l.get('QuoteId').lstrip('#') == quote_id.lstrip('#')]

# Gather suspicious config flags
suspicious = []
for l in line_items:
    # normalize numeric fields
    try:
        disc = float(l.get('Discount') or 0)
    except:
        disc = 0.0
    try:
        qty = float(l.get('Quantity') or 0)
    except:
        qty = 0.0
    try:
        up = float(l.get('UnitPrice') or 0)
    except:
        up = 0.0
    if disc > 10:
        suspicious.append({'type':'excessive_discount','discount':disc,'line':l})
    if qty > 30:
        suspicious.append({'type':'excessive_quantity','quantity':qty,'line':l})

# Search knowledge articles for rules mentioning discount thresholds or quantity limits
keywords = ['discount', 'approval', 'approval required', 'quantity', 'maximum', 'max', 'limit', 'discount_limit', 'discount limit', 'price', 'pricing policy', 'pricebook', 'discounts']
matching_articles = []
for a in k_articles:
    text = ' '.join([str(a.get('title','')), str(a.get('faq_answer__c','')), str(a.get('summary',''))]).lower()
    matches = [kw for kw in keywords if kw in text]
    if matches:
        matching_articles.append({'id': a.get('id'), 'title': a.get('title'), 'matches': matches, 'summary': a.get('summary')})

# Narrow down to articles that mention discount specifically or quantity/limit
discount_articles = [m for m in matching_articles if 'discount' in m['matches'] or 'discounts' in m['matches'] or 'discount limit' in m['matches']]
quantity_articles = [m for m in matching_articles if 'quantity' in m['matches'] or 'maximum' in m['matches'] or 'max' in m['matches'] or 'limit' in m['matches']]

result = {
    'quote_id': quote_id,
    'line_items_count': len(line_items),
    'suspicious_flags': suspicious,
    'discount_related_articles': discount_articles[:10],
    'quantity_related_articles': quantity_articles[:10]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_f5TulKsCWfNiIQjYh8AEuu85': [], 'var_call_Aw7RtuPc88ZOg87xkD70HTGs': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_call_WT6oGoEwZJI1WaCVzele8Lo8': [], 'var_call_IqZD5B4iS32EkLOdzIlxjcrp': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_xjrGc45h0QyzaOlZQUClsKeE': 'file_storage/call_xjrGc45h0QyzaOlZQUClsKeE.json'}

exec(code, env_args)
