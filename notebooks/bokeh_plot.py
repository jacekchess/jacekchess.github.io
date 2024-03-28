from bokeh.io import output_file
import pandas as pd
from distinctipy import get_colors
import numpy as np
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure, show

output_file("bokeh_plot.html")

data = pd.read_csv('../socialdata2024/files/Police_Department_Incident_Reports__Historical_2003_to_May_2018_20240210.csv')
data['Datetime'] = pd.to_datetime(data['Date'] + ' ' + data['Time'])
data = data.loc[data['Datetime'] < '2018-01-01 00:00:00']
data['Hour'] = data['Datetime'].apply(lambda x: x.hour)

focuscrimes = set(['WEAPON LAWS', 'PROSTITUTION', 'DRIVING UNDER THE INFLUENCE', 'ROBBERY', 'BURGLARY', 'ASSAULT', 'DRUNKENNESS', 'DRUG/NARCOTIC', 'TRESPASS', 'LARCENY/THEFT', 'VANDALISM', 'VEHICLE THEFT', 'STOLEN PROPERTY', 'DISORDERLY CONDUCT'])
data_focus = data.loc[data['Category'].isin(focuscrimes)]

data_count = data_focus[['PdId', 'Category', 'Hour']].groupby(['Category', 'Hour']).count()
data_count = data_count.reset_index(level=['Category'])
data_count = data_count.pivot(columns='Category', values='PdId')
data_count = data_count/data_count.sum()

colors = ['#%02x%02x%02x' % (int(r*255), int(g*255), int(b*255)) for r, g, b in get_colors(14)]

source = ColumnDataSource(data_count)
p = figure(x_range = FactorRange(factors=np.arange(25).astype(str)))

bar = {}
for indx, i in enumerate(focuscrimes):
    bar[i] = p.vbar(x='Hour', top=i, source=source, legend_label=i, muted_alpha=0.05, muted=True, color=colors[indx])

p.legend.click_policy="mute"
show(p)