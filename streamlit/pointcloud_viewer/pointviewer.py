
from inspect import trace
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go


data1 = pd.DataFrame(np.random.random((50000,3)))
data2 = pd.DataFrame(np.random.random((50000,3)))


trace1 = [go.Scatter3d(x=data1[0], y=data1[1], z=data1[2])]
trace2 = [go.Scatter3d(x=data2[0], y=data2[1], z=data2[2])]

layout = go.Layout(
    title="Pointcloud Viewer",
    scene = go.layout.Scene(
        aspectmode='manual',
        aspectratio=go.layout.scene.Aspectratio(
            x=1,y=1,z=0.5
        ),
        xaxis=dict(
            title="X axis",
            backgroundcolor='rgb(50,50,50)',
            gridcolor="rgba(100,100,100,100)",
            showbackground=True,
            zerolinecolor="white",
            showspikes=False,
            range=[0,200],
            dtick=20
        ),
        yaxis=dict(
            title="Y axis",
            backgroundcolor='rgb(50,50,50)',
            gridcolor="rgba(100,100,100,100)",
            showbackground=True,
            zerolinecolor="white",
            showspikes=False,
            range=[-100,100],
            dtick=20

        ),
        zaxis=dict(
            backgroundcolor='rgb(50,50,50)',
            gridcolor="rgba(100,100,100,10)",
            showbackground=True,
            zerolinecolor="rgb(100,100,100)",
            showspikes=False,
            range=[0,5.0]

        )
    ),
    paper_bgcolor= 'rgb(50,50,50)',
)

fig = go.Figure(layout=layout)

fig_trace1 = fig.add_trace(
    go.Scatter3d(
        x=data1[0]*200,
        y=data1[1]*100,
        z=data1[2]-0.5,
        mode="markers",
        opacity=0.5,
        marker=dict(
            size=2,
            line=dict(
                width=0.1
            )
        ),
        name="Opacity 0.5"
    )
)

fig_trace1 = fig.add_trace(
    go.Scatter3d(
        x=data2[0]*200,
        y=data2[1]*-100,
        z=data2[2]-0.5,
        mode="markers",
        opacity=1.0,
        marker=dict(
            size=2,
            line=dict(
                width=0.1
            )
        ),
        name="Opacity 1.0"
    )
)

#fig.update_zaxes(gridcolor="gray", griddash="dash", minor_griddash="dot")


fig.update_layout(height=800, width=1200)
#st.plotly_chart(fig, height=1200)
st.plotly_chart(fig)