# 1. 生成模拟数据 (simulate_data.py)
import pandas as pd
import numpy as np

np.random.seed(42)
n = 1000

data = {
    'age': np.random.randint(18, 70, n),
    'constipation_freq': np.random.randint(0, 8, n),  # 每周便秘天数
    'stress_level': np.random.randint(1, 6, n),       # 1-5分
    'water_intake': np.random.randint(0, 4, n),       # 每日饮水杯数（0=几乎不喝）
    'fiber_intake': np.random.randint(0, 4, n)        # 蔬果摄入频率
}

df = pd.DataFrame(data)

# 简单规则定义风险（模拟“专家知识”）
df['risk_score'] = (
    df['constipation_freq'] * 0.4 +
    (5 - df['water_intake']) * 0.3 +
    (5 - df['fiber_intake']) * 0.2 +
    (df['stress_level'] > 3) * 0.1
)
df['risk_level'] = pd.cut(df['risk_score'], bins=[-1, 1.5, 2.5, 10], labels=[0, 1, 2])  # 0=低, 1=中, 2=高

df.to_csv('gut_health_data.csv', index=False)