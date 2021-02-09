import pyautogui as pt
from time import sleep
import random
import pyperclip

sleep(5)

position1 = pt.locateOnScreen("smilie.png", confidence=0.6)
# confidence level makes sure that any image which looks 60% lookalike like image mentioned it shoukd work
x = position1[0]
y = position1[1]

# gets message


def get_message():
    global x, y

    position = pt.locateOnScreen("smilie.png", confidence=0.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y)
    pt.moveTo(x + 70, y - 55)
    pt.tripleClick()
    pt.rightClick()
    sleep(2)
    pt.moveTo(527, 750)
    pt.moveRel(12, 15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("Message Recieved: " + whatsapp_message)

    return whatsapp_message
# Posts


def post_response(message):
    global x, y

    position = pt.locateOnScreen("smilie.png", confidence=0.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x+200, y+20)
    pt.click()
    pt.typewrite(message, interval=0.1)

    pt.typewrite("\n", interval=0.1)
    # enter is clicked hence copied msg is sent

# processes response


def process_response(message):
    random_no = random.randrange(3)

    if "?" in str(message).lower():
        return "Don't ask me any questions!"
    else:
        if random_no == 0:
            return "That's cool!"
        elif random_no == 1:
            return "Yayy!"
        else:
            return"i want to eat something"

# check for new messages


def check_for_new_msgs():
    pt.moveTo(x+50, y-55)

    while True:
        # continuously checks for green dots and new messages
        try:
            position = pt.locateOnScreen("greendot.png", confidence=0.7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                sleep(0.5)

        except Exception:
            print("No new other users with new messages located")
        # checks for white
        if pt.pixelMatchesColor(int(x+50), int(y-55), (255, 255, 255), tolerance=10):
            # tolerance is given in case the value is +-10
            print("is white")
            processed_msg = process_response(get_message())
            post_response(processed_msg)
        else:
            print("No new messages yet...")
        sleep(5)


check_for_new_msgs()
