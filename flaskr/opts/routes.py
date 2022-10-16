"""最適化を解く Webアプリケーション"""
from flask import make_response, redirect, render_template, request, url_for, flash
import pandas as pd
from flaskr.opts.problem import CarGroupProblem
from . import opts
from flaskr.opts.forms import SolveForm

def preprocess(request):
    """リクエストデータを受け取り、データフレームに変換する関数"""
    # 各ファイルを取得する
    students = request.files['students']
    cars = request.files['cars']
    # pandas で読み込む
    students_df = pd.read_csv(students)
    cars_df = pd.read_csv(cars)

    return students_df, cars_df


def postprocess(solution_df):
    """最適化結果をHTML形式に変換する関数"""
    solution_html = solution_df.to_html(header=True, index=False)
    return solution_html


@opts.route('/solve', methods=['GET', 'POST'])
def solve():
    form = SolveForm()
    if form.validate_on_submit():
        students = request.files['students']
        cars = request.files['cars']
        students_df = pd.read_csv(students)
        cars_df = pd.read_csv(cars)
        solution_df = CarGroupProblem(students_df, cars_df).solve()
        solution_html = postprocess(solution_df)
        return render_template('opts/solve.html', solution_html=solution_html, form=form)
    return render_template('opts/solve.html', solution_html=None, form=form)

@opts.route('/download', methods=['POST'])
def download():
    """リクエストに含まれるHTMLの表形式データをcsv形式に変換してダウンロードする関数"""
    solution_html = request.form.get('solution_html')
    solution_df = pd.read_html(solution_html)[0]
    solution_csv = solution_df.to_csv(index=False)
    response = make_response()
    response.data = solution_csv
    response.headers['Content-Type'] = 'text/csv'
    response.headers['Content-Disposition'] = 'attachment; filename=solution.csv'
    return response
