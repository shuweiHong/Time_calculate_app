# work_time_app.py
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="雷雨的专属工作时长计算器", page_icon="⏰")

st.title("🕒 雷雨的专属工作时长计算器")

st.markdown("请亲爱的输入以下时间：")

start_time = st.time_input("上班开始时间", value=datetime.strptime("07:00", "%H:%M").time())
break_start = st.time_input("午休开始时间", value=datetime.strptime("12:00", "%H:%M").time())
break_end = st.time_input("午休结束时间", value=datetime.strptime("13:00", "%H:%M").time())
end_time = st.time_input("下班时间", value=datetime.strptime("17:00", "%H:%M").time())

if st.button("计算总工作时间"):
    today = datetime.today().date()
    t1 = datetime.combine(today, start_time)
    t2 = datetime.combine(today, break_start)
    t3 = datetime.combine(today, break_end)
    t4 = datetime.combine(today, end_time)

    total_work = (t2 - t1) + (t4 - t3)
    hours, remainder = divmod(total_work.seconds, 3600)
    minutes = remainder // 60

    st.success(f"亲爱的你今天总共工作了 **{hours} 小时 {minutes} 分钟**。")
