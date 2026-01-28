code = """import json, re
# Load variables from storage
quote_line_items = var_call_GNZ4YqhK6BSiDSN6TLlA9DF7
products = var_call_Zjq3xAsWgjEtORyz6bJHYUXW
# knowledge query result stored in a file path string or list
kvar = var_call_XS9gSXkXsfBRx1pL7zNytRhe
if isinstance(kvar, str):
    with open(kvar, 'r', encoding='utf-8') as f:
        knowledge = json.load(f)
else:
    knowledge = kvar

# Build product id -> name map, normalize ids by stripping leading '#'
prod_map = {}
for p in products:
    pid = p.get('Id','')
    pid_norm = pid.lstrip('#')
    prod_map[pid_norm] = p.get('Name','').strip()

# Find the Product Quantity Limits article
pq_article = None
for a in knowledge:
    title = a.get('title','') or ''
    if 'product quantity limits' in title.lower():
        pq_article = a
        break

violating_article_id = None
if pq_article:
    text = (pq_article.get('faq_answer__c') or '')
    # For each product, try to extract limit from the article text
    limits = {}
    for pid, name in prod_map.items():
        # build regex to find e.g. 'CollabDesign Studio - Each order is limited to 25 units.'
        pattern = re.compile(re.escape(name) + r"[\s\S]{0,200}?([0-9]{1,3})\s*(?:units|unit)", re.IGNORECASE)
        m = pattern.search(text)
        if m:
            try:
                limits[name] = int(m.group(1))
            except:
                pass
    # Now check quote line items for violations
    for qli in quote_line_items:
        q_pid = qli.get('Product2Id','').lstrip('#')
        q_qty_raw = qli.get('Quantity')
        try:
            q_qty = int(float(q_qty_raw))
        except:
            continue
        pname = prod_map.get(q_pid)
        if pname and pname in limits:
            if q_qty > limits[pname]:
                violating_article_id = pq_article.get('id')
                break

# Fallback: if no parsed limits but we know by name presence in article
if not violating_article_id and pq_article:
    # check if any product name appears in article and quantity numeric > any number in article overall for that product
    text = pq_article.get('faq_answer__c') or ''
    for qli in quote_line_items:
        q_pid = qli.get('Product2Id','').lstrip('#')
        q_qty_raw = qli.get('Quantity')
        try:
            q_qty = int(float(q_qty_raw))
        except:
            continue
        pname = prod_map.get(q_pid)
        if pname and pname.lower() in text.lower():
            # extract any number following the product name
            pattern = re.compile(re.escape(pname) + r"[\s\S]{0,200}?([0-9]{1,3})", re.IGNORECASE)
            m = pattern.search(text)
            if m:
                try:
                    limit = int(m.group(1))
                    if q_qty > limit:
                        violating_article_id = pq_article.get('id')
                        break
                except:
                    pass

# Prepare output
out = violating_article_id if violating_article_id is not None else ''
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_GCY6DmpaNmn4KbPFgZcAclFd': [], 'var_call_9jjD5tOluAg8E3RLit4ieQHn': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Status': 'Needs Review'}], 'var_call_GNZ4YqhK6BSiDSN6TLlA9DF7': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_sg0ddkteHuN548HJb2Twz8CE': [{'Id': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Pi5IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'UnitPrice': '399.99'}], 'var_call_Zjq3xAsWgjEtORyz6bJHYUXW': [{'Id': '01tWt000006hPffIAE', 'Name': 'DevVision IDE', 'Description': 'Integrated development environment with intuitive coding and debugging capabilities.', 'IsActive': '1', 'External_ID__c': 'Integrated Development Environments,Educational and Training Platforms_6'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.', 'IsActive': '1', 'External_ID__c': 'AI-Powered Circuit Design Tools,Customizable Workflow Automation_5'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio', 'Description': 'Enhanced design collaboration platform offering real-time editing and feedback.', 'IsActive': '1', 'External_ID__c': 'Cloud-Based Design Collaboration,Integrated Development Environments_30'}], 'var_call_HxZUG1MNLdrNo3ad7arCbt4B': 'file_storage/call_HxZUG1MNLdrNo3ad7arCbt4B.json', 'var_call_XS9gSXkXsfBRx1pL7zNytRhe': 'file_storage/call_XS9gSXkXsfBRx1pL7zNytRhe.json'}

exec(code, env_args)
