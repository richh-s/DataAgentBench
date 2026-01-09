code = """import json, pandas as pd

qlis = pd.DataFrame(var_call_HRbjA4e5AG1LazdQwQb1lUMa)
pbe_sub = pd.DataFrame(var_call_aPw0uemmwmpkLGNlZDVHh1UE)

for c in ['Product2Id','PricebookEntryId']:
    qlis[c] = qlis[c].astype(str).str.strip().str.lstrip('#')
for c in ['Product2Id','PricebookEntryId']:
    pbe_sub[c] = pbe_sub[c].astype(str).str.strip().str.lstrip('#')

for c in ['Quantity','UnitPrice','Discount','TotalPrice','ListUnitPrice']:
    if c in qlis.columns:
        qlis[c] = pd.to_numeric(qlis[c], errors='coerce')
    if c in pbe_sub.columns:
        pbe_sub[c] = pd.to_numeric(pbe_sub[c], errors='coerce')

m = qlis.merge(pbe_sub, on='PricebookEntryId', how='left', suffixes=('','_ref'))

# identify which lines violate quantity limits article (if any product exceeds its max from article)
# Parse quantity limits from article text
import re

path = var_call_YCt0svQDZXBzS0ulqSRHcM4w
if isinstance(path, str):
    with open(path,'r',encoding='utf-8') as f:
        arts = json.load(f)
else:
    arts = path
art_map = {a['title'].strip(): a for a in arts}
qty_art = None
for a in arts:
    if a.get('title','').lower().strip().startswith('product quantity limits'):
        qty_art = a
        break

limits = {}
if qty_art:
    txt = qty_art.get('faq_answer__c','')
    # patterns like **Product** - Customers can purchase up to 20 units per order.
    for prod, lim in re.findall(r"\*\*(.*?)\*\*\s*-\s*Customers can purchase up to\s*(\d+)\s*units", txt):
        limits[prod.strip().lower()] = int(lim)
    for prod, lim in re.findall(r"\*\*(.*?)\*\*\s*-\s*A maximum of\s*(\d+)\s*units", txt):
        limits[prod.strip().lower()] = int(lim)
    for prod, lim in re.findall(r"\*\*(.*?)\*\*\s*-\s*Each order is limited to\s*(\d+)\s*units", txt):
        limits[prod.strip().lower()] = int(lim)
    for prod, lim in re.findall(r"\*\*(.*?)\*\*\s*-\s*For .*?, customers can order up to\s*(\d+)\s*units", txt):
        limits[prod.strip().lower()] = int(lim)
    for prod, lim in re.findall(r"\*\*(.*?)\*\*\s*-\s*Orders can include up to\s*(\d+)\s*units", txt):
        limits[prod.strip().lower()] = int(lim)
    for prod, lim in re.findall(r"\*\*(.*?)\*\*\s*-\s*Limited to\s*(\d+)\s*units", txt):
        limits[prod.strip().lower()] = int(lim)
    for prod, lim in re.findall(r"\*\*(.*?)\*\*\s*-\s*Users can order up to\s*(\d+)\s*units", txt):
        limits[prod.strip().lower()] = int(lim)
    for prod, lim in re.findall(r"\*\*(.*?)\*\*\s*-\s*This dynamic product is available in quantities of up to\s*(\d+)\s*units", txt):
        limits[prod.strip().lower()] = int(lim)
    for prod, lim in re.findall(r"\*\*(.*?)\*\*\s*-\s*Clients may order a maximum of\s*(\d+)\s*units", txt):
        limits[prod.strip().lower()] = int(lim)

viol_qty = False
if limits:
    m['ProductName_lc'] = m['ProductName'].astype(str).str.strip().str.lower()
    m['limit'] = m['ProductName_lc'].map(limits)
    viol_qty = bool(((m['limit'].notna()) & (m['Quantity'] > m['limit'])).any())

# Determine violation based on found: CollabDesign Studio quantity 35, article limit 25.
answer_id = qty_art['id'].strip().lstrip('#') if viol_qty and qty_art else None

print('__RESULT__:')
print(json.dumps({'viol_qty': viol_qty, 'answer_id': answer_id}))"""

env_args = {'var_call_HRbjA4e5AG1LazdQwQb1lUMa': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_GMxuzuDNQ1j0Rq6RAUzqoaNO': [{'PricebookEntryId': '01uWt0000027P5NIAU', 'ListUnitPrice': '599.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '#01tWt000006hV58IAE', 'ProductName': 'SecureFlow Suite'}, {'PricebookEntryId': '#01uWt0000027P6zIAE', 'ListUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'PricebookEntryId': '01uWt0000027P8cIAE', 'ListUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech'}, {'PricebookEntryId': '01uWt0000027PDRIA2', 'ListUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVBZIA2', 'ProductName': 'EduTech Lab'}, {'PricebookEntryId': '01uWt0000027PIIIA2', 'ListUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVI1IAM', 'ProductName': 'AIOptics Vision'}, {'PricebookEntryId': '#01uWt0000027PN7IAM', 'ListUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hPfgIAE', 'ProductName': 'EcoPower Convert'}, {'PricebookEntryId': '#01uWt0000027POjIAM', 'ListUnitPrice': '299.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVMrIAM', 'ProductName': 'TrainEDU Suite'}, {'PricebookEntryId': '#01uWt0000027PTaIAM', 'ListUnitPrice': '459.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVUvIAM', 'ProductName': 'OptiEnergy Suite'}, {'PricebookEntryId': '01uWt0000027PVBIA2', 'ListUnitPrice': '339.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVQ5IAM', 'ProductName': 'CircuitSync Pro'}, {'PricebookEntryId': '#01uWt0000027PWnIAM', 'ListUnitPrice': '429.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVQ6IAM', 'ProductName': 'VeriSim Express  '}, {'PricebookEntryId': '01uWt0000027Pa1IAE', 'ListUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVTJIA2', 'ProductName': 'IntegrGuard Secure'}, {'PricebookEntryId': '01uWt0000027PerIAE', 'ListUnitPrice': '559.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVZlIAM', 'ProductName': 'SecuManage Pro  '}, {'PricebookEntryId': '01uWt0000027PgTIAU', 'ListUnitPrice': '349.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVbNIAU', 'ProductName': 'EnergyReduce Pro'}, {'PricebookEntryId': '01uWt0000027PjhIAE', 'ListUnitPrice': '549.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVebIAE', 'ProductName': 'CircuitAI Innovator'}, {'PricebookEntryId': '#01uWt0000027Pq9IAE', 'ListUnitPrice': '429.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVjRIAU', 'ProductName': 'Workflow Genius'}, {'PricebookEntryId': '#01uWt0000027PtNIAU', 'ListUnitPrice': '399.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVmfIAE', 'ProductName': 'EduTech Advance'}, {'PricebookEntryId': '01uWt0000027PtOIAU', 'ListUnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVwLIAU', 'ProductName': 'SimulateX Edge'}, {'PricebookEntryId': '01uWt0000027Q1RIAU', 'ListUnitPrice': '579.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVujIAE', 'ProductName': 'CyberShield Core'}, {'PricebookEntryId': '01uWt0000027Q4fIAE', 'ListUnitPrice': '299.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hVjSIAU', 'ProductName': 'InnoTrain Hub'}, {'PricebookEntryId': '01uWt0000027Q6HIAU', 'ListUnitPrice': '619.99', 'Pricebook2Id': '01sWt000000imiTIAQ', 'PricebookName': 'Standard Price Book', 'Product2Id': '01tWt000006hUtqIAE', 'ProductName': 'SecureTrack Pro '}], 'var_call_CF4PlOrUhGEdY5ozBvcHBrLo': 'file_storage/call_CF4PlOrUhGEdY5ozBvcHBrLo.json', 'var_call_9opEvtBvhXl1iY1JG2RRpqCr': [], 'var_call_lXrhtAXF27NFA4zX7E93hmPB': {'suspect_count': 3, 'top_candidates': [{'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'score': 3}, {'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers', 'score': 3}, {'id': '#ka0Wt000000EpSUIA0', 'title': 'TechPulse Solution Volume-Based Installation Timeline Policy', 'score': 2}, {'id': 'ka0Wt000000EpDzIAK', 'title': 'Advanced Security Measures in Electronic Design', 'score': 1}, {'id': '#ka0Wt000000EnwvIAC', 'title': 'Product Quantity Limits   ', 'score': 1}, {'id': 'ka0Wt000000EmklIAC', 'title': 'Advancing PCB Design with AI and Eco-Friendly Solutions', 'score': 1}, {'id': 'ka0Wt000000EoOLIA0', 'title': 'Effective Optical Design: Achieving Efficiency and Innovation with AI ', 'score': 1}, {'id': 'ka0Wt000000EnyXIAS', 'title': 'TechPulse Solutions: Defining Values that Drive Innovation and Success', 'score': 1}, {'id': 'ka0Wt000000EoPxIAK', 'title': 'Precision in Circuit Design: Addressing Verification Software Challenges', 'score': 1}, {'id': '#ka0Wt000000EmkkIAC', 'title': 'Advanced Data Protection with SecuManage Pro   ', 'score': 1}, {'id': 'ka0Wt000000Ep7WIAS', 'title': 'Enhancing Workflow Security with CryptGuard Module', 'score': 1}, {'id': 'ka0Wt000000Eo8EIAS', 'title': 'Seamless Simulation Integration with TechPulse AI Tools', 'score': 1}, {'id': 'ka0Wt000000EpaXIAS', 'title': 'Scaling Security Solutions with CryptSecure Core', 'score': 1}, {'id': 'ka0Wt000000Ens5IAC', 'title': 'Mandatory Bundles for Quotes', 'score': 1}, {'id': 'ka0Wt000000EpNgIAK', 'title': 'Dynamic Security Strategies with SecuManage Pro', 'score': 1}, {'id': 'ka0Wt000000EpdlIAC', 'title': 'CryptGuard Module: Pioneering Data Integrity   ', 'score': 1}, {'id': 'ka0Wt000000EowFIAS', 'title': 'Competitor: Adaptive Design Solutions', 'score': 0}, {'id': 'ka0Wt000000EpXNIA0', 'title': 'Competitor: Quantum Circuits Inc', 'score': 0}, {'id': 'ka0Wt000000EptuIAC', 'title': 'Streamlining Workflow with AI-Powered Circuit Design', 'score': 0}, {'id': 'ka0Wt000000EpXLIA0', 'title': 'Optimizing Power Utilization Across EDA Projects   ', 'score': 0}]}, 'var_call_YCt0svQDZXBzS0ulqSRHcM4w': 'file_storage/call_YCt0svQDZXBzS0ulqSRHcM4w.json', 'var_call_aPw0uemmwmpkLGNlZDVHh1UE': [{'PricebookEntryId': '01uWt0000027P8cIAE', 'ListUnitPrice': '529.99', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech'}, {'PricebookEntryId': '01uWt0000027PADIA2', 'ListUnitPrice': '299.99', 'Product2Id': '01tWt000006hPffIAE', 'ProductName': 'DevVision IDE'}, {'PricebookEntryId': '01uWt0000027Pi5IAE', 'ListUnitPrice': '399.99', 'Product2Id': '01tWt000006hVczIAE', 'ProductName': 'CollabDesign Studio'}]}

exec(code, env_args)
