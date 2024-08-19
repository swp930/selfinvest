import posixpath
from pathlib import Path

from django.utils._os import safe_join
from django.views.static import serve as static_serve
from django.http import HttpResponse

def serve_react_static(request, path, document_root=None):
    path = posixpath.normpath(path).lstrip("/")
    fullpath = Path(safe_join(document_root, path))
    if fullpath.is_file():
        return static_serve(request, path, document_root)
    else:
        html = "<html><body>Invalid URL</body></html>"
        return HttpResponse(html)

def serve_react_index(request, document_root=None):
    return static_serve(request, "index.html", document_root)
        