code = """import json

# Initialize articles list
articles = []

# Load from var_functions.query_db:2
articles_2 = locals().get('var_functions.query_db:2')
if isinstance(articles_2, str):
    with open(articles_2, 'r') as f:
        articles.extend(json.load(f))
elif isinstance(articles_2, list):
    articles.extend(articles_2)

# Load from var_functions.query_db:10
articles_10 = locals().get('var_functions.query_db:10')
if isinstance(articles_10, str):
    with open(articles_10, 'r') as f:
        articles.extend(json.load(f))
elif isinstance(articles_10, list):
    articles.extend(articles_10)

# Load from var_functions.query_db:18
articles_18 = locals().get('var_functions.query_db:18')
if isinstance(articles_18, str):
    with open(articles_18, 'r') as f:
        articles.extend(json.load(f))
elif isinstance(articles_18, list):
    articles.extend(articles_18)

# Search for policy articles
policy_keywords = [
    'quote approval', 'approval required', 'approval threshold', 'setup requirements',
    'install', 'installation', 'timeline', 'volume', 'discount limit', 'maximum discount',
    'quote policy', 'pricing policy', 'competing offers'
]

policy_articles = []
for article in articles:
    title = article.get('title', '').lower()
    content = article.get('faq_answer__c', '').lower()
    
    for keyword in policy_keywords:
        if keyword in title or keyword in content:
            policy_articles.append({
                'id': article.get('id'),
                'title': article.get('title'),
                'content_preview': content[:300]
            })
            break

# Remove duplicates by ID
unique_articles = {}
for art in policy_articles:
    unique_articles[art['id']] = art

print("__RESULT__:")
print(json.dumps(list(unique_articles.values()), indent=2))"""

env_args = {'var_functions.query_db:0': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_functions.execute_python:8': {'quote_id': '0Q0Wt000001WSDVKA4', 'total_amount': 9140.78, 'line_items': 3, 'line_items_details': [{'quantity': 8.0, 'unit_price': 349.99, 'discount': 15.0, 'total_price': 2379.932}, {'quantity': 10.0, 'unit_price': 499.99, 'discount': 10.0, 'total_price': 4499.91}, {'quantity': 7.0, 'unit_price': 339.99, 'discount': 5.0, 'total_price': 2260.9335}]}, 'var_functions.query_db:10': [{'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers', 'faq_answer__c': 'In a competitive marketplace, flexibility and responsiveness to customer needs are critical to maintaining a successful business operation. TechPulse Solution recognizes that potential clients may be considering multiple vendors for their technological needs. To remain competitive and secure long-term partnerships, we have implemented a Competing Offers Policy. This policy enables us to adjust pricing beyond our standard volume discounts when customers present competing offers from other vendors. By doing this, we aim to not only provide competitive pricing but also demonstrate our commitment to fostering strong business relationships.\n\nThe purpose of the Competing Offers Policy is to ensure that TechPulse Solution remains a preferred and trusted partner for our customers by being agile in our pricing strategies. It is our goal to provide the best value for our products and services without compromising on quality. This policy allows us to go beyond conventional pricing models, offering a customizable approach that reflects real-world scenarios where customers seek the most beneficial options for their budget and requirements.\n\nFor the Competing Offers Policy to be applied effectively, certain guidelines must be met:\n\n1. **Validity of Competing Offer**: Customers must present a valid, written offer from another vendor that outlines the competing price. This offer should be current and applicable to the same product or service specifications that TechPulse Solution provides. This ensures fairness and transparency in the pricing review process.\n\n2. **Product or Service Equivalence**: The competing offer must pertain to an equivalent product or service. TechPulse Solution will evaluate the specifications, features, and service terms to ensure comparability. This step is crucial to maintaining the integrity of the policy and ensuring that our response is aligned with the market landscape.\n\n3. **Review and Approval Process**: Once a competing offer is submitted, it will undergo a review process by our sales and management team to assess the feasibility of matching or improving the offer. Decisions will be guided by strategic business considerations, including potential long-term value, business volume, and relationship history with the client.\n\n4. **Volume and Contractual Commitments**: While our standard volume discounts apply to larger purchases, the Competing Offers Policy may further enhance discounts if it aligns with TechPulse Solution’s business objectives. In some cases, additional discounts may be contingent on contractual commitments or meeting certain purchase thresholds.\n\n5. **Timeliness**: Customers are encouraged to bring competing offers to our attention promptly, as this policy is best applied when potential savings can be realized in a timely manner. Delays can impact our ability to respond effectively and capitalize on market opportunities.\n\nThrough our Competing Offers Policy, TechPulse Solution aims to offer exceptional value and retain our competitive edge in the industry. While the policy is designed to provide flexibility in pricing, it ensures that each adjustment maintains the high standards of quality and support associated with our brand. By adopting this responsive approach, we aim to build enduring partnerships and deliver solutions that meet the diverse needs of our customers.', 'summary': 'Policy for price adjustments based on competing offers', 'urlname': '1745269013-7zuul'}], 'var_functions.execute_python:14': {'available_vars': ['var_functions.query_db:0', 'var_functions.query_db:2', 'var_functions.query_db:5', 'var_functions.query_db:6', 'var_functions.execute_python:8', 'var_functions.query_db:10'], 'quote_line_items': 3, 'grand_total': 9140.7755, 'knowledge_articles_count': 195, 'sample_article_titles': ['Competitor: Quantum Circuits Inc', 'Competitor: Adaptive Design Solutions', 'Competitor: NanoDesign Systems   ', 'Competitor: AI Chip Design Corp', 'Competitor: CircuitWave Technologies  ']}, 'var_functions.execute_python:16': [{'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers', 'summary': 'Policy for price adjustments based on competing offers'}, {'id': 'ka0Wt000000EnthIAC', 'title': 'Competing Offers', 'summary': 'Policy for price adjustments based on competing offers'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
