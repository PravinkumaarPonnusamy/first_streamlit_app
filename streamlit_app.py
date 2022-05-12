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


fruit_choice = streamlit.text_input('What Fruit would you like Infromation about?','kiwi')
streamlit.write('the user entered',fruit_choice)


streamlit.header('Fruityvise Fruit Advice!')
import requests
fruityvise_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


# take the json version of the data and normalize it
fruityvise_normalized = pandas.json_normalize(fruityvise_response.json())
#output it the screen as table
streamlit.dataframe(fruityvise_normalized)


import snowflake.connector


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The Fruit Load List Contains:")
streamlit.dataframe(my_data_rows)



# allow end user to add fruit to list
add_my_fruit = streamlit.text_input('What Fruit would you like to add ?','jackfruit')
streamlit.write('Thanks for Adding ',add_my_fruit)



my_cur.execute("insert into fruit_load_list values ('from stramlit')")
