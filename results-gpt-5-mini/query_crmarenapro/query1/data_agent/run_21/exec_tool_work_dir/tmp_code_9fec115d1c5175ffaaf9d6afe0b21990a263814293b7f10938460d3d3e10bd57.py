code = """import json
import re
# Access storage variables
transcripts = var_call_xjq2cIkiXaBPPa2NrlCded7x
# var_call_TAC... is a filepath to JSON
knowledge_filepath = var_call_TACd1elz3myK62mTpgn4LmSg
with open(knowledge_filepath, 'r', encoding='utf-8') as f:
    knowledge = json.load(f)

# Combine transcript bodies for the lead
body_text = "\n".join([t.get('Body__c','') for t in transcripts])

# Heuristics to determine BANT
failed = []

# Need: look for explicit interest or stated need
need_indicators = ['interested', 'want to', 'need', 'enhance', 'looking to']
need = any(re.search(r"\b"+re.escape(w)+r"\b", body_text, flags=re.IGNORECASE) for w in need_indicators)

# Budget: extract budget and price & quantity from transcript
budget = None
unit_price = None
quantity = None
# Find $ amounts
dollars = re.findall(r"\$\s?([0-9,]+(?:\.[0-9]+)?)", body_text)
nums = [float(s.replace(',','')) for s in dollars]
# From transcript context, first $ number likely budget 2261 and price 500
if nums:
    # crude assignment based on values
    # find a number >=1000 likely budget
    budget_candidates = [n for n in nums if n>=1000]
    if budget_candidates:
        budget = budget_candidates[0]
    else:
        budget = nums[0]
    # find unit price ~500
    unit_candidates = [n for n in nums if 50 <= n <= 2000 and n!=budget]
    if unit_candidates:
        unit_price = unit_candidates[0]

# Find quantity mention like 'four units' or '4 units'
m = re.search(r"(\b\d+\b)\s+units", body_text, flags=re.IGNORECASE)
if m:
    quantity = int(m.group(1))
else:
    # words to numbers for four
    if re.search(r"\bfour units\b", body_text, flags=re.IGNORECASE):
        quantity = 4

budget_ok = False
if budget is not None and unit_price is not None and quantity is not None:
    total = unit_price * quantity
    budget_ok = (budget >= total)

# Authority: look for phrases indicating lack of decision power
authority_clues = ['don\'t have the final say', 'i don\'t have the final say', 'consult with the finance', 'need to consult', 'need to consult with', 'will need to consult', 'not the decision', 'need approval']
authority = True
if any(re.search(clue, body_text, flags=re.IGNORECASE) for clue in authority_clues):
    authority = False

# Timeline: check if lead mentioned tight timeline and whether knowledge articles indicate feasible timelines
timeline_issue = False
if re.search(r"tight timeline|timeline", body_text, flags=re.IGNORECASE):
    # Find installation timelines in knowledge articles
    timelines = []
    for k in knowledge:
        text = (k.get('faq_answer__c') or '') + ' ' + (k.get('summary') or '') + ' ' + (k.get('title') or '')
        found = re.findall(r"(\b\d+\b)\s+day", text, flags=re.IGNORECASE)
        timelines += [int(x) for x in found]
    # For our quantity, estimate expected timeline from policy: single=1, small(5)=3, medium(15)=7, large(25)=14
    est_timeline = None
    if quantity is not None:
        if quantity == 1:
            est_timeline = 1
        elif quantity <=5:
            est_timeline = 3
        elif quantity <=15:
            est_timeline = 7
        else:
            est_timeline = 14
    # If lead said tight timeline but we don't know their required days, can't assume failure
    # Only mark timeline_issue True if lead explicitly requires less than estimated
    # Search for phrases like 'within a day' or 'by tomorrow'
    if re.search(r"within a day|by tomorrow|ASAP|urgent|end of the day|today", body_text, flags=re.IGNORECASE):
        # If required <=1 and est_timeline >1 then fail
        required_quick = True
        if est_timeline is not None and est_timeline > 1:
            timeline_issue = True

# Determine failing factors
if not need:
    failed.append('Need')
if not budget_ok:
    failed.append('Budget')
if not authority:
    failed.append('Authority')
if timeline_issue:
    failed.append('Timeline')

# If none failed, lead is qualified (empty list)
result = failed
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_xjq2cIkiXaBPPa2NrlCded7x': [{'Id': 'a05Wt000003SukEIAS', 'OpportunityId__c': 'None', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}], 'var_call_TACd1elz3myK62mTpgn4LmSg': 'file_storage/call_TACd1elz3myK62mTpgn4LmSg.json'}

exec(code, env_args)
