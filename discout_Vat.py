import streamlit as st
st.title("แอปพลิเคชันคำนวณส่วนลดสินค้าและ 

price = st.number_input("กรอกราคาเต็มของสินค้า (บาท):", min_value=0.0, value=0.0)
sale = st.number_input(
    "กรอกเปอร์เซ็นต์ส่วนลด (%):", min_value=0.0, max_value=100.0, value=0.0
)

discount = price * sale / 100
vat = (price - discount) * 0.07
netprice = (price - discount) + vat

st.header(f"ราคาสินค้า: **{price:.2f}** บาท (ส่วนลด **{sale:.0f}%**)")
st.header(f"ส่วนลดที่คำนวณได้: **{discount:.2f}** บาท")
st.header(f"ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
st.header(f"ราคาสุทธิที่ต้องจ่าย: **{netprice:.2f}** บาท")

st.divider()
st.write("น.ส.กวินปวีณ์ ปราณี เลขที่ 9 ม.4/5")
