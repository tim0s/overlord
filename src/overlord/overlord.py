import re
import yaml
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import ActionChains


class overlord:

    def __init__(self):
        with open(r'/home/timos/.config/overlord') as file:
            self.config = yaml.load(file, Loader=yaml.FullLoader)


    def upload_file(self, project, overleaf_path, file_path, overwrite=True, email=None, password=None):

        opts = Options()
        #opts.headless = True
        browser = Firefox(options=opts)
        browser.get('https://overleaf.com/login')

        if email is None:
            email = self.config.get('email')
            if email is None:
                raise ValueError("No email provided for login")
        if password is None:
            password = self.config.get('password')
            if password is None:
                raise ValueError("No password provided for login")

        login_email = browser.find_element_by_id('email')
        login_email.send_keys(email)
        login_pw = browser.find_element_by_id('password')
        login_pw.send_keys(password)
        login_pw.submit()
        browser.implicitly_wait(2) 

        try:
            project = browser.find_element_by_link_text(project)
            project.click()
        except:
            raise ValueError("Project: " + project + " not found!")
        browser.implicitly_wait(2)


        items = browser.find_elements_by_class_name("item-name-button")
        for i in items:
            x = str(i.get_attribute('innerHTML'))
            m = re.match("<span>" + overleaf_path + "</span>", x)
            if m:
                action = ActionChains(browser)
                action.context_click(i).perform()
                browser.implicitly_wait(2)
                up = browser.find_element_by_link_text('Upload')
                up.click()
                browser.implicitly_wait(2)
                e = browser.find_element_by_xpath("//input[@type='file']")
                e.send_keys(file_path)

                try:
                    overwrite = browser.find_element_by_link_text('Overwrite')
                    overwrite.click()
                except:
                    pass

        

if __name__ == "__main__":
    o = overlord()
    o.upload_file("TimoTestproject", "plots", "/home/timos/Screenshot from 2021-04-04 13-14-40.png")