code = """import json
opps = var_call_9SC76K0xKeNpTCcHN4XjGol1
olis = var_call_1hj6cEZEL1a6zcHkMUfKnF1u
products = var_call_oYzp8FjCKJ9mMJRh6tRhId8i
# filter opportunities closed in June 2021
opp_ids_june = [o['Id'] for o in opps if o.get('CloseDate') and o['CloseDate'].startswith('2021-06')]
# get product ids from olis matching those opportunities
prod_ids = [o['Product2Id'].lstrip('#').strip() for o in olis if o['OpportunityId'] in opp_ids_june]
# map product id to name
prod_map = {p['Id'].lstrip('#').strip(): p.get('Name','').strip() for p in products}
# find products with 'ai' or 'processing' in name
matches = [pid for pid in prod_ids if pid in prod_map and ('ai' in prod_map[pid].lower() or 'processing' in prod_map[pid].lower())]
# deduplicate preserve order
seen=set()
matches_uniq=[]
for pid in matches:
    if pid not in seen:
        matches_uniq.append(pid)
        seen.add(pid)
# fallback to any prod id if no match
final_id = matches_uniq[0] if matches_uniq else (prod_ids[0] if prod_ids else None)
print('__RESULT__:')
print(json.dumps(final_id))"""

env_args = {'var_call_9Kb6vecatoooJahP1VXYJdIc': [{'Id': '003Wt00000Jqy8SIAR', 'FirstName': 'Anita', 'LastName': 'Kabir', 'Email': 'anita.kabir@futuretechinnovations.com   ', 'AccountId': '#001Wt00000PGXrNIAX'}], 'var_call_7yEyMh87Y2eWxf1hDRxn7oaT': [], 'var_call_nguPvVdKyRFa876p7K4g45vN': '001Wt00000PGXrNIAX', 'var_call_9SC76K0xKeNpTCcHN4XjGol1': [{'Id': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'Name': 'FutureTech Expansion Collaboration', 'CloseDate': '2021-06-15', 'CreatedDate': '2021-03-01T10:15:30.000+0000'}, {'Id': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'Name': 'FutureTech AI Design Enhancement ', 'CloseDate': '2021-06-15', 'CreatedDate': '2021-03-15T10:27:45.000+0000'}, {'Id': '006Wt000007BBx1IAG', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'Name': "FutureTech's Advanced EDA Integration   ", 'CloseDate': '2021-11-01', 'CreatedDate': '2021-03-05T09:47:23.000+0000'}, {'Id': '006Wt000007BInBIAW', 'AccountId': '#001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'Name': 'FutureTech Innovations EDA Transformation ', 'CloseDate': '2022-06-20', 'CreatedDate': '2021-04-15T14:22:35.000+0000'}], 'var_call_1hj6cEZEL1a6zcHkMUfKnF1u': [{'Id': '00kWt000002HHpvIAG', 'OpportunityId': '006Wt000007BBx1IAG', 'Product2Id': '01tWt000006hV57IAE', 'PricebookEntryId': '01uWt0000027P3lIAE', 'Quantity': '10.0', 'TotalPrice': '4499.91'}, {'Id': '#00kWt000002HKCZIA4', 'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '#01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '10.0', 'TotalPrice': '4769.91'}, {'Id': '00kWt000002HLf9IAG', 'OpportunityId': '006Wt000007BBx1IAG', 'Product2Id': '01tWt000006hVmfIAE', 'PricebookEntryId': '01uWt0000027PtNIAU', 'Quantity': '1.0', 'TotalPrice': '399.99'}, {'Id': '#00kWt000002HLwnIAG', 'OpportunityId': '006Wt000007BInBIAW', 'Product2Id': '01tWt000006hUgwIAE', 'PricebookEntryId': '01uWt0000027Q34IAE', 'Quantity': '5.0', 'TotalPrice': '2849.9525'}, {'Id': '00kWt000002HMXmIAO', 'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hTUkIAM', 'PricebookEntryId': '01uWt0000027P6zIAE', 'Quantity': '20.0', 'TotalPrice': '6799.83'}, {'Id': '00kWt000002HOY1IAO', 'OpportunityId': '006Wt000007BInBIAW', 'Product2Id': '01tWt000006hVgDIAU', 'PricebookEntryId': '01uWt0000027PoXIAU', 'Quantity': '4.0', 'TotalPrice': '1839.96'}, {'Id': '00kWt000002HPdfIAG', 'OpportunityId': '006Wt000007BBx1IAG', 'Product2Id': '01tWt000006hVY9IAM', 'PricebookEntryId': '01uWt0000027PdFIAU', 'Quantity': '1.0', 'TotalPrice': '299.99'}, {'Id': '00kWt000002HPiQIAW', 'OpportunityId': '006Wt000007BBx1IAG', 'Product2Id': '01tWt000006hV6jIAE', 'PricebookEntryId': '01uWt0000027P8bIAE', 'Quantity': '12.0', 'TotalPrice': '3779.892'}, {'Id': '00kWt000002HSmqIAG', 'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '10.0', 'TotalPrice': '4769.91'}, {'Id': '00kWt000002HTEHIA4', 'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '01tWt000006hV9xIAE', 'PricebookEntryId': '01uWt0000027PBpIAM', 'Quantity': '12.0', 'TotalPrice': '4859.892'}, {'Id': '00kWt000002HW2RIAW', 'OpportunityId': '006Wt000007BBx1IAG', 'Product2Id': '01tWt000006hV8LIAU', 'PricebookEntryId': '01uWt0000027P8cIAE', 'Quantity': '9.0', 'TotalPrice': '4531.4145'}, {'Id': '#00kWt000002Hce1IAC', 'OpportunityId': '006Wt000007BBx1IAG', 'Product2Id': '01tWt000006hV58IAE', 'PricebookEntryId': '01uWt0000027P5NIAU', 'Quantity': '8.0', 'TotalPrice': '4559.924'}], 'var_call_oYzp8FjCKJ9mMJRh6tRhId8i': [{'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer'}, {'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hV57IAE', 'Name': 'PulseSim Pro'}, {'Id': '01tWt000006hV6jIAE', 'Name': 'EcoPCB Creator   '}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVgDIAU', 'Name': 'CloudInnovate Space '}, {'Id': '01tWt000006hVmfIAE', 'Name': 'EduTech Advance'}]}

exec(code, env_args)
