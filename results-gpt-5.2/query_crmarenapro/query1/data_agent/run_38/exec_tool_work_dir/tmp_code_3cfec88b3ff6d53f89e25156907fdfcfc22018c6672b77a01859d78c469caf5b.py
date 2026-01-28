code = """import json

calls = var_call_lTipBmY5FBHkVqy8IiOh5jAS
lead = var_call_CoOakmZJslg65gjdRTenDdOJ[0] if var_call_CoOakmZJslg65gjdRTenDdOJ else {}

body = calls[0]['Body__c'] if calls else ''
body_l = body.lower()

fails = []
# Budget: explicit budget and pricing fit
budget_ok = ('budget' in body_l and ('$2,261' in body or '2261' in body_l) and ('2,000' in body or '2000' in body_l) and ('below your budget' in body_l or 'fits' in body_l))
if not budget_ok:
    fails.append('Budget')

# Authority: lead says needs finance team / no final say
authority_fail = ('need to consult with the finance team' in body_l) or ("don't have the final say" in body_l) or ('i don\u2019t have the final say' in body)
if authority_fail:
    fails.append('Authority')

# Need: interest in product, wants 4 units, enhance simulation capabilities
need_ok = ('interested' in body_l and 'four units' in body_l) or ('enhance our simulation' in body_l)
if not need_ok:
    fails.append('Need')

# Timeline: tight timeline discussed but no clear deadline; however installation within a day suggests timeline manageable
timeline_ok = 'tight timeline' in body_l or 'installation' in body_l
# If timeline mentioned without a target date, consider unmet
if 'tight timeline' in body_l and not any(tok in body_l for tok in ['by', 'within', 'date', 'week', 'month', 'day']):
    # but transcript includes within a day
    timeline_ok = timeline_ok and ('within a day' in body_l)
if not timeline_ok:
    fails.append('Timeline')

# Per prompt: if cannot be qualified, return failed BANT factors. Here only authority is failing.
result = fails
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_lTipBmY5FBHkVqy8IiOh5jAS': [{'Id': 'a05Wt000003SukEIAS', 'OpportunityId__c': 'None', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}], 'var_call_CoOakmZJslg65gjdRTenDdOJ': [{'Id': '00QWt0000089AekMAE', 'FirstName': 'Ali', 'LastName': 'Hussein', 'Email': 'ali.hussein@baghdadhtechhub.com', 'Phone': '555-452-7654', 'Company': 'Baghdad Tech Hub', 'Status': 'Converted', 'Title': 'Head of Emerging Technologies', 'CreatedDate': '2023-08-18T15:35:50.000+0000', 'ConvertedDate': 'None', 'IsConverted': '0', 'OwnerId': '005Wt000003NErnIAG'}], 'var_call_E0wRNMmhXjkOXxgmhDD4k6TA': []}

exec(code, env_args)
