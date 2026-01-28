code = """import json
import pandas as pd
import re

# Load previous tool results
knowledge_file = var_call_NBzLA7n19shAjPZY0LiwUykW
with open(knowledge_file, 'r') as f:
    knowledge = json.load(f)

quotes = var_call_skmsgzWFQncFcDwuEtSKHJmp
qli = var_call_hUK3vhYT85oY7vMwSni8MfZ1
pbe = var_call_utlF3Mo3Vi0pGxctKEchQ6i3
prod = var_call_vHaLu5A2QnNnIDshYGoQGtXo

qli_df = pd.DataFrame(qli)
qli_df['UnitPrice'] = qli_df['UnitPrice'].astype(float)
qli_df['Discount'] = qli_df['Discount'].astype(float)
qli_df['Quantity'] = qli_df['Quantity'].astype(float)
qli_df['TotalPrice'] = qli_df['TotalPrice'].astype(float)

total_quote = float(qli_df['TotalPrice'].sum())
max_discount = float(qli_df['Discount'].max())

# Build list of candidate articles containing discount or approval related terms
keywords = ['discount', 'approval', 'approval required', 'discount policy', 'quote approval', 'pricing policy', 'requires approval']

violations = []
for row in knowledge:
    # combine fields
    text_parts = []
    for k in ('title','faq_answer__c','summary','urlname'):
        if k in row and row[k]:
            text_parts.append(str(row[k]))
    text = '\n'.join(text_parts).lower()
    if any(kw in text for kw in keywords):
        # find percent numbers
        percents = re.findall(r"(\d+(?:\.\d+)?)\s*%", text)
        percents = [float(p) for p in percents] if percents else []
        # check for explicit phrases
        if 'discount' in text:
            if percents:
                # assume threshold is the largest percent mentioned as allowed
                threshold = max(percents)
                if max_discount > threshold:
                    violations.append({'article_id': row.get('id'), 'title': row.get('title'), 'threshold_percent': threshold, 'max_discount': max_discount})
            else:
                if 'no discounts' in text or 'requires approval' in text or 'approval required' in text:
                    if max_discount > 0:
                        violations.append({'article_id': row.get('id'), 'title': row.get('title'), 'threshold_percent': None, 'max_discount': max_discount})

# If no violations found, set result to None
result_id = None
if violations:
    result_id = violations[0]['article_id']

print("__RESULT__:")
print(json.dumps(result_id))"""

env_args = {'var_call_skmsgzWFQncFcDwuEtSKHJmp': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_hUK3vhYT85oY7vMwSni8MfZ1': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_1YNW0H5gEItNSVvdXOm5pU57': [], 'var_call_utlF3Mo3Vi0pGxctKEchQ6i3': [{'Id': '01uWt0000027P3lIAE', 'Pricebook2Id': '#01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hV57IAE', 'UnitPrice': '499.99'}, {'Id': '01uWt0000027PVBIA2', 'Pricebook2Id': '01sWt000000imiTIAQ', 'Product2Id': '01tWt000006hVQ5IAM', 'UnitPrice': '339.99'}], 'var_call_vHaLu5A2QnNnIDshYGoQGtXo': [{'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro', 'Description': 'Advanced simulation and verification software for optimizing circuit designs.', 'IsActive': '1', 'External_ID__c': 'Simulation and Verification Software,AI-Powered Circuit Design Tools_1'}], 'var_call_NBzLA7n19shAjPZY0LiwUykW': 'file_storage/call_NBzLA7n19shAjPZY0LiwUykW.json'}

exec(code, env_args)
