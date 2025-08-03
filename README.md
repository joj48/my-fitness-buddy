# my-fitness-buddy
IBM cloud project

A simple Python application that uses the IBM Granite foundation model on the Watsonx.ai platform to generate ideas for fitness and nutrition. This project is inspired by the "Fitness Buddy" problem statement (Problem Statement No. 13) from the IBM SkillsBuild for Academia challenge.

This script serves as a basic example of how to connect to and use the `ibm-watsonx-ai` Python library.

***
## Technology Used
* Python 3
* IBM Watsonx.ai
* IBM Granite Foundation Model (`ibm/granite-13b-instruct-v2`)
* `ibm-watsonx-ai` Python Library

***
## Prerequisites
Before you begin, you will need the following:
1.  An **IBM Cloud Account** (a Lite account is sufficient).
2.  A **Watsonx.ai Project** created on IBM Cloud.
3.  Your **IBM Cloud API Key**.
4.  Your **Watsonx.ai Project ID**.
5.  **Python** installed on your local computer.

***
## Setup and Installation

Follow these steps to set up and run the project on your local machine.

1.  **Clone or Download the Repository**
    Clone this GitHub repository or download the files (`app.py`, `requirements.txt`) to a new folder on your computer.

2.  **Navigate to the Project Folder**
    Open your terminal or command prompt and use the `cd` command to navigate into the folder where you saved the files.
    ```bash
    cd path/to/your/project-folder
    ```

3.  **Install Required Libraries**
    Run the following command to install the necessary Python library from the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```
***
## Configuration

You must add your personal IBM Cloud credentials to the script before you can run it.

1.  Open the **`app.py`** file in a text editor.
2.  Find the section marked `--- IMPORTANT: PASTE YOUR CREDENTIALS HERE ---`.
3.  Replace the placeholder text (`YOUR_API_KEY` and `YOUR_PROJECT_ID`) with your actual API Key and Project ID that you saved from IBM Cloud.

    ```python
    # --- IMPORTANT: PASTE YOUR CREDENTIALS HERE ---
    # Replace 'YOUR_API_KEY' with your actual IBM Cloud API Key
    # Replace 'YOUR_PROJECT_ID' with your actual Watsonx.ai Project ID
    api_key = "paste-your-api-key-here"
    project_id = "paste-your-project-id-here"
    # ----------------------------------------------------
    ```
4.  Save the `app.py` file.

***
## Running the Application
Once the setup and configuration are complete, run the application from your terminal with the following command:
```bash
python app.py
```
***
## Sample Output
The script will print the prompt it is sending and then stream the response from the AI model. The output will look something like this:
```
Sending prompt to the AI model...
PROMPT: Suggest three simple, nutritious meal ideas for a healthy lunch.

--- AI RESPONSE ---
Here are three simple and nutritious meal ideas for a healthy lunch:

1.  **Quinoa Salad with Roasted Vegetables and Lemon-Herb Vinaigrette:**
    * **Base:** Cooked quinoa.
    * **Vegetables:** Roasted bell peppers, zucchini, and cherry tomatoes.
    * **Protein:** Chickpeas or grilled chicken strips.
    * **Dressing:** A simple vinaigrette made with olive oil, lemon juice, and fresh herbs like parsley and dill.

2.  **Greek Yogurt Chicken Salad Sandwich:**
    * **Base:** Whole-wheat bread or a large lettuce wrap.
    * **Filling:** Shredded cooked chicken breast mixed with plain Greek yogurt, diced celery, red onion, and grapes.
    * **Seasoning:** A pinch of salt, pepper, and a squeeze of lemon juice.

3.  **Lentil Soup:**
    * **Base:** A hearty soup made with brown or green lentils, vegetable broth, diced carrots, celery, and onions.
    * **Flavor:** Season with herbs like thyme and a bay leaf.
    * **Serving Suggestion:** Serve with a slice of whole-grain bread for dipping.
--------------------
```
