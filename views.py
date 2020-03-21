from flask.views import MethodView

class FormatterView(MethodView):

	def get(self):

		return 'hello world'