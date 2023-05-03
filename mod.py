import requests

class StartingNewProjet:
    def __init__(self, querystring, payload):
        """
        :param querystring:
                -EX: {"key":"{API_Key}"}
        :param payload:
                _EX:{'competitors': ['google.com', 'ebay.com'],
                    'keywords': [{'keyword': 'search tool', 'tags': ['search']},
                                 {'keyword': 'search engine', 'tags': ['search']}],
                    'project_name': 'ProjectAPI',
                    'url': 'amazon.com'}
        """
        self.url = "https://api.semrush.com/management/v1/projects"
        self.querystring = querystring
        self.payload = payload
        self.headers = {'content-type': "application/json", 'cache-control': "no-cache"}

    def run(self):
        return {'------>  StartingNewProjet output  <-----': "capsssssssss"}
        # return requests.request('POST', self.url, data=self.payload, headers=self.headers, params=self.querystring)
        # Recuperer l'id_project #TODO


class ActiverAudit:
    def __init__(self, querystring, payload, id_projet):
        """
        :param querystring:
                -EX: {"key":"{API_Key}"}
        :param payload:
                -EX: {'device': 'desktop',
                      'domain': 'amazon.com',
                      'notify': False,
                      'pageLimit': 1000,
                      'scheduleDay': 0,
                      'userAgentType': 1}
        :param id_projet:
                -EX: "XXXXXXXXXXXXXXXXXXX"
        """
        self.url = f"https://api.semrush.com/management/v1/projects/{id_projet}/siteaudit/enable"
        self.querystring = querystring
        self.payload = payload
        self.headers = {'content-type': "application/json", 'cache-control': "no-cache"}

    def run(self):
        return {'------>  ActiverAudit output  <-----': "capsssssssss"}
        # return requests.request('POST', self.url, data=self.payload, headers=self.headers, params=self.querystring)


class ExecuterAudit:
    def __init__(self, querystring, id_projet):
        """
        :param querystring:
                -EX: {"key":"{API_Key}"}
        :param id_projet:
                -EX: "XXXXXXXXXXXXXXXXXXX"
        """
        self.url = f"https://api.semrush.com/reports/v1/projects/{id_projet}/siteaudit/launch"
        self.querystring = querystring
        self.headers = {'content-type': "application/json", 'cache-control': "no-cache"}

    def run(self):
        return {'------>  ExecuterAudit output  <-----': "capsssssssss"}
        # return requests.request('POST', self.url, headers=self.headers, params=self.querystring)


class ObtenirRapport:
    def __init__(self, querystring, id_projet):
        """
        :param querystring:
                -EX: {"key":"{API_Key}"}
        :param id_projet:
                -EX: "XXXXXXXXXXXXXXXXXXX"
        """
        self.url = f"https://api.semrush.com/reports/v1/projects/{id_projet}/siteaudit/info"
        self.querystring = querystring
        self.headers = {'cache-control': "no-cache"}

    def run(self):
        return {'------>  ObtenirRapport output  <-----': "capsssssssss"}
        # return requests.request('POST', self.url, headers=self.headers, params=self.querystring)



if __name__ == '__main__':
    pass