from flask.views import MethodView
from flask import jsonify, request
from .formatter import get_parameter_names, fill_parameters, BindingException


class FormatterView(MethodView):

	def __init__(self, *args, **kwargs):

		MethodView.__init__(self,*args, **kwargs)

	def _error_checker(f):

		def inner(self, *args, **kwargs):

			try:
				if self.txt is None:
					return jsonify(dict(error="You must provide an argument called SQL."))
			except:
				return jsonify(dict(error="Could not decode JSON content in request."))

			if len(self.parameters) == 0:
				return jsonify(dict(message="Your SQL contains no parameter markers!"))

			return f(self, *args, **kwargs)

		return inner

	@_error_checker
	def get(self):
		''' Returns a list of parameter markers from the provided query. '''
		return jsonify(sql=self.txt, parameters=self.parameters)


	@_error_checker
	def post(self):
		''' Returns a query with values inserted at each parameter marker. '''

		try:
			fmt_sql = fill_parameters(self.txt, self.values)
		except BindingException as e:
			return jsonify(error="Could not finish binding. Not all needed parameters were provided.",
				parameters=self.parameters)


		return jsonify(fmt_sql=fmt_sql)

	@property
	def txt(self):
		return request.json.get('sql', None)

	@property
	def parameters(self):
		return get_parameter_names(self.txt)

	@property
	def values(self):
		return request.json.get('parameters', None)






