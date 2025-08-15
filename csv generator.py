import streamlit as st
import pandas as pd
import random as rm

st.title('YOUR CSV GENERATOR')

# Rows input

a1, a2 = st.columns(2)
a1.write('Enter the number of rows')
rows = a2.number_input('Number of rows', min_value=1, max_value=10000, value=5)

# Amount range
b1, b2, b3 = st.columns(3)
b1.write('Specify the range for amount column')
amount_min = b2.number_input('Min amount', 1, 10, 1)
amount_max = b3.number_input('Max amount', 10, 1000, 10)

# Column name for field values
field_col_name = st.text_input('Enter field name (like City or Region)', placeholder='City')

# Field values
c1, c2, c3 = st.columns(3)
c1.write('Enter the possible values for the field')
value1 = c1.text_input("", placeholder='Value1')
value2 = c2.text_input("", placeholder='Value2')
value3 = c3.text_input("", placeholder='Value3')

# Generate CSV Button
if st.button('Generate CSV'):
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

    st.write(df)

    # Download
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name='generated_data.csv',
        mime='text/csv',
    )
