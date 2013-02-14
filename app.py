import flask, flask.views
import matcher as matcher

app = flask.Flask(__name__)

app.secret_key = "bacon"
count = -2

def incr():
	global count
	count = count + 1
	return count

class View(flask.views.MethodView):

	def get(self):
		return flask.render_template('index.html')

	def post(self):
		result = flask.request.form['expression']
		count = incr()
		if count == 0:
			res = matcher.hi_eliza(result)
			flask.flash(res)
			count = incr()
			print count
		elif count > 1 and count < 20:
			res = matcher.main(result)
			flask.flash(res)
			count = incr()
			print count
		elif count >= 20:
			res = matcher.stop_eliza()
			flask.flash(res)
			count = incr()
			print count
		return self.get()
        

app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST'])

app.debug = True
app.run()