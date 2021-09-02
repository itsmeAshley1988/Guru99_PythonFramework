import configparser

# We get the file and This line reads the ini file
config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")


class ReadConfig():
    # Login & Signup details below
    # Getting the Application URL from config.ini file
    @staticmethod
    def getApplicationURL():
        baseUrl = config.get('common details', 'baseURL')
        return baseUrl

    # Getting the username from config.ini file
    @staticmethod
    def getUsernameLogin():
        username_login = config.get('login details', 'username_login')
        return username_login

        # Getting the password from config.ini file
    @staticmethod
    def getPasswordLogin():
        password_login = config.get('login details', 'password_login')
        return password_login
