code = """import json
import re
import os

# Access the transcript result stored in var_call_BfYB0zRaSFkoEgVY8Y9EvLPO
transcripts = var_call_BfYB0zRaSFkoEgVY8Y9EvLPO
transcript_text = " ".join([t.get("Body__c", "") for t in transcripts])
transcript_text_lower = transcript_text.lower()

# Load knowledge articles result (may be a file path)
kas = []
ka_var = var_call_VN8o3bdMeMii3IZGfFdYiegv
if isinstance(ka_var, str) and os.path.exists(ka_var):
    with open(ka_var, 'r') as f:
        kas = json.load(f)
elif isinstance(ka_var, list):
    kas = ka_var
else:
    # try to load if it's a JSON string
    try:
        kas = json.loads(ka_var)
    except Exception:
        kas = []

# Initialize BANT flags
budget_ok = False
authority_ok = True
need_ok = False
timeline_ok = False

# Analyze transcript for budget
# Look for explicit budget and pricing info
budget_matches = re.findall(r'\$[\d,]+', transcript_text)
nums = [int(m.replace('$','').replace(',','')) for m in budget_matches]
if nums:
    # He mentioned budget $2,261 and unit price $500 in the transcript
    # If there's a budget number and a unit price that fits the requested quantity, consider budget OK
    if len(nums) >= 2:
        # assume largest is budget, one of the others is unit price
        budget = max(nums)
        unit_price = min(nums)
        # check quantity mentioned
        qty_match = re.search(r'([0-9]+) units', transcript_text_lower)
        qty = int(qty_match.group(1)) if qty_match else None
        if qty and unit_price * qty <= budget:
            budget_ok = True
    else:
        # presence of price/budget mention — assume OK
        budget_ok = True

# Analyze authority: look for consult/finance/approval phrases
if any(kw in transcript_text_lower for kw in ["consult", "finance team", "need to consult", "don't have the final say", "do not have the final say", "i don\'t have the final say", "need approval", "not the final decision"]):
    authority_ok = False

# Analyze need: look for interest and stated need
if any(kw in transcript_text_lower for kw in ["interested", "want to", "we want", "need", "enhance our", "fits with what we need", "fit with what we need"]):
    need_ok = True

# Analyze timeline: look for timeline mention and vendor's ability to meet it
if "timeline" in transcript_text_lower or "installation" in transcript_text_lower:
    # if vendor explicitly states they can meet tight timelines, consider timeline OK
    if "complete installations within a day" in transcript_text_lower or "complete installations within a day" in transcript_text:
        timeline_ok = True
    else:
        # check knowledge articles about installation timelines for potential conflicts
        kb_timeline_conflict = False
        for k in kas:
            body = (k.get('faq_answer__c') or '').lower()
            title = (k.get('title') or '').lower()
            if 'volume-based installation timeline' in title or 'volume-based installation timeline' in body or 'installation timeline' in title or 'installation timeline' in body:
                # if policy lists that 5 units take 3 days, a request for 4 units may not be guaranteed within 1 day
                if 'small batch purchase' in body and '3 days' in body:
                    # transcript requested 4 units (less than 5) and vendor claimed 1 day; assume acceptable
                    kb_timeline_conflict = False
        timeline_ok = not kb_timeline_conflict

# Compile failed factors
failed = []
if not budget_ok:
    failed.append("Budget")
if not authority_ok:
    failed.append("Authority")
if not need_ok:
    failed.append("Need")
if not timeline_ok:
    failed.append("Timeline")

# Default: if nothing failed, return empty list

print("__RESULT__:")
print(json.dumps(failed))"""

env_args = {'var_call_BfYB0zRaSFkoEgVY8Y9EvLPO': [{'Id': 'a05Wt000003SukEIAS', 'OpportunityId__c': 'None', 'LeadId__c': '00QWt0000089AekMAE', 'Body__c': "[2023-10-21T10:02:00] Ava Sullivan: Hi Ali, this is Ava Sullivan from TechSolutions. How are you today?\n[2023-10-21T10:02:10] Ali Hussein: Hi Ava, I'm doing well, thank you. How about you?\n[2023-10-21T10:02:20] Ava Sullivan: I'm great, thank you for asking! I'm glad we could connect. I was looking over the details you provided about your interest in the PulseSim Pro. Is now a good time to discuss?\n[2023-10-21T10:02:30] Ali Hussein: Yes, now works for me. I'm interested to learn more and see how it fits with what we need.\n[2023-10-21T10:02:40] Ava Sullivan: Fantastic! From what you’ve mentioned, you’re interested in four units of the PulseSim Pro, correct?\n[2023-10-21T10:02:50] Ali Hussein: That's right. We want to enhance our simulation capabilities, and the PulseSim Pro seems like a great fit.\n[2023-10-21T10:03:05] Ava Sullivan: Absolutely. The PulseSim Pro is one of our top products for high precision simulation. It offers advanced analytics and seamless integration with existing systems, which is great for boosting efficiency.\n[2023-10-21T10:03:15] Ali Hussein: Those features sound beneficial. We do have a tight timeline for installation, though. Could you tell me more about that?\n[2023-10-21T10:03:30] Ava Sullivan: Certainly. We understand the importance of meeting tight schedules. We usually aim to complete installations within a day and ensure everything runs smoothly. Our technical team is very efficient.\n[2023-10-21T10:03:40] Ali Hussein: That’s reassuring. And as for the budget, how does it look for four units?\n[2023-10-21T10:03:55] Ava Sullivan: Considering your budget is $2,261, I think we can work something out. Each PulseSim Pro unit is priced at $500. For four units, it will come to $2,000. This is below your budget, leaving room for additional services if you wish.\n[2023-10-21T10:04:10] Ali Hussein: That fits really well. I'd like to move forward, but I'll need to consult with the finance team here since I don’t have the final say.\n[2023-10-21T10:04:20] Ava Sullivan: I completely understand, Ali. Would you like me to send over a detailed proposal and pricing information so you can present it to your team?\n[2023-10-21T10:04:25] Ali Hussein: Yes, please. That would be very helpful.\n[2023-10-21T10:04:35] Ava Sullivan: Great! I'll have that to you by the end of the day. Is there anything else you would need from my side?\n[2023-10-21T10:04:40] Ali Hussein: No, that sounds good for now. Thank you, Ava.\n[2023-10-21T10:04:50] Ava Sullivan: You're welcome, Ali. If any questions come up, feel free to reach out. Have a wonderful day!\n[2023-10-21T10:04:55] Ali Hussein: Thanks, Ava. You too!", 'CreatedDate': '2023-10-21T10:02:00.000+0000', 'EndTime__c': '2023-10-21'}], 'var_call_VN8o3bdMeMii3IZGfFdYiegv': 'file_storage/call_VN8o3bdMeMii3IZGfFdYiegv.json'}

exec(code, env_args)
