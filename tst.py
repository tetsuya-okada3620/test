import numpy as np
import pandas as pd

# NumPyで乱数データを生成
rng = np.random.default_rng(seed=42)
data1 = rng.integers(0, 100, size=(5, 3))
data2 = rng.standard_normal((5, 3))

# DataFrameに変換
df1 = pd.DataFrame(data1, columns=["A", "B", "C"])
df2 = pd.DataFrame(data2, columns=["D", "E", "F"])

# 横方向に連結
df_concat = pd.concat([df1, df2], axis=1)

# 結果を表示
print("=== df1 (整数乱数) ===")
print(df1)
print()
print("=== df2 (正規分布乱数) ===")
print(df2)
print()
print("=== 連結結果 ===")
print(df_concat)

# CSVファイルとして出力
df_concat.to_csv("output.csv", index=False)
print()
print("output.csv に保存しました")
