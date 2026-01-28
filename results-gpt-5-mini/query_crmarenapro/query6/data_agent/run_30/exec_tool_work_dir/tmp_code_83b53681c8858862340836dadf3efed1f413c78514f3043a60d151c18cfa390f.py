code = """import json, re
# Load variables
qlines = var_call_JhgHx9vHefskldJcuPxwAlhm
products = var_call_uzcGifIxJdLrqSLtfUHHb6Tj
knowledge = var_call_h621moWjFVvD31htUJxF7UQ8

# Ensure types
if isinstance(qlines, str):
    qlines = json.loads(qlines)
if isinstance(products, str):
    products = json.loads(products)
if isinstance(knowledge, str):
    knowledge = json.loads(knowledge)

prod_map = {p['Id']: p.get('Name','').strip() for p in products}

limits_article = None
for k in knowledge:
    title = k.get('title','').strip().lower()
    if 'product quantity limits' in title:
        limits_article = k
        break

violation_article_id = None
limit_map = {}
if limits_article:
    faq = limits_article.get('faq_answer__c','')
    # parse product limits lines like '**Name** - ... up to N units'
    # simplified parsing by known list in the article: lines with ' - ' and 'up to N units' or 'maximum of N units'
    lines = faq.split('\n')
    for line in lines:
        line = line.strip()
        # match patterns
        m = re.match(r"\*\*(.*?)\*\*.*?(?:up to|maximum of|can purchase up to|limited to|limited to\s*)(\d+)", line, re.IGNORECASE)
        if m:
            pname = m.group(1).strip()
            lim = int(m.group(2))
            limit_map[pname] = lim
    # fallback: known mapping from preview
    if not limit_map:
        limit_map = {
            'AIOptics Vision':20,
            'CloudLink Designer':15,
            'CollabDesign Studio':25,
            'CryptGuard Module':10,
            'EduFlow Academy':5,
            'SecuManage Pro':30,
            'SecureAnalytics Pro':12,
            'IntegrGuard Secure':8,
            'CloudInnovate Space':18,
            'AI DesignShift':7
        }

# Check each quote line item
if limit_map:
    for q in qlines:
        pid = q.get('Product2Id','')
        qty = 0
        try:
            qty = float(q.get('Quantity',0))
        except:
            qty = 0
        pname = prod_map.get(pid,'').strip()
        if pname and pname in limit_map:
            if qty > limit_map[pname]:
                violation_article_id = limits_article.get('id')
                break

# Print result
print("__RESULT__:")
print(json.dumps(violation_article_id if violation_article_id else ''))"""

env_args = {'var_call_8MX8CLBBOUHCma04VcXApGAu': [], 'var_call_J04Uzj30pcHdIVN55ypZeJ9L': 'file_storage/call_J04Uzj30pcHdIVN55ypZeJ9L.json', 'var_call_hD916T3ylJMI1FOQX7MJH8c6': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'Name': 'NeoGreen EDA Expansion Quote', 'Status': 'Needs Review'}], 'var_call_JhgHx9vHefskldJcuPxwAlhm': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_XPwr38YtHJNTjHk8ySl5y8YH': 'file_storage/call_XPwr38YtHJNTjHk8ySl5y8YH.json', 'var_call_jAJ2y0N2nOEToOzuKmDf1rCj': [{'Id': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Pi5IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'UnitPrice': '399.99'}], 'var_call_uzcGifIxJdLrqSLtfUHHb6Tj': [{'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}], 'var_call_h621moWjFVvD31htUJxF7UQ8': 'file_storage/call_h621moWjFVvD31htUJxF7UQ8.json'}

exec(code, env_args)
