import re, string, copy

class BindingException(Exception):
	pass

def fill_parameters(txt:str, params:dict) -> str:

	if not all([i in get_parameter_names(txt) for i in params]):
		raise BindingException("Parameter input was not valid.")
	
	def recursive_replace(params:dict, txt:str):

		cpy_params = copy.deepcopy(params)
		key = cpy_params.__iter__().__next__()
		new_str = txt.replace(':%s' % key, "'%s'" % cpy_params.get(key))
		cpy_params.pop(key)

		if len(cpy_params) == 0:
			return new_str
		else:
			return recursive_replace(cpy_params, new_str)

	return recursive_replace(params, txt)


def get_parameter_names(txt:str) -> list:

	# Taken directly from sqla Source Code
	# /sqlalchemy/sql/elements.py#L1484
	_bind_params_regex = re.compile(r"(?<![:\w\x5c]):(\w+)(?!:)", re.UNICODE)
	return [i for i in set([i for i in re.findall(_bind_params_regex, txt)])]
