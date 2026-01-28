code = """import json
import re

# Get the knowledge articles result
kb_result = locals().get('var_functions.query_db:10')

# Parse JSON if result is a string
if isinstance(kb_result, str):
    with open(kb_result, 'r') as f:
        kb_result = json.load(f)

# Search for articles about discount limits, maximum discounts, or discount policies
discount_keywords = ['discount limit', 'maximum discount', 'discount policy', 'discount approval', 'discount threshold', 'discount rules']
quantity_keywords = ['quantity limit', 'maximum quantity', 'bulk order', 'large quantity']

relevant_articles = []

for article in kb_result:
    title = article.get('title', '').lower()
    faq = article.get('faq_answer__c', '').lower()
    summary = article.get('summary', '').lower()
    
    text_to_search = title + ' ' + faq + ' ' + summary
    
    # Check for discount-related articles
    for keyword in discount_keywords:
        if keyword in text_to_search:
            relevant_articles.append(article)
            break
    
    # Check for quantity-related articles
    if not any(article['id'] == a['id'] for a in relevant_articles):
        for keyword in quantity_keywords:
            if keyword in text_to_search:
                relevant_articles.append(article)
                break

# Also extract the Volume-Based Discounts article specifically
volume_discount_article = None
for article in kb_result:
    if 'volume-based discounts' in article.get('title', '').lower():
        volume_discount_article = article
        break

print('__RESULT__:')
print(json.dumps({
    'relevant_articles': relevant_articles[:10],  # Limit to first 10
    'volume_discount_article': volume_discount_article
}, indent=2))"""

env_args = {'var_functions.query_db:0': [], 'var_functions.query_db:2': [{'Id': '#0Q0Wt000001WLjvKAG', 'OpportunityId': '#006Wt000007BA3HIAW', 'AccountId': '001Wt00000PFj4zIAD', 'ContactId': '003Wt00000Jqs7tIAB', 'Name': 'TechPulse-NaviCorp EDA Strategic Quote  ', 'Description': 'Initial quote for strategic partnership in electronic design automation solutions focused on AI-powered innovations.', 'Status': 'Approved', 'CreatedDate': '2024-03-18T14:15:00.000+0000', 'ExpirationDate': '2024-05-17'}, {'Id': '0Q0Wt000001WRJ3KAO', 'OpportunityId': '006Wt000007BFEFIA4', 'AccountId': '001Wt00000PFj4zIAD', 'ContactId': '#003Wt00000JqmtfIAB', 'Name': 'NaviCorp Tech Advanced Navigation Optimization Quote', 'Description': 'Quote for enhancing navigation system through AI-powered EDA solutions.', 'Status': 'Accepted', 'CreatedDate': '2021-07-01T10:00:00.000+0000', 'ExpirationDate': '2021-08-01'}, {'Id': '0Q0Wt000001WKEPKA4', 'OpportunityId': '#006Wt000007BFfeIAG', 'AccountId': '001Wt00000PFj4zIAD', 'ContactId': '003Wt00000Jqs7tIAB', 'Name': 'NaviCorp Strategic EDA Solutions Quote', 'Description': "Initial quote for AI-powered EDA solutions tailored for NaviCorp's navigation systems enhancement.", 'Status': 'Approved', 'CreatedDate': '2024-03-12T10:30:00.000+0000', 'ExpirationDate': '2024-04-12'}, {'Id': '0Q0Wt000001WREDKA4', 'OpportunityId': '006Wt000007BFpKIAW', 'AccountId': '001Wt00000PFj4zIAD', 'ContactId': '003Wt00000JqyGWIAZ', 'Name': 'NaviCorp Expansion Quote', 'Description': 'Initial quote for enhancement and expansion of navigation systems with integrated AI-powered EDA solutions.', 'Status': 'Draft', 'CreatedDate': '2023-02-10T11:00:00.000+0000', 'ExpirationDate': '2023-03-10'}, {'Id': '0Q0Wt000001WRHRKA4', 'OpportunityId': '006Wt000007BFxOIAW', 'AccountId': '001Wt00000PFj4zIAD', 'ContactId': '003Wt00000JqogwIAB', 'Name': 'NaviCorp Strategic Partnership Quote', 'Description': "Comprehensive proposal aligning TechPulse's AI-powered EDA solutions with NaviCorp's navigation technology goals, emphasizing cost-effectiveness and seamless integration.", 'Status': 'Needs Review   ', 'CreatedDate': '2021-05-12T09:00:00.000+0000', 'ExpirationDate': '2021-06-10'}, {'Id': '0Q0Wt000001WRCbKAO', 'OpportunityId': '#006Wt000007BGewIAG', 'AccountId': '#001Wt00000PFj4zIAD', 'ContactId': '003Wt00000JqyGWIAZ', 'Name': 'NaviCorp Expansion Proposal', 'Description': 'Initial quote for the expansion of partnership with NaviCorp Tech, integrating AI-powered EDA solutions to enhance navigation technology systems.', 'Status': 'Approved', 'CreatedDate': '2023-03-20T10:00:00.000+0000', 'ExpirationDate': '2023-04-20'}, {'Id': '0Q0Wt000001WRFpKAO', 'OpportunityId': '006Wt000007BGlNIAW', 'AccountId': '001Wt00000PFj4zIAD', 'ContactId': '#003Wt00000JqyGWIAZ', 'Name': 'NaviCorp Tech - AI Navigation Enhancement Quote', 'Description': 'Proposal for AI-powered features to enhance navigation systems with advanced integration and efficiency improvements.', 'Status': 'In Review', 'CreatedDate': '2023-10-15T10:00:00.000+0000', 'ExpirationDate': '2023-12-15'}, {'Id': '0Q0Wt000001WMHpKAO', 'OpportunityId': '#006Wt000007B1koIAC', 'AccountId': '001Wt00000PFj50IAD', 'ContactId': '003Wt00000JqmLtIAJ', 'Name': 'FusionTech_AIMfg_Enhancement_Quote', 'Description': "Initial quote for AI-Driven Manufacturing Enhancement with TechPulse's solutions.", 'Status': 'Accepted', 'CreatedDate': '2021-11-25T09:00:00.000+0000', 'ExpirationDate': '2022-02-25'}, {'Id': '0Q0Wt000001WNnKKAW', 'OpportunityId': '006Wt000007B4vXIAS', 'AccountId': '001Wt00000PFj50IAD', 'ContactId': '003Wt00000JqyefIAB', 'Name': 'FusionTech Strategic Collaboration Quote', 'Description': 'Initial quote for collaboration on AI-powered EDA solutions for technology manufacturing processes.', 'Status': 'Accepted', 'CreatedDate': '2021-04-20T10:15:00.000+0000', 'ExpirationDate': '2021-10-30'}, {'Id': '#0Q0Wt000001WS5RKAW', 'OpportunityId': '006Wt000007BBIiIAO', 'AccountId': '#001Wt00000PFj50IAD', 'ContactId': '003Wt00000Jqf7OIAR', 'Name': 'FusionTech EDA Transformation Proposal ', 'Description': 'Quote for AI-powered EDA solutions and integration for FusionTech Systems', 'Status': 'Approved', 'CreatedDate': '2021-12-05T10:15:00.000+0000', 'ExpirationDate': '2022-04-05'}], 'var_functions.query_db:5': [{'Id': '#0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '#003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}], 'var_functions.query_db:6': [], 'var_functions.query_db:8': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '#01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '#0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'quote': {'Id': '0Q0Wt000001WRAzKAO', 'OpportunityId': '006Wt000007BGgXIAW', 'AccountId': '001Wt00000PHVsDIAX', 'ContactId': '003Wt00000JqyI6IAJ', 'Name': 'NeoGreen EDA Expansion Quote', 'Description': 'Quote for expanding EDA solutions including AI-powered tools to enhance energy system analytics.', 'Status': 'Needs Review', 'CreatedDate': '2021-05-15T10:30:00.000+0000', 'ExpirationDate': '2021-06-15'}, 'line_items': [{'Id': '0QLWt0000022j3GOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HUwhIAG', 'Product2Id': '01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '3.0', 'UnitPrice': '349.99', 'Discount': '0.0', 'TotalPrice': '1049.97'}, {'Id': '0QLWt0000022j81OAA', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HHRkIAO', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '2.0', 'UnitPrice': '529.99', 'Discount': '0.0', 'TotalPrice': '1059.98'}, {'Id': '0QLWt0000022n8TOAQ', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJYIA4', 'Product2Id': '01tWt000006hPffIAE', 'PricebookEntryId': '01uWt0000027PADIA2', 'Quantity': '4.0', 'UnitPrice': '299.99', 'Discount': '0.0', 'TotalPrice': '1199.96'}, {'Id': '0QLWt0000022oAvOAI', 'QuoteId': '0Q0Wt000001WRAzKAO', 'OpportunityLineItemId': '00kWt000002HQJZIA4', 'Product2Id': '01tWt000006hVczIAE', 'PricebookEntryId': '01uWt0000027Pi5IAE', 'Quantity': '35.0', 'UnitPrice': '399.99', 'Discount': '15.0', 'TotalPrice': '11899.7025'}]}}

exec(code, env_args)
