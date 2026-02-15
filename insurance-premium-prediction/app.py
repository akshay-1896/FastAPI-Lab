from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from schema.prediction_response import PredictionResponse
from model.predict import predict_output, model, MODEL_VERSION

app = FastAPI()
        
# human readable
@app.get('/')
def home():
    return {'message': 'Insurance Premium Prediction API'}

# machine readable (AWS, Kubernetes, etc.)
@app.get('/health')
def health_check():
    return{
        'status': 'OK',
        'version': '1.0.0',
        'model_loaded': model is not None
    }

@app.post('/predict', response_model=PredictionResponse)
def predict_premium(data: UserInput):

    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:

        prediction = predict_output(user_input)[0]
        probabilities = predict_output(user_input)[1]

        # Get the confidence (max probability)
        confidence = predict_output(user_input)[2]

        # Map class names to their probabilities
        class_probs = predict_output(user_input)[3]

        return JSONResponse(status_code=200, content={
            'response': prediction,
            'confidence': confidence,
            'class_probabilities': class_probs
            })
    
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))