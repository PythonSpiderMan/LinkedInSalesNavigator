from selenium import webdriver
import time
import getpass
import copy
from scrapy.selector import Selector
import json

waitseconds = 5

class Step2:
    def __init__(self):
        # The Final Result we are looking for
        final_profiles = []


        # Get all search result html file paths from `temp/step_1/file_paths.json` file
        last_step_directory = 'temp/step_1/'
        f = open(file=last_step_directory + 'file_paths.json', mode='rb')
        file_paths = json.loads(f.read().decode('utf-8'))
        f.close()


        # Parse Downloaded HTML files 1 by 1
        count = 1
        for each_html in file_paths:
            parser = SaleNavigatorProfileHtmlParser(each_html)
            parser.extract_profile()
            final_profiles += parser.extracted_result()
            # print(parser.extracted_result())
            print("%s html file parsed" % (str(count)))
            count += 1

        # Save Parsed Result to `temp/step_2/final_profiles.json` file
        step_directory = 'temp/step_2/'
        f = open(file=step_directory + 'final_profiles.json', mode='wb')
        f.write(json.dumps(final_profiles).encode('utf-8'))
        f.close()

        print("We have parsed all the search result pages of step1")
        print("Step 2 Finished !")
class SaleNavigatorProfileHtmlParser:
    # TODO: Xpath in Sales Navigator Search Result Pages
    xpath_card = """//*[@id="results-list"]/li"""

    xpath_contact_linkedin_profile_url = """//li/div[@class="content-wrapper"]//*[@class="name"]/*[concat('https://www.linkedin.com', @href)]/@href"""
    xpath_name = """//li/div[@class="content-wrapper"]/div//*[@class="name"]/*/@title"""

    xpath_title = """//li/div[@class="content-wrapper"]//p[@class="info-value"][1]/text() | //li/div[@class="content-wrapper"]//p[@class="info-value"][1]/*/text()"""  
    xpath_time_in_role = """//li/div[@class="content-wrapper"]//*[@class="info-value"][contains(text(), 'role')]/text()"""
    xpath_contact_location = """//li/div[@class="content-wrapper"]//*[@class="info-value"][last()]/text() | //li/div[@class="content-wrapper"]//*[@class="info-value"][last()]/*/text()"""
    xpath_company = """//li/div[@class="content-wrapper"]//*[contains(@class, 'company-name')]/@title"""
    xpath_company_profile_linkedin_url = """//li/div[@class="content-wrapper"]//a[contains(@class, 'company-name')][concat('https://www.linkedin.com', @href)]/@href"""

    def __init__(self, html_file):
        # Final profiles
        self.final_profiles = []

        # Read a html file
        f = open(file=html_file, mode='rb')
        self.html = f.read().decode('utf-8')
        f.close()


    def extract_profile(self):
        # Extract contact card
        cards = None
        try:
            cards = Selector(text=self.html).xpath(self.xpath_card).extract()

        except:
            print("Please make sure you passed reCAPTCHA before enter something")

        if len(cards) > 1:
            for each_card in cards:
                self.extract_and_append_profiles(each_card)

        else:
            pass

    def extract_and_append_profiles(self, each_card):
        linked_in_sales_navigator_person_template = {
            'title': str()

            # Person information
            ,'name'                             : str()
            ,'first_name'                       : str()
            ,'last_name'                        : str()
            ,'time_in_role'                     : str()
            ,'twitter'                          : str()
            ,'contact_linkedin_profile_url'     : str()
            ,'contact_location'                 : str()

            # Company information
            ,'company'                          : str()
            ,'company_size'                     : str()
            ,'industry'                         : str()
            ,'company_profile_linkedin_url'     : str()
            ,'company_website'          : str()
        }

        # TODO: Remove xpath that doesn't belongs to linkedin sales navigator search html

        for each_title in Selector(text=each_card).xpath(self.xpath_title).extract():
            linked_in_sales_navigator_person_template['title'] += (copy.deepcopy(each_title))

        linked_in_sales_navigator_person_template['name'] = Selector(text=each_card).xpath(
            self.xpath_name).extract_first(default='NOPE NOPE')

        try:
            if len(linked_in_sales_navigator_person_template['name'].split(' ')) >= 2:
                linked_in_sales_navigator_person_template['first_name'] = \
                    linked_in_sales_navigator_person_template['name'].split(' ')[0]

                linked_in_sales_navigator_person_template['last_name'] = \
                    linked_in_sales_navigator_person_template['name'].split(' ')[1]
            else:
                linked_in_sales_navigator_person_template['first_name'] = \
                    linked_in_sales_navigator_person_template['name']

                linked_in_sales_navigator_person_template['last_name'] = \
                    linked_in_sales_navigator_person_template['name']
        except:
            linked_in_sales_navigator_person_template['first_name'] = \
                linked_in_sales_navigator_person_template['name']
            linked_in_sales_navigator_person_template['last_name'] = \
                linked_in_sales_navigator_person_template['name']

        for each_role in Selector(text=each_card).xpath(self.xpath_time_in_role).extract():
            linked_in_sales_navigator_person_template['time_in_role'] += (copy.deepcopy(each_role))

        linked_in_sales_navigator_person_template['contact_linkedin_profile_url'] = "https://www.linkedin.com" + Selector(text=each_card).xpath(
            self.xpath_contact_linkedin_profile_url).extract_first(default='/')

        for each_location in Selector(text=each_card).xpath(self.xpath_contact_location).extract():
            linked_in_sales_navigator_person_template['contact_location'] += (copy.deepcopy(each_location))

        for each_company in Selector(text=each_card).xpath(self.xpath_company).extract():
            linked_in_sales_navigator_person_template['company'] += (copy.deepcopy(each_company))

        linked_in_sales_navigator_person_template['company_profile_linkedin_url'] = "https://www.linkedin.com" + Selector(text=each_card).xpath(
            self.xpath_company_profile_linkedin_url).extract_first(default='/')

        self.final_profiles.append(copy.deepcopy(linked_in_sales_navigator_person_template))

    def extracted_result(self):
        return copy.deepcopy(self.final_profiles)

class Step3:
    def __init__(self, driver):
        # Get all User's profile links from step_2
        last_step_directory = 'temp/step_2/'
        f = open(file=last_step_directory + 'final_profiles.json', mode='rb')
        self.final_profiles = json.loads(f.read().decode('utf-8'))
        f.close()
        self.profile_total = len(self.final_profiles)

        # Selenium initialization
        self.driver = driver

    def run(self):

        for index in range(0, self.profile_total):
            if 'contact_linkedin_profile_url' in self.final_profiles[index]:
                self.download_linkedin_personal_profile_page(self.final_profiles[index]['contact_linkedin_profile_url'], index)

    def download_linkedin_personal_profile_page(self, profile_url, index):
        # TODO: Check if this time is enough to load profile page
        self.driver.get(str(profile_url))
        # TODO: time
        time.sleep(waitseconds)

        # Save Opened Profile Page
        step_directory = 'temp/step_3/'
        f = open(file=step_directory + str(index) + '.html', mode='wb')
        f.write(self.driver.page_source.encode('utf-8'))
        f.close()

class Step4:
    def __init__(self):

        # Get final user profiles from step2
        step_2_directory = 'temp/step_2/'
        f = open(file=step_2_directory + 'final_profiles.json', mode='rb')
        final_profiles = json.loads(f.read().decode('utf-8'))
        f.close()


        # Parse each user's personal profile page and insert extracted data
        total_profiles = len(final_profiles)
        for index in range(0, total_profiles):
            self.extract_and_append_person_information(final_profiles, index)

        # Save new final profile
        step_directory = 'temp/step_4/'
        f = open(file=step_directory + 'final_profiles.json', mode='wb')
        f.write(json.dumps(final_profiles).encode('utf-8'))
        f.close()

    def extract_and_append_person_information(self, profile, index):
        # Get the person's profile html
        last_step_directory = 'temp/step_3/'

        parser = PersonalProfileHtmlParser(last_step_directory + str(index) + '.html', profile, index)
        parser.extract_and_insert_personal_information()
class PersonalProfileHtmlParser:
    # TODO: Xpath in Personal Profile Page
    xpath_twitter = """//a[contains(@href, 'twitter')]/@href"""

    def __init__(self, html_file, profile, index):
        # Read a html file
        f = open(file=html_file, mode='rb')
        self.html = f.read().decode('utf-8')
        f.close()

        self.profile = profile
        self.index = index

    def extract_and_insert_personal_information(self):
        # TODO: Remove xpath that doesn't belongs to personal profile page
        self.profile[self.index]['twitter'] = Selector(text=self.html).xpath(self.xpath_twitter).extract_first(default='NOPE')

class Step5:
    def __init__(self, driver):

        # Get all User's profile links from step_4
        last_step_directory = 'temp/step_4/'
        f = open(file=last_step_directory + 'final_profiles.json', mode='rb')
        self.final_profiles = json.loads(f.read().decode('utf-8'))
        f.close()
        self.profiles_total = len(self.final_profiles)

        # Selenium initialization
        self.driver = driver

    def run(self):
        for index in range(0, self.profiles_total):
            if 'company_profile_linkedin_url' in self.final_profiles[index]:
                self.download_linkedin_company_profile_page(self.final_profiles[index]['company_profile_linkedin_url'], index)


    def download_linkedin_company_profile_page(self, company_profile_url, index):
        # TODO: Check if this time is enough to load profile page
        self.driver.get(str(company_profile_url))
        # TODO: time
        time.sleep(waitseconds)


        # Save Opened Profile Page
        step_directory = 'temp/step_5/'
        f = open(file=step_directory + str(index) + '.html', mode='wb')
        f.write(self.driver.page_source.encode('utf-8'))
        f.close()


if __name__ == '__main__':
    driver = webdriver.Firefox(executable_path=r'geckodriver.exe')

    username = input("Please enter your LinkedIn Username: ")
    password = getpass.getpass("Please enter your LinkedIn Password: ")

    sales_navigator_url = input("Please enter a LinkedIn Sales Navigator URL: ")


    # Switch to LinkedIn Login Page
    driver.get("https://www.linkedin.com/")
    # TODO: time
    time.sleep(waitseconds)


    # Login to Linked In
    xpath_user_name = """//*[@id="login-email"]"""
    xpath_password = """//*[@id="login-password"]"""
    xpath_login = """//*[@id="login-submit"]"""

    driver.find_element_by_xpath(xpath_user_name).send_keys(str(username).strip())
    driver.find_element_by_xpath(xpath_password).send_keys(str(password).strip())
    driver.find_element_by_xpath(xpath_login).click()
    # TODO: time
    time.sleep(waitseconds)

    key = input("Enter any key when you have finished reCAPCHA verification: ")

    # Open LinkedIn Sales Navigator URL
    driver.get(str(sales_navigator_url))
    # TODO: time
    time.sleep(waitseconds)


    # Download all search result pages to temp/step_1/ folder
    sales_navigator_search_result_html_paths = []


    # TODO: Xpath of Next_Page Button
    xpath_next_page = """//*[@id="pagination"]/a[2][not(contains(@class, 'disabled'))]"""
    step_directory = 'temp/step_1/'

    next_button = None
    while True:
        next_button = Selector(text=driver.page_source).xpath(xpath_next_page).extract_first()
        if next_button is None:
            waitseconds += 1
            time.sleep(1)
            if waitseconds >= 15:
                print("Please check your linkedin sales navigator url and your internet connection")
        else:
            waitseconds -= 1
            break

    index = 0

    while True:
        # Find next_button
        next_button = Selector(text=driver.page_source).xpath(xpath_next_page).extract_first()

        # Save this page to file
        html_file_path = step_directory + str(index) + '.html'
        f = open(file=html_file_path, mode='wb')
        f.write(driver.page_source.encode('utf-8'))
        f.close()

        # Append this file's path to list
        sales_navigator_search_result_html_paths.append(html_file_path)

        if next_button is not None:
            # Go to the next page
            driver.find_element_by_xpath(xpath_next_page).click()
            # TODO: time
            time.sleep(waitseconds)

            index += 1
        else:
            break

    # Save file's paths to a json file
    json_string = json.dumps(sales_navigator_search_result_html_paths)
    json_file_path = step_directory + 'file_paths' + '.json'
    f = open(file=json_file_path, mode='wb')
    f.write(json_string.encode('utf-8'))
    f.close()

    print("We have saved all the search result pages in to step1 folder")
    print("Total: %s pages collected" % (len(sales_navigator_search_result_html_paths)))
    print("We will parse search result pages next.")
    print("Step 1 Finished !")


    Step2()


    program = Step3(driver)
    program.run()
    print("We have downloaded all users' personal profile page")
    print("Step 3 Finished !")


    Step4()
    print("We have parsed all users' personal profile page")
    print("Step 4 Finished !")


    program = Step5(driver)
    program.run()
    print("We have downloaded all users' company profile page")
    print("Step 5 Finished !")

    # Close the browser
    driver.close()
