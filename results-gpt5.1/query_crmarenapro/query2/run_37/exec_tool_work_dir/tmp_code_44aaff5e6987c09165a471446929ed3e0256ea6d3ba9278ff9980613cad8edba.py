code = """import json
import pandas as pd

# Load knowledge articles from JSON file path stored in var_call_HIjjwSBaOB2VGlHqdjm6D3fQ
path = var_call_HIjjwSBaOB2VGlHqdjm6D3fQ
with open(path, 'r') as f:
    knowledge_articles = json.load(f)

# Simple heuristic policy rules based on article text
violating_article_id = None
quote = var_call_NZdDu5acp70i0L4pxl4NmtYi[0]
quote_items = pd.DataFrame(var_call_oyn5lQTUNyOe7M4DKqcYaNTE)

# Compute total discount-weighted average discount
quote_items['Discount'] = quote_items['Discount'].astype(float)
avg_discount = quote_items['Discount'].mean()

# Example policies:
# 1) If quote Status is 'Needs Review' and avg discount > 10%, map to an article about discount / pricing policy
# 2) If expiration longer than 30 days -> article about quote validity (not applicable here since 1 month)

# Find candidate articles by keywords
for art in knowledge_articles:
    title = art.get('title','').lower().strip()
    summary = (art.get('summary') or '').lower()
    faq = (art.get('faq_answer__c') or '').lower()
    text = title + ' ' + summary + ' ' + faq
    if 'discount' in text or 'pricing' in text or 'total cost of ownership' in text or 'roi' in text:
        # candidate pricing policy article
        pricing_article_id = art['id'].lstrip('#')
        break
else:
    pricing_article_id = None

if quote['Status'].strip().lower() == 'needs review' and avg_discount > 10 and pricing_article_id:
    violating_article_id = pricing_article_id

result = json.dumps(violating_article_id if violating_article_id is not None else None)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_NZdDu5acp70i0L4pxl4NmtYi': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_oyn5lQTUNyOe7M4DKqcYaNTE': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HHpqIAG', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_HIjjwSBaOB2VGlHqdjm6D3fQ': 'file_storage/call_HIjjwSBaOB2VGlHqdjm6D3fQ.json', 'var_call_XKbnOp2oPgfD94kJpf04hA3m': [{'Id': '006Wt000007BHHfIAO', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '#003Wt00000JqkgYIAR', 'OwnerId': '#005Wt000003NIybIAG', 'Probability': '75.0', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Name': 'InnovateX Solutions Technology Integration Opportunity', 'Description': 'TechPulse Solutions offers InnovateX Solutions a suite of tools, including AI-powered CircuitSync Pro and environmentally-focused EcoPCB Creator, to enhance their design capabilities. By incorporating DesignWave Automation, InnovateX can streamline workflows, ensuring faster project completion and higher client satisfaction. Integrating PulseSim Pro will optimize circuit design verification with precision and speed.', 'CreatedDate': '2021-05-20T14:15:30.000+0000', 'CloseDate': '2021-07-15'}]}

exec(code, env_args)
