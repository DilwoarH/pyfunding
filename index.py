import stripe
import json
from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    stripe_publishable_key = os.environ.get("STRIPE_PUBLISHABLE_KEY", default=None)
    if not stripe_publishable_key:
        raise ValueError("No STRIPE_PUBLISHABLE_KEY set for Stripe, get this from https://dashboard.stripe.com/account/apikeys.")
    
    return render_template('index.html', stripe_publishable_key=stripe_publishable_key)

@app.route("/charge", methods=["POST"])
def charge():
    # Set your secret key: remember to change this to your live secret key in production
    # See your keys here: https://dashboard.stripe.com/account/apikeys
    stripe_api_key = os.environ.get("STRIPE_API_KEY", default=None)
    if not stripe_api_key:
        raise ValueError("No STRIPE_API_KEY set for Stripe, get this from https://dashboard.stripe.com/account/apikeys.")
    
    stripe.api_key = stripe_api_key

    # Token is created using Checkout or Elements!
    # Get the payment token ID submitted by the form:
    token = request.form['stripeToken'] # Using Flask

    try:
        charge = stripe.Charge.create(
            amount=10000,
            currency='usd',
            description='Fund a PyCon ticket',
            source=token,
        )
    except stripe.error.InvalidRequestError as e:
        return e.json_body['error']['message']
    
    return json.dumps(charge)
