from crypt import methods
from flask import Flask
import os
import stripe
import routes.Payout
import routes.WebHook
import routes.PymentMethods

# app name 
app = Flask(__name__)

#stripe configuration
stripe.api_key = 'sk_test_51Ln8E7BftJasxDGEQllKFvbHakZyuJEcNWqUOtZpDLZGWfqr3UFQNKqHudN18RXRfBtFs3D0eZ62Ssq0q7AhYrC600MYqU5qh4'



app.add_url_rule('/payout', view_func=routes.Payout.index,  methods = ['GET', 'POST', 'DELETE'])
app.add_url_rule('/webhook', view_func=routes.WebHook.webhook_v1, methods= ['POST', 'GET'])

app.add_url_rule('/paymentmethods', view_func=routes.PymentMethods.paymentmethods, methods=['GET', 'POST'])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
