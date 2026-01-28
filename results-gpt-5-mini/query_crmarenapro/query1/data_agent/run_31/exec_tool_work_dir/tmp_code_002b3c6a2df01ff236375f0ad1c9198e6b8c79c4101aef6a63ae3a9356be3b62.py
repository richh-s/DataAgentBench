code = """import json
transcripts = var_call_QeLvMpZRftM2TZZiwrJlig8Z
body = ''
if transcripts:
    body = transcripts[0].get('Body__c','')
body_low = body.lower()

bant_failures = []

# Budget check
budget_ok = False
if '$2,261' in body or '$2261' in body_low or 'budget is $2,261' in body_low or 'your budget is $2,261' in body_low:
    # find unit price and quantity
    if '$500' in body or 'priced at $500' in body_low or '500' in body_low:
        if 'four units' in body_low or '4 units' in body_low or '4' in body_low:
            # total 2000, which is <= 2261
            budget_ok = True

# Also check explicit acceptance phrase
if 'that fits really well' in body_low or 'that fits really well.' in body_low:
    budget_ok = True

if not budget_ok:
    bant_failures.append('Budget')

# Authority check
authority_phrases = ["i don't have the final say", 'i do not have the final say', 'need to consult with the finance', 'consult with the finance', 'i will need to consult', "i'll need to consult", 'not the final say']
authority_flag = any(p in body_low for p in authority_phrases)
if authority_flag:
    bant_failures.append('Authority')

# Need check
need_phrases = ['interested to learn more', 'interested', 'want to move forward', 'we want to enhance', 'want to move forward']
need_flag = any(p in body_low for p in need_phrases)
if not need_flag:
    bant_failures.append('Need')

# Timeline check
timeline_ok = True
if 'tight timeline' in body_low or 'tight timeline for installation' in body_low or 'tight timeline for' in body_low:
    if 'complete installations within a day' in body_low or 'within a day' in body_low or 'aim to complete installations within a day' in body_low:
        timeline_ok = True
    else:
        timeline_ok = False

if not timeline_ok:
    bant_failures.append('Timeline')

# Remove duplicates
bant_failures = list(dict.fromkeys(bant_failures))

if not bant_failures:
    result = 'Qualified'
else:
    result = ', '.join(bant_failures)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_QeLvMpZRftM2TZZiwrJlig8Z': [{'Id': 'a05Wt000003SukEIAS', 'OpportunityId__c': 'None', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}], 'var_call_wxVhQkg2fTQ4I6mJIAeYFyTb': 'file_storage/call_wxVhQkg2fTQ4I6mJIAeYFyTb.json'}

exec(code, env_args)
