code = """import json, re

kav_path = var_call_IMH8rwJQVnko7i5LaTJ1vNkW

with open(kav_path, 'r') as f:
    kav = json.load(f)

text = json.dumps(kav).lower()

patterns = [
    r'quote approval policy',
    r'max(imum)? discount',
    r'discount threshold',
    r'pricing exception',
    r'approval.*quote',
    r'quote.*approval',
    r'quote discount',
    r'non-standard deal',
]

candidates = []
for art in kav:
    body = (' '+(art.get('title') or '')+' '+(art.get('summary') or '')+' '+(art.get('faq_answer__c') or '')).lower()
    if any(re.search(p, body) for p in patterns):
        candidates.append(art)

qid = '0Q0Wt000001WSDVKA4'
qli = var_call_o77hJCiB0kECQyiNp2J2Di9E

max_discount = 20.0
violated = False
for li in qli:
    try:
        d = float(li.get('Discount') or 0)
    except:
        d = 0.0
    if d > max_discount:
        violated = True
        break

article_id = None
if violated and candidates:
    article_id = re.sub('#', '', candidates[0]['id'])

result = json.dumps(article_id if article_id is not None else None)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_ZqBq94iZSk7oLsfvacrHPFom': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_Nh3IOg4uoQ8jZE7E4oY39STH': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_o77hJCiB0kECQyiNp2J2Di9E': [{'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HavbIAC', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HXg4IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'OpportunityLineItemId': '00kWt000002HL76IAG', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_IMH8rwJQVnko7i5LaTJ1vNkW': 'file_storage/call_IMH8rwJQVnko7i5LaTJ1vNkW.json', 'var_call_S1wjfSobYtHVQF0USswIo0Dm': [{'Id': '006Wt000007BHHfIAO', 'ContractID__c': 'None', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '#003Wt00000JqkgYIAR', 'OwnerId': '#005Wt000003NIybIAG', 'Probability': '75.0', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Name': 'InnovateX Solutions Technology Integration Opportunity', 'Description': 'TechPulse Solutions offers InnovateX Solutions a suite of tools, including AI-powered CircuitSync Pro and environmentally-focused EcoPCB Creator, to enhance their design capabilities. By incorporating DesignWave Automation, InnovateX can streamline workflows, ensuring faster project completion and higher client satisfaction. Integrating PulseSim Pro will optimize circuit design verification with precision and speed.', 'CreatedDate': '2021-05-20T14:15:30.000+0000', 'CloseDate': '2021-07-15'}]}

exec(code, env_args)
