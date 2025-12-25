code = """import json
rows = var_call_TQEcTEI72A7Pph8ShdjUI6X6
rows_sorted = sorted(rows, key=lambda r: r['CreatedDate'], reverse=True)
ai_product_id = rows_sorted[0]['Product2Id'] if rows_sorted else None
result = json.dumps(ai_product_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_wcwSmLY8G61UiBjiVYpi8XFB': [{'Id': '006Wt000007BInBIAW', 'ContactId': '003Wt00000Jqy8SIAR', 'CreatedDate': '2021-04-15T14:22:35.000+0000'}, {'Id': '#006Wt000007BIjxIAG', 'ContactId': '#003Wt00000Jqy8SIAR', 'CreatedDate': '2021-04-10T11:15:45.000+0000'}, {'Id': '006Wt000007B7TcIAK', 'ContactId': '003Wt00000Jqy8SIAR', 'CreatedDate': '2021-03-15T10:27:45.000+0000'}, {'Id': '006Wt000007BBx1IAG', 'ContactId': '003Wt00000Jqy8SIAR', 'CreatedDate': '2021-03-05T09:47:23.000+0000'}, {'Id': '006Wt000007B0g2IAC', 'ContactId': '003Wt00000Jqy8SIAR', 'CreatedDate': '2021-03-01T10:15:30.000+0000'}], 'var_call_VBp0SfkDIkEmcYIDZ9CUrI5w': [], 'var_call_TQEcTEI72A7Pph8ShdjUI6X6': [{'Product2Id': '01tWt000006hUgwIAE', 'CreatedDate': '2021-04-15T14:22:35.000+0000'}, {'Product2Id': '01tWt000006hVgDIAU', 'CreatedDate': '2021-04-15T14:22:35.000+0000'}, {'Product2Id': '01tWt000006hVebIAE', 'CreatedDate': '2021-04-10T11:15:45.000+0000'}, {'Product2Id': '01tWt000006hTUkIAM', 'CreatedDate': '2021-03-15T10:27:45.000+0000'}, {'Product2Id': '01tWt000006hV8LIAU', 'CreatedDate': '2021-03-15T10:27:45.000+0000'}, {'Product2Id': '01tWt000006hV57IAE', 'CreatedDate': '2021-03-05T09:47:23.000+0000'}, {'Product2Id': '01tWt000006hVmfIAE', 'CreatedDate': '2021-03-05T09:47:23.000+0000'}, {'Product2Id': '01tWt000006hVY9IAM', 'CreatedDate': '2021-03-05T09:47:23.000+0000'}, {'Product2Id': '01tWt000006hV6jIAE', 'CreatedDate': '2021-03-05T09:47:23.000+0000'}, {'Product2Id': '01tWt000006hV8LIAU', 'CreatedDate': '2021-03-05T09:47:23.000+0000'}, {'Product2Id': '01tWt000006hV58IAE', 'CreatedDate': '2021-03-05T09:47:23.000+0000'}, {'Product2Id': '#01tWt000006hV8LIAU', 'CreatedDate': '2021-03-01T10:15:30.000+0000'}, {'Product2Id': '01tWt000006hV9xIAE', 'CreatedDate': '2021-03-01T10:15:30.000+0000'}], 'var_call_AHsJDIjvZ3yfEkxaFwLCBe7e': []}

exec(code, env_args)
