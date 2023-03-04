from flask import render_template, redirect, url_for, request, flash
from elastic_app_search import exceptions as ex_app_search
from requests import exceptions as ex_requests
from app import app, client_app_search
from app.searchForm import SearchForm


@app.route('/', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    engine_name = 'flask-app-search'
    if request.method == 'POST':
        if form.validate_on_submit():
            # Paging:
            # documents = client_app_search.search(engine_name, form.searchbox.data,
            # {"page": {"size": 25, "current": 3}})
            try:
                documents = client_app_search.search(engine_name, form.searchbox.data,
                                                     {"page": {"size": app.config['POSTS_PER_PAGE']}})
            except ex_requests.ConnectionError:
                # connection error
                flash('Connection Error!! Please check connection to App-search.')
                return redirect(url_for('search'))

            # print("Method: " + request.method)
            return render_template('search.html', title='Search', form=form, search_results=documents,
                                   query=form.searchbox.data)
        else:
            return redirect(url_for('search'))
    else:
        if request.args.get('page') and request.args.get('query'):
            # print("Other: " + str(form.validate_on_submit()))
            # print("Page: " + request.args.get('page'))
            # print("Query: " + request.args.get('query'))
            # print("Method: " + request.method)
            try:
                documents = client_app_search.search(engine_name, request.args.get('query'),
                                                     {"page": {"current": int(request.args.get('page')),
                                                               "size": app.config['POSTS_PER_PAGE']}})
            except ex_app_search.BadRequest:
                # 100 pages limit or other bad requests
                flash('Bad request or requested more than 100 pages.')
                return render_template('search.html', title='Search', form=form,
                                       query=request.args.get('query'))

            return render_template('search.html', title='Search', form=form, search_results=documents,
                                   query=request.args.get('query'))
        else:
            return render_template('search.html', title='Search', form=form)



