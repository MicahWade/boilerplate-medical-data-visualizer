import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = np.read_csv()

# 2
df['overweight'] = ((df["weight"] / df["height"]) > 25).astype(int)

# 3
# Normalize cholesterol and gluc columns
df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['id'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], var_name='variable', value_name='value')


    # 6
    df_cat = (df_cat.groupby(['cardio', 'variable', 'value'])
        .size()
        .reset_index(name='total'))
    

    # 7



    # 8
    fig = None


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
