"""Step_6: Parse all scrapped user's company profile pages"""
from scrapy.selector import Selector
import json


def main():
    # Get final user profiles from step4
    step_4_directory = 'temp/step_4/'
    f = open(file=step_4_directory + 'final_profiles.json', mode='rb')
    final_profiles = json.loads(f.read().decode('utf-8'))
    f.close()


    # Parse each user's personal profile page and insert extracted data
    for index in range(0, len(final_profiles)):
        extract_and_append_company_information(final_profiles, index)

    # Save new final profile
    step_directory = 'temp/step_6/'
    f = open(file=step_directory + 'final_profiles.json', mode='wb')
    f.write(json.dumps(final_profiles).encode('utf-8'))
    f.close()


def extract_and_append_company_information(profile, index):
    # Get the person's company profile html
    last_step_directory = 'temp/step_5/'

    parser = CompanyProfileHtmlParser(last_step_directory + str(index) + '.html', profile, index)
    parser.extract_and_insert_company_information()


class CompanyProfileHtmlParser:
    # TODO: Xpath in Company Profile Page
    xpath_company_size = """//*[contains(@class,'size')]//text()"""
    xpath_industry = """//*[contains(@class, 'top-bar')]//*[contains(@class, 'industry')]/text()"""
    xpath_company_website = """//div[contains(@id, 'account-introduction')]//*[contains(@href, 'http')]/@href"""

    def __init__(self, html_file, profile, index):
        # Read a html file
        f = open(file=html_file, mode='rb')
        self.html = f.read().decode('utf-8')
        f.close()

        self.profile = profile
        self.index = index

    def extract_and_insert_company_information(self):
        # TODO: Remove xpath that doesn't belongs to company profile page
        self.profile[self.index]['company_size'] = Selector(text=self.html).xpath(self.xpath_company_size).extract_first(default='NOPE')

        self.profile[self.index]['industry'] = Selector(text=self.html).xpath(self.xpath_industry).extract_first(default='NOPE')

        self.profile[self.index]['company_website'] = Selector(text=self.html).xpath(self.xpath_company_website).extract_first(default='NOPE')

if __name__ == '__main__':
    main()

    print("We have parsed all users' company profile page")
    print("Step 6 Finished !")
