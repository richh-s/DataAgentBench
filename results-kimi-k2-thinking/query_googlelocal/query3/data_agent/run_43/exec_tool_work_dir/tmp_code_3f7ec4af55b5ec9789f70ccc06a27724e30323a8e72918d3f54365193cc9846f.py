code = """import re
import json

# Sample data to test the logic
businesses = [
    {"gmap_id": "gmap_44", "name": "City Textile", "hours": "None"},
    {"gmap_id": "gmap_41", "name": "San Soo Dang", "hours": "[[\"Thursday\", \"6:30AM–6PM\"], [\"Friday\", \"6:30AM–6PM\"], [\"Saturday\", \"6:30AM–6PM\"], [\"Sunday\", \"7AM–12PM\"], [\"Monday\", \"Closed\"], [\"Tuesday\", \"6:30AM–6PM\"], [\"Wednesday\", \"6:30AM–6PM\"]]"},
    {"gmap_id": "gmap_74", "name": "Vons Chicken", "hours": "[[\"Thursday\", \"11AM–9:30PM\"], [\"Friday\", \"11AM–9:30PM\"], [\"Saturday\", \"11AM–9:30PM\"], [\"Sunday\", \"11AM–9:30PM\"], [\"Monday\", \"Closed\"], [\"Tuesday\", \"11AM–9:30PM\"], [\"Wednesday\", \"11AM–9:30PM\"]]"},
    {"gmap_id": "gmap_22", "name": "Angel-A Massage", "hours": "[[\"Thursday\", \"9:30AM–9:30PM\"], [\"Friday\", \"9:30AM–9:30PM\"], [\"Saturday\", \"9:30AM–9:30PM\"], [\"Sunday\", \"10AM–8PM\"], [\"Monday\", \"10AM–9:30PM\"], [\"Tuesday\", \"10AM–9:30PM\"], [\"Wednesday\", \"9:30AM–9:30PM\"]]"}
]

def parse_time(time_str):
    time_str = str(time_str).strip()
    match = re.search(r'(\d{1,2}):?(\d{2})?\s*([AP]M)', time_str, re.IGNORECASE)
    if match:
        hour = int(match.group(1))
        minute = int(match.group(2)) if match.group(2) else 0
        am_pm = str(match.group(3)).upper()
        if am_pm == 'PM' and hour != 12:
            hour += 12
        elif am_pm == 'AM' and hour == 12:
            hour = 0
        return hour + minute/60
    return None

def is_open_after_6pm(hours_str):
    if not hours_str or str(hours_str) == "None" or str(hours_str) == "":
        return False
    try:
        # Replace unicode dash with regular dash and fix quotes
        hours_clean = str(hours_str).replace('\u2013', '--').replace('--', '-')
        # For simplicity, let's just check if the string contains patterns like X:XXPM with time > 6PM
        import itertools
        # Split by day entries
        day_entries = re.findall(r'\[\"[^\"]+\", \"[^\"]+\"\]', hours_clean)
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        for entry in day_entries:
            for day in weekdays:
                if day in entry:
                    # Extract time range
                    time_match = re.search(r'\d{1,2}:?\d{0,2}\s*[AP]M\s*-\s*(\d{1,2}:?\d{0,2}\s*[AP]M)', entry.replace('\\', ''), re.IGNORECASE)
                    if time_match:
                        end_time_str = time_match.group(1)
                        end_hour = parse_time(end_time_str)
                        if end_hour and end_hour > 18.0:
                            return True
                    # Also check for simple pattern
                    if 'PM' in entry:
                        # Look for closing time like 9:30PM, 9PM, etc.
                        parts = entry.split('", "')
                        if len(parts) >= 2:
                            time_part = parts[1].replace('"]', '')
                            if '-' in time_part:
                                end_time = time_part.split('-')[1].strip()
                                end_hour = parse_time(end_time)
                                if end_hour and end_hour > 18.0:
                                    return True
    except Exception as e:
        pass
    return False

# Test parsing
eligible = []
for biz in businesses:
    if is_open_after_6pm(biz['hours']):
        eligible.append(biz['gmap_id'])

print('__RESULT__:')
print(json.dumps(eligible))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}, {'gmap_id': 'gmap_74', 'name': 'Vons Chicken', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]'}, {'gmap_id': 'gmap_17', 'name': 'Black Tie Ski Rental Delivery of Mammoth', 'hours': '[["Thursday", "8AM–5PM"], ["Friday", "8AM–5PM"], ["Saturday", "8AM–5PM"], ["Sunday", "8AM–5PM"], ["Monday", "Closed"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]'}, {'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'gmap_id': 'gmap_29', 'name': 'Dunn-Edwards Paints', 'hours': '[["Thursday", "6:30AM–5PM"], ["Friday", "6:30AM–5PM"], ["Saturday", "7AM–3PM"], ["Sunday", "Closed"], ["Monday", "6:30AM–5PM"], ["Tuesday", "6:30AM–5PM"], ["Wednesday", "6:30AM–5PM"]]'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'hours': 'None'}], 'var_functions.query_db:6': [{'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '3'}, {'gmap_id': 'gmap_44', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}]}

exec(code, env_args)
