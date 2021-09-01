import sys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import selenium
import random
import traceback

from selenium import webdriver

#------------------------------------------------

# options = webdriver.ChromeOptions()
options = webdriver.FirefoxOptions()

################################################################################
#########  Comment the following line if want to run with GUI  #################
################################################################################

options.add_argument("--headless")

profile = webdriver.FirefoxProfile()
profile.accept_untrusted_certs = True

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options, firefox_profile=profile)

# driver = webdriver.Chrome(ChromeDriverManager().install(),  options=chrome_options)

default_target = "https://10.86.226.32"

#------------------------------------------------
# Useage: 
# python canvas_group_scraper.py <target groups page>
#------------------------------------------------

def register(email:str, password:str, displayname:str, questionidx:int, safetyanswer:str):
    print("Redirecting to register page...")
    driver.get(default_target+"/signup")
    print("Inserting credentials...")
    driver.find_element_by_xpath("/html/body/center/form/input[1]").send_keys(email)
    driver.find_element_by_xpath("/html/body/center/form/input[2]").send_keys(password)
    driver.find_element_by_xpath("/html/body/center/form/input[3]").send_keys(password)
    driver.find_element_by_xpath("/html/body/center/form/input[4]").send_keys(displayname)
    driver.find_element_by_xpath("/html/body/center/form/select/option[{}]".format(str(questionidx))).click()
    driver.find_element_by_xpath("/html/body/center/form/input[5]").send_keys(safetyanswer)
    print("Finished inserting credentials ~")
    driver.find_element_by_xpath("/html/body/center/form/input[6]").click()
    print("Finished signup with {} {} ~".format(email, password))

def login(email:str, password:str):
    print("Redirecting to login page...")
    driver.get(default_target+"/login")
    print("Inserting credentials...")
    driver.find_element_by_xpath("/html/body/center/form/input[1]").send_keys(email)
    driver.find_element_by_xpath("/html/body/center/form/input[2]").send_keys(password)
    print("Finished inserting credentials ~")
    driver.find_element_by_xpath("/html/body/center/form/input[3]").click()
    print("Log in successfully as {}!".format(email))

def log_out():
    print("Attempt to log out...")
    driver.get(default_target+"/account")
    driver.find_element_by_xpath("/html/body/div/div[1]/div[4]/a").click()
    print("Logout successfully!")

def virtual_user_1():
    register("FamilyGuy@gmail.com", "familyguysyyds", "FamilyGuy", 2, "andruey")
    login("FamilyGuy@gmail.com", "familyguysyyds")

    # Chat with admin@sydney.edu.au
    print("Redirecting to message page...")
    driver.get(default_target+"/message")
    print("Establishing chat...")
    driver.find_element_by_xpath("/html/body/center/form/input[1]").send_keys("1")
    driver.find_element_by_xpath("/html/body/center/form/input[2]").click()
    print("Inserting message...")
    driver.find_element_by_xpath("/html/body/center/form/textarea").send_keys("hey admin, this is FamilyGuy")
    driver.find_element_by_xpath("/html/body/center/form/input[2]").click()
    print("Message sent!")

    # Submit post
    print("Redirecting to forum page...")
    driver.get(default_target+"/forum")
    driver.find_element_by_xpath("/html/body/div[1]/a/button").click()
    print("Filling the post title...")
    driver.find_element_by_xpath("/html/body/div[1]/center/form/textarea[1]").clear()
    driver.find_element_by_xpath("/html/body/div[1]/center/form/textarea[1]").send_keys("FamilyGuy first post")
    print("Filling the post content...")
    driver.find_element_by_xpath("/html/body/div[1]/center/form/textarea[2]").clear()
    driver.find_element_by_xpath("/html/body/div[1]/center/form/textarea[2]").send_keys("Does anyone dream in code?:)")
    print("Submitting post...")
    driver.find_element_by_xpath("/html/body/div[1]/center/form/input").click()
    print("Post submitted!")

    # view content pages
    print("Viewing course pages...")
    driver.get(default_target+"/course")
    driver.get(default_target+"/js1")
    driver.get(default_target+"/html1")
    driver.get(default_target+"/css1")

def virtual_user_2():
    register("FamilyGuy@gmail.com", "familyguysyyds", "FamilyGuy", 2, "andruey")
    login("admin@sydney.edu.au", "admin")
   
    # view content pages
    print("Viewing course pages...")
    driver.get(default_target+"/course")
    driver.get(default_target+"/js2")
    driver.get(default_target+"/html2")
    driver.get(default_target+"/css2")

    # chat with FamilyGuy@gmail.com
    print("Redirecting to message page...")
    driver.get(default_target+"/message")
    print("Establishing chat...")
    driver.find_element_by_xpath("/html/body/center/form/input[1]").send_keys("3")
    driver.find_element_by_xpath("/html/body/center/form/input[2]").click()
    print("Inserting message...")
    driver.find_element_by_xpath("/html/body/center/form/textarea").clear()
    driver.find_element_by_xpath("/html/body/center/form/textarea").send_keys("hey FamilyGuy, this is admin")
    driver.find_element_by_xpath("/html/body/center/form/input[2]").click()
    print("Message sent!")

    # check post and comment
    print("Redirecting to forum page...")
    driver.get(default_target+"/forum")
    driver.find_element_by_xpath("/html/body/div[1]/p[3]/a/span").click()
    print("Inserting comment...")
    driver.find_element_by_xpath("/html/body/div/form/textarea").clear()
    driver.find_element_by_xpath("/html/body/div/form/textarea").send_keys("That is good point")
    driver.find_element_by_xpath("/html/body/div/form/input").click()
    print("Comment posted!")

    # mute FamilyGuy
    print("Redirecting to account page...")
    try:
        driver.get(default_target+"/account")
        element = driver.find_element_by_xpath("/html/body/div/div[1]/div[5]/a")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

        user_to_mute = "FamilyGuy@gmail.com"
        driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div[1]/form/input[1]").send_keys(user_to_mute)
        driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div[1]/form/input[2]").click()
        print("User {} muted!".format(user_to_mute))

        driver.find_element_by_xpath("/html/body/center/a").click()

        # promote FamilyGuy
        element = driver.find_element_by_xpath("/html/body/div/div[1]/div[5]/a")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        user_to_promote = "FamilyGuy@gmail.com"
        driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div[3]/form/input[1]").send_keys(user_to_promote)
        driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div[3]/form/input[2]").click()
        print("User {} promoted!".format(user_to_promote))

        driver.find_element_by_xpath("/html/body/center/a").click()
        log_out()
        login("FamilyGuy@gmail.com", "familyguysyyds")
        log_out()

        # delete FamilyGuy
        login("admin@sydney.edu.au", "admin")
        print("Redirecting to account page...")
        driver.get(default_target+"/account")

        element = driver.find_element_by_xpath("/html/body/div/div[1]/div[5]/a")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        user_to_delete = "FamilyGuy@gmail.com"
        driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div[4]/form/input[1]").send_keys(user_to_delete)
        driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div[4]/form/input[2]").click()
        print("User {} deleted!".format(user_to_delete))

        driver.find_element_by_xpath("/html/body/center/a").click()
    
    except selenium.common.exceptions.ElementNotInteractableException:
        pass
    log_out()

    login("FamilyGuy@gmail.com", "familyguysyyds")

def virtual_user_3():
    login("bottlecourse@gmail.com", "bottlecourse")
    print("Redirecting to account page...")
    driver.get(default_target+"/account")

    # Change password
    print("Changing password...")
    driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/a").click()
    driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/div[2]/div[1]/div/form/input[1]").send_keys("bottlecourse")
    driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/div[2]/div[1]/div/form/input[2]").send_keys("bottlecourse")
    driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/div[2]/div[1]/div/form/input[3]").click()
    print("Password changed!")
    driver.find_element_by_xpath("/html/body/center/a").click()
    
    # Change safety question
    print("Changing safety question...")

    driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/a").click()
    driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/div[2]/div[2]/div/form/select/option[1]").click()
    driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/div[2]/div[2]/div/form/input[1]").send_keys("Just for Fun")
    driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/div[2]/div[2]/div/form/input[2]").click()
    print("Safety question changed!")
    driver.find_element_by_xpath("/html/body/center/a").click()

    # Change username
    print("Changing username...")
    driver.find_element_by_xpath("/html/body/div/div[1]/div[3]/a").click()

    driver.find_element_by_xpath("/html/body/div/div[3]/div[4]/div[2]/div[1]/div/form/input[1]").send_keys("bottlecourse_reset")
    driver.find_element_by_xpath("/html/body/div/div[3]/div[4]/div[2]/div[1]/div/form/input[2]").click()
    print("Username changed!")

    driver.find_element_by_xpath("/html/body/center/a").click()

    # Change gender
    print("Changing gender...")
    driver.find_element_by_xpath("/html/body/div/div[1]/div[3]/a").click()

    driver.find_element_by_xpath("/html/body/div/div[3]/div[4]/div[2]/div[2]/div/form/select/option[3]").click()
    driver.find_element_by_xpath("/html/body/div/div[3]/div[4]/div[2]/div[2]/div/form/input").click()
    print("Gender changed!")

    driver.find_element_by_xpath("/html/body/center/a").click()

    # Change bio
    print("Changing bio...")
    driver.find_element_by_xpath("/html/body/div/div[1]/div[3]/a").click()

    driver.find_element_by_xpath("/html/body/div/div[3]/div[4]/div[2]/div[3]/div/form/input[1]").send_keys("The price of excellence is eternal vigilance")
    driver.find_element_by_xpath("/html/body/div/div[3]/div[4]/div[2]/div[3]/div/form/input[2]").click()
    print("Bio changed!")
    driver.find_element_by_xpath("/html/body/center/a").click()

    # Change contact
    print("Changing contact...")
    driver.find_element_by_xpath("/html/body/div/div[1]/div[3]/a").click()

    driver.find_element_by_xpath("/html/body/div/div[3]/div[4]/div[2]/div[4]/div/form/input[1]").send_keys("0456666666")
    button = driver.find_element_by_xpath("/html/body/div/div[3]/div[4]/div[2]/div[4]/div/form/input[2]")
    driver.execute_script("arguments[0].click();", button)
    print("Contact changed!")

    print("Viewing course pages...")
    driver.get(default_target+"/course")
    driver.get(default_target+"/js2")
    driver.get(default_target+"/html2")
    driver.get(default_target+"/css2")
#------------------------------------------------

if __name__ == '__main__':
    if len(sys.argv)>1:
        if sys.argv[1] == "setup":
            register("FamilyGuy@gmail.com", "familyguysyyds", "FamilyGuy", 2, "andruey")
            register("bottlecourse@gmail.com", "bottlecourse", "bottlecourse", 1, "2021")
    else:
        temp = random.randint(1,3)
        if temp == 1:
            virtual_user_1()
        elif temp == 2:
             virtual_user_2()
        elif temp == 3:
            virtual_user_3()


print("Finished!")
