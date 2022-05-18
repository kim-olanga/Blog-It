# from flask import Flask, render_template, flash, request
# from datetime import datetime
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from werkzeug.security import generate_password_hash,  check_password_hash
# from datetime import datetime
# from webforms import LoginForm, PostForm, UserForm, PasswordForm, NamerForm, SearchForm
# from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
# from webforms import LoginForm, PostForm, UserForm, PasswordForm, NamerForm
# from flask_ckeditor import CKEditor 
# from werkzeug.utils import secure_filename
# import uuid as uuid
# import os



# #create flask instance
# app = Flask(__name__)
# #Add CKEditor
# CKEditor = CKEditor(app)
# #Add Database
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# #New database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kimberly:kim12345@localhost/test'
# #Secret Key
# app.config['SECRET_KEY'] = "kimzyy12345"

# UPLOAD_FOLDER = 'static/images/'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# #initialize database
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# # Flask_Login Stuff
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

# @login_manager.user_loader
# def load_user(user_id):
# 	return User.query.get(int(user_id))

# # Pass Stuff To Navbar
# @app.context_processor
# def base():
# 	form = SearchForm()
# 	return dict(form=form)

# # Create Admin Page
# @app.route('/admin')
# @login_required
# def admin():
#   id = current_user.id
#   if id == 1:
#         return render_template("admin.html")
#   else:
#         flash("Sorry you must be the Admin to access the Admin Page...")
#         return redirect(url_for('dashboard'))



# # Create Search Function
# @app.route('/search', methods=["POST"])
# def search():
#   form = SearchForm()
#   posts = Post.query
#   if form.validate_on_submit():
#     # Get data from submitted form
#     posts.searched = form.searched.data
#     # Query the Database
#     posts = posts.filter(Post.content.like('%' + posts.searched + '%'))
#     posts = posts.order_by(Post.title).all()

#   return render_template("search.html",
#     form=form,
#     searched = posts.searched,
#     posts = posts)


# # Create Login Page
# @app.route('/login', methods=['GET', 'POST'])
# def login():
# 	form = LoginForm()
# 	if form.validate_on_submit():
# 		user = User.query.filter_by(username=form.username.data).first()
# 		if user:
# 			# Check the hash
# 			if check_password_hash(user.password_hash, form.password.data):
# 				login_user(user)
# 				flash("Login Succesfull!!")
# 				return redirect(url_for('dashboard'))
# 			else:
# 				flash("Wrong Password - Try Again!")
# 		else:
# 			flash("That User Doesn't Exist! Try Again...")


# 	return render_template('login.html', form=form)

# # Create Logout Page
# @app.route('/logout', methods=['GET', 'POST'])
# @login_required
# def logout():
# 	logout_user()
# 	flash("You Have Been Logged Out!  Thanks For Stopping By...")
# 	return redirect(url_for('login'))

# # Create Dashboard Page
# @app.route('/dashboard', methods=['GET', 'POST'])
# @login_required
# def dashboard():
# 	form = UserForm()
# 	id = current_user.id
# name_to_update = User.query.get_or_404(id)
# if request.method == "POST":
# 		name_to_update.name = request.form['name']
# 		name_to_update.email = request.form['email']
# 		name_to_update.favorite_color = request.form['favorite_color']
# 		name_to_update.username = request.form['username']
# 		name_to_update.about_author = request.form['about_author']
		

# 		# Check for profile pic
# if request.files['profile_pic']:
#         name_to_update.profile_pic = request.files['profile_pic']

#         # Grab Image Name
#         pic_filename = secure_filename(name_to_update.profile_pic.filename)
#         # Set UUID
#         pic_name = str(uuid.uuid1()) + "_" + pic_filename
#         # Save That Image
#         saver = request.files['profile_pic']
			

#         # Change it to a string to save to db
#         name_to_update.profile_pic = pic_name
# try:
#         db.session.commit()
#         saver.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
#         flash("User Updated Successfully!")
#         return render_template("dashboard.html", 
#         form=form,
# 		name_to_update = name_to_update)
# except:
# 		flash("Error!  Looks like there was a problem...try again!")
# 		return render_template("dashboard.html", 
# 		form=form,
# 		name_to_update = name_to_update)
        
#         else:
# 	db.session.commit()
# 	flash("User Updated Successfully!")
# 	return render_template("dashboard.html", form=form, name_to_update = name_to_update)
# else:
# 	return render_template("dashboard.html", form=form,name_to_update = name_to_update,id = id)

# 	return render_template('dashboard.html')



# @app.route('/posts/delete/<int:id>')
# @login_required
# def delete_post(id):
# 	post_to_delete = Posts.query.get_or_404(id)
# 	id = current_user.id
# 	if id == post_to_delete.poster.id or id == 14:
# 		try:
# 			db.session.delete(post_to_delete)
# 			db.session.commit()

# 			# Return a message
# 			flash("Blog Post Was Deleted!")

# 			# Grab all the posts from the database
# 			posts = Posts.query.order_by(Posts.date_posted)
# 			return render_template("posts.html", posts=posts)


# 		except:
# 			# Return an error message
# 			flash("Whoops! There was a problem deleting post, try again...")

# 			# Grab all the posts from the database
# 			posts = Posts.query.order_by(Posts.date_posted)
#             return render_template("posts.html", posts=posts)
# 	else:
# 		# Return a message
# 		flash("You Aren't Authorized To Delete That Post!")

# 		# Grab all the posts from the database
# 		posts = Posts.query.order_by(Posts.date_posted)
# 		return render_template("posts.html", posts=posts)

# @app.route('/posts')
# def posts():
# 	# Grab all the posts from the database
# 	posts = Posts.query.order_by(Posts.date_posted)
# 	return render_template("posts.html", posts=posts)

# @app.route('/posts/<int:id>')
# def post(id):
# 	post = Posts.query.get_or_404(id)
# 	return render_template('post.html', post=post)

# @app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
# @login_required
# def edit_post(id):
# 	post = Posts.query.get_or_404(id)
# 	form = PostForm()
# 	if form.validate_on_submit():
# 		post.title = form.title.data
# 		#post.author = form.author.data
# 		post.slug = form.slug.data
# 		post.content = form.content.data
# 		# Update Database
# 		db.session.add(post)
# 		db.session.commit()
# 		flash("Post Has Been Updated!")
# 		return redirect(url_for('post', id=post.id))
	
# 	if current_user.id == post.poster_id or current_user.id == 14:
# 		form.title.data = post.title
# 		#form.author.data = post.author
#         form.slug.data = post.slug
# 		form.content.data = post.content
# 		return render_template('edit_post.html', form=form)
# 	else:
# 		flash("You Aren't Authorized To Edit This Post...")
# 		posts = Posts.query.order_by(Posts.date_posted)
# 		return render_template("posts.html", posts=posts)



# # Add Post Page
# @app.route('/add-post', methods=['GET', 'POST'])
# #@login_required
# def add_post():
# 	form = PostForm()

# 	if form.validate_on_submit():
# 		poster = current_user.id
# 		post = Posts(title=form.title.data, content=form.content.data, poster_id=poster, slug=form.slug.data)
# 		# Clear The Form
# 		form.title.data = ''
# 		form.content.data = ''
# 		#form.author.data = ''
# 		form.slug.data = ''

# 		# Add post data to database
# 		db.session.add(post)
# 		db.session.commit()

# 		# Return a Message
# 		flash("Blog Post Submitted Successfully!")

# 	# Redirect to the webpage
# 	return render_template("add_post.html", form=form)



# # Json Thing
# @app.route('/date')
# def get_current_date():
#     	favorite_pizza = {
# 		"John": "Pepperoni",
# 		"Mary": "Cheese",
# 		"Tim": "Mushroom"
# 	}
# 	return favorite_pizza
# 	#return {"Date": date.today()}



# @app.route('/delete/<int:id>')
# @login_required
# def delete(id):
# 	# Check logged in id vs. id to delete
# 	if id == current_user.id:
# 		user_to_delete = Users.query.get_or_404(id)
# 		name = None
# 		form = UserForm()

# 		try:
# 			db.session.delete(user_to_delete)
# 			db.session.commit()
# 			flash("User Deleted Successfully!!")

# 			our_users = Users.query.order_by(Users.date_added)
# 			return render_template("add_user.html", 
# 			form=form,
# 			name=name,
# 			our_users=our_users)

# 		except:
# 			flash("Whoops! There was a problem deleting user, try again...")
# 			return render_template("add_user.html", 
# 			form=form, name=name,our_users=our_users)
# 	else:
# 		flash("Sorry, you can't delete that user! ")
#         return redirect(url_for('dashboard'))

# # Update Database Record
# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# @login_required
# def update(id):
# 	form = UserForm()
# 	name_to_update = Users.query.get_or_404(id)
# 	if request.method == "POST":
# 		name_to_update.name = request.form['name']
# 		name_to_update.email = request.form['email']
# 		name_to_update.favorite_color = request.form['favorite_color']
# 		name_to_update.username = request.form['username']
# 		try:
# 			db.session.commit()
# 			flash("User Updated Successfully!")
# 			return render_template("update.html", 
# 				form=form,
# 				name_to_update = name_to_update, id=id)
# 		except:
# 			flash("Error!  Looks like there was a problem...try again!")
# 			return render_template("update.html", 
# 				form=form,
# 				name_to_update = name_to_update,
# 				id=id)
# 	else:
# 		return render_template("update.html", 
# 				form=form,
# 				name_to_update = name_to_update,
# 				id = id)
#                 @app.route('/user/add', methods=['GET', 'POST'])
# def add_user():
# 	name = None
# 	form = UserForm()
# 	if form.validate_on_submit():
# 		user = Users.query.filter_by(email=form.email.data).first()
# 		if user is None:
# 			# Hash the password!!!
# 			hashed_pw = generate_password_hash(form.password_hash.data, "sha256")
# 			user = Users(username=form.username.data, name=form.name.data, email=form.email.data, favorite_color=form.favorite_color.data, password_hash=hashed_pw)
# 			db.session.add(user)
# 			db.session.commit()
# 		name = form.name.data
# 		form.name.data = ''
# 		form.username.data = ''
# 		form.email.data = ''
# 		form.favorite_color.data = ''
# 		form.password_hash.data = ''

# 		flash("User Added Successfully!")
# 	our_users = Users.query.order_by(Users.date_added)
# 	return render_template("add_user.html", 
# 		form=form,
# 		name=name,
# 		our_users=our_users)

# #create the first route
# @app.route('/')
# def index():
#     return render_template("index.html", user_name=name)

# # localhost:500/user/john
# @app.route('/user/<name>')
# def user(name):
#     return render_template("user.html", user_name=name)

# # Create Custom Error Pages

# # Invalid URL
# @app.errorhandler(404)
# def page_not_found(e):
# 	return render_template("404.html"), 404

# # Internal Server Error
# @app.errorhandler(500)
# def page_not_found(e):
# 	return render_template("500.html"), 500

# # Create Password Test Page
# @app.route('/test_pw', methods=['GET', 'POST'])
# def test_pw():
# 	email = None
# 	password = None
# 	pw_to_check = None
# 	passed = None
# 	form = PasswordForm()


# 	# Validate Form
# 	if form.validate_on_submit():
# 		email = form.email.data
# 		password = form.password_hash.data
# 		# Clear the form
# 		form.email.data = ''
# 		form.password_hash.data = ''

# 		# Lookup User By Email Address
# 		pw_to_check = Users.query.filter_by(email=email).first()
		
# 		# Check Hashed Password
#         passed = check_password_hash(pw_to_check.password_hash, password)

# 	return render_template("test_pw.html", 
# 		email = email,
# 		password = password,
# 		pw_to_check = pw_to_check,
# 		passed = passed,
# 		form = form)


# # Create Name Page
# @app.route('/name', methods=['GET', 'POST'])
# def name():
# 	name = None
# 	form = NamerForm()
# 	# Validate Form
# 	if form.validate_on_submit():
# 		name = form.name.data
# 		form.name.data = ''
# 		flash("Form Submitted Successfully!")
		
# 	return render_template("name.html", 
# 		name = name,
# 		form = form)




# # Create a Blog Post model
# class Post(db.Model):
# 	id = db.Column(db.Integer, primary_key=True)
# 	title = db.Column(db.String(255))
# 	content = db.Column(db.Text)
# 	#author = db.Column(db.String(255))
# 	date_posted = db.Column(db.DateTime, default=datetime.utcnow)
# 	slug = db.Column(db.String(255))
# 	# Foreign Key To Link Users (refer to primary key of the user)
# 	poster_id = db.Column(db.Integer, db.ForeignKey('users.id'))

# # Create Model
# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), nullable=False, unique=True)
#     name = db.Column(db.String(200), nullable=False)
#     email = db.Column(db.String(120), nullable=False, unique=True)
#     about_author = db.Column(db.Text(), nullable=True)
#     date_added = db.Column(db.DateTime, default=datetime.utcnow)
#     profile_pic = db.Column(db.String(), nullable=True)

# 	# Do some password stuff!
#     password_hash = db.Column(db.String(128))
# 	# User Can Have Many Posts 
#     posts = db.relationship('Posts', backref='poster')


#     @property
#     def password(self):
# 	    raise AttributeError('password is not a readable attribute!')

#     @password.setter
#     def password(self, password):
# 		self.password_hash = generate_password_hash(password)

# 	def verify_password(self, password):
# 		return check_password_hash(self.password_hash, password)

# 	# Create A String
# 	def __repr__(self):
# 		return '<Name %r>' % self.name






#create Model
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(200), nullable=False)
#     email = db.Column(db.String(120), nullable=False, unique=True)
#     data_added = db.Column(db.DateTime, default=datetime.utcnow)
#     #password
#     password_hash = db.Column(db.String(120))

#     @property
#     def password(self):
#         raise AttributeError('password is not a readable attribute')
    
#     @password.setter
#     def password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def verify_password(self, password):
#         return check_password_hash(self.password_hash, password) 



#     #create string
#     def __repr__(self):
#         return '<Name %r>' % self.name

# #delete database record
# @app.route('/delete/<init:id>')
# def delete(id):
#     user_to_delete = User.querry.get_or_404(id)
#     name = None
#     form = UserForm()

#     try:
#         db.seesion.delete(user_to_delete)
#         db.session.commit()
#         flash("user deleted successfully..")
#         our_user = User.querry.order_by(User.date_added)
#         return render_template("add_user.html", 
#         form=form,
#         name=name,
#         our_user=our_user)
#     except:
#         flash("there was a problem deleting the user")
#         return render_template("add_user.html", 
#         form=form,
#         name=name,
#         our_user=our_user)

# #create form class
# class UserForm(FlaskForm):
#     name = StringField("Name", validators=[DataRequired()])
#     email = StringField("Email", validators=[DataRequired()])
#     submit = SubmitField("Submit")

# #Update database record
# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     form = UserForm()
#     name_to_update = User.querry.get_or_404(id)
#     if request.method =="POST":
#         name_to_update.name = request.form['name']
#         name_to_update.email = request.form['email']
#         try:
#             db.session.commit()
#             flash("User updated successfully!")
#             return render_template("update.html", 
#             form=form,
#             name_to_update = name_to_update)
#         except:
#            flash("Looks like there was a problem updating try again")
#            return render_template("update.html", 
#            form=form,
#            name_to_update = name_to_update) 
#     else:
#         return render_template("update.html", 
#            form=form,
#            name_to_update = name_to_update,
#            id = id) 



# #create the route
# @app.route('/user/add', methods=['GET', 'POST'])
# def add_user():
#     name = None
#     form = UserForm()
#     #validate form
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user is None:
#             user = User(name=form.name.data, email=form.email.data)
#             db.session.add(user)
#             db.session.commit()
#         name = form.name.data
#         form.name.data = ''
#         form.email.data = ''

#         flash("user added successfully..")
#     our_user = User.querry.order_by(User.date_added)
#     return render_template("add_user.html", 
#     form=form,
#     name=name,
#     our_user=our_user)

# #create the first route
# @app.route('/')
# def index():
#     return render_template("index.html", user_name=name)

# # localhost:500/user/john
# @app.route('/user/<name>')
# def user(name):
#     return render_template("user.html", user_name=name)


# #create custom error pages
# # invalid url
# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template("404.html"),404

# #internal server error
# @app.errorhandler(500)
# def page_not_found(e):
#     return render_template("500.html"), 500

# #create form class
# class NamerForm(FlaskForm):
#     name = StringField("Name", validators=[DataRequired()])
#     submit = SubmitField("Submit")

# #create name page
# @app.route('/name', methods=['GET', 'POST'])
# def name():
#     name = None
#     form = NamerForm()
#     #validate form
#     if form.validate_on_submit():
#         name = form.name.data
#         form.name.data = ''
#         flash("Form submitted successfully.!!")

#     return render_template("name.html", 
#         name=name, 
#         form=form)

# #create the route
# @app.route('/user/add', methods=['GET', 'POST'])
# def add_user():
#     name = None
#     form = UserForm()
#     #validate form
#     if form.validate_on_submit():
#         user = UserForm.query.filter_by(email=form.email.data).first()
#         if user is None:
#             user = UserForm(name=form.name.data, email=form.email.data)
#             db.session.add(user)
#             db.session.commit()
#         name = form.name.data
#         form.name.data = ''
#         form.email.data = ''
#         our_users = User.querry.order_by(User.date_added)
#     return render_template("add_user.html", 
#     name=name,
#     form=form,
#     our_users=our_users)
