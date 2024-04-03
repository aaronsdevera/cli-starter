from clistarter.const import DEFAULT_USER_AGENT

import requests

class CLIStarter:
    """CLIStarter base class"""
    user_agent: str = DEFAULT_USER_AGENT

    socks5: str = None

    session: requests.Session = None

    def __init__(self, socks5: str = None, user_agent: str = None):
        if socks5:
            self.socks5 = socks5
        if user_agent:
            self.user_agent = user_agent
        pass
    
    def set_socks(self, socks5: str = None):
        if socks5:
           self.socks5 = socks5 

    def set_user_agent(self, user_agent: str = None):
        if user_agent:
            self.user_agent = user_agent 

    def create_session(self, socks5: str = None, user_agent: str = None):
        self.session = requests.Session()
        if not user_agent:
            self.session.headers.update({
                'User-Agent': self.user_agent
            })
        else:
            self.session.headers.update({
                'User-Agent': user_agent
            })

        if socks5 or self.socks5:
            self.socks5 = socks5
            self.session.proxies ={
                'http': f'socks5h://{self.socks5}',
                'https': f'socks5h://{self.socks5}'
            }
