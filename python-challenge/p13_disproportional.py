__author__ = 'julenka'


import xmlrpclib

# create a ServerProxy with an URI that doesn't respond to XMLRPC requests
proxy = xmlrpclib.ServerProxy("http://huge:file@www.pythonchallenge.com/pc/phonebook.php")

def phone(s):
    try:
        print "trying",s
        # I need to figure out which number to call
        resp = proxy.phone(s)

        return resp
    except xmlrpclib.Fault as err:
        print "A fault occurred"
        print "Fault code: %d" % err.faultCode
        print "Fault string: %s" % err.faultString

if __name__ == '__main__':
    print phone("Bert")