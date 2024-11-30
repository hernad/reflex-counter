from importlib import metadata
for pkg in ['uvicorn', 'gunicorn']:
    print(pkg, ':', metadata.version(pkg))

