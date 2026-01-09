code = """import json
opps = var_call_dwMDZXuy56t6DYsGT0f0fBwr
ai_order_products = {r['ProductId'].replace('#','') for r in var_call_Pd80GkNm9hJuWf4tkCYlMpED}
# pick product purchased last month (June 2021) and AI processing unit -> match AI products from orders, else from opps where product name includes AI
# Prefer order-based match
picked = None
if ai_order_products:
    picked = sorted(ai_order_products)[0]
else:
    picked = None

print('__RESULT__:')
print(json.dumps(picked))"""

env_args = {'var_call_dwMDZXuy56t6DYsGT0f0fBwr': [{'OpportunityId': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15', 'StageName': 'Discovery', 'Product2Id': '#01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15', 'StageName': 'Discovery', 'Product2Id': '#01tWt000006hV58IAE'}, {'OpportunityId': '006Wt000007B7TcIAK', 'CloseDate': '2021-06-15', 'StageName': 'Negotiation', 'Product2Id': '01tWt000006hTUkIAM'}, {'OpportunityId': '006Wt000007B7TcIAK', 'CloseDate': '2021-06-15', 'StageName': 'Negotiation', 'Product2Id': '01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15', 'StageName': 'Discovery', 'Product2Id': '01tWt000006hV9xIAE'}, {'OpportunityId': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15', 'StageName': 'Discovery', 'Product2Id': '01tWt000006hVczIAE'}], 'var_call_tUYtvGvs8uw5YAVovL7G1m5Z': [{'AccountId': '#001Wt00000PGXrNIAX'}], 'var_call_Pd80GkNm9hJuWf4tkCYlMpED': [{'ProductId': '01tWt000006hV8LIAU'}, {'ProductId': '01tWt000006hV8LIAU'}], 'var_call_Em0zLoiHkqb55TjuTxXlcXeE': [{'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift', 'Description': 'Dynamic AI-powered design tool shifting paradigms in circuit creation.'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager', 'Description': 'Enhanced power optimization tools for sustainable electronics development.'}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision', 'Description': 'AI-powered optical design tool for developing efficient light-based components.'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite', 'Description': 'Robust training platform for mastering EDA tools with hands-on labs.'}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro', 'Description': 'AI-enhanced design tool for seamless circuit synchronization and development.'}, {'Id': '#01tWt000006hVY9IAM', 'Name': 'EduFlow Academy', 'Description': 'All-inclusive training platform for EDA tools with interactive learning modules.'}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator', 'Description': 'AI-enhanced circuit design tool for innovative electronic development.'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub', 'Description': 'Innovative training platform offering advanced EDA courses and certifications.'}, {'Id': '01tWt000006hVmfIAE', 'Name': 'EduTech Advance', 'Description': 'Advanced educational platform providing expert training in modern EDA tools.'}, {'Id': '01tWt000006hVt7IAE', 'Name': 'PCB EcoModel  ', 'Description': 'Eco-conscious PCB design platform focusing on sustainable materials.'}]}

exec(code, env_args)
