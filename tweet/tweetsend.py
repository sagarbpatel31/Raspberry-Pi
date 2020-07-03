from twython import Twython
C_K = "my key"
C_SK = "my secret key"
A_K = "Token key"
A_SK = "Secret Token key"
api = Twython(C_K,C_SK,A_K,A_SK)
api.update_status(status="Any message")
