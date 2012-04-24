from anthrax.frontend import Frontend

def dummy_view(*args, **kwargs):
    return ''

dummy_frontend = Frontend({
    'wysiwyg_editor': dummy_view,
}, dummy_view)
