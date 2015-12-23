from libsms import sms_transport
from libsms import sms_transports

if __name__ == "__main__":
    sms_transport.send( phone="123123", msg="qweqwe")
    sms_transports["dummy"].send( phone="123123", msg="qweqwe")

