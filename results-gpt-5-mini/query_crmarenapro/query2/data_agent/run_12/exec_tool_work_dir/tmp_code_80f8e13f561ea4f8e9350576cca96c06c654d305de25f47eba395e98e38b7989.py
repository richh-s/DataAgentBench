code = """import json
# load the full knowledge articles result from the provided storage key
path = var_call_igVBXllKj3BL4hA8oy86uIzY
with open(path, 'r') as f:
    ka = json.load(f)
# find relevant articles by id or title keywords
candidates = [a for a in ka if any(k in (a.get('title') or '').lower() for k in ['volume-based discounts','mandatory bundles','installation timeline','installation','volume-based installation','competing offers','mandatory bundles for quotes','volume-based discounts'])]
# Also pick by id if starts with ka0Wt000000Eq0MIAS etc
ids_of_interest = ['ka0Wt000000Eq0MIAS','ka0Wt000000Ens5IAC','#ka0Wt000000EpSUIA0','ka0Wt000000Em4zIAC','ka0Wt000000EnthIAC']
for iid in ids_of_interest:
    for a in ka:
        if a.get('id') == iid:
            candidates.append(a)
# dedupe
seen = set()
unique = []
for a in candidates:
    if a.get('id') not in seen:
        unique.append(a)
        seen.add(a.get('id'))
# prepare output showing ids, titles, faq answer
out = [{'id': a.get('id'), 'title': a.get('title'), 'faq_answer__c': a.get('faq_answer__c'), 'summary': a.get('summary')} for a in unique]

import math
# load quote and items from storage
quote = var_call_StaKtyRzyGB9MIe7GduACybN[0]
items = var_call_gy68ByWYDs6G36tu445uRA0N
products = var_call_rAjGJMcetkgOVjiEFdZoQU5T
# compute totals
for it in items:
    qty = float(it['Quantity'])
    unit = float(it['UnitPrice'])
    discount = float(it['Discount'])
    gross = qty * unit
    net = gross * (1 - discount/100)
    it['_computed_gross'] = gross
    it['_computed_net'] = net
# compute quote total
quote_total = sum(it['_computed_net'] for it in items)

# Determine violations by scanning candidate articles for rules
violations = []
# naive rule checks based on article contents
for a in out:
    txt = (a.get('faq_answer__c') or '') + ' ' + (a.get('summary') or '')
    low = txt.lower()
    # check volume discount policy: if article mentions max discount percent
    if 'volume' in low and 'discount' in low:
        # try to extract any percentage limits mentioned
        import re
        percents = [int(p) for p in re.findall(r'(\d{1,2})%','%'+txt) if 0<int(p)<100]
        # fallback: look for phrases like 'up to X%'
        m = re.search(r'up to (\d{1,2})%',''.join([txt]), re.IGNORECASE)
        if percents:
            maxp = max(percents)
            # if any item discount > maxp, violation
            for it in items:
                if float(it['Discount']) > maxp:
                    violations.append({'article_id': a['id'], 'reason': f"item {it['Id']} discount {it['Discount']}% > allowed {maxp}%"})
        elif m:
            maxp = int(m.group(1))
            for it in items:
                if float(it['Discount']) > maxp:
                    violations.append({'article_id': a['id'], 'reason': f"item {it['Id']} discount {it['Discount']}% > allowed {maxp}%"})
    # check mandatory bundles: if article mentions mandatory bundle and our quote lacks required product
    if 'mandatory bundle' in low or 'mandatory bundles' in low:
        # try to find mentioned product names in the article
        # simplistic: if article mentions 'installation' or 'bundle' with product name 'Pulse' etc.
        # For this dataset, assume article enforces that certain products must be bundled; find product names from products
        prod_names = [p['Name'].lower() for p in products]
        # if article mentions a product and our items don't include it, flag
        for pn in prod_names:
            if pn and pn in low:
                # check if any quote line item product matches
                present = False
                for it in items:
                    # try match product ids via products list (we have only one product row for PulseSim Pro)
                    if it.get('Product2Id') == products[0]['Id']:
                        present = True
                if not present:
                    violations.append({'article_id': a['id'], 'reason': f"required product {pn} not in quote"})
    # installation timeline policy: check if quantity triggers timeline and article forbids quoting without setup fee? We'll check for 'setup' or 'installation fee' mentions
    if 'installation' in low or 'setup' in low:
        # if article mentions 'priority support upgrade' or 'comprehensive training access' as paid addons, ensure setup fee present; but we lack explicit setup fee field
        # check if article forbids discounts over X on installation-related items; attempt to match
        if 'priority support' in low or 'setup' in low:
            # heuristic: if any item has discount > 10% and article mentions faster response times as paid, flag
            for it in items:
                if float(it['Discount']) > 10:
                    violations.append({'article_id': a['id'], 'reason': f"item {it['Id']} discount {it['Discount']}% conflicts with installation policy"})
    # competing offers: if article mentions price match and requires approval if greater than competitor, skip
    if 'competing offer' in low or 'competing offers' in low or 'competing' in low:
        # if any discount < 5% maybe fine; we won't flag
        pass

# dedupe violations and choose highest priority: Volume-Based Discounts first, Mandatory Bundles next, Installation timeline next
priority_ids = ['ka0Wt000000Eq0MIAS','ka0Wt000000Ens5IAC','#ka0Wt000000EpSUIA0','ka0Wt000000Em4zIAC','ka0Wt000000EnthIAC']
final_violation = None
for pid in priority_ids:
    for v in violations:
        if v['article_id'] == pid:
            final_violation = pid
            break
    if final_violation:
        break

# if no violation found, return None
res = final_violation if final_violation is not None else None

import json
print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_call_StaKtyRzyGB9MIe7GduACybN': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_gy68ByWYDs6G36tu445uRA0N': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_rAjGJMcetkgOVjiEFdZoQU5T': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1', 'UnitPrice': '499.99'}], 'var_call_igVBXllKj3BL4hA8oy86uIzY': 'file_storage/call_igVBXllKj3BL4hA8oy86uIzY.json', 'var_call_43FnrrjDUQyLRlTXaTQCrY9n': [{'id': 'ka0Wt000000EowFIAS', 'title': 'Competitor: Adaptive Design Solutions', 'summary': 'Adaptive Design Solutions positions itself as a key player in the electronic design automation sector, emphasizing exceptional user experience and streamlined adoption processes. Despite these strengths, the company faces challenges in maintaining a competitive roadmap and offering future enhancements that align with evolving market demands. Additionally, clients often cite concerns regarding the total cost of ownership and ROI, as well as complexities in implementation and deployment stages. While their user-centric approach garners positive feedback, the company continues to work on improving the economic and strategic aspects of its offerings to enhance its value proposition.'}, {'id': '#ka0Wt000000EqRlIAK', 'title': 'Competitor: NanoDesign Systems   ', 'summary': "NanoDesign Systems is a prominent player in the electronic design automation industry, hailed for its strong vendor stability and partnership model, ensuring reliable, long-term collaborations with its clients. The company places significant emphasis on its roadmap and future enhancements, continually striving to align with emerging market demands and technological advancements. However, it faces challenges in offering highly customizable and flexible solutions, sometimes falling short of catering to specific and unique client workflows. Additionally, NanoDesign's support and service level agreements could be more responsive, with their pricing strategy occasionally seen as less transparent compared to competitors like TechPulse Solutions. Despite these challenges, NanoDesign remains a formidable entity with a focus on vendor reliability and technological growth."}, {'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'summary': 'Volume-Based Discounts'}, {'id': '#ka0Wt000000EpSUIA0', 'title': 'TechPulse Solution Volume-Based Installation Timeline Policy', 'summary': 'TechPulse Solution Volume-Based Installation Timeline Policy'}, {'id': 'ka0Wt000000EorOIAS', 'title': 'Automating Development Processes with AutoGen IDE', 'summary': 'Discussing the benefits of automation in accelerating coding and project setup using AutoGen IDE.'}, {'id': '#ka0Wt000000Eo8FIAS', 'title': 'Optimizing Workflow Automation with AutoGen IDE', 'summary': 'Exploring automation features in AutoGen IDE to streamline project workflows.'}, {'id': 'ka0Wt000000EoJWIA0', 'title': 'Streamlined Development with AutoGen IDE', 'summary': 'An overview of how AutoGen IDE supports rapid coding and project setup through automation.'}, {'id': 'ka0Wt000000Em4zIAC', 'title': 'Navigating Installation Challenges: Solutions for Seamless Setup of TechPulse EDA Tools', 'summary': "TechPulse Solutions clients sometimes face software installation errors, which can be an obstacle during the initial setup of the company's powerful electronic design automation tools. This article delves into the two main solutions designed to address these challenges effectively. The 'Priority Support Upgrade' offers customers the advantage of faster response times to installation issues, ensuring minimal disruption and timely resolution. Additionally, 'Comprehensive Training Access' equips users with the necessary skills and confidence to handle potential roadblocks in the installation process, fostering a deeper understanding of the product's intricacies. These strategies, together with TechPulse Solutions' commitment to innovation and customer satisfaction, reinforce the seamless integration of their AI-powered solutions into existing workflows, ensuring clients maximize their investment."}, {'id': 'ka0Wt000000EnvKIAS', 'title': 'The Xtreme Approach to Simulation: A High-Speed Solution   ', 'summary': "TechPulse Solutions' focus on speed and comprehensive verification in simulation tools maximizes design efficiency."}, {'id': 'ka0Wt000000EnyXIAS', 'title': 'TechPulse Solutions: Defining Values that Drive Innovation and Success', 'summary': 'Company core values.'}, {'id': 'ka0Wt000000Ens5IAC', 'title': 'Mandatory Bundles for Quotes', 'summary': 'Mandatory Bundles for Quotes'}, {'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers', 'summary': 'Policy for price adjustments based on competing offers'}]}

exec(code, env_args)
