import json
from engine import msgAI
from sendMail import sendMail


def makeEmailList():

    with open('sendTo.json') as file:
        emailList = json.load(file)

    return emailList


def sendEmail(email, recieverMail):
    sendMail(recieverMail)
    # send generated email to the user via api  


def main():

    emailList = makeEmailList()
    baseMsg = ""
    attachments = []

    # No of mails to...
    print("The number of mails you are sending this to are: ", len(emailList))

    # main engine

    for i in emailList:
        msg = msgAI(baseMsg, i)
        sendEmail(msg, i)



if __name__ == "__main__":
    main()