import streamlit as st

st.title("💰 Price Calculator")

# Input fields
unit_cost = st.number_input("Unit Cost", min_value=0.0, format="%.2f")
quantity = st.number_input("Quantity", min_value=0.0, format="%.0f")
profit_percent = st.number_input("Profit Percent (%)", min_value=0.0, format="%.2f")
tax_percent = st.number_input("Tax Percent (%)", min_value=0.0, format="%.2f")
vat_percent = st.number_input("VAT Percent (%)", min_value=0.0, format="%.2f")

# Calculate button
if st.button("Calculate Final Price"):
    try:
        total_cost = unit_cost * quantity
        profit = (profit_percent / 100) * total_cost
        tax = (tax_percent / 100) * (total_cost + profit)
        vat = (vat_percent / 100) * (total_cost + profit + tax)

        final_price = '₦{:,.0f}'.format(total_cost + profit + tax + vat)

        st.success(f"Final Price: {final_price}")
    except Exception:
        st.error("Invalid input. Please enter numeric values.")