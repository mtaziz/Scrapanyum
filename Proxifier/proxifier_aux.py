# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.support.ui import Select
from dateutil.relativedelta import relativedelta
from distutils.dir_util import copy_tree
from datetime import datetime
from selenium import webdriver
from .models import *
import humanizer
import string
import random
import pickle
import os


class Selenium:
    # def __init__(self, account_id):
    def create_browser(self, account_id):
        self.account = ProxifierAccount.objects.get(id=account_id)
        account = self.account

        final_profile = 'Proxifier\default_profile'
        # account.profile_file = final_profile
        profile = FirefoxProfile(final_profile)

        # For linux
        # default_profile = 'Proxifier/profiles/DEFAULT'
        # For windows
        # default_profile = 'Proxifier\default_profile'

        # final_profile = id_generator()
        # shutil.copy(os.path.join(default_profile), os.path.join('Proxifier/profiles/', final_profile))
        # copy_tree(os.path.join(default_profile), os.path.join('Proxifier/profiles/', final_profile))
        # account.profile_file = final_profile

        # Create profile if it doesn't exist
        # if account.profile_file == "":
        #     profile = FirefoxProfile()
        #
        #     # For linux
        #     # default_profile = 'Proxifier/profiles/DEFAULT'
        #     # For windows
        #     default_profile = 'C:\Users\Volk\AppData\Roaming\Mozilla\Firefox\Profiles'
        #
        #
        #     final_profile = id_generator()
        #     # shutil.copy(os.path.join(default_profile), os.path.join('Proxifier/profiles/', final_profile))
        #     copy_tree(os.path.join(default_profile), os.path.join('Proxifier/profiles/', final_profile))
        #     account.profile_file = final_profile
        #     account.save()
        # else:
        #     profile_file = os.path.join('Proxifier/profiles/', account.profile_file)
        #     profile = FirefoxProfile(profile_file)

        # Set download dir
        profile.set_preference("browser.download.folderList", 2)
        profile.set_preference("browser.download.manager.showWhenStarting", False)
        profile.set_preference("browser.download.dir", "/proxifier")
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "image/jpeg")

        # Set user agent
        profile.set_preference("general.useragent.override", account.user_agent)
        print ("User agent: %s" % account.user_agent)

        # Add plugins:
        if account.plugin_list != "":
            for p in account.plugin_list.split(','):
                profile.add_extension(extension="Proxifier/plugins/%s.xpi" % p)

        # --------- #
        # Set proxy
        # proxyHost = "173.232.14.3"
        # proxyPort = "3128"
        # profile.set_preference("network.proxy.type", 1)
        # profile.set_preference('network.proxy.socks', proxyHost)
        # profile.set_preference('network.proxy.socks_port', proxyPort)
        # profile.set_preference('signon.autologin.proxy', True)
        # profile.set_preference('network.websocket.enabled', False)
        # profile.update_preferences()

        # Setting up profile, now raise browser
        # firefox_capabilities = DesiredCapabilities.FIREFOX
        # firefox_capabilities['marionette'] = True
        # firefox_capabilities['binary'] = 'C:' + os.path.sep + 'Program Files' + os.path.sep + 'Mozilla Firefox' + \
        #                                  os.path.sep + 'firefox.exe'

        # self.driver = webdriver.Firefox(firefox_profile=profile, capabilities=firefox_capabilities)
        self.driver = webdriver.Firefox(firefox_profile=profile)
        pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))

        # Set screen size
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(account.screen_width, account.screen_height)
        print "%s x %s" % (account.screen_width, account.screen_height)

        # load cookies
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
            print cookie

        return self.driver

        # url = "http://www.whatsmyip.org/"
        # self.driver.get(url)

    def google_search(self, search_term):
        # Visit page
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.google.es/")

        # Write and search for term
        DOM = self.driver.find_element_by_class_name("gsfi")
        humanizer.human_type(search_term, DOM)

        # Save new cookies
        pickle.dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))

        self.driver.close()


def id_generator(size=24, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_hotmail(self):
    driver = self.driver
    account = self.account
    driver.get("https://signup.live.com")
    try:
        # Use driver, string to send, DOM element
        humanizer.human_wait()
        humanizer.human_type(account.first_name, driver.find_element_by_id("FirstName"))
        humanizer.human_wait()
        humanizer.human_type(account.last_name, driver.find_element_by_id("LastName"))
        humanizer.human_wait()
        humanizer.human_type(account.user_name, driver.find_element_by_id("MemberName"))
        humanizer.human_wait()
        humanizer.human_type(account.password, driver.find_element_by_id("Password"))
        humanizer.human_wait()
        humanizer.human_type(account.password, driver.find_element_by_id("RetypePassword"))
        humanizer.human_wait()

        # TODO: Write humanizer for dropdowns
        Select(driver.find_element_by_id("BirthDay")).select_by_visible_text("10")
        humanizer.human_wait()
        Select(driver.find_element_by_id("BirthMonth")).select_by_visible_text("April")
        humanizer.human_wait()
        Select(driver.find_element_by_id("BirthYear")).select_by_visible_text("1990")
        humanizer.human_wait()
        Select(driver.find_element_by_id("Gender")).select_by_visible_text("Male")
        humanizer.human_wait()

        humanizer.human_type(account.phone, driver.find_element_by_id("PhoneNumber"))
        humanizer.human_wait()
        humanizer.human_type(account.alt_mail, driver.find_element_by_id("iAltEmail"))
        humanizer.human_wait()
    except Exception as e:
        print "Error in user form"

    # Spanish version
    # solved_captcha = humanizer.solve_captcha(driver, u"//img[@alt='Desafío visual']")
    #
    check = False

    while not check:
        try:
            solved_captcha = humanizer.solve_captcha(driver, driver.find_element_by_xpath(
                u"//img[@alt='Visual Challenge']"))
            driver.find_element_by_class_name('spHipNoClear').clear()
            humanizer.human_type(solved_captcha.replace(' ', ''), driver.find_element_by_class_name('spHipNoClear'))

            humanizer.human_wait()
            humanizer.human_wait()
            driver.find_element_by_id("CredentialsAction").click()
            humanizer.human_wait()
            humanizer.human_wait()

            if len(driver.find_elements_by_css_selector('.alert-error')) > 0:
                print "wrong captcha, trying again"
            else:
                check = True

        except Exception as e:
            print e

    humanizer.human_wait()
    humanizer.human_wait()

    driver.close()
