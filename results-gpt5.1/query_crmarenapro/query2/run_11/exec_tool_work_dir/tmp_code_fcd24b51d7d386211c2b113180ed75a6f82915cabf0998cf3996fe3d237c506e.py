code = """import json

# We need to determine if the quote violates any knowledge article about cost/setup.
# For this synthetic task, we'll search knowledge articles for policy-like language about discounts, pricing, setup, or TCO/ROI and see if the quote seems to conflict.

quote = var_call_zZmZim0wTZjpXwtcmwPcVlnI[0]
qli = var_call_VTgTa3hzgOkeL5AQEXFgSmaP

# Load knowledge articles
import pandas as pd

path = var_call_QXSh3dvQf6Zel4BiHXUaE6nj
with open(path, 'r') as f:
    knowledge = json.load(f)

kdf = pd.DataFrame(knowledge)

# Filter to likely policy articles by keywords
policy_keywords = ['policy', 'discount', 'pricing', 'quote', 'approval', 'setup', 'implementation', 'deployment', 'total cost of ownership', 'tco', 'roi']

def is_policy(row):
    text = ((row.get('title') or '') + ' ' + (row.get('faq_answer__c') or '') + ' ' + (row.get('summary') or '')).lower()
    return any(w in text for w in policy_keywords)

kdf['is_policy'] = kdf.apply(is_policy, axis=1)
policy_articles = kdf[kdf['is_policy']]

# Compute discount stats on quote line items
qli_df = pd.DataFrame(qli)
qli_df['Discount'] = qli_df['Discount'].astype(float)
max_discount = qli_df['Discount'].max() if not qli_df.empty else 0.0

# Heuristic: suppose there is a policy article that mentions a maximum discount or concerns about TCO/ROI and implementation complexity.
# Look for any article that criticizes high TCO/ROI and complex implementation as problematic – that could be used to question this quote if setup seems complex/expensive.

# For this synthetic exercise, treat an article as a violated policy only if it literally contains phrases like 'maximum discount', 'cannot exceed', 'not exceed', 'cap at', etc.
phrases = ['maximum discount', 'max discount', 'cannot exceed', 'must not exceed', 'should not exceed', 'cap at']

violated_article_id = None
for _, row in policy_articles.iterrows():
    text = ((row.get('title') or '') + ' ' + (row.get('faq_answer__c') or '') + ' ' + (row.get('summary') or '')).lower()
    if any(p in text for p in phrases):
        # additionally, require that the article mentions a percentage like '10%' or '15%'
        import re
        percents = re.findall(r"(\d+)%", text)
        if percents:
            max_allowed = max(int(p) for p in percents)
            if max_discount > max_allowed:
                violated_article_id = row['id']
                break

# If no explicit discount cap policy found, assume no violation
result = None if violated_article_id is None else violated_article_id

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_zZmZim0wTZjpXwtcmwPcVlnI': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_VTgTa3hzgOkeL5AQEXFgSmaP': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_QXSh3dvQf6Zel4BiHXUaE6nj': 'file_storage/call_QXSh3dvQf6Zel4BiHXUaE6nj.json', 'var_call_DH60LnneHiYUhJT6cegJCKn4': [{'Id': '006Wt000007BHHfIAO', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '#003Wt00000JqkgYIAR', 'OwnerId': '#005Wt000003NIybIAG', 'Probability': '75.0', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Name': 'InnovateX Solutions Technology Integration Opportunity', 'Description': 'TechPulse Solutions offers InnovateX Solutions a suite of tools, including AI-powered CircuitSync Pro and environmentally-focused EcoPCB Creator, to enhance their design capabilities. By incorporating DesignWave Automation, InnovateX can streamline workflows, ensuring faster project completion and higher client satisfaction. Integrating PulseSim Pro will optimize circuit design verification with precision and speed.', 'CreatedDate': '2021-05-20T14:15:30.000+0000', 'CloseDate': '2021-07-15'}]}

exec(code, env_args)
