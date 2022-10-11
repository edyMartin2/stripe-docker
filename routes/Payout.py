from flask import render_template
import stripe

stripe.api_key = 'sk_test_51Ln8E7BftJasxDGEQllKFvbHakZyuJEcNWqUOtZpDLZGWfqr3UFQNKqHudN18RXRfBtFs3D0eZ62Ssq0q7AhYrC600MYqU5qh4'

def index():
    payoutNew = stripe.Payout.create(amount=5000, currency="usd")
    return payoutNew
