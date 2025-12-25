code = """import json

with open(locals()['var_function-call-13285449411680244839'], 'r') as f:
    knowledge_articles = json.load(f)

relevant_article_id = None
quote_status = locals()['var_function-call-15306793819652253267'][0]['Status']

for article in knowledge_articles:
    if "pricing" in article["title"].lower() or \
       "cost" in article["title"].lower() or \
       "discount" in article["title"].lower() or \
       "setup" in article["title"].lower() or \
       "installation" in article["title"].lower() or \
       "policy" in article["title"].lower() or \
       "compliance" in article["title"].lower() or \
       "approval" in article["title"].lower() or \
       "security" in article["title"].lower():
        
        if "pricing" in article["faq_answer__c"].lower() or \
           "cost" in article["faq_answer__c"].lower() or \
           "discount" in article["faq_answer__c"].lower() or \
           "setup" in article["faq_answer__c"].lower() or \
           "installation" in article["faq_answer__c"].lower() or \
           "policy" in article["faq_answer__c"].lower() or \
           "compliance" in article["faq_answer__c"].lower() or \
           "approval" in article["faq_answer__c"].lower() or \
           "security" in article["faq_answer__c"].lower():

            # For example, if a quote is "Needs Review" and an article talks about "Approval Process" or "Compliance"
            if quote_status == "Needs Review" and ("approval" in article["title"].lower() or "compliance" in article["title"].lower() or "policy" in article["faq_answer__c"].lower()):
                relevant_article_id = article["id"]
                break

print("__RESULT__:")
print(json.dumps(relevant_article_id))"""

env_args = {'var_function-call-15306793819652253267': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_function-call-3707398279472196795': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-13285449411680244839': 'file_storage/function-call-13285449411680244839.json', 'var_function-call-3538474139087207220': [{'id': 'ka0Wt000000EqQ9IAK', 'title': "Understanding TechPulse's Return Policy for Purchased Items"}, {'id': '#ka0Wt000000EpSUIA0', 'title': 'TechPulse Solution Volume-Based Installation Timeline Policy'}], 'var_function-call-5827941129795828585': []}

exec(code, env_args)
