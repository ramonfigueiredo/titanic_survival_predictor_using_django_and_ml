import pickle

import numpy as np
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def index_page(request):
    return_data = {
        "error": "0",
        "message": "Successful",
    }
    return Response(return_data)


@api_view(["POST"])
def predict_titanic_survival(request):
    try:

        print('request.data', request.data)
        pclass = request.data.get('pclass', None)
        sex = request.data.get('sex', None)
        age = request.data.get('age', None)
        sibsp = request.data.get('sibsp', None)
        parch = request.data.get('parch', None)
        fare = request.data.get('fare', None)
        embC = request.data.get('embC', None)
        embQ = request.data.get('embQ', None)
        embS = request.data.get('embS', None)

        fields = [pclass, sex, age, sibsp, parch, fare, embC, embQ, embS]

        print('fields', fields)

        if not None in fields:
            # Data preprocessing Convert the values to int
            pclass = int(pclass)
            sex = int(sex)
            age = int(age)
            sibsp = int(sibsp)
            parch = int(parch)
            fare = int(fare)
            embC = int(embC)
            embQ = int(embQ)
            embS = int(embS)

            model_input = [pclass, sex, age, sibsp, parch, fare, embC, embQ, embS]

            print('model_input', model_input)

            # Loading the model and scaler
            model = pickle.load(open('ml_model.sav', 'rb'))
            scaled = pickle.load(open('scaler.sav', 'rb'))

            prediction = model.predict(scaled.transform([
                model_input
            ]))

            print('prediction', prediction)

            conf_score = np.max(model.predict_proba([model_input])) * 100
            predictions = {
                'error': '0',
                'message': 'Successfull',
                'prediction': prediction,
                'confidence_score': conf_score
            }
        else:
            predictions = {
                'error': '1',
                'message': 'Invalid Parameters'
            }
    except Exception as e:
        predictions = {
            'error': '2',
            "message": str(e)
        }

    return Response(predictions)
