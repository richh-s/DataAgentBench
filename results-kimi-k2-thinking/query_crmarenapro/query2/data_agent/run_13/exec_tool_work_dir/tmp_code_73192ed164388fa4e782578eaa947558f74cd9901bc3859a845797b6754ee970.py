code = """import json

# Analyze the quote and knowledge articles
quote_data = var_functions_query_db_2
quote_items = var_functions_query_db_5
knowledge_articles = var_functions_query_db_18

print("=== QUOTE ANALYSIS ===")
print("Quote ID:", quote_data[0]['Id'])
print("Status:", quote_data[0]['Status'])
print()

print("Quote Line Items:")
total_quantity = 0
total_amount = 0
for item in quote_items:
    quantity = float(item['Quantity'])
    discount = float(item['Discount'])
    total_price = float(item['TotalPrice'])
    
    total_quantity += quantity
    total_amount += total_price
    
    print(f"  Product: {item['Product2Id']}")
    print(f"    Quantity: {quantity}")
    print(f"    Discount: {discount}%")
    print(f"    Total Price: ${total_price:.2f}")
    print()

print(f"TOTALS:")
print(f"  Total Quantity: {total_quantity}")
print(f"  Total Amount: ${total_amount:.2f}")
print()

print("=== KNOWLEDGE ARTICLES ANALYSIS ===")
for article in knowledge_articles:
    print(f"ID: {article['id']}")
    print(f"Title: {article['title']}")
    print(f"Summary: {article['summary']}")
    print()

# Check for policy violations
print("=== POLICY VIOLATION CHECK ===")

# Check Volume-Based Discounts policy (ka0Wt000000Eq0MIAS)
print("Checking Volume-Based Discounts policy...")
if total_amount > 20:
    print(f"  ✓ Total amount ${total_amount:.2f} exceeds $20 threshold")
    print(f"  ✓ According to policy, should receive 15% discount on entire purchase")
    
    # Check if all items have 15% discount
    all_items_have_15_discount = all(float(item['Discount']) == 15.0 for item in quote_items)
    
    if not all_items_have_15_discount:
        print(f"  ✗ VIOLATION: Not all items have 15% discount")
        print(f"  ✗ Found discounts: {[float(item['Discount']) for item in quote_items]}")
        print(f"  ✗ This violates article: ka0Wt000000Eq0MIAS")
        violation_article = "ka0Wt000000Eq0MIAS"
    else:
        print(f"  ✓ All items have correct 15% discount")
        violation_article = None
else:
    print(f"  ✓ Total amount ${total_amount:.2f} does not exceed $20 threshold")
    violation_article = None

print()

# Output final result
if violation_article:
    print("VIOLATION FOUND:", violation_article)
else:
    print("NO VIOLATION FOUND")

print("__RESULT__:")
print(json.dumps(violation_article))"""

env_args = {'var_functions.list_db:0': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_functions.query_db:2': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:5': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.list_db:6': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': [{'id': '#ka0Wt000000EpSUIA0', 'title': 'TechPulse Solution Volume-Based Installation Timeline Policy', 'faq_answer__c': 'TechPulse Solution Volume-Based Installation Timeline Policy\n\nAt TechPulse Solution, we understand that time is of the essence when deploying new technologies, which is why we have crafted a clear and efficient volume-based installation timeline policy. This policy ensures that our installation and setup services align with your purchase volume, providing a structured approach that is both predictable and reliable for your business needs.\n\nTo cater to varying scales of purchase and to maintain a streamlined installation process, we have implemented specific timelines based on the quantity of units purchased. Below, you will find the detailed schedule outlining the installation timelines according to different purchase volumes:\n\n1. **Single Unit Purchase (Volume: 1)**  \n   For customers purchasing a single unit, we offer rapid installation services, completing the process within a single day. This timeline guarantees that even small-scale acquisitions receive prompt attention and quick operational readiness.\n\n2. **Small Batch Purchase (Volume: 5)**  \n   When purchasing a slightly larger batch of 5 units, our installation timeline extends to 3 days. This duration allows our team to efficiently manage and deploy the necessary resources and services to ensure each unit is correctly installed and fully operational.\n\n3. **Medium Batch Purchase (Volume: 15)**  \n   For medium batch purchases involving 15 units, our installation timeline is planned at 7 days. This one-week period is carefully designed to accommodate the increased complexity and coordination required to handle a higher volume of installations while maintaining exceptional service standards.\n\n4. **Large Batch Purchase (Volume: 25)**  \n   In cases where our clients opt for a large batch of 25 units, the installation timeline extends to 14 days. This two-week window allows our team to meticulously address all logistical, technical, and quality assurance aspects associated with larger deployments, ensuring seamless integration into your existing infrastructure.\n\nBy adhering to these predefined timelines, TechPulse Solution aims to provide transparent expectations and optimal customer service. Our commitment to delivering excellence, regardless of the size of the purchase, ensures that each client receives the comprehensive support they deserve, enhancing the overall technology deployment experience.\n\nIt is important to note that all timelines are subject to the availability of inventory and resources at the time of purchase. We recommend coordinating with your account manager to discuss any specific requirements that may necessitate timeline adjustments, allowing us to tailor our installations to your company’s unique operational schedule.\n\nShould you have any questions or require further details about our installation processes, please do not hesitate to contact us. TechPulse Solution remains dedicated to supporting your technological advancements with precision and efficiency, ensuring your investments bring maximum value to your organization.', 'summary': 'TechPulse Solution Volume-Based Installation Timeline Policy', 'urlname': '1745269013-n1rg3'}, {'id': 'ka0Wt000000EqQ9IAK', 'title': "Understanding TechPulse's Return Policy for Purchased Items", 'faq_answer__c': "TechPulse Solutions is committed to ensuring customer satisfaction with a clear, customer-focused return policy for its purchased items. This policy outlines the processes for returns, refunds, and exchanges, ensuring a seamless experience for all customers while reinforcing TechPulse’s dedication to transparency and quality.\n\nFirstly, TechPulse acknowledges that sometimes products might not meet customer expectations or specific needs. To address this, the company offers a straightforward return process. Customers can initiate a return request within 30 days from the date of purchase. It’s essential that the products are returned in their original condition, with all components, manuals, and accessories included. This ensures that the items can either be resold or appropriately processed.\n\nTo initiate a return, customers can easily access their accounts on the TechPulse website or contact the customer support team directly. The process is designed to be user-friendly, reflecting TechPulse's emphasis on a seamless customer experience. After initiating a return, customers will receive a prepaid shipping label to make the return process as convenient as possible.\n\nUpon receiving and inspecting the returned items, TechPulse aims to process refunds swiftly. Typically, refunds are issued within 7-10 business days to the original payment method, ensuring a prompt resolution. In certain situations, TechPulse might offer store credit or exchanges as alternatives, based on customer preferences and the specifics of the transaction.\n\nTechPulse also understands that customers may sometimes require exchanges instead of refunds. Whether due to product malfunction or a desire for a different item, exchanges are handled with utmost efficiency. Customers are encouraged to contact customer support to discuss their needs and identify solutions that best match their requirements, further solidifying TechPulse’s commitment to delivering personalized service.\n\nFurthermore, for products demonstrating manufacturing defects, TechPulse has a robust system in place for resolution. The company commits to replacing or repairing defective products at no additional cost to the customer, showcasing their commitment to quality and reliability.\n\nBeyond procedural details, TechPulse’s return policy underscores the importance of transparency and open communication. By providing clear guidelines and exceptional support during the return process, TechPulse strives to build trust and foster long-lasting customer relationships. This policy not only reflects TechPulse’s focus on customer satisfaction but also its broader strategic objective of fostering collaborative relationships that ensure mutual success in the rapidly evolving technological marketplace.\n\nFor additional support or clarification regarding the return policy, TechPulse encourages customers to reach out directly. Their dedicated customer service team is always ready to assist, ensuring every customer interaction aligns with the company’s high standards for excellence and care.", 'summary': "Details of TechPulse Solutions' return policy for purchased items, outlining the process for returns, refunds, and exchanges to ensure transparency and customer satisfaction.", 'urlname': '1745269013-p6yto'}, {'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'faq_answer__c': "Volume-based discounts are a strategic tool for fostering customer loyalty and encouraging bulk purchases. At TechPulse Solution, we aim to provide value-added benefits to our customers, and volume-based discounts are integral to this mission. Here is a detailed overview of the volume-based discounts currently available:\n\n1. **5% Discount for Purchases Over $5**: This entry-level discount is designed for customers making modest but regular purchases. If your transaction totals $5 or more, you automatically become eligible for a 5% discount on your total purchase. This incentive is perfect for small businesses or individuals looking to maximize their purchasing power without committing to large upfront investments.\n\n2. **10% Discount for Purchases Over $10**: By increasing your purchase to $10, you can enjoy a more substantial 10% discount. This tier is targeted at growing businesses or tech enthusiasts planning for larger projects. Whether you're a startup needing essential tech solutions or an established entity upgrading current systems, this level of discount allows you to save significant amounts while meeting your needs.\n\n3. **15% Discount for Purchases Over $20**: The highest discount tier is designed for customers planning substantial investments in tech solutions. With a purchase of $20 or more, you can benefit from a generous 15% discount. This is particularly advantageous for businesses engaged in major scaling projects or for those who require extensive tech solutions for operational expansion.\n\nThese volume-based discounts are designed to reward you as you invest more in our innovative solutions, ensuring that you receive the best possible value. They are automatically applied at checkout, simplifying the purchasing process and enabling you to focus on selecting the best technology for your needs.\n\nIncorporating these discounts into your purchasing strategy can significantly reduce costs while allowing access to premium technology and support from TechPulse Solution. Whether you are a small business making selective purchases or a large company procuring extensive solutions, our discount structure provides a tailored approach to meet varying budgetary needs.\n\nOptimize your purchasing strategy and operational efficiency with our volume-based discounts, designed to bring you closer to innovative technology that can drive your success. At TechPulse Solution, your needs are at the forefront, and these carefully crafted discounts provide a pathway to affordable excellence.", 'summary': 'Volume-Based Discounts', 'urlname': '1745269013-mq1zw'}]}

exec(code, env_args)
