import streamlit as st
import PIL
import pandas as pd
import altair as alt

st.header("MONEY SAVING CALCULATOR")
st.markdown("""
- See How much you'll have to save each day and month to reach your financial Goal.
- Set the Customized pricing to 0 when using specified targets.

""")

st.sidebar.header("SideHUT BAR")

target_amount_specified = st.sidebar.selectbox("HOW MUCH DO YOU WANT TO SAVE?",
                                               ["1k", "5k", "10k", "50k", "1lakh", "10lakhs"])
target_amount = target_amount_specified

custom_button = st.sidebar.button("ENTER CUSTOMIZED SAVINGS")
custom_amount = st.sidebar.number_input("ENTER CUSTOMIZED SAVING TARGET(Optional)", 0)
if custom_amount > 0:
    target_amount = custom_amount

target_months = st.sidebar.number_input("In how many months do you want to save it?", 1)


try:
    if "k" in target_amount:
        if target_amount == "1k":
            target_amount = 1_0_0_0
        elif target_amount == "5k":
            target_amount = 5000
        elif target_amount == "10k":
            target_amount = 10_000
        elif target_amount == "50k":
            target_amount = 50_000
        elif target_amount == "1lakh":
            target_amount = 100_000
        elif target_amount == "10lakhs":
            target_amount = 1000_000
except:
    pass


def save_per_day(monthl_savings):
    savingsperDay = monthl_savings / 29
    return savingsperDay


def save_per_month(amount, no_of_months):
    savingsPerMonth = amount / no_of_months
    return savingsPerMonth


def save_per_hour(daily_amount):
    savingsPerhour = daily_amount / 24
    return savingsPerhour


def save_per_sec(amount):
    savingsperSec = amount / 60
    return savingsperSec


savingsPerMonth = save_per_month(target_amount, target_months)
savingsPerMonth = round(savingsPerMonth)

savingsPerDAY = save_per_day(savingsPerMonth)
savingsPerDAY = round(savingsPerDAY, 2)

savingsPerHour = save_per_hour(savingsPerDAY)
savingsPerHour = round(savingsPerHour, 2)

savingsperSec = save_per_sec(savingsPerHour)
savingsperSec = round(savingsperSec, 5)

st.header("Savings You'll have to do in")
st.subheader("1. ONE MONTH")
st.write("You'll have to save  " + str('{:,}'.format(savingsPerMonth)) + "  rs Per Month.")

st.subheader("2. ONE DAY")
st.write("You'll have to save " + str('{:,}'.format(savingsPerDAY)) + "rs Per Day.")

st.subheader("3. ONE HOUR")
st.write("You'll have to save " + str('{:,}'.format(savingsPerHour)) + "rs Per Hour.")

st.subheader("3. ONE SEC")
st.write(f"You'll have to save "+ str(savingsperSec) +"rs Per Sec.")
