code = """import json, re
# load tool results from storage variables
quotes = var_call_EAZuqBIpNLL3mHseVwhqsIei
qlis = var_call_MNwVnZ0aQWxpfIRlZmLZLIp9
# knowledge articles file path
kav_path = var_call_solDY72XvdnwcKmY2QOGkLBE

def load_json_path(p):
    with open(p, 'r', encoding='utf-8') as f:
        return json.load(f)

kavs = load_json_path(kav_path)

# compute quote totals
def to_float(x):
    try:
        return float(x)
    except:
        return None

line_totals = [to_float(item.get('TotalPrice')) for item in qlis]
line_discounts = [to_float(item.get('Discount')) for item in qlis]
line_unit = [to_float(item.get('UnitPrice')) for item in qlis]
line_qty = [to_float(item.get('Quantity')) for item in qlis]
quote_total = sum([v for v in line_totals if v is not None])

# find policy articles mentioning discounts, approval, setup, pricing
keywords = ['discount', 'approval', 'approve', 'setup', 'setup fee', 'pricing', 'price', 'discounts', 'volume']
candidate_articles = []
for a in kavs:
    text = ' '.join([str(a.get('title','') or ''), str(a.get('summary','') or ''), str(a.get('faq_answer__c','') or '')]).lower()
    if any(k in text for k in keywords):
        candidate_articles.append({'id': a.get('id'), 'title': a.get('title'), 'text': text})

# analyze candidate articles for rules about discount thresholds requiring approval
violation_article_id = None
# check if any article specifies a max discount without approval, or that discounts above X% require approval
for art in candidate_articles:
    t = art['text']
    # find percentage numbers in context of approval
    # pattern: discounts above 10% require approval
    m = re.search(r"discounts? (?:above|over|greater than|more than|exceeding) (\d{1,3})%.*approval|approval.*discounts? (?:above|over|>(\d{1,3}))%", t)
    if m:
        # extract number
        nums = re.findall(r"(\d{1,3})%", t)
        if nums:
            # take the first percentage as threshold
            try:
                threshold = float(nums[0])
            except:
                threshold = None
            if threshold is not None:
                # if any line discount exceeds threshold => violation
                for d in line_discounts:
                    if d is not None and d > threshold:
                        violation_article_id = art['id']
                        break
    if violation_article_id:
        break

# If no explicit approval-percentage found, look for volume-based discount policy that prescribes tiers
if not violation_article_id:
    for art in candidate_articles:
        if 'volume-based discounts' in (art.get('title') or '').lower() or 'volume-based discounts' in art['text']:
            # parse tiers in text: look for lines like '5% Discount for Purchases Over $5' -> interpret as tiers apply to total purchase
            percents = re.findall(r"(\d{1,3})%.*over \$?(\d+[\d,\.]*)", art['text'])
            # convert
            tiers = []
            for p,c in percents:
                try:
                    tiers.append((float(p), float(c.replace(',',''))))
                except:
                    pass
            # find max allowed discount based on total quote
            if tiers:
                # find applicable tier for quote_total
                # Note: the policy uses small dollar numbers, but assume same unit as quote
                applicable = None
                for perc, amount in sorted(tiers, key=lambda x: x[1]):
                    if quote_total >= amount:
                        applicable = perc
                # If any line discount exceeds applicable perc, violation
                if applicable is not None:
                    for d in line_discounts:
                        if d is not None and d > applicable:
                            violation_article_id = art['id']
                            break
        if violation_article_id:
            break

# As fallback, look for articles that state pricing must be transparent or prohibit hidden discounts/setup fees
if not violation_article_id:
    for art in candidate_articles:
        if 'requires approval' in art['text'] or 'require approval' in art['text'] or 'approval required' in art['text']:
            # if any discount >=10% mark potential violation if policy says approval needed for discounts
            for d in line_discounts:
                if d is not None and d >= 10.0:
                    violation_article_id = art['id']
                    break
        if violation_article_id:
            break

# Prepare output: if violation_article_id set, return it; else None
result = violation_article_id if violation_article_id else None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_EAZuqBIpNLL3mHseVwhqsIei': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_MNwVnZ0aQWxpfIRlZmLZLIp9': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_e5m3kUBfMysgxSWDawNwAh2T': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1', 'UnitPrice': '499.99'}], 'var_call_8R44qF6FRsvCWQ050tjONEwz': 'file_storage/call_8R44qF6FRsvCWQ050tjONEwz.json', 'var_call_solDY72XvdnwcKmY2QOGkLBE': 'file_storage/call_solDY72XvdnwcKmY2QOGkLBE.json'}

exec(code, env_args)
