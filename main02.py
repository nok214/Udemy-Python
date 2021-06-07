import streamlit as st
import numpy as np
import pandas as pa
from PIL import Image

#テキスト表示
st.title('左右のカラム分け')

#左右２つのカラム設定
left_column, right_column = st.beta_columns(2)

#ボタン作成
btn = left_column.button('右カラムに表示')

#ボタンが押されたとき
if btn:
    #右カラムにテキスト表示する
    right_column.write('右カラム')

#
expander1 = st.beta_expander('問い合わせ')

#
expander1.write('内容表示')

#
expander2 = st.beta_expander('問い合わせ')

#
expander2.write('内容表示')
expander2.write('内容表示')