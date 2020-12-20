from selenium import webdriver
from time import sleep
import random
'''self.driver.find_element_by_xpath(
            """"""
        )
'''


class mybot:
    def __init__(self):
        self.driver = webdriver.Chrome("C:\webdrivers\chromedriver")
        self.driver.get("https://www.instagram.com/")

    def login(self, username, password):
        while True:
            try:
                self.driver.find_element_by_xpath(
                    """//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input"""
                ).send_keys(username)
                self.driver.find_element_by_xpath(
                    """//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input"""
                ).send_keys(password)
                self.driver.find_element_by_xpath("""
                //*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]""").click()
                break
            except:
                pass

    # def show_notifications(self):
    #     try:
    #         sleep(5)
    #         self.driver.find_element_by_xpath(
    #             "//button[contains(text(), 'Not Now')]").click()
    #     except:
    #         pass

    def get_followers_page(self):
        sleep(5)
        try:
            self.driver.get(
                """https://www.instagram.com/explore/people/suggested/""")
        except:
            pass
        sleep(5)
    def following_adding(self):
        print("Im following_adding")
        while True:
            list_of_buttons = self.driver.find_elements_by_class_name(
                "y3zKF")
            for buttons in list_of_buttons:              
                try:
                    buttons.click()
                    random_time = random.randint(1000, 3000)/1000
                    sleep(random_time)
                except:
                    pass

            sleep(5)


if __name__ == "__main__":
    bot = mybot()
    bot.login("username", "password")
    bot.get_followers_page()
    bot.following_adding()
