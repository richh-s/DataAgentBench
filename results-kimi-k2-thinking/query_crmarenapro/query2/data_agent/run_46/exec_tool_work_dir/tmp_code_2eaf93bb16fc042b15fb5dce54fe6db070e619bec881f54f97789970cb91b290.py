code = """import json
import re

# Load all knowledge articles
knowledge_file = locals()['var_functions.query_db:4']
if isinstance(knowledge_file, str) and '.json' in knowledge_file:
    with open(knowledge_file, 'r') as f:
        all_articles = json.load(f)
else:
    all_articles = knowledge_file

print('Total articles:', len(all_articles))

# Look for articles about discount limits, setup costs, approval thresholds, etc.
policy_keywords = [
    'discount limit',
    'maximum discount',
    'approval threshold',
    'quote approval',
    'setup cost',
    'setup fee',
    'pricing policy',
    'quote policy',
    'bundle requirement',
    'mandatory bundle'
]

relevant_articles = []
for article in all_articles:
    title = article.get('title', '').lower()
    summary = article.get('summary', '').lower()
    faq_answer = article.get('faq_answer__c', '').lower()
    
    for keyword in policy_keywords:
        if keyword in title or keyword in summary or keyword in faq_answer:
            relevant_articles.append(article)
            break

print('Relevant policy articles:', len(relevant_articles))

# Display the articles
for article in relevant_articles:
    print('\nID:', article.get('id'))
    print('Title:', article.get('title'))
    print('Summary:', article.get('summary', 'No summary'))

# Also search the content for specific numeric policies
print('\n=== Searching for discount percentages and limits ===')
for article in relevant_articles:
    content = (article.get('title', '') + ' ' + 
               article.get('summary', '') + ' ' + 
               article.get('faq_answer__c', ''))
    
    # Look for percentages
    percentages = re.findall(r'(\d+)%', content)
    if percentages:
        print(f"Article {article.get('id')}: Found percentages: {percentages}")
    
    # Look for dollar amounts
    dollar_amounts = re.findall(r'\$([\d,]+\.?\d*)', content)
    if dollar_amounts:
        print(f"Article {article.get('id')}: Found amounts: {dollar_amounts}")

result = {'relevant_articles': relevant_articles, 'count': len(relevant_articles)}
print('__RESULT__:')
print(json.dumps(result, default=str))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:12': {'policy_count': 3, 'total_amount': 9140.7755}, 'var_functions.execute_python:18': {'article_count': 2, 'articles': [{'id': 'ka0Wt000000Ens5IAC', 'title': 'Mandatory Bundles for Quotes', 'faq_answer__c': "In the fast-paced world of technological solutions, understanding mandatory product bundles is crucial for securing the best performance and compatibility. At TechPulse Solution, we have streamlined our product offerings, ensuring optimal functionality through specific bundled requirements. This guide provides a comprehensive overview of the mandatory bundles required for quoting our top-tier products.\n\n1. PulseSim Pro Bundle: When purchasing PulseSim Pro, customers must also include the CircuitMaster Analyzer and VeriSim Express in their package. This bundling is designed to enhance your simulation experience, providing unparalleled accuracy and efficiency. CircuitMaster Analyzer works to deliver precise circuit analysis, while VeriSim Express complements it by facilitating swift verification processes. Together, these tools enhance the functionalities of PulseSim Pro, resulting in top-notch simulation capabilities.\n\n2. CloudLink Designer Bundle: To acquire the CloudLink Designer, it's essential to purchase DesignEdge Pro and AI DesignShift as well. This trio creates a robust design platform ideally suited for cloud-based operations. DesignEdge Pro offers advanced design capabilities, ensuring top-quality outcomes, while AI DesignShift incorporates artificial intelligence for intelligent design adaptability and innovation. By combining these products with CloudLink Designer, you achieve a seamless integration that improves performance and design fluidity on the cloud.\n\n3. AI Cirku-Tech Bundle: Customers interested in AI Cirku-Tech must also consider acquiring CircuitAI Innovator and AI DesignShift. Partnered with CircuitAI Innovator, AI Cirku-Tech brings artificial intelligence enhancements to circuit design, optimizing both creativity and efficiency. AI DesignShift, on the other hand, introduces advanced AI-driven design shifts, facilitating a broader scope of design possibilities. This bundle offers a significant leap forward in circuit technology, fully realizing the potential of AI integration.\n\n4. OptiPower Manager Bundle: Purchasing OptiPower Manager necessitates the inclusion of the OptiEnergy Suite and PowerPro Optimize. This comprehensive power management bundle ensures users can effectively monitor and optimize power usage. OptiEnergy Suite offers robust tools for energy management and efficiency, while PowerPro Optimize provides critical power optimization features. Combined with OptiPower Manager, these tools help in achieving significant energy savings and power control.\n\n5. AIOptics Vision Bundle: Lastly, AIOptics Vision requires the Workflow Genius and AI DesignShift as part of its package. This requirement ensures customers have access to superior workflow management tools and AI capabilities. Workflow Genius enhances project management and operational workflows, while AI DesignShift contributes AI-enhanced design innovations. Together with AIOptics Vision, these products deliver a powerful platform for optical analysis and design.\n\nUnderstanding these mandatory bundles helps ensure you receive the full potential of each product offered by TechPulse Solution. By purchasing these curated packages, customers benefit from enhanced functionality, superior performance, and seamless integration, providing an unparalleled technological advantage.", 'summary': 'Mandatory Bundles for Quotes', 'urlname': '1745269013-flbrj'}, {'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers', 'faq_answer__c': 'In a competitive marketplace, flexibility and responsiveness to customer needs are critical to maintaining a successful business operation. TechPulse Solution recognizes that potential clients may be considering multiple vendors for their technological needs. To remain competitive and secure long-term partnerships, we have implemented a Competing Offers Policy. This policy enables us to adjust pricing beyond our standard volume discounts when customers present competing offers from other vendors. By doing this, we aim to not only provide competitive pricing but also demonstrate our commitment to fostering strong business relationships.\n\nThe purpose of the Competing Offers Policy is to ensure that TechPulse Solution remains a preferred and trusted partner for our customers by being agile in our pricing strategies. It is our goal to provide the best value for our products and services without compromising on quality. This policy allows us to go beyond conventional pricing models, offering a customizable approach that reflects real-world scenarios where customers seek the most beneficial options for their budget and requirements.\n\nFor the Competing Offers Policy to be applied effectively, certain guidelines must be met:\n\n1. **Validity of Competing Offer**: Customers must present a valid, written offer from another vendor that outlines the competing price. This offer should be current and applicable to the same product or service specifications that TechPulse Solution provides. This ensures fairness and transparency in the pricing review process.\n\n2. **Product or Service Equivalence**: The competing offer must pertain to an equivalent product or service. TechPulse Solution will evaluate the specifications, features, and service terms to ensure comparability. This step is crucial to maintaining the integrity of the policy and ensuring that our response is aligned with the market landscape.\n\n3. **Review and Approval Process**: Once a competing offer is submitted, it will undergo a review process by our sales and management team to assess the feasibility of matching or improving the offer. Decisions will be guided by strategic business considerations, including potential long-term value, business volume, and relationship history with the client.\n\n4. **Volume and Contractual Commitments**: While our standard volume discounts apply to larger purchases, the Competing Offers Policy may further enhance discounts if it aligns with TechPulse Solution’s business objectives. In some cases, additional discounts may be contingent on contractual commitments or meeting certain purchase thresholds.\n\n5. **Timeliness**: Customers are encouraged to bring competing offers to our attention promptly, as this policy is best applied when potential savings can be realized in a timely manner. Delays can impact our ability to respond effectively and capitalize on market opportunities.\n\nThrough our Competing Offers Policy, TechPulse Solution aims to offer exceptional value and retain our competitive edge in the industry. While the policy is designed to provide flexibility in pricing, it ensures that each adjustment maintains the high standards of quality and support associated with our brand. By adopting this responsive approach, we aim to build enduring partnerships and deliver solutions that meet the diverse needs of our customers.', 'summary': 'Policy for price adjustments based on competing offers', 'urlname': '1745269013-7zuul'}]}}

exec(code, env_args)
