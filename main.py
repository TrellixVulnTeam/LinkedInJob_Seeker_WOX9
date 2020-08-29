import pdb
from time import sleep
import csv
import pickle
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox("C:\Program Files\Mozilla Firefox")
f = open("testData.csv", "a", newline="")


class Cookies:

    def save_cookies(driver, location):
        pickle.dump(driver.get_cookies(), open(location, "wb"))

    def load_cookies(driver, location, url=None):
        cookies = pickle.load(open(location, "rb"))
        driver.delete_all_cookies()
        # Have to be on a page before adding any cookies. ANy page
        driver.get("https://google.com" if url is None else url)
        for cookie in cookies:
            if isinstance(cookie.get('expiry'), float):  # Checks if the instance expiry a float
                cookie['expiry'] = int(cookie['expiry'])  # it converts expiry cookie to a int
            driver.add_cookie(cookie)

    def delete_cookies(driver, domains=None):
        if domains is not None:
            cookies = driver.get_cookies()
            original_len = len(cookies)
            for cookie in cookies:
                if str(cookie["domain"]) in domains:
                    cookies.remove(cookie)
            if len(cookies) < original_len:  # if cookies changed, we will update them
                # deleting everything and adding the modified cookie object
                driver.delete_all_cookies()
                for cookie in cookies:
                    driver.add_cookie(cookie)
        else:
            driver.delete_all_cookies()

    cookies_location = r"C:\Users\user\PycharmProjects\DataScrapingLinkedIn\cookies.txt"



driver.get('https://www.linkedin.com/login/en?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
# ---------------------------------
'''
# Login Credentials
username = driver.find_element_by_id("username")
username.clear()
username.send_keys("moffici1234@gmail.com")

password = driver.find_element_by_id("password")
password.clear()
password.send_keys("007SkyFall")
# --------------------------------
driver.find_element_by_class_name("login__form_action_container").click()
sleep(50)
Cookies.save_cookies(driver, Cookies.cookies_location)
driver.quit()
sleep(10)

''' 


driver = webdriver.Firefox("C:\Program Files\Mozilla Firefox")
Cookies.load_cookies(driver, Cookies.cookies_location,
                     'https://www.linkedin.com/jobs/search/?geoId=101165590&keywords=junior%20software%20engineer&location=United'
                     '%20Kingdom&originalSubdomain=en')
driver.get(
    'https://www.linkedin.com/jobs/search/?geoId=101165590&keywords=junior%20software%20engineer&location=United'
    '%20Kingdom&originalSubdomain=en')

premium_skills = []


def AssignPriority(alums, skillsMatch, applicantRank):
    priority = 0

    return priority
    pass


class JobAdvert:
    def __init__(self, title, skills, alums, skillsMatch, applicantRank, url):
        # self.url = url
        self.title = title
        self.skills = skills
        self.alum = alums
        self.skillsMatch = skillsMatch
        self.url = url
        self.applicantRank = applicantRank
        priority = AssignPriority(alums, skillsMatch, applicantRank)
        _updatedSkills = []

        _updatedSkills = {skill.replace('(You have this skill!)', '').replace('\n', '') for skill in skills}
        _updatedSkills = {skill.replace('\n', '') for skill in _updatedSkills}
        writer = csv.writer(f)
        # writer.writerow(["Title", "Skills", "Alums", "skillsMatch", "Applicant Rank", "Priority"])
        writer.writerow([title, _updatedSkills, alums, skillsMatch, applicantRank, url, priority])


driver.execute_script("document.querySelector('div[class*=jobs-search-results--is-two-pane]').scrollTop = 3500")
sleep(1)




def changeSkillsMatch(skillText):
    if len(skillText) == 4:
        skillText = skillText[2, "/"]
    else:
        skillText = skillText[1, "/"]
    return skillText


class CheckJobOffer:
    # driver.find_elements_by_class_name("job-flavors__flavor job-flavors__flavor--school-recruit ember-view") # This
    # checks if I have people from Uni there
    # for x in range(0, len(jobOffers)):
    # saver = False
    total_height = 3000

    for i in range(1, total_height, 5):
        driver.execute_script("document.querySelector('div[class*=jobs-search-results--is-two-pane]').scrollTo(0, {});".format(i))

    sleep(5)


    currentPage = 0
    for currentPage in range(1, 40):
        x = -1
        pageNumberDiv = driver.find_element_by_xpath(
            "/html/body/div[8]/div[3]/div[3]/div/div/div/section/div/div/section/div/ul")
        pageButtons = pageNumberDiv.find_elements_by_tag_name("li")
        # for each job offer: check the skills and move onto the next one, repeat
        for i in range(1, total_height, 5):
            driver.execute_script(
                "document.querySelector('div[class*=jobs-search-results--is-two-pane]').scrollTo(0, {});".format(i))
        jobOffers = driver.find_elements_by_class_name("artdeco-entity-lockup__title")
        sleep(5)
        print(len(jobOffers), " Job Offers on page: ", currentPage)
        for jobOffer in jobOffers:
            sleep(1)
            #driver.execute_script("document.querySelector('div[class*=jobs-search-two-pane__details]').scrollTop= 2500")
            for i in range(1, total_height, 5):
                driver.execute_script(
                    "document.querySelector('div[class*=jobs-search-two-pane__details]').scrollTo(0, {});".format(i))
            sleep(1)
            parentElement = driver.find_elements_by_class_name("jobs-premium-applicant-insights__pill")
            # url = driver.current_url
            Titles = driver.find_elements_by_class_name("jobs-details-top-card__job-title")
            for title in Titles:
                _title = title.text

            # print(_title)
            _alums = ""
            _skills = []
            _skillsMatch = ""
            _applicantRank = "0"
            _url = driver.current_url
            try:
                alumni = driver.find_element_by_xpath(
                    "/html/body/div[8]/div[3]/div[3]/div/div/div/div/div/div[1]/div/div[1]/ul/li[3]/div/ul/li/div/a/div[2]")
                _alums = alumni.text

            except:

                _alums = "0"
            try:
                _skillsMatch = driver.find_element_by_xpath(
                    "/html/body/div[8]/div[3]/div[3]/div/div/div/div/div/div[1]/div/div[3]/div/div[1]/div[2]/div[2]/p/span").text

                # re.sub("[^0-9]", "", skillsMatch)
                #_skillsMatch = skillsMatch
                # print(skillsMatch)
                # _skillsMatch = changeSkillsMatch(skillsMatch)

            except:
                skillsMatch = "N/A"

            try:
                ApplicantRank = driver.find_element_by_xpath(
                    "/html/body/div[8]/div[3]/div[3]/div/div/div/div/div/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/span[1]").text
                _applicantRank = ApplicantRank

            except:
                _applicantRank = "N/A"

            for element in parentElement:
                _skills.append(element.text)

            JobAdvert(_title, _skills, _alums, _skillsMatch, _applicantRank, _url)
            x += 1

            sleep(2)
            jobOffers[x].click()
        pageButtons[currentPage+1].click()
        sleep(3)
f.close()
