code = """import json
# Load previously stored query results from storage keys
ql_items = var_call_jfEUkoH7QckUOwDxFeNKpfWL  # QuoteLineItem rows
price_entries = var_call_QImgvfgioj3lI2H7TFTTVFtz  # PricebookEntry rows
products = var_call_PjPsiOaXcoz7OxsjVyAzp894  # Product2+Pricebook entries
knowledge = var_call_OCCEvzN1vAiHhbANaHwgWirW  # selected knowledge articles

# Convert quantities and unit prices to numeric, detect issues
issues = []
for q in ql_items:
    qid = q['Id']
    qty = None
    up = None
    disc = None
    try:
        qty = float(q.get('Quantity') or 0)
    except:
        qty = None
    try:
        up = float(q.get('UnitPrice') or 0)
    except:
        up = None
    try:
        disc = float(q.get('Discount') or 0)
    except:
        disc = 0.0
    # find corresponding pricebook entry
    pbe = next((p for p in price_entries if p['Id'] == q.get('PricebookEntryId')), None)
    if pbe:
        pb_up = float(pbe.get('UnitPrice') or 0)
    else:
        pb_up = None
    # check for discount > 0 and large quantity
    if disc > 0:
        issues.append({'QuoteLineItemId': qid, 'issue': 'Discount applied', 'discount': disc, 'knowledge_id': 'ka0Wt000000Eq0MIAS'})
    # if quantity > 30 and there's a 'Product Quantity Limits' article
    if qty is not None and qty > 30:
        issues.append({'QuoteLineItemId': qid, 'issue': 'Quantity exceeds typical limits', 'quantity': qty, 'knowledge_id': '#ka0Wt000000EnwvIAC'})
    # if unit price doesn't match pricebook entry
    if pb_up is not None and up is not None and abs(pb_up - up) > 0.01:
        issues.append({'QuoteLineItemId': qid, 'issue': 'UnitPrice mismatch with PricebookEntry', 'unitprice_quote': up, 'unitprice_pricebook': pb_up, 'knowledge_id': 'ka0Wt000000EnthIAC'})

# Also check if any product ids are missing from product table (inactive or missing) -> potential invalid
for q in ql_items:
    pid = q.get('Product2Id')
    # product catalog had missing entries for two product ids
    missing_products = ['#01tWt000006hV6jIAE','#01tWt000006hPffIAE']
    if pid in missing_products:
        issues.append({'QuoteLineItemId': q['Id'], 'issue': 'Product not active or missing in catalog', 'productid': pid, 'knowledge_id': '#ka0Wt000000EqRlIAK'})

# Determine most relevant knowledge article id: prioritize quantity limits and volume discounts and product issues
priority = ['#ka0Wt000000EnwvIAC','ka0Wt000000Eq0MIAS','#ka0Wt000000EqRlIAK','ka0Wt000000EnthIAC']
selected = None
for p in priority:
    for it in issues:
        if it.get('knowledge_id') == p:
            selected = p
            break
    if selected:
        break

# If none selected but issues exist, pick the first issue's knowledge id
if not selected and issues:
    selected = issues[0].get('knowledge_id')

# Print the selected knowledge article id as final result
print("__RESULT__:")
print(json.dumps(selected))"""

env_args = {'var_call_bzH9wjEFTS6ii2hhuYzXD1KS': [], 'var_call_SI3ERZc6ParkU17Bt2Xy70Eo': [{'Id': '#0Q0Wt000001WRAzKAO', 'Name': 'NeoGreen EDA Expansion Quote', 'AccountId': '001Wt00000PHVsDIAX', 'Status': 'Needs Review'}], 'var_call_jfEUkoH7QckUOwDxFeNKpfWL': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_call_PjPsiOaXcoz7OxsjVyAzp894': [{'Product2Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'IsActive': '1', 'PricebookEntryId': '01uWt0000027P8cIAE', 'UnitPrice': '529.99', 'Pricebook2Id': '01sWt000000imiTIAQ'}, {'Product2Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio', 'IsActive': '1', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'UnitPrice': '399.99', 'Pricebook2Id': '#01sWt000000imiTIAQ'}], 'var_call_vO6Fz2Rj4JtZLdPSU55JiZ1b': [], 'var_call_QImgvfgioj3lI2H7TFTTVFtz': [{'Id': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Pi5IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'UnitPrice': '399.99'}], 'var_call_mo4R0OOuWr34mvRux0hRahOA': 'file_storage/call_mo4R0OOuWr34mvRux0hRahOA.json', 'var_call_3atzJZ8omQ4ZSRUo6z4X9rPp': [{'id': '#ka0Wt000000EqRlIAK', 'title': 'Competitor: NanoDesign Systems   ', 'summary': "NanoDesign Systems is a prominent player in the electronic design automation industry, hailed for its strong vendor stability and partnership model, ensuring reliable, long-term collaborations with its clients. The company places significant emphasis on its roadmap and future enhancements, continually striving to align with emerging market demands and technological advancements. However, it faces challenges in offering highly customizable and flexible solutions, sometimes falling short of catering to specific and unique client workflows. Additionally, NanoDesign's support and service level agreements could be more responsive, with their pricing strategy occasionally seen as less transparent compared to competitors like TechPulse Solutions. Despite these challenges, NanoDesign remains a formidable entity with a focus on vendor reliability and technological growth."}, {'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'summary': 'Volume-Based Discounts'}, {'id': '#ka0Wt000000EpSUIA0', 'title': 'TechPulse Solution Volume-Based Installation Timeline Policy', 'summary': 'TechPulse Solution Volume-Based Installation Timeline Policy'}, {'id': '#ka0Wt000000EnwvIAC', 'title': 'Product Quantity Limits   ', 'summary': 'Product Quantity Limits'}, {'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers', 'summary': 'Policy for price adjustments based on competing offers'}], 'var_call_OCCEvzN1vAiHhbANaHwgWirW': [{'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'summary': 'Volume-Based Discounts'}, {'id': '#ka0Wt000000EpSUIA0', 'title': 'TechPulse Solution Volume-Based Installation Timeline Policy', 'summary': 'TechPulse Solution Volume-Based Installation Timeline Policy'}, {'id': '#ka0Wt000000EnwvIAC', 'title': 'Product Quantity Limits   ', 'summary': 'Product Quantity Limits'}, {'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers', 'summary': 'Policy for price adjustments based on competing offers'}], 'var_call_EFzGWufKBbEJW2GDyQ7LCuAi': []}

exec(code, env_args)
