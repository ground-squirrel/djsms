import libsms.backends.sms.SmsTransport as sms
import libsms.backends.dummy.SmsTransport as dummy
import libsms.backends.other.SmsTransport as other

sms_transports = {"default": sms.smsTransport, "dummy" : dummy.smsTransport, "other" : other.smsTransport}
sms_transport = sms.smsTransport