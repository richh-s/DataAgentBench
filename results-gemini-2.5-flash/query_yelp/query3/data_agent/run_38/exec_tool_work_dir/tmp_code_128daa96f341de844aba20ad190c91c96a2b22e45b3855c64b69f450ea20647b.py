code = """import pandas as pd
import json

review_data = pd.read_json(locals()['var_function-call-4625815798308216618'])
businesses_2018 = set()

for index, row in review_data.iterrows():
    date_str = str(row['date'])
    business_ref = row['business_ref']
    
    # Try different date formats
    try:
        dt = pd.to_datetime(date_str, format='%Y-%m-%d %H:%M:%S', errors='coerce')
    except:
        dt = pd.NaT

    if pd.isna(dt):
        try:
            dt = pd.to_datetime(date_str, format='%d %b %Y, %H:%M', errors='coerce')
        except:
            dt = pd.NaT

    if pd.isna(dt):
        try:
            dt = pd.to_datetime(date_str, format='%B %d, %Y at %I:%M %p', errors='coerce')
        except:
            dt = pd.NaT
    
    if not pd.isna(dt) and dt.year == 2018:
        businesses_2018.add(business_ref.replace('businessref_', 'businessid_'))

print('__RESULT__:')
print(json.dumps(list(businesses_2018)))"""

env_args = {'var_function-call-1309093741827193459': [{'date': '2019-05-30 11:54:00'}, {'date': '2017-08-05 01:46:00'}, {'date': '17 Jul 2020, 20:30'}, {'date': '2019-12-15 18:28:00'}, {'date': '2016-06-28 02:18:33'}, {'date': 'June 22, 2019 at 08:35 PM'}, {'date': '18 Dec 2020, 20:22'}, {'date': 'February 08, 2014 at 04:33 AM'}, {'date': '2021-07-05 17:24:00'}, {'date': '10 Sep 2021, 13:32'}, {'date': '09 Jan 2021, 21:20'}, {'date': '12 Jan 2013, 04:37'}, {'date': 'July 05, 2016 at 11:43 PM'}, {'date': 'January 22, 2011 at 12:14 AM'}, {'date': '2015-11-13 15:51:00'}, {'date': '2014-07-09 22:09:00'}, {'date': '2009-01-12 19:40:00'}, {'date': '2012-03-17 15:49:12'}, {'date': 'December 31, 2019 at 12:41 AM'}, {'date': '2012-06-20 09:58:00'}, {'date': 'July 14, 2021 at 11:52 PM'}, {'date': '16 Jun 2014, 21:24'}, {'date': '2018-02-19 14:12:00'}, {'date': '06 Aug 2016, 21:19'}, {'date': '2021-07-15 18:14:00'}, {'date': '09 Jun 2014, 16:40'}, {'date': '2020-09-20 06:10:00'}, {'date': '2018-08-12 15:51:00'}, {'date': 'November 04, 2016 at 08:48 PM'}, {'date': '02 Jan 2021, 05:18'}, {'date': 'April 02, 2015 at 02:01 AM'}, {'date': '2014-03-17 18:43:00'}, {'date': '21 Jan 2020, 03:42'}, {'date': 'September 25, 2014 at 01:58 AM'}, {'date': 'May 23, 2015 at 02:32 AM'}, {'date': '2018-06-02 14:52:00'}, {'date': '11 Jun 2010, 01:40'}, {'date': '28 Oct 2018, 14:55'}, {'date': 'December 22, 2020 at 08:14 PM'}, {'date': '07 Sep 2021, 22:33'}, {'date': '2016-05-06 16:02:13'}, {'date': 'February 08, 2016 at 04:30 AM'}, {'date': '2018-07-09 02:34:16'}, {'date': '2021-04-18 18:51:26'}, {'date': 'October 17, 2015 at 08:38 PM'}, {'date': 'October 07, 2017 at 04:36 AM'}, {'date': '03 Dec 2014, 06:04'}, {'date': 'October 20, 2015 at 05:34 PM'}, {'date': '2021-07-21 19:50:37'}, {'date': '2017-01-16 18:21:00'}, {'date': '09 Jun 2016, 12:46'}, {'date': '09 Aug 2016, 22:36'}, {'date': '13 Feb 2018, 17:05'}, {'date': '2015-04-13 02:21:33'}, {'date': '23 Feb 2015, 21:00'}, {'date': 'July 15, 2019 at 02:50 PM'}, {'date': '31 Dec 2013, 06:19'}, {'date': 'March 21, 2016 at 04:32 PM'}, {'date': '2011-12-14 14:24:00'}, {'date': 'September 05, 2020 at 06:28 PM'}, {'date': '2019-02-11 06:49:17'}, {'date': '2019-04-09 05:52:00'}, {'date': '2013-09-26 23:24:41'}, {'date': 'April 17, 2016 at 08:31 PM'}, {'date': 'October 26, 2016 at 01:27 PM'}, {'date': '05 May 2014, 05:18'}, {'date': '31 Jul 2014, 15:42'}, {'date': '22 Dec 2014, 01:47'}, {'date': '2016-12-02 00:06:00'}, {'date': '08 Aug 2014, 18:05'}, {'date': '2019-02-08 18:22:00'}, {'date': 'March 10, 2020 at 01:49 AM'}, {'date': '29 Jul 2017, 10:30'}, {'date': 'November 14, 2014 at 10:01 PM'}, {'date': '07 Aug 2019, 20:31'}, {'date': 'December 16, 2016 at 04:32 AM'}, {'date': '02 Mar 2016, 23:35'}, {'date': '2012-07-27 00:46:35'}, {'date': '2010-09-29 19:30:00'}, {'date': '29 Dec 2018, 21:14'}, {'date': '20 Jun 2020, 00:03'}, {'date': '28 May 2021, 18:02'}, {'date': '19 Oct 2015, 15:54'}, {'date': '2017-07-17 21:38:00'}, {'date': '2019-01-05 19:43:00'}, {'date': 'October 20, 2011 at 07:03 PM'}, {'date': '08 Jan 2013, 23:14'}, {'date': 'August 26, 2019 at 09:23 PM'}, {'date': '10 Jul 2013, 14:11'}, {'date': '14 Jun 2012, 08:25'}, {'date': 'September 28, 2021 at 03:37 PM'}, {'date': '10 Jun 2021, 21:23'}, {'date': 'January 20, 2015 at 04:21 AM'}, {'date': 'June 25, 2018 at 06:23 PM'}, {'date': '30 Nov 2017, 22:10'}, {'date': 'May 04, 2020 at 07:49 PM'}, {'date': 'November 10, 2011 at 02:47 PM'}, {'date': '20 Jun 2018, 16:16'}, {'date': '28 Sep 2013, 01:24'}, {'date': 'May 13, 2016 at 02:24 PM'}], 'var_function-call-4625815798308216618': 'file_storage/function-call-4625815798308216618.json'}

exec(code, env_args)
