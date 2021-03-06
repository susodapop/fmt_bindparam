import re, string, copy

class BindingException(Exception):
	pass

def fill_parameters(txt:str, params:dict) -> str:

	if not all([i in get_parameter_names(txt) for i in params]):
		raise BindingException("Parameter input was not valid.")

	cpy_params = copy.deepcopy(params)
	
	def recursive_replace(params:dict, txt:str):

		key = params.__iter__().__next__()
		wrap_template = "'%s'" if params.get(key).get('wrap') else "%s"
		new_str = txt.replace(':%s' % key, wrap_template % params.get(key).get('value'))
		params.pop(key)

		if len(params) == 0:
			return new_str
		else:
			return recursive_replace(params, new_str)

	return recursive_replace(cpy_params, txt)


def get_parameter_names(txt:str) -> list:

	# Taken directly from sqla Source Code
	# /sqlalchemy/sql/elements.py#L1484
	_bind_params_regex = re.compile(r"(?<![:\w\x5c]):(\w+)(?!:)", re.UNICODE)
	return [i for i in set([i for i in re.findall(_bind_params_regex, txt)])]
