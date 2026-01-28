code = """import json
# Accessing the large knowledge articles result stored in var_call_AEH2Lx8acHGE8YZrT56EQm7Q
path = var_call_AEH2Lx8acHGE8YZrT56EQm7Q
with open(path, 'r') as f:
    data = json.load(f)

# We'll inspect which of these knowledge articles conflict with the quote details.
# Load quote and quote line items from storage variables
quote = var_call_knhd8tdLIb8l8SsS0G3yymRF[0]
quote_line_items = var_call_ik0x9EiFLIg7GV7l0yJCUsiM
products = var_call_FDAKEJ0hLnRBMT1L1xegdOra
pricebook_entries = var_call_axvsk80LCvITMTxwa1EQZcPa

# Normalize numeric values from strings
for qli in quote_line_items:
    qli['Quantity'] = float(qli['Quantity'])
    qli['UnitPrice'] = float(qli['UnitPrice'])
    qli['Discount'] = float(qli['Discount'])
    qli['TotalPrice'] = float(qli['TotalPrice'])

# Compute expected total per line and overall
for qli in quote_line_items:
    subtotal = qli['Quantity'] * qli['UnitPrice']
    expected_total = subtotal * (1 - qli['Discount']/100)
    qli['ComputedTotal'] = round(expected_total, 6)

overall_computed = round(sum(qli['ComputedTotal'] for qli in quote_line_items),6)

# Check for bundle violations: from 'Mandatory Bundles for Quotes' article
# Determine which products are present by matching Product2Id to products list
product_id_to_name = {p['Id']: p['Name'] for p in products}
# Some Product2Ids in quote_line_items include leading # so normalize keys
for p in list(product_id_to_name.keys()):
    product_id_to_name['#'+p] = product_id_to_name[p]

present_product_names = []
for qli in quote_line_items:
    pid = qli['Product2Id']
    name = product_id_to_name.get(pid)
    if name:
        present_product_names.append(name)

# Check if PulseSim Pro is included and if its mandatory bundle components are present
violating_article_id = None
for item in data:
    if item['id'] == 'ka0Wt000000Ens5IAC':
        faq = item.get('faq_answer__c','').lower()
        # Check rules for PulseSim Pro bundle
        if 'pulsesim pro' in faq:
            # Mandatory items listed: CircuitMaster Analyzer and VeriSim Express
            required = {'circuitmaster analyzer','verisim express'}
            # Check if any required are in product names (lowercased)
            present_lower = [n.lower() for n in present_product_names]
            missing = required - set(present_lower)
            if 'pulsesim pro' in present_lower and missing:
                violating_article_id = item['id']

# Also check volume-based discounts conflicts: see if discounts applied exceed allowed tiers
for item in data:
    if item['id'] == 'ka0Wt000000Eq0MIAS':
        faq = item.get('faq_answer__c','')
        # Simplify: parse allowed discounts tiers from text
        # We will check each quote line if discount percent is in {5,10,15}
        allowed_discounts = {5.0,10.0,15.0}
        for qli in quote_line_items:
            if qli['Discount'] not in allowed_discounts:
                violating_article_id = item['id']

# Build result: either the violating article id or None
result = violating_article_id if violating_article_id is not None else None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_knhd8tdLIb8l8SsS0G3yymRF': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_9RsvNN8OYPGORwUeGP7gkClt': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_call_ik0x9EiFLIg7GV7l0yJCUsiM': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_FDAKEJ0hLnRBMT1L1xegdOra': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.'}], 'var_call_axvsk80LCvITMTxwa1EQZcPa': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_MLp4qsKsmcEiMokWJjcT2GbC': [], 'var_call_tPAgyaNmLBbhB5MmQGGiUqZY': [{'Id': '006Wt000007BHHfIAO', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '#003Wt00000JqkgYIAR', 'OwnerId': '#005Wt000003NIybIAG', 'Probability': '75.0', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Name': 'InnovateX Solutions Technology Integration Opportunity', 'Description': 'TechPulse Solutions offers InnovateX Solutions a suite of tools, including AI-powered CircuitSync Pro and environmentally-focused EcoPCB Creator, to enhance their design capabilities. By incorporating DesignWave Automation, InnovateX can streamline workflows, ensuring faster project completion and higher client satisfaction. Integrating PulseSim Pro will optimize circuit design verification with precision and speed.', 'CreatedDate': '2021-05-20T14:15:30.000+0000', 'CloseDate': '2021-07-15'}], 'var_call_m4bvzbvo6Q59sbSJu8m1JYpE': [{'Id': '#001Wt00000PGXrKIAX', 'Name': 'InnovateX Solutions', 'Phone': '222-111-2222', 'Industry': 'Tech Consulting', 'Description': 'InnovateX Solutions provides cutting-edge consulting services, assisting businesses in integrating the latest technologies into their operations. Using tools like CloudLink Designer and CircuitAI Innovator, they enhance collaborative efforts and circuit design precision. Their focus on seamless tech integration empowers clients to achieve significant efficiency gains.', 'NumberOfEmployees': '850.0', 'ShippingState': 'WA'}], 'var_call_Pyu9CHMreyj8F0Gcu0Hf2BgR': [{'Id': '003Wt00000JqkgYIAR', 'FirstName': 'Nina', 'LastName': 'Tran', 'Email': 'nina.tran@innovatexsolutions.com', 'AccountId': '001Wt00000PGXrKIAX'}], 'var_call_MTp9VAiEi5OxSCOIcyIbYbhe': [{'id': '#ka0Wt000000EqRlIAK', 'title': 'Competitor: NanoDesign Systems   ', 'summary': "NanoDesign Systems is a prominent player in the electronic design automation industry, hailed for its strong vendor stability and partnership model, ensuring reliable, long-term collaborations with its clients. The company places significant emphasis on its roadmap and future enhancements, continually striving to align with emerging market demands and technological advancements. However, it faces challenges in offering highly customizable and flexible solutions, sometimes falling short of catering to specific and unique client workflows. Additionally, NanoDesign's support and service level agreements could be more responsive, with their pricing strategy occasionally seen as less transparent compared to competitors like TechPulse Solutions. Despite these challenges, NanoDesign remains a formidable entity with a focus on vendor reliability and technological growth."}, {'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'summary': 'Volume-Based Discounts'}], 'var_call_37cHFLZiYB78CsFCg5L8KE6O': [{'id': 'ka0Wt000000Ens5IAC', 'title': 'Mandatory Bundles for Quotes', 'summary': 'Mandatory Bundles for Quotes'}], 'var_call_tvulywbW9jsKbMg5ml1UagNL': [{'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'summary': 'Volume-Based Discounts'}, {'id': 'ka0Wt000000Ens5IAC', 'title': 'Mandatory Bundles for Quotes', 'summary': 'Mandatory Bundles for Quotes'}], 'var_call_AEH2Lx8acHGE8YZrT56EQm7Q': 'file_storage/call_AEH2Lx8acHGE8YZrT56EQm7Q.json'}

exec(code, env_args)
