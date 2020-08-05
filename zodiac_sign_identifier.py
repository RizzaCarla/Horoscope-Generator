class ZodiacSignIdentifier:

    def __init__(self, month, date):
        self.month = month
        self.date = date

    # -----Zodiac Sign Generator Function-----
    # This section will take user's birthday info and generate their zodiac sign.
    # The function will compare the user's birth month to the dictionary.
    # The function should be able to retrieve the value using the fully or partially spelled month.
    # Once the value has been retrieved, the series of if/elif/else statements will use the month and date to identify your zodiac.
    # ---------------------------------------

    def zodiac_sign_generator(self):
        month_dictionary = {
            'january': 1,
            'jan': 1,
            'february': 2,
            'feb': 2,
            'march': 3,
            'mar': 4,
            'april': 4,
            'apr': 4,
            'may': 5,
            'june': 6,
            'jun': 6,
            'july': 7,
            'jul': 7,
            'august': 8,
            'aug': 8,
            'september': 9,
            'sep': 9,
            'october': 10,
            'oct': 10,
            'november': 11,
            'nov': 11,
            'december': 12,
            'dec': 12
        }
        keys = month_dictionary.keys()
        values = month_dictionary.values()
        month_num = ""
        found_flag = False
        for x in keys:
            if self.month == x:
                found_flag = True
                month_num = int(month_dictionary[x])
        date_num = int(self.date)

        if (date_num < 1 or date_num > 31) and not found_flag:
            return "Please enter a valid month and date.For example: Jan 1, february 2, mar 3, April 4, etc"
        if date_num < 1 or date_num > 31:
            return "Please enter a valid date. For example: 1, 2,...31"
        elif not found_flag:
            return "Please enter a valid month. For example: January, feb,...december"

        #
        # print("date num = " + str(date_num))

        if month_num == 1 and 1 <= date_num <= 20:
            user_zodiac = "Capricorn"
        elif month_num == 1 and 21 <= date_num <= 31:
            user_zodiac = "Aquarius"
        elif month_num == 2 and 1 <= date_num <= 18:
            user_zodiac = "Aquarius"
        elif month_num == 2 and 19 <= date_num <= 31:
            user_zodiac = "Pisces"
        elif month_num == 3 and 1 <= date_num <= 20:
            user_zodiac = "Pisces"
        elif month_num == 3 and 21 <= date_num <= 31:
            user_zodiac = "Aries"
        elif month_num == 4 and 1 <= date_num <= 20:
            user_zodiac = "Aries"
        elif month_num == 4 and 21 <= date_num <= 31:
            user_zodiac = "Taurus"
        elif month_num == 5 and 1 <= date_num <= 20:
            user_zodiac = "Taurus"
        elif month_num == 5 and 21 <= date_num <= 31:
            user_zodiac = "Gemini"
        elif month_num == 6 and 1 <= date_num <= 21:
            user_zodiac = "Gemini"
        elif month_num == 6 and 22 <= date_num <= 31:
            user_zodiac = "Cancer"
        elif month_num == 7 and 1 <= date_num <= 22:
            user_zodiac = "Cancer"
        elif month_num == 7 and 23 <= date_num <= 31:
            user_zodiac = "Leo"
        elif month_num == 8 and 1 <= date_num <= 23:
            user_zodiac = "Leo"
        elif month_num == 8 and 24 <= date_num <= 31:
            user_zodiac = "Virgo"
        elif month_num == 9 and 1 <= date_num <= 23:
            user_zodiac = "Virgo"
        elif month_num == 9 and 24 <= date_num <= 31:
            user_zodiac = "Libra"
        elif month_num == 10 and 1 <= date_num <= 23:
            user_zodiac = "Libra"
        elif month_num == 10 and 24 <= date_num <= 31:
            user_zodiac = "Scorpio"
        elif month_num == 11 and 1 <= date_num <= 22:
            user_zodiac = "Scorpio"
        elif month_num == 11 and 23 <= date_num <= 31:
            user_zodiac = "Sagittarius"
        elif month_num == 12 and 1 <= date_num <= 21:
            user_zodiac = "Sagittarius"
        elif month_num == 12 and 22 <= date_num <= 31:
            user_zodiac = "Capricorn"
        else:
            user_zodiac = "unidentifiable"
        return user_zodiac
