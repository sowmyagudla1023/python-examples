def years(limak,bob):
    year=0
    while limak<=bob:
        limak*=3
        bob*=2
        year+=1
    return year
limak=3
bob=5
years_needed=years(limak,bob)
print(years_needed)
