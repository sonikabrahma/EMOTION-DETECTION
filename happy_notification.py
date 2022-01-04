from plyer import notification
import time
def notice():
    notification.notify(
        title = "Healthy reminder",
        message = "Good to see you healthy!!! Enjoy your day xD",
        timeout=15,
    )
notice()
activate=True