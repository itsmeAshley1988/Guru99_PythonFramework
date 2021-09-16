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

    @staticmethod
    def getFirstNameRegistration():
        firstName = config.get('registration details', 'firstName')
        return firstName

    @staticmethod
    def getLastNameRegistration():
        lastName = config.get('registration details', 'lastName')
        return lastName

    @staticmethod
    def getPhoneRegistration():
        phone = config.get('registration details', 'phone')
        return phone

    @staticmethod
    def getEmailRegistration():
        email = config.get('registration details', 'email')
        return email

    @staticmethod
    def getAddressRegistration():
        address = config.get('registration details', 'address')
        return address

    @staticmethod
    def getCityRegistration():
        city = config.get('registration details', 'city')
        return city

    @staticmethod
    def getProvinceRegistration():
        province = config.get('registration details', 'province')
        return province

    @staticmethod
    def getPostalCodeRegistration():
        postal_code = config.get('registration details', 'postal_code')
        return postal_code

    @staticmethod
    def getCountryRegistration():
        country = config.get('registration details', 'country')
        return country

    @staticmethod
    def getUsernameRegistration():
        username = config.get('registration details', 'username')
        return username

    @staticmethod
    def getPasswordRegistration():
        password = config.get('registration details', 'password')
        return password

    @staticmethod
    def getConfirmPasswordRegistration():
        confirm_password = config.get('registration details', 'confirm_password')
        return confirm_password


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

    @staticmethod
    def getFlightType():
        flight_type = config.get('flight details', 'flight_type')
        return flight_type

    @staticmethod
    def getPassengerCount():
        passengers = config.get('flight details', 'passengers')
        return passengers

    @staticmethod
    def getDepartingFrom():
        departingFrom = config.get('flight details', 'departingFrom')
        return departingFrom

    @staticmethod
    def getDepartingMonth():
        departingMonth = config.get('flight details', 'departingMonth')
        return departingMonth

    @staticmethod
    def getDepartingDay():
        departingDay = config.get('flight details', 'departingDay')
        return departingDay

    @staticmethod
    def getArrivingCountry():
        arrivingIn = config.get('flight details', 'arrivingIn')
        return arrivingIn

    @staticmethod
    def getReturningMonth():
        returningMonth = config.get('flight details', 'returningMonth')
        return returningMonth

    @staticmethod
    def getReturningDay():
        returningDay = config.get('flight details', 'returningDay')
        return returningDay

    @staticmethod
    def getServiceClass():
        serviceClass = config.get('flight details', 'serviceClass')
        return serviceClass

    @staticmethod
    def getAirlineName():
        airline = config.get('flight details', 'airline')
        return airline


