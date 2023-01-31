from app import app
###############################################
#          Import some packages               #
###############################################
from flask import Flask, render_template, request
from forms import ContactForm
from forms import NewsLetterForm
import pandas as pd

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')
    
@app.route('/product')
def product():
    return render_template('product.html', title='Products/Menu')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html', title="About Us")
    
@app.route('/specials')
def specials():
    return render_template('specials.html', title="Specials")
    
@app.route('/donuts')
def donuts():
    return render_template('donuts.html', title="Donuts")
    
@app.route('/vanillaslice')
def vanillaslice():
    return render_template('vanillaslice.html', title="Vanilla Slice")
    
@app.route('/randytart')
def randytart():
    return render_template('randytart.html', title="Randy Tart")

@app.route('/custardtart')
def custardtart():
    return render_template('custardtart.html', title="custardtart")
    
@app.route('/raspberrycheesecake')
def raspberrycheesecake():
    return render_template('raspberrycheesecake.html', title="Raspberry Cheesecake")
    
@app.route('/applecake')
def applecake():
    return render_template('applecake.html', title="Apple cake Slice")
    
###############################################
#       Render Contact page                   #
###############################################
@app.route('/contactus', methods=["GET","POST"])
def get_contact():
    form = ContactForm()
    if request.method == 'POST':
        name =  request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]
        res = pd.DataFrame({'name':name, 'email':email, 'subject':subject ,'message':message}, index=[0])
        res.to_csv('./contactusMessage.csv', mode='a')
        return render_template('contact.html', form=form)
    else:
        return render_template('contact.html', form=form)

###############################################
#       Render News letter page               #
###############################################
@app.route('/newsletter', methods=["GET","POST"])
def get_newsletter():
    form = NewsLetterForm()
    if request.method == 'POST':
        name =  request.form["name"]
        email = request.form["email"]
        res = pd.DataFrame({'name':name, 'email':email}, index=[0])
        res.to_csv('./newsletter.csv', mode='a')
        return render_template('newsletter.html', form=form)
    else:
        return render_template('newsletter.html', form=form)