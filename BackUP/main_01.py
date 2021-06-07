import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('streamlit_超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目':[1, 2, 3, 4],
    '2列目':[10, 20, 30, 40]
})

st.table(df.style.highlight_max(axis=0))

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

chart = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(chart)

st.write('Display Image')

img = Image.open('Oniroku.jpg')

st.image(img, caption='鬼六', use_column_width=True)