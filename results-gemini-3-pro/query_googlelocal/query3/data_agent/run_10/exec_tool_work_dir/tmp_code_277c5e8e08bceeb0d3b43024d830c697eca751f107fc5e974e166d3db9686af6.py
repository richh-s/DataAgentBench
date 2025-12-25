code = """import json

# Load the business data from the previous step
# The key for the large result is var_function-call-12622269306112281358
# The previous query output was a file path.
file_path = "12622269306112281358.json" # Based on the variable name provided in the preview

# Actually, I need to read the file content.
# The tool output says: "The file path is stored under key: var_function-call-12622269306112281358"
# So I should access locals()['var_function-call-12622269306112281358'] to get the path.

try:
    file_path = locals()['var_function-call-12622269306112281358']
except KeyError:
    # If for some reason it's not in locals (should be), use the hardcoded one from previous message if available or fail.
    # But usually it is available.
    pass

with open(file_path, 'r') as f:
    businesses = json.load(f)

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

filtered_businesses = []

def parse_time(t_str):
    # Formats: "6PM", "6:30AM", "12PM", "12AM", "12:30AM"
    # Returns minutes from midnight 00:00
    # Special case: "Open 24 hours" -> handled outside
    if t_str == 'Open 24 hours':
        return 24 * 60 # Treat as max
    
    t_str = t_str.strip()
    is_pm = t_str.endswith('PM')
    is_am = t_str.endswith('AM')
    
    if not (is_pm or is_am):
        return None # unknown format
    
    time_part = t_str[:-2]
    if ':' in time_part:
        h, m = map(int, time_part.split(':'))
    else:
        h = int(time_part)
        m = 0
    
    if is_pm and h != 12:
        h += 12
    if is_am and h == 12:
        h = 0
        
    return h * 60 + m

def is_open_after_6pm(hours_list_str):
    if not hours_list_str or hours_list_str == 'None':
        return False
    try:
        hours_list = json.loads(hours_list_str.replace("'", '"')) # Sometimes it's single quotes? The sample showed double quotes.
        # Sample: [["Thursday", "6:30AM\u20136PM"], ...]
    except:
        return False
        
    for day_hours in hours_list:
        day = day_hours[0]
        times = day_hours[1]
        
        if day in weekdays:
            if times == 'Closed':
                continue
            if times == 'Open 24 hours':
                return True
                
            # Split by en-dash or hyphen
            # Unicode for en-dash is \u2013
            if '\u2013' in times:
                parts = times.split('\u2013')
            elif '-' in times:
                parts = times.split('-')
            else:
                continue
                
            if len(parts) == 2:
                closing_str = parts[1]
                closing_mins = parse_time(closing_str)
                
                # Check if > 18:00 (1080 mins)
                # But also handle next day AM (e.g. 1AM = 60 mins)
                # If closing time is small (e.g., < 1000) and it was PM open?
                # Usually closing times like 1AM are explicitly AM.
                # If it's 1AM, that's after 6PM.
                # If it's 6:01PM (1081), it's after.
                # If it's 6PM (1080), it's not after.
                # Logic: Valid if closing_mins > 1080 OR closing_mins < 600 (assuming businesses don't close at 10 AM if they open in PM, but checking if open late).
                # Simpler: if it closes in PM, must be > 6PM. If it closes in AM, it's open past midnight (which is after 6PM).
                # Exception: Opens 6AM closes 10AM (AM closing). Not after 6PM.
                
                # We need opening time too to be sure?
                # Usually ranges are "Start - End".
                # If End is AM (e.g. 2AM), and Start is PM or AM, it crossed midnight -> Open after 6PM.
                # If End is PM (e.g. 8PM), check if > 6PM.
                
                if closing_str.endswith('AM'):
                    # Closes in AM. If it's early morning (0-6AM), it likely crossed midnight or is open late.
                    # Unless it's a breakfast place 6AM-10AM.
                    # Start time check?
                    # Most places closing at 1AM, 2AM are open in evening.
                    # Let's assume if closing is 00:00 to 05:00 AM, it's late night.
                    if 0 <= closing_mins <= 5 * 60:
                        return True
                    # What if closes at 11AM? Not after 6PM.
                elif closing_str.endswith('PM'):
                    if closing_mins > 18 * 60: # Strictly after 18:00
                        return True
                        
    return False

filtered_gmap_ids = []
filtered_info = {}

for b in businesses:
    if is_open_after_6pm(b['hours']):
        filtered_gmap_ids.append(b['gmap_id'])
        filtered_info[b['gmap_id']] = {
            'name': b['name'],
            'hours': b['hours']
        }

print("__RESULT__:")
print(json.dumps(filtered_gmap_ids))"""

env_args = {'var_function-call-881768199417983075': ['business_description'], 'var_function-call-881768199417986022': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}], 'var_function-call-881768199417984873': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}], 'var_function-call-5425583791465788172': [{'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}], 'var_function-call-6638118803054670111': [{'count': '66'}], 'var_function-call-850693757138100208': [{'count': '79'}], 'var_function-call-12622269306112281358': 'file_storage/function-call-12622269306112281358.json'}

exec(code, env_args)
