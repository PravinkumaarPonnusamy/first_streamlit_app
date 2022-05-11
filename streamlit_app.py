import streamlit

streamlit.title ('My Mom\'s New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



import pandas
My_Fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#streamlit.dataframe(My_Fruit_list)
My_Fruit_list = My_Fruit_list.set_index('Fruit')


# let's put a picklist here so they pick the fruit what they want to include
Fruits_selected = streamlit.multiselect("Pick some fruits",list(My_Fruit_list.index),['Avocado','Strawberries'])
Fruits_to_show = My_Fruit_list.loc[Fruits_selected]
# display the table on the page
streamlit.dataframe(Fruits_to_show)


#new section to display fruityvice API advise
streamlit.header('Fruityvise Fruit Advice!')
import requests
fruityvise_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvise_response.json())
