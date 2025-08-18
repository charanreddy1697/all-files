import streamlit as st
import pandas as pd
import random as rm

st.title('CSV GENERATOR')

# Rows input

rows = st.number_input('Enter the number of rows', min_value=1, max_value=10000, value=5)
st.write('Specify the range for amount column')
# Amount range
b1, b2 = st.columns(2)
amount_min = b1.number_input('Min amount', 1, 10000, 1)
amount_max = b2.number_input('Max amount', 10, 1000000000000, 10)

# Column name for field values
field_col_name = st.text_input('Enter field name (like City or Region)', placeholder='City')

c1, c2, c3 = st.columns(3)
# Field values

value1 = c1.text_input("Value1", placeholder='city1')
value2 = c2.text_input("Value2", placeholder='city2')
value3 = c3.text_input("Value3", placeholder='city3')


a1,a2 = st.columns(2)
# Generate CSV Button

if a1.button('Generate CSV'):
    ids = []
    fields = []
    amounts = []

    for i in range(1, rows + 1):
        ids.append(i)
        fields.append(rm.choice([value1, value2, value3]))
        amounts.append(rm.randint(amount_min, amount_max))

    df = pd.DataFrame({
        "ID": ids,
        field_col_name: fields,
        "Amount": amounts
    })
    st.write('displaying top 5 rows')
    st.write(df.head())
    


    
    # Count repetitions
    st.write('### Repetitions of each value')
    v1 = df.groupby(field_col_name)['ID'].count()
    st.write(v1)
    
    # Download
    csv = df.to_csv(index=False)
    a2.download_button(
        label="Download CSV",
        data=csv,
        file_name='generated_data.csv',
        mime='text/csv',
    )
