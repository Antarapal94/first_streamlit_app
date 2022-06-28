#created by the main python file.
import streamlit
streamlit.title('MY Parents new healthy diner')
streamlit.header('🥝Breakfast menu')
streamlit.text('🥝omega3 & Blueberry Oatmeal')
streamlit.text('🥝kale, spinach &Rocket smothie')
streamlit.text('🥝Hard boiled Free-range egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_lists= pandas.read_csv ("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
my_fruit_list = my_fruit_list.set_index('Fruit')

# Display the table on the page.
streamlit.dataframe(my_fruit_lists)
