code = """import json

# Load the quote and line items from storage
quote_result = var_functions.query_db:0
quotelineitems_result = var_functions.query_db:2

quote = quote_result[0]
line_items = quotelineitems_result

print('Quote details:')
print(f"  Quote ID: {quote['Id']}")
print(f"  Status: {quote['Status']}")
print(f"  Opportunity ID: {quote['OpportunityId']}")

print('\nLine items:')
total_quote_value = 0
for item in line_items:
    total_price = float(item['TotalPrice'])
    discount = float(item['Discount'])
    quantity = float(item['Quantity'])
    unit_price = float(item['UnitPrice'])
    
    # Calculate what the undiscounted total would be
    undiscounted_total = quantity * unit_price
    discounted_total = float(item['TotalPrice'])
    
    print(f"  Item: {item['Id']}")
    print(f"    Product: {item['Product2Id']}")
    print(f"    Quantity: {quantity}")
    print(f"    Unit Price: ${unit_price}")
    print(f"    Discount: {discount}%")
    print(f"    Undiscounted Total: ${undiscounted_total:.2f}")
    print(f"    Discounted Total: ${discounted_total:.2f}")
    print()
    
    total_quote_value += discounted_total

print(f'Total quote value: ${total_quote_value:.2f}')

# Check discounts against Volume-Based Discounts policy
print('\n--- Policy Analysis ---')
print('Volume-Based Discounts Policy:')
print('  - 5% Discount for Purchases Over $5')
print('  - 10% Discount for Purchases Over $10')
print('  - 15% Discount for Purchases Over $20')
print()

violations = []

for item in line_items:
    total_price = float(item['TotalPrice'])
    discount = float(item['Discount'])
    
    # Determine what discount should be applied based on total price
    expected_discount = 0
    if total_price >= 20:
        expected_discount = 15
    elif total_price >= 10:
        expected_discount = 10
    elif total_price >= 5:
        expected_discount = 5
    
    # Check if applied discount matches expected discount
    if discount != expected_discount and discount > 0:
        violations.append({
            'item_id': item['Id'],
            'applied_discount': discount,
            'expected_discount': expected_discount,
            'total_price': total_price,
            'reason': f'Applied discount ({discount}%) does not match policy for purchase amount ${total_price:.2f}'
        })

if violations:
    print('VIOLATIONS FOUND:')
    for i, violation in enumerate(violations, 1):
        print(f"  {i}. Item {violation['item_id']}: {violation['reason']}")
    print()
else:
    print('No discount violations found based on volume thresholds.')
    print()

# Check if quote status indicates approval is needed
if quote['Status'] == 'Needs Review':
    print('Quote status is "Needs Review" - this indicates approval may be required.')
    print('Competing Offers Policy (ka0Wt000000EnthIAC) states:')
    print('  "Review and Approval Process: Once a competing offer is submitted, it will undergo')
    print('   a review process by our sales and management team..."')
    print()

result = {
    'quote_id': quote['Id'],
    'total_value': total_quote_value,
    'status': quote['Status'],
    'violations_found': len(violations) > 0,
    'violations': violations,
    'knowledge_articles_checked': [
        'ka0Wt000000Eq0MIAS',  # Volume-Based Discounts
        'ka0Wt000000EnthIAC'   # Competing Offers
    ]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers', 'faq_answer__c': 'In a competitive marketplace, flexibility and responsiveness to customer needs are critical to maintaining a successful business operation. TechPulse Solution recognizes that potential clients may be considering multiple vendors for their technological needs. To remain competitive and secure long-term partnerships, we have implemented a Competing Offers Policy. This policy enables us to adjust pricing beyond our standard volume discounts when customers present competing offers from other vendors. By doing this, we aim to not only provide competitive pricing but also demonstrate our commitment to fostering strong business relationships.\n\nThe purpose of the Competing Offers Policy is to ensure that TechPulse Solution remains a preferred and trusted partner for our customers by being agile in our pricing strategies. It is our goal to provide the best value for our products and services without compromising on quality. This policy allows us to go beyond conventional pricing models, offering a customizable approach that reflects real-world scenarios where customers seek the most beneficial options for their budget and requirements.\n\nFor the Competing Offers Policy to be applied effectively, certain guidelines must be met:\n\n1. **Validity of Competing Offer**: Customers must present a valid, written offer from another vendor that outlines the competing price. This offer should be current and applicable to the same product or service specifications that TechPulse Solution provides. This ensures fairness and transparency in the pricing review process.\n\n2. **Product or Service Equivalence**: The competing offer must pertain to an equivalent product or service. TechPulse Solution will evaluate the specifications, features, and service terms to ensure comparability. This step is crucial to maintaining the integrity of the policy and ensuring that our response is aligned with the market landscape.\n\n3. **Review and Approval Process**: Once a competing offer is submitted, it will undergo a review process by our sales and management team to assess the feasibility of matching or improving the offer. Decisions will be guided by strategic business considerations, including potential long-term value, business volume, and relationship history with the client.\n\n4. **Volume and Contractual Commitments**: While our standard volume discounts apply to larger purchases, the Competing Offers Policy may further enhance discounts if it aligns with TechPulse Solution’s business objectives. In some cases, additional discounts may be contingent on contractual commitments or meeting certain purchase thresholds.\n\n5. **Timeliness**: Customers are encouraged to bring competing offers to our attention promptly, as this policy is best applied when potential savings can be realized in a timely manner. Delays can impact our ability to respond effectively and capitalize on market opportunities.\n\nThrough our Competing Offers Policy, TechPulse Solution aims to offer exceptional value and retain our competitive edge in the industry. While the policy is designed to provide flexibility in pricing, it ensures that each adjustment maintains the high standards of quality and support associated with our brand. By adopting this responsive approach, we aim to build enduring partnerships and deliver solutions that meet the diverse needs of our customers.'}], 'var_functions.query_db:16': [{'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers', 'faq_answer__c': 'In a competitive marketplace, flexibility and responsiveness to customer needs are critical to maintaining a successful business operation. TechPulse Solution recognizes that potential clients may be considering multiple vendors for their technological needs. To remain competitive and secure long-term partnerships, we have implemented a Competing Offers Policy. This policy enables us to adjust pricing beyond our standard volume discounts when customers present competing offers from other vendors. By doing this, we aim to not only provide competitive pricing but also demonstrate our commitment to fostering strong business relationships.\n\nThe purpose of the Competing Offers Policy is to ensure that TechPulse Solution remains a preferred and trusted partner for our customers by being agile in our pricing strategies. It is our goal to provide the best value for our products and services without compromising on quality. This policy allows us to go beyond conventional pricing models, offering a customizable approach that reflects real-world scenarios where customers seek the most beneficial options for their budget and requirements.\n\nFor the Competing Offers Policy to be applied effectively, certain guidelines must be met:\n\n1. **Validity of Competing Offer**: Customers must present a valid, written offer from another vendor that outlines the competing price. This offer should be current and applicable to the same product or service specifications that TechPulse Solution provides. This ensures fairness and transparency in the pricing review process.\n\n2. **Product or Service Equivalence**: The competing offer must pertain to an equivalent product or service. TechPulse Solution will evaluate the specifications, features, and service terms to ensure comparability. This step is crucial to maintaining the integrity of the policy and ensuring that our response is aligned with the market landscape.\n\n3. **Review and Approval Process**: Once a competing offer is submitted, it will undergo a review process by our sales and management team to assess the feasibility of matching or improving the offer. Decisions will be guided by strategic business considerations, including potential long-term value, business volume, and relationship history with the client.\n\n4. **Volume and Contractual Commitments**: While our standard volume discounts apply to larger purchases, the Competing Offers Policy may further enhance discounts if it aligns with TechPulse Solution’s business objectives. In some cases, additional discounts may be contingent on contractual commitments or meeting certain purchase thresholds.\n\n5. **Timeliness**: Customers are encouraged to bring competing offers to our attention promptly, as this policy is best applied when potential savings can be realized in a timely manner. Delays can impact our ability to respond effectively and capitalize on market opportunities.\n\nThrough our Competing Offers Policy, TechPulse Solution aims to offer exceptional value and retain our competitive edge in the industry. While the policy is designed to provide flexibility in pricing, it ensures that each adjustment maintains the high standards of quality and support associated with our brand. By adopting this responsive approach, we aim to build enduring partnerships and deliver solutions that meet the diverse needs of our customers.'}]}

exec(code, env_args)
