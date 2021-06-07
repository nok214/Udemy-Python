import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

#タイトル
st.title('streamlit_超入門')

#テキスト表示
st.write('DataFrame')

#表の作成
df = pd.DataFrame({
    '1列目':[1, 2, 3, 4],
    '2列目':[10, 20, 30, 40]
})

#作成した表の表示(最大値のハイライトオプション付き)
st.table(df.style.highlight_max(axis=0))

#"""で囲う表示の仕方もある,```pythonで記述内容をコードとして表示することもできる
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""
#棒グラフの作成
chart_bar = pd.DataFrame(
    np.random.rand(20, 5),
    columns =['A', 'B', 'C', 'D', 'E']
)

#マップの作成
chart_map = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

#作成したグラフの表示
st.map(chart_map)
st.bar_chart(chart_bar)

#テキスト表示
st.write('Display Image')

#画像の読み込み
img01 = Image.open('img/Oniroku_01.jpg')
img02 = Image.open('img/Oniroku_02.jpg')

#読み込んだ画像の表示
st.image(img01, caption='鬼六', use_column_width=True)

#チェックボックスの作成(チェックしたら画像表示するオプション付き)
if st.checkbox('鬼六チェック'):
    st.image(img02, caption='鬼六', use_column_width=True)

#セレクトボックスを作成(1～10までの数字)
num_list = st.selectbox(
    '好きな数字を選んで下さい',
    list(range(1, 11))
)

#選択した数字を表示
st.write('あなたの好きな数字は', num_list, 'です。')

#テキスト表示
st.write('Interactive Widgets')

#テキスト入力ボックス作成
tx_input = st.text_input('あなたの名前を教えてください')

#入力したテキスト表示
st.write('あなたの名前は', tx_input, 'ですか？')

#スライドバー作成
slid_input = st.slider('調子はどうですか？', 0, 100, 50)

#スライドの値を表示
st.write('あなたのコンディション：', slid_input)

#**************************************** サイドバーで表示

#セレクトボックスを作成(1～10までの数字)
num_list = st.sidebar.selectbox(
    'what youre favorite number?',
    list(range(1, 11))
)

#テキスト入力ボックス作成
tx_input_side = st.sidebar.text_input('Please tell youre name?')

#スライドバー作成
slid_input_side = st.sidebar.slider('How are you?', 0, 100, 50)

#******************************************

#選択した数字を表示
st.write('you choosed', num_list, '!!')

#入力したテキスト表示
st.write('youre...', tx_input_side, '？')

#スライドの値を表示
st.write('youre condition：', slid_input_side)

#テキスト表示
st.write('Progress Bar')

#変数に空の値を入れる
latest_iteration = st.empty()

#プログレスバーを作成(0→100の数値)
bar = st.progress(0)

#繰り返し(iが0から99になるまで)
for i in range(100):
    #f-stringを使用し、Latest_iterationの数値を+1更新する
    latest_iteration.text(f'iteration {i + 1}')

    #プログレスバーの値を+1更新する
    bar.progress(i +1)

    #0.1秒止める
    time.sleep(0.1)
