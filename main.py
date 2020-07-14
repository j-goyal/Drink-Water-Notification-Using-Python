import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Sir Drink Water Please !",
            message = "You should drink water now. Its very important for you. So kindly stop doing everything for a minute and drink a glass of water.",
            app_icon = "drink.ico",
            timeout = 6 
        )
        time.sleep(3600)


# to run in task manager use ------> pythonw main.py