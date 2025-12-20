code = """import json
import re

# Load the data
file_path = locals()['var_function-call-4072584036690662513']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define keywords
sports_keywords = {
    "sport", "sports", "football", "baseball", "basketball", "hockey", "tennis", "golf", 
    "soccer", "olympic", "olympics", "medal", "gold", "silver", "bronze", "athens", 
    "game", "match", "tournament", "cup", "league", "championship", "champion", 
    "team", "coach", "athlete", "player", "score", "win", "victory", "defeat", 
    "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "nascar", "f1", "racing", "driver", 
    "swim", "gymnastics", "marathon", "sprint", "stadium", "referee", "umpire", 
    "quarterback", "touchdown", "goal", "striker", "midfielder", "defender", "goalkeeper",
    "wrestling", "boxing", "round", "knockout", "bout", "interception", "baseman", "inning",
    "homerun", "puck", "lap", "pole", "rugby", "cricket", "wicket", "bowler", "batsman",
    "doping", "drug", "ban", "record", "world record", "final", "semifinal", "quarterfinal"
}

non_sports_keywords = {
    "market", "stock", "price", "oil", "economy", "business", "company", "corp", "inc", 
    "shares", "investor", "profit", "revenue", "iraq", "war", "military", "president", 
    "election", "minister", "software", "internet", "technology", "microsoft", "google", 
    "apple", "ibm", "court", "judge", "police", "bomb", "kill", "dead", "died", "attack",
    "un", "united nations", "eu", "european union", "nuclear", "terror", "terrorist",
    "windows", "unix", "linux", "system", "computer", "application", "program", "code", 
    "bug", "developer", "server", "data", "file", "network", "politics", "senate", 
    "congress", "democrat", "republican", "kerry", "bush", "vote", "voter", "campaign", 
    "navy", "army", "soldier", "vietnam", "prize", "rocket", "space", "launch", 
    "science", "nasa", "orbit", "wireless", "broadband", "chip", "intel", "amd"
}

candidates = []

for art in articles:
    title = art.get('title', '')
    desc = art.get('description', '')
    full_text = (title + " " + desc).lower()
    # Remove punctuation for keyword matching
    clean_text = re.sub(r'[^\w\s]', '', full_text)
    words = set(clean_text.split())
    
    s_score = len(words.intersection(sports_keywords))
    ns_score = len(words.intersection(non_sports_keywords))
    
    # Specific exclusion for 'drug' in non-sports context (e.g. pharma)
    if "drug" in words and ("pharma" in words or "fda" in words):
        ns_score += 2
        
    # Heuristic: Must have some sports keywords. 
    # If ns_score is high, likely not sports unless s_score is very high.
    if s_score > 0 and s_score >= ns_score:
        candidates.append({
            "title": title,
            "description": desc,
            "len": len(desc),
            "s_score": s_score,
            "ns_score": ns_score
        })

# Sort by description length descending
candidates.sort(key=lambda x: x['len'], reverse=True)

# Print top 15 results
print("__RESULT__:")
print(json.dumps(candidates[:15]))"""

env_args = {'var_function-call-17593565785959345447': [{'_id': '69447dd145be82594bde559a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447dd145be82594bde559b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447dd145be82594bde559c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447dd145be82594bde559d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447dd145be82594bde559e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17079897375883321610': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_function-call-7209232652231767810': [{'_id': '69447dd145be82594bde559a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447dd145be82594bde559b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447dd145be82594bde559c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447dd145be82594bde559d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447dd145be82594bde559e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17184403664428919554': [{'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-4072584036690662513': 'file_storage/function-call-4072584036690662513.json', 'var_function-call-15886135838529908688': [{'title': "Why Windows isn't Unix", 'description': '\\\\"I first heard about this from one of the developers of the hit game SimCity, who\\told me that there was a critical bug in his application: it used memory right\\after freeing it, a major no-no that happened to work OK on DOS but would not\\work under Windows where memory that is freed is likely to be snatched up by\\another running application right away. The testers on the Windows team were\\going through various popular applications, testing them to make sure they\\worked OK, but SimCity kept crashing. They reported this to the Windows\\developers, who disassembled SimCity, stepped through it in a debugger, found\\the bug, and added special code that checked if SimCity was running, and if it\\did ...\\\\', 'len': 708, 's_score': 2, 'o_score': 0}, {'title': 'THECHAT', 'description': '&lt;em&gt; Dean Cain has spent much of his life in a uniform. He\'s done time as an all-American safety at Princeton (where he established a since-broken single-season Division I-AA record for interceptions), an undrafted free agent with the Buffalo Bills (before a preseason knee injury ended his football career), a sportsman of the future (in the aptly named movie "Futuresport") and an iconic superhero (in television\'s "Lois and Clark: The New Adventures of Superman"). Next up is a set of pinstripes -- Cain plays star third baseman Conrad Dean in the CBS drama "Clubhouse," which is scheduled to debut next month. &lt;/em&gt;', 'len': 631, 's_score': 1, 'o_score': 0}, {'title': 'Canadian Ansari X Prize Entrant Takes the Plunge in Test (SPACE.com)', 'description': 'SPACE.com - A Canadian team of rocketeers has moved one step closer to\\launching its own manned spacecraft with the successful parachute drop test of a\\crew capsule today.\\\\ nbsp;\\\\The backers of Canadian Arrow, a rocket entry in the  #36;10 million\\Ansari X Prize competition, watched happily as their crew compartment drifted\\down into Lake Ontario.\\\\ nbsp;\\\\Today totally proves our Canadian Arrow design, said\\Geoff Sheerin, leader of the London, Ontario-based Arrows bid for the X Prize.\\It went really well and everything worked as it should. ...', 'len': 552, 's_score': 1, 'o_score': 0}, {'title': "Unit's Report Supports Kerry's Version", 'description': "WASHINGTON - The Navy task force overseeing John Kerry's swift boat squadron in Vietnam reported that his group of boats came under enemy fire during a March 13, 1969, incident that three decades later is being challenged by the Democratic presidential nominee's critics.    The March 18, 1969, weekly report from Task Force 115, which was located by The Associated Press during a search of Navy archives, is the latest document to surface that supports Kerry's description of an event for which he won a Bronze Star and a third Purple Heart...", 'len': 544, 's_score': 1, 'o_score': 0}, {'title': 'U.S. Bounces Back to Beat Greece 77-71', 'description': "ATHENS, Greece - Lamar Odom made a key defensive play on Greece's Dimitris Pipanikoulaou, preventing him from getting a clean layup attempt that could have cut the United States' lead to two points, and the Americans won 77-71 Tuesday night in the second round of the Olympic men's basketball tournament.    In a much closer game than expected, the Americans bounced back from their embarrassing loss to Puerto Rico in their opener and avoided dropping to 0-2, which would have matched their loss total from the previous 68 years...", 'len': 532, 's_score': 6, 'o_score': 0}]}

exec(code, env_args)
