
import os
import configparser
config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\configurations\\config.ini')

class get_config:

    @staticmethod
    def get_application_url():
        url = (config.get('commonInfo', 'base_URL'))
        return url

    @staticmethod
    def get_application_email():
        email= (config.get("commonInfo", "email"))
        return email

    @staticmethod
    def get_application_pass():
        passw= (config.get("commonInfo", "password"))
        return passw














