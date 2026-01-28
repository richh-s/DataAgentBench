code = """import json
import pandas as pd

with open(var_call_wjijicMPNedUw4ONyAHg4xMA, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
for col in ['article_id','title','description']:
    if col not in df.columns:
        df[col] = ''

df['title'] = df['title'].fillna('').astype(str)
df['description'] = df['description'].fillna('').astype(str)
df['desc_len'] = df['description'].apply(len)

sports_keywords = [
    'pga','ryder','world cup','worldcup','olympic','olympics','olympic','broncos','bills','vikings','packers','cowboys',
    'giants','patriots','jets','eagles','bears','ravens','steelers','browns','chargers','seahawks','niners','49ers',
    'mcgahee','pronger','roddick','venus','navratilova','phelps','thorpe','golf','golfers','pga','mlb','nba','nfl','nhl',
    'mls','playoff','playoffs','quarterback','touchdown','innings','inning','homered','home run','batting','runs','beat','beats','beat','defeat','defeats','wins','win','won','advances','advance','semifinal','final','championship','champion','scored','score','scoring'
]

lower_text = (df['title'] + ' ' + df['description']).str.lower()
mask = lower_text.apply(lambda t: any(k in t for k in sports_keywords))

sports_df = df[mask].copy()

if sports_df.empty:
    out = {'count':0,'top_titles':[], 'max_desc_len':None}
else:
    max_len = int(sports_df['desc_len'].max())
    tops = sports_df[sports_df['desc_len']==max_len][['article_id','title','desc_len']].to_dict(orient='records')
    out = {'count': int(sports_df.shape[0]), 'max_desc_len': max_len, 'top_titles': tops}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_wjijicMPNedUw4ONyAHg4xMA': 'file_storage/call_wjijicMPNedUw4ONyAHg4xMA.json', 'var_call_cx5PEPS95YUVsIvlHoiREaKF': None, 'var_call_Ats8FczWZ8SwMGxhTTwZuUnX': {'count': 0, 'top_title': None, 'top_desc_len': None, 'candidates': []}, 'var_call_aJqG3rrWo7CQ8FQ1AtonOPh1': 'file_storage/call_aJqG3rrWo7CQ8FQ1AtonOPh1.json', 'var_call_nruyzJAR6yKoMAqgfjuLfSis': 'AMD starts shipping 90-nanometer chips to customers', 'var_call_MxCX9FDWB4fvOaQ9UoMoSgsv': [{'article_id': '368', 'title': 'AMD starts shipping 90-nanometer chips to customers', 'desc_len': 810}, {'article_id': '443', 'title': 'Technology as Fashion', 'desc_len': 749}, {'article_id': '183', 'title': "Why Windows isn't Unix", 'desc_len': 708}, {'article_id': '184', 'title': 'Microsoft, IE and Bloat', 'desc_len': 708}, {'article_id': '175', 'title': 'Ron Regan Jr is My Kinda Guy', 'desc_len': 708}, {'article_id': '167', 'title': 'RuntimeProperties... Reflection from System Properties', 'desc_len': 708}, {'article_id': '172', 'title': 'Pretty Log4J', 'desc_len': 708}, {'article_id': '618', 'title': "I Confess.  I'm a Software Pirate.", 'desc_len': 708}, {'article_id': '177', 'title': 'Mission Accomplished!', 'desc_len': 672}, {'article_id': '181', 'title': 'What would Baby Jesus Think?', 'desc_len': 591}, {'article_id': '279', 'title': 'China Begins Countdown for Next Manned Space Flight', 'desc_len': 580}, {'article_id': '159', 'title': 'Customers of Telco Companies Face Privacy Breach', 'desc_len': 540}, {'article_id': '709', 'title': 'Muddling Through (or Not): Mid-2004 Update on the Philippines', 'desc_len': 521}, {'article_id': '661', 'title': 'DiMarco, Riley Play Way Into Ryder Cup (AP)', 'desc_len': 483}, {'article_id': '284', 'title': 'NASA Approves Robotic Hubble Repair Mission', 'desc_len': 480}, {'article_id': '988', 'title': 'Microsoft Lists XP SP2 Problems (NewsFactor)', 'desc_len': 460}, {'article_id': '281', 'title': 'Japanese Lunar Probe Mission Facing Delays', 'desc_len': 454}, {'article_id': '290', 'title': "Last Year's Flu Shot Imperfect But Effective", 'desc_len': 440}, {'article_id': '165', 'title': "Insecurity: (Or Why Americans Aren't Feeling The Recovery)", 'desc_len': 438}, {'article_id': '271', 'title': "Saturn's Moon Titan: Prebiotic Laboratory", 'desc_len': 433}, {'article_id': '303', 'title': 'Progress Is Made Battling Strep Germ', 'desc_len': 422}, {'article_id': '174', 'title': 'Mozilla Exceptions (mexception)', 'desc_len': 421}, {'article_id': '763', 'title': 'They flocked from Games', 'desc_len': 406}, {'article_id': '529', 'title': 'Venezuela Holds Referendum on President', 'desc_len': 405}, {'article_id': '469', 'title': 'Rehabbing his career', 'desc_len': 402}, {'article_id': '69', 'title': 'Autodesk tackles project collaboration', 'desc_len': 402}, {'article_id': '8', 'title': 'Safety Net (Forbes.com)', 'desc_len': 390}, {'article_id': '273', 'title': 'Chandra Celebrates Five Years of Scientific Breakthroughs', 'desc_len': 386}, {'article_id': '552', 'title': 'Computer Naivete Costs A Bundle', 'desc_len': 377}, {'article_id': '767', 'title': 'Phelps #146;s quest for 8 golds goes under', 'desc_len': 373}, {'article_id': '300', 'title': 'Britain Approves Human Cloning', 'desc_len': 371}, {'article_id': '468', 'title': 'Leskanic winning arms race', 'desc_len': 369}, {'article_id': '912', 'title': 'Phelps to Take on Thorpe in Busy Night', 'desc_len': 367}, {'article_id': '562', 'title': 'Zahringer Leads Field at U.S. Amateur (AP)', 'desc_len': 366}, {'article_id': '474', 'title': 'For Revolution, this tie looks good', 'desc_len': 366}, {'article_id': '473', 'title': 'Enough to make you flip', 'desc_len': 365}, {'article_id': '537', 'title': 'Phelps, Thorpe Advance in 200 Freestyle', 'desc_len': 361}, {'article_id': '582', 'title': 'Phelps, Rival Thorpe in 200M-Free Semis', 'desc_len': 361}, {'article_id': '245', 'title': 'News: Droughts Like 1930s Dust Bowl May Have Been Unexceptional in Prehistoric Times, New Study Suggests', 'desc_len': 361}, {'article_id': '688', 'title': 'McGahee Helps Bills Beat Broncos 16-6 (AP)', 'desc_len': 360}, {'article_id': '656', 'title': 'Singh Wins PGA Championship in Playoff (AP)', 'desc_len': 360}, {'article_id': '533', 'title': 'Phelps, Thorpe Advance in 200 Freestyle', 'desc_len': 358}, {'article_id': '744', 'title': 'Pronger opts out of World Cup', 'desc_len': 352}, {'article_id': '603', 'title': 'Roddick, Venus, Navratilova Win Openers (AP)', 'desc_len': 350}, {'article_id': '963', 'title': 'PivX hardens Windows with Qwik-Fix Pro', 'desc_len': 346}, {'article_id': '547', 'title': 'A Digital Doctor Treats Computer Contamination (washingtonpost.com)', 'desc_len': 345}, {'article_id': '270', 'title': 'Hubble Peers Inside a Celestial Geode', 'desc_len': 345}, {'article_id': '448', 'title': 'Phelps, Thorpe Advance in 200 Freestyle (AP)', 'desc_len': 344}, {'article_id': '291', 'title': 'Olympics Could Call Out the Couch Potatoes', 'desc_len': 341}, {'article_id': '749', 'title': 'Dorman #146;s been dandy of late', 'desc_len': 341}]}

exec(code, env_args)
