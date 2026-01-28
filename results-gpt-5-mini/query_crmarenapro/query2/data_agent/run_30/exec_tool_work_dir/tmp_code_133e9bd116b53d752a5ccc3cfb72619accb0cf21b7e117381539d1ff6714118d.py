code = """import json
# Accessing tool results
quote = var_call_MlLHCXIyU20mZ7dK86MssesS[0]
qlis = var_call_gyBbGzyOl1OELEVa164BMB6U
kav = var_call_OU209PffMpbx9tdVBk6MlqHV[0]

# Compute pre-discount total
def to_float(x):
    try:
        return float(x)
    except:
        return 0.0

total_pre = 0.0
for li in qlis:
    qty = to_float(li.get('Quantity', 0))
    up = to_float(li.get('UnitPrice', 0))
    total_pre += qty * up

# Determine expected volume discount based on knowledge article tiers
# From the article: 5% for > $5, 10% for > $10, 15% for > $20
expected_discount = 0.0
if total_pre > 20:
    expected_discount = 15.0
elif total_pre > 10:
    expected_discount = 10.0
elif total_pre > 5:
    expected_discount = 5.0
else:
    expected_discount = 0.0

# Check if all line items have the expected discount
violation = False
for li in qlis:
    disc = to_float(li.get('Discount', 0))
    # allow small tolerance
    if abs(disc - expected_discount) > 1e-6:
        violation = True
        break

result = kav['id'] if violation else None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_MlLHCXIyU20mZ7dK86MssesS': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_gyBbGzyOl1OELEVa164BMB6U': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_YBuM18N6XmRr1S0pbb0KebLZ': [], 'var_call_1s7mjMTzLnG1SdjBr1rHDBdD': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_aOvfJcMOspxp0i7k1dRW6Yaz': [{'Id': '01sWt000000imiTIAQ', 'Name': 'Standard Price Book', 'Description': 'None', 'IsActive': '1', 'ValidFrom': 'None', 'ValidTo': 'None'}], 'var_call_huYSjDyLrrUuxXEdbVAQwjGw': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   ', 'Description': 'Environmentally-friendly PCB design solution with power utilization analytics.', 'IsActive': '1', 'External_ID__c': 'PCB Design Solutions,Power Optimization Tools_4'}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro', 'Description': 'AI-enhanced design tool for seamless circuit synchronization and development.', 'IsActive': '1', 'External_ID__c': 'AI-Powered Circuit Design Tools,Cloud-Based Design Collaboration_21'}], 'var_call_rfMyqEXXcgtw7j5YWIe7Yg83': 'file_storage/call_rfMyqEXXcgtw7j5YWIe7Yg83.json', 'var_call_0j9y4m5zPiAQ7JcM9YLDVSzS': [], 'var_call_vFaDMVKmSsGJjviHfpCaIzfj': [{'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'summary': 'Volume-Based Discounts'}], 'var_call_OU209PffMpbx9tdVBk6MlqHV': [{'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'faq_answer__c': "Volume-based discounts are a strategic tool for fostering customer loyalty and encouraging bulk purchases. At TechPulse Solution, we aim to provide value-added benefits to our customers, and volume-based discounts are integral to this mission. Here is a detailed overview of the volume-based discounts currently available:\n\n1. **5% Discount for Purchases Over $5**: This entry-level discount is designed for customers making modest but regular purchases. If your transaction totals $5 or more, you automatically become eligible for a 5% discount on your total purchase. This incentive is perfect for small businesses or individuals looking to maximize their purchasing power without committing to large upfront investments.\n\n2. **10% Discount for Purchases Over $10**: By increasing your purchase to $10, you can enjoy a more substantial 10% discount. This tier is targeted at growing businesses or tech enthusiasts planning for larger projects. Whether you're a startup needing essential tech solutions or an established entity upgrading current systems, this level of discount allows you to save significant amounts while meeting your needs.\n\n3. **15% Discount for Purchases Over $20**: The highest discount tier is designed for customers planning substantial investments in tech solutions. With a purchase of $20 or more, you can benefit from a generous 15% discount. This is particularly advantageous for businesses engaged in major scaling projects or for those who require extensive tech solutions for operational expansion.\n\nThese volume-based discounts are designed to reward you as you invest more in our innovative solutions, ensuring that you receive the best possible value. They are automatically applied at checkout, simplifying the purchasing process and enabling you to focus on selecting the best technology for your needs.\n\nIncorporating these discounts into your purchasing strategy can significantly reduce costs while allowing access to premium technology and support from TechPulse Solution. Whether you are a small business making selective purchases or a large company procuring extensive solutions, our discount structure provides a tailored approach to meet varying budgetary needs.\n\nOptimize your purchasing strategy and operational efficiency with our volume-based discounts, designed to bring you closer to innovative technology that can drive your success. At TechPulse Solution, your needs are at the forefront, and these carefully crafted discounts provide a pathway to affordable excellence.", 'summary': 'Volume-Based Discounts', 'urlname': '1745269013-mq1zw'}], 'var_call_kUG3HiF3lUBPCRLTtCIHUcam': [{'id': '#ka0Wt000000EpSUIA0', 'title': 'TechPulse Solution Volume-Based Installation Timeline Policy', 'summary': 'TechPulse Solution Volume-Based Installation Timeline Policy'}, {'id': 'ka0Wt000000EorOIAS', 'title': 'Automating Development Processes with AutoGen IDE', 'summary': 'Discussing the benefits of automation in accelerating coding and project setup using AutoGen IDE.'}, {'id': 'ka0Wt000000EoJWIA0', 'title': 'Streamlined Development with AutoGen IDE', 'summary': 'An overview of how AutoGen IDE supports rapid coding and project setup through automation.'}, {'id': 'ka0Wt000000Em4zIAC', 'title': 'Navigating Installation Challenges: Solutions for Seamless Setup of TechPulse EDA Tools', 'summary': "TechPulse Solutions clients sometimes face software installation errors, which can be an obstacle during the initial setup of the company's powerful electronic design automation tools. This article delves into the two main solutions designed to address these challenges effectively. The 'Priority Support Upgrade' offers customers the advantage of faster response times to installation issues, ensuring minimal disruption and timely resolution. Additionally, 'Comprehensive Training Access' equips users with the necessary skills and confidence to handle potential roadblocks in the installation process, fostering a deeper understanding of the product's intricacies. These strategies, together with TechPulse Solutions' commitment to innovation and customer satisfaction, reinforce the seamless integration of their AI-powered solutions into existing workflows, ensuring clients maximize their investment."}]}

exec(code, env_args)
