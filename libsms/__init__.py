import libsms.backends.sms.SmsTransport as sms
import libsms.backends.dummy.SmsTransport as dummy
import libsms.backends.other.SmsTransport as other

sms_transports = {"default": sms.sms_transport, "dummy" : dummy.sms_transport, "other" : other.sms_transport}
sms_transport = sms.sms_transport