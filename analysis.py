import pandas as pd

gold_data = pd.read_csv("gold.csv")

date = gold_data["Date"]
one_g_of_24k = gold_data["1g of 24k gold"]
num_of_data = one_g_of_24k.size

def one_day_inc_in_24k_price():
    todays_price = one_g_of_24k[0]
    yesterday_price = one_g_of_24k[1]
    diff =  todays_price-yesterday_price
    value = abs(diff)
    if diff < 0:
      return "The price of 1g of 24k gold decreased by " + str(value)

    if diff > 0:
      return "The price of 1g of 24k gold increased by " + str(value)

    if diff == 0:
      return "There is no price difference in 1g of 24k gold"

diff = one_day_inc_in_24k_price()
print(diff)
