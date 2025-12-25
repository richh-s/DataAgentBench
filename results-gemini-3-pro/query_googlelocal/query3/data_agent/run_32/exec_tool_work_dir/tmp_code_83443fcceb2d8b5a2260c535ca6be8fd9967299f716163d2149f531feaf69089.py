code = """import json
import re

# Load businesses
with open(locals()['var_function-call-12351195923220380137'], 'r') as f:
    businesses = json.load(f)

def parse_time(time_str):
    # time_str example: "6:30AM", "6PM", "12PM" (noon), "12AM" (midnight)
    # Returns minutes from start of day
    if not time_str: return None
    match = re.match(r"(\d+):?(\d+)?(AM|PM)", time_str)
    if not match:
        # Handle cases like "3" -> "3PM" implicitly? No, usually "3PM"
        # Wait, "3-8PM" means 3PM to 8PM? or 3AM? Usually the suffix applies to the end, but if missing on start, it's tricky.
        # But looking at data: "3\u20138PM". "11AM\u20139:30PM".
        # "8:30\u201310AM".
        # Logic: If start time has no AM/PM, it inherits from end time? 
        # No, "8:30-10AM" -> 8:30 AM. "3-8PM" -> 3 PM.
        # But "11AM-9:30PM" has both.
        # Let's assume if missing, and it's small number, maybe check end?
        # Actually, let's look at specific regex.
        pass
    
    # Let's use a simpler approach. Split by \u2013 or -
    # But first, I need a function to convert "6:30PM" to minutes.
    pass

def to_minutes(t_str, ref_suffix=None):
    # t_str: "6:30PM" or "3" or "10:30"
    # return minutes
    t_str = t_str.strip()
    match = re.search(r"(\d+)(?::(\d+))?\s*(AM|PM)?", t_str, re.IGNORECASE)
    if not match: return None
    h = int(match.group(1))
    m = int(match.group(2) or 0)
    suffix = match.group(3)
    
    if suffix:
        suffix = suffix.upper()
    elif ref_suffix:
        suffix = ref_suffix
    else:
        # Ambiguous. Usually if end is PM and start is small (1-5), start is PM?
        # If end is AM and start is large (8-11), start is AM?
        pass
        
    if suffix == 'PM' and h != 12:
        h += 12
    if suffix == 'AM' and h == 12:
        h = 0
    return h * 60 + m

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

qualified_businesses = []

for b in businesses:
    hours_str = b.get('hours')
    if not hours_str or hours_str == 'None':
        continue
    
    try:
        # It's a string representation of a list
        hours_list = json.loads(hours_str.replace("'", '"')) # Sometimes simple quotes
        # Wait, the sample showed double quotes inside: "[[\"Thursday\", ...]]"
        # json.loads(hours_str) should work if it's valid JSON.
    except:
        # If simple json.loads fails, try evaluating? No, use ast.literal_eval or manual parse
        # Sample: "[[\"Thursday\", \"6:30AM\u20136PM\"], ...]"
        # This is valid JSON.
        try:
             hours_list = json.loads(hours_str)
        except:
            continue

    is_qualified = False
    
    # Convert list to dict for easier lookup
    # But the list contains pairs: [Day, TimeRange]
    
    for day, time_range in hours_list:
        if day in weekdays:
            if "Open 24 hours" in time_range:
                is_qualified = True
                break
            if "Closed" in time_range:
                continue
                
            # Parse range "6:30AM–6PM"
            # Split by \u2013 (en-dash) or - (hyphen)
            parts = re.split(r'[\u2013-]', time_range)
            if len(parts) == 2:
                start_str = parts[0].strip()
                end_str = parts[1].strip()
                
                # Determine suffix for start if missing
                # Strategy: parse end first to get suffix?
                # Actually, filtering only depends on END time.
                # "Remain open after 6:00 PM" -> End time > 18:00
                
                end_mins = to_minutes(end_str)
                
                # 6:00 PM is 18 * 60 = 1080 minutes
                if end_mins is not None and end_mins > 1080:
                    # Special case: closing at 12AM or 1AM (next day)
                    # 12AM is 0 mins. But in context of "open until", it's effectively 24:00 (1440 mins) or later.
                    # My to_minutes converts 12AM to 0.
                    # If end_str is 12AM, 1AM, etc. it means it's open late.
                    # If end_str is 12PM (noon), it's 720.
                    # If end_str is 12AM, it returns 0.
                    # If closing time is 0 (midnight) or small AM (1AM), it is definitely after 6PM.
                    # So if end_mins < start_mins (crossing midnight) OR end_mins > 1080?
                    # Wait, if end_mins is 0 (12 AM), it's > 18:00 effectively.
                    
                    # Let's check for 'AM' in end_str.
                    # If end_str has 'AM' and it's like 12AM, 1AM, 2AM... it's late night.
                    # Unless it closes at 11AM.
                    # Assuming standard business hours, if it closes at X AM, check if X is small (0-5?).
                    
                    if "AM" in end_str.upper():
                        # If it closes in AM, is it early morning (closes at 11AM) or late night (closes at 1AM)?
                        # Compare with start time?
                        # If start is PM and end is AM, it crosses midnight -> Open after 6PM.
                        # If start is AM and end is AM, e.g. 9AM-11AM -> Not open after 6PM.
                        start_mins = to_minutes(start_str, ref_suffix="AM") # Default to AM if missing?
                        
                        # Correct logic:
                        # Parse start and end. If start > end, it crosses midnight.
                        # If crosses midnight, it is open after 6 PM (since it's open until at least midnight).
                        
                        # Re-parse start with inference
                        # If start has no suffix, and end is PM, start likely AM or PM?
                        # "3-8PM" -> 3PM. "11-2PM" -> 11AM.
                        # "9-5PM" -> 9AM.
                        # Heuristic: If num < 7, assume PM? 
                        # Let's look at `to_minutes` again.
                        
                        pass
                    
                    # Let's refine the logic.
                    # We only care if it stays open AFTER 6pm.
                    # 1. Closes > 6PM (18:00) and < 11:59PM.
                    # 2. Closes next day (crosses midnight).
                    
                    # Convert end_str to minutes (0-1439).
                    # If end_str is 12AM -> 0.
                    # If end_str is 1AM -> 60.
                    # If end_str is 6:01PM -> 1081.
                    
                    # Logic:
                    # If end_mins > 1080 (18:00): Qualified.
                    # If end_mins < start_mins (crosses midnight): Qualified (assuming start is before midnight... even if start is 11PM, it's open after 6PM? No, must be open AT 6PM?
                    # "Remain open after 6:00 PM".
                    # Does it mean "Open at 6PM AND continues to be open"?
                    # Or "Closing time is after 6PM"?
                    # "Remain open after 6:00 PM" usually implies coverage of the post-6PM period.
                    # If I open at 8PM and close at 10PM, do I "remain open after 6:00 PM"? Strictly speaking, I am open after 6PM.
                    # But "remain" might imply continuity.
                    # However, usually "open after 6PM" is satisfied by closing time > 18:00.
                    # Let's stick to: Closing Time > 18:00 OR Crosses Midnight.
                    
                    # Need accurate start/end parsing.
                    pass

    # Re-implement parsing inside the loop more carefully
    pass

print("__RESULT__:")
print(json.dumps(businesses)) # Placeholder, I will output the qualified list in the real run."""

env_args = {'var_function-call-4613583688241027152': ['business_description'], 'var_function-call-10114926834381514642': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]', 'description': ' This vibrant shop in Commerce, CA 90023 offers a wide selection of textiles and sewing materials for all your crafting needs.'}], 'var_function-call-13529672724907323289': [{'count': '79'}], 'var_function-call-12351195923220380137': 'file_storage/function-call-12351195923220380137.json'}

exec(code, env_args)
