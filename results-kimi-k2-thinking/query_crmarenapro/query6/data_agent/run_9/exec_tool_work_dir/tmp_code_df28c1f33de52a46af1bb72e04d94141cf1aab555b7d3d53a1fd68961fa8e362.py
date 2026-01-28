code = """import json

# Parse and clean data
line_items = locals()['var_functions.query_db:0']
pricebook_entries = {entry['Id']: entry for entry in locals()['var_functions.query_db:6']}

# Calculate expected discounts based on Volume-Based Discounts policy
policy_id = "ka0Wt000000Eq0MIAS"
validation_results = []

for item in line_items:
    quote_id = item['QuoteId']
    total_price = float(item['TotalPrice'])
    current_discount = float(item['Discount'])
    
    # Determine expected discount based on policy
    if total_price >= 20:
        expected_discount = 15.0
    elif total_price >= 10:
        expected_discount = 10.0
    elif total_price >= 5:
        expected_discount = 5.0
    else:
        expected_discount = 0.0
    
    # Check if discount is correct
    is_valid = abs(current_discount - expected_discount) < 0.01
    
    validation_results.append({
        'line_item_id': item['Id'],
        'total_price': total_price,
        'current_discount': current_discount,
        'expected_discount': expected_discount,
        'is_valid': is_valid
    })

# Overall validation
all_valid = all(result['is_valid'] for result in validation_results)

total_quote_amount = sum(float(item['TotalPrice']) for item in line_items)

print("__RESULT__:")
print(json.dumps({
    'quote_id': '0Q0Wt000001WRAzKAO',
    'total_quote_amount': total_quote_amount,
    'line_items_checked': len(line_items),
    'validation_passed': all_valid,
    'violations': [result for result in validation_results if not result['is_valid']],
    'knowledge_article_id': policy_id
}))"""

env_args = {'var_functions.query_db:0': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_functions.query_db:2': [], 'var_functions.execute_python:4': {'line_items_count': 4, 'line_items_sample': {'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, 'quote_found': False, 'quote_preview': []}, 'var_functions.query_db:6': [{'Id': '01uWt0000027P8cIAE', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV8LIAU', 'UnitPrice': '529.99'}, {'Id': '01uWt0000027PADIA2', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hPffIAE', 'UnitPrice': '299.99'}, {'Id': '01uWt0000027Pi5IAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVczIAE', 'UnitPrice': '399.99'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'knowledge_file_path': 'file_storage/functions.query_db:8.json', 'type': "<class 'str'>"}, 'var_functions.execute_python:12': {'total_articles': 194, 'sample_titles': ['ka0Wt000000EpXNIA0: Competitor: Quantum Circuits Inc', 'ka0Wt000000EowFIAS: Competitor: Adaptive Design Solutions', '#ka0Wt000000EqRlIAK: Competitor: NanoDesign Systems   ', 'ka0Wt000000EqTNIA0: Competitor: AI Chip Design Corp', 'ka0Wt000000Eo8IIAS: Competitor: CircuitWave Technologies  ', 'ka0Wt000000Eot0IAC: Competitor: FlexEDA Innovations', 'ka0Wt000000Eq0MIAS: Volume-Based Discounts', "ka0Wt000000EqQ9IAK: Understanding TechPulse's Return Policy for Purchased Items", 'ka0Wt000000EqA3IAK: Customer Feedback and Improvement Initiatives at TechPulse', '#ka0Wt000000EpSUIA0: TechPulse Solution Volume-Based Installation Timeline Policy', 'ka0Wt000000EqOXIA0: Cultivating Long-Term Client Relationships at TechPulse', 'ka0Wt000000EqMvIAK: Navigating Tech Support for Swift Issue Resolution', "#ka0Wt000000Eo8HIAS: TechPulse's Commitment to Exceptional Customer Service", '#ka0Wt000000EqLJIA0: Training Excellence with TrainEDU Suite', 'ka0Wt000000Ep7XIAS: Interactive Learning with EduFlow Academy', 'ka0Wt000000EqI7IAK: Advanced EDA Education with InnoTrain Hub', 'ka0Wt000000EqJiIAK: Comprehensive EDA Training with EduTech Advance', 'ka0Wt000000Eq1yIAC: Seamless Integration of EduFlow Academy in EDA Training', 'ka0Wt000000EptuIAC: Streamlining Workflow with AI-Powered Circuit Design', 'ka0Wt000000EpXLIA0: Optimizing Power Utilization Across EDA Projects   ']}, 'var_functions.query_db:14': [{'id': 'ka0Wt000000EqTNIA0', 'title': 'Competitor: AI Chip Design Corp'}, {'id': 'ka0Wt000000Eo8IIAS', 'title': 'Competitor: CircuitWave Technologies  '}, {'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts'}, {'id': 'ka0Wt000000EpXLIA0', 'title': 'Optimizing Power Utilization Across EDA Projects   '}, {'id': '#ka0Wt000000EpYxIAK', 'title': 'Improving Workflow Automation with Workflow Genius'}, {'id': '#ka0Wt000000EqErIAK', 'title': 'Securing Data Transactions in EDA'}, {'id': 'ka0Wt000000EmklIAC', 'title': 'Advancing PCB Design with AI and Eco-Friendly Solutions'}, {'id': 'ka0Wt000000Eq1xIAC', 'title': 'Advancements in Workflow Automation Tools'}, {'id': 'ka0Wt000000EpU6IAK', 'title': 'Comprehensive Security for Collaborative Design'}, {'id': '#ka0Wt000000EpttIAC', 'title': 'Enhancing EDA Security with AI'}, {'id': 'ka0Wt000000EpViIAK', 'title': 'Unified Simulation Platforms for Enhanced Design Testing  '}, {'id': '#ka0Wt000000Epp3IAC', 'title': 'Secure Data Management in Electronic Design'}, {'id': 'ka0Wt000000EpFbIAK', 'title': 'AI-Enhanced Security Modules in EDA'}, {'id': 'ka0Wt000000EooBIAS', 'title': 'Security and Compliance in EDA Platforms'}, {'id': 'ka0Wt000000EpNgIAK', 'title': 'Dynamic Security Strategies with SecuManage Pro'}, {'id': 'ka0Wt000000EpdlIAC', 'title': 'CryptGuard Module: Pioneering Data Integrity   '}, {'id': 'ka0Wt000000EpNfIAK', 'title': 'Ensuring Reliable Compliance with SecureData Nexus'}, {'id': '#ka0Wt000000EpU5IAK', 'title': 'Customizing Security Protocols with TechPulse'}, {'id': 'ka0Wt000000EowEIAS', 'title': 'Achieving Compliance in EDA with IntegrGuard Secure'}, {'id': '#ka0Wt000000EmkkIAC', 'title': 'Advanced Data Protection with SecuManage Pro   '}, {'id': 'ka0Wt000000EoTDIA0', 'title': 'Enhancing Security in AI-Powered EDA'}, {'id': 'ka0Wt000000EpPFIA0', 'title': 'Integrating Training Modules with TrainEDU Suite '}, {'id': '#ka0Wt000000EpHBIA0', 'title': 'Security in Cloud-Based EDA Solutions'}, {'id': '#ka0Wt000000Ep13IAC', 'title': 'Ensuring PCB Design Reliability'}, {'id': 'ka0Wt000000Eo8EIAS', 'title': 'Seamless Simulation Integration with TechPulse AI Tools'}, {'id': 'ka0Wt000000EoUnIAK', 'title': 'Harnessing AI for Innovative Circuit Creation'}, {'id': 'ka0Wt000000EoEgIAK', 'title': 'Customizing Workflow Automation: Meeting Unique Circuit Design Needs'}, {'id': '#ka0Wt000000EoGHIA0', 'title': 'Ensuring Secure Design Collaboration in Cloud Environments  '}, {'id': 'ka0Wt000000EnyXIAS', 'title': 'TechPulse Solutions: Defining Values that Drive Innovation and Success'}, {'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers'}], 'var_functions.query_db:16': [{'id': 'ka0Wt000000Eq0MIAS', 'title': 'Volume-Based Discounts', 'faq_answer__c': "Volume-based discounts are a strategic tool for fostering customer loyalty and encouraging bulk purchases. At TechPulse Solution, we aim to provide value-added benefits to our customers, and volume-based discounts are integral to this mission. Here is a detailed overview of the volume-based discounts currently available:\n\n1. **5% Discount for Purchases Over $5**: This entry-level discount is designed for customers making modest but regular purchases. If your transaction totals $5 or more, you automatically become eligible for a 5% discount on your total purchase. This incentive is perfect for small businesses or individuals looking to maximize their purchasing power without committing to large upfront investments.\n\n2. **10% Discount for Purchases Over $10**: By increasing your purchase to $10, you can enjoy a more substantial 10% discount. This tier is targeted at growing businesses or tech enthusiasts planning for larger projects. Whether you're a startup needing essential tech solutions or an established entity upgrading current systems, this level of discount allows you to save significant amounts while meeting your needs.\n\n3. **15% Discount for Purchases Over $20**: The highest discount tier is designed for customers planning substantial investments in tech solutions. With a purchase of $20 or more, you can benefit from a generous 15% discount. This is particularly advantageous for businesses engaged in major scaling projects or for those who require extensive tech solutions for operational expansion.\n\nThese volume-based discounts are designed to reward you as you invest more in our innovative solutions, ensuring that you receive the best possible value. They are automatically applied at checkout, simplifying the purchasing process and enabling you to focus on selecting the best technology for your needs.\n\nIncorporating these discounts into your purchasing strategy can significantly reduce costs while allowing access to premium technology and support from TechPulse Solution. Whether you are a small business making selective purchases or a large company procuring extensive solutions, our discount structure provides a tailored approach to meet varying budgetary needs.\n\nOptimize your purchasing strategy and operational efficiency with our volume-based discounts, designed to bring you closer to innovative technology that can drive your success. At TechPulse Solution, your needs are at the forefront, and these carefully crafted discounts provide a pathway to affordable excellence.", 'summary': 'Volume-Based Discounts', 'urlname': '1745269013-mq1zw'}]}

exec(code, env_args)
