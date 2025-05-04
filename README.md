# Emotion Detector Application 
This application, developed as part of a course project, leverages natural language processing to detect emotions from input text. It analyzes the user's message and displays a range of emotions—such as joy, sadness, anger, and fear—each with its corresponding confidence level. The goal is to provide deeper insights into the emotional context of written communication.
### Technologies Used
-  Python – Used for building the core logic of the application.
  
-  Flask – A minimal web framework for creating the application interface and handling HTTP requests.
  
 - IBM Watson – A cloud-based AI tool that processes and analyzes emotional tones in text.
  
 - Pylint – A code linting tool that ensures consistent coding standards and detects potential issues.

### Real-World Use Cases
- Chatbots and Virtual Assistants: Enhance interactions by adapting responses based on the user’s emotional state.

- Online Education Platforms: Understand student feedback or learning frustration by analyzing their comments.

- Human Resources Tools: Analyze employee feedback to assess workplace morale and engagement.

- Content Moderation: Detect emotionally charged or potentially harmful content in online forums or social platforms.


# Prerequisite
1. Download the latest python version from its [offical website](https://www.python.org/downloads/) and validate the installation on terminal with help below command:
```
python --version
```
2. After the python is installed, install its libraries with the below commands:
 ```
pip3 install Flask
pip3 install pylint
pip3 install requests
```
# Project Activity
* Begin by cloning the repository from this [link]( https://github.com/ibm-developer-skills-network/oaqjp-final-project-emb-ai.git) to your local machine. This will provide all essential code and resources to get started.

* Make your changes locally and then push the updated project to your personal GitHub repository.

* Integrate the IBM Watson AI library to enable emotion detection based on user-input text.

* Ensure the emotion analysis results from Watson AI are cleanly formatted and easy for users to interpret.

* Prepare your application for deployment by packaging it properly and including simple, step-by-step deployment instructions.

* Create a dedicated file for unit tests to verify the application's logic and expected behavior.

* Use Flask to deploy the application so it can run in a web browser environment.

* Add error handling mechanisms to ensure your application can respond effectively to unexpected inputs or failures.

* Run static analysis with Pylint to catch coding issues early and enforce clean, maintainable code. for eg pylint sample.py


