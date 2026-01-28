code = """import json
# Access previous tool results from storage
transcripts = var_call_ODGYUt9koYO7Vl7PNzPWoR6Z
# var_call_fZKECSywC9N1ZiuAN1XuQJ4f is a filepath to the JSON result
with open(var_call_fZKECSywC9N1ZiuAN1XuQJ4f, 'r') as f:
    knowledge_articles = json.load(f)

# Combine transcript bodies (should be only one for this lead)
transcript_text = "\n".join([t.get('Body__c','') for t in transcripts])
transcript_lower = transcript_text.lower()

failed = []

# Check Budget: look for budget statements and pricing
budget_ok = False
# Find explicit budget value in transcript
import re
budget_match = re.search(r"budget is \$?([0-9,]+(?:\.[0-9]{2})?)", transcript_lower)
price_matches = re.findall(r"\$([0-9,]+(?:\.[0-9]{2})?)", transcript_text)

# Extract numbers
def parse_num(s):
    return float(s.replace(',',''))

budget_val = None
if budget_match:
    try:
        budget_val = parse_num(budget_match.group(1))
    except:
        budget_val = None

# Look for unit price and quantity in transcript
qty = None
unit_price = None
# quantity mention like 'four units' or numeric
qty_match = re.search(r"(\b\d+\b)\s+units", transcript_lower)
if qty_match:
    qty = int(qty_match.group(1))
else:
    # words to number for common ones (one-two-three-four-five)
    words = {'one':1,'two':2,'three':3,'four':4,'five':5,'fifteen':15,'twenty-five':25}
    for w,n in words.items():
        if f"{w} unit" in transcript_lower or f"{w} units" in transcript_lower:
            qty = n
            break

# unit price match from transcript (e.g., Each PulseSim Pro unit is priced at $500)
up_match = re.search(r"priced at \$([0-9,]+(?:\.[0-9]{2})?)", transcript_text)
if up_match:
    unit_price = parse_num(up_match.group(1))
else:
    # fallback: any price occurrence that looks like unit price context
    up2 = re.search(r"for four units, it will come to \$([0-9,]+(?:\.[0-9]{2})?)", transcript_text, re.IGNORECASE)
    if up2:
        total_val = parse_num(up2.group(1))
        if qty:
            unit_price = total_val / qty

# Determine budget_ok
if budget_val is not None and qty is not None and unit_price is not None:
    total_cost = qty * unit_price
    if total_cost <= budget_val:
        budget_ok = True

# Also if explicit textual acceptance of budget exists
if 'that fits really well' in transcript_lower or 'that fits' in transcript_lower or 'below your budget' in transcript_lower:
    budget_ok = True

if not budget_ok:
    failed.append('Budget')

# Check Authority: look for phrases indicating lack of decision-making
authority_issue = False
if 'i don\'t have the final say' in transcript_lower or 'i will need to consult' in transcript_lower or 'consult with the finance team' in transcript_lower or 'need to consult with the finance team' in transcript_lower:
    authority_issue = True

if authority_issue:
    failed.append('Authority')

# Check Need: if lead expressed direct interest and product fit, then need is satisfied
need_issue = False
if 'i\'m interested' in transcript_lower or 'we want to' in transcript_lower or 'we want to enhance' in transcript_lower:
    need_issue = False
else:
    need_issue = True

if need_issue:
    failed.append('Need')

# Check Timeline: if lead mentions 'tight timeline' and knowledge article indicates installation for qty may take multiple days
timeline_issue = False
if 'tight timeline' in transcript_lower or 'tight timeline for installation' in transcript_lower or 'tight timeline for' in transcript_lower:
    # try to find volume-based timeline from knowledge articles
    # look for small batch (5 units -> 3 days) or similar
    # if qty exists and qty >=2 and <=5 and policy says 3 days -> could conflict with 'within a day' expectation
    policy_days = None
    for art in knowledge_articles:
        faq = (art.get('faq_answer__c') or '').lower()
        if 'small batch purchase (volume: 5)' in faq:
            m = re.search(r"small batch purchase \(volume: 5\)\s+.*?(\d+) days", faq)
            if m:
                policy_days = int(m.group(1))
                break
        # also check other numeric mappings
        m2 = re.search(r"single unit purchase \(volume: 1\).*?within a single day", faq)
        if m2:
            # single unit -> 1 day
            pass
    # If transcript also contains salesperson claim of 1 day, that may be optimistic
    if qty is not None and policy_days is not None:
        # If policy_days > 1 and lead has tight timeline, mark issue
        if policy_days > 1:
            timeline_issue = True
    else:
        # If we can't determine policy but lead said 'tight timeline' and no clear confirmation, mark as potential issue
        timeline_issue = True

if timeline_issue:
    failed.append('Timeline')

# Remove duplicates and ensure order Budget, Authority, Need, Timeline
order = ['Budget','Authority','Need','Timeline']
failed_ordered = [f for f in order if f in failed]

# If no failures, return an empty list
result = failed_ordered

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ODGYUt9koYO7Vl7PNzPWoR6Z': [{'Id': 'a05Wt000003SukEIAS', 'OpportunityId__c': 'None', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}], 'var_call_fZKECSywC9N1ZiuAN1XuQJ4f': 'file_storage/call_fZKECSywC9N1ZiuAN1XuQJ4f.json'}

exec(code, env_args)
