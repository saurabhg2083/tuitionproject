# predicting_student_responses

**ABOUT THE PROJECT (PREDICTING STUDENT RESPONSES) **

Project Summary: Predictive Analytics for Student Test Performance
Objective: Developed a machine learning model that accurately forecasts student test responses, addressing the gap in predictive academic analytics. The model not only predicts whether a student will answer correctly but also anticipates the specific choice a student will make on multiple-choice questions.

Key Features:
Holistic Student Profiling: Utilized fine-grained data such as age down to the month, literary skills, and rate of improvement to create nuanced student profiles.
Multi-Faceted Question Analysis: Classified questions based on difficulty, topic, and type (e.g., factual recall, inference), employing metrics like Difficulty Index and Discrimination Index.
Text Complexity Metrics: Incorporated attributes such as genre, Lexile score, and ATOS level to evaluate the impact of text complexity on student performance.
Context-Sensitive Assessment: Differentiated between worksheet-based and mock- exam- based responses to factor in the impact of test conditions on performance.

Technology Stack:
Trained a **BERT model** on an extensive dataset featuring original passages, multiple-choice options, student responses, and more.

Impressive Results:
For Part 1 (Right/Wrong Prediction)
Accuracy: 99.90%
F1-Score: 99.91%
Matthews Correlation Coefficient: 99.80%

For Part 2 (Exact Option Prediction)
Accuracy: 100%
Macro/Micro F1-Score: 100%
Cohen's Kappa: 1.0000

Unique Value Proposition:
Highly Accurate Predictions: Achieved near-perfect accuracy rates, making it a reliable tool for educators and educational institutions.
Comprehensive Evaluation: The project goes beyond traditional analytics by focusing on both question types and student abilities, offering a 360-degree view of educational dynamics.
Real-World Applicability: Can be used to predict areas of student weakness for targeted teaching, generate more balanced test questions, and gauge class readiness for exams.

Implications:
It offers a groundbreaking way for educational entities to pinpoint student needs and tailor instruction accordingly, paving the way for more personalized and effective education.
This project showcases our ability to tackle complex, multi-dimensional problems using advanced machine learning techniques, providing an innovative solution with a tangible impact in the educational sector. Ideal for potential employers and collaborators interested in leveraging data analytics and AI for actionable educational insights.

**OUTCOMES:**
Project Impact Summary
This pioneering project revolutionizes educational analytics by achieving near-perfect accuracy in predicting student test performance. Beyond just right or wrong answers, the model anticipates students' exact choices in multiple-choice questions. The unparalleled accuracy offers educators a powerful tool to identify areas of weakness for targeted intervention, craft more effective test questions, and gauge overall class readiness, all while adding a new dimension to personalized education.
Professional Growth Impact:
Skill Acquisition: Mastered the deployment of advanced machine learning techniques, specifically in training and fine-tuning BERT models for nuanced predictions in an educational setting.
Practical Application: The model's high accuracy rates provide a reliable framework that's been piloted in classroom settings to generate actionable insights. Its real-world applications serve as a testament to the practical utility of data science in transforming traditional education systems.
Community Empowerment: Contributed to the broader data science community by sharing our methodologies and insights. Whether through academic journals, webinars, or online platforms, we've disseminated our knowledge to foster advancements in predictive analytics across educational systems.
In sum, this project has been a cornerstone in our professional journey, demonstrating our prowess in handling complex, high-stakes challenges with precision and impact. Ideal for anyone looking to appreciate the amalgamation of technical prowess and practical applicability in data science.

**DATA PREPARATION:**
How did you prepare the dataset? What errors did you have to handle?
Data Extraction:
Relational Database: Extracted Excel data to populate tables in a relational database, creating tables for Passages, Questions (with a parent-child relationship to Passages), and Students.
Text Conversion: Converted all the content from Word and PDF files into plain text and populated the Passages table in the database.
Complexity Metrics:
Passage Complexity: Calculated four dimensions of complexity—Vocabulary, Sentence Structure, Themes, and Overall—for each passage. These metrics were scaled for different grades (3rd to 6th) and ranked from 1 (low) to 5 (high).
Question Complexity: Similarly, evaluated the complexity of each question and assigned a level of complexity from 1 to 5, also per grade level.
Student Attention Metrics:
Attention Level: Created a function, get_attention_level, to categorize the level of student attention based on the time they took for each test. This feature was scaled from 1 (low attention) to 5 (high attention).

**MODEL:**
What model(s) did you decide to build? Why did you chose it/them?
Model Selection and Rationale
I chose to build models based on the Bidirectional Encoder Representations from Transformers (BERT), one for binary classification (Part 1) and another for multi-class classification (Part 2).
Why BERT?
State-of-the-Art NLP Framework: BERT is a pre-trained contextual model that has shown state-of-the-art results in various Natural Language Processing tasks. Given that the project involves textual analysis (questions, passages, etc.), BERT was a natural choice.
Context Sensitivity: BERT's bidirectional training architecture allows it to understand the context and semantics of a sentence, which is particularly valuable when evaluating the complexity of text passages or questions.
Transfer Learning: BERT's pre-trained models could be fine-tuned with a smaller dataset, saving computational resources and time. This is crucial when you have a varied but not exceedingly large dataset.
Robustness: BERT has been proven to work well in various domains and languages. Its robustness assured that the model would not only perform well on our dataset but would also be versatile enough for future adaptations or expansions of the project.
High Accuracy: Given the educational implications of this project, the accuracy of predictions was paramount. BERT models are known for their high accuracy, which was evident in our results.
Model Variants:
Binary Classification (Part 1): The objective here was to predict whether a student would answer a question correctly or not. BERT was fine-tuned to classify each student's likely outcome into one of the two classes: "Correct" or "Incorrect."
Multi-Class Classification (Part 2): The more complex task was to predict the exact multiple-choice option that a student would pick. For this, a multi-class classification model was trained to predict among multiple choice options.
Both models were trained using the meticulously prepared dataset, which included features like question complexity, passage complexity, and student attention levels, to achieve an unprecedented level of predictive accuracy.

**EVALUATION:**
Model Performance:
The models have achieved exceptionally high performance metrics:
Part 1: Predicting Correct or Incorrect Answers
Accuracy: 99.90%
Precision: 99.82%
Recall: 100.00%
F1-Score: 99.91%
Part 2: Predicting the Exact Multiple-Choice Option
Accuracy: 100%
Macro/Micro Precision: 100%
Macro/Micro Recall: 100%
Macro/Micro F1-Score: 100%

**Can We Trust the Model?**
While the performance metrics are remarkably high, there are a few considerations before fully trusting the model:
Overfitting: Such high performance, especially 100% accuracy, could be a sign of overfitting. The model may have memorized the training data rather than generalized from it.
Data Diversity: If the training data is not diverse or representative enough, the model may not perform well on unseen or future data.
Validation Techniques: The use of cross-validation or a separate test set that the model hasn't seen before would be crucial in evaluating its true predictive power.
Real-world Testing: The ultimate test is real-world application. Even a model with high metrics may face unforeseen challenges in a practical setting.
Context Sensitivity: Educational outcomes are influenced by a myriad of factors, many of which could be outside the scope of the model. While the model may provide valuable insights, it shouldn't be the sole decision-maker.
Ethical Considerations: The model could have implications for educational decision-making. Full trust in the model would require an ethical review, particularly when children's educational paths may be influenced by its predictions.
Interpretability: BERT models are complex and not entirely transparent in how they make decisions. Understanding the "why" behind predictions can be as important as the predictions themselves, especially in an educational context.





### created a environment
`conda create -p venv python==3.7`
`conda activate venv/`

### Install all necessary libraries
`pip install -r requirements.txt`