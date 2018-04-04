import os
import yaml
from flask import Blueprint, current_app, render_template, url_for
from .post import Post


blueprint = Blueprint(
    'blog',
    __name__,
    static_folder='static',
    template_folder='templates',
)


@blueprint.route('/')
def index():
    meta = current_app.config.get('META')
    source_path = os.path.join(
        current_app.root_path,
        'source',
        current_app.config['DIR']['source']['post'],
    )

    contents = []
    for each in os.listdir(source_path):
        if each.endswith('.md'):
            path = os.path.join(source_path, each)
            configs = Post(path).meta
            configs['file'] = each[:-3]
            contents.append(configs)

    # return url_for('blog.post', name='demo')
    # return str(blueprint.jinja_loader.searchpath)
    return render_template('blog/index.html', contents=contents, meta=meta)


@blueprint.route('/<name>/')
def post(name):
    md_extensions = current_app.config['MARKDOWN']
    filepath = os.path.join(
        current_app.root_path,
        'source',
        current_app.config['DIR']['source']['post'],
        name + '.md'
    )
    name, _ = os.path.splitext(name)
    post = Post(filepath, **md_extensions)

    context = {
        'meta': post.meta,
        'html': post.html,
    }

    return render_template('blog/post.html', **context)
