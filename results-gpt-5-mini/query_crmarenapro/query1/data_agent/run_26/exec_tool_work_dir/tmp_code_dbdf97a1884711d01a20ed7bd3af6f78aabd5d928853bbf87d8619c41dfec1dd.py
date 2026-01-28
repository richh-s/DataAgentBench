code = """import json
# Access previously stored query results
transcript_records = var_call_WRv9wrNDuYWpi9n64MxswFw4
# The knowledge articles result is stored in a .json file path
kav_path = var_call_UPBZKNwh05x1cb88rrXFwmV8

# Read the knowledge articles JSON file
with open(kav_path, 'r', encoding='utf-8') as f:
    kav_records = json.load(f)

# Basic checks to determine failing BANT factors
# From transcript: check for budget, authority, need, timeline
body = transcript_records[0].get('Body__c','').lower()
budget_ok = False
authority_ok = False
need_ok = False
timeline_ok = False

# Budget: transcript mentions budget $2,261 and price $500 per unit for 4 units => $2000
if '$2,261' in body or '2261' in body or 'budget' in body:
    # detect price and quantity
    if '$500' in body and 'four' in body or '4 units' in body or 'four units' in body:
        budget_ok = True
    else:
        # fallback: if numerical price present and less than budget
        if '$500' in body and '4' in body:
            budget_ok = True

# Authority: transcript contains "I'll need to consult with the finance team here since I don't have the final say."
if "i don't have the final say" in body or "need to consult" in body or 'consult with the finance' in body or "consult" in body:
    authority_ok = False
else:
    authority_ok = True

# Need: transcript shows clear interest "I'm interested to learn more" and purpose "enhance our simulation capabilities"
if 'interested' in body or 'enhance our simulation' in body or 'want to enhance' in body:
    need_ok = True

# Timeline: transcript mentions "tight timeline for installation" and rep says can usually complete within a day.
# Use knowledge articles to check official timeline policy for volumes
timeline_info = [k for k in kav_records if 'Installation Timeline' in (k.get('title') or '') or 'Installation Timeline' in (k.get('summary') or '')]
# If transcript indicates tight timeline but vendor can meet it, consider timeline_ok True
if 'tight timeline' in body:
    # check if vendor assures quick install
    if 'complete installations within a day' in body or 'within a day' in body:
        timeline_ok = True
    else:
        timeline_ok = False
else:
    timeline_ok = True

# Determine failing factors
failing = []
if not budget_ok:
    failing.append('Budget')
if not authority_ok:
    failing.append('Authority')
if not need_ok:
    failing.append('Need')
if not timeline_ok:
    failing.append('Timeline')

# If none failing, empty list
result = json.dumps(failing)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_WRv9wrNDuYWpi9n64MxswFw4': [{'Id': 'a05Wt000003SukEIAS', 'OpportunityId__c': 'None', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}], 'var_call_UPBZKNwh05x1cb88rrXFwmV8': 'file_storage/call_UPBZKNwh05x1cb88rrXFwmV8.json'}

exec(code, env_args)
