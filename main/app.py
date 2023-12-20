import streamlit as st
import pandas as pd

con = st.connection("snowflake")

st.title("PoCDataInput")

tab1, tab2 = st.tabs(["Form", "DB Connection"])

materialcode = tab1.number_input("MaterialCode")
projectcategory = tab1.selectbox(
    'ProjectCategory',
    ("Select",)+('savings', 'costup', 'costavoidance','noinitiative'))

subcategory_dict = {"savings": ["PN_price_negotiation","BulkManufacturing"], 
               "costup":["PN_price_negotiation"],
               "noinitiative":["noinitiative"],
               "costavoidance":["PN_price_negotiation"]}

if projectcategory:
    if projectcategory == "savings":
        subcategory = tab1.selectbox('subcategory',["Select"] + subcategory_dict["savings"])
    if projectcategory == "costup":
        subcategory = tab1.selectbox('subcategory',["Select"] + subcategory_dict["costup"])        
    if projectcategory == "noinitiative":
        subcategory = tab1.selectbox('subcategory',["Select"] + subcategory_dict["noinitiative"])
    if projectcategory == "costavoidance":
        subcategory = tab1.selectbox('subcategory',["Select"] + subcategory_dict["costavoidance"])
print(projectcategory)


projectdescription = tab1.text_area("projectdescription","It Cannot Be Blank")

if len(projectdescription) == 0:
     tab1.error("Please enter description. It cannot be blank")
else:
    if len(projectdescription) <10:
        tab1.error("Please describe in detail")
comment = tab1.text_area("Please provide additional comments if any")       
NewPriceRequestedbysupplier_basisforcostavoidance = tab1.number_input("NewPriceRequestedBySupplier",min_value = 0,max_value=10000)

submit = tab1.button("submitbutton",type="primary")

# if submit:
#     con.query(f"INSERT INTO APPTBL(MaterialCode ,ProjectCategory,SubCategory, ProjectDescription ,AdditionalComment ,NewPriceRequestedBySupplier) values ({materialcode},{projectcategory},{subcategory},{projectdescription},{comment},{NewPriceRequestedbysupplier_basisforcostavoidance})")
# df = con.query("select * from APPTBL", ttl=60)
# tab2.table(df)

if submit:
# Using parameterized query to prevent SQL injection
    query = """
        INSERT INTO APPTBL (MaterialCode, ProjectCategory, SubCategory, ProjectDescription, AdditionalComment, NewPriceRequestedBySupplier)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    # Assuming you have a database cursor named cur
    con.query(query, (materialcode, projectcategory, subcategory, projectdescription, comment, NewPriceRequestedbysupplier_basisforcostavoidance))

    # Commit the changes to the database
    con.commit()

# Fetch the data from the database table
df = con.query("SELECT * FROM APPTBL", ttl=60)
tab2.table(df)

# if submit:
#     st.write("MaterialCode",type(materialcode))
#     st.write("ProjectCategory",type(projectcategory))
#     st.write("SubCategory",type(subcategory))
#     st.write("ProjectDescription",type(projectdescription))
#     st.write("Comment",type(comment))
#     st.write("NewPriceRequestedBySupplier",type(NewPriceRequestedbysupplier_basisforcostavoidance))