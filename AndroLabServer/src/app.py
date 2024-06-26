import getopt
import sys
import logging
from functools import wraps
from flask import Flask, request, request_started
import json
from models import User, Account
from database import db_session
from waitress import serve

makejson = json.dumps
app = Flask(__name__)
makejson = json.dumps

DEFAULT_PORT_NO = 8888

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def usageguide():
    logger.info("InsecureBankv2 Backend-Server")
    logger.info("Options: ")
    logger.info("  --port p     serve on port p (default 8888)")
    logger.info("  --help       print this message")
    logger.info("  --log        enable logging messages")

@app.errorhandler(500)
def internal_servererror(error):
    logger.error(" [!]", error)
    return "Internal Server Error", 500

@app.route('/login', methods=['POST'])
def login():
    Responsemsg = "fail"
    user = request.form['username']
    u = User.query.filter(User.username == request.form["username"]).first()
    logger.info("u=%s", u)
    if u and u.password == request.form["password"]:
        Responsemsg = "Correct Credentials"
    elif u and u.password != request.form["password"]:
        Responsemsg = "Wrong Password"
    elif not u:
        Responsemsg = "User Does not Exist"
    else:
        Responsemsg = "Some Error"
    data = {"message": Responsemsg, "user": user}
    logger.info(makejson(data))
    return makejson(data)

@app.route('/getaccounts', methods=['POST'])
def getaccounts():
    Responsemsg = "fail"
    acc1 = acc2 = from_acc = to_acc = 0
    user = request.form['username']
    u = User.query.filter(User.username == user).first()
    if not u or u.password != request.form["password"]:
        Responsemsg = "Wrong Credentials so trx fail"
    else:
        Responsemsg = "Correct Credentials so get accounts will continue"
        a = Account.query.filter(Account.user == user)
        for i in a:
            if i.type == 'from':
                from_acc = i.account_number
        for j in a:
            if i.type == 'to':
                to_acc = i.account_number
    data = {"message": Responsemsg, "from": from_acc, "to": to_acc}
    logger.info(makejson(data))
    return makejson(data)

@app.route('/changepassword', methods=['POST'])
def changepassword():
    Responsemsg = "fail"
    newpassword = request.form['newpassword']
    user = request.form['username']
    logger.info(newpassword)
    u = User.query.filter(User.username == user).first()
    if not u:
        Responsemsg = "Error"
    else:
        Responsemsg = "Change Password Successful"
        u.password = newpassword
        db_session.commit()
    data = {"message": Responsemsg}
    logger.info(makejson(data))
    return makejson(data)

@app.route('/dotransfer', methods=['POST'])
def dotransfer():
    Responsemsg = "fail"
    user = request.form['username']
    amount = request.form['amount']
    u = User.query.filter(User.username == user).first()
    if not u or u.password != request.form["password"]:
        Responsemsg = "Wrong Credentials so trx fail"
    else:
        Responsemsg = "Success"
        from_acc = request.form["from_acc"]
        to_acc = request.form["to_acc"]
        amount = request.form["amount"]
        from_account = Account.query.filter(Account.account_number == from_acc).first()
        to_account = Account.query.filter(Account.account_number == to_acc).first()
        to_account.balance += int(request.form['amount'])
        from_account.balance -= int(request.form['amount'])
        db_session.commit()
    data = {"message": Responsemsg, "from": from_acc, "to": to_acc, "amount": amount}
    logger.info(makejson(data))
    return makejson(data)

@app.route('/devlogin', methods=['POST'])
def devlogin():
    user = request.form['username']
    Responsemsg = "Correct Credentials"
    data = {"message": Responsemsg, "user": user}
    logger.info(makejson(data))
    return makejson(data)

if __name__ == '__main__':
    port = DEFAULT_PORT_NO
    enable_logging = False

    options, args = getopt.getopt(sys.argv[1:], "", ["help", "port=", "log"])
    for op, arg1 in options:
        if op == "--help":
            usageguide()
            sys.exit(2)
        elif op == "--port":
            port = int(arg1)
        elif op == "--log":
            enable_logging = True

    if enable_logging:
        logging.basicConfig(level=logging.INFO)

    logger.info("The server is hosted on port: %s", port)

    try:
        serve(app, host='0.0.0.0', port=port)
    except Exception as e:
        logger.exception("An error occurred while running the server: %s", str(e))
