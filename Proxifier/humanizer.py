from selenium.webdriver.common.keys import Keys
from twocaptchaapi import TwoCaptchaApi
from PIL import Image
import StringIO
import random
import time
import os


def human_type(string_chain, DOM):
    for c in list(string_chain):
        r = random.uniform(0.15, 0.415)
        time.sleep(r)
        DOM.send_keys(c)
    DOM.send_keys(Keys.RETURN)


def human_wait():
    r = random.uniform(1.2, 2.0)
    time.sleep(r)


def solve_captcha(driver, DOM):
    # Downloads image of
    rect = DOM.rect
    points = [rect['x'], rect['y'], rect['x'] + rect['width'], rect['y'] + rect['height']]
    with Image.open(StringIO.StringIO(driver.get_screenshot_as_png())) as img:
        with img.crop(points) as imgsub:
            imgsub.save("Proxifier/image.jpeg", 'jpeg')

    captcher = TwoCaptchaApi("133e845b9084b4db3dc5e0e18a0f98ed")
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'image.jpeg')
    with open(path, 'rw') as captcha_file:
        captcha = captcher.solve(captcha_file)
    # os.remove(captcha_file)

    return captcha.await_result()
