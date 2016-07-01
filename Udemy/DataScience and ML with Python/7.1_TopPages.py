import re

#regex to parse the log line

format_pat= re.compile(
    r"(?P<host>[\d\.]+)\s"
    r"(?P<identity>\S*)\s"
    r"(?P<user>\S*)\s"
    r"\[(?P<time>.*?)\]\s"
    r'"(?P<request>.*?)"\s'
    r"(?P<status>\d+)\s"
    r"(?P<bytes>\S*)\s"
    r'"(?P<referer>.*?)"\s'
    r'"(?P<user_agent>.*?)"\s*'
)

logPath = "./Documents/Udemy_Datascience/Datascience/access_log.txt"

#Extract URL in each access and use a dictionary to count up number of times each url appears
# The below code snippet throws an error. Request part of url should have HTTO action, URL and the Protocol. Seems some of the entries doesnt have it
#URLCounts = {}

#with open(logPath, "r") as f:
    #for line in (l.rstrip() for l in f):
#        match= format_pat.match(line)
#        if match:
#            access = match.groupdict()
#            request = access['request']
#            (action, URL, protocol) = request.split()
#            if URLCounts.has_key(URL):
#                URLCounts[URL] = URLCounts[URL] + 1
#            else:
#                URLCounts[URL] = 1

#results = sorted(URLCounts, key=lambda i: int(URLCounts[i]), reverse=True)

#for result in results[:20]:
#    print result + ": " + str(URLCounts[result])


#Identify the user agents, we can see some of them are blank
UserAgents = {}

with open(logPath, "r") as f:
    for line in (l.rstrip() for l in f):
        match= format_pat.match(line)
        if match:
            access = match.groupdict()
            agent = access['user_agent']
            if UserAgents.has_key(agent):
                UserAgents[agent] = UserAgents[agent] + 1
            else:
                UserAgents[agent] = 1

results = sorted(UserAgents, key=lambda i: int(UserAgents[i]), reverse=True)

for result in results:
    print result + ": " + str(UserAgents[result])
#Print out requests that doesnt contain all three parts and modify the script
#filter only GET requests
#filter out web robots
#filter out URL that doesnt end in /
URLCounts = {}

with open(logPath, "r") as f:
    for line in (l.rstrip() for l in f):
        match= format_pat.match(line)
        if match:
            access = match.groupdict()
            agent = access['user_agent']
            if (not('bot' in agent or 'spider' in agent or 
                    'Bot' in agent or 'Spider' in agent or
                    'W3 Total Cache' in agent or agent =='-')):
                request = access['request']
                fields = request.split()
                if (len(fields) == 3):
                    (action, URL, protocol) = fields
                    if (URL.endswith("/")):
                        if (action == 'GET'):
                            if URLCounts.has_key(URL):
                                URLCounts[URL] = URLCounts[URL] + 1
                            else:
                                URLCounts[URL] = 1
results = sorted(URLCounts, key=lambda i: int(URLCounts[i]), reverse=True)

for result in results[:20]:
    print result + ": " + str(URLCounts[result])