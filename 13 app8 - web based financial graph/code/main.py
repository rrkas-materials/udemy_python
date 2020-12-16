from datetime import datetime
from flask import render_template
from pandas_datareader import data
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN

start = datetime(2015, 11, 1)
end = datetime(2016, 3, 10)


def plot_main():
    df = data.DataReader(name='GOOG', data_source='yahoo', start=start, end=end)

    p = figure(x_axis_type='datetime', width=1000, height=300, sizing_mode='scale_width')
    p.title.text = 'Candlestick Chart'
    p.grid.grid_line_alpha = 0.3

    width = 12 * 60 * 60 * 1000  # 12hrs -> milliseconds

    def inc_dec(c, o):
        if c > o:
            value = 'i'
        elif c < o:
            value = 'd'
        else:
            value = 'e'
        return value

    df['Status'] = [inc_dec(c, o) for c, o in zip(df.Close, df.Open)]
    df['Middle'] = (df.Open + df.Close) / 2
    df['Height'] = abs(df.Open - df.Close)

    p.segment(df.index, df.High, df.index, df.Low, color='black')

    p.rect(
        df.index[df.Status == 'i'],
        df.Middle[df.Status == 'i'],
        width,
        df.Height[df.Status == 'i'],
        fill_color='#CCFFFF',
        line_color='black'
    )

    p.rect(
        df.index[df.Status == 'd'],
        df.Middle[df.Status == 'd'],
        width,
        df.Height[df.Status == 'd'],
        fill_color='#FF3333',
        line_color='black'
    )

    js, html, = components(p)
    cdn_js = CDN.js_files[0]
    return render_template(
        'plot.html',
        js=js,
        html=html,
        cdn_js=cdn_js,
    )
    # cdn_css = CDN.css_files  # unnecessary css files are stopped since bokeh 2.0
    # print(cdn_js, cdn_css)
    # output_file('output.html')
    # show(p)
