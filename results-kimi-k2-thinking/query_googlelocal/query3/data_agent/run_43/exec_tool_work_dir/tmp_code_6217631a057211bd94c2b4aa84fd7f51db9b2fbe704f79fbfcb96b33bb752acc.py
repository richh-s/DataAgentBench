code = """import re
import json

businesses = [
    {"gmap_id": "gmap_44", "name": "City Textile", "hours": "None"},
    {"gmap_id": "gmap_41", "name": "San Soo Dang", "hours": "[[\"Thursday\", \"6:30AM\u20136PM\"], [\"Friday\", \"6:30AM\u20136PM\"], [\"Saturday\", \"6:30AM\u20136PM\"], [\"Sunday\", \"7AM\u201312PM\"], [\"Monday\", \"Closed\"], [\"Tuesday\", \"6:30AM\u20136PM\"], [\"Wednesday\", \"6:30AM\u20136PM\"]]"},
    {"gmap_id": "gmap_43", "name": "Nova Fabrics", "hours": "[[\"Thursday\", \"9AM\u20135PM\"], [\"Friday\", \"9AM\u20135PM\"], [\"Saturday\", \"Closed\"], [\"Sunday\", \"Closed\"], [\"Monday\", \"9AM\u20135PM\"], [\"Tuesday\", \"9AM\u20135PM\"], [\"Wednesday\", \"9AM\u20135PM\"]]"},
    {"gmap_id": "gmap_38", "name": "Nobel Textile Co", "hours": "[[\"Thursday\", \"9AM\u20135PM\"], [\"Friday\", \"9AM\u20135PM\"], [\"Saturday\", \"Closed\"], [\"Sunday\", \"Closed\"], [\"Monday\", \"9AM\u20135PM\"], [\"Tuesday\", \"9AM\u20135PM\"], [\"Wednesday\", \"9AM\u20135PM\"]]"},
    {"gmap_id": "gmap_45", "name": "Matrix International Textiles", "hours": "[[\"Thursday\", \"8:30AM\u20135:30PM\"], [\"Friday\", \"8:30AM\u20135:30PM\"], [\"Saturday\", \"Closed\"], [\"Sunday\", \"Closed\"], [\"Monday\", \"8:30AM\u20135:30PM\"], [\"Tuesday\", \"8:30AM\u20135:30PM\"], [\"Wednesday\", \"8:30AM\u20135:30PM\"]]"},
    {"gmap_id": "gmap_74", "name": "Vons Chicken", "hours": "[[\"Thursday\", \"11AM\u20139:30PM\"], [\"Friday\", \"11AM\u20139:30PM\"], [\"Saturday\", \"11AM\u20139:30PM\"], [\"Sunday\", \"11AM\u20139:30PM\"], [\"Monday\", \"Closed\"], [\"Tuesday\", \"11AM\u20139:30PM\"], [\"Wednesday\", \"11AM\u20139:30PM\"]]"},
    {"gmap_id": "gmap_17", "name": "Black Tie Ski Rental Delivery of Mammoth", "hours": "[[\"Thursday\", \"8AM\u20135PM\"], [\"Friday\", \"8AM\u20135PM\"], [\"Saturday\", \"8AM\u20135PM\"], [\"Sunday\", \"8AM\u20135PM\"], [\"Monday\", \"Closed\"], [\"Tuesday\", \"Closed\"], [\"Wednesday\", \"Closed\"]]"},
    {"gmap_id": "gmap_22", "name": "Angel-A Massage", "hours": "[[\"Thursday\", \"9:30AM\u20139:30PM\"], [\"Friday\", \"9:30AM\u20139:30PM\"], [\"Saturday\", \"9:30AM\u20139:30PM\"], [\"Sunday\", \"10AM\u20138PM\"], [\"Monday\", \"10AM\u20139:30PM\"], [\"Tuesday\", \"10AM\u20139:30PM\"], [\"Wednesday\", \"9:30AM\u20139:30PM\"]]"},
    {"gmap_id": "gmap_29", "name": "Dunn-Edwards Paints", "hours": "[[\"Thursday\", \"6:30AM\u20135PM\"], [\"Friday\", \"6:30AM\u20135PM\"], [\"Saturday\", \"7AM\u20133PM\"], [\"Sunday\", \"Closed\"], [\"Monday\", \"6:30AM\u20135PM\"], [\"Tuesday\", \"6:30AM\u20135PM\"], [\"Wednesday\", \"6:30AM\u20135PM\"]]"},
    {"gmap_id": "gmap_25", "name": "Elite Massage", "hours": "None"}
]

def parse_time(time_str):
    # Extract hour from time string like "9:30AM" or "9:30PM"
    match = re.search(r'(\d{1,2}):?(\d{2})?\s*([AP]M)', time_str, re.IGNORECASE)
    if match:
        hour = int(match.group(1))
        minute = int(match.group(2)) if match.group(2) else 0
        am_pm = match.group(3).upper()
        
        if am_pm == 'PM' and hour != 12:
            hour += 12
        elif am_pm == 'AM' and hour == 12:
            hour = 0
            
        return hour + minute/60
    return None

def is_open_after_6pm(hours_str):
    if not hours_str or hours_str == "None":
        return False
    
    try:
        # Parse the hours list from string
        hours_list = eval(hours_str)
        
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        
        for day, hours in hours_list:
            if day in weekdays and hours != 'Closed':
                # Parse the end time
                time_range = hours.split('\u2013')
                if len(time_range) == 2:
                    end_time = time_range[1].strip()
                    end_hour = parse_time(end_time)
                    
                    if end_hour and end_hour > 18.0:  # After 6:00 PM (18:00)
                        return True
                        
    except:
        return False
    
    return False

# Test on sample data
eligible_businesses = []
for biz in businesses:
    if is_open_after_6pm(biz['hours']):
        eligible_businesses.append(biz['gmap_id'])

print('__RESULT__:')
print(json.dumps(eligible_businesses))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['business_description'], 'var_functions.query_db:5': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}, {'gmap_id': 'gmap_74', 'name': 'Vons Chicken', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]'}, {'gmap_id': 'gmap_17', 'name': 'Black Tie Ski Rental Delivery of Mammoth', 'hours': '[["Thursday", "8AM–5PM"], ["Friday", "8AM–5PM"], ["Saturday", "8AM–5PM"], ["Sunday", "8AM–5PM"], ["Monday", "Closed"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]'}, {'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'gmap_id': 'gmap_29', 'name': 'Dunn-Edwards Paints', 'hours': '[["Thursday", "6:30AM–5PM"], ["Friday", "6:30AM–5PM"], ["Saturday", "7AM–3PM"], ["Sunday", "Closed"], ["Monday", "6:30AM–5PM"], ["Tuesday", "6:30AM–5PM"], ["Wednesday", "6:30AM–5PM"]]'}, {'gmap_id': 'gmap_25', 'name': 'Elite Massage', 'hours': 'None'}], 'var_functions.query_db:6': [{'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '5'}, {'gmap_id': 'gmap_44', 'rating': '3'}, {'gmap_id': 'gmap_44', 'rating': '4'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '5'}, {'gmap_id': 'gmap_41', 'rating': '4'}]}

exec(code, env_args)
