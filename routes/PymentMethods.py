from flask import request
import stripe

stripe.api_key = "sk_test_51Ln8E7BftJasxDGEQllKFvbHakZyuJEcNWqUOtZpDLZGWfqr3UFQNKqHudN18RXRfBtFs3D0eZ62Ssq0q7AhYrC600MYqU5qh4"



def paymentmethods():
    if request.method == "GET":
        return RetrievePaymentMethods()
    elif request.method == "POST":
        return CreatePaymentMethodAndAtach()
    else :
        return f"""No hay metodo implementado para ${request.method}"""
    
#return a payment method by customer @GET
def RetrievePaymentMethods():
    args = request.args
    new_card = stripe.PaymentMethod.list(
        customer=args.get("customer"),
        type=args.get("type"),
    )
    return new_card

#crea una forma de pago y la añade a un customer @POST
def CreatePaymentMethodAndAtach():
    json_data = request.json
    customer = json_data['customer']

    new_card = CreateNewPaymentMethod()
    paymentToCustomer = attach(new_card.id, customer)
    
    return paymentToCustomer


#--------------------------------------------------------------Funciones extra----------------------------------------------------------------------#

#registra una nueva forma de pago
def CreateNewPaymentMethod():
    json_data = request.json

    new_card = stripe.PaymentMethod.create(
        type=json_data["type"],
        card={
            "number": json_data["number"],
            "exp_month": json_data["month"],
            "exp_year": json_data["year"],
            "cvc": json_data["cvc"],
        },
    )

    
    return new_card 

#atach to costumer
def attach(paymentMethod, customer):
    return stripe.PaymentMethod.attach(
        paymentMethod,
        customer=customer,
    )
