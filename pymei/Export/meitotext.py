import logging
lg = logging.getLogger('pymei')


def meitotext(meidocument, filename=None):
    r = meidocument.root
    
def _mei_to_text(el):
    el_name = el.getname()
    
    if el.getattributes() is not None:
        attb = el.getattributes()
    
    if el.getvalue()