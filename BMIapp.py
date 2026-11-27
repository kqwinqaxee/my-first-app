import streamlit as st

st.markdown("# :rad [แอปพลิเคชั่นคำนวณค่า BMI⚖️]")
st.write("กรอกข้อมูลน้ำหนักและส่วนสูงของคุณ")
 
weight = st.number_input("กรอกน้ำหนักของคุณ (kg) :", min_value=1.0, value=1.0)
height_cm = st.number_input("กรอกส่วนสูงของคุณ (cm):", min_value=1.0, value=1.0)

if st.button("คำนวณค่า bmi"):
  
   height_m = height_cm / 100
   bmi = weight / (height_m ** 2)

   st.write("...")
   st.header(f"ค่า BMI ของคุณคือ: **{bmi:.2f}**")

   if bmi < 18.5:
      st.warning("คุณมีน้ำหนักน้อยกว่าเกณฑ์(ผอม)🥗 ")
   elif 18.5 <= bmi < 23.0:
      st.success("คุณมีน้ำหนักอยู่ในเกณฑ์ปกติ(สุขภาพดี)✅ ")
   elif 23.0 <= bmi < 25.0:
      st.info("คุณเริ่มมีน้ำหนักเกินเกณฑ์(ท้วม)🏋️")
   else:
      st.error("คุณมีน้ำหนักเกินเกณฑ์ ควรรักษาสุขภาพ⚠️")

   st.divider()
st.write("น.ส.กวินปวีณ์ ปราณี เลขที่ 9 ม.4/5")
