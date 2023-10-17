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

import time

import numpy as np

import streamlit as st
from streamlit.hello.utils import show_code

import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn import decomposition
import altair as alt






st.set_page_config(page_title="Clustering", page_icon="📈")
st.markdown("# Clustering Techniques")

st.write(
    """
    One of the main jobs of a Marketing Analysr is to suceesfully create marketing campingg for the target audience.
    In order to do this we need to have a deep undestanding of the customerds and their needs. However, each costumer has 
    their own background, culturees, gruop and undertanding costumer needs become difficutl, specially if businnes have millions of customers.
    
    ### Solution:
     Costumer Segmentation
     * Customer segmentations lets you divided custimer into few segments and undertaind their chatracyeristics 
    
    
"""
)


mall_data = pd.read_csv('data/Mall_Customers.csv')
st.dataframe(mall_data.head())


