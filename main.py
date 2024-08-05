import plotly.graph_objects as go

# Create figure
fig = go.Figure(layout=go.Layout())
newx = []
newy = []
labels = ['Oil', 'Gas', 'Water']
values = [[4500, 2500, 1053], [1, 2, 3], [3, 4, 5], [5, 6, 7], [4, 2, 1], [1, 2, 3], [3, 4, 5], [5, 6, 7], [4, 2, 1]]
scatterx = [0.2, 0.5, 1, 2, 2.2, 3]
scattery = [1.23, 2.5, 0.42, 3, 1, 5]
# Add trace
fig.add_trace(
    go.Scatter(x=scatterx, y=scattery),)

for i in range(len(scatterx)):
    newx.append(max(scatterx)*(scatterx[i]/(max(scatterx)*max(scatterx))))

for i in range(len(scattery)):
    newy.append(max(scattery)*(scattery[i]/max(scattery) ** 2))

for i in range(len(scatterx)):
    if scatterx[i] < .9 and scattery[i] < .9:
        print(newx[i], newy[i], '1')
        fig.add_trace(
            go.Pie(domain={'x': [0 + newx[i], 0 + newx[i]+.1], 'y': [0 + newy[i], 0 + newy[i]+.1]}, labels=labels, values=values[i])
            )

    elif newx[i] < .9 <= newy[i]:
        print(newx[i], newy[i], '2')
        fig.add_trace(
            go.Pie(domain={'x': [0 + newx[i], 0 + newx[i]], 'y': [0 + newy[i] - .1, 0 + newy[i]]}, labels=labels, values=values[i])
            )

    elif newx[i] >= .9 > newy[i]:
        print(newx[i], newy[i], '3')
        fig.add_trace(
            go.Pie(domain={'x': [0 + newx[i] - .1, 0 + newx[i]], 'y': [0 + newy[i]-.1, 0 + newy[i]]}, labels=labels, values=values[i])
            )

    elif newx[i] <= 0.1 < newy[i]:
        print(newx[i], newy[i], '4')
        fig.add_trace(
            go.Pie(domain={'x': [0, 0 + newx[i]], 'y': [0 + newy[i]-.1, 0 + newy[i]]}, labels=labels, values=values[i])
            )

    elif newx[i] > .1 >= newy[i]:
        print(newx[i], newy[i], '5')
        fig.add_trace(
            go.Pie(domain={'x': [0 + newx[i], 0 + newx[i]+.1], 'y': [0 + newy[i], 0 + newy[i]+.1]}, labels=labels, values=values[i])
            )

    elif newx[i] >= .9 < newy[i]:
        print(newx[i], newy[i], '6')
        fig.add_trace(
            go.Pie(domain={'x': [0 + newx[i] - .1, 0 + newx[i]], 'y': [0 + newy[i]-.1, 0 + newy[i]]}, labels=labels, values=values[i])
            )

    else:
        print(newx[i], newy[i], '7')
        fig.add_trace(
            go.Pie(domain={'x': [0 + newx[i]-.1, 0 + newx[i]], 'y': [0 + newy[i]-.1, 0 + newy[i]]}, labels=labels,
                   values=values[i])
        )

# Add images
fig.add_layout_image(
    dict(
        source="https://images.plot.ly/language-icons/api-home/python-logo.png",
        xref='x', yref='y',
        x=0, y=7600,
        sizex=16000, sizey=4400,
        sizing="stretch",
        opacity=0.5,
        layer="below")
)

# Set templates
fig.update_layout(template="plotly_white")

fig.show()
