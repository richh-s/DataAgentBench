code = """import json

with open(locals()['var_function-call-13285449411680244839'], 'r') as f:
    knowledge_articles = json.load(f)

relevant_article_id = None
quote_status = locals()['var_function-call-15306793819652253267'][0]['Status']

# Keywords for identifying articles related to quote cost, setup, and compliance
keywords_cost_setup_compliance = [
    "pricing policy", "cost policy", "setup cost", "discount policy",
    "quote approval", "quote compliance", "sales policy", "commercial policy",
    "installation policy", "financial compliance", "deal structure"
]

for article in knowledge_articles:
    article_text = (article.get("title", "") + " " + article.get("faq_answer__c", "") + " " + article.get("summary", "")).lower()

    # Check for keywords directly related to the query
    for keyword_phrase in keywords_cost_setup_compliance:
        if keyword_phrase in article_text:
            # If the quote needs review and an article talks about approval/compliance/policy related to quotes, pricing, or setup
            if quote_status == "Needs Review":
                # Prioritize articles that specifically mention 'quote' or 'sales' in conjunction with policies
                if ("quote" in article_text or "sales" in article_text) and \
                   ("policy" in article_text or "compliance" in article_text or "approval" in article_text or "guideline" in article_text):
                    relevant_article_id = article["id"]
                    break # Found the most relevant, break from inner loop
    if relevant_article_id: # Break from outer loop if an article is found
        break

print("__RESULT__:")
print(json.dumps(relevant_article_id))"""

env_args = {'var_function-call-15306793819652253267': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_function-call-3707398279472196795': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-13285449411680244839': 'file_storage/function-call-13285449411680244839.json', 'var_function-call-3538474139087207220': [{'id': 'ka0Wt000000EqQ9IAK', 'title': "Understanding TechPulse's Return Policy for Purchased Items"}, {'id': '#ka0Wt000000EpSUIA0', 'title': 'TechPulse Solution Volume-Based Installation Timeline Policy'}], 'var_function-call-5827941129795828585': [], 'var_function-call-9457845136576653084': 'ka0Wt000000EqQ9IAK'}

exec(code, env_args)
