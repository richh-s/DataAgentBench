code = """import json, re

# Load KB from storage path
kb_path = var_call_EJsq60vhGWHqFw5CXtxkiCYx
with open(kb_path, 'r', encoding='utf-8') as f:
    kb = json.load(f)

# Load quote and quote line items
quote = None
if isinstance(var_call_BIrHCzMM2apIpXK477mn3kv7, list) and len(var_call_BIrHCzMM2apIpXK477mn3kv7) > 0:
    quote = var_call_BIrHCzMM2apIpXK477mn3kv7[0]
qlis = var_call_99zQi9M6WgJ9EQnIRgavPUSz

# Compute max discount from quote line items
discounts = []
for li in qlis:
    d = li.get('Discount')
    if d is None:
        discounts.append(0.0)
        continue
    try:
        discounts.append(float(d))
    except Exception:
        sd = str(d).strip().replace('%','')
        try:
            discounts.append(float(sd))
        except Exception:
            discounts.append(0.0)
max_discount = max(discounts) if discounts else 0.0

# Compile regex patterns
p_above = re.compile(r"discounts? (?:above|greater than|over|>)\s*(\d{1,3})\s*%")
p_require = re.compile(r"require approval for discounts?.*?(\d{1,3})\s*%")
p_max = re.compile(r"(?:maximum|max) discount(?: is|:)?\s*(\d{1,3})\s*%")
p_up_to = re.compile(r"discounts? up to\s*(\d{1,3})\s*%")
p_no = re.compile(r"no discount|discounts not allowed")
p_percent = re.compile(r"(\d{1,3})\s*%")

violation_id = None

for art in kb:
    # Combine relevant fields
    parts = []
    for k in ('title','summary','faq_answer__c','urlname'):
        v = art.get(k) or ''
        parts.append(str(v))
    full = ' '.join(parts).lower()

    if 'discount' in full or 'approval' in full:
        # No discounts at all
        if p_no.search(full):
            if max_discount > 0.0:
                violation_id = art.get('id')
                break
        m = p_above.search(full)
        if m:
            try:
                thresh = float(m.group(1))
                if max_discount > thresh:
                    violation_id = art.get('id')
                    break
            except:
                pass
        m = p_require.search(full)
        if m:
            try:
                thresh = float(m.group(1))
                if max_discount > thresh:
                    violation_id = art.get('id')
                    break
            except:
                pass
        m = p_max.search(full)
        if m:
            try:
                allowed = float(m.group(1))
                if max_discount > allowed:
                    violation_id = art.get('id')
                    break
            except:
                pass
        m = p_up_to.search(full)
        if m:
            try:
                allowed = float(m.group(1))
                if max_discount > allowed:
                    violation_id = art.get('id')
                    break
            except:
                pass
        # If discounts mentioned with any percent, assume that percent is a policy threshold
        percents = [float(x) for x in p_percent.findall(full)]
        if percents:
            # choose first percent found
            pct = percents[0]
            if max_discount > pct:
                violation_id = art.get('id')
                break

# If still no violation, check for generic approval phrases with percent numbers
if not violation_id:
    p_generic = re.compile(r"approval required for.*?(\d{1,3})\s*%|authorize.*?(\d{1,3})\s*%|approval.*?(\d{1,3})\s*%")
    for art in kb:
        full = ' '.join([str(art.get(k,'')).lower() for k in ('title','summary','faq_answer__c')])
        m = p_generic.search(full)
        if m:
            nums = [g for g in m.groups() if g]
            if nums:
                try:
                    thresh = float(nums[0])
                    if max_discount > thresh:
                        violation_id = art.get('id')
                        break
                except:
                    pass

# Output result
res = violation_id if violation_id is not None else None
print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_call_EJsq60vhGWHqFw5CXtxkiCYx': 'file_storage/call_EJsq60vhGWHqFw5CXtxkiCYx.json', 'var_call_99zQi9M6WgJ9EQnIRgavPUSz': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_BIrHCzMM2apIpXK477mn3kv7': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_iCRR9CVS1yQWDvjkPid5p9PW': [], 'var_call_ya3PdpbQn96mzYZimt4haaRN': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_jNvMeUixr0AFqsXYKbq9d4tJ': []}

exec(code, env_args)
