# Import the necessary libraries
from ibm_watsonx_ai.foundation_models import Model

api_key = "fFZEt9RgQ9Ka4BdsqMBKzm-Z96Ascc98FDVfNAWUZWz9"
project_id = "f6038327-f6f8-453f-a516-be4304a1ace3"
# ----------------------------------------------------

# Setup the credentials for the AI model
credentials = {
    "url": "https://us-south.ml.cloud.ibm.com",
    "apikey": api_key
}

# Define the model we want to use (IBM Granite Instruct)
model_id = "ibm/granite-13b-instruct-v2"

# Define the model parameters
parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 200,
}

# Create the model instance
model = Model(
    model_id=model_id,
    params=parameters,
    credentials=credentials,
    project_id=project_id
)

# --- This is the prompt we will send to the AI ---
prompt_to_send = "Suggest three simple, nutritious meal ideas for a healthy lunch."
# ------------------------------------------------

# --- Let's run the AI! ---
print("Sending prompt to the AI model...")
print("PROMPT: " + prompt_to_send)

generated_response = model.generate(prompt=prompt_to_send)
response_text = generated_response['results'][0]['generated_text']

print("\n--- AI RESPONSE ---")
print(response_text)
print("--------------------")
