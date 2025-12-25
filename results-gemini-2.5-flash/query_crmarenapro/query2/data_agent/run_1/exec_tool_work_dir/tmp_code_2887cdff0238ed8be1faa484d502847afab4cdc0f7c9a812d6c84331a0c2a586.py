code = """import json

# Load the full knowledge articles from the file
with open(locals()['var_function-call-4351354252382509361'], 'r') as f:
    knowledge_articles = json.load(f)

# Get the quote data
quote_data = locals()['var_function-call-6334346647056966407'][0]

violation_article_id = None

# Extract relevant information from the quote
quote_name = quote_data.get('Name', '').lower()
quote_status = quote_data.get('Status', '')

# Check if the quote status is 'Needs Review' for policy evaluation
if quote_status == 'Needs Review':
    # Iterate through knowledge articles to find if any competitor's name is in the quote name
    for article in knowledge_articles:
        article_id = article.get('id')
        article_title = article.get('title', '').lower()

        # Simplified policy: If a competitor's name from an article title is in the quote name, it's a violation.
        if 'competitor:' in article_title:
            # Extract competitor name from article title
            # Example: "Competitor: Quantum Circuits Inc" -> "quantum circuits inc"
            competitor_full_name = article_title.split('competitor:', 1)[1].strip()
            
            # Clean up the competitor name for better matching (remove common suffixes and extra spaces)
            competitor_clean_name = competitor_full_name.replace('inc', '').replace('solutions', '').replace('systems', '').strip().replace('  ', ' ')

            # Check if the cleaned competitor name is present in the quote name
            if competitor_clean_name and competitor_clean_name in quote_name:
                violation_article_id = article_id
                break # Found a violation, exit loop

print("__RESULT__:")
print(json.dumps(violation_article_id))"""

env_args = {'var_function-call-6334346647056966407': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_function-call-3917038309144769406': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-4351354252382509361': 'file_storage/function-call-4351354252382509361.json'}

exec(code, env_args)
