userYear = 0
userYear = int(input("Enter your birth year: "))
zodiac = ""


if  userYear < 1900:
    print("Invalid Year, it should not be earlier than 1900.")
elif userYear > 2026:
    print("Invalid Year, it should not be later than 2026.")
else:
    if userYear % 12 == 0:
        zodiac = "Monkey (猴 / Hóu)"
    elif userYear % 12 == 1:
        zodiac = "Rooster (鸡 / Jī)"
    elif userYear % 12 == 2:
        zodiac = "Dog (狗 / Gǒu)"
    elif userYear % 12 == 3:
        zodiac = "Pig (猪 / Zhū)"
    elif userYear % 12 == 4:
        zodiac = "Rat (鼠 / Shǔ)"
    elif userYear % 12 == 5:
        zodiac = "Ox (牛 / Niú)"
    elif userYear % 12 == 6:
        zodiac = "Tiger (虎 / Hǔ)"
    elif userYear % 12 == 7:
        zodiac = "Rabbit (兔 / Tù)"
    elif userYear % 12 == 8:
        zodiac = "Dragon (龙 / Lóng)"
    elif userYear % 12 == 9:
        zodiac = "Snake (蛇 / Shé)"
    elif userYear % 12 == 10:
        zodiac = "Horse (马 / Mǎ)"
    elif userYear % 12 == 11:
        zodiac = "Goat (羊 / Yáng)"

    print()
    print(f"Your Chinese Zodiac Sign is: {zodiac}")
    print()