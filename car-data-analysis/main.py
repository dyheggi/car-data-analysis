# coding: utf-8

# In[1]:

from bokeh.plotting import figure, output_notebook, show

# output_notebook()

# In[2]:

from bokeh.sampledata.autompg import autompg  # 车辆MPG数据每加仑英里数
from numpy import array

grouped = autompg.groupby("yr")  # 直接可以根据列分类排序
mpg = grouped["mpg"]  # 单独取mpg列
avg = mpg.mean()  # 均值
std = mpg.std()  # 标准差
years = array(list(grouped.groups.keys()))
american = autompg[autompg["origin"] == 1]  # 选择数据，同pandas
japanese = autompg[autompg["origin"] == 3]

p = figure()  # 在一张图件上不同图层绘制

p.quad(left=years - 0.4, right=years + 0.4, bottom=avg - std, top=avg + std, fill_alpha=0.4)  # 矩形边界数据，默认颜色，透明度0.4

p.circle(x=japanese["yr"], y=japanese["mpg"], size=8,
         alpha=0.4, line_color="red", fill_color=None, line_width=2)  # 圆形圆心坐标位置，大小，线的颜色，填充颜色、线宽等

p.triangle(x=american["yr"], y=american["mpg"], size=8,
           alpha=0.4, line_color="blue", fill_color=None, line_width=2)  # 三角形形心坐标，大小，线的颜色，填充颜色、线宽等

show(p)

# In[2]:

from bokeh.sampledata.autompg import autompg  # 车辆MPG数据每加仑英里数
from numpy import array

grouped = autompg.groupby("yr")  # 直接可以根据列分类排序
mpg = grouped["mpg"]  # 单独取mpg列
avg = mpg.mean()  # 均值
std = mpg.std()  # 标准差
years = array(list(grouped.groups.keys()))
american = autompg[autompg["origin"] == 1]  # 选择数据，同pandas
japanese = autompg[autompg["origin"] == 3]

p = figure()  # 在一张图件上不同图层绘制

p.quad(left=years - 0.4, right=years + 0.4, bottom=avg - std, top=avg + std, fill_alpha=0.4)  # 矩形边界数据，默认颜色，透明度0.4

p.circle(x=japanese["yr"], y=japanese["mpg"], size=8,
         alpha=0.4, line_color="red", fill_color=None, line_width=2)  # 圆形圆心坐标位置，大小，线的颜色，填充颜色、线宽等

p.triangle(x=american["yr"], y=american["mpg"], size=8,
           alpha=0.4, line_color="blue", fill_color=None, line_width=2)  # 三角形形心坐标，大小，线的颜色，填充颜色、线宽等

show(p)

# In[3]:

from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot

source = ColumnDataSource(autompg.to_dict("list"))
source.add(autompg["yr"], name="yr")

plot_config = dict(plot_width=300, plot_height=300,
                   tools="pan,wheel_zoom,box_zoom,box_select,lasso_select")  # 转换为字典格式

p1 = figure(title="MPG by Year", **plot_config)
p1.circle(x="yr", y="mpg", color="blue", source=source)  # 年份和mpg关系

p2 = figure(title="HP vs. Displacement", **plot_config)
p2.circle(x="hp", y="displ", color="green", source=source)  # 马力和排放量

p3 = figure(title="MPG vs. Displacement", **plot_config)  # mpg和排放量
p3.circle("mpg", "displ", size="cyl", line_color="red", fill_color=None, source=source)  # 圆圈大小采用cyl列数据

p = gridplot([[p1, p2, p3]], toolbar_location="right")  # 采用网格式布置图，可以定义每行图形的数量

show(p)
