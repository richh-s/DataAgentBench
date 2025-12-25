code = """import json
import re

file_path = locals()['var_function-call-15612293713888002429']

with open(file_path, 'r') as f:
    articles = json.load(f)

# Keywords
sports_keywords = {
    "sport", "sports", "football", "soccer", "basketball", "baseball", "hockey", "tennis", "golf",
    "rugby", "cricket", "boxing", "wrestling", "racing", "motorsport", "f1", "nascar",
    "olympic", "olympics", "olympiad", "medal", "athlete", "athletics", "swimming", "gymnastics",
    "marathon", "triathlon", "skiing", "skating", "snowboarding",
    "nba", "nfl", "mlb", "nhl", "fifa", "uefa", "pga", "lpga", "atp", "wta",
    "wimbledon", "super bowl", "world cup", "stanley cup", "davis cup", "ryder cup",
    "championship", "tournament", "league", "playoff", "playoffs",
    "stadium", "arena", "coach", "quarterback", "goalkeeper", "striker", "pitcher", "batter",
    "touchdown", "homerun", "slam dunk", "hat trick",
    "lakers", "knicks", "bulls", "celtics", "warriors", "spurs", "pistons", "heat",
    "yankees", "red sox", "mets", "dodgers", "giants", "cardinals", "cubs", "phillies", "braves",
    "patriots", "eagles", "cowboys", "steelers", "packers", "bears", "raiders", "broncos",
    "manchester united", "arsenal", "liverpool", "chelsea", "real madrid", "barcelona", "bayern munich", "juventus", "ac milan",
    "red wings", "maple leafs", "canadiens", "rangers", "bruins", "flyers",
    "formula one", "grand prix"
}

business_keywords = {
    "business", "company", "corp", "corporation", "inc", "ltd", "stock", "market", "share", "finance", "financial",
    "economy", "economic", "dollar", "euro", "yen", "currency", "trade", "investment", "investor", "profit", "revenue",
    "loss", "earnings", "bank", "banking", "deal", "merger", "acquisition", "buyout", "ceo", "cfo", "wall street",
    "dow jones", "nasdaq", "s&p", "oil", "price", "prices", "sales", "retail"
}

tech_keywords = {
    "technology", "tech", "science", "computer", "software", "hardware", "internet", "web", "online", "digital",
    "mobile", "phone", "wireless", "broadband", "network", "server", "chip", "processor", "semiconductor",
    "microsoft", "google", "apple", "intel", "ibm", "cisco", "oracle", "yahoo", "amazon", "ebay",
    "linux", "windows", "virus", "worm", "hacker", "security", "space", "nasa", "astronomy", "satellite"
}

world_keywords = {
    "world", "international", "government", "politics", "political", "president", "minister", "prime minister",
    "official", "leader", "election", "vote", "party", "congress", "senate", "parliament", "war", "peace",
    "military", "army", "navy", "air force", "troops", "soldier", "attack", "bomb", "blast", "explosion",
    "police", "crime", "court", "judge", "law", "legal", "iraq", "iran", "afghanistan", "israel", "palestine",
    "china", "russia", "eu", "european union", "un", "united nations"
}

def classify(title, desc):
    text = (title + " " + desc).lower()
    # Remove punctuation for word matching
    words = set(re.findall(r'\b\w+\b', text))
    
    s_score = len(words.intersection(sports_keywords))
    b_score = len(words.intersection(business_keywords))
    t_score = len(words.intersection(tech_keywords))
    w_score = len(words.intersection(world_keywords))
    
    # Heuristics
    if "olympic" in text or "olympics" in text:
        s_score += 5
    if "nba" in text or "nfl" in text or "mlb" in text or "nhl" in text:
        s_score += 5
    
    scores = {'Sports': s_score, 'Business': b_score, 'Sci/Tech': t_score, 'World': w_score}
    
    # Get max score
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return "Unknown"
    
    # Tie breaking?
    # Usually sports is distinct.
    # If "game" is present, check if "video" or "computer" is present (Tech).
    if "game" in words and ("video" in words or "computer" in words or "console" in words):
        t_score += 5
        if t_score > s_score:
            return 'Sci/Tech'
            
    return best_cat

max_len = -1
best_article = None

for art in articles:
    title = art.get('title', '')
    desc = art.get('description', '')
    if not desc:
        continue
    
    cat = classify(title, desc)
    
    if cat == 'Sports':
        if len(desc) > max_len:
            max_len = len(desc)
            best_article = art

print("__RESULT__:")
print(json.dumps(best_article))"""

env_args = {'var_function-call-6513570509615239386': ['authors', 'article_metadata'], 'var_function-call-6513570509615242717': [{'_id': '6944884d534a15233af03e42', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-17762501110464143052': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-4622591016866841051': [{'_id': '6944884d534a15233af03e42', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944884d534a15233af03e43', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944884d534a15233af03e44', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944884d534a15233af03e45', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944884d534a15233af03e46', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-3354242101260204773': [{'author_id': '0', 'name': 'Felicia Miles'}], 'var_function-call-6890103473169118366': [{'region': 'Asia'}, {'region': 'North America'}, {'region': 'South America'}, {'region': 'Europe'}, {'region': 'Africa'}], 'var_function-call-15016213404923792143': [{'cnt': '127600'}], 'var_function-call-3419387817260907694': [{'_id': '6944884d534a15233af03f46', 'article_id': '260', 'title': 'Ancient Olympics Mixed Naked Sports, Pagan Partying', 'description': 'Nude athletes, performance-enhancing lizard meat, and animal sacrifices are just a few of the things that separate the ancient Olympics from the modern games, says the author of &lt;i&gt;The Naked Olympics.&lt;/i&gt;'}, {'_id': '6944884d534a15233af041bc', 'article_id': '890', 'title': 'Briefly: AOL kicks off free fantasy sports', 'description': "roundup Plus: HP partners with 3G gear maker...AMD starts shipping 90-nanometer chips...ABC.com to air on Real's SuperPass."}, {'_id': '6944884d534a15233af044cf', 'article_id': '1677', 'title': 'Olympics-Shooting-loving Rathore promotes Olympic sports', 'description': 'ATHENS, Aug 17 (Reuters) - Rajyavardhan Singh Rathore loves cricket as much as any Indian, even if the national obsession with ball and bat can make it hard for the country #39;s Olympic athletes to get a look in. '}, {'_id': '6944884d534a15233af0483c', 'article_id': '2554', 'title': 'E-passports to put new face on old documents', 'description': 'Countries begin test programs--get ready for a facial scan the next time you take an overseas flight.'}, {'_id': '6944884d534a15233af0490a', 'article_id': '2760', 'title': 'Sportsview: Bills Get Playoff Hunger (AP)', 'description': 'AP - Pat Williams is a big man with a big heart and appetite. So imagine his dilemma when the Buffalo Bills were back to their bumbling selves at the start of this season.'}], 'var_function-call-7820992371091763764': [{'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13484661405459322591': 5, 'var_function-call-6846647973350822076': 'file_storage/function-call-6846647973350822076.json', 'var_function-call-15612293713888002429': 'file_storage/function-call-15612293713888002429.json'}

exec(code, env_args)
