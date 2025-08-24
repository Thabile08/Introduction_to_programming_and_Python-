def main():
    time = input("What time is it? ")
    m_time = convert(time)
    if m_time >= 7 and m_time <= 8:
        print("Breakfast time")
    elif m_time >= 12 and m_time <= 13:
        print("Lunch time")
    elif m_time >= 18 and m_time <= 19:
        print("Dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours) + (float(minutes)/60)
    return hours

if __name__ == "__main__":
    main()
