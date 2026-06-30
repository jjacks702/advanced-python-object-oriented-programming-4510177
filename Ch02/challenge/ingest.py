# %% Events
class LoginEvent:
    def __init__(self, login):
        self.login = login

    def notify_loaded(self):
        print('LoginEvent loaded')


class AccessEvent:
    def __init__(self, login, uri):
        self.login = login
        self.uri = uri

    def notify_loaded(self):
        print(f'AccessEvent loaded (uri={self.uri!r})')


# Add an ability to load events from JSON data (str)
# Use a Mixin class
# Make sure that Events have notify_loaded method (ABC)
from abc import ABC, abstractMethod
import json
    
    class Serialized(ABC):
        @classmethod
        def from_json(cls,data)
        params = json.loads(data)
        inst = cls(**params)
        inst.notify_loaded()
        return inst
        
    @classmethod
    def notify_loaded(self):
        pass
#MIXIN
class serialAccess(AccessEvent,Serialized)

class serialLogin(LoginEvent,Serialized)
# %% Test
# LoginEvent
login_data = '{"login": "elliot"}'
# AccessEvent
access_data = '''
{
  "login": "elliot",
  "uri": "file:///etc/passwd"
}
'''
