print("Script is running...")
members = {
    "Jin": {
        "name": "Kim Seok-jin",
        "birthday": "December 4, 1992",
        "position": "vocalist",
        "hometown": "Gwacheon, Gyeonggi Province, South Korea",
        "zodiac": "sagittarius",
        "instagram": "@jin",
        "nickname": "world wide handsome",
        "favorite number": "4",
        "allergies": "garlic, potatoes",
        "role model": "t.o.p from bigbang",
        "idol friends": "b1a4's sandeul, vixx's ken, monsta x's jooheon",
        "details": {}
    },
    "SUGA": {
        "name": "Min Yoon-gi",
        "birthday": "March 9, 1993",
        "position": "rapper",
        "hometown": "Daegu, South Korea",
        "zodiac": "Pisces",
        "big_three": "pisces sun, virgo moon, cancer rising",
        "solo_discography": {
            "mixtapes": ["Agust D (August 15, 2016)", "D-2 (May 22, 2020)"],
            "singles": ["Agust D (August 15, 2016)", "Give It to Me (August 15, 2016)", "Daechwita (May 22, 2020)", "People Pt.2 (April 7, 2023)"],
            "albums": ["D-Day (April 21, 2023)"]
        },
        "allergies": "grass",
        "basketball position": "shooting guard",
        "musical influences": "Eminem, Epik High, Ryouchi Sakamoto",
        "details": {}
    },
    "J-Hope": {
        "name": "Jung Ho-seok",
        "birthday": "February 18, 1994",
        "position": "rapper",
        "hometown": "Gwangju, South Korea",
        "zodiac": "Aquarius",
        "big_three": "aquarius sun, scorpio moon, leo rising",
        "solo_discography": {
            "mixtapes": ["Hope World (March 1, 2018)", "Jack In The Box (July 15, 2022)"],
            "singles": ["Daydream (March 1, 2018)", "Hangsang (March 1, 2018)", "Airplane Pt.2 (March 1, 2018)", "More (July 15, 2022)", "Arson (July 15, 2022)"],
            "albums": []
        },
        "details": {}
    },
    "RM": {
        "name": "Kim Nam-joon",
        "birthday": "September 12, 1994",
        "position": "leader, rapper",
        "hometown": "Seoul, South Korea",
        "zodiac": "Virgo",
        "big_three": "virgo sun, leo moon, libra rising",
        "solo_discography": {
            "mixtapes": ["RM (March 17, 2015)", "mono. (October 23, 2018)"],
            "singles": ["awake (March 17, 2015)", "seoul (March 17, 2015)", "forever rain (October 23, 2018)", "seoul (prod. HONNE) (October 23, 2018)"],
            "albums": ["Indigo (December 2, 2022)"]
        },
        "details": {}
    },
    "Jimin": {
        "name": "Park Ji-min",
        "birthday": "October 13, 1995",
        "position": "vocalist",
        "hometown": "Busan, South Korea",
        "zodiac": "Libra",
        "big_three": "libra sun, leo moon, scorpio rising",
        "solo_discography": {
            "albums": ["Face (March 24, 2023)"],
            "singles": ["Promise (December 31, 2018)", "Christmas Love (December 23, 2020)", "Set Me Free Pt.2 (March 17, 2023)", "Like Crazy (March 24, 2023)"]
        },
        "allergies": "cats",
        "details": {
            "Jimmy Fallon": "Jimin appeared solo on The Tonight Show Starring Jimmy Fallon to promote his album FACE on March 23rd and 24th, 2023.",
            "Music Bank": "Jimin appeared on Music Bank and performed 'Set Me Free Pt.2' and 'Like Crazy' from his album Face on March 31st, 2023."
        }
    },
    "V": {
        "name": "Kim Tae-hyung",
        "birthday": "December 30, 1995",
        "position": "vocalist",
        "hometown": "Daegu, South Korea",
        "zodiac": "Capricorn",
        "big_three": "capricorn sun, scorpio moon, aquarius rising",
        "solo_discography": {
            "albums": ["Layover (August 2023)"],
            "singles": ["Scenery (January 30, 2019)", "Winter Bear (August 9, 2019)", "Christmas Tree (December 24, 2020)", "Singularity (October 6, 2022)", "Rainy Days (August 2023)"]
        },
        "details": {}
    },
    "Jungkook": {
        "name": "Jeon Jung-kook",
        "birthday": "September 1, 1997",
        "position": "main vocalist, lead dancer, center, maknae",
        "hometown": "Busan, South Korea",
        "zodiac": "virgo",
        "allergies": "cats",
        "solo_discography": {
            "mixtapes": ["Hope World (March 1, 2018)"],
            "singles": ["Euphoria (April 5, 2018)", "My Time (February 21, 2020)", "Stay Alive (February 11, 2022)"],
            "albums": ["Golden (November 3, 2023)"]
        },
        "details": {}
    }
}

bts_info = {
    "concerts": [
        {"name": "Love Yourself: Speak Yourself Tour", "dates": "2019-05-04 - 2019-10-26"},
        {"name": "BTS World Tour 'Love Yourself: Speak Yourself'", "dates": "2019-04-12 - 2019-10-29"}
    ],
    "tours": [
        {"name": "2017 BTS Live Trilogy Episode III The Wings Tour", "dates": "2017-02-18 - 2017-12-10"},
        {"name": "BTS World Tour 'Love Yourself'", "dates": "2018-08-25 - 2019-01-27"},
        {"name": "BTS World Tour 'Love Yourself: Speak Yourself'", "dates": "2019-05-04 - 2019-10-26"}
    ],
    "tv_shows": {
        "USA": [
            {"name": "The Tonight Show Starring Jimmy Fallon", "date": "2019-05-22"},
            {"name": "The Late Show with Stephen Colbert", "date": "2019-09-24"},
            {"name": "Good Morning America", "date": "2019-05-21"},
            {"name": "The Ellen DeGeneres Show", "date": "2019-05-20"},
            {"name": "Jimmy Kimmel Live!", "date": "2019-05-16"}
        ],
        "Korea": [
            {"name": "M! Countdown", "date": "2013-06-13"},
            {"name": "Music Bank", "date": "2013-06-14"},
            {"name": "Inkigayo", "date": "2013-06-16"}
        ],
        "Japan": [
            {"name": "Music Station", "date": "2014-11-28"},
            {"name": "FNS Music Festival", "date": "2014-12-02"}
        ]
    },
    "awards": {
        "won": [
            {"name": "Billboard Music Award", "year": 2017, "category": "Top Social Artist"},
            {"name": "Billboard Music Award", "year": 2018, "category": "Top Social Artist"},
            {"name": "Billboard Music Award", "year": 2019, "category": "Top Social Artist"},
            {"name": "Billboard Music Award", "year": 2020, "category": "Top Social Artist"},
            {"name": "Billboard Music Award", "year": 2021, "category": "Top Duo/Group"},
            {"name": "Billboard Music Award", "year": 2021, "category": "Top Song Sales Artist"},
            {"name": "Billboard Music Award", "year": 2021, "category": "Top Selling Song"},
            {"name": "Billboard Music Award", "year": 2022, "category": "Top Duo/Group"},
            {"name": "Billboard Music Award", "year": 2022, "category": "Top Song Sales Artist"}
        ],
        "nominated": [
            {"name": "American Music Award", "year": 2018, "category": "Favorite Duo or Group - Pop"},
            {"name": "American Music Award", "year": 2019, "category": "Favorite Duo or Group - Pop"},
            {"name": "American Music Award", "year": 2020, "category": "Favorite Duo or Group - Pop"},
            {"name": "American Music Award", "year": 2021, "category": "Favorite Duo or Group - Pop"},
            {"name": "American Music Award", "year": 2021, "category": "Favorite Music Video"},
            {"name": "American Music Award", "year": 2022, "category": "Favorite Duo or Group - Pop"}
        ],
        "performances": [
            {"name": "American Music Awards", "year": 2021, "song": "Butter"},
            {"name": "Grammy Awards", "year": 2022, "song": "Butter"}
        ]
    }
}

def main_menu():
    print("Select an option:")
    print("1. Members")
    print("2. BTS Info")
    while True:
        choice = input("Enter your choice (1-2): ")
        if choice == "1":
            member_menu()
            break
        elif choice == "2":
            bts_info_menu()
            break
        else:
            print("Invalid choice. Please try again.")

def member_menu():
    print("Select a member to begin!")
    members_list = list(members.keys())
    for i, member in enumerate(members_list, start=1):
        print(f"{i}. {member}")
    while True:
        choice = input("Enter your choice (1-7) or * for general info: ")
        if choice == "*":
            general_info()
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(members_list):
            member_name = members_list[int(choice) - 1]
            print(f"In the mind of {member_name}...")
            member_menu(member_name)
            break
        else:
            print("Invalid choice. Please try again.")

def member_menu(member_name):
    member_info = members.get(member_name)
    if member_info:
        options = [key for key in member_info.keys() if key != "details"]
        print(f"{member_name} Menu:")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option.replace('_', ' ').title()}")
        print(f"{len(options) + 1}. Return to Main Menu")
        while True:
            choice = input(f"Enter your choice (1-{len(options) + 1}): ")
            if choice == str(len(options) + 1):
                main_menu()
                break
            elif choice.isdigit() and 1 <= int(choice) <= len(options):
                query = options[int(choice) - 1]
                print(answer_query(member_name, query))
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Member not found")
        main_menu()

def answer_query(member_name, query):
    member_info = members.get(member_name)
    if member_info:
        query_key = query.lower().replace(" ", "_")
        answer = member_info.get(query_key)
        if answer:
            if isinstance(answer, list) or isinstance(answer, dict):
                return f"{member_name} {query}: {answer}"
            else:
                return f"{member_name} {query}: {answer}"
        else:
            details = member_info.get("details", {})
            detail_answer = details.get(query, None)
            if detail_answer:
                return f"{member_name} {query}: {detail_answer}"
            else:
                return f"{member_name} has no information about {query}"
    elif member_name == "BTS":
        if query == "concerts":
            return bts_info["concerts"]
        elif query == "tours":
            return bts_info["tours"]
        elif query == "tv_shows":
            return bts_info["tv_shows"]
        elif query == "awards":
            return bts_info["awards"]
        else:
            return f"No information found for {query}"
    else:
        return "Member not found"

def bts_info_menu():
    print("BTS Info Menu:")
    options = ["Concerts", "Tours", "TV Shows", "Awards"]
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    while True:
        choice = input("Enter your choice (1-4) or * to return to main menu: ")
        if choice == "*":
            main_menu()
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(options):
            category = options[int(choice) - 1].lower().replace(" ", "_")
            print(f"{category.title()} Information:")
            print(answer_query("BTS", category))
            break
        else:
            print("Invalid choice. Please try again.")


def general_info():
    print("General Information:")
    print("To be implemented")

main_menu()
