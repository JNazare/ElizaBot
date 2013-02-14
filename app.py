import flask, flask.views
import matcher as matcher
import os
from flask import session

app = flask.Flask(__name__)

app.secret_key = "bacon"

class View(flask.views.MethodView):

	def get(self):
		session["count"] = 0
		return flask.render_template('index.html')


	def post(self):
		result = flask.request.form['expression']
		count = session.get("count", 0)
		session["count"] = count + 1
		if count == 0:
			res = matcher.hi_eliza(result)
			flask.flash(res)
			print count
		elif count >= 1 and count < 10:
			res = matcher.main(result)
			flask.flash(res)
			print count
		elif count >= 10:
			res = matcher.stop_eliza()
			flask.flash(res)
			print count
		return flask.render_template('index.html')
        

app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST'])

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)