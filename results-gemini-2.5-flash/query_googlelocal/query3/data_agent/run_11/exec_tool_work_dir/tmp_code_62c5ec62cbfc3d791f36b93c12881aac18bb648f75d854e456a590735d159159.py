code = """import json
import pandas as pd

# Load the business data from the JSON file
with open(locals()['var_function-call-3480839269620664486'], 'r') as f:
    business_data = json.load(f)

df_business = pd.DataFrame(business_data)

# Filter for businesses that are open (excluding "Permanently closed")
df_business = df_business[~df_business['state'].astype(str).str.contains('Permanently closed', na=False)]

def is_open_after_6pm_on_weekday(hours_str):
    if hours_str is None or hours_str == "None":
        return False
    try:
        hours_list = json.loads(hours_str)
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        for day, time_range in hours_list:
            if day in weekdays:
                if "Open 24 hours" in time_range:
                    return True
                # Handle cases like "6:30AM–6PM" or "3–8PM" or "7AM–4PM" or "11AM–9:30PM"
                if "–" in time_range:
                    try:
                        _, close_time_str = time_range.split("–")
                        close_time_str = close_time_str.replace("AM", "").replace("PM", "")
                        
                        # handle cases like "8:30–5:30", "6:30–5"
                        if ":" not in close_time_str:
                            close_time = int(close_time_str)
                            if "PM" in time_range and close_time <= 12 and close_time != 12:
                                close_time += 12
                            elif "AM" in time_range and close_time == 12: # 12 AM
                                close_time = 0

                        else:
                            hour, minute = map(int, close_time_str.split(":"))
                            if "PM" in time_range and hour <= 12 and hour != 12:
                                hour += 12
                            elif "AM" in time_range and hour == 12: # 12 AM
                                hour = 0

                            close_time = hour * 100 + minute

                        if close_time > 1800:  # 6:00 PM is 1800
                            return True
                    except ValueError:
                        # Handles cases like "7:30AM–4PM"
                        pass
                elif "Reopens" in time_range:
                    # For cases like "Open ⋅ Closes 12PM ⋅ Reopens 1PM"
                    # We need to check the reopens time and closing time
                    parts = time_range.split("⋅")
                    close_part = parts[0].strip()
                    reopen_part = parts[2].strip() if len(parts) > 2 else ""

                    if "Closes" in close_part:
                        try:
                            close_time_str = close_part.split("Closes ")[1].strip()
                            close_hour_str = close_time_str.replace("AM", "").replace("PM", "")
                            
                            if ":" not in close_hour_str:
                                close_hour = int(close_hour_str)
                                if "PM" in close_time_str and close_hour <= 12 and close_hour != 12:
                                    close_hour += 12
                                elif "AM" in close_time_str and close_hour == 12: # 12 AM
                                    close_hour = 0
                                close_time_val = close_hour * 100
                            else:
                                hour, minute = map(int, close_hour_str.split(":"))
                                if "PM" in close_time_str and hour <= 12 and hour != 12:
                                    hour += 12
                                elif "AM" in close_time_str and hour == 12: # 12 AM
                                    hour = 0
                                close_time_val = hour * 100 + minute

                            if close_time_val > 1800:
                                return True
                        except (IndexError, ValueError):
                            pass
                    
                    if "Reopens" in reopen_part:
                        try:
                            reopen_time_str = reopen_part.split("Reopens ")[1].strip()
                            reopen_hour_str = reopen_time_str.replace("AM", "").replace("PM", "")
                            
                            if ":" not in reopen_hour_str:
                                reopen_hour = int(reopen_hour_str)
                                if "PM" in reopen_time_str and reopen_hour <= 12 and reopen_hour != 12:
                                    reopen_hour += 12
                                elif "AM" in reopen_time_str and reopen_hour == 12: # 12 AM
                                    reopen_hour = 0
                                reopen_time_val = reopen_hour * 100
                            else:
                                hour, minute = map(int, reopen_hour_str.split(":"))
                                if "PM" in reopen_time_str and hour <= 12 and hour != 12:
                                    hour += 12
                                elif "AM" in reopen_time_str and hour == 12: # 12 AM
                                    hour = 0
                                reopen_time_val = hour * 100 + minute

                            if reopen_time_val < 1800 and close_time_val > 1800: # Business is open after 6 PM if it reopens before 6PM and closes after 6PM
                                return True
                            elif reopen_time_val >= 1800: # If it reopens after or at 6PM, it is open after 6PM
                                return True
                        except (IndexError, ValueError):
                            pass

    except json.JSONDecodeError:
        return False
    return False

df_business['open_after_6pm'] = df_business['hours'].apply(is_open_after_6pm_on_weekday)

open_after_6pm_gmap_ids = df_business[df_business['open_after_6pm']][['gmap_id', 'name', 'hours']].to_json(orient='records')

print('__RESULT__:')
print(open_after_6pm_gmap_ids)"""

env_args = {'var_function-call-3480839269620664486': 'file_storage/function-call-3480839269620664486.json'}

exec(code, env_args)
