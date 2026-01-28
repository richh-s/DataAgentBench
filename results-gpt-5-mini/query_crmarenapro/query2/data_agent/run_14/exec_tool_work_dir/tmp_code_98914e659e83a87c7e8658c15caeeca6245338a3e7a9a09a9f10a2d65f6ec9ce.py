code = """import json
# access stored variables
quotes = var_call_H2cqgkxtZKTwYGbN3fsB5MOX
qlis = var_call_dxlhu94sEcG4RQQTm9T5tbj4
products = var_call_sACMVu6qMWeCLBLNVXpFlUDT
k_articles = json.load(open(var_call_fPLLH4nl9Mdxu0QNTcqoFZkN, 'r', encoding='utf-8'))

# normalize numeric fields
def to_float(x):
    try:
        return float(str(x).strip())
    except:
        return 0.0

for q in qlis:
    q['UnitPrice_f'] = to_float(q.get('UnitPrice'))
    q['Quantity_f'] = to_float(q.get('Quantity'))
    q['Discount_f'] = to_float(q.get('Discount'))
    q['TotalPrice_f'] = to_float(q.get('TotalPrice'))

quote_total = sum([q['TotalPrice_f'] for q in qlis])
# compute average discount weighted by line extended price
numer = 0.0
denom = 0.0
for q in qlis:
    line_ext = q['UnitPrice_f'] * q['Quantity_f']
    numer += q['Discount_f'] * line_ext
    denom += line_ext
avg_discount = (numer/denom) if denom else 0.0

# prepare function to find matching knowledge article
import re
violation_id = None
# rule: check articles mentioning discount tiers and approvals; detect if avg_discount exceeds allowed tiers
for art in k_articles:
    text = ' '.join([str(art.get('title','')), str(art.get('faq_answer__c','')), str(art.get('summary',''))]).lower()
    # look for explicit tiers like '5%','10%','15%'
    matches = re.findall(r'(\d{1,2})%\s*discount', text)
    if matches:
        # take max mentioned
        nums = [float(x) for x in matches]
        maxpct = max(nums)
        # if avg discount exceeds maxpct and article mentions approval required beyond that
        if avg_discount > maxpct and ('approval' in text or 'approve' in text or 'requires approval' in text):
            violation_id = art.get('id')
            break
    # check for phrases like 'discount for purchases over $X' -> content describes volume-based discounts
    if 'volume' in text and 'discount' in text:
        # find highest tier percent
        tier_matches = re.findall(r'(\d{1,2})%\s*discount for purchases over \$(\d+)', text)
        if tier_matches:
            # pick highest percent
            percents = [float(m[0]) for m in tier_matches]
            max_tier = max(percents)
            # our avg_discount compared to max_tier
            if avg_discount > max_tier and ('approval' in text or 'requires approval' in text):
                violation_id = art.get('id')
                break
    # check for explicit competing offers policy allowing price matching - that would permit discounts beyond standard
    if 'competing offers' in text:
        # This allows extra discounts if conditions met; so not a violation
        continue

# fallback: if any article mentions 'discount' and 'approval' and avg_discount >10 -> assume violation
if violation_id is None:
    for art in k_articles:
        text = ' '.join([str(art.get('title','')), str(art.get('faq_answer__c','')), str(art.get('summary',''))]).lower()
        if 'discount' in text and ('approval' in text or 'requires approval' in text or 'must be approved' in text):
            if avg_discount > 10.0:
                violation_id = art.get('id')
                break

# Final result
res = violation_id if violation_id is not None else None

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_H2cqgkxtZKTwYGbN3fsB5MOX': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_dxlhu94sEcG4RQQTm9T5tbj4': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_sACMVu6qMWeCLBLNVXpFlUDT': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1', 'UnitPrice': '499.99'}], 'var_call_fPLLH4nl9Mdxu0QNTcqoFZkN': 'file_storage/call_fPLLH4nl9Mdxu0QNTcqoFZkN.json', 'var_call_G60p68XnkSHdgLgSX3fDKzqw': [{'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'faq_answer__c': "Volume-based discounts are a strategic tool for fostering customer loyalty and encouraging bulk purchases. At TechPulse Solution, we aim to provide value-added benefits to our customers, and volume-based discounts are integral to this mission. Here is a detailed overview of the volume-based discounts currently available:\n\n1. **5% Discount for Purchases Over $5**: This entry-level discount is designed for customers making modest but regular purchases. If your transaction totals $5 or more, you automatically become eligible for a 5% discount on your total purchase. This incentive is perfect for small businesses or individuals looking to maximize their purchasing power without committing to large upfront investments.\n\n2. **10% Discount for Purchases Over $10**: By increasing your purchase to $10, you can enjoy a more substantial 10% discount. This tier is targeted at growing businesses or tech enthusiasts planning for larger projects. Whether you're a startup needing essential tech solutions or an established entity upgrading current systems, this level of discount allows you to save significant amounts while meeting your needs.\n\n3. **15% Discount for Purchases Over $20**: The highest discount tier is designed for customers planning substantial investments in tech solutions. With a purchase of $20 or more, you can benefit from a generous 15% discount. This is particularly advantageous for businesses engaged in major scaling projects or for those who require extensive tech solutions for operational expansion.\n\nThese volume-based discounts are designed to reward you as you invest more in our innovative solutions, ensuring that you receive the best possible value. They are automatically applied at checkout, simplifying the purchasing process and enabling you to focus on selecting the best technology for your needs.\n\nIncorporating these discounts into your purchasing strategy can significantly reduce costs while allowing access to premium technology and support from TechPulse Solution. Whether you are a small business making selective purchases or a large company procuring extensive solutions, our discount structure provides a tailored approach to meet varying budgetary needs.\n\nOptimize your purchasing strategy and operational efficiency with our volume-based discounts, designed to bring you closer to innovative technology that can drive your success. At TechPulse Solution, your needs are at the forefront, and these carefully crafted discounts provide a pathway to affordable excellence.", 'summary': 'Volume-Based Discounts'}, {'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers', 'faq_answer__c': 'In a competitive marketplace, flexibility and responsiveness to customer needs are critical to maintaining a successful business operation. TechPulse Solution recognizes that potential clients may be considering multiple vendors for their technological needs. To remain competitive and secure long-term partnerships, we have implemented a Competing Offers Policy. This policy enables us to adjust pricing beyond our standard volume discounts when customers present competing offers from other vendors. By doing this, we aim to not only provide competitive pricing but also demonstrate our commitment to fostering strong business relationships.\n\nThe purpose of the Competing Offers Policy is to ensure that TechPulse Solution remains a preferred and trusted partner for our customers by being agile in our pricing strategies. It is our goal to provide the best value for our products and services without compromising on quality. This policy allows us to go beyond conventional pricing models, offering a customizable approach that reflects real-world scenarios where customers seek the most beneficial options for their budget and requirements.\n\nFor the Competing Offers Policy to be applied effectively, certain guidelines must be met:\n\n1. **Validity of Competing Offer**: Customers must present a valid, written offer from another vendor that outlines the competing price. This offer should be current and applicable to the same product or service specifications that TechPulse Solution provides. This ensures fairness and transparency in the pricing review process.\n\n2. **Product or Service Equivalence**: The competing offer must pertain to an equivalent product or service. TechPulse Solution will evaluate the specifications, features, and service terms to ensure comparability. This step is crucial to maintaining the integrity of the policy and ensuring that our response is aligned with the market landscape.\n\n3. **Review and Approval Process**: Once a competing offer is submitted, it will undergo a review process by our sales and management team to assess the feasibility of matching or improving the offer. Decisions will be guided by strategic business considerations, including potential long-term value, business volume, and relationship history with the client.\n\n4. **Volume and Contractual Commitments**: While our standard volume discounts apply to larger purchases, the Competing Offers Policy may further enhance discounts if it aligns with TechPulse Solution’s business objectives. In some cases, additional discounts may be contingent on contractual commitments or meeting certain purchase thresholds.\n\n5. **Timeliness**: Customers are encouraged to bring competing offers to our attention promptly, as this policy is best applied when potential savings can be realized in a timely manner. Delays can impact our ability to respond effectively and capitalize on market opportunities.\n\nThrough our Competing Offers Policy, TechPulse Solution aims to offer exceptional value and retain our competitive edge in the industry. While the policy is designed to provide flexibility in pricing, it ensures that each adjustment maintains the high standards of quality and support associated with our brand. By adopting this responsive approach, we aim to build enduring partnerships and deliver solutions that meet the diverse needs of our customers.', 'summary': 'Policy for price adjustments based on competing offers'}], 'var_call_cu7wCw0YEBdnryrlMERQY0m0': [{'Id': '#001Wt00000PGXrKIAX', 'Name': 'InnovateX Solutions'}]}

exec(code, env_args)
