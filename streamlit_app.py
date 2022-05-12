import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError




streamlit.title ('My Mom\'s New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



# import pandas
My_Fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#streamlit.dataframe(My_Fruit_list)
My_Fruit_list = My_Fruit_list.set_index('Fruit')


# let's put a picklist here so they pick the fruit what they want to include
Fruits_selected = streamlit.multiselect("Pick some fruits",list(My_Fruit_list.index),['Avocado','Strawberries'])
Fruits_to_show = My_Fruit_list.loc[Fruits_selected]
# display the table on the page
streamlit.dataframe(Fruits_to_show)

#create repeatable code block (called a function)
def get_fruityvise_data(this_fruit_choice):
    fruityvise_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvise_normalized = pandas.json_normalize(fruityvise_response.json())
    return fruityvise_normalized
  
#new section to display fruityvice API advise
streamlit.header('Fruityvise Fruit Advice!')
try:
  fruit_choice = streamlit.text_input('What Fruit would you like Infromation about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvise_data(fruit_choice)
    streamlit.dataframe(back_from_function)
    
except URLError as e:
  streamlit.error()
  
#import requests

#fruityvise_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


# take the json version of the data and normalize it
#fruityvise_normalized = pandas.json_normalize(fruityvise_response.json())
#output it the screen as table
#streamlit.dataframe(fruityvise_normalized)


# don't run anything past here while we trouble shoot
#streamlit.stop()



# import snowflake.connector


#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT * from fruit_load_list")
#my_data_rows = my_cur.fetchall()
#streamlit.header("The Fruit Load List Contains:")
#streamlit.dataframe(my_data_rows)

streamlit.header("The Fruit Load List Contains:")
#snowflake related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * from fruit_load_list")
        return my_cur.fetchall()

# Add a button to load the fruit
if streamlit.button('Get fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)

#streamlit.stop()
    
    
# allow end user to add fruit to list
#-- add_my_fruit = streamlit.text_input('What Fruit would you like to add ?','jackfruit')
#-- streamlit.write('Thanks for Adding ',add_my_fruit)

#This will not work correctly, but just go with it for now
#-- my_cur.execute("insert into fruit_load_list values ('from stramlit')")


# allow end user to add fruit to list
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('from streamlit')")
        return "Thanks for adding  " + new_fruit

add_my_fruit = streamlit.text_input('What Fruit would you like to add ?')
if streamlit.button('Add a Fruit to the List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_function)

    
streamlit.stop() 
