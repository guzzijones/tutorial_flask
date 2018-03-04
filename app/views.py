from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'aj'}
    posts =[
        {'author' :
              {'nickname': 'John'},
         'body':'something'
         },
        {
         'author' :
               {'nickname': 'Susan'},
          'body':'another movie review'
        }
     ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OPENID:"%s", remember_me:%s' %
              (form.openid.data,str(form.remember_me.data)))
        return redirect('/index')
    return render_template('signin.html',title='Sign In',form=form)
