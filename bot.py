import json
from engine import msgAI


def makeEmailList():

    with open('sendTo.json') as file:
        emailList = json.load(file)

    return emailList


def sendEmail(email):
    pass



def main():

    emailList = makeEmailList()
    baseMsg = ""

    # No of mails to...
    print("The number of mails you are sending this to are: ", len(emailList))

    # main engine

    for i in emailList:
        msg = msgAI(baseMsg, i)
        sendEmail(msg)



if __name__ == "__main__":
    main()