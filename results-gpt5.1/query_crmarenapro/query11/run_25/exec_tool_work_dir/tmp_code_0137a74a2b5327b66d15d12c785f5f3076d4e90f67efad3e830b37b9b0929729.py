code = """import json
opps = var_call_wDWzox8hL4Awp0W3bWcIMRla
products = var_call_i8zSrbPtOC4q9FU99mNSkN0x
# Assume AI processing unit corresponds to the AI-related product name
ai_products = [p for p in products if 'AI' in p['Name'].upper() or 'AI ' in p['Description'].upper()]
# Fallback: if multiple, pick the one whose Id appears most recently (first row in opps)
if ai_products:
    # Score by earliest occurrence in opps list
    id_order = [row['Product2Id'].replace('#','') for row in opps]
    def score(p):
        pid = p['Id'].replace('#','')
        return id_order.index(pid) if pid in id_order else 999
    ai_products_sorted = sorted(ai_products, key=score)
    chosen_id = ai_products_sorted[0]['Id'].replace('#','')
else:
    chosen_id = None
result = json.dumps(chosen_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_wDWzox8hL4Awp0W3bWcIMRla': [{'OpportunityId': '006Wt000007B0g2IAC', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'Product2Id': '#01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B7TcIAK', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hTUkIAM'}, {'OpportunityId': '006Wt000007B7TcIAK', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B0g2IAC', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hV9xIAE'}], 'var_call_uS0kfvrWIS2k8fXyziSbFQqU': [], 'var_call_i8zSrbPtOC4q9FU99mNSkN0x': [{'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer', 'Description': 'Cloud-based design collaboration tool enhancing team productivity across global projects.'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager', 'Description': 'Enhanced power optimization tools for sustainable electronics development.'}]}

exec(code, env_args)
