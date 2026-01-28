code = """import json

result_file = locals()['var_functions.query_db:2']
with open(result_file, 'r') as f:
    articles_data = json.load(f)

# Very strict identification of sports articles only
sports_articles = []

for article in articles_data:
    title = article.get('title', '')
    desc = article.get('description', '')
    title_lower = title.lower()
    desc_lower = desc.lower()
    description = article.get('description', '')
    
    is_sports = False
    
    # EXPLICIT sports indicators only
    # Olympic Games
    if 'olympic' in title_lower or 'olympic' in desc_lower:
        is_sports = True
    
    # Games in Athens/Greece context (Olympic Games)
    elif 'games' in title_lower and ('athens' in desc_lower or 'greece' in desc_lower):
        is_sports = True
    
    # Major sports leagues
    elif any(league in title_lower or league in desc_lower for league in ['nfl', 'nba', 'mlb', 'nhl']):
        is_sports = True
    
    # Specific sports with athletic context (exclude video games)
    elif any(sport in title_lower or sport in desc_lower for sport in ['football', 'soccer', 'tennis', 'golf', 'basketball', 'baseball', 'hockey']):
        if not ('video game' in desc_lower or title == 'Why Windows isn\'t Unix'):
            if any(context in title_lower or context in desc_lower for context in ['team', 'player', 'coach', 'championship', 'tournament', 'game', 'match']):
                is_sports = True
    
    if is_sports:
        sports_articles.append({
            'title': title,
            'desc_length': len(description)
        })

# Find the sports article with the longest description
if sports_articles:
    longest = max(sports_articles, key=lambda x: x['desc_length'])
    result = longest['title']
else:
    result = "No sports articles found"

# Also provide some debug info
print('Found', len(sports_articles), 'sports articles')
sports_articles_sorted = sorted(sports_articles, key=lambda x: x['desc_length'], reverse=True)[:5]
print('Top 5 by length:', [(a['title'], a['desc_length']) for a in sports_articles_sorted])

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': "Why Windows isn't Unix", 'var_functions.execute_python:12': 1000, 'var_functions.execute_python:16': "Why Windows isn't Unix", 'var_functions.execute_python:20': "Why Windows isn't Unix", 'var_functions.execute_python:22': 'Examining 1000 articles for sports content', 'var_functions.execute_python:24': "Last Year's Flu Shot Imperfect But Effective", 'var_functions.execute_python:26': 'China Begins Countdown for Next Manned Space Flight', 'var_functions.execute_python:28': 'China Begins Countdown for Next Manned Space Flight', 'var_functions.execute_python:30': "Why Windows isn't Unix", 'var_functions.execute_python:32': 'They flocked from Games', 'var_functions.execute_python:34': {'title': 'They flocked from Games', 'description': "ATHENS -- During yesterday's celebration of the assumption of the Virgin Mary, the Greek orthodox clergy had a stern reminder for the organizers of the Olympic Games: No matter what the advertisements and speeches say about Greece's modern, Western orientation, this country is still the domain of its decidedly traditional, ubiquitous state-sanctioned religion. Speaking over the Byzantine chants of a ...", 'description_length': 406}, 'var_functions.execute_python:36': {'title': "Why Windows isn't Unix", 'description_length': 708, 'top_5_sports_articles': [{'title': "Why Windows isn't Unix", 'description': '\\\\"I first heard about this from one of the developers of the hit game SimCity, who\\told me that there was a critical bug in his application: it used memory right\\after freeing it, a major no-no that happened to work OK on DOS but would not\\work under Windows where memory that is freed is likely to be snatched up by\\another running application right away. The testers on the Windows team were\\going through various popular applications, testing them to make sure they\\worked OK, but SimCity kept crashing. They reported this to the Windows\\developers, who disassembled SimCity, stepped through it in a debugger, found\\the bug, and added special code that checked if SimCity was running, and if it\\did ...\\\\', 'desc_length': 708}, {'title': 'Microsoft, IE and Bloat', 'description': '\\\\Zawodny  threads off of Scoble  on the IE issue:\\\\"I have to say, when I first read that I nearly fell off my chair laughing. I was\\thinking "how stupid ARE these IE guys?!?!?!" But we all know that Microsoft is\\full of smart people who care about what they\'re doing. So something really\\doesn\'t compute here."\\\\"Last time I checked, IE wasn\'t even close to feature parity with Mozilla\'s\\browsers. No popup blocking, no tabbed browsing, etc."\\\\"Does the IE team really not know what their product is missing?"\\\\Perhaps.  It\'s highly likely that they just don\'t know.\\\\The bigger issue here is that Microsoft products can\'t fail and they can\'t\\succeed.  Microsoft has 40-50 billion in the bank.  There ...\\\\', 'desc_length': 708}, {'title': 'China Begins Countdown for Next Manned Space Flight', 'description': 'By ELAINE KURTENBACH    SHANGHAI, China (AP) -- Chinese astronauts are in the final stages of preparing for a manned space mission that will orbit the globe 14 times before returning to Earth, a state-run newspaper reported Thursday.    The launch, expected sometime this month, will initially send a manned craft, the Shenzhou 5, into an oval orbit that at its closest will be 125 miles from Earth, the Liberation Daily reported, citing "relevant channels."    After circling the earth several times, the ship will enter an orbit at about 220 miles from earth, the report said...', 'desc_length': 580}, {'title': 'NASA Approves Robotic Hubble Repair Mission', 'description': '(AP) -- NASA\'s chief is urging his Hubble Space Telescope team to press ahead with plans for a robotic repair mission to the aging observatory, saying, "Let\'s go save the Hubble."    Administrator Sean O\'Keefe says he will ask Congress for money to accomplish the job. He estimates it will take about \\$1 billion to \\$1.6 billion to develop and launch a robot to make the needed upgrades to keep the popular telescope running and to get it out of orbit once its work is through...', 'desc_length': 480}, {'title': "Last Year's Flu Shot Imperfect But Effective", 'description': "By Amanda Gardner, HealthDay Reporter    HealthDayNews -- Last year's influenza vaccine was far from a perfect match against the virus that sickened people, but it offered more protection from the illness than experts had previously thought.    In very young children, the shot was found to be 25 percent to 49 percent effective in preventing influenza-like illness, which is a suspected case of flu that wasn't confirmed in a laboratory...", 'desc_length': 440}]}, 'var_functions.execute_python:38': 'China Begins Countdown for Next Manned Space Flight', 'var_functions.execute_python:40': 'China Begins Countdown for Next Manned Space Flight', 'var_functions.execute_python:42': 'They flocked from Games', 'var_functions.execute_python:46': 'China Begins Countdown for Next Manned Space Flight', 'var_functions.execute_python:48': 'China Begins Countdown for Next Manned Space Flight'}

exec(code, env_args)
