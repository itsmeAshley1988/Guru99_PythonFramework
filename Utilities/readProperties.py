import configparser

# We get the file and This line reads the ini file
config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")


class ReadConfig():

    # Getting the Application URL from config.ini file
    @staticmethod
    def getApplicationURL():
        url = config.get('Common Details', 'baseURL')
        return url

    # Getting the username from config.ini file
    @staticmethod
    def getUsernameLogin():
        username_login = config.get('Login Details', 'username_login')
        return username_login

        # Getting the password from config.ini file
    @staticmethod
    def getPasswordLogin():
        password_login = config.get('Login Details', 'password_login')
        return password_login
