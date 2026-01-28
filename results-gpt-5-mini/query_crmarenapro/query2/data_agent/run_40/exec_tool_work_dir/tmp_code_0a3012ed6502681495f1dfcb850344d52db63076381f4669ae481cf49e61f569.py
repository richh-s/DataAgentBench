code = """import json
# load previous query results available as variables
quotes = var_call_ltRdW8VEhXnDicJi7FinhuaY
qli = var_call_ADjaZJceV2uVTu4kvRMO8LmI
kb_hits = var_call_cH0bIjwPzErmTYv4XTZtFFdb
kb_specific = var_call_9DBpLGEPj8ARVHPVVvAi3Ahe
products_file = var_call_HVttk98xjsn7aYykSbHGivnR

# Build numeric total from quote line items (consider strings and possible corruption)
import decimal

def to_decimal(x):
    try:
        return decimal.Decimal(str(x).strip())
    except Exception:
        try:
            return decimal.Decimal(x.replace(',','').strip())
        except Exception:
            return decimal.Decimal('0')

# sum line items' TotalPrice
total = decimal.Decimal('0')
for r in qli:
    total += to_decimal(r.get('TotalPrice',0))
    
# Gather any knowledge articles that look relevant from kb_hits/kb_specific
# We have two likely relevant: Volume-Based Discounts and Mandatory Bundles for Quotes
# Check quote for discounts and bundle requirements

# Determine if any line item product is one that requires a mandatory bundle per 'Mandatory Bundles for Quotes'
# From kb_specific, bundles mention product names: PulseSim Pro requires CircuitMaster Analyzer and VeriSim Express
# AI Cirku-Tech requires CircuitAI Innovator and AI DesignShift etc.
# We need to map Product2Id in quote line items to Product2 names from products query result (products_file)

with open(products_file, 'r') as f:
    products = json.load(f)

# create mapping from Id (strip possible leading # and whitespace) to Name (strip)
prod_map = {}
for p in products:
    pid = p.get('Id','').strip()
    pid_clean = pid.lstrip('#')
    prod_map[pid] = p.get('Name','').strip()
    prod_map[pid_clean] = p.get('Name','').strip()

# check each quoted product
quoted_product_names = []
for r in qli:
    pid = r.get('Product2Id','').strip()
    pid_clean = pid.lstrip('#')
    name = prod_map.get(pid) or prod_map.get(pid_clean)
    if name:
        quoted_product_names.append(name)
    else:
        quoted_product_names.append(None)

# check for Volume-Based Discounts violation: the knowledge article describes discounts tiers for purchases over $5, $10, $20
# The quote has specific Discount field per line item; company policy likely restricts discounting beyond allowed tiers
# But the prompt: Does the cost and setup of this quote comply with our company policy? If it doesn't, which knowledge article is it in conflict with? Return only the Id of the knowledge article that the quote violates. If no violation found, return None.

# Interpret violation conditions heuristically:
# 1) If any line item discount exceeds 15% (highest tier) => violates Volume-Based Discounts
# 2) If any product in the quote is part of a mandatory bundle but required companion products are NOT in the quote => violates Mandatory Bundles for Quotes

violations = []
# check discounts
for r in qli:
    try:
        disc = float(str(r.get('Discount','0')).strip())
    except:
        disc = 0.0
    if disc > 15.0:
        violations.append('ka0Wt000000Eq0MIAS')
        break

# check mandatory bundles
# From kb_specific faq text, we know specific mappings. Build required companion mapping
required_bundles = {
    'PulseSim Pro': ['CircuitMaster Analyzer','VeriSim Express'],
    'CloudLink Designer': ['DesignEdge Pro','AI DesignShift'],
    'AI Cirku-Tech': ['CircuitAI Innovator','AI DesignShift'],
    'OptiPower Manager': ['OptiEnergy Suite','PowerPro Optimize'],
    'AIOptics Vision': ['Workflow Genius','AI DesignShift']
}

# For each quoted product, if it's a key in required_bundles, check if required companions present in quoted_product_names
for name in quoted_product_names:
    if name in required_bundles:
        companions = required_bundles[name]
        # check presence
        present = all(any((c and c.lower() == qn.lower()) for qn in quoted_product_names) for c in companions)
        if not present:
            violations.append('ka0Wt000000Ens5IAC')
            break

# dedupe
violations = list(dict.fromkeys(violations))

# Decide final result: if any violations, choose the first? The user asks which knowledge article it is in conflict with -> likely return the id. If multiple, return first.
result = None
if violations:
    result = violations[0]
else:
    result = None

# print result according to format
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ltRdW8VEhXnDicJi7FinhuaY': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_ADjaZJceV2uVTu4kvRMO8LmI': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_ysPDnLF8SgzrcZLbj2VVgk5J': [], 'var_call_cH0bIjwPzErmTYv4XTZtFFdb': [{'id': '#ka0Wt000000EqRlIAK', 'title': 'Competitor: NanoDesign Systems   ', 'summary': "NanoDesign Systems is a prominent player in the electronic design automation industry, hailed for its strong vendor stability and partnership model, ensuring reliable, long-term collaborations with its clients. The company places significant emphasis on its roadmap and future enhancements, continually striving to align with emerging market demands and technological advancements. However, it faces challenges in offering highly customizable and flexible solutions, sometimes falling short of catering to specific and unique client workflows. Additionally, NanoDesign's support and service level agreements could be more responsive, with their pricing strategy occasionally seen as less transparent compared to competitors like TechPulse Solutions. Despite these challenges, NanoDesign remains a formidable entity with a focus on vendor reliability and technological growth."}, {'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'summary': 'Volume-Based Discounts'}, {'id': 'ka0Wt000000EorOIAS', 'title': 'Automating Development Processes with AutoGen IDE', 'summary': 'Discussing the benefits of automation in accelerating coding and project setup using AutoGen IDE.'}, {'id': 'ka0Wt000000EoJWIA0', 'title': 'Streamlined Development with AutoGen IDE', 'summary': 'An overview of how AutoGen IDE supports rapid coding and project setup through automation.'}, {'id': 'ka0Wt000000Em4zIAC', 'title': 'Navigating Installation Challenges: Solutions for Seamless Setup of TechPulse EDA Tools', 'summary': "TechPulse Solutions clients sometimes face software installation errors, which can be an obstacle during the initial setup of the company's powerful electronic design automation tools. This article delves into the two main solutions designed to address these challenges effectively. The 'Priority Support Upgrade' offers customers the advantage of faster response times to installation issues, ensuring minimal disruption and timely resolution. Additionally, 'Comprehensive Training Access' equips users with the necessary skills and confidence to handle potential roadblocks in the installation process, fostering a deeper understanding of the product's intricacies. These strategies, together with TechPulse Solutions' commitment to innovation and customer satisfaction, reinforce the seamless integration of their AI-powered solutions into existing workflows, ensuring clients maximize their investment."}, {'id': 'ka0Wt000000Ens5IAC', 'title': 'Mandatory Bundles for Quotes', 'summary': 'Mandatory Bundles for Quotes'}], 'var_call_9DBpLGEPj8ARVHPVVvAi3Ahe': [{'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'summary': 'Volume-Based Discounts', 'faq_answer__c': "Volume-based discounts are a strategic tool for fostering customer loyalty and encouraging bulk purchases. At TechPulse Solution, we aim to provide value-added benefits to our customers, and volume-based discounts are integral to this mission. Here is a detailed overview of the volume-based discounts currently available:\n\n1. **5% Discount for Purchases Over $5**: This entry-level discount is designed for customers making modest but regular purchases. If your transaction totals $5 or more, you automatically become eligible for a 5% discount on your total purchase. This incentive is perfect for small businesses or individuals looking to maximize their purchasing power without committing to large upfront investments.\n\n2. **10% Discount for Purchases Over $10**: By increasing your purchase to $10, you can enjoy a more substantial 10% discount. This tier is targeted at growing businesses or tech enthusiasts planning for larger projects. Whether you're a startup needing essential tech solutions or an established entity upgrading current systems, this level of discount allows you to save significant amounts while meeting your needs.\n\n3. **15% Discount for Purchases Over $20**: The highest discount tier is designed for customers planning substantial investments in tech solutions. With a purchase of $20 or more, you can benefit from a generous 15% discount. This is particularly advantageous for businesses engaged in major scaling projects or for those who require extensive tech solutions for operational expansion.\n\nThese volume-based discounts are designed to reward you as you invest more in our innovative solutions, ensuring that you receive the best possible value. They are automatically applied at checkout, simplifying the purchasing process and enabling you to focus on selecting the best technology for your needs.\n\nIncorporating these discounts into your purchasing strategy can significantly reduce costs while allowing access to premium technology and support from TechPulse Solution. Whether you are a small business making selective purchases or a large company procuring extensive solutions, our discount structure provides a tailored approach to meet varying budgetary needs.\n\nOptimize your purchasing strategy and operational efficiency with our volume-based discounts, designed to bring you closer to innovative technology that can drive your success. At TechPulse Solution, your needs are at the forefront, and these carefully crafted discounts provide a pathway to affordable excellence."}, {'id': 'ka0Wt000000Ens5IAC', 'title': 'Mandatory Bundles for Quotes', 'summary': 'Mandatory Bundles for Quotes', 'faq_answer__c': "In the fast-paced world of technological solutions, understanding mandatory product bundles is crucial for securing the best performance and compatibility. At TechPulse Solution, we have streamlined our product offerings, ensuring optimal functionality through specific bundled requirements. This guide provides a comprehensive overview of the mandatory bundles required for quoting our top-tier products.\n\n1. PulseSim Pro Bundle: When purchasing PulseSim Pro, customers must also include the CircuitMaster Analyzer and VeriSim Express in their package. This bundling is designed to enhance your simulation experience, providing unparalleled accuracy and efficiency. CircuitMaster Analyzer works to deliver precise circuit analysis, while VeriSim Express complements it by facilitating swift verification processes. Together, these tools enhance the functionalities of PulseSim Pro, resulting in top-notch simulation capabilities.\n\n2. CloudLink Designer Bundle: To acquire the CloudLink Designer, it's essential to purchase DesignEdge Pro and AI DesignShift as well. This trio creates a robust design platform ideally suited for cloud-based operations. DesignEdge Pro offers advanced design capabilities, ensuring top-quality outcomes, while AI DesignShift incorporates artificial intelligence for intelligent design adaptability and innovation. By combining these products with CloudLink Designer, you achieve a seamless integration that improves performance and design fluidity on the cloud.\n\n3. AI Cirku-Tech Bundle: Customers interested in AI Cirku-Tech must also consider acquiring CircuitAI Innovator and AI DesignShift. Partnered with CircuitAI Innovator, AI Cirku-Tech brings artificial intelligence enhancements to circuit design, optimizing both creativity and efficiency. AI DesignShift, on the other hand, introduces advanced AI-driven design shifts, facilitating a broader scope of design possibilities. This bundle offers a significant leap forward in circuit technology, fully realizing the potential of AI integration.\n\n4. OptiPower Manager Bundle: Purchasing OptiPower Manager necessitates the inclusion of the OptiEnergy Suite and PowerPro Optimize. This comprehensive power management bundle ensures users can effectively monitor and optimize power usage. OptiEnergy Suite offers robust tools for energy management and efficiency, while PowerPro Optimize provides critical power optimization features. Combined with OptiPower Manager, these tools help in achieving significant energy savings and power control.\n\n5. AIOptics Vision Bundle: Lastly, AIOptics Vision requires the Workflow Genius and AI DesignShift as part of its package. This requirement ensures customers have access to superior workflow management tools and AI capabilities. Workflow Genius enhances project management and operational workflows, while AI DesignShift contributes AI-enhanced design innovations. Together with AIOptics Vision, these products deliver a powerful platform for optical analysis and design.\n\nUnderstanding these mandatory bundles helps ensure you receive the full potential of each product offered by TechPulse Solution. By purchasing these curated packages, customers benefit from enhanced functionality, superior performance, and seamless integration, providing an unparalleled technological advantage."}], 'var_call_HVttk98xjsn7aYykSbHGivnR': 'file_storage/call_HVttk98xjsn7aYykSbHGivnR.json'}

exec(code, env_args)
