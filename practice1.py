import pandas as pd
import matplotlib.pyplot as plt

# 日本語フォント設定
plt.rcParams["font.family"] = "MS Gothic"

# 1. 読み込み（シンプルに読み込む）
df = pd.read_csv("Game Results JP".csv)
# こう書く（コードと同じフォルダにCSVを置く場合）

# 2. 列名の掃除（ここで "スコア" が '"スコア"' になっていても、一括で剥ぎ取る）
df.columns = df.columns.str.replace('"', '').str.strip()

# 【重要】もしこれでも「スコア」が見つからないなら、番号で無理やり名前を付ける
# 送ってくれたデータでは「スコア」は 8 番目にあるので、index[7] を指定
df.rename(columns={df.columns[7]: "スコア"}, inplace=True)

# 3. 認識した列名を一応表示（ここで「スコア」があればOK）
print("認識した列名一覧:", df.columns.tolist())

# 4. 型変換（エラーが出ないように慎重に）
df["スコア"] = pd.to_numeric(df["スコア"], errors='coerce').fillna(0).astype("int32")

# 5. グループ化と表示
# 「日付」も同様に番号(index[1])で強制指定しておくと安心
df.rename(columns={df.columns[1]: "日付"}, inplace=True)

daily = df.groupby("日付")
for date, group in daily:
    print(f"\n--- 日付: {date} ---")
    for row in group.itertuples():
        # itertuplesの属性名でも「・」は「_」に変わるので getattr を使う
        try:
            hv = getattr(row, "ホーム_ビジター")
            if hv == "ビジター":
                print(f"球団: {row.球団}, スコア: {row.スコア}")
        except AttributeError:
            # 万が一属性名が違った場合、列番号で直接指定
            if row[6] == "ビジター": 
                print(f"球団: {row[5]}, スコア: {row[8]}")

# --- 設計図の処理スタート ---

# 1. 各「球団」別にグループ分けして、スコアの平均を計算する
# これで「球団ごとの平均得点」が一気に計算されます
team_avg = df.groupby("球団")["スコア"].mean()

# 2. 12球団のランキングに並べ替える（得点が高い順：ascending=False）
team_ranking = team_avg.sort_values(ascending=False)

# 3. 「球団」と「平均得点」を並べて出力
print("\n===== 1試合あたりの平均得点ランキング =====")
print(team_ranking)

# 4. 【おまけ】ランキングを棒グラフにして可視化する
plt.figure(figsize=(12, 6))
team_ranking.plot(kind='bar', color='orange', edgecolor='black')

plt.title("2025年 球団別・平均得点ランキング")
plt.xlabel("球団名")
plt.ylabel("平均得点（1試合あたり）")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()