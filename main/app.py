import streamlit as st
import pandas as pd

st.title("PoCDataInput")

materialcode = st.text_input("MaterialCode", "Enter Material Code")
projectcategory = st.selectbox(
    'ProjectCategory',
    ("Select",)+('savings', 'costup', 'costavoidance','noinitiative'))

subcategory_dict = {"savings": ["PN_price_negotiation","BulkManufacturing"], 
               "costup":["PN_price_negotiation"],
               "noinitiative":["noinitiative"],
               "costavoidance":["PN_price_negotiation"]}

if projectcategory:
    if projectcategory == "savings":
        subcategory = st.selectbox('subcategory',["Select"] + subcategory_dict["savings"])
    if projectcategory == "costup":
        subcategory = st.selectbox('subcategory',["Select"] + subcategory_dict["costup"])        
    if projectcategory == "noinitiative":
        subcategory = st.selectbox('subcategory',["Select"] + subcategory_dict["noinitiative"])
    if projectcategory == "costavoidance":
        subcategory = st.selectbox('subcategory',["Select"] + subcategory_dict["costavoidance"])
print(projectcategory)


projectdescription = st.text_area("projectdescription","It Cannot Be Blank")

if len(projectdescription) == 0:
     st.error("Please enter description. It cannot be blank")
else:
    if len(projectdescription) <10:
        st.error("Please describe in detail")
comment = st.text_area("Please provide additional comments, if any")       
NewPriceRequestedbysupplier_basisforcostavoidance = st.number_input("NewPriceRequestedBySupplier",min_value = 0,max_value=10000)

submit = st.button("submitbutton",type="primary")

if submit:
    
