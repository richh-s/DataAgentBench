code = """import json

# Load previous query results from storage
quotes = var_call_wvSWocroqxXzZPEsD8AcumCq
qli = var_call_YhuEQFSjhJviKUmXB6Vmoif0
pbe = var_call_ZnXv9FZgUQh05wahwR9A6W1X
product2 = var_call_1Ab1N51zjZMHOb9RU865i4DV
kb_matches = var_call_spTrKE5cwq6F6beSX1At7UQI

# Parse numeric fields and compute expected totals
import decimal

def to_decimal(x):
    try:
        return decimal.Decimal(str(x))
    except:
        return decimal.Decimal('0')

violations = []

# Check each quote line item if discounts and totals match and whether volume-based discounts or installation timeline policy apply
for q in quotes:
    qid = q['Id']
    # find qli items
    items = [i for i in qli if i['QuoteId']==qid]
    # compute sum of TotalPrice
    sum_total = decimal.Decimal('0')
    for it in items:
        qty = to_decimal(it['Quantity'])
        unit = to_decimal(it['UnitPrice'])
        disc = to_decimal(it['Discount'])
        # apply discount percent
        expected_total = qty * unit * (decimal.Decimal('1') - disc/decimal.Decimal('100'))
        # round to 4 decimal places as seen
        expected_total = expected_total.quantize(decimal.Decimal('0.0001'))
        actual = to_decimal(it['TotalPrice']).quantize(decimal.Decimal('0.0001'))
        if expected_total != actual:
            violations.append({'type':'lineitem_mismatch','item':it['Id'],'expected':str(expected_total),'actual':str(actual)})
        sum_total += actual

# Check if any KB match relates to volume discounts or installation timeline
kb_ids = [k['id'] for k in kb_matches]
# From KB matches, identify specific policy articles IDs for Volume-Based Discounts and Volume-Based Installation Timeline
# We saw ids: 'ka0Wt000000Eq0MIAS' (Volume-Based Discounts), '#ka0Wt000000EpSUIA0' (Volume-Based Installation Timeline Policy)
found_kb = None
for k in kb_matches:
    t = k['title'].lower() if k['title'] else ''
    if 'volume-based' in t or 'volume based' in t or 'volume' in t:
        # prefer exact matches
        if 'volume-based installation' in t:
            found_kb = k['id']
            break
        if 'volume-based discounts' in t:
            found_kb = k['id']
            # continue loop to prefer installation timeline if present

# Determine if quote conflicts: check if discounts applied match Volume-Based Discounts tiers
# Total quote sum
quote_total = sum_total

# For the quote, calculate pre-discount totals and applied discounts
# compute pre-discount based on qty * unit
pre_discount_total = decimal.Decimal('0')
applied_discounts = []
for it in items:
    qty = to_decimal(it['Quantity'])
    unit = to_decimal(it['UnitPrice'])
    pre = qty*unit
    pre_discount_total += pre
    applied_discounts.append(to_decimal(it['Discount']))

# According to Volume-Based Discounts article: tiers are 5% for >$5, 10% for >$10, 15% for >$20
# These thresholds seem unrealistic (dollars) but we'll apply as written.
violation_kb = None
# Determine expected discount percent by pre_discount_total
if pre_discount_total > decimal.Decimal('20'):
    expected_percent = decimal.Decimal('15')
elif pre_discount_total > decimal.Decimal('10'):
    expected_percent = decimal.Decimal('10')
elif pre_discount_total > decimal.Decimal('5'):
    expected_percent = decimal.Decimal('5')
else:
    expected_percent = decimal.Decimal('0')

# Compare applied discounts: if items have differing discounts or not matching expected_percent, mark violation against Volume-Based Discounts
# If any item discount != expected_percent, consider violation
if expected_percent > 0:
    for d in applied_discounts:
        if d != expected_percent:
            # we have a mismatch
            violation_kb = 'ka0Wt000000Eq0MIAS'
            break

# Additionally, check installation timeline policy: if quantities correspond to specific volumes (1,5,15,25) and timeline not adhered --
# We don't have explicit setup time in quote, but maybe 'setup' implied. The user asks: Does the cost and setup of this quote comply with our company policy? If not which article is it in conflict with?
# Based on our checks, if discount mismatch found, return that KB id. Else, None.

result = violation_kb if violation_kb else None

print('__RESULT__:')
import json
print(json.dumps(result))"""

env_args = {'var_call_wvSWocroqxXzZPEsD8AcumCq': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_YhuEQFSjhJviKUmXB6Vmoif0': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_1Ab1N51zjZMHOb9RU865i4DV': [{'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1', 'UnitPrice': '499.99', 'Pricebook2Id': '#01sWt000000imiTIAQ'}], 'var_call_ZnXv9FZgUQh05wahwR9A6W1X': [{'Id': '01uWt0000027P3lIAE', 'UnitPrice': '499.99', 'Pricebook2Id': '#01sWt000000imiTIAQ'}, {'Id': '01uWt0000027PVBIA2', 'UnitPrice': '339.99', 'Pricebook2Id': '01sWt000000imiTIAQ'}], 'var_call_iAweqGB6AbEEKrZr570JYP95': [{'Id': '#001Wt00000PGXrKIAX', 'Name': 'InnovateX Solutions', 'Phone': '222-111-2222', 'Industry': 'Tech Consulting', 'Description': 'InnovateX Solutions provides cutting-edge consulting services, assisting businesses in integrating the latest technologies into their operations. Using tools like CloudLink Designer and CircuitAI Innovator, they enhance collaborative efforts and circuit design precision. Their focus on seamless tech integration empowers clients to achieve significant efficiency gains.', 'NumberOfEmployees': '850.0', 'ShippingState': 'WA'}], 'var_call_IkMNuZteIaWUp78yho7YAJRG': [{'Id': '003Wt00000JqkgYIAR', 'FirstName': 'Nina', 'LastName': 'Tran', 'Email': 'nina.tran@innovatexsolutions.com', 'AccountId': '001Wt00000PGXrKIAX'}], 'var_call_lKpArYVIoxMof4y0t6v3uK6H': [], 'var_call_Eb7bluxzNBaJTy9sHCEC5yRj': [{'Id': '006Wt000007BHHfIAO', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '#003Wt00000JqkgYIAR', 'OwnerId': '#005Wt000003NIybIAG', 'Probability': '75.0', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Name': 'InnovateX Solutions Technology Integration Opportunity', 'Description': 'TechPulse Solutions offers InnovateX Solutions a suite of tools, including AI-powered CircuitSync Pro and environmentally-focused EcoPCB Creator, to enhance their design capabilities. By incorporating DesignWave Automation, InnovateX can streamline workflows, ensuring faster project completion and higher client satisfaction. Integrating PulseSim Pro will optimize circuit design verification with precision and speed.', 'CreatedDate': '2021-05-20T14:15:30.000+0000', 'CloseDate': '2021-07-15'}], 'var_call_ZKPrJMFL2kXWEGYBC1Q6hYOX': 'file_storage/call_ZKPrJMFL2kXWEGYBC1Q6hYOX.json', 'var_call_spTrKE5cwq6F6beSX1At7UQI': [{'id': '#ka0Wt000000EqRlIAK', 'title': 'Competitor: NanoDesign Systems   ', 'summary': "NanoDesign Systems is a prominent player in the electronic design automation industry, hailed for its strong vendor stability and partnership model, ensuring reliable, long-term collaborations with its clients. The company places significant emphasis on its roadmap and future enhancements, continually striving to align with emerging market demands and technological advancements. However, it faces challenges in offering highly customizable and flexible solutions, sometimes falling short of catering to specific and unique client workflows. Additionally, NanoDesign's support and service level agreements could be more responsive, with their pricing strategy occasionally seen as less transparent compared to competitors like TechPulse Solutions. Despite these challenges, NanoDesign remains a formidable entity with a focus on vendor reliability and technological growth."}, {'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'summary': 'Volume-Based Discounts'}, {'id': '#ka0Wt000000EpSUIA0', 'title': 'TechPulse Solution Volume-Based Installation Timeline Policy', 'summary': 'TechPulse Solution Volume-Based Installation Timeline Policy'}, {'id': 'ka0Wt000000EorOIAS', 'title': 'Automating Development Processes with AutoGen IDE', 'summary': 'Discussing the benefits of automation in accelerating coding and project setup using AutoGen IDE.'}, {'id': 'ka0Wt000000EoJWIA0', 'title': 'Streamlined Development with AutoGen IDE', 'summary': 'An overview of how AutoGen IDE supports rapid coding and project setup through automation.'}, {'id': 'ka0Wt000000Em4zIAC', 'title': 'Navigating Installation Challenges: Solutions for Seamless Setup of TechPulse EDA Tools', 'summary': "TechPulse Solutions clients sometimes face software installation errors, which can be an obstacle during the initial setup of the company's powerful electronic design automation tools. This article delves into the two main solutions designed to address these challenges effectively. The 'Priority Support Upgrade' offers customers the advantage of faster response times to installation issues, ensuring minimal disruption and timely resolution. Additionally, 'Comprehensive Training Access' equips users with the necessary skills and confidence to handle potential roadblocks in the installation process, fostering a deeper understanding of the product's intricacies. These strategies, together with TechPulse Solutions' commitment to innovation and customer satisfaction, reinforce the seamless integration of their AI-powered solutions into existing workflows, ensuring clients maximize their investment."}, {'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers', 'summary': 'Policy for price adjustments based on competing offers'}], 'var_call_HhJe72dCpIq8x5GyU2M2et2P': 'file_storage/call_HhJe72dCpIq8x5GyU2M2et2P.json', 'var_call_TIAvMuInG3FkzwMWB5sHZAGZ': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1'}]}

exec(code, env_args)
