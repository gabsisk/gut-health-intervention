# 3. app.py
import streamlit as st
import joblib
import pandas as pd

# 加载模型
model = joblib.load('gut_health_model.pkl')

# 页面标题
st.set_page_config(page_title="肠道健康风险评估", layout="centered")
st.title("🌱 肠道健康风险评估助手")
st.markdown("填写简单问卷，获取个性化健康建议")

# 用户输入
age = st.slider("年龄", 18, 70, 30)
constipation = st.slider("每周便秘天数", 0, 7, 2)
stress = st.select_slider("压力水平", options=[1, 2, 3, 4, 5], value=3)
water = st.select_slider("每日饮水杯数（约250ml/杯）", options=[0, 1, 2, 3, 4], value=2)
fiber = st.select_slider("每日蔬果摄入次数", options=[0, 1, 2, 3, 4], value=2)

# 预测按钮
if st.button("评估我的肠道健康风险"):
    # 构造输入
    input_data = pd.DataFrame([{
        'age': age,
        'constipation_freq': constipation,
        'stress_level': stress,
        'water_intake': water,
        'fiber_intake': fiber
    }])
    
    # 预测
    pred = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0]
    
    # 风险映射
    risk_labels = {0: "低风险", 1: "中风险", 2: "高风险"}
    risk_colors = {0: "🟢", 1: "🟡", 2: "🔴"}
    
    st.subheader(f"{risk_colors[pred]} 您的肠道健康风险：{risk_labels[pred]}")
    
    # 个性化建议（规则引擎）
    suggestions = []
    
    if constipation >= 3:
        suggestions.append("💡 便秘较频繁，建议增加膳食纤维（如燕麦、奇亚籽、西梅）")
    if water <= 1:
        suggestions.append("💧 饮水不足！建议每日至少饮用1.5L水（约6杯）")
    if fiber <= 1:
        suggestions.append("🥬 蔬果摄入较少，建议每餐包含1拳头蔬菜")
    if stress >= 4:
        suggestions.append("🧘 压力可能影响肠道功能，尝试每天10分钟深呼吸或冥想")
    
    if not suggestions:
        suggestions = ["✅ 当前习惯良好！继续保持均衡饮食与规律作息"]
    
    st.markdown("### 📝 个性化建议")
    for s in suggestions:
        st.write(s)
    
    st.markdown("⚠️ 本工具仅用于健康科普，不替代医疗建议")