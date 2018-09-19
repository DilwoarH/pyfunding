# PyFunding

Crowdfunding platform to help fund tickets for those who cannot afford to pay but love Python.

## Setting up env variables

### Stripe API keys

You can find these on: https://dashboard.stripe.com/account/apikeys

```
export STRIPE_API_KEY=sk_test_....
export STRIPE_PUBLISHABLE_KEY=pk_test_.....
```

## Running application

```
FLASK_APP=index.py flask run
```