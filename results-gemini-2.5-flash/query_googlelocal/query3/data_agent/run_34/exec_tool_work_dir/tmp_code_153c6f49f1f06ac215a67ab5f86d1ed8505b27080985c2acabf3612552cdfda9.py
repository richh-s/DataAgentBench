code = """import json
import pandas as pd

business_data = pd.read_json(locals()['var_function-call-4878574359109983823'])
open_after_6pm_businesses = []

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

for index, row in business_data.iterrows():
    hours_str = row['hours']
    if hours_str == 'None':
        continue
    
    try:
        hours_list = json.loads(hours_str)
    except json.JSONDecodeError:
        # Handle cases where hours_str is not a valid JSON string (e.g., malformed)
        continue

    is_open_after_6pm = False
    for day_info in hours_list:
        day = day_info[0]
        time_range = day_info[1]

        if day in weekdays and time_range != "Closed" and "Open 24 hours" not in time_range:
            if '–' in time_range:
                try:
                    end_time_str = time_range.split('–')[1].strip().replace('PM', '').replace('AM', '')
                    end_hour = int(end_time_str.split(':')[0])
                    
                    if 'PM' in time_range and end_hour < 12: # For 7PM-11PM, it should be 19-23, so if end_hour is 7, it means 7PM, not 7AM
                        end_hour += 12
                    elif 'AM' in time_range and end_hour == 12: # For 12AM-6AM, 12AM is 0 hour
                        end_hour = 0

                    if end_hour > 18:  # 6 PM is 18:00
                        is_open_after_6pm = True
                        break
                except (ValueError, IndexError):
                    continue
            elif "Open 24 hours" in time_range:
                is_open_after_6pm = True
                break

    if is_open_after_6pm:
        open_after_6pm_businesses.append(row)

result_df = pd.DataFrame(open_after_6pm_businesses)
print("__RESULT__:")
print(result_df.to_json(orient='records'))"""

env_args = {'var_function-call-17726516570863623093': [{'hours': 'None'}, {'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}, {'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]'}, {'hours': '[["Thursday", "8AM–5PM"], ["Friday", "8AM–5PM"], ["Saturday", "8AM–5PM"], ["Sunday", "8AM–5PM"], ["Monday", "Closed"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]'}, {'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'hours': '[["Thursday", "6:30AM–5PM"], ["Friday", "6:30AM–5PM"], ["Saturday", "7AM–3PM"], ["Sunday", "Closed"], ["Monday", "6:30AM–5PM"], ["Tuesday", "6:30AM–5PM"], ["Wednesday", "6:30AM–5PM"]]'}, {'hours': 'None'}], 'var_function-call-4878574359109983823': 'file_storage/function-call-4878574359109983823.json'}

exec(code, env_args)
