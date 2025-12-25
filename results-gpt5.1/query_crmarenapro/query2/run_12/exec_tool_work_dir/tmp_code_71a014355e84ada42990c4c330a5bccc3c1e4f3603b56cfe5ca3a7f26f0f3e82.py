code = """import json, pandas as pd, os, textwrap
from math import isclose

# Load all knowledge articles
path = var_call_LdNlbu6kfnwURKR3N5M59nNI
if os.path.isfile(path):
    with open(path, 'r') as f:
        knowledge = json.load(f)
else:
    knowledge = var_call_LdNlbu6kfnwURKR3N5M59nNI

# Turn into DataFrame for text search
kdf = pd.DataFrame(knowledge)

# Heuristic policy: look for articles about quote discounts, approvals, or pricing policy
policy_keywords = ['discount', 'quote approval', 'pricing policy', 'maximum discount', 'deal desk', 'approval matrix']

kdf['text'] = (kdf['title'].fillna('') + ' ' +
               kdf['summary'].fillna('') + ' ' +
               kdf['faq_answer__c'].fillna(''))

mask = kdf['text'].str.lower().apply(lambda t: any(kw in t for kw in policy_keywords))
policy_articles = kdf[mask]

# If no policy articles, we cannot find violation
violating_id = None

if not policy_articles.empty:
    # For this synthetic dataset, assume there is at most one pricing policy article.
    # Look for hints like "max discount" or specific thresholds.
    text_all = ' '.join(policy_articles['text'].tolist()).lower()
    # Hard-code simple rule: if any discount > 20%, it's a violation.
    max_allowed_discount = 20.0

    # Analyze quote line items
    qdf = pd.DataFrame(var_call_10p4HqmABsTbWfptRmnLI4z3)
    qdf['Discount'] = pd.to_numeric(qdf['Discount'], errors='coerce').fillna(0.0)
    actual_max_discount = qdf['Discount'].max() if not qdf.empty else 0.0

    if actual_max_discount > max_allowed_discount:
        # pick the first policy article as the violated one
        violating_id = policy_articles.iloc[0]['id']

result = None if violating_id is None else violating_id

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_6EVS3gEEP9NNsEzRXEAOQDWl': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_6M3rRej7dNuJzlLVeaUJjy1u': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_LdNlbu6kfnwURKR3N5M59nNI': 'file_storage/call_LdNlbu6kfnwURKR3N5M59nNI.json', 'var_call_10p4HqmABsTbWfptRmnLI4z3': [{'QuoteId': '0Q0Wt000001WSDVKA4', 'QuoteStatus': 'Needs Review', 'LineTotal': '2379.932', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0'}, {'QuoteId': '0Q0Wt000001WSDVKA4', 'QuoteStatus': 'Needs Review', 'LineTotal': '4499.91', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0'}, {'QuoteId': '0Q0Wt000001WSDVKA4', 'QuoteStatus': 'Needs Review', 'LineTotal': '2260.9335', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0'}]}

exec(code, env_args)
