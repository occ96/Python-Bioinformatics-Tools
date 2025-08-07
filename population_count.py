# Purpose: Organism population growth count

# Prompt user for organism count
organisms = int(input("Type the number of organisms in the population: "))
if (organisms < 2):
    print("Organisms in the population must be greater than 2.")
else:
    avg_percent = float(input("Please type the daily average percent of population increase: "))
    # Verifies percent is a positive, whole number or yields message
    if (avg_percent < 0):
        print("The percent of daily population increase cannot be negative")
    else:
        # Else continues loop
        days = int(input("Type the total number of days they will multiply.  "))
        # Verifies days entered by user is more than 1
        if (days <1):
            print("Total days entered must be greater than 1.")
        # Else continues loop
        else:
            # Float to ensure decimal accuracy
            organism = float(organisms)
            # Format table
            print("{:<8} {:<12}".format("DAY", "ORGANISMS"))
            print("--------------------")
            for z in range(days):
                # Print format for days in relation to organisms
                print("{:<8} {:<12}".format((z + 1), organism))
                # Continue to predict size of a population of organisms
                # Float value multipled by average increase divided by 100
                organism += ((organism * avg_percent)/100)
