import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Cài đặt giao diện trang web
st.set_page_config(page_title="Production Plan", layout="wide")

# Tiêu đề chính của Dashboard
st.title("🏢 2027 PRODUCTION AND PURCHASING PLAN")

# 1. Input data from the Case Study
bom_data = [
    {"item": "Substrate", "qty_per_cpu": 1, "price_usd": 3.0},
    {"item": "Capacitor A", "qty_per_cpu": 10, "price_usd": 0.1},
    {"item": "Capacitor B", "qty_per_cpu": 4, "price_usd": 0.1},
    {"item": "Solder ball", "qty_per_cpu": 30, "price_usd": 0.05},
    {"item": "Die", "qty_per_cpu": 1, "price_usd": 10.0}
]

cpu_per_quarter = 1_000_000
quarters_per_year = 4
total_cpu_2027 = cpu_per_quarter * quarters_per_year

# 2. Calculate the order date for Q1/2027
start_production_date = datetime(2027, 1, 1)
lead_time_weeks = 5
order_deadline_q1 = start_production_date - timedelta(weeks=lead_time_weeks)

# ---- HIỂN THỊ LÊN DASHBOARD ----

st.header("🗓️ 1. Kế hoạch Thời gian (Timeline)")
col1, col2 = st.columns(2)
with col1:
    st.info(f"**Ngày bắt đầu sản xuất (Full Capacity):**\n\n {start_production_date.strftime('%Y-%m-%d')}")
with col2:
    st.error(f"**Hạn chót đặt hàng cho Q1 (Lead time 5 tuần):**\n\n {order_deadline_q1.strftime('%Y-%m-%d')}")

st.header("📊 2. Kế hoạch Ngân sách và Số lượng (BOM)")
st.write(f"Mục tiêu sản xuất: **{total_cpu_2027:,} CPU** trong năm 2027 ({cpu_per_quarter:,} CPU/Quý)")

# Chuyển dữ liệu BOM thành bảng và hiển thị
df_bom = pd.DataFrame(bom_data)
# Thêm cột tổng tiền
df_bom['total_cost_usd_per_cpu'] = df_bom['qty_per_cpu'] * df_bom['price_usd']
df_bom['total_budget_2027'] = df_bom['total_cost_usd_per_cpu'] * total_cpu_2027

# Hiện bảng dữ liệu tuyệt đẹp
st.dataframe(df_bom, use_container_width=True)

# Tính tổng ngân sách
total_budget = df_bom['total_budget_2027'].sum()
st.success(f"💰 **TỔNG NGÂN SÁCH DỰ KIẾN 2027: ${total_budget:,.2f}**")
