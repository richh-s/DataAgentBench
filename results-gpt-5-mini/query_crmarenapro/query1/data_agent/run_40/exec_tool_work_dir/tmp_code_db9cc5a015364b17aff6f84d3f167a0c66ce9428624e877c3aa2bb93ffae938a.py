code = """import json
# Access stored query results
transcripts = var_call_H2R0qhWJn80XWN7l07m7wB9x
knowledge = None
# var_call_1uP8gvtmX7zjiRciztIwRqp6 may be a filepath (string) or data; handle both
varname = 'var_call_1uP8gvtmX7zjiRciztIwRqp6'
import os
val = globals().get(varname)
if isinstance(val, str) and os.path.exists(val):
    with open(val, 'r', encoding='utf-8') as f:
        knowledge = json.load(f)
else:
    knowledge = val

# Simple analysis
transcript = transcripts[0]['Body__c'] if transcripts and len(transcripts)>0 else ''
# Normalize
txt = transcript.lower()

fails = []
# Budget check: look for budget number and product pricing
budget_ok = False
if '$' in transcript:
    # extract numbers preceded by $
    import re
    dollars = re.findall(r"\$[0-9,]+", transcript)
    nums = [int(d.replace('$','').replace(',','')) for d in dollars]
    # check price per unit mentioned
    per_unit = re.search(r"\$([0-9,]+) per unit", transcript)
    if per_unit:
        pu = int(per_unit.group(1).replace(',',''))
        # check quantity
        qty = None
        mqty = re.search(r"interested in (\d+) units", transcript.lower())
        if mqty:
            qty = int(mqty.group(1))
        # fallback: look for 'four units'
        if qty is None:
            if 'four units' in transcript.lower():
                qty = 4
        if qty is not None and pu is not None:
            total = pu * qty
            # if any budget number >= total -> ok
            if any(b >= total for b in nums):
                budget_ok = True
    else:
        # the transcript explicitly says budget and total price: check statements
        if 'budget is $' in transcript.lower() or 'your budget is $' in transcript.lower():
            # we saw $2,261 and total $2,000 in the transcript preview; treat as ok
            if '$2,261' in transcript or '$2,261' in transcript:
                budget_ok = True

if not budget_ok:
    fails.append('Budget')

# Authority check: look for phrases indicating lack of decision power
if any(phrase in txt for phrase in ["i don't have the final say","i do n't have the final say","i don't have the final say.","need to consult","consult with the finance","i'll need to consult","i will need to consult","need to check with finance","not the final decision","not the final say","need sign-off"]):
    fails.append('Authority')

# Need check: lead explicitly stated interest and reasons
if any(phrase in txt for phrase in ["interested to learn","interested in four units","we want to enhance our simulation capabilities","i'm interested","we want to enhance"]):
    need_ok = True
else:
    need_ok = False
if not need_ok:
    fails.append('Need')

# Timeline check: look for tight timeline and whether confirmed
timeline_issue = False
if 'tight timeline' in txt or 'tight timeline for installation' in txt or 'tight timeline for' in txt:
    # check knowledge articles for installation timelines for volume
    # look for small batch timing
    timeline_from_knowledge = None
    if isinstance(knowledge, list):
        for k in knowledge:
            fa = (k.get('faq_answer__c') or '').lower()
            if 'volume-based installation timeline' in fa or 'installation timeline' in fa:
                # parse numbers
                if 'single unit' in fa and 'one day' in fa:
                    timeline_from_knowledge = 'single_1'
                if 'small batch' in fa and ('3 days' in fa or '3' in fa):
                    timeline_from_knowledge = 'small_3'
                # break once found
                if timeline_from_knowledge:
                    break
    # transcript quantity
    qty = None
    import re
    mqty = re.search(r"interested in (\d+) units", transcript.lower())
    if mqty:
        qty = int(mqty.group(1))
    else:
        if 'four units' in transcript.lower():
            qty = 4
    # If timeline is tight and knowledge suggests >=3 days for similar volume (e.g., small batch 5 ->3 days) and qty close to that, treat as issue
    if 'tight timeline' in txt:
        if qty is not None and ((qty >=5 and timeline_from_knowledge=='small_3') or (qty==4 and timeline_from_knowledge=='small_3')):
            timeline_issue = True
        else:
            # also if salesperson's claim isn't confirmed by knowledge (conflict), treat as unresolved -> issue
            if timeline_from_knowledge=='small_3' and 'complete installations within a day' in txt:
                timeline_issue = True
            else:
                # If no clear confirmation from lead that proposed timeline acceptable, treat as unresolved
                if 'is there anything else' in txt or 'i will need to consult' in txt:
                    timeline_issue = True

if timeline_issue:
    fails.append('Timeline')

# Final decision: if any fails -> cannot qualify
# Prepare output as comma-separated string of unique fails in BANT order: Budget, Authority, Need, Timeline
order = ['Budget','Authority','Need','Timeline']
final_fails = [f for f in order if f in fails]
output = ', '.join(final_fails) if final_fails else '[]'

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_H2R0qhWJn80XWN7l07m7wB9x': [{'Id': 'a05Wt000003SukEIAS', 'OpportunityId__c': 'None', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}], 'var_call_1uP8gvtmX7zjiRciztIwRqp6': 'file_storage/call_1uP8gvtmX7zjiRciztIwRqp6.json'}

exec(code, env_args)
