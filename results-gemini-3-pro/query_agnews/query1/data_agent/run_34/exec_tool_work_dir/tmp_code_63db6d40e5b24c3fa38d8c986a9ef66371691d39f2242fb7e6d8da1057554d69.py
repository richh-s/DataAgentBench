code = """import json
import re

# Load the data
file_path = locals()['var_function-call-10228615712224783799']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define weighted keywords
keywords = {
    "Sports": {
        5: [
            "olympic", "olympics", "olympiad", "medal", "medalist", "stadium", "athlete", "athletics", 
            "championship", "tournament", "nba", "nfl", "mlb", "nhl", "fifa", "uefa", "wimbledon", 
            "superbowl", "world cup", "football", "basketball", "baseball", "soccer", "hockey", "tennis", 
            "golf", "rugby", "cricket", "boxing", "wrestling", "volleyball", "badminton", "swimming", 
            "gymnastics", "marathon", "sprint", "sprinter", "coach", "referee", "umpire", "quarterback", 
            "goalkeeper", "striker", "touchdown", "homerun", "slamdunk", "davis cup", "ryder cup", 
            "stanley cup", "world series", "premier league", "bundesliga", "serie a", "la liga", "athens", 
            "greece", "summer games"
        ],
        1: [
            "sport", "sports", "game", "games", "team", "teams", "match", "matches", "score", "scores", 
            "victory", "defeat", "player", "players", "season", "seasons", "club", "clubs", "win", "wins", 
            "winner", "winners", "cup"
        ]
    },
    "Business": {
        5: [
            "stock", "stocks", "market", "markets", "economy", "economic", "company", "companies", 
            "corp", "corporation", "inc", "profit", "profits", "loss", "losses", "revenue", "merger", 
            "acquisition", "bank", "banks", "dollar", "euro", "yen", "inflation", "fed", "federal reserve", 
            "treasury", "ceo", "cfo", "wall street", "nasdaq", "dow jones", "ipo", "dividend", 
            "shareholder", "investor", "oil"
        ],
        1: [
            "price", "prices", "rate", "rates", "deal", "deals", "trade", "trading", "invest", "investment"
        ]
    },
    "World": {
        5: [
            "president", "minister", "prime minister", "iraq", "iraqi", "iran", "iranian", "war", "wars", 
            "military", "army", "bomb", "bombing", "attack", "attacks", "peace", "treaty", "un", 
            "united nations", "parliament", "senate", "congress", "election", "elections", "vote", 
            "voting", "voter", "voters", "government", "troops", "rebel", "rebels", "terrorist", 
            "terrorism", "al qaeda", "palestinian", "israel", "israeli", "gaza", "baghdad", "kabul", 
            "darfur", "sudan", "russia", "putin", "bush", "kerry", "blair"
        ],
        1: [
            "country", "countries", "official", "officials", "police", "blast", "kill", "killed", "crash"
        ]
    },
    "Sci/Tech": {
        5: [
            "computer", "computers", "software", "hardware", "internet", "web", "website", "google", 
            "microsoft", "apple", "intel", "space", "nasa", "virus", "antivirus", "study", "research", 
            "science", "scientist", "technology", "mobile", "phone", "cellphone", "chip", "processor", 
            "server", "linux", "windows", "spam", "hacker", "digital", "wireless", "broadband", 
            "satellite", "robot", "gadget", "biotechnology", "biotech", "astronomy"
        ],
        1: [
            "online", "network", "networks", "system", "systems"
        ]
    }
}

def classify(title, description):
    text = (title + " " + description).lower()
    tokens = set(re.split(r'\W+', text))
    
    scores = {cat: 0 for cat in keywords}
    
    for cat, weight_dict in keywords.items():
        for weight, words in weight_dict.items():
            for word in words:
                if word in tokens:
                    scores[cat] += weight
                    
    # Heuristics:
    # If "oil" is present, it's strongly Business unless "spill" (Env/World) or "cooking" (Lifestyle).
    # But for AG News, Oil is Business.
    # If "iraq" is present, it's strongly World.
    
    if sum(scores.values()) == 0:
        return "Unknown"
        
    return max(scores, key=scores.get)

sports_candidates = []
counts = {cat: 0 for cat in keywords}
counts["Unknown"] = 0

for article in articles:
    cat = classify(article['title'], article['description'])
    counts[cat] += 1
    if cat == "Sports":
        sports_candidates.append({
            "title": article['title'],
            "desc": article['description'],
            "len": len(article['description'])
        })

sports_candidates.sort(key=lambda x: x['len'], reverse=True)

result = {
    "counts": counts,
    "top_sports": sports_candidates[:3] if sports_candidates else []
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-14006709642830065521': [{'_id': '69447c785b7637ecc90b9d05', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447c785b7637ecc90b9d06', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447c785b7637ecc90b9d07', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447c785b7637ecc90b9d08', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447c785b7637ecc90b9d09', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14006709642830061862': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_function-call-13273772338279766106': [{'_id': '69447c785b7637ecc90b9d05', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447c785b7637ecc90b9d06', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447c785b7637ecc90b9d07', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447c785b7637ecc90b9d08', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447c785b7637ecc90b9d09', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11371123564863916700': [{'_id': '69447c785b7637ecc90b9d05', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447c785b7637ecc90b9d06', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447c785b7637ecc90b9d07', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447c785b7637ecc90b9d08', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447c785b7637ecc90b9d09', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7183472748245529967': 'file_storage/function-call-7183472748245529967.json', 'var_function-call-9596134104357642270': 'Pretty Log4J', 'var_function-call-1112962506276459453': None, 'var_function-call-29683656630397164': [{'_id': '69447c785b7637ecc90b9d05', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447c785b7637ecc90b9d06', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447c785b7637ecc90b9d07', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447c785b7637ecc90b9d08', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447c785b7637ecc90b9d09', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-10228615712224783799': 'file_storage/function-call-10228615712224783799.json', 'var_function-call-14774662353111638022': None, 'var_function-call-6919485285260926270': {'counts': {'Sports': 0, 'Business': 0, 'World': 0, 'Sci/Tech': 0, 'Unknown': 120000}, 'top_sports': [], 'sample_unknown': ['Wall St. Bears Claw Back Into the Black (Reuters)', 'Carlyle Looks Toward Commercial Aerospace (Reuters)', "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'Oil prices soar to all-time record, posing new menace to US economy (AFP)']}, 'var_function-call-10600307482996590419': {'counts': {'Sports': 31279, 'Business': 27742, 'World': 41074, 'Sci/Tech': 11685, 'Unknown': 8220}, 'top_sports': [{'title': '2004 US Senate Outlook', 'desc': "With all the hoopla over Bush and Kerry, some of you may not have been paying close attention to the other races going on in this loaded US political season. I've read a good dozen or so Senate outlooks, and my blurry eyes and spinning brain kept getting lost in all the numbers and losing track of who, ultimately, was likely to control the Senate on November third. So I made my very own Senate outlook to figure it out (or add further confusion, depending on what you think of my predictions). The bad news is, we probably won't know who controls the Senate on November third. The good news, if you're a Democrat (or a person who loves one), is that my best guess at this point is that when the dust settles, Democrats will probably be in control by the very slimmest possible margin. Shock! But everyone knows the Dems have no chance of taking either house of Congress. I think everyone hasn't been paying attention. Read on for my rundown.", 'len': 944}, {'title': "Biotech's 5 Baggers", 'desc': 'How can yesterday\'s biotech winners lead you to today\'s top performers?" /&gt;  &lt;meta name="keywords" content="charly travers rule breakers biotech eln elan imclone imcl sepracor sepr" /&gt;  &lt;meta name="tickers" content="NASDAQ-BIIB; NASDAQ-IMCL; NASDAQ-SEPR; NYSE-ELN; NYSE-WYE; NYSE-BMY; BIIB; IMCL; SEPR; ELN; WYE; BMY" /&gt;  &lt;meta name="summary" content="" /&gt;  &lt;meta name="author" content="Charly Travers" /&gt;  &lt;meta name="date" content="2004-10-18T12:21-04:00" /&gt;  &lt;meta name="language" content="en-us" /&gt;  &lt;meta name="STORY_UID" content="/USMF_Content/datasource/commentary/centerized/2004/__Commentary10182004ct.xml" /&gt;  &lt;meta name="expiration" content="Date  12 months" /&gt;  &lt;meta name="articletype" content="Investing"/&gt;  &lt;meta name="contenttype" content="a" /&gt;  &lt;title&gt;Fool.com: Biotech\'s 5 Baggers Commentary October 18, 2004&lt;/title&gt;  &lt;script language="JavaScript', 'len': 943}, {'title': "Finding the Best Programmer's Font", 'desc': 'Becoming frustrated with source code not aligning in my favorite source editor I decided to hunt  for the best font. In particular, I began to hunt down the available fixed-width or monospaced fonts.    What are monospaced fonts you ask? From Xerox:Monospace fonts (Such as Courier or LetterGothic), or "fixed pitch" fonts, contain characters that all have the same character width, producing text that can be used to create forms, tabular material or documents that require exact text line lengths. An example of a fixed pitch font is Courier 12 pitch, which is a 10 point font that will print at exactly 12 characters per inch.    Why use  monospaced fonts? Primarily because the text will align more readily. Especially is areas like the comment block header. Updated versions of this document will be located at http://www.lowing.org/fonts/', 'len': 844}]}}

exec(code, env_args)
