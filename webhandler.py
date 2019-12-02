"""Collection of DTOs and class for interacting with the service"""
import gzip
import http.client
import json

SERVER_URL = "devrecruitmentchallenge.com"
API_KEY = "61037bc2-d0d0-4d23-afcb-d0dc2af0d922"

class ChallengeInfo(object):
    """Information regarding a challenge"""
    def __init__(self, cid, challenge_type, name, description):
        self.cid = cid
        self.challenge_type = challenge_type.lower()
        self.name = name
        self.description = description

class Question(object):
    """A single question"""
    def __init__(self, tid, question):
        self.tid = tid
        self.question = question

class Challenge(object):
    """A Challenge definition"""
    def __init__(self, info, questions):
        self.info = info
        self.questions = questions

class ChallengeResult(object):
    """Response from a challenge submission"""
    def __init__(self, submission_id, mark):
        self.submission_id = submission_id
        self.mark = mark

def get_challenge_list():
    """Get the list of challenges"""
    data = get_json("/api/challenges/")
    return [ChallengeInfo(k["id"], k["challengeType"], k["name"], k["description"])
            for k in data["challenges"]]

def get_challenge(cid):
    """Get the details of a specific challenge"""
    data = get_json("/api/challenges/{}".format(cid))
    info_json = data["challenge"]
    info = ChallengeInfo(info_json["id"], info_json["challengeType"], ["name"], 
                         info_json["description"])
    questions = [Question(k["id"], k["question"]) for k in data["questions"]]
    return Challenge(info, questions)

def post_standard_submission(submission):
    """Post a standard challenge submission and return the result"""
    j = json.dumps(submission)
    data = post_json("/api/submissions/standard", j)
    return ChallengeResult(data["submissionId"], data["mark"])

def get_json(url):
    """Return json result of GET"""
    connection = http.client.HTTPConnection(SERVER_URL)
    headers = {
        "Authorization": "ApiKey {}".format(API_KEY),
        "Accept-encoding": "gzip"
    }
    connection.request("GET", url, headers=headers)
    response = connection.getresponse()
    raw_content = response.read()
    if response.getheader("Content-encoding") == "gzip":
        content = gzip.decompress(raw_content).decode()
    else:
        content = raw_content.decode()
    print("GET {} {} ({} bytes)".format(response.status, url, len(raw_content)))
    #print(content)
    if response.status != 200:
        print(content)
        raise ValueError("GET of {} was not successful".format(url))
    return json.loads(content)

def post_json(url, j):
    """Return json result of a POST"""
    connection = http.client.HTTPConnection(SERVER_URL)
    headers = {"Authorization": "ApiKey {}".format(API_KEY), "Content-type": "application/json"}
    connection.request("POST", url, j, headers=headers)
    response = connection.getresponse()
    content = response.read().decode()
    print("POST {} {} ({} bytes)".format(response.status, url, len(content)))
    #print(content)
    if response.status != 200:
        print(content)
        raise ValueError("POST to {} was not successful. Sent JSON '{}'".format(url, j))
    return json.loads(content)