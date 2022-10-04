from flask import Flask, redirect
import os
import stripe


# app name 
app = Flask(__name__)

#stripe configuration
stripe.api_key = 'sk_test_51Ln8E7BftJasxDGEQllKFvbHakZyuJEcNWqUOtZpDLZGWfqr3UFQNKqHudN18RXRfBtFs3D0eZ62Ssq0q7AhYrC600MYqU5qh4'

@app.route("/")
def home ():
    return "Hola mundo"


@app.route("/create_session")
def stripe_create_session():
    session = stripe.checkout.Session.create(
        line_items=[{
        'price_data': {
            'currency': 'usd',
            'product_data': {
            'name': 'T-shirt',
            },
            'unit_amount': 2000,
        },
        'quantity': 1,
        }],
        mode='payment',
        success_url='https://example.com/success',
        cancel_url='https://example.com/cancel',
    )

    return redirect(session.url, code=303)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
