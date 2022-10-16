from flask import render_template
from . import charts


@charts.route("/chart")
def chart():

    title='Chart Page'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    legend = 'Monthly Data'
    values = [10, 9, 8, 7, 6, 4, 7, 8]

    return render_template('charts/chart.html', title=title, labels=labels, legend=legend, values=values)
