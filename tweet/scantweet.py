
from twython import TwythonStreamer
C_K = "my_key"
C_SK = "secret key"
A_K = "access token"
A_SK = "secret access token"
class MyStreamer(TwythonStreamer):
    def on_success(self,data):
        if 'text' in data:
            print("Got it..")


stream =MyStreamer(C_K,C_SK,A_K,A_SK)
stream.statuses.filter(track="iot")

