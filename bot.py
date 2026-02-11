import json
from engine import msgAI
from sendMail import sendMail


def makeEmailList():

    with open('sendTo.json') as file:
        emailList = json.load(file)

    return emailList



def main():

    emailList = makeEmailList()
    subject = ""
    baseMsg = ""
    attachments = []

    # No of mails to...
    print("The number of mails you are sending this to are: ", len(emailList))

    # main engine

    for i in emailList:
        msg = msgAI(baseMsg, i)
        sendMail(i, subject, msg)



if __name__ == "__main__":
    main()