# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any

import numpy as np

import streamlit as st
from streamlit.hello.utils import show_code
import pandas as pd
import numpy as np
import altair as alt



st.set_page_config(page_title="Linear Regression")
st.image('images/reg.png')


st.write(
    """
    In this section we are performing linear regression to the famous marketing datase. 
    As a Bussines Inetelligence / Data Ananlyst there is a good chance that we are going to encounter 
    similar problems like this. 
"""
)

st.markdown("### What is Linear Regression")
st.write("""
    $$Y = mx+b$$
""")

st.write("""
We are xploring this dataset to see if
* Is there a relationship betwen sales and adverising? 
* How strong is the relationship? 
* Whcih media is assocaited with sales?
* How large is the association between each medium
* How accuralty can we predict future sales?
* Is the relatiionship linear? 
* Is there synergies 


""")




st.write("""
    ### Problmes with linear regression. 
    * Linear assumption
    * Outliers
    
""")

ad_data = pd.read_csv('data/Advertising.csv').set_index("Unnamed: 0")
st.dataframe(ad_data.head())

chart = alt.Chart(ad_data).mark_point().encode(
    x='TV',
    y='sales'
).interactive()
st.altair_chart(
    chart,  theme="streamlit", use_container_width=True
)


##########################

Boston = load_data("Boston")
Boston.columns