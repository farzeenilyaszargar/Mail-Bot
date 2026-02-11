import json
from engine import msgAI
from sendMail import gmail_send_message


def makeEmailList():

    with open('sendTo.json') as file:
        emailList = json.load(file)

    return emailList

def sendMail(receiver, subject, msg):
    gmail_send_message(receiver, subject, msg)

def main():

    emailList = makeEmailList()
    subject = "Nap Editor | The Next Big Update"
    coreMsg = "I have made Nap IDE, which is just like cursor. Market it to the indivuduals properly using any method you know "
    user = "Farzeen"

    # No of mails to...
    print("The number of mails you are sending this to are: ", len(emailList))

    # main engine

    for i in emailList:
        msg = msgAI(coreMsg, i, user)
        sendMail(i, subject, msg)



if __name__ == "__main__":
    main()