code = """import json, pandas as pd

quote = pd.DataFrame(var_call_XeVaQ5CtX7LizDCSGP6iuWdj)
qli = pd.DataFrame(var_call_OuKqZqyrDPSpnuUKH8Hbm0We)

# Load knowledge articles
ka_src = var_call_PtlRPJGISgeC3WkDeCBsU2RK
if isinstance(ka_src, str):
    with open(ka_src, 'r', encoding='utf-8') as f:
        kas = json.load(f)
else:
    kas = ka_src
ka = pd.DataFrame(kas)

# Normalize text for searching
def norm(s):
    if s is None:
        return ''
    return str(s).lower().strip()

ka['__text'] = (ka.get('title','').map(norm) + ' ' + ka.get('summary','').map(norm) + ' ' + ka.get('faq_answer__c','').map(norm))

# Determine likely policy violation: discount thresholds / approval.
# Heuristic: if any QLI discount >= 15% or quote status Needs Review indicates approval required.
qli['Discount'] = pd.to_numeric(qli['Discount'], errors='coerce')
max_disc = float(qli['Discount'].max()) if len(qli) else 0.0
status = norm(quote.loc[0,'Status']) if len(quote) else ''

violation = None
# Search for relevant knowledge article about discounts/approvals/setup fees.
keywords = ['discount', 'approval', 'needs review', 'quote approval', 'pricing', 'setup fee', 'implementation', 'professional services']

# If max discount high or status indicates review, find best matching KA containing discount approval policy.
if max_disc >= 15.0 or 'needs review' in status:
    # Score articles by keyword hits, with emphasis on discount/approval.
    def score(txt):
        sc = 0
        for k in keywords:
            if k in txt:
                sc += 1
        # extra weight if mentions specific threshold like '15%' or '10%'
        if '15%' in txt or '15 percent' in txt:
            sc += 3
        if 'discount' in txt and 'approval' in txt:
            sc += 3
        return sc
    ka['__score'] = ka['__text'].map(score)
    top = ka.sort_values('__score', ascending=False).head(5)
    # pick first with nonzero score
    cand = top[top['__score']>0]
    if len(cand):
        violation = cand.iloc[0]['id']

out = json.dumps(violation if violation is not None else None)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_XeVaQ5CtX7LizDCSGP6iuWdj': [{'Id': '0Q0Wt000001WSDVKA4', 'OpportunityId': '#006Wt000007BHHfIAO', 'AccountId': '#001Wt00000PGXrKIAX', 'ContactId': '003Wt00000JqkgYIAR', 'Name': 'TechPulse-InnovateX Integration Quote', 'Description': 'Initial quote for AI-powered EDA solutions integration', 'Status': 'Needs Review', 'CreatedDate': '2021-06-01T10:00:00.000+0000', 'ExpirationDate': '2021-07-01'}], 'var_call_OuKqZqyrDPSpnuUKH8Hbm0We': [{'Id': '0QLWt0000022xB1OAI', 'QuoteId': '#0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVEnIAM', 'PricebookEntryId': '01uWt0000027PGfIAM', 'Quantity': '5.0', 'UnitPrice': '479.99', 'Discount': '5.0', 'TotalPrice': '2279.9525'}, {'Id': '0QLWt0000022yNAOAY', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '8.0', 'UnitPrice': '349.99', 'Discount': '15.0', 'TotalPrice': '2379.932'}, {'Id': '0QLWt0000022z7tOAA', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'UnitPrice': '499.99', 'Discount': '10.0', 'TotalPrice': '4499.91'}, {'Id': '0QLWt0000022z9VOAQ', 'QuoteId': '0Q0Wt000001WSDVKA4', 'Product2Id': '#01tWt000006hVQ5IAM', 'PricebookEntryId': '01uWt0000027PVBIA2', 'Quantity': '7.0', 'UnitPrice': '339.99', 'Discount': '5.0', 'TotalPrice': '2260.9335'}], 'var_call_PtlRPJGISgeC3WkDeCBsU2RK': 'file_storage/call_PtlRPJGISgeC3WkDeCBsU2RK.json', 'var_call_B2dyxggRUTtzUt6TP1LKvMr3': [{'Id': '006Wt000007BHHfIAO', 'Amount': '11420.728', 'StageName': 'Negotiation  ', 'Probability': '75.0', 'Name': 'InnovateX Solutions Technology Integration Opportunity', 'Description': 'TechPulse Solutions offers InnovateX Solutions a suite of tools, including AI-powered CircuitSync Pro and environmentally-focused EcoPCB Creator, to enhance their design capabilities. By incorporating DesignWave Automation, InnovateX can streamline workflows, ensuring faster project completion and higher client satisfaction. Integrating PulseSim Pro will optimize circuit design verification with precision and speed.', 'CreatedDate': '2021-05-20T14:15:30.000+0000', 'CloseDate': '2021-07-15', 'OwnerId': '#005Wt000003NIybIAG'}]}

exec(code, env_args)
