code = """import json

lead = var_call_jJ4rjGGN2M0mul6dtNExj0TV[0] if var_call_jJ4rjGGN2M0mul6dtNExj0TV else {}
call = var_call_jZUMoy1XsxNcFxNcmE0aw8Ip[0] if var_call_jZUMoy1XsxNcFxNcmE0aw8Ip else {}
body = (call.get('Body__c') or '').lower()

fails = []
# Need: look for explicit interest/fit
need_ok = any(kw in body for kw in ['interested', 'fit', 'we need', 'enhance', 'move forward'])
# Budget: explicit budget mentioned and pricing fits
budget_ok = ('budget' in body and ('$' in body or 'priced' in body) and ('below your budget' in body or 'fits' in body))
# Timeline: mentions tight timeline + installation within a day (some plan)
timeline_ok = ('timeline' in body and ('installation' in body or 'within a day' in body))
# Authority: states needs to consult finance / no final say
authority_ok = not any(kw in body for kw in ["don't have the final say", 'need to consult', 'consult with the finance', "i'll need to consult"])

if not budget_ok:
    fails.append('Budget')
if not authority_ok:
    fails.append('Authority')
if not need_ok:
    fails.append('Need')
if not timeline_ok:
    fails.append('Timeline')

print('__RESULT__:')
print(json.dumps(fails))"""

env_args = {'var_call_jJ4rjGGN2M0mul6dtNExj0TV': [{'Id': '00QWt0000089AekMAE', 'FirstName': 'Ali', 'LastName': 'Hussein', 'Email': 'ali.hussein@baghdadhtechhub.com', 'Phone': '555-452-7654', 'Company': 'Baghdad Tech Hub', 'Status': 'Converted', 'Title': 'Head of Emerging Technologies', 'CreatedDate': '2023-08-18T15:35:50.000+0000', 'IsConverted': '0', 'OwnerId': '005Wt000003NErnIAG'}], 'var_call_jZUMoy1XsxNcFxNcmE0aw8Ip': [{'Id': 'a05Wt000003SukEIAS', 'LeadId__c': '00QWt0000089AekMAE', 'OpportunityId__c': 'None', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}], 'var_call_2hwj9m8U75nwPmwHvgdn7Ylo': [], 'var_call_cyzhkprGed2NaWeE0KL8kgvU': [], 'var_call_6yVtYYRvHLeC2Mad2ko5TH3B': 'file_storage/call_6yVtYYRvHLeC2Mad2ko5TH3B.json', 'var_call_fJHZehx5jE03zncgaCJk9eqW': [], 'var_call_bn8tmzAtK4DfNDeTdVY9ncFg': []}

exec(code, env_args)
