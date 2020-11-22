# first main will be executed
from motion_detector import df

from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df['Start_str'] = df['Start'].dt.strftime('%Y-%m-%d %H:%M:%S')
df['End_str'] = df['End'].dt.strftime('%Y-%m-%d %H:%M:%S')

cds = ColumnDataSource(df)

f = figure(x_axis_type='datetime', height=100, title='Motion Graph')
f.yaxis.minor_tick_line_color = None
f.yaxis[0].ticker.desired_num_ticks = 1

hover = HoverTool(tooltips=[("Start","@Start_str"),('End','@End_str')])
f.add_tools(hover)

q = f.quad(left='Start', right='End', bottom=0, top=1, color='green',source=cds)

output_file('output.html')
show(f)
