import datetime

def interestingFacts(seconds):
    print("Seconds: ", seconds)

    # TODO: Calculate minutes
    minutes = 
    print("Minutes: ", minutes)

    # TODO: Calculate hours
    hours = 
    print("Hours: ", hours)

    # TODO: Calculate days
    days = 
    print("Days: ", days)

    # TODO: Calculate weeks
    weeks = 
    print("Weeks: ", weeks)

    # TODO: Calcualte years
    years = 
    print("Years: ", years)

    # Tell the user if they can drive (16+)
    if years >= 16:
        # TODO: Print a message to the user
    else:
        # TODO: Print a message to the user

    # TODO: Tell the user if they can vote (18+)

    # TODO: Tell the user if they can be predient (35+)
        

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
