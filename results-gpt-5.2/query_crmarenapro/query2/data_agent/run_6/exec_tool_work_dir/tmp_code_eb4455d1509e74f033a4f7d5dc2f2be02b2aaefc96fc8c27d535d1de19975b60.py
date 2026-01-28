code = """import json, re

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

quote = load_maybe_path(var_call_QRgAdhJVfpt416CADsTsN4Zz)
qlis = load_maybe_path(var_call_h3f17QycqsLALUs7lW89Gpdn)
products = load_maybe_path(var_call_UEboiWQ22JwQcRyQErgHEC7l)
kas = load_maybe_path(var_call_WweI1BBFS8wzAP3arfPFlOEZ)

for r in qlis:
    for k in ['Quantity','UnitPrice','Discount','TotalPrice']:
        try:
            r[k] = float(r[k])
        except Exception:
            pass

prod_map = {str(p['Id']).replace('#','').strip(): p for p in products}

setup_keywords = ['setup','implementation','onboarding','integration fee','install','deployment']
setup_lines = []
for r in qlis:
    pid = str(r.get('Product2Id','')).replace('#','').strip()
    p = prod_map.get(pid)
    text = ''
    if p:
        text = (str(p.get('Name',''))+' '+str(p.get('Description',''))).lower()
    if any(kw in text for kw in setup_keywords):
        setup_lines.append(r)

policy_keywords = ['quote','approval','discount','setup','implementation','onboarding','fee','pricing','policy']
scored = []
for ka in kas:
    blob = (str(ka.get('title',''))+' '+str(ka.get('summary',''))+' '+str(ka.get('faq_answer__c',''))).lower()
    score = sum(blob.count(k) for k in policy_keywords)
    scored.append((score, ka.get('id'), blob))
scored.sort(reverse=True)

max_discount = max([r.get('Discount',0) for r in qlis] or [0])
violation_id = None

cap_re = re.compile(r'(max(?:imum)?|up to|no more than|not exceed|cannot exceed)\s*(\d{1,2}(?:\.\d+)?)\s*%')
req_re = re.compile(r'(over|greater than|above)\s*(\d{1,2}(?:\.\d+)?)\s*%[^\.;\n]{0,120}(requires|need|must)[^\.;\n]{0,60}approval')

for score, ka_id, blob in scored[:200]:
    if ka_id is None:
        continue
    if ('discount' not in blob) and ('setup' not in blob) and ('fee' not in blob) and ('pricing' not in blob):
        continue
    caps = [float(m.group(2)) for m in cap_re.finditer(blob)]
    if caps and max_discount > min(caps):
        violation_id = ka_id
        break
    reqs = [float(m.group(2)) for m in req_re.finditer(blob)]
    if reqs and max_discount > min(reqs):
        violation_id = ka_id
        break

if violation_id is None and setup_lines:
    for score, ka_id, blob in scored[:200]:
        if ka_id is None:
            continue
        if ('setup' in blob or 'implementation' in blob or 'onboarding' in blob) and ('approval' in blob):
            violation_id = ka_id
            break

print('__RESULT__:')
print(json.dumps(violation_id))"""

env_args = {'var_call_QRgAdhJVfpt416CADsTsN4Zz': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_h3f17QycqsLALUs7lW89Gpdn': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_UEboiWQ22JwQcRyQErgHEC7l': 'file_storage/call_UEboiWQ22JwQcRyQErgHEC7l.json', 'var_call_WweI1BBFS8wzAP3arfPFlOEZ': 'file_storage/call_WweI1BBFS8wzAP3arfPFlOEZ.json'}

exec(code, env_args)
