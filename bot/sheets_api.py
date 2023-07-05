from credentials.config import CRED_FILE, SCOPES, SHEET_ID
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Initializing credentials information needed for initialization
cred, _ = google.auth.load_credentials_from_file(CRED_FILE, scopes=SCOPES)
service = build('sheets',
                'v4',
                credentials=cred
                )  # Creates connection


class SheetApi:

    # Adding new users to table
    def get_data(self):
        return service.spreadsheets().values().get(
            spreadsheetId=SHEET_ID,
            range="Users"
        ).execute()

    def get_balance(self, idd):
        result = self.get_data()
        for i in result['values']:  # Searching for balance of specific user
            if i[0] == idd:
                balance = i[1].replace(',', '.')  # For convertation to float

                return balance

    def creat_new_user(self, idd):
        try:
            # Getting data from Google sheets
            result = self.get_data()

        except HttpError:
            print("An error occurred")  # Should be tg bot message to owner

        for i in result['values']:  # Searching for balance of specific user
            if i[0] == idd:
                return 'user already exist'
        else:
            # Adding new users to database
            service.spreadsheets().values().append(
                spreadsheetId=SHEET_ID,
                range="Users",
                valueInputOption="USER_ENTERED",
                body={'values': [[idd, '0']]}
            ).execute()

    # Withdraw certain amount of money from user balance
    def chek_out(self, idd, amount):
        try:
            # Getting data from Google sheets
            result = self.get_data()
        except HttpError:
            print("An error occurred")  # Should be tg bot message to owner
        for i in result['values']:  # Searching for balance of specific user
            if i[0] == idd:
                balance = i[1].replace(',', '.')  # For convertation to float
                if float(balance) < amount:
                    return 0  # Return 0 if balance lower then withdraw
                else:
                    # Otherwise charging money from balance and write new balance
                    ind = result['values'].index(i) + 1

                    # Try to write balance after withdraw
                    try:
                        service.spreadsheets().values().update(
                            spreadsheetId=SHEET_ID,
                            range=f"Users!B{ind}",
                            valueInputOption="USER_ENTERED",
                            body={'values': [[str(float(balance) - amount).replace('.', ',')]]}
                        ).execute()
                    except HttpError:
                        print("An error occurred")  # Should be tg bot message to owner

                    return 1  # Return 1 if successful
        else:
            return 'No such user'  # Message to bot owner
