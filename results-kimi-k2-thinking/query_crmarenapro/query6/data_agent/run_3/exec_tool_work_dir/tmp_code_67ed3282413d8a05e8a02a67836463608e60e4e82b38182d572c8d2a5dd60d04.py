code = """import json

# Read the quote line items from storage
line_items_raw = '''[
  {"Id": "0QLWt0000022j3GOAQ", "QuoteId": "0Q0Wt000001WRAzKAO", "OpportunityLineItemId": "00kWt000002HUwhIAG", "Product2Id": "#01tWt000006hV6jIAE", "PricebookEntryId": "01uWt0000027P8bIAE", "Quantity": "3.0", "UnitPrice": "349.99", "Discount": "0.0", "TotalPrice": "1049.97"},
  {"Id": "0QLWt0000022j81OAA", "QuoteId": "0Q0Wt000001WRAzKAO", "OpportunityLineItemId": "00kWt000002HHRkIAO", "Product2Id": "01tWt000006hV8LIAU", "PricebookEntryId": "01uWt0000027P8cIAE", "Quantity": "3.0", "UnitPrice": "529.99", "Discount": "0.0", "TotalPrice": "1059.98"},
  {"Id": "0QLWt0000022n8TOAQ", "QuoteId": "0Q0Wt000001WRAzKAO", "OpportunityLineItemId": "00kWt000002HQJYIA4", "Product2Id": "#01tWt000006hPffIAE", "PricebookEntryId": "01uWt0000027PADIA2", "Quantity": "4.0", "UnitPrice": "299.99", "Discount": "0.0", "TotalPrice": "1199.96"},
  {"Id": "#0QLWt0000022oAvOAI", "QuoteId": "0Q0Wt000001WRAzKAO", "OpportunityLineItemId": "00kWt000002HQJZIA4", "Product2Id": "01tWt000006hVczIAE", "PricebookEntryId": "01uWt0000027Pi5IAE", "Quantity": "35.0", "UnitPrice": "399.99", "Discount": "15.0", "TotalPrice": "11899.7025"}
]'''

line_items = json.loads(line_items_raw)

# Analyze the quote configuration
print("=== QUOTE ANALYSIS ===")
print(f"Quote ID: 0Q0Wt000001WRAzKAO")
print(f"Total Line Items: {len(line_items)}")
print()

total_amount = 0
max_quantity = 0
max_discount = 0
violations_found = []

for item in line_items:
    quantity = float(item['Quantity'])
    unit_price = float(item['UnitPrice'])
    discount = float(item['Discount'])
    total_price = float(item['TotalPrice'])
    product_id = item['Product2Id'].replace('#', '')
    
    total_amount += total_price
    
    if quantity > max_quantity:
        max_quantity = quantity
    
    if discount > max_discount:
        max_discount = discount
    
    print(f"Product: {product_id}")
    print(f"  Quantity: {quantity}")
    print(f"  Unit Price: ${unit_price:.2f}")
    print(f"  Discount: {discount}%")
    print(f"  Line Total: ${total_price:.2f}")
    print()

print(f"=== SUMMARY ===")
print(f"Total Quote Amount: ${total_amount:.2f}")
print(f"Maximum Quantity: {max_quantity}")
print(f"Maximum Discount: {max_discount}%")
print()

# Check for potential violations based on common business rules
if max_quantity > 25:
    violations_found.append(f"Quantity violation: Maximum quantity of {max_quantity} exceeds typical single line item limit")

if max_discount > 10:
    violations_found.append(f"Discount violation: Maximum discount of {max_discount}% exceeds standard approval threshold")

if total_amount > 20000:
    violations_found.append(f"Total amount violation: Quote total of ${total_amount:.2f} exceeds standard approval limit")

if violations_found:
    print("=== POTENTIAL VIOLATIONS DETECTED ===")
    for i, violation in enumerate(violations_found, 1):
        print(f"{i}. {violation}")
else:
    print("No obvious violations detected based on standard rules")

print("__RESULT__:")
print(json.dumps({
    "quote_id": "0Q0Wt000001WRAzKAO",
    "total_amount": total_amount,
    "max_quantity": max_quantity,
    "max_discount": max_discount,
    "violations": violations_found,
    "line_items": line_items
}))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_functions.query_db:4': [{'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers', 'faq_answer__c': 'In a competitive marketplace, flexibility and responsiveness to customer needs are critical to maintaining a successful business operation. TechPulse Solution recognizes that potential clients may be considering multiple vendors for their technological needs. To remain competitive and secure long-term partnerships, we have implemented a Competing Offers Policy. This policy enables us to adjust pricing beyond our standard volume discounts when customers present competing offers from other vendors. By doing this, we aim to not only provide competitive pricing but also demonstrate our commitment to fostering strong business relationships.\n\nThe purpose of the Competing Offers Policy is to ensure that TechPulse Solution remains a preferred and trusted partner for our customers by being agile in our pricing strategies. It is our goal to provide the best value for our products and services without compromising on quality. This policy allows us to go beyond conventional pricing models, offering a customizable approach that reflects real-world scenarios where customers seek the most beneficial options for their budget and requirements.\n\nFor the Competing Offers Policy to be applied effectively, certain guidelines must be met:\n\n1. **Validity of Competing Offer**: Customers must present a valid, written offer from another vendor that outlines the competing price. This offer should be current and applicable to the same product or service specifications that TechPulse Solution provides. This ensures fairness and transparency in the pricing review process.\n\n2. **Product or Service Equivalence**: The competing offer must pertain to an equivalent product or service. TechPulse Solution will evaluate the specifications, features, and service terms to ensure comparability. This step is crucial to maintaining the integrity of the policy and ensuring that our response is aligned with the market landscape.\n\n3. **Review and Approval Process**: Once a competing offer is submitted, it will undergo a review process by our sales and management team to assess the feasibility of matching or improving the offer. Decisions will be guided by strategic business considerations, including potential long-term value, business volume, and relationship history with the client.\n\n4. **Volume and Contractual Commitments**: While our standard volume discounts apply to larger purchases, the Competing Offers Policy may further enhance discounts if it aligns with TechPulse Solution’s business objectives. In some cases, additional discounts may be contingent on contractual commitments or meeting certain purchase thresholds.\n\n5. **Timeliness**: Customers are encouraged to bring competing offers to our attention promptly, as this policy is best applied when potential savings can be realized in a timely manner. Delays can impact our ability to respond effectively and capitalize on market opportunities.\n\nThrough our Competing Offers Policy, TechPulse Solution aims to offer exceptional value and retain our competitive edge in the industry. While the policy is designed to provide flexibility in pricing, it ensures that each adjustment maintains the high standards of quality and support associated with our brand. By adopting this responsive approach, we aim to build enduring partnerships and deliver solutions that meet the diverse needs of our customers.', 'summary': 'Policy for price adjustments based on competing offers', 'urlname': '1745269013-7zuul'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
