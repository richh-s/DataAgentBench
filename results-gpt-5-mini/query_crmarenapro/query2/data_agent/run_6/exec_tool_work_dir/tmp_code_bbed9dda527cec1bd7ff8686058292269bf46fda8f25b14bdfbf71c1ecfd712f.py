code = """import json
# Access quote line items
qlis = var_call_G8theRiwNOA3qE2TtGGOEW0x

pre_total = 0.0
post_total = 0.0
for li in qlis:
    qty = float(li.get('Quantity') or 0)
    unit = float(li.get('UnitPrice') or 0)
    disc = float(li.get('Discount') or 0)
    total_price = float(li.get('TotalPrice') or 0)
    pre_total += qty * unit
    post_total += total_price

# Determine expected discount based on Volume-Based Discounts policy
if pre_total > 20:
    expected_rate = 0.15
elif pre_total > 10:
    expected_rate = 0.10
elif pre_total > 5:
    expected_rate = 0.05
else:
    expected_rate = 0.0

actual_rate = 0.0
if pre_total > 0:
    actual_rate = (pre_total - post_total) / pre_total

# check within tolerance
violation = not (abs(actual_rate - expected_rate) < 1e-6)

result = None
if violation:
    result = 'ka0Wt000000Eq0MIAS'
else:
    result = None

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_LtvV6QNm6OcSbcFu8sKlqZqE': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_G8theRiwNOA3qE2TtGGOEW0x': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_lS7HCxMmAq6QWYMeq2KTu5TM': [], 'var_call_I5sOXMpuQFvXTv11ONbKEv96': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_UNg7enQnQkxW9cXuXpjvfZMV': [], 'var_call_qTbXKcII5Y6w6wZnKwWPhdG1': 'file_storage/call_qTbXKcII5Y6w6wZnKwWPhdG1.json', 'var_call_D6UIsEemRqV12NwDKnHbnAJH': 'file_storage/call_D6UIsEemRqV12NwDKnHbnAJH.json', 'var_call_xHv5UWaguJEYlQt0W3j69SYq': [{'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'summary': 'Volume-Based Discounts'}, {'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers', 'summary': 'Policy for price adjustments based on competing offers'}], 'var_call_JbbepE7ctMSAgKUo2AfwsqTY': [{'Id': '#001Wt00000PGXrKIAX', 'Name': 'InnovateX Solutions'}], 'var_call_mpVCCPBcQY9OKfPmjSVa9XBD': [{'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'summary': 'Volume-Based Discounts'}, {'id': '#ka0Wt000000EpSUIA0', 'title': 'TechPulse Solution Volume-Based Installation Timeline Policy', 'summary': 'TechPulse Solution Volume-Based Installation Timeline Policy'}], 'var_call_E9ML9elkgx7cR41E7k2RVxF1': [{'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'faq_answer__c': "Volume-based discounts are a strategic tool for fostering customer loyalty and encouraging bulk purchases. At TechPulse Solution, we aim to provide value-added benefits to our customers, and volume-based discounts are integral to this mission. Here is a detailed overview of the volume-based discounts currently available:\n\n1. **5% Discount for Purchases Over $5**: This entry-level discount is designed for customers making modest but regular purchases. If your transaction totals $5 or more, you automatically become eligible for a 5% discount on your total purchase. This incentive is perfect for small businesses or individuals looking to maximize their purchasing power without committing to large upfront investments.\n\n2. **10% Discount for Purchases Over $10**: By increasing your purchase to $10, you can enjoy a more substantial 10% discount. This tier is targeted at growing businesses or tech enthusiasts planning for larger projects. Whether you're a startup needing essential tech solutions or an established entity upgrading current systems, this level of discount allows you to save significant amounts while meeting your needs.\n\n3. **15% Discount for Purchases Over $20**: The highest discount tier is designed for customers planning substantial investments in tech solutions. With a purchase of $20 or more, you can benefit from a generous 15% discount. This is particularly advantageous for businesses engaged in major scaling projects or for those who require extensive tech solutions for operational expansion.\n\nThese volume-based discounts are designed to reward you as you invest more in our innovative solutions, ensuring that you receive the best possible value. They are automatically applied at checkout, simplifying the purchasing process and enabling you to focus on selecting the best technology for your needs.\n\nIncorporating these discounts into your purchasing strategy can significantly reduce costs while allowing access to premium technology and support from TechPulse Solution. Whether you are a small business making selective purchases or a large company procuring extensive solutions, our discount structure provides a tailored approach to meet varying budgetary needs.\n\nOptimize your purchasing strategy and operational efficiency with our volume-based discounts, designed to bring you closer to innovative technology that can drive your success. At TechPulse Solution, your needs are at the forefront, and these carefully crafted discounts provide a pathway to affordable excellence.", 'summary': 'Volume-Based Discounts'}]}

exec(code, env_args)
