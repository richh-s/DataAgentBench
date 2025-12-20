code = """import json
import re

file_path = locals()['var_function-call-16498150637540614880']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Strong sports keywords
sports_keywords = [
    "olympic", "olympics", "athens", "athlete", "athletics", "medal", "medals",
    "basketball", "nba", "knicks", "lakers", "celtics", "spurs", "pistons", "bulls", "heat",
    "baseball", "mlb", "yankees", "red sox", "mets", "dodgers", "cubs", "cardinals", "braves", "marlins", "giants",
    "football", "nfl", "quarterback", "touchdown", "super bowl", "patriots", "eagles", "colts", "steelers",
    "soccer", "fifa", "uefa", "premier league", "manchester united", "arsenal", "liverpool", "real madrid", "barcelona", "chelsea",
    "tennis", "wimbledon", "us open", "grand slam", "agassi", "roddick", "federer", "serena", "venus", "sharapova",
    "golf", "pga", "tiger woods", "masters", "ryder cup",
    "hockey", "nhl", "stanley cup",
    "cycling", "tour de france", "lance armstrong",
    "swimming", "michael phelps", "ian thorpe",
    "gymnastics", "marathon", "sprint",
    "f1", "formula one", "nascar", "racing", "driver", "grand prix",
    "boxing", "wrestling", "championship", "tournament", "world cup"
]

# Compile regex
pattern = re.compile(r'\b(' + '|'.join(sports_keywords) + r')\b', re.IGNORECASE)

candidates = []

for art in articles:
    title = art.get('title', '')
    desc = art.get('description', '')
    text = (title + " " + desc).lower()
    
    match = pattern.search(text)
    if match:
        matched_kw = match.group(1)
        
        # Filtering False Positives
        # "gold" alone -> check context
        # "medal" alone -> check context (Medal of Honor)
        # "driver" -> could be hardware driver
        # "racing" -> "heart racing"
        
        valid = True
        
        if matched_kw == "driver" and ("software" in text or "hardware" in text or "computer" in text):
            valid = False
        
        if matched_kw == "racing" and ("heart" in text):
            valid = False
            
        if "medal" in matched_kw and "honor" in text:
            valid = False
            
        if matched_kw == "gold" or matched_kw == "silver" or matched_kw == "bronze":
            # These are not in my strict list above (I put "medal" etc, but "gold" is common in business)
            # Wait, I didn't put "gold" in the strict list above? 
            # I put "medal", "gold medal".
            pass
            
        # Specific check for "THECHAT" (Entertainment)
        if "cbs drama" in text or "movie" in text:
            # Likely entertainment
            # But let's keep it flagged to see
            art['is_entertainment'] = True
        else:
            art['is_entertainment'] = False

        if valid:
            candidates.append({
                "title": title,
                "desc_len": len(desc),
                "description": desc,
                "matched": matched_kw,
                "is_entertainment": art.get('is_entertainment', False)
            })

# Sort by length
candidates.sort(key=lambda x: x['desc_len'], reverse=True)

print("__RESULT__:")
print(json.dumps(candidates[:10]))"""

env_args = {'var_function-call-4311503606640885860': ['articles'], 'var_function-call-14832231781823878473': [{'_id': '694483ba1f759e2c2778f8e2', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-15881672882449061525': ['authors', 'article_metadata'], 'var_function-call-9407118945008870673': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-1536730069265665031': [{'_id': '694483ba1f759e2c2778f8e2', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694483ba1f759e2c2778f8e3', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694483ba1f759e2c2778f8e4', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694483ba1f759e2c2778f8e5', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694483ba1f759e2c2778f8e6', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6936758391387168330': [{'_id': '694483ba1f759e2c2778f8e2', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694483ba1f759e2c2778f8e3', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694483ba1f759e2c2778f8e4', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694483ba1f759e2c2778f8e5', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694483ba1f759e2c2778f8e6', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-5455468116689382879': 5, 'var_function-call-16498150637540614880': 'file_storage/function-call-16498150637540614880.json', 'var_function-call-16439670988805249589': [{'title': 'AMD starts shipping 90-nanometer chips to customers', 'desc_len': 810, 'description': 'Advanced Micro Devices Inc.\'s (AMD Inc.\'s) 90-nanometer notebook processors are on their way to customers, according to a research note published by Goldman Sachs   Co. Thursday.&lt;p&gt;ADVERTISEMENT&lt;/p&gt;&lt;p&gt;&lt;img src="http://ad.doubleclick.net/ad/idg.us.ifw.general/ibmpseries;sz=1x1;ord=200301151450?" width="1" height="1" border="0"/&gt;&lt;a href="http://ad.doubleclick.net/clk;9824455;9690404;u?http://ad.doubleclick.net/clk;9473681;9688522;d?http://www.ibm.com/servers/eserver/pseries/campaigns/boardroom/index.html?ca=pSeries met=boardroom me=E P_Creative=P_InfoW_RSS"&gt;Introducing IBM eServer p5 systems.&lt;/a&gt;&lt;br/&gt;Powered by IBMs most advanced 64-bit microprocessor (POWER5(tm)), p5 systems can run UNIX and Linux simultaneously. Learn more about eServer p5 systems.&lt;/p&gt;'}, {'title': 'THECHAT', 'desc_len': 631, 'description': '&lt;em&gt; Dean Cain has spent much of his life in a uniform. He\'s done time as an all-American safety at Princeton (where he established a since-broken single-season Division I-AA record for interceptions), an undrafted free agent with the Buffalo Bills (before a preseason knee injury ended his football career), a sportsman of the future (in the aptly named movie "Futuresport") and an iconic superhero (in television\'s "Lois and Clark: The New Adventures of Superman"). Next up is a set of pinstripes -- Cain plays star third baseman Conrad Dean in the CBS drama "Clubhouse," which is scheduled to debut next month. &lt;/em&gt;'}, {'title': 'China Begins Countdown for Next Manned Space Flight', 'desc_len': 580, 'description': 'By ELAINE KURTENBACH    SHANGHAI, China (AP) -- Chinese astronauts are in the final stages of preparing for a manned space mission that will orbit the globe 14 times before returning to Earth, a state-run newspaper reported Thursday.    The launch, expected sometime this month, will initially send a manned craft, the Shenzhou 5, into an oval orbit that at its closest will be 125 miles from Earth, the Liberation Daily reported, citing "relevant channels."    After circling the earth several times, the ship will enter an orbit at about 220 miles from earth, the report said...'}, {'title': "Unit's Report Supports Kerry's Version", 'desc_len': 544, 'description': "WASHINGTON - The Navy task force overseeing John Kerry's swift boat squadron in Vietnam reported that his group of boats came under enemy fire during a March 13, 1969, incident that three decades later is being challenged by the Democratic presidential nominee's critics.    The March 18, 1969, weekly report from Task Force 115, which was located by The Associated Press during a search of Navy archives, is the latest document to surface that supports Kerry's description of an event for which he won a Bronze Star and a third Purple Heart..."}, {'title': 'U.S. Bounces Back to Beat Greece 77-71', 'desc_len': 532, 'description': "ATHENS, Greece - Lamar Odom made a key defensive play on Greece's Dimitris Pipanikoulaou, preventing him from getting a clean layup attempt that could have cut the United States' lead to two points, and the Americans won 77-71 Tuesday night in the second round of the Olympic men's basketball tournament.    In a much closer game than expected, the Americans bounced back from their embarrassing loss to Puerto Rico in their opener and avoided dropping to 0-2, which would have matched their loss total from the previous 68 years..."}]}

exec(code, env_args)
