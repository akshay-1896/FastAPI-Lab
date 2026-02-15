import pickle
import pandas as pd

# import the ml model
with open('model/model.pkl', 'rb') as file:
    model = pickle.load(file)

# extracted by MLflow
MODEL_VERSION = '1.0.0'

def predict_output(user_input: dict):

    input_df = pd.DataFrame([user_input])

    output = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0]

    # Get the confidence (max probability)
    confidence = round(float(max(probabilities)), 4)

    # Map class names to their probabilities
    class_probs = {
        model.classes_[i]: round(float(probabilities[i]), 4)
        for i in range(len(model.classes_))
    }

    return output, probabilities, confidence, class_probs