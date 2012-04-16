import xmpp
import pycurl
import StringIO
import re
import sqlite3

jabberid = '<xmpp/jabber ID>'
password = '<xmpp/jabber password'
registerurl = "<Register URL>"
cbfurl = "<Responder URL>"

jid = xmpp.JID(jabberid)
conn = xmpp.Client(jid.getDomain(),debug=[])
conres = conn.connect()
authres = conn.auth(jid.getNode(),password)

def messagehandler(conn,mess):
    print mess.getBody()
    if str(mess.getBody()) == 'None':
        return
    localdb = sqlite3.connect('./refutdcli.db')
    cursor = localdb.cursor()
    cursor.execute('''SELECT serverid FROM registrations WHERE userid = ?''',(str(mess.getFrom()),))
    rows = cursor.fetchall()
    if len(rows) == 0:
        splitstring = str(mess.getBody()).split(' ',1)
        if splitstring[0].lower() == 'register':
            c = pycurl.Curl()
            c.setopt(pycurl.URL, registerurl)
            c.setopt(pycurl.POST, 1)
            c.setopt(pycurl.POSTFIELDS, "confirmcode=%s" % splitstring[1])
            b = StringIO.StringIO()
            c.setopt(pycurl.WRITEFUNCTION, b.write)
            c.perform()
            c.close()
            data = b.getvalue()
            if not re.match('[0-9]*',data):
                conn.send(xmpp.Message(mess.getFrom(),data))
            else:
                cursor.execute('''INSERT INTO registrations (userid,serverid) VALUES (?,?)''',(str(mess.getFrom()),data))
                conn.send(xmpp.Message(mess.getFrom(),'You are now registered.'))
        else:
            conn.send(xmpp.Message(mess.getFrom(),"Sorry, you're not registered for this system."))
            conn.send(xmpp.Message(mess.getFrom(),"Please visit {0} to register.".format(registerurl)))
    else:
        c = pycurl.Curl()
        c.setopt(pycurl.URL, cbfurl)
        c.setopt(pycurl.POST, 1)
        c.setopt(pycurl.POSTFIELDS, "message={0}&userid={1}".format(str(mess.getBody()),str(rows[0][0])))
        b = StringIO.StringIO()
        c.setopt(pycurl.WRITEFUNCTION, b.write)
        c.perform()
        c.close()
        data = b.getvalue()
        conn.send(xmpp.Message(mess.getFrom(),data))
    localdb.commit()
    cursor.close()

def StepOn(conn):
    try:
        conn.Process(1)
    except KeyboardInterrupt: return 0
    return 1


def GoOn(conn):
    while StepOn(conn): pass


conn.RegisterHandler('message',messagehandler)
conn.sendInitPresence()
GoOn(conn)