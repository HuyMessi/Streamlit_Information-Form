import streamlit as st

st.title("📋Form đăng ký thông tin cá nhân")
frm_thong_tin = st.form("form_thong_tin")
with frm_thong_tin:
    st.header("🔷Nhập thông tin của bạn")
    ho_ten = st.text_input("Họ và tên:")
    email = st.text_input("Email:")
    ngay_sinh = st.text_input("Ngày sinh:", placeholder="DD/MM/YYYY")
    gioi_tinh = st.radio("Giới tính:", ["Nam", "Nữ", 'Khác'])
    nghe_nghiep = st.selectbox("Nghề nghiệp", ["Học sinh", "Sinh viên", "Đi làm"], index=None)
    so_thich = st.multiselect("Sở thích", ["Lập trình", "Chơi game","Bắn bida", "Đọc sách"])
    gioi_thieu = st.text_area("Giới thiệu bản thân:", placeholder="Viết vài dòng ngắn gọn về bạn...")
    onClick = st.form_submit_button("✅Gửi thông tin")
if onClick:
    st.markdown(f'''
                <b>Thông tin bạn vừa nhập là:</b> <br>
                <b>Họ và tên:</b> {ho_ten} <br>
                <b>Email:</b> {email} <br>
                <b>Ngày sinh:</b> {ngay_sinh} <br>
                <b>Giới tính:</b> {gioi_tinh} <br>
                <b>Nghề nghiệp:</b> {nghe_nghiep} <br>
                <b>Sở thích:</b> {', '.join(so_thich)} <br>
                <b>Giới thiệu bản thân:</b> <br>{gioi_thieu}
                ''', True)
    
    