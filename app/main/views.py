from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from..import db
from flask_login import login_required,current_user
#getting our random quotes from the quotes API
from .forms import BlogForm,CommentForm
from ..models import User,Blog,Comment, Subscriber
@main.route('/')
def index():
    blogs = Blog.query.order_by(Blog.date_created.desc()).all()
    # quote= get_quote()

    return render_template('index.html', blogs=blogs   )

@main.route('/newblog', methods=['GET', 'POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        blog_title = form.title.data
        blog_content = form.content.data
        new_user_blog= Blog(blog_title=blog_title, blog_content=blog_content,user_id=current_user.id)
        
        new_user_blog.save_blog()
    
        
        return redirect(url_for('main.index'))
        
    
    return render_template('post.html',form = form)


@main.route('/blog/<blog_id>', methods=['GET', 'POST'])
def blog(blog_id):
    blog=Blog.query.filter_by(id=blog_id).first()