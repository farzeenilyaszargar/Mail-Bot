import os
import base64
from email.message import EmailMessage
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

SCOPES = ["https://www.googleapis.com/auth/gmail.send"]


def get_service():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("gmail", "v1", credentials=creds)
    return service


def gmail_send_message(to, subject, body):
    service = get_service()

    message = EmailMessage()
    message.set_content(body)
    message["To"] = to
    message["Subject"] = subject

    encoded_message = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    create_message = {"raw": encoded_message}

    send_message = (
        service.users()
        .messages()
        .send(userId="me", body=create_message)
        .execute()
    )

    print("Message Id:", send_message["id"])


if __name__ == "__main__":
    gmail_send_message(
        "test@example.com",
        "Automated Email",
        "This is an automated message."
    )
