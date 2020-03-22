from . import bp
from .views import FormatterView, WebView

bp.add_url_rule('/', view_func=WebView.as_view('index'))
bp.add_url_rule('/api', view_func=FormatterView.as_view('fmt_bindparam'))

