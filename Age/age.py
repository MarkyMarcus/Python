import datetime

def interestingFacts(seconds):
    print("Seconds: ", seconds)

    # TODO: Calculate minutes
    minutes = seconds // 60
    print("Minutes: ", minutes)

    # TODO: Calculate hours
    hours = minutes // 60
    print("Hours: ", hours)

    # TODO: Calculate days
    days = hours // 24
    print("Days: ", days)

    # TODO: Calculate weeks
    weeks = days // 7
    print("Weeks: ", weeks)

    # TODO: Calcualte years
    years = days // 365
    print("Years: ", years)

    # Tell the user if they can drive (16+)
    if years >= 16:
        # TODO: Print a message to the user
        print("You may drive")
    else:
        # TODO: Print a message to the user
        print("You may not drive")

    # TODO: Tell the user if they can vote (18+)
    if years >= 18:
        print("You may vote")
    else:
        print("You may not vote")

    # TODO: Tell the user if they can be predient (35+)
    if years >= 35:
        print("You may be president")
    else:
        print("You may not be president")
        

# Start with today's date
today = datetime.datetime.today()

# Use some prior date
# TODO: Update the date
birthday = datetime.datetime(2018, 11, 12) # year, month, day

# today and birthday are the number of seconds since January 1, 1970 so we must subtract birthday from today
ageInSeconds = (today - birthday).total_seconds()

# Remove decimal by converting to integer
ageInSeconds = int(ageInSeconds)

# Report interesting facts
interestingFacts(ageInSeconds)
