code = """import json

file_path = locals()['var_function-call-11540516602756077214']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Keywords
keywords = {
    "Business": ["stock", "market", "economy", "company", "profit", "oil", "price", "business", "corp", "inc", "bank", "investment", "fund", "trade", "dollar", "euro", "yen", "wall st", "nasdaq", "dow", "share", "revenue", "sale", "merger", "acquisition", "deal", "financial", "credit", "rate", "inflation", "ceo", "cfo", "money", "cost", "spending", "industry", "fed", "federal reserve"],
    "Sci/Tech": ["computer", "software", "technology", "internet", "web", "science", "space", "nasa", "phone", "microsoft", "apple", "google", "intel", "ibm", "server", "virus", "hacker", "online", "digital", "chip", "wireless", "network", "broadband", "satellite", "robot", "gadget", "linux", "windows", "browser", "search engine", "biotech", "unix", "application", "developer", "code", "program", "spam", "email", "orbit", "mission", "astronaut", "launch", "telescope", "physics", "biology"],
    "Sports": ["football", "baseball", "basketball", "soccer", "tennis", "golf", "olympic", "championship", "tournament", "league", "cup", "racing", "athlete", "medal", "coach", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "wimbledon", "super bowl", "world cup", "athens", "cycling", "swimming", "boxing", "hockey", "rugby", "cricket", "f1", "racer", "gold", "silver", "bronze", "stadium", "club", "red sox", "yankees", "lakers", "pistons", "formula one", "grand prix", "quarterback", "touchdown", "homerun", "inning", "pitcher", "goalkeeper", "striker", "marathon", "sprint"],
    "World": ["iraq", "president", "war", "government", "election", "minister", "country", "peace", "military", "police", "kill", "bomb", "blast", "explosion", "terror", "attack", "politic", "official", "diplomat", "un", "united nations", "eu", "european union", "israel", "palestin", "bush", "kerry", "putin", "china", "russia", "iran", "korea", "nuclear", "troop", "army", "prime minister", "baghdad", "gaza", "afghanistan", "voter", "vote", "poll", "parliament", "senate", "congress", "democrat", "republican"]
}

# Exclusion list for Sports
sports_exclusion = ["software", "windows", "unix", "linux", "microsoft", "intel", "internet", "computer", "stock", "market", "prices", "oil", "iraq", "president", "war", "bush", "kerry", "google", "ipo", "profit", "economy", "dollar", "technology", "server", "nasdaq", "dow jones", "wall street", "space", "orbit", "nasa", "science", "research", "lab"]

sports_articles = []

for art in articles:
    text = (art.get('title', '') + " " + art.get('description', '')).lower()
    
    # Check exclusion
    if any(ex in text for ex in sports_exclusion):
        continue

    scores = {cat: 0 for cat in keywords}
    for cat, keys in keywords.items():
        for k in keys:
            if k in text:
                scores[cat] += 1
    
    best_cat = max(scores, key=scores.get)
    
    if scores[best_cat] > 0 and best_cat == "Sports":
        # Additional safety: if tie with Business or Sci/Tech or World?
        # Check if Sports score is strictly greater than others
        if all(scores["Sports"] > scores[c] for c in keywords if c != "Sports" and scores[c] > 0):
             sports_articles.append(art)
        elif scores["Sports"] > 0 and scores["Sports"] == max(scores.values()):
             # If tie, only accept if tied with nothing (others are 0) or ...
             # Tie with World/Business might be tricky.
             # Let's exclude ties.
             if list(scores.values()).count(scores["Sports"]) == 1:
                 sports_articles.append(art)
             else:
                 # It's a tie. Skip to be safe? Or include?
                 # Tie with World: "Olympic peace"?
                 # Tie with Business: "Sports team sold"?
                 pass

# Find max description length
longest_desc_art = None
max_len = -1

for art in sports_articles:
    desc_len = len(art.get('description', ''))
    if desc_len > max_len:
        max_len = desc_len
        longest_desc_art = art

result = {
    "count_sports": len(sports_articles),
    "total_articles": len(articles)
}

if longest_desc_art:
    result.update({
        "title": longest_desc_art['title'],
        "description_length": max_len,
        "description": longest_desc_art['description']
    })
else:
    result["error"] = "No sports articles found"

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-12594114767327251742': ['articles'], 'var_function-call-5270483452774594840': [{'_id': '69446d9169b041cb64e43401', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-8096038159271761827': ['authors', 'article_metadata'], 'var_function-call-15141708381897059680': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-2396374694705425971': [{'_id': '69446d9169b041cb64e43401', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446d9169b041cb64e43402', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446d9169b041cb64e43403', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446d9169b041cb64e43404', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446d9169b041cb64e43405', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-3178287544905296170': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-5984680396501901704': {'count': 5, 'sample_titles': ['Wall St. Bears Claw Back Into the Black (Reuters)', 'Carlyle Looks Toward Commercial Aerospace (Reuters)', "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'Oil prices soar to all-time record, posing new menace to US economy (AFP)']}, 'var_function-call-15234722739855961936': 'file_storage/function-call-15234722739855961936.json', 'var_function-call-17770637732625910946': {'title': "Why Windows isn't Unix", 'description_length': 708, 'description': '\\\\"I first heard about this from one of the developers of the hit game SimCity, who\\told me that there was a critical bug in his application: it used memory right\\after freeing it, a major no-no that happened to work OK on DOS but would not\\work under Windows where memory that is freed is likely to be snatched up by\\another running application right away. The testers on the Windows team were\\going through various popular applications, testing them to make sure they\\worked OK, but SimCity kept crashing. They reported this to the Windows\\developers, who disassembled SimCity, stepped through it in a debugger, found\\the bug, and added special code that checked if SimCity was running, and if it\\did ...\\\\'}, 'var_function-call-13529367684207534136': {'title': 'China Begins Countdown for Next Manned Space Flight', 'description_length': 580, 'description': 'By ELAINE KURTENBACH    SHANGHAI, China (AP) -- Chinese astronauts are in the final stages of preparing for a manned space mission that will orbit the globe 14 times before returning to Earth, a state-run newspaper reported Thursday.    The launch, expected sometime this month, will initially send a manned craft, the Shenzhou 5, into an oval orbit that at its closest will be 125 miles from Earth, the Liberation Daily reported, citing "relevant channels."    After circling the earth several times, the ship will enter an orbit at about 220 miles from earth, the report said...'}, 'var_function-call-11191629561345527874': {'title': 'DiMarco, Riley Play Way Into Ryder Cup (AP)', 'description_length': 483, 'description': "AP - Chris DiMarco and Chris Riley faced knee-knocking pressure in the last round of the PGA Championship. And what did they get for their efforts? More of the same. DiMarco and Riley played themselves into the pressure-packed Ryder Cup with their performances Sunday in the year's final major. DiMarco finished second after a three-man, three-hole playoff and Riley was fourth  #151; good enough to knock Jay Haas and Steve Flesch out of the top 10 in the Ryder Cup point standings."}, 'var_function-call-11540516602756077214': 'file_storage/function-call-11540516602756077214.json'}

exec(code, env_args)
