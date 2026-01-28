code = """import json
# Load knowledge articles from the provided file path
path = var_call_mRydcSM7vAxw2Zw4c1icyM9E
with open(path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Load quote line items
qli = var_call_gMwhwsEvDFZIeFR4qcVYvunG

# Convert numbers
for item in qli:
    try:
        item['Quantity'] = float(item.get('Quantity') if item.get('Quantity') is not None else 0)
        item['UnitPrice'] = float(item.get('UnitPrice') if item.get('UnitPrice') is not None else 0)
        item['Discount'] = float(item.get('Discount') if item.get('Discount') is not None else 0)
        item['TotalPrice'] = float(item.get('TotalPrice') if item.get('TotalPrice') is not None else 0)
    except:
        pass

# Gather potential violations
violations = []
# Check pricebook entry matching unit price
pbe = var_call_EdLwlPGeibhTIDeq4ibcnroa
pbe_map = {r['Id']: r for r in pbe}

# Check product existence
prod = var_call_yLTOqo930uvbvetPabQJYfK0
prod_ids = {r['Id'] for r in prod}

for item in qli:
    reasons = []
    # missing pricebook entry
    if item.get('PricebookEntryId') not in pbe_map:
        reasons.append('Missing or invalid PricebookEntry')
    else:
        # unit price mismatch
        pbe_price = float(pbe_map[item['PricebookEntryId']]['UnitPrice'])
        if abs(pbe_price - item['UnitPrice']) > 0.001:
            reasons.append('UnitPrice does not match PricebookEntry')
    # product not found or inactive
    pid = item.get('Product2Id')
    if pid not in prod_ids:
        reasons.append('Product not found in Product2')
    else:
        # check if active
        for p in prod:
            if p['Id'] == pid and p.get('IsActive') in ('0','False','false',''):
                reasons.append('Product inactive')
    # excessive discount (>10% rule assumed)
    if item.get('Discount', 0) > 10.0:
        reasons.append('Discount exceeds allowed threshold')
    # large quantity rule (>30) as potential violation
    if item.get('Quantity', 0) > 30:
        reasons.append('Quantity exceeds allowed maximum without approval')
    if reasons:
        violations.append({'QuoteLineItemId': item['Id'], 'reasons': reasons, 'item': item})

# Now search knowledge articles for matching rules
keywords_map = {
    'Missing or invalid PricebookEntry': ['pricebook entry','pricebookentry','pricebook','unitprice','unit price','pricing entry','price book entry'],
    'UnitPrice does not match PricebookEntry': ['unit price','unitprice','pricebook entry','pricing mismatch','do not change unit price','pricing policy'],
    'Product not found in Product2': ['product not found','product2','inactive product','product is inactive','product not found in Product2'],
    'Product inactive': ['inactive','product inactive','is inactive','not active','IsActive'],
    'Discount exceeds allowed threshold': ['discount','discount approval','discounts greater than','maximum discount','approval required for discounts','discount policy'],
    'Quantity exceeds allowed maximum without approval': ['quantity','maximum quantity','order quantity','bulk order','approval for quantity','maximum units']
}

matched_articles = []
for v in violations:
    for reason in v['reasons']:
        kws = keywords_map.get(reason, [])
        for art in articles:
            text = ' '.join([str(art.get('title','')).lower(), str(art.get('faq_answer__c','')).lower(), str(art.get('summary','')).lower()])
            for kw in kws:
                if kw in text:
                    matched_articles.append({'QuoteLineItemId': v['QuoteLineItemId'], 'reason': reason, 'article_id': art['id'], 'article_title': art.get('title')})
                    break

# If no matched articles found via keywords, attempt broader search for articles containing 'discount' or 'price' or 'quantity'
if not matched_articles:
    for v in violations:
        for art in articles:
            text = ' '.join([str(art.get('title','')).lower(), str(art.get('faq_answer__c','')).lower(), str(art.get('summary','')).lower()])
            if any(k in text for k in ['discount','pricebook','unit price','quantity','approval','product inactive','pricing']):
                matched_articles.append({'QuoteLineItemId': v['QuoteLineItemId'], 'reason': 'General match', 'article_id': art['id'], 'article_title': art.get('title')})

# Deduplicate article ids and prefer exact matches for discount or quantity
article_ids = []
for m in matched_articles:
    if m['article_id'] not in article_ids:
        article_ids.append(m['article_id'])

# Prepare output: If there is a violation related to discount or quantity, prefer that article id; else return first matched id
preferred = None
for m in matched_articles:
    if 'Discount exceeds' in m['reason'] or 'Quantity exceeds' in m['reason']:
        preferred = m['article_id']
        break
if not preferred and article_ids:
    preferred = article_ids[0]

# If still no match, return an explanatory short string
if not preferred:
    output = json.dumps(None)
else:
    output = json.dumps(preferred)

print("__RESULT__:")
print(output)"""

env_args = {'var_call_D8dFQAtS5L2zWhdVXEhbBkhf': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_call_5z43wReKPSADLbV9H0K9n0ae': [], 'var_call_gMwhwsEvDFZIeFR4qcVYvunG': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_mRydcSM7vAxw2Zw4c1icyM9E': 'file_storage/call_mRydcSM7vAxw2Zw4c1icyM9E.json', 'var_call_EdLwlPGeibhTIDeq4ibcnroa': [{'Id': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Pi5IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'UnitPrice': '399.99'}], 'var_call_yLTOqo930uvbvetPabQJYfK0': [{'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.', 'IsActive': '1', 'External_ID__c': 'AI-Powered Circuit Design Tools,Customizable Workflow Automation_5'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio', 'Description': 'Enhanced design collaboration platform offering real-time editing and feedback.', 'IsActive': '1', 'External_ID__c': 'Cloud-Based Design Collaboration,Integrated Development Environments_30'}]}

exec(code, env_args)
