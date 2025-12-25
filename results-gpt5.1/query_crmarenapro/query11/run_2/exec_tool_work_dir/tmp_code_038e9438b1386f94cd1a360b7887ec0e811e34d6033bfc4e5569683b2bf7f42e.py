code = """import json
op_lines = var_call_wZb7dlennkagFYT6St5Vcp0L
products = var_call_uolqYecrukx6LtbTx1U8eVTP

ai_product_ids = {p['Id'].replace('#',''): p for p in products if 'ai' in p['Name'].lower()}

# Filter opportunity lines to those matching any AI product (after cleaning #)
matching = []
for row in op_lines:
    pid_clean = row['Product2Id'].replace('#','') if row['Product2Id'] else None
    if pid_clean in ai_product_ids:
        matching.append(pid_clean)

# Assume "AI processing unit" refers to any AI-labeled product; choose the most recent one (rows already sorted desc by CloseDate)
result_id = matching[0] if matching else None

result = json.dumps(result_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_wZb7dlennkagFYT6St5Vcp0L': [{'OpportunityId': '006Wt000007B0g2IAC', 'ContactId': '003Wt00000Jqy8SIAR', 'Product2Id': '#01tWt000006hV8LIAU', 'CloseDate': '2021-06-15'}, {'OpportunityId': '006Wt000007B7TcIAK', 'ContactId': '003Wt00000Jqy8SIAR', 'Product2Id': '01tWt000006hTUkIAM', 'CloseDate': '2021-06-15'}, {'OpportunityId': '006Wt000007B7TcIAK', 'ContactId': '003Wt00000Jqy8SIAR', 'Product2Id': '01tWt000006hV8LIAU', 'CloseDate': '2021-06-15'}, {'OpportunityId': '006Wt000007B0g2IAC', 'ContactId': '003Wt00000Jqy8SIAR', 'Product2Id': '01tWt000006hV9xIAE', 'CloseDate': '2021-06-15'}], 'var_call_dUNOjEFZ5yUHqAfYgPzrvz0Q': [], 'var_call_rBDgAnLy9QJxJW9O1mF7xhDL': [], 'var_call_uolqYecrukx6LtbTx1U8eVTP': [{'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager'}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro'}, {'Id': '#01tWt000006hVY9IAM', 'Name': 'EduFlow Academy'}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}, {'Id': '01tWt000006hVmfIAE', 'Name': 'EduTech Advance'}, {'Id': '01tWt000006hVt7IAE', 'Name': 'PCB EcoModel  '}]}

exec(code, env_args)
