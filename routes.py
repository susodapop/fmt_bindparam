from . import bp
from .views import FormatterView

bp.add_url_rule('/', view_func=FormatterView.as_view('fmt_bindparam'))

