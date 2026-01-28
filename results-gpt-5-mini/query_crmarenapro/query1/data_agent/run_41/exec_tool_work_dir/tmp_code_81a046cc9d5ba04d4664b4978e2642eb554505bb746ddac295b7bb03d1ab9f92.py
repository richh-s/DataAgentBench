code = """import json
# Accessing stored query results
leads = var_call_LyjErUQ53rUmTsXYtpVIOMO0
transcripts = var_call_YD9xJpOJv7AZ7nFey8FOeQEg
knowledge = var_call_9R1gHTjzgfZf3xRPPpzvPC9x

# Basic text aggregation
transcript_text = "".join([t.get('Body__c','') for t in transcripts])
lead = leads[0] if leads else {}

failed = []

# Check Budget: look for budget mention and pricing; simple heuristics
budget_ok = False
if 'budget' in transcript_text.lower():
    # find any dollar amounts
    import re
    amounts = re.findall(r"\$[0-9,]+(?:\.[0-9]{2})?", transcript_text)
    # crude logic: if both budget and price present and price <= budget -> ok
    budget_vals = []
    price_vals = []
    for a in amounts:
        val = float(a.replace('$','').replace(',',''))
        # heuristics: budgets often larger than single-unit price; here we have context
        budget_vals.append(val)
        price_vals.append(val)
    # Specific known values from transcript
    if '$2,261' in transcript_text and '$2,000' in transcript_text:
        budget_ok = True
    elif amounts:
        # if any two amounts, assume smaller is price and larger is budget
        if len(amounts) >= 2:
            vals = sorted([float(a.replace('$','').replace(',','')) for a in amounts])
            if vals[-1] >= vals[0]:
                budget_ok = True
        else:
            budget_ok = False
else:
    # no budget mentioned, treat as unknown -> fail budget
    budget_ok = False

if not budget_ok:
    failed.append('Budget')

# Check Authority: look for phrases indicating they need approval
authority_phrases = ["i'll need to consult", "i need to consult", "i don't have the final say", "need to consult with", "consult with the finance team", "need approval", "not the final decision"]
if any(p.lower() in transcript_text.lower() for p in authority_phrases):
    failed.append('Authority')

# Check Need: look for expression of interest and clear need
need_indicators = ["interested to learn", "we want to", "we're interested", "would like to move forward", "need"]
need_ok = any(p.lower() in transcript_text.lower() for p in need_indicators)
if not need_ok:
    failed.append('Need')

# Check Timeline: look for mention of timeline and whether vendor can meet it
if 'timeline' in transcript_text.lower() or 'tight timeline' in transcript_text.lower() or 'installation' in transcript_text.lower():
    # if vendor states they can complete installations within a day -> timeline ok
    if 'complete installations within a day' in transcript_text.lower() or 'complete installations within a day' in transcript_text.lower() or 'installations within a day' in transcript_text.lower():
        timeline_ok = True
    else:
        timeline_ok = False
else:
    # no timeline mentioned -> treat as ok
    timeline_ok = True

if not timeline_ok:
    failed.append('Timeline')

# Remove duplicates and preserve order Budget, Authority, Need, Timeline
ordered = ['Budget','Authority','Need','Timeline']
failed_final = [f for f in ordered if f in failed]

print("__RESULT__:")
print(json.dumps(failed_final))"""

env_args = {'var_call_LyjErUQ53rUmTsXYtpVIOMO0': [{'Id': '00QWt0000089AekMAE', 'FirstName': 'Ali', 'LastName': 'Hussein', 'Email': 'ali.hussein@baghdadhtechhub.com', 'Phone': '555-452-7654', 'Company': 'Baghdad Tech Hub', 'Status': 'Converted', 'ConvertedContactId': 'None', 'ConvertedAccountId': 'None', 'Title': 'Head of Emerging Technologies', 'CreatedDate': '2023-08-18T15:35:50.000+0000', 'ConvertedDate': 'None', 'IsConverted': '0', 'OwnerId': '005Wt000003NErnIAG'}], 'var_call_YD9xJpOJv7AZ7nFey8FOeQEg': [{'Id': 'a05Wt000003SukEIAS', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}], 'var_call_9R1gHTjzgfZf3xRPPpzvPC9x': []}

exec(code, env_args)
