import json
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from sympy import true
from core.models import Course
from datetime import datetime

User = get_user_model()

COURSE_DATA = {
    "Machine Learning A-Z: AI, Python & R + ChatGPT Prize [2024]": {
        "Description": "Learn to create Machine Learning Algorithms in Python and R from two Data Science experts. Code templates included.",
        "Subscribers": 1027251,
        "Average Rating": 4.55,
        "Number of Reviews": 181209,
        "Number of Lectures": 384,
        "Content Length": "42.5 total hours",
        "Last Update": "2024-02-05",
        "Badges": ["Bestseller"],
        "Course Language": "English",
        "Instructional Level": "All Levels",
        "Authors": ["Kirill Eremenko", "Hadelin de Ponteves"],
        "Image URL": "https://img-c.udemycdn.com/course/125_H/950390_270f_3.jpg"
    },
    "Python for Data Science and Machine Learning Bootcamp": {
        "Description": "Learn Python for Data Science and Machine Learning.",
        "Subscribers": 150000,
        "Average Rating": 4.6,
        "Number of Reviews": 45000,
        "Number of Lectures": 120,
        "Content Length": "35 total hours",
        "Last Update": "2024-01-01",
        "Badges": ["Bestseller"],
        "Course Language": "English",
        "Instructional Level": "Beginner",
        "Authors": ["Jose Portilla"],
        "Image URL": "https://img-c.udemycdn.com/course/125_H/671576_a272_4.jpg"
    },

    "The Data Science Course: Complete Data Science Bootcamp 2024": {
        "Description": "Complete Data Science Training: Math, Statistics, Python, Advanced Statistics in Python, Machine and Deep Learning",
        "Is Paid": True,
        "Subscribers": 659718,
        "Average Rating": 4.5743966,
        "Number of Reviews": 135710,
        "Number of Lectures": 518,
        "Content Length": "31.5 total hours",
        "Last Update": "2024-01-30",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "365 Careers"
        ],
        "Course URL": "https://www.udemy.com/course/the-data-science-course-complete-data-science-bootcamp/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1754098_e0df_3.jpg"
    },
    "R Programming A-Z™: R For Data Science With Real Exercises!": {
        "Description": "Learn Programming In R And R Studio. Data Analytics, Data Science, Statistical Analysis, Packages, Functions, GGPlot2",
        "Is Paid": True,
        "Subscribers": 265416,
        "Average Rating": 4.623007,
        "Number of Reviews": 52902,
        "Number of Lectures": 80,
        "Content Length": "10.5 total hours",
        "Last Update": "2024-02-06",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Kirill Eremenko",
            "SuperDataScience Team",
            "Ligency Team"
        ],
        "Course URL": "https://www.udemy.com/course/r-programming/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/765242_2578_6.jpg"
    },
    "Deep Learning A-Z 2024: Neural Networks, AI & ChatGPT Prize": {
        "Description": "Learn to create Deep Learning models in Python from two Machine Learning, Data Science experts. Code templates included.",
        "Is Paid": True,
        "Subscribers": 373865,
        "Average Rating": 4.5336785,
        "Number of Reviews": 45202,
        "Number of Lectures": 192,
        "Content Length": "23 total hours", 
        "Last Update": "2024-02-05",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Kirill Eremenko",
            "Hadelin de Ponteves",
            "SuperDataScience Team",
            "Ligency Team"
        ],
        "Course URL": "https://www.udemy.com/course/deeplearning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1151632_de9b.jpg"
    },
    "Statistics for Data Science and Business Analysis": {
        "Description": "Statistics you need in the office: Descriptive & Inferential statistics, Hypothesis testing, Regression analysis",
        "Is Paid": True,
        "Subscribers": 194028,
        "Average Rating": 4.548471,
        "Number of Reviews": 41924,
        "Number of Lectures": 92,
        "Content Length": "5 total hours",
        "Last Update": "2023-08-14",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "365 Careers"
        ],
        "Course URL": "https://www.udemy.com/course/statistics-for-data-science-and-business-analysis/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1298780_731f_4.jpg"
    },
    "Artificial Intelligence A-Z 2024: Build 5 AI + LLM & ChatGPT": {
        "Description": "Combine the power of Data Science, Machine Learning and Deep Learning to create powerful AI for Real-World applications!",
        "Is Paid": True,
        "Subscribers": 256037,
        "Average Rating": 4.466843,
        "Number of Reviews": 36422,
        "Number of Lectures": 128,
        "Content Length": "15.5 total hours",
        "Last Update": "2024-02-05",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Hadelin de Ponteves",
            "Kirill Eremenko",
            "SuperDataScience Team",
            "Luka Anicin",
            "Ligency Team"
        ],
        "Course URL": "https://www.udemy.com/course/artificial-intelligence-az/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1219332_bdd7.jpg"
    },
    "Data Science A-Z: Hands-On Exercises & ChatGPT Prize [2024]": {
        "Description": "Learn Data Science step by step through real Analytics examples. Data Mining, Modeling, Tableau Visualization and more!",
        "Is Paid": True,
        "Subscribers": 216869,
        "Average Rating": 4.54067,
        "Number of Reviews": 33812,
        "Number of Lectures": 217,
        "Content Length": "21 total hours",
        "Last Update": "2024-02-06",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Kirill Eremenko",
            "SuperDataScience Team",
            "Ligency Team"
        ],
        "Course URL": "https://www.udemy.com/course/datascience/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/513244_b831_4.jpg"
    },
    "Machine Learning, Data Science and Generative AI with Python": {
        "Description": "Complete hands-on machine learning and AI tutorial with data science, Tensorflow, GPT, OpenAI, and neural networks",
        "Is Paid": True,
        "Subscribers": 191256,
        "Average Rating": 4.6046214,
        "Number of Reviews": 30571,
        "Number of Lectures": 140,
        "Content Length": "19 total hours",
        "Last Update": "2024-02-07",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Sundog Education by Frank Kane",
            "Frank Kane",
            "Sundog Education Team"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-and-machine-learning-with-python-hands-on/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/671576_a272_4.jpg"
    },
    "Python A-Z™: Python For Data Science With Real Exercises!": {
        "Description": "Programming In Python For Data Analytics And Data Science. Learn Statistical Analysis, Data Mining And Visualization",
        "Is Paid": True,
        "Subscribers": 160609,
        "Average Rating": 4.568507,
        "Number of Reviews": 27630,
        "Number of Lectures": 73,
        "Content Length": "11 total hours",
        "Last Update": "2024-02-06",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Kirill Eremenko",
            "SuperDataScience Team",
            "Ligency Team"
        ],
        "Course URL": "https://www.udemy.com/course/python-coding/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/913448_e6e2_4.jpg"
    },
    "Spark and Python for Big Data with PySpark": {
        "Description": "Learn how to use Spark with Python, including Spark Streaming, Machine Learning, Spark 2.0 DataFrames and more!",
        "Is Paid": True,
        "Subscribers": 129887,
        "Average Rating": 4.5252337,
        "Number of Reviews": 23466,
        "Number of Lectures": 67,
        "Content Length": "10.5 total hours",
        "Last Update": "2020-05-31",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Jose Portilla"
        ],
        "Course URL": "https://www.udemy.com/course/spark-and-python-for-big-data-with-pyspark/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/980798_6081.jpg"
    },
    "Master Data Engineering using GCP Data Analytics": {
        "Description": "Learn GCS for Data Lake, BigQuery for Data Warehouse, GCP Dataproc and Databricks for Big Data Pipelines",
        "Is Paid": true, 
        "Subscribers": 4699,
        "Average Rating": 4.5958905,
        "Number of Reviews": 406,
        "Number of Lectures": 283,
        "Conte nt Length": "19.5 total hours",
        "Last Update": "2023-11-08",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Durga Viswanatha Raju Gadiraju",
            "Kavitha Penmetsa"
        ],
        "Course URL": "https://www.udemy.com/course/master-data-engineering-using-gcp-data-analytics/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4918702_6284.jpg"
    },
    "Data Science in Python: Data Prep & EDA": {
        "Description": "Learn how to use Python & Pandas to gather, clean, explore and analyze data for Data Science and Machine Learning",
        "Is Paid": true,
        "Subscribers": 3389,
        "Average Rating": 4.756024,
        "Number of Reviews": 405,
        "Number of Lectures": 180,
        "Content Length": "8.5 total hours",
        "Last Update": "2023-09-26",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Maven Analytics",
            "Alice Zhao"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-in-python-data-prep-eda/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5457418_5f1f_2.jpg"
    },
    "Machine Learning for Data Science using MATLAB": {
        "Description": "Learn to implement classification and clustering algorithms using MATLAB with practical examples, projects and datasets",
        "Is Paid": true,
        "Subscribers": 2117,
        "Average Rating": 4.5,
        "Number of Reviews": 402,
        "Number of Lectures": 104,
        "Content Length": "16 total hours",
        "Last Update": "2023-01-11",
        "Badges": [],
        "Course Language": "English (UK)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Nouman Azam"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-for-datascience-using-matlab/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1378566_238b_3.jpg"
    },
    "Data Science:Data Mining & Natural Language Processing in R": {
        "Description": "Harness the Power of Machine Learning in R for Data/Text Mining, & Natural Language Processing with Practical Examples",
        "Is Paid": true,
        "Subscribers": 4305,
        "Average Rating": 4.45,
        "Number of Reviews": 401,
        "Number of Lectures": 112,
        "Content Length": "13.5 total hours",
        "Last Update": "2022-10-08",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Minerva Singh"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-datamining-natural-language-processing-in-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1413580_ead8_2.jpg"
    },
    "Time Series Analysis and Forecasting with Python": {
        "Description": "Learn Python for Pandas, Statsmodels, ARIMA, SARIMAX, Deep Learning, LSTM and Forecasting into Future",
        "Is Paid": true,
        "Subscribers": 5309,
        "Average Rating": 4.629032,
        "Number of Reviews": 395,
        "Number of Lectures": 52,
        "Content Length": "10.5 total hours",
        "Last Update": "2022-01-26",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Navid Shirzadi, Ph.D."
        ],
        "Course URL": "https://www.udemy.com/course/time-series-analysis-and-forecasting-with-python/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4228910_eb21_3.jpg"
    },
    "Reinforcement Learning with Pytorch": {
        "Description": "Learn to apply Reinforcement Learning and Artificial Intelligence algorithms using Python, Pytorch and OpenAI Gym",
        "Is Paid": true,
        "Subscribers": 2685,
        "Average Rating": 3.65,
        "Number of Reviews": 394,
        "Number of Lectures": 69,
        "Content Length": "7 total hours",
        "Last Update": "2020-08-09",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Atamai AI Team"
        ],
        "Course URL": "https://www.udemy.com/course/reinforcement-learning-with-pytorch/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1678738_a49b_2.jpg"
    },
    "Introduction to Natural Language Processing": {
        "Description": "Learn basics of Natural Language Processing (NLP), Regular Expressions and Text Pre-processing using Python",
        "Is Paid": true,
        "Subscribers": 17387,
        "Average Rating": 4.2,
        "Number of Reviews": 388,
        "Number of Lectures": 14,
        "Content Length": "1 total hour",
        "Last Update": "2020-02-06",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Analytics Vidhya"
        ],
        "Course URL": "https://www.udemy.com/course/introduction-to-natural-language-processing/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2796110_cc99_2.jpg"
    },
    "Complete Python and Machine Learning in Financial Analysis": {
        "Description": "Using Python, Machine Learning, and Deep Learning in Financial Analysis with step-by-step coding (with all codes)",
        "Is Paid": true,
        "Subscribers": 44366,
        "Average Rating": 4.6190476,
        "Number of Reviews": 387,
        "Number of Lectures": 83,
        "Content Length": "20.5 total hours",
        "Last Update": "2023-11-04",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "S. Emadedin Hashemi"
        ],
        "Course URL": "https://www.udemy.com/course/python-and-machine-learning-in-financial-analysis/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4248756_2478.jpg"
    },
    "The Ultimate Beginners Guide to Natural Language Processing": {
        "Description": "Learn step-by-step the main concepts of natural language processing in Python! Build a sentiment classifier!",
        "Is Paid": true,
        "Subscribers": 8460,
        "Average Rating": 4.409091,
        "Number of Reviews": 385,
        "Number of Lectures": 49,
        "Content Length": "6 total hours",
        "Last Update": "2023-04-27",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Jones Granatyr",
            "AI Expert Academy"
        ],
        "Course URL": "https://www.udemy.com/course/the-ultimate-beginners-guide-to-natural-language-processing/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4188850_3af0_2.jpg"
    },
    "Statistics for MBA/ Business statistics explained by example": {
        "Description": "Statistics Made Easy by Excel Simulations. Master most important concepts of introductory statistics through simulation",
        "Is Paid": true,
        "Subscribers": 2438,
        "Average Rating": 4.4,
        "Number of Reviews": 384,
        "Number of Lectures": 110,
        "Content Length": "15.5 total hours",
        "Last Update": "2021-01-26",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Gopal Prasad Malakar"
        ],
        "Course URL": "https://www.udemy.com/course/statistics-by-example/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/302174_400c_15.jpg"
    },
    "Computer Vision: Face Recognition Quick Starter in Python": {
        "Description": "Python Deep Learning based Face Detection, Recognition, Emotion , Gender and Age Classification using all popular models",
        "Is Paid": true,
        "Subscribers": 6153,
        "Average Rating": 4.1153846,
        "Number of Reviews": 384,
        "Number of Lectures": 93,
        "Content Length": "9.5 total hours",
        "Last Update": "2023-10-20",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Abhilash Nelson"
        ],
        "Course URL": "https://www.udemy.com/course/computer-vision-face-recognition-quick-starter-in-python/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/2835704_027a.jpg"
    },
    "Statistics with R - Intermediate Level": {
        "Description": "Statistical analyses using the R program",
        "Is Paid": true,
        "Subscribers": 31712,
        "Average Rating": 4.45,
        "Number of Reviews": 379,
        "Number of Lectures": 33,
        "Content Length": "2.5 total hours",
        "Last Update": "2020-12-08",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Bogdan Anastasiei"
        ],
        "Course URL": "https://www.udemy.com/course/statistics-with-r-intermediate-level/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/691892_ed21_2.jpg"
    },
    "Learn By Example: Statistics and Data Science in R": {
        "Description": "A gentle yet thorough introduction to Data Science, Statistics and R using real life examples",
        "Is Paid": true,
        "Subscribers": 4869,
        "Average Rating": 3.8,
        "Number of Reviews": 377,
        "Number of Lectures": 82,
        "Content Length": "9 total hours",
        "Last Update": "2016-12-01",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Loony Corn"
        ],
        "Course URL": "https://www.udemy.com/course/statistics-and-data-science-in-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/783694_3216_2.jpg"
    },
    "Machine Learning using Python Programming": {
        "Description": "Learn the core concepts of Machine Learning and its algorithms and how to implement them in Python 3",
        "Is Paid": true,
        "Subscribers": 34804,
        "Average Rating": 4.5,
        "Number of Reviews": 376,
        "Number of Lectures": 66,
        "Content Length": "8 total hours",
        "Last Update": "2023-04-14",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Sujithkumar MA"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-using-python-programming/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4108510_8a0b_4.jpg"
    },
    "Learn Machine Learning & Data Mining with Python": {
        "Description": "Learn Building Machine Learning & Deep Learning Models in Python, and use the Results in Data Mining Analyses",
        "Is Paid": true,
        "Subscribers": 1196,
        "Average Rating": 4.6,
        "Number of Reviews": 376,
        "Number of Lectures": 145,
        "Content Length": "8.5 total hours",
        "Last Update": "2023-05-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Data Science Guide"
        ],
        "Course URL": "https://www.udemy.com/course/implement-machine-learning-in-data-mining-using-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2568068_d073_2.jpg"
    },
    "Machine Learning: Build neural networks in 77 lines of code": {
        "Description": "Machine Learning and Artificial Intelligence for beginners. How to build a neural network in 77 lines of Python code.",
        "Is Paid": true,
        "Subscribers": 1308,
        "Average Rating": 4.6691175,
        "Number of Reviews": 372,
        "Number of Lectures": 18,
        "Content Length": "1 total hour",
        "Last Update": "2019-01-10",
        "Badges": [],
        "Course Language": "English (UK)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Milo Spencer-Harper"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-build-a-neural-network-in-77-lines-of-code/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2134920_7eb7_2.jpg"
    },
    "Data Visualization with Power BI Simplified": {
        "Description": "\"Unlocking the Power of Data: A Comprehensive Guide to Building Dynamic Dashboards and Visualizations with Power BI\"",
        "Is Paid": true,
        "Subscribers": 22026,
        "Average Rating": 4.167742,
        "Number of Reviews": 370,
        "Number of Lectures": 16,
        "Content Length": "1.5 total hours",
        "Last Update": "2023-04-21",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Okot Samuel"
        ],
        "Course URL": "https://www.udemy.com/course/data-visualization-with-power-bi-simplified/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5264010_1352.jpg"
    },
    "Natural Language Processing: NLP In Python with 2 Projects": {
        "Description": "Learn NLP with Machine Learning Algorithms, Spacy, NLTK, TextBlob for Text Processing, Text Classification and Much More",
        "Is Paid": true,
        "Subscribers": 20708,
        "Average Rating": 4.2580647,
        "Number of Reviews": 368,
        "Number of Lectures": 61,
        "Content Length": "3 total hours",
        "Last Update": "2022-03-24",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Dataisgood Academy"
        ],
        "Course URL": "https://www.udemy.com/course/nlp-bootcamp-machine-learning-deep-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4182296_a852.jpg"
    },
    "Python Data Visualization: Matplotlib & Seaborn Masterclass": {
        "Description": "Bring your data to LIFE and master Python's most popular data analytics & visualization libraries: Matplotlib & Seaborn",
        "Is Paid": true,
        "Subscribers": 3887,
        "Average Rating": 4.631579,
        "Number of Reviews": 367,
        "Number of Lectures": 94,
        "Content Length": "7.5 total hours",
        "Last Update": "2023-09-26",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Maven Analytics",
            "Chris Bruehl"
        ],
        "Course URL": "https://www.udemy.com/course/python-data-visualization-matplotlib-seaborn/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4943118_c9aa.jpg"
    },
    "Clustering & Classification With Machine Learning In Python": {
        "Description": "Harness The Power Of Machine Learning For Unsupervised & Supervised Learning In Python",
        "Is Paid": true,
        "Subscribers": 7722,
        "Average Rating": 4.435484,
        "Number of Reviews": 363,
        "Number of Lectures": 60,
        "Content Length": "6 total hours",
        "Last Update": "2022-11-01",
        "Badges": [],
        "Course Language": "English (UK)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Minerva Singh"
        ],
        "Course URL": "https://www.udemy.com/course/clustering-classification-with-machine-learning-in-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1533128_44d0_2.jpg"
    },
    "Logistic Regression in R Studio": {
        "Description": "Logistic regression in R Studio tutorial for beginners. You can do Predictive modeling using R Studio after this course.",
        "Is Paid": true,
        "Subscribers": 94544,
        "Average Rating": 4.3076925,
        "Number of Reviews": 363,
        "Number of Lectures": 77,
        "Content Length": "6.5 total hours",
        "Last Update": "2024-01-12",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Start-Tech Academy"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-basics-classification-models-in-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2332706_b5c4_2.jpg"
    },
    "Practical Data Science: Analyzing Stock Market Data with R": {
        "Description": "Learn basic financial technical analysis technics using R (quantmod, TTR) to better understand your favorites stocks. ",
        "Is Paid": true,
        "Subscribers": 2374,
        "Average Rating": 4.45,
        "Number of Reviews": 362,
        "Number of Lectures": 18,
        "Content Length": "4 total hours",
        "Last Update": "2017-06-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Manuel Amunategui"
        ],
        "Course URL": "https://www.udemy.com/course/practical-data-science-analyzing-stock-market-data-with-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/570544_da05_5.jpg"
    },
    "2024 Deployment of Machine Learning Models in Production": {
        "Description": "Deploy ML Model with BERT, DistilBERT, FastText NLP Models in Production with Flask, uWSGI, and NGINX at AWS EC2",
        "Is Paid": true,
        "Subscribers": 18200,
        "Average Rating": 4.4411764,
        "Number of Reviews": 362,
        "Number of Lectures": 85,
        "Content Length": "9.5 total hours",
        "Last Update": "2024-01-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Laxmi Kant | KGP Talkie"
        ],
        "Course URL": "https://www.udemy.com/course/nlp-with-bert-in-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3174934_b2df_4.jpg"
    },
    "Generate and visualize data in Python and MATLAB": {
        "Description": "Learn how to simulate and visualize data for data science, statistics, and machine learning in MATLAB and Python",
        "Is Paid": true,
        "Subscribers": 20191,
        "Average Rating": 4.6,
        "Number of Reviews": 360,
        "Number of Lectures": 46,
        "Content Length": "6.5 total hours",
        "Last Update": "2024-01-31",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Mike X Cohen"
        ],
        "Course URL": "https://www.udemy.com/course/suv-data-mxc/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1470452_deda_4.jpg"
    },
    "Microsoft Azure Cognitive Services Crash Course": {
        "Description": "Build Smart Applications in Minutes with Azure Cognitive Vision, Language, Speech, Decision and Search services",
        "Is Paid": true,
        "Subscribers": 9405,
        "Average Rating": 4.5375,
        "Number of Reviews": 358,
        "Number of Lectures": 56,
        "Content Length": "5 total hours",
        "Last Update": "2022-01-10",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Reza Salehi"
        ],
        "Course URL": "https://www.udemy.com/course/azure-cognitive-services-crash-course/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2037902_7fb9_16.jpg"
    },
    "Linear Algebra Mastery for Data Science & ML Math Essentials": {
        "Description": "Master Linear Algebra: Essential Math for Data Science, Machine Learning, and Deep Learning Applications - Your Key to M",
        "Is Paid": true,
        "Subscribers": 4938,
        "Average Rating": 4.35,
        "Number of Reviews": 357,
        "Number of Lectures": 196,
        "Content Length": "24.5 total hours",
        "Last Update": "2024-01-09",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Manifold AI Learning \u00ae"
        ],
        "Course URL": "https://www.udemy.com/course/linear-algebra-for-data-science-machine-learning-ai/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2027668_2508_3.jpg"
    },
    "Artificial Neural Network and Machine Learning using MATLAB": {
        "Description": "Learn to Create Neural Network with Matlab Toolbox and Easy to Follow Codes; with Comprehensive Theoretical Concepts",
        "Is Paid": true,
        "Subscribers": 1284,
        "Average Rating": 4.2916665,
        "Number of Reviews": 356,
        "Number of Lectures": 52,
        "Content Length": "4.5 total hours",
        "Last Update": "2022-07-28",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Nastaran Reza Nazar Zadeh"
        ],
        "Course URL": "https://www.udemy.com/course/artificial-neural-network-and-machine-learning-using-matlab/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3412802_e83e_2.jpg"
    },
    "Machine Learning using Python": {
        "Description": "Linear & Logistic Regression, Decision Trees, XGBoost, SVM & other ML models in Python",
        "Is Paid": true,
        "Subscribers": 17061,
        "Average Rating": 4.5,
        "Number of Reviews": 351,
        "Number of Lectures": 159,
        "Content Length": "19 total hours",
        "Last Update": "2024-01-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Start-Tech Academy"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-using-python-starttech/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4850130_02dd_2.jpg"
    },
    "Object Detection Web App with TensorFlow, OpenCV and Flask": {
        "Description": "Build an Object Detection Model from Scratch using Deep Learning and Transfer Learning",
        "Is Paid": true,
        "Subscribers": 52351,
        "Average Rating": 4.25,
        "Number of Reviews": 351,
        "Number of Lectures": 10,
        "Content Length": "1 total hour",
        "Last Update": "2021-01-14",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Yaswanth Sai Palaghat"
        ],
        "Course URL": "https://www.udemy.com/course/object-detection-web-app-with-tensorflow-opencv-and-flask/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/3498426_13e8_3.jpg"
    },
    "Machine Learning Optimization Using Genetic Algorithm": {
        "Description": "Learn how to optimize Machine Learning algorithms' performances and apply feature selection using Genetic Algorithm",
        "Is Paid": true,
        "Subscribers": 2972,
        "Average Rating": 3.65,
        "Number of Reviews": 349,
        "Number of Lectures": 57,
        "Content Length": "6.5 total hours",
        "Last Update": "2020-08-08",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Curiosity for Data Science"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-optimization-using-genetic-algorithm/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/1602180_c701_4.jpg"
    },
    "Deploy Machine Learning Models on GCP + AWS Lambda (Docker)": {
        "Description": "How to Serialize - Deserialize model with scikit-learn & Deployment on Heroku, AWS Lambda, ECS, Docker and Google Cloud",
        "Is Paid": true,
        "Subscribers": 3489,
        "Average Rating": 4.75,
        "Number of Reviews": 348,
        "Number of Lectures": 53,
        "Content Length": "4.5 total hours",
        "Last Update": "2021-10-08",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Ankit Mistry",
            "Data Science & Machine Learning Academy"
        ],
        "Course URL": "https://www.udemy.com/course/deploy-machine-learning-model/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/2796454_1311_8.jpg"
    },
    "TensorFlow 2.0 Practical Advanced": {
        "Description": "Master Tensorflow 2.0, Google\u2019s most powerful Machine Learning Library, with 5 advanced practical projects",
        "Is Paid": true,
        "Subscribers": 5278,
        "Average Rating": 3.95,
        "Number of Reviews": 343,
        "Number of Lectures": 83,
        "Content Length": "12.5 total hours",
        "Last Update": "2023-12-22",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Dr. Ryan Ahmed, Ph.D., MBA",
            "SuperDataScience Team",
            "Mitchell Bouchard",
            "Ligency Team"
        ],
        "Course URL": "https://www.udemy.com/course/tensorflow-2-practical-advanced/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/2517920_755e_4.jpg"
    },
    "A/B Testing in Python": {
        "Description": "Learn How To Define, Start, And Analyze The Results Of An A/B Test. Improve Business Performance Through A/B Testing",
        "Is Paid": true,
        "Subscribers": 2315,
        "Average Rating": 4.3703704,
        "Number of Reviews": 342,
        "Number of Lectures": 27,
        "Content Length": "3 total hours",
        "Last Update": "2022-04-20",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "365 Careers",
            "Anastasia K"
        ],
        "Course URL": "https://www.udemy.com/course/ab-testing-in-python/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4613156_acaf_2.jpg"
    },
    "Bayesian Computational Analyses with R": {
        "Description": "Learn the concepts and practical side of using the Bayesian approach to estimate likely event outcomes.",
        "Is Paid": true,
        "Subscribers": 3925,
        "Average Rating": 4.25,
        "Number of Reviews": 342,
        "Number of Lectures": 82,
        "Content Length": "11.5 total hours",
        "Last Update": "2020-09-28",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Geoffrey Hubona, Ph.D."
        ],
        "Course URL": "https://www.udemy.com/course/bayesian-computational-analyses-with-r/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/616072_2b5d_5.jpg"
    },
    "Machine Learning : A Beginner's Basic Introduction": {
        "Description": "Learn Machine  Learning Basics with a Practical Example",
        "Is Paid": true,
        "Subscribers": 25391,
        "Average Rating": 4.25,
        "Number of Reviews": 342,
        "Number of Lectures": 17,
        "Content Length": "2 total hours",
        "Last Update": "2021-06-09",
        "Badges": [],
        "Course Language": "English (UK)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Bluelime Learning Solutions"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-a-beginners-basic-introduction/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/1613970_447c_4.jpg"
    },
    "Data Science Mega-Course: #Build {120-Projects In 120-Days}": {
        "Description": "Build & Deploy Data Science, Machine Learning, Deep Learning (Python, Flask, Django, AWS, Azure, GCP, Heruko Cloud)",
        "Is Paid": true,
        "Subscribers": 5429,
        "Average Rating": 4.090909,
        "Number of Reviews": 337,
        "Number of Lectures": 800,
        "Content Length": "132.5 total hours",
        "Last Update": "2022-09-06",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Pianalytix ."
        ],
        "Course URL": "https://www.udemy.com/course/real-world-data-science-projects-using-python/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4538648_c13e_2.jpg"
    },
    "ML for Business Managers: Build Regression model in R Studio": {
        "Description": "Simple Regression & Multiple Regression| must-know for Machine Learning & Econometrics | Linear Regression in R studio",
        "Is Paid": true,
        "Subscribers": 78416,
        "Average Rating": 4.65,
        "Number of Reviews": 337,
        "Number of Lectures": 72,
        "Content Length": "6.5 total hours",
        "Last Update": "2024-01-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Start-Tech Academy"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-basics-building-a-regression-model-in-r/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/2236090_a6f5_6.jpg"
    },
    "No-Code Machine Learning Using Amazon AWS SageMaker Canvas": {
        "Description": "Build your Machine Learning Model and get accurate predictions without writing any Code using AWS SageMaker Canvas",
        "Is Paid": true,
        "Subscribers": 52645,
        "Average Rating": 4.172414,
        "Number of Reviews": 332,
        "Number of Lectures": 26,
        "Content Length": "1.5 total hours",
        "Last Update": "2021-12-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Prince Patni"
        ],
        "Course URL": "https://www.udemy.com/course/no-code-machine-learning-using-amazon-aws-sagemaker-canvas/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4429048_7e67_2.jpg"
    },
    "Natural Language Processing: Machine Learning NLP In Python": {
        "Description": "A Complete Beginner NLP Syllabus. Practicals: Linguistics, Flask,Sentiment, Scrape Tweets, Chatbot, Hugging Face & more!",
        "Is Paid": true,
        "Subscribers": 2625,
        "Average Rating": 3.8,
        "Number of Reviews": 329,
        "Number of Lectures": 178,
        "Content Length": "19.5 total hours",
        "Last Update": "2021-11-10",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Nidia Sahjara",
            "Rajeev D. Ratan"
        ],
        "Course URL": "https://www.udemy.com/course/nidia-natural-language-processing-deep-learning-zero-to-hero/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4000788_1ce5_3.jpg"
    },
    "Data Engineer/Data Scientist  - Power BI/ Python/ ETL/SSIS": {
        "Description": "Hands-on Data  Interaction and Manipulation.",
        "Is Paid": true,
        "Subscribers": 33730,
        "Average Rating": 4.3,
        "Number of Reviews": 328,
        "Number of Lectures": 124,
        "Content Length": "13.5 total hours",
        "Last Update": "2021-06-12",
        "Badges": [],
        "Course Language": "English (UK)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Bluelime Learning Solutions"
        ],
        "Course URL": "https://www.udemy.com/course/data-engineerdata-scientist-power-bi-python-etlssis/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4011242_08f1_3.jpg"
    },
    "Machine Learning with Python from Scratch": {
        "Description": "Mastering Machine Learning Algorithms including Neural Networks with Numpy, Pandas, Matplotlib, Seaborn and Scikit-Learn",
        "Is Paid": true,
        "Subscribers": 4528,
        "Average Rating": 3.9,
        "Number of Reviews": 325,
        "Number of Lectures": 64,
        "Content Length": "12.5 total hours",
        "Last Update": "2023-11-22",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Tim Buchalka's Learn Programming Academy",
            "CARLOS QUIROS"
        ],
        "Course URL": "https://www.udemy.com/course/python-machine-learning/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/1673570_30b1.jpg"
    },
    "Maths for Data Science by DataTrained": {
        "Description": "Explore the application of key mathematical topics related to linear algebra with the Python programming language",
        "Is Paid": true,
        "Subscribers": 23034,
        "Average Rating": 3.8,
        "Number of Reviews": 325,
        "Number of Lectures": 13,
        "Content Length": "1 total hour",
        "Last Update": "2019-03-18",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "DataTrained Education"
        ],
        "Course URL": "https://www.udemy.com/course/maths-for-data-science-by-datatrained/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/2272560_a2ca_2.jpg"
    },
    "Practical MLOps: AWS Mastery for Data Scientists & DevOps": {
        "Description": "Empower Your MLOps Journey: AWS AI/ML Mastery - From Notebook to Production Operation with Expert Guidance - MLOps 2024",
        "Is Paid": true,
        "Subscribers": 3775,
        "Average Rating": 4.5439563,
        "Number of Reviews": 325,
        "Number of Lectures": 159,
        "Content Length": "30.5 total hours",
        "Last Update": "2024-01-24",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Manifold AI Learning \u00ae"
        ],
        "Course URL": "https://www.udemy.com/course/practical-mlops-for-data-scientists-devops-engineers-aws/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4393768_cb15_3.jpg"
    },
    "Artificial Intelligence with Machine Learning, Deep Learning": {
        "Description": "Artificial Intelligence (AI) with Python Machine Learning and Python Deep Learning, Transfer Learning, Tensorflow",
        "Is Paid": true,
        "Subscribers": 2649,
        "Average Rating": 4.5731707,
        "Number of Reviews": 324,
        "Number of Lectures": 171,
        "Content Length": "23 total hours",
        "Last Update": "2024-02-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Oak Academy",
            "OAK Academy Team"
        ],
        "Course URL": "https://www.udemy.com/course/artificial-intelligence-with-machine-learning-deep-learning/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4415712_daac_10.jpg"
    },
    "Statistics in R - The R Language for Statistical Analysis": {
        "Description": "Statistics made easy with the open source R language. Learn about Regression, Hypothesis tests, R Commander ...",
        "Is Paid": true,
        "Subscribers": 3372,
        "Average Rating": 4.45,
        "Number of Reviews": 322,
        "Number of Lectures": 43,
        "Content Length": "4 total hours",
        "Last Update": "2018-11-29",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "R-Tutorials Training"
        ],
        "Course URL": "https://www.udemy.com/course/statisticsinr/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/330386_49fd_5.jpg"
    },
    "Dell Boomi AtomSphere - IPaaS Beginner Training": {
        "Description": "Master the fundamentals of Dell Boomi AtomSphere",
        "Is Paid": true,
        "Subscribers": 1636,
        "Average Rating": 4.1923075,
        "Number of Reviews": 321,
        "Number of Lectures": 24,
        "Content Length": "5.5 total hours",
        "Last Update": "2021-03-26",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Saad Qureshi"
        ],
        "Course URL": "https://www.udemy.com/course/dellboomi/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2889584_4ad2_2.jpg"
    },
    "2023 CORE: Data Science and Machine Learning": {
        "Description": "A complete survey of all core skills required on the job",
        "Is Paid": true,
        "Subscribers": 3143,
        "Average Rating": 4.6153846,
        "Number of Reviews": 321,
        "Number of Lectures": 267,
        "Content Length": "28.5 total hours",
        "Last Update": "2023-08-28",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Dr. Isaac Faber"
        ],
        "Course URL": "https://www.udemy.com/course/core-data-science-and-machine-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4287096_6357_2.jpg"
    },
    "ChatGPT: GPT-3, GPT-4 Turbo: Unleash the Power of LLM's": {
        "Description": "Your Gateway to AI-Powered Creativity and Innovation",
        "Is Paid": true,
        "Subscribers": 23733,
        "Average Rating": 4.85,
        "Number of Reviews": 320,
        "Number of Lectures": 130,
        "Content Length": "15 total hours",
        "Last Update": "2023-12-01",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Avinash A"
        ],
        "Course URL": "https://www.udemy.com/course/open-ais-generative-pre-trained-transformer-3-gpt3/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5020244_56cc.jpg"
    },
    "Machine Learning with Python : COMPLETE COURSE FOR BEGINNERS": {
        "Description": "Complete Machine Learning Course with Python for beginners",
        "Is Paid": true,
        "Subscribers": 23828,
        "Average Rating": 4.5757575,
        "Number of Reviews": 318,
        "Number of Lectures": 35,
        "Content Length": "13 total hours",
        "Last Update": "2023-11-22",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Selfcode Academy"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-a-z-with-python-with-project-beginner/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4391444_88fb_3.jpg"
    },
    "Natural Language Processing for Text Summarization": {
        "Description": "Understand the basic theory and implement three algorithms step by step in Python! Implementations from scratch!",
        "Is Paid": true,
        "Subscribers": 15571,
        "Average Rating": 4.483871,
        "Number of Reviews": 316,
        "Number of Lectures": 44,
        "Content Length": "5 total hours",
        "Last Update": "2023-04-27",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Jones Granatyr",
            "AI Expert Academy"
        ],
        "Course URL": "https://www.udemy.com/course/text-summarization-natural-language-processing-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4059902_d952_3.jpg"
    },
    "Artificial Intelligence (AI) in Software Testing": {
        "Description": "The Future of Automated Testing with Machine Learning - Implementing Artificial Intelligence (AI) in Test Automation",
        "Is Paid": true,
        "Subscribers": 1152,
        "Average Rating": 3.659091,
        "Number of Reviews": 311,
        "Number of Lectures": 37,
        "Content Length": "1.5 total hours",
        "Last Update": "2019-01-12",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Sujal Patel"
        ],
        "Course URL": "https://www.udemy.com/course/artificial-intelligence-ai-in-software-testing/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1674948_4fce_2.jpg"
    },
    "Complete Pandas for Absolute Beginners 2023": {
        "Description": "Learn how to use the powerful Python pandas library to analyze and manipulate data.",
        "Is Paid": true,
        "Subscribers": 35912,
        "Average Rating": 4.2093024,
        "Number of Reviews": 309,
        "Number of Lectures": 8,
        "Content Length": "1 total hour",
        "Last Update": "2023-01-19",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Hassan Shoayb"
        ],
        "Course URL": "https://www.udemy.com/course/complete-pandas-for-absolute-beginners/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5097114_5ee1_2.jpg"
    },
    "Image Recognition for Beginners using CNN in R Studio": {
        "Description": "Deep Learning based Convolutional Neural Networks (CNN) for Image recognition using Keras and Tensorflow in R Studio",
        "Is Paid": true,
        "Subscribers": 83556,
        "Average Rating": 4.5,
        "Number of Reviews": 307,
        "Number of Lectures": 59,
        "Content Length": "6.5 total hours",
        "Last Update": "2024-01-12",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Start-Tech Academy"
        ],
        "Course URL": "https://www.udemy.com/course/cnn-for-computer-vision-with-keras-and-tensorflow-in-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2755960_4129.jpg"
    },
    "TensorFlow and the Google Cloud ML Engine for Deep Learning": {
        "Description": "CNNs, RNNs and other neural networks for unsupervised and supervised deep learning",
        "Is Paid": true,
        "Subscribers": 4163,
        "Average Rating": 4.55,
        "Number of Reviews": 306,
        "Number of Lectures": 132,
        "Content Length": "17.5 total hours",
        "Last Update": "2018-07-11",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Loony Corn"
        ],
        "Course URL": "https://www.udemy.com/course/from-0-to-1-tensorflow-for-deep-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1474682_cc04_2.jpg"
    },
    "Linear Regression and Logistic Regression using R Studio": {
        "Description": "Linear Regression and Logistic Regression for beginners. Understand the difference between Regression & Classification",
        "Is Paid": true,
        "Subscribers": 60098,
        "Average Rating": 4.571429,
        "Number of Reviews": 305,
        "Number of Lectures": 63,
        "Content Length": "6 total hours",
        "Last Update": "2024-01-12",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Start-Tech Academy"
        ],
        "Course URL": "https://www.udemy.com/course/linear-regression-and-logistic-regression-r-studio-starttech/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3215305_e355_2.jpg"
    },
    "Data Science with Python (beginner to expert)": {
        "Description": "Start your career as Data Scientist from scratch. Learn Data Science with Python. Predict trends with advanced analytics",
        "Is Paid": true,
        "Subscribers": 30675,
        "Average Rating": 4.65,
        "Number of Reviews": 302,
        "Number of Lectures": 56,
        "Content Length": "44.5 total hours",
        "Last Update": "2020-12-04",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Uplatz Training"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-with-python-certification-training/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3665928_9aa1_4.jpg"
    },
    "Automated Machine Learning for Beginners (Google & Apple)": {
        "Description": "Learn AI: Computer Vision, NLP, Tabular Data - build powerful models with Google AutoML & Apple CreateML",
        "Is Paid": true,
        "Subscribers": 64863,
        "Average Rating": 4.5212765,
        "Number of Reviews": 298,
        "Number of Lectures": 92,
        "Content Length": "3.5 total hours",
        "Last Update": "2023-10-05",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "AIBrain Inc."
        ],
        "Course URL": "https://www.udemy.com/course/automl-for-ai-powered-professionals/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4204684_a7e6_2.jpg"
    },
    "Decision Tree - Theory, Application and Modeling using R": {
        "Description": "Analytics/ Supervised Machine Learning/ Data Science: CHAID / CART / Random Forest etc. workout (Python demo at the end)",
        "Is Paid": true,
        "Subscribers": 1897,
        "Average Rating": 4.8,
        "Number of Reviews": 298,
        "Number of Lectures": 71,
        "Content Length": "8 total hours",
        "Last Update": "2021-01-27",
        "Badges": [
            "Highest Rated"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Gopal Prasad Malakar"
        ],
        "Course URL": "https://www.udemy.com/course/decision-tree-theory-application-and-modeling-using-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/367468_f78f_5.jpg"
    },
    "Complete iOS Machine Learning Masterclass": {
        "Description": "The most comprehensive course on Machine Learning for iOS development. Master building smart apps iOS Swift 4",
        "Is Paid": true,
        "Subscribers": 16807,
        "Average Rating": 4.65,
        "Number of Reviews": 298,
        "Number of Lectures": 97,
        "Content Length": "7.5 total hours",
        "Last Update": "2017-08-28",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Yohann Taieb"
        ],
        "Course URL": "https://www.udemy.com/course/complete-ios-machine-learning-masterclass/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1246246_04dd_5.jpg"
    },
    "Python for Data Science & Machine Learning: Zero to Hero": {
        "Description": "Master Data Science & Machine Learning in Python: Numpy, Pandas, Matplotlib, Scikit-Learn, Machine Learning, and more!",
        "Is Paid": true,
        "Subscribers": 42918,
        "Average Rating": 4.265306,
        "Number of Reviews": 297,
        "Number of Lectures": 187,
        "Content Length": "6 total hours",
        "Last Update": "2024-01-16",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Meta Brains"
        ],
        "Course URL": "https://www.udemy.com/course/python-for-data-science-machine-learning-zero-to-hero/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4928056_3bdd.jpg"
    },
    "Intelligently Extract Text & Data from Document with OCR NER": {
        "Description": "Develop Document Scanner App project that is Named entity extraction from scan documents with OpenCV, Pytesseract, Spacy",
        "Is Paid": true,
        "Subscribers": 2634,
        "Average Rating": 4.6216216,
        "Number of Reviews": 295,
        "Number of Lectures": 89,
        "Content Length": "7.5 total hours",
        "Last Update": "2023-11-12",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "G Sudheer",
            "Data Science Anywhere",
            "Brightshine Learn"
        ],
        "Course URL": "https://www.udemy.com/course/business-card-reader-app/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4107158_9338_5.jpg"
    },
    "Deploy Serverless Machine Learning Models to AWS Lambda": {
        "Description": "Use Serverless Framework for fast deployment of different ML models to scalable and cost-effective AWS Lambda service.",
        "Is Paid": true,
        "Subscribers": 2570,
        "Average Rating": 4.05,
        "Number of Reviews": 290,
        "Number of Lectures": 62,
        "Content Length": "8 total hours",
        "Last Update": "2020-12-27",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Milan Pavlovi\u0107"
        ],
        "Course URL": "https://www.udemy.com/course/deploy-serverless-machine-learning-models-to-aws-lambda/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2094130_84db.jpg"
    },
    "The Complete Visual Guide to Machine Learning & Data Science": {
        "Description": "Explore Data Science & Machine Learning topics with simple, step-by-step demos and user-friendly Excel models (NO code!)",
        "Is Paid": true,
        "Subscribers": 3041,
        "Average Rating": 4.647059,
        "Number of Reviews": 287,
        "Number of Lectures": 182,
        "Content Length": "9 total hours",
        "Last Update": "2023-12-07",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Maven Analytics",
            "Chris Dutton",
            "Joshua MacCarty"
        ],
        "Course URL": "https://www.udemy.com/course/visual-guide-to-machine-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5190450_bd9e_3.jpg"
    },
    "Complete Data Science BootCamp 2024": {
        "Description": "Learn about Data Science, Machine Learning and Deep Learning and build 5 different projects.",
        "Is Paid": true,
        "Subscribers": 35406,
        "Average Rating": 4.2265625,
        "Number of Reviews": 286,
        "Number of Lectures": 54,
        "Content Length": "7.5 total hours",
        "Last Update": "2023-01-13",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Raj Chhabria"
        ],
        "Course URL": "https://www.udemy.com/course/complete-data-science-bootcamp/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5078474_ed8a_2.jpg"
    },
    "Prompt Engineering: Getting Future Ready (1000+ Prompts inc)": {
        "Description": "Prompt Engineering for beginners in 2023. 1000+ prompts, resources, and templates for ChatGPT and Image-to-Image & text",
        "Is Paid": true,
        "Subscribers": 2194,
        "Average Rating": 4.1911764,
        "Number of Reviews": 287,
        "Number of Lectures": 47,
        "Content Length": "7 total hours",
        "Last Update": "2024-01-31",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Yash Thakker"
        ],
        "Course URL": "https://www.udemy.com/course/prompt-engineering-course/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5204002_8402_5.jpg"
    },
    "Master Vector Database with Python for AI & LLM Use Cases": {
        "Description": "Learn Vector Database using Python, Pinecone, LangChain, Open AI, Hugging Face and build out AI, ML , Chat applications",
        "Is Paid": true,
        "Subscribers": 2747,
        "Average Rating": 4.3680553,
        "Number of Reviews": 285,
        "Number of Lectures": 58,
        "Content Length": "7 total hours",
        "Last Update": "2023-10-03",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Dr. KM Mohsin"
        ],
        "Course URL": "https://www.udemy.com/course/vector-db/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5326682_5b87_3.jpg"
    },
    "Data Science for Professionals": {
        "Description": "It's time to leave spreadsheets behind...",
        "Is Paid": true,
        "Subscribers": 7144,
        "Average Rating": 4.681818,
        "Number of Reviews": 284,
        "Number of Lectures": 33,
        "Content Length": "6.5 total hours",
        "Last Update": "2018-11-30",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Gregory Sward"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-for-professionals/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1886862_e7e0_3.jpg"
    },
    "Real Life Machine Learning and Data Science Projects[2024]": {
        "Description": "Build Data Science and ML Projects and Land on Dream job as Data Scientists or Data Analyst-Handson Projects",
        "Is Paid": true,
        "Subscribers": 2114,
        "Average Rating": 4.763889,
        "Number of Reviews": 282,
        "Number of Lectures": 64,
        "Content Length": "2.5 total hours",
        "Last Update": "2022-10-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Sheik Jamil Ahmed"
        ],
        "Course URL": "https://www.udemy.com/course/real-life-machine-learning-and-data-science-projects/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4799174_78af_4.jpg"
    },
    "neural networks for sentiment and stock price prediction": {
        "Description": "How to predict stock prices with neural networks and sentiment with neural networks. Machine learning hands on data scie",
        "Is Paid": true,
        "Subscribers": 1680,
        "Average Rating": 4.45,
        "Number of Reviews": 280,
        "Number of Lectures": 21,
        "Content Length": "3 total hours",
        "Last Update": "2023-05-03",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Dan We"
        ],
        "Course URL": "https://www.udemy.com/course/neural-networks-for-stock-price-prediction-and-sentiment/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2062941_0a75_2.jpg"
    },
    "Exploring The Technologies Behind ChatGPT, GPT4 & LLMs": {
        "Description": "COMPLETELY REDONE - The only course you need to learn large language models (LLMs) - ChatGPT, GPT4, BERT &amp; More!",
        "Is Paid": true,
        "Subscribers": 2553,
        "Average Rating": 4.364865,
        "Number of Reviews": 274,
        "Number of Lectures": 84,
        "Content Length": "9.5 total hours",
        "Last Update": "2024-02-08",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Justin Coleman",
            "Tim Reynolds"
        ],
        "Course URL": "https://www.udemy.com/course/exploring-the-technologies-behind-chatgpt-openai/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5027500_2df0_2.jpg"
    },
    "Tensorflow Deep Learning - Data Science in Python": {
        "Description": "Tensorflow Deep Learning Python : Tensorflow Neural Network Training : Tensorflow Models - Android Java : Tensorflow C#",
        "Is Paid": true,
        "Subscribers": 3174,
        "Average Rating": 4.7,
        "Number of Reviews": 272,
        "Number of Lectures": 71,
        "Content Length": "7.5 total hours",
        "Last Update": "2022-11-01",
        "Badges": [],
        "Course Language": "English (UK)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Minerva Singh"
        ],
        "Course URL": "https://www.udemy.com/course/tensorflow-bootcamp-for-data-science-in-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1776912_8b00_2.jpg"
    },
    "Data Science & Machine Learning: Naive Bayes in Python": {
        "Description": "Master a crucial artificial intelligence algorithm and skyrocket your Python programming skills",
        "Is Paid": true,
        "Subscribers": 3789,
        "Average Rating": 4.75,
        "Number of Reviews": 272,
        "Number of Lectures": 45,
        "Content Length": "7.5 total hours",
        "Last Update": "2024-02-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Lazy Programmer Inc.",
            "Lazy Programmer Team"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-machine-learning-naive-bayes-in-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4929064_b97d.jpg"
    },
    "Deep learning for object detection using Tensorflow 2": {
        "Description": "Understand, train and evaluate Faster RCNN, SSD and YOLO v3 models using Tensorflow 2 and Google AI Platform",
        "Is Paid": true,
        "Subscribers": 2353,
        "Average Rating": 4.6666665,
        "Number of Reviews": 271,
        "Number of Lectures": 72,
        "Content Length": "10 total hours",
        "Last Update": "2023-04-29",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Nour Islam Mokhtari"
        ],
        "Course URL": "https://www.udemy.com/course/deep-learning-for-object-detection-using-tensorflow-2/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3511868_3296_3.jpg"
    },
    "2022 Python Bootcamp for Data Science Numpy Pandas & Seaborn": {
        "Description": "With Exercises : Learn to use NumPy, Pandas, Seaborn , Matplotlib  for Data Manipulation and Exploration with Python",
        "Is Paid": true,
        "Subscribers": 39405,
        "Average Rating": 4.05,
        "Number of Reviews": 270,
        "Number of Lectures": 91,
        "Content Length": "6.5 total hours",
        "Last Update": "2021-10-19",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Taher Assaf"
        ],
        "Course URL": "https://www.udemy.com/course/python-bootcamp-for-data-science-2021-numpy-pandas-seaborn/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4058268_057d_5.jpg"
    },
    "Practical Introduction to Machine Learning with Python": {
        "Description": "Quickly Learn the Essentials of Artificial Intelligence (AI) and Machine Learning (ML)",
        "Is Paid": true,
        "Subscribers": 10605,
        "Average Rating": 4.3,
        "Number of Reviews": 269,
        "Number of Lectures": 58,
        "Content Length": "4.5 total hours",
        "Last Update": "2020-05-17",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Madhu Siddalingaiah"
        ],
        "Course URL": "https://www.udemy.com/course/practical-machine-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2133386_5ce2.jpg"
    },
    "Deep Learning Masterclass with TensorFlow 2 Over 20 Projects": {
        "Description": "Master Deep Learning with TensorFlow 2 with Computer Vision,Natural Language Processing, Sound Recognition & Deployment",
        "Is Paid": true,
        "Subscribers": 4322,
        "Average Rating": 4.084746,
        "Number of Reviews": 267,
        "Number of Lectures": 205,
        "Content Length": "63.5 total hours",
        "Last Update": "2023-08-27",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Neuralearn Dot AI"
        ],
        "Course URL": "https://www.udemy.com/course/deep-learning-masterclass-with-tensorflow-2-over-15-projects/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4735368_d75d_4.jpg"
    },
    "RASA :Build and Deploy Chatbot On The Cloud (100% FREE)": {
        "Description": "Your RASA Course Guide From Installation to Deployment And Get Your RASA Certification !",
        "Is Paid": true,
        "Subscribers": 33121,
        "Average Rating": 3.95,
        "Number of Reviews": 267,
        "Number of Lectures": 27,
        "Content Length": "2 total hours",
        "Last Update": "2021-02-09",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Yassine AI"
        ],
        "Course URL": "https://www.udemy.com/course/create-artificial-intelligent-chatbot-with-rasa-in-one-hour/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3230665_2f86_14.jpg"
    },
    "Computer Vision: YOLO Custom Object Detection with Colab GPU": {
        "Description": "YOLO: Pre-Trained Coco Dataset and Custom Trained Coronavirus Object Detection Model with Google Colab GPU Training",
        "Is Paid": true,
        "Subscribers": 3758,
        "Average Rating": 3.95,
        "Number of Reviews": 265,
        "Number of Lectures": 48,
        "Content Length": "4 total hours",
        "Last Update": "2023-01-08",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Abhilash Nelson"
        ],
        "Course URL": "https://www.udemy.com/course/computer-vision-yolo-custom-object-detection-with-colab-gpu/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/3129498_45ae_6.jpg"
    },
    "Beginner's Guide to Python Data Analysis & Visualization": {
        "Description": "Get started on data science with pandas and numpy from scratch in Python 3. Learn thoroughly, with breeze.",
        "Is Paid": true,
        "Subscribers": 3440,
        "Average Rating": 4.1,
        "Number of Reviews": 264,
        "Number of Lectures": 51,
        "Content Length": "4 total hours",
        "Last Update": "2021-12-30",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Alan Y",
            "Rake Smith"
        ],
        "Course URL": "https://www.udemy.com/course/complete-pandas-bootcamp-with-python-3/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/931456_9597.jpg"
    },
    "Cluster Analysis- Theory & workout using  SAS and R": {
        "Description": "Unsupervised Machine Learning  : Hierarchical & non hierarchical clustering (k-means), theory & SAS / R program",
        "Is Paid": true,
        "Subscribers": 1975,
        "Average Rating": 4.5,
        "Number of Reviews": 264,
        "Number of Lectures": 64,
        "Content Length": "6.5 total hours",
        "Last Update": "2022-07-23",
        "Badges": [],
        "Course Language": "English (India)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Gopal Prasad Malakar"
        ],
        "Course URL": "https://www.udemy.com/course/cluster-analysis-motivation-theory-practical-application/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/150714_9ade_8.jpg"
    },
    "Object Tracking using Python and OpenCV": {
        "Description": "Implement 12 different algorithms for tracking objects in videos and webcam!",
        "Is Paid": true,
        "Subscribers": 2382,
        "Average Rating": 4.3076925,
        "Number of Reviews": 262,
        "Number of Lectures": 34,
        "Content Length": "5 total hours",
        "Last Update": "2023-04-27",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Jones Granatyr",
            "Dalton Luiz Vargas",
            "AI Expert Academy"
        ],
        "Course URL": "https://www.udemy.com/course/object-tracking-using-python-and-opencv/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4382164_f5df_2.jpg"
    },
    "Python for Data Analytics - Beginner to Advanced": {
        "Description": "Learn Python for Data Analytics. Learn how to analyze and visualize different data types and do projects with them.",
        "Is Paid": true,
        "Subscribers": 22125,
        "Average Rating": 3.5714285,
        "Number of Reviews": 262,
        "Number of Lectures": 40,
        "Content Length": "2 total hours",
        "Last Update": "2023-08-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Onur Baltac\u0131"
        ],
        "Course URL": "https://www.udemy.com/course/python-for-data-analytics/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4854204_9a21.jpg"
    },
    "DP-100 Azure Data Scientist Associate Complete Exam Guide": {
        "Description": "Complete DP-100 Azure Machine Learning training guide to prepare you for DP-100, with practice exams on DP 100 Azure ML",
        "Is Paid": true,
        "Subscribers": 1921,
        "Average Rating": 4.39,
        "Number of Reviews": 261,
        "Number of Lectures": 96,
        "Content Length": "8.5 total hours",
        "Last Update": "2022-11-29",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Henry Habib"
        ],
        "Course URL": "https://www.udemy.com/course/dp-100-azure-data-scientist-associate-complete-exam-guide/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4992188_0f74_2.jpg"
    },
    "YOLOv8: Object Detection, Tracking & Web App in Python 2023": {
        "Description": "YOLOv8, Train Custom Dataset, Object Detection, Segmentation, Tracking, Real World 17 + Projects & Web Apps in Python",
        "Is Paid": true,
        "Subscribers": 2475,
        "Average Rating": 4.3175673,
        "Number of Reviews": 261,
        "Number of Lectures": 46,
        "Content Length": "12 total hours",
        "Last Update": "2023-07-13",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Muhammad Moin"
        ],
        "Course URL": "https://www.udemy.com/course/yolov8-the-ultimate-course-for-object-detection-tracking/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5134858_bd37_3.jpg"
    },
    "iOS Machine Learning with Core ML 2 and Swift 5": {
        "Description": "Learn how to integrate machine learning into iOS apps. Hands-on Swift 5 coding using CoreML 2, Vision, NLP and CreateML.",
        "Is Paid": true,
        "Subscribers": 1942,
        "Average Rating": 4.1944447,
        "Number of Reviews": 261,
        "Number of Lectures": 45,
        "Content Length": "2 total hours",
        "Last Update": "2024-02-04",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Karoly Nyisztor \u2022 Professional Software Architect"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-with-core-ml-2-and-swift/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1691490_a442_7.jpg"
    },
    "Explainable Al (XAI) with Python": {
        "Description": "Simplified Way to Learn XAI",
        "Is Paid": true,
        "Subscribers": 2923,
        "Average Rating": 4.4074073,
        "Number of Reviews": 261,
        "Number of Lectures": 56,
        "Content Length": "8 total hours",
        "Last Update": "2022-07-06",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Parteek Bhatia",
            "DeepFindr YouTube"
        ],
        "Course URL": "https://www.udemy.com/course/xai-with-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4362666_843c_3.jpg"
    },
    "Data Science and Machine Learning Masterclass with R": {
        "Description": "Data Science by IITan - Data Science :Data Manipulation , Data Science Data Visualization, Data Science : Data Analytics",
        "Is Paid": true,
        "Subscribers": 9432,
        "Average Rating": 4.45,
        "Number of Reviews": 259,
        "Number of Lectures": 152,
        "Content Length": "15 total hours",
        "Last Update": "2019-05-10",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Up Degree"
        ],
        "Course URL": "https://www.udemy.com/course/business-analytics-with-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1726730_0cac_3.jpg"
    },
    "Machine Learning for Apps": {
        "Description": "Start building more intelligent apps with Machine Learning. Take advantage of this new foundational framework!",
        "Is Paid": true,
        "Subscribers": 11367,
        "Average Rating": 4.55,
        "Number of Reviews": 257,
        "Number of Lectures": 42,
        "Content Length": "7 total hours",
        "Last Update": "2017-10-19",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Devslopes by Mark Wahlbeck"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-for-apps/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1400924_5598.jpg"
    },
    "Applied Machine Learning in R": {
        "Description": "Get the essential machine learning skills and use them in real life situations",
        "Is Paid": true,
        "Subscribers": 23987,
        "Average Rating": 4.75,
        "Number of Reviews": 256,
        "Number of Lectures": 80,
        "Content Length": "8 total hours",
        "Last Update": "2020-12-08",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Bogdan Anastasiei"
        ],
        "Course URL": "https://www.udemy.com/course/applied-machine-learning-in-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1221664_ef84_3.jpg"
    },
    "The Complete Artificial Intelligence for Cyber Security 2022": {
        "Description": "Combine the power of Data Science, Machine Learning and Deep Learning to create powerful AI for Real-World applications",
        "Is Paid": true,
        "Subscribers": 2417,
        "Average Rating": 4.4583335,
        "Number of Reviews": 256,
        "Number of Lectures": 99,
        "Content Length": "14.5 total hours",
        "Last Update": "2023-08-22",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Hoang Quy La"
        ],
        "Course URL": "https://www.udemy.com/course/the-complete-artificial-intelligence-for-cyber-security-2021/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3941384_b658.jpg"
    },
    "The Complete Intro to Machine Learning": {
        "Description": "Hands-on ML with Python, Pandas, Regression, Decision Trees, Neural Networks, and more!",
        "Is Paid": true,
        "Subscribers": 27465,
        "Average Rating": 4.15,
        "Number of Reviews": 255,
        "Number of Lectures": 30,
        "Content Length": "5 total hours",
        "Last Update": "2023-02-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Student ML Coalition",
            "Michael Lutz",
            "Arjun Rajaram",
            "Saurav Kumar",
            "Aswin Surya",
            "Chatanya Sarin"
        ],
        "Course URL": "https://www.udemy.com/course/the-complete-intro-to-machine-learning-with-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4348164_8c92_2.jpg"
    },
    "Spark Scala coding framework, testing, Structured streaming": {
        "Description": "Spark Scala Framework, Hive, IntelliJ, Maven, Logging, Exception Handling, log4j, ScalaTest, JUnit, Structured Streaming",
        "Is Paid": true,
        "Subscribers": 3840,
        "Average Rating": 4.4,
        "Number of Reviews": 255,
        "Number of Lectures": 57,
        "Content Length": "5 total hours",
        "Last Update": "2024-01-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "FutureX Skills"
        ],
        "Course URL": "https://www.udemy.com/course/spark-scala-coding-best-practices-data-pipeline/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2927256_a2b8_12.jpg"
    },
    "The Comprehensive Programming in R Course": {
        "Description": "How to design and develop efficient general-purpose R applications for diverse tasks and domains.",
        "Is Paid": true,
        "Subscribers": 3265,
        "Average Rating": 4.6,
        "Number of Reviews": 255,
        "Number of Lectures": 120,
        "Content Length": "25 total hours",
        "Last Update": "2020-08-01",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Geoffrey Hubona, Ph.D."
        ],
        "Course URL": "https://www.udemy.com/course/the-comprehensive-programming-in-r-course/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/584472_d901.jpg"
    },
    "Introduction To Data Science": {
        "Description": "Your First Step Into The Data Science Journey",
        "Is Paid": true,
        "Subscribers": 6638,
        "Average Rating": 3.7,
        "Number of Reviews": 131,
        "Number of Lectures": 9,
        "Content Length": "1 total hour",
        "Last Update": "2021-06-24",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Intro School"
        ],
        "Course URL": "https://www.udemy.com/course/introduction-to-data-science-c/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4139800_1038.jpg"
    },
    "Build 75 Powerful Data Science & Machine Learning Projects": {
        "Description": "Build & Deploy Data Science, Machine Learning, Deep Learning (Python, Flask, Django, AWS, Azure, GCP, Heruko Cloud)",
        "Is Paid": true,
        "Subscribers": 3693,
        "Average Rating": 3.9318182,
        "Number of Reviews": 253,
        "Number of Lectures": 555,
        "Content Length": "73.5 total hours",
        "Last Update": "2022-03-04",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Pianalytix ."
        ],
        "Course URL": "https://www.udemy.com/course/real-world-data-science-projects-practically/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4539666_59cb.jpg"
    },
    "Introduction to Python Programming (for Data Analytics)": {
        "Description": "Learn the fundamentals of the python programming language for data analytics. Practice and solution resources included.",
        "Is Paid": true,
        "Subscribers": 10921,
        "Average Rating": 4.25,
        "Number of Reviews": 252,
        "Number of Lectures": 16,
        "Content Length": "2 total hours",
        "Last Update": "2023-10-19",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Valentine Mwangi"
        ],
        "Course URL": "https://www.udemy.com/course/learn-python-for-data-science/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2733832_eec6_4.jpg"
    },
    "LLM Fine Tuning on OpenAI": {
        "Description": "Learn to use OpenAI to fine tune LLMs on your own datasets!",
        "Is Paid": true,
        "Subscribers": 1801,
        "Average Rating": 4.513944,
        "Number of Reviews": 251,
        "Number of Lectures": 11,
        "Content Length": "2 total hours",
        "Last Update": "2023-12-11",
        "Badges": [
            "Hot & New"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Jose Portilla"
        ],
        "Course URL": "https://www.udemy.com/course/llm-fine-tuning-on-openai/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5637510_87bd.jpg"
    },
    "The Comprehensive Statistics and Data Science with R Course": {
        "Description": "Learn how to use R for data science tasks, all about R data structures, functions and visualizations, and statistics.",
        "Is Paid": true,
        "Subscribers": 2880,
        "Average Rating": 4.45,
        "Number of Reviews": 251,
        "Number of Lectures": 219,
        "Content Length": "19.5 total hours",
        "Last Update": "2019-10-09",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Geoffrey Hubona, Ph.D."
        ],
        "Course URL": "https://www.udemy.com/course/comprcourse/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/929220_c5f2_2.jpg"
    },
    "Data Analysis with Polars": {
        "Description": "Transform your data analysis with Polars - the powerful new dataframe library",
        "Is Paid": true,
        "Subscribers": 1784,
        "Average Rating": 4.5113635,
        "Number of Reviews": 249,
        "Number of Lectures": 67,
        "Content Length": "3 total hours",
        "Last Update": "2024-02-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Liam Brannigan"
        ],
        "Course URL": "https://www.udemy.com/course/data-analysis-with-polars/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4788902_03fe_6.jpg"
    },
    "Learn LangChain: Build #22 LLM Apps using OpenAI & Llama 2": {
        "Description": "Build Real World LLM powered applications with LangChain, OpenAI, Llama2, Hugging Face. Create Web Apps with Streamlit.",
        "Is Paid": true,
        "Subscribers": 2125,
        "Average Rating": 4.04,
        "Number of Reviews": 249,
        "Number of Lectures": 56,
        "Content Length": "18 total hours",
        "Last Update": "2023-12-12",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Muhammad Moin"
        ],
        "Course URL": "https://www.udemy.com/course/learn-langchain-build-12-llm-apps-using-openai-llama-2/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5456432_f40f.jpg"
    },
    "Create Interactive Dashboards in Python by Plotly Dash": {
        "Description": "Create interactive data science web dashboards using the Plotly data visualizations library and Dash library in Python.",
        "Is Paid": true,
        "Subscribers": 2064,
        "Average Rating": 3.6,
        "Number of Reviews": 249,
        "Number of Lectures": 146,
        "Content Length": "23.5 total hours",
        "Last Update": "2023-04-22",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Mubeen Ali"
        ],
        "Course URL": "https://www.udemy.com/course/create-interactive-dashboards-in-python-by-plotly-dash/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3710786_9f96_4.jpg"
    },
    "The Complete Python and JavaScript Course: Build Projects": {
        "Description": "Want to learn ES6 development and TensorFlow stock market prediction modeling? Build your first web app in this course!",
        "Is Paid": true,
        "Subscribers": 24982,
        "Average Rating": 4.05,
        "Number of Reviews": 248,
        "Number of Lectures": 228,
        "Content Length": "27 total hours",
        "Last Update": "2018-07-26",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Mammoth Interactive",
            "John Bura"
        ],
        "Course URL": "https://www.udemy.com/course/the-complete-python-and-javascript-course-build-projects/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/1820022_8e85.jpg"
    },
    "40 Real World Data Science, Machine Learning Projects 2023": {
        "Description": "Learn To Build & Deploy AI, ML, DS, Deep Learning, NLP Web Apps With Python Projects Course(Flask, Django, Heruko Cloud)",
        "Is Paid": true,
        "Subscribers": 7398,
        "Average Rating": 3.95,
        "Number of Reviews": 248,
        "Number of Lectures": 250,
        "Content Length": "29.5 total hours",
        "Last Update": "2023-11-01",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Pianalytix ."
        ],
        "Course URL": "https://www.udemy.com/course/intro-to-machine-learning-course/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3474510_5d2c_4.jpg"
    },
    "Text Analysis and Natural Language Processing With Python": {
        "Description": "Use Python and Google CoLab For Social Media Mining and Text Analysis and Natural Language Processing (NLP)",
        "Is Paid": true,
        "Subscribers": 1788,
        "Average Rating": 4.478261,
        "Number of Reviews": 244,
        "Number of Lectures": 70,
        "Content Length": "5 total hours",
        "Last Update": "2023-11-15",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Minerva Singh"
        ],
        "Course URL": "https://www.udemy.com/course/text-analysis-and-natural-language-processing-with-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4038326_82d8_2.jpg"
    },
    "Machine Learning In The Cloud With Azure Machine Learning": {
        "Description": "Introduction to machine learning in the cloud with Azure Machine Learning.",
        "Is Paid": true,
        "Subscribers": 5595,
        "Average Rating": 4.1,
        "Number of Reviews": 243,
        "Number of Lectures": 35,
        "Content Length": "3 total hours",
        "Last Update": "2019-02-07",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "TetraNoodle Team",
            "Manuj Aggarwal"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-in-the-cloud-with-azure-machine-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1568060_4df3_2.jpg"
    },
    "ChatGPT Productivity + Time Management. ChatGPT Productivity": {
        "Description": "ChatGPT To Dramatically Improve Productivity + Unusual Time Mgmt. Tips. ChatGPT Work, Chat GPT Automation, ChatGPT 2023!",
        "Is Paid": true,
        "Subscribers": 4729,
        "Average Rating": 4.328358,
        "Number of Reviews": 242,
        "Number of Lectures": 43,
        "Content Length": "3.5 total hours",
        "Last Update": "2024-01-25",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Steve Ballinger, MBA"
        ],
        "Course URL": "https://www.udemy.com/course/chatgpt-foundation-course-complete-chatgpt-course-chatgpt-new/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5154496_86fe_4.jpg"
    },
    "Introduction to AI, Machine Learning and Python basics": {
        "Description": "Learn to understand Artificial Intelligence and Machine Learning algorithms, and learn the basics of Python Programming",
        "Is Paid": true,
        "Subscribers": 4673,
        "Average Rating": 4.478261,
        "Number of Reviews": 242,
        "Number of Lectures": 21,
        "Content Length": "2.5 total hours",
        "Last Update": "2021-10-29",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Timur Kazantsev"
        ],
        "Course URL": "https://www.udemy.com/course/introduction-to-ai-machine-learning-and-python-basics/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2907564_d74d.jpg"
    },
    "Linear Regression, GLMs and GAMs with R": {
        "Description": "How to extend linear regression to specify and estimate generalized linear models and additive models.",
        "Is Paid": true,
        "Subscribers": 2300,
        "Average Rating": 4.0,
        "Number of Reviews": 242,
        "Number of Lectures": 69,
        "Content Length": "8 total hours",
        "Last Update": "2020-09-28",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Geoffrey Hubona, Ph.D."
        ],
        "Course URL": "https://www.udemy.com/course/linear-regression-glms-and-gams-with-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/701416_2a37_6.jpg"
    },
    "Exploratory Data Analysis in Python": {
        "Description": "A course about how to approach a dataset for the first time",
        "Is Paid": true,
        "Subscribers": 5889,
        "Average Rating": 4.1911764,
        "Number of Reviews": 242,
        "Number of Lectures": 15,
        "Content Length": "2 total hours",
        "Last Update": "2021-10-18",
        "Badges": [],
        "Course Language": "English (UK)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Gianluca Malato"
        ],
        "Course URL": "https://www.udemy.com/course/exploratory-data-analysis-in-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4354856_6617.jpg"
    },
    "Data Science:Hands-on Covid19 Face Mask Detection-CNN&OpenCV": {
        "Description": "A Practical Hands-on Data Science Guided Project on Covid-19 Face Mask Detection using Deep Learning & OpenCV",
        "Is Paid": true,
        "Subscribers": 10704,
        "Average Rating": 4.45,
        "Number of Reviews": 241,
        "Number of Lectures": 10,
        "Content Length": "2 total hours",
        "Last Update": "2020-11-16",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "School of Disruptive Innovation"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-hands-on-covid19-face-mask-detection-cnn-opencv/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3631178_7914_5.jpg"
    },
    "One Week of Data Science in Python - New 2024!": {
        "Description": "Master Data Science Fundamentals Quickly &amp; Efficiently in one week! Course is Designed for Busy People",
        "Is Paid": true,
        "Subscribers": 3421,
        "Average Rating": 4.630435,
        "Number of Reviews": 238,
        "Number of Lectures": 136,
        "Content Length": "13 total hours",
        "Last Update": "2023-12-22",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Dr. Ryan Ahmed, Ph.D., MBA",
            "SuperDataScience Team",
            "Ligency Team"
        ],
        "Course URL": "https://www.udemy.com/course/one-week-of-data-science/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4722740_e014_4.jpg"
    },
    "Machine Learning : Complete Maths for Machine Learning": {
        "Description": "Learn Math for Machine Learning, Math for Data Science, Linear Algebra, Calculus, Vectors & Matrices, Probability & more",
        "Is Paid": true,
        "Subscribers": 1162,
        "Average Rating": 4.65625,
        "Number of Reviews": 237,
        "Number of Lectures": 25,
        "Content Length": "2.5 total hours",
        "Last Update": "2022-04-04",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Jitesh Khurkhuriya",
            "Python, Data Science & Machine Learning A-Z Team"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-2020-complete-maths-for-machine-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2674092_8ec5_3.jpg"
    },
    "Modern Data Analysis Masterclass in Pandas and Python": {
        "Description": "Build your Data Analysis and Visualization skills with Python\u2019s Pandas, Numpy, Matplotlib and Seaborn Libraries",
        "Is Paid": true,
        "Subscribers": 2563,
        "Average Rating": 4.8,
        "Number of Reviews": 237,
        "Number of Lectures": 177,
        "Content Length": "21 total hours",
        "Last Update": "2023-12-22",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Dr. Ryan Ahmed, Ph.D., MBA",
            "Ligency Team",
            "Mitchell Bouchard",
            "SuperDataScience Team"
        ],
        "Course URL": "https://www.udemy.com/course/modern-data-analytics-masterclass/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4012126_22cd.jpg"
    },
    "Improving data quality in data analytics & machine learning": {
        "Description": "Learn why, when, and how to maximize the quality of your data to optimize data-based decisions",
        "Is Paid": true,
        "Subscribers": 2156,
        "Average Rating": 4.6625,
        "Number of Reviews": 236,
        "Number of Lectures": 45,
        "Content Length": "5.5 total hours",
        "Last Update": "2024-01-31",
        "Badges": [
            "Highest Rated"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Mike X Cohen"
        ],
        "Course URL": "https://www.udemy.com/course/dataqc_x/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4604146_fb24.jpg"
    },
    "R for Data Science: Learn R Programming in 2 Hours": {
        "Description": "Enter the world of R Programming: Everything you need to get started with R and Data Science in just 2 HOURS!",
        "Is Paid": true,
        "Subscribers": 3910,
        "Average Rating": 4.2,
        "Number of Reviews": 235,
        "Number of Lectures": 35,
        "Content Length": "2 total hours",
        "Last Update": "2022-02-03",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Ajay Warrier"
        ],
        "Course URL": "https://www.udemy.com/course/r-for-data-science-learn-r-programming-in-2-hours/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2444730_2e40.jpg"
    },
    "Statistics Masterclass for Data Science and Data Analytics": {
        "Description": "Build a Solid Foundation of Statistics for Data Science, Learn Probability, Distributions, Hypothesis Testing, and More!",
        "Is Paid": true,
        "Subscribers": 1198,
        "Average Rating": 4.65,
        "Number of Reviews": 234,
        "Number of Lectures": 43,
        "Content Length": "5 total hours",
        "Last Update": "2023-10-03",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Vijay Gadhave"
        ],
        "Course URL": "https://www.udemy.com/course/statistics-for-data-science-and-analytics-masterclass/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2367448_faf7_2.jpg"
    },
    "Generative AI & ChatGPT : Text, Image and Code completion": {
        "Description": "Guides and projects to guide you through all the steps required to get started with OpenAI, Codex and DALLe. APIs",
        "Is Paid": true,
        "Subscribers": 1080,
        "Average Rating": 4.2972975,
        "Number of Reviews": 234,
        "Number of Lectures": 42,
        "Content Length": "2 total hours",
        "Last Update": "2023-04-16",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Sandra L. Sorel"
        ],
        "Course URL": "https://www.udemy.com/course/gpt-3-open-ai-api-dalle-api-codex-quickstart/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5103812_7f50_4.jpg"
    },
    "Machine Learning Essentials (2023) - Master core ML concepts": {
        "Description": "Kickstart Machine Learning, understand maths behind essential algorithms, implement them in python & build 8+ projects!",
        "Is Paid": true,
        "Subscribers": 2989,
        "Average Rating": 4.380435,
        "Number of Reviews": 234,
        "Number of Lectures": 198,
        "Content Length": "28 total hours",
        "Last Update": "2023-05-23",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Mohit Uniyal",
            "Prateek Narang"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-artificial-intelligence-essentials/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4244284_46e8.jpg"
    },
    "Sentiment Analysis with NLP using Python and Flask": {
        "Description": "Along with a Project",
        "Is Paid": true,
        "Subscribers": 32763,
        "Average Rating": 4.2,
        "Number of Reviews": 233,
        "Number of Lectures": 16,
        "Content Length": "1.5 total hours",
        "Last Update": "2021-01-14",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Yaswanth Sai Palaghat"
        ],
        "Course URL": "https://www.udemy.com/course/sentiment-analysis-with-nlp-using-python-flask/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3432584_2aca_5.jpg"
    },
    "Essential Calculus for Data Science & Machine Learning": {
        "Description": "Master Calculus: Essential Math for Deep Learning, Machine Learning, Data Science, Data Analysis, and AI - Hands-On",
        "Is Paid": true,
        "Subscribers": 3159,
        "Average Rating": 4.590909,
        "Number of Reviews": 233,
        "Number of Lectures": 112,
        "Content Length": "13 total hours",
        "Last Update": "2024-01-09",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Manifold AI Learning \u00ae"
        ],
        "Course URL": "https://www.udemy.com/course/deep-learning-calculus-data-science-machine-learning-ai/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2113900_e5cd_4.jpg"
    },
    "How to Become A Data Scientist Using Azure Machine Learning": {
        "Description": "A Practical Introduction To Microsoft's Azure Machine Learning Tools",
        "Is Paid": true,
        "Subscribers": 1189,
        "Average Rating": 3.85,
        "Number of Reviews": 231,
        "Number of Lectures": 39,
        "Content Length": "1 total hour",
        "Last Update": "2015-12-28",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Mike West"
        ],
        "Course URL": "https://www.udemy.com/course/azure-machine-learning-introduction/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/691182_95a0.jpg"
    },
    "ChatGPT for Data Science and Data Analysis in Python": {
        "Description": "Learn to Leverage AI to Fast-Track Your Data Science Project Execution, Data Analysis, Data Visualization and Reporting",
        "Is Paid": true,
        "Subscribers": 2570,
        "Average Rating": 4.2,
        "Number of Reviews": 231,
        "Number of Lectures": 37,
        "Content Length": "4 total hours",
        "Last Update": "2023-12-21",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Tony Simonovsky",
            "Ligency Team",
            "SuperDataScience Team"
        ],
        "Course URL": "https://www.udemy.com/course/chatgpt-for-data-science-and-data-analysis-in-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5225024_863f.jpg"
    },
    "Data science and Data preparation with KNIME": {
        "Description": "KNIME - a powerful tool for data science and machine learning Data science with higher efficiency. KNIME data cleaning",
        "Is Paid": true,
        "Subscribers": 1917,
        "Average Rating": 4.7727275,
        "Number of Reviews": 230,
        "Number of Lectures": 65,
        "Content Length": "11 total hours",
        "Last Update": "2024-01-01",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Dan We"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-and-data-preparation-with-knime/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3024566_62fb_4.jpg"
    },
    "YOLO: Automatic License Plate Detection & Extract text App": {
        "Description": "Learn to Develop License Plate Object Detection, OCR and Create Web App Project using Deep Learning, TensorFlow 2, Flask",
        "Is Paid": true,
        "Subscribers": 1844,
        "Average Rating": 4.2,
        "Number of Reviews": 230,
        "Number of Lectures": 77,
        "Content Length": "5.5 total hours",
        "Last Update": "2023-09-22",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Data Science Anywhere",
            "G Sudheer",
            "Brightshine Learn"
        ],
        "Course URL": "https://www.udemy.com/course/deep-learning-web-app-project-number-plate-detection-ocr/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3893664_51a6_3.jpg"
    },
    "Artificial Intelligence for Simple Games": {
        "Description": "Learn how to use powerful Deep Reinforcement Learning and Artificial Intelligence tools on examples of AI simple games!",
        "Is Paid": true,
        "Subscribers": 2513,
        "Average Rating": 3.7,
        "Number of Reviews": 230,
        "Number of Lectures": 120,
        "Content Length": "12.5 total hours",
        "Last Update": "2023-12-21",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Jan Warchocki",
            "SuperDataScience Team",
            "Ligency Team"
        ],
        "Course URL": "https://www.udemy.com/course/artificial-intelligence-for-simple-games/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2472890_03c6_2.jpg"
    },
    "Practical Neural Networks & Deep Learning In R": {
        "Description": "Artificial Intelligence & Machine Learning for Practical Data Science in R",
        "Is Paid": true,
        "Subscribers": 1859,
        "Average Rating": 4.95,
        "Number of Reviews": 229,
        "Number of Lectures": 53,
        "Content Length": "5.5 total hours",
        "Last Update": "2021-10-31",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Minerva Singh"
        ],
        "Course URL": "https://www.udemy.com/course/practical-neural-networks-deep-learning-in-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1637178_aeed.jpg"
    },
    "Automated Multiple Face Recognition AI Using Python": {
        "Description": "Learn about OpenCv Basics, Face Recognition in an image, Automation of Face Recognition System using User Inputs",
        "Is Paid": true,
        "Subscribers": 19682,
        "Average Rating": 3.85,
        "Number of Reviews": 228,
        "Number of Lectures": 10,
        "Content Length": "2 total hours",
        "Last Update": "2019-11-11",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Nishit Maru",
            "Three Millennials"
        ],
        "Course URL": "https://www.udemy.com/course/automated-multiple-face-recognition-ai-using-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2648784_d21b.jpg"
    },
    "Question Generation using Natural Language processing": {
        "Description": "Auto generate assessments in edtech like MCQs, True/False, Fill-in-the-blanks etc using state-of-the-art NLP techniques",
        "Is Paid": true,
        "Subscribers": 865,
        "Average Rating": 4.55,
        "Number of Reviews": 226,
        "Number of Lectures": 38,
        "Content Length": "5.5 total hours",
        "Last Update": "2022-03-25",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Ramsri Golla"
        ],
        "Course URL": "https://www.udemy.com/course/question-generation-using-natural-language-processing/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3713412_69a1_3.jpg"
    },
    "Python Regression Analysis: Statistics & Machine Learning": {
        "Description": "Learn Complete Hands-On Regression Analysis for Practical Statistical Modelling and Machine Learning in Python",
        "Is Paid": true,
        "Subscribers": 2178,
        "Average Rating": 4.7,
        "Number of Reviews": 226,
        "Number of Lectures": 55,
        "Content Length": "6.5 total hours",
        "Last Update": "2023-11-17",
        "Badges": [],
        "Course Language": "English (UK)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Minerva Singh"
        ],
        "Course URL": "https://www.udemy.com/course/python-regression-analysis-statistics-machine-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1762130_4cf6.jpg"
    },
    "Data Science Project Planning": {
        "Description": "Fundamental Concepts for Beginners",
        "Is Paid": true,
        "Subscribers": 1477,
        "Average Rating": 4.382353,
        "Number of Reviews": 225,
        "Number of Lectures": 56,
        "Content Length": "5 total hours",
        "Last Update": "2020-11-19",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Gopinath Ramakrishnan"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-project-planning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2861934_af64.jpg"
    },
    "Build Neural Networks In Python From Scratch. Step By Step!": {
        "Description": "Understand machine learning and deep learning by building linear regression and gradient descent from the ground up.",
        "Is Paid": true,
        "Subscribers": 1205,
        "Average Rating": 4.7045455,
        "Number of Reviews": 225,
        "Number of Lectures": 19,
        "Content Length": "3 total hours",
        "Last Update": "2022-02-16",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Loek van den Ouweland"
        ],
        "Course URL": "https://www.udemy.com/course/build-neural-networks-from-scratch-with-python-step-by-step/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4475410_130a_15.jpg"
    },
    "Machine Learning for Absolute Beginners - Level 3": {
        "Description": "Learn to Master Data Visualization and perform Exploratory Data Analysis (EDA) using Python, Matplotlib and Seaborn",
        "Is Paid": true,
        "Subscribers": 12819,
        "Average Rating": 4.5657897,
        "Number of Reviews": 224,
        "Number of Lectures": 40,
        "Content Length": "3 total hours",
        "Last Update": "2023-10-27",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Idan Gabrieli"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-for-absolute-beginners-level-3/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3226045_19ca_5.jpg"
    },
    "Computer Vision - OCR using Python": {
        "Description": "Become a Computer Vision expert and learn optical character recognition - OCR using Tesseract, OpenCV and Deep Learning",
        "Is Paid": true,
        "Subscribers": 1038,
        "Average Rating": 4.6153846,
        "Number of Reviews": 224,
        "Number of Lectures": 79,
        "Content Length": "6.5 total hours",
        "Last Update": "2024-01-18",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Vineeta Vashistha"
        ],
        "Course URL": "https://www.udemy.com/course/computer-vision-ocr-using-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3885252_3479_2.jpg"
    },
    "YOLO: Custom Object Detection & Web App in Python": {
        "Description": "Learn to train custom object detection model using Python, OpenCV. Develop web app with Streamlit",
        "Is Paid": true,
        "Subscribers": 1609,
        "Average Rating": 4.352941,
        "Number of Reviews": 222,
        "Number of Lectures": 76,
        "Content Length": "5.5 total hours",
        "Last Update": "2023-03-14",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "G Sudheer",
            "Data Science Anywhere",
            "Brightshine Learn"
        ],
        "Course URL": "https://www.udemy.com/course/yolo-custom-object-detection/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4583290_a570_2.jpg"
    },
    "Pandas Masterclass 2022: Advanced Data Analysis with Pandas": {
        "Description": "Master Pandas library to Analyze, Manipulate & Visualize Big Data. Data Analysis with Pandas using Multiple Projects",
        "Is Paid": true,
        "Subscribers": 22572,
        "Average Rating": 4.35,
        "Number of Reviews": 222,
        "Number of Lectures": 71,
        "Content Length": "9 total hours",
        "Last Update": "2022-03-24",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Dataisgood Academy"
        ],
        "Course URL": "https://www.udemy.com/course/pandas-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4113716_f5b0.jpg"
    },
    "2024 Mastering dbt (Data Build Tool) - From Beginner to Pro": {
        "Description": "Hands-on Analytics Engineering Bootcamp With: Theory, Building a dbt Project from Scratch, and Deploying to dbt Cloud",
        "Is Paid": true,
        "Subscribers": 1907,
        "Average Rating": 4.2747254,
        "Number of Reviews": 222,
        "Number of Lectures": 107,
        "Content Length": "7.5 total hours",
        "Last Update": "2024-02-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Jack Colsey"
        ],
        "Course URL": "https://www.udemy.com/course/mastering-dbt-data-build-tool-bootcamp/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5152140_dba0_3.jpg"
    },
    "Time Series Analysis in Python: Master Applied Data Analysis": {
        "Description": "Python Time Series Analysis with 10+ Forecasting Models including ARIMA, SARIMA, Regression & Time Series Data Analysis",
        "Is Paid": true,
        "Subscribers": 15465,
        "Average Rating": 4.7,
        "Number of Reviews": 220,
        "Number of Lectures": 152,
        "Content Length": "9.5 total hours",
        "Last Update": "2022-03-24",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Dataisgood Academy"
        ],
        "Course URL": "https://www.udemy.com/course/time-series-data-analysis-with-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3914658_f361_2.jpg"
    },
    "AI & ML Starter Course with Hands-On Projects [2024]": {
        "Description": "Learn Artificial Intelligence &amp; Machine Learning with Hands-On Projects",
        "Is Paid": true,
        "Subscribers": 20886,
        "Average Rating": 4.067164,
        "Number of Reviews": 220,
        "Number of Lectures": 10,
        "Content Length": "1.5 total hours",
        "Last Update": "2023-03-19",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Prathamesh Khedekar"
        ],
        "Course URL": "https://www.udemy.com/course/zero-to-hero-ai-ml-starter-course-with-hands-on-projects/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5221538_5038_8.jpg"
    },
    "2024 Python for Linear Regression in Machine Learning": {
        "Description": "Linear &amp; Non-Linear Regression, Lasso &amp; Ridge Regression, SHAP, LIME, Yellowbrick, Feature Selection &amp; Outliers Removal",
        "Is Paid": true,
        "Subscribers": 12542,
        "Average Rating": 4.266667,
        "Number of Reviews": 219,
        "Number of Lectures": 138,
        "Content Length": "14.5 total hours",
        "Last Update": "2024-01-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Laxmi Kant | KGP Talkie"
        ],
        "Course URL": "https://www.udemy.com/course/python-for-advanced-linear-regression-masterclass/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3683662_1a3c.jpg"
    },
    "Clustering & Classification With Machine Learning In R": {
        "Description": "Harness The Power Of Machine Learning For Unsupervised & Supervised Learning In R -- With Practical Examples",
        "Is Paid": true,
        "Subscribers": 2512,
        "Average Rating": 4.7,
        "Number of Reviews": 218,
        "Number of Lectures": 71,
        "Content Length": "8 total hours",
        "Last Update": "2022-10-08",
        "Badges": [],
        "Course Language": "English (UK)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Minerva Singh"
        ],
        "Course URL": "https://www.udemy.com/course/clustering-classification-with-machine-learning-in-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1580888_ba55_2.jpg"
    },
    "Outlier Detection Algorithms in Data Mining and Data Science": {
        "Description": "Outlier Detection in Data Mining, Data Science, Machine Learning, Data Analysis and Statistics using PYTHON,R and SAS",
        "Is Paid": true,
        "Subscribers": 2195,
        "Average Rating": 4.0,
        "Number of Reviews": 217,
        "Number of Lectures": 13,
        "Content Length": "2.5 total hours",
        "Last Update": "2019-01-12",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "KDD Expert"
        ],
        "Course URL": "https://www.udemy.com/course/outlier-detection-techniques/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1099670_0e0d_7.jpg"
    },
    "Computer Vision in Python for Beginners (Theory & Projects)": {
        "Description": "Computer Vision-Become an ace of Computer Vision, Computer Vision for Apps using Python, OpenCV, TensorFlow, etc.",
        "Is Paid": true,
        "Subscribers": 1974,
        "Average Rating": 4.4,
        "Number of Reviews": 217,
        "Number of Lectures": 345,
        "Content Length": "26.5 total hours",
        "Last Update": "2024-02-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "AI Sciences",
            "AI Sciences Team"
        ],
        "Course URL": "https://www.udemy.com/course/mastering-computer-vision-theory-projects-in-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3763238_8b06_2.jpg"
    },
    "Tidy Data: Updated Data Processing With tidyr and dplyr in R": {
        "Description": "Learn Data Preprocessing, Data Wrangling and Data Visualisation With the Two Most Happening R Data Science Packages",
        "Is Paid": true,
        "Subscribers": 1500,
        "Average Rating": 4.6363635,
        "Number of Reviews": 215,
        "Number of Lectures": 42,
        "Content Length": "4.5 total hours",
        "Last Update": "2022-10-08",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Minerva Singh"
        ],
        "Course URL": "https://www.udemy.com/course/tidy-data-updated-data-processing-with-tidyr-and-dplyr-in-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2414146_d644_3.jpg"
    },
    "AutoML Automated Machine Learning BootCamp (No Code ML)": {
        "Description": "Build State of the Art Machine Learning Models without a single line of code",
        "Is Paid": true,
        "Subscribers": 27951,
        "Average Rating": 3.7368422,
        "Number of Reviews": 214,
        "Number of Lectures": 10,
        "Content Length": "1 total hour",
        "Last Update": "2023-01-14",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Raj Chhabria"
        ],
        "Course URL": "https://www.udemy.com/course/automl-automated-machine-learning-bootcamp-no-code-ml/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5049556_f105_3.jpg"
    },
    "Deep Reinforcement Learning: Hands-on AI Tutorial in Python": {
        "Description": "Develop Artificial Intelligence Applications using Reinforcement Learning in Python.",
        "Is Paid": true,
        "Subscribers": 17419,
        "Average Rating": 4.2,
        "Number of Reviews": 214,
        "Number of Lectures": 51,
        "Content Length": "4 total hours",
        "Last Update": "2020-10-30",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Mehdi Mohammadi"
        ],
        "Course URL": "https://www.udemy.com/course/deep-reinforcement-learning-a-hands-on-tutorial-in-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2369480_c479_5.jpg"
    },
    "Decision Trees, Random Forests, Bagging & XGBoost: R Studio": {
        "Description": "Decision Trees and Ensembling techinques in R studio. Bagging, Random Forest, GBM, AdaBoost & XGBoost in R programming",
        "Is Paid": true,
        "Subscribers": 63920,
        "Average Rating": 4.3,
        "Number of Reviews": 213,
        "Number of Lectures": 55,
        "Content Length": "6 total hours",
        "Last Update": "2024-01-12",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Start-Tech Academy"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-advanced-decision-trees-in-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2401052_2792_3.jpg"
    },
    "Mastering OCR using Deep Learning and OpenCV-Python": {
        "Description": "A complete guide to optical character recognition pipeline using Deep Learning, python and OpenCV",
        "Is Paid": true,
        "Subscribers": 1012,
        "Average Rating": 3.6,
        "Number of Reviews": 213,
        "Number of Lectures": 27,
        "Content Length": "2.5 total hours",
        "Last Update": "2021-06-16",
        "Badges": [],
        "Course Language": "English (India)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Pankaj Kang",
            "Atul Krishna Singh"
        ],
        "Course URL": "https://www.udemy.com/course/mastering-ocr-using-deep-learning-and-opencv-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3896504_f0ae.jpg"
    },
    "Deep Learning Bootcamp with 5 Capstone Projects": {
        "Description": "Learn about Deep Learning - ANN, CNN, RNN, LSTMs along with Real Time Capstone Projects",
        "Is Paid": true,
        "Subscribers": 19476,
        "Average Rating": 3.8,
        "Number of Reviews": 213,
        "Number of Lectures": 94,
        "Content Length": "6.5 total hours",
        "Last Update": "2022-03-24",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Dataisgood Academy"
        ],
        "Course URL": "https://www.udemy.com/course/deep-learning-machine-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4181880_993d.jpg"
    },
    "YOLOv3 - Robust Deep Learning Object Detection in 1 hour": {
        "Description": "The Complete Guide to Creating your own Custom AI Object Detection. Learn the Full Workflow - From Training to Inference",
        "Is Paid": true,
        "Subscribers": 1359,
        "Average Rating": 4.3,
        "Number of Reviews": 212,
        "Number of Lectures": 20,
        "Content Length": "2.5 total hours",
        "Last Update": "2020-05-26",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Augmented Startups"
        ],
        "Course URL": "https://www.udemy.com/course/yolo-v3-robust-deep-learning-object-detection-in-1-hour/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1950334_9b79_8.jpg"
    },
    "VSD - Machine Intelligence in EDA/CAD": {
        "Description": "Listen from CEO/architect himself on Machine learning",
        "Is Paid": true,
        "Subscribers": 811,
        "Average Rating": 4.35,
        "Number of Reviews": 211,
        "Number of Lectures": 27,
        "Content Length": "4 total hours",
        "Last Update": "2019-04-18",
        "Badges": [
            "Highest Rated"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Kunal Ghosh",
            "Rohit Sharma"
        ],
        "Course URL": "https://www.udemy.com/course/vsd-machine-intelligence-in-eda-cad/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1626838_1c50_4.jpg"
    },
    "Statistics with R - Advanced Level": {
        "Description": "Advanced statistical analyses using the R program",
        "Is Paid": true,
        "Subscribers": 28150,
        "Average Rating": 4.05,
        "Number of Reviews": 211,
        "Number of Lectures": 37,
        "Content Length": "4.5 total hours",
        "Last Update": "2020-12-08",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Expert Level",
        "Authors": [
            "Bogdan Anastasiei"
        ],
        "Course URL": "https://www.udemy.com/course/statistics-with-r-advanced-level/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/691894_1aec_3.jpg"
    },
    "R Programming Complete Certification Training": {
        "Description": "R concepts, coding examples. Data structure, loops, functions, packages, plots/charts, data/files, decision-making in R.",
        "Is Paid": true,
        "Subscribers": 14590,
        "Average Rating": 3.7857144,
        "Number of Reviews": 210,
        "Number of Lectures": 39,
        "Content Length": "21 total hours",
        "Last Update": "2020-07-10",
        "Badges": [],
        "Course Language": "English (UK)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Uplatz Training"
        ],
        "Course URL": "https://www.udemy.com/course/r-programming-training/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3317064_c5b4_3.jpg"
    },
    "Complete Machine Learning & Data Science with Python | A-Z": {
        "Description": "Use Scikit, learn NumPy, Pandas, Matplotlib, Seaborn and dive into machine learning A-Z with Python and Data Science.",
        "Is Paid": true,
        "Subscribers": 17977,
        "Average Rating": 4.65,
        "Number of Reviews": 209,
        "Number of Lectures": 64,
        "Content Length": "8.5 total hours",
        "Last Update": "2024-02-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Oak Academy",
            "OAK Academy Team"
        ],
        "Course URL": "https://www.udemy.com/course/complete-machine-learning-data-science-with-python-a-z/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4060614_2874_8.jpg"
    },
    "Master AI Image Generation using Stable Diffusion": {
        "Description": "Create stunning images using Generative Artificial Intelligence! Step by step with Stable Diffusion and Python!",
        "Is Paid": true,
        "Subscribers": 2076,
        "Average Rating": 4.3461537,
        "Number of Reviews": 208,
        "Number of Lectures": 53,
        "Content Length": "7 total hours",
        "Last Update": "2023-11-21",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Jones Granatyr",
            "Gabriel Alves",
            "AI Expert Academy"
        ],
        "Course URL": "https://www.udemy.com/course/master-ai-image-generation-using-stable-diffusion/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5389028_ffe5.jpg"
    },
    "Data Analytics and Artificial Intelligence for Beginners": {
        "Description": "Learn the basic concepts of data analytics, AI, business intelligence, big data, machine learning, and deep learning.",
        "Is Paid": true,
        "Subscribers": 1159,
        "Average Rating": 4.288235,
        "Number of Reviews": 208,
        "Number of Lectures": 23,
        "Content Length": "3 total hours",
        "Last Update": "2023-03-10",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Simon Sez IT"
        ],
        "Course URL": "https://www.udemy.com/course/data-analytics-and-artificial-intelligence-for-beginners/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5203294_cfca_4.jpg"
    },
    "Machine Learning | Deep Learning | Explainable AI | Vertex": {
        "Description": "Course Covers Basic & Advanced Contents relevant to practitioners",
        "Is Paid": true,
        "Subscribers": 16677,
        "Average Rating": 4.4,
        "Number of Reviews": 205,
        "Number of Lectures": 58,
        "Content Length": "8.5 total hours",
        "Last Update": "2024-01-14",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "SeaportAi ."
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-on-google-cloud/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3771370_f6e8_5.jpg"
    },
    "Machine Learning using Python: A Comprehensive Course": {
        "Description": "Learn core concepts of Machine Learning. Apply ML techniques to real-world problems and develop AI/ML based applications",
        "Is Paid": true,
        "Subscribers": 39381,
        "Average Rating": 3.25,
        "Number of Reviews": 205,
        "Number of Lectures": 160,
        "Content Length": "63.5 total hours",
        "Last Update": "2024-01-20",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Uplatz Training"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-concepts-and-application-of-ml-using-python/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/3701682_a16c_6.jpg"
    },
    "Jetson Nano Boot Camp": {
        "Description": "Learn Jetson Nano with Machine Learning Project, Python, OpenCV and Serial Communication!",
        "Is Paid": true,
        "Subscribers": 1037,
        "Average Rating": 4.45,
        "Number of Reviews": 205,
        "Number of Lectures": 91,
        "Content Length": "6 total hours",
        "Last Update": "2022-05-30",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Y\u0131lmaz Alaca"
        ],
        "Course URL": "https://www.udemy.com/course/jetson-nano-boot-camp/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4300411_0e28_2.jpg"
    },
    "Machine Learning Guide: Learn Machine Learning Algorithms": {
        "Description": "Machine Learning: A comprehensive guide to machine learning. Learn machine learning algorithms & machine learning tools",
        "Is Paid": true,
        "Subscribers": 10081,
        "Average Rating": 3.05,
        "Number of Reviews": 204,
        "Number of Lectures": 12,
        "Content Length": "1 total hour",
        "Last Update": "2019-05-10",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Grid Wire"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-algorithms/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/2361148_5c48.jpg"
    },
    "Excel files with Python": {
        "Description": "Use Excel spreadsheets with Python",
        "Is Paid": true,
        "Subscribers": 33852,
        "Average Rating": 3.9565217,
        "Number of Reviews": 204,
        "Number of Lectures": 9,
        "Content Length": "31 total mins",
        "Last Update": "2021-07-12",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Frank Anemaet"
        ],
        "Course URL": "https://www.udemy.com/course/excel-files-with-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4178604_6f6a.jpg"
    },
    "Probability and Statistics: Complete Course 2024": {
        "Description": "Learn the Probability and Statistics You Need to Succeed in Data Science and Business Analytics",
        "Is Paid": true,
        "Subscribers": 1408,
        "Average Rating": 4.775862,
        "Number of Reviews": 203,
        "Number of Lectures": 116,
        "Content Length": "16.5 total hours",
        "Last Update": "2024-01-02",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (UK)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Woody Lewenstein"
        ],
        "Course URL": "https://www.udemy.com/course/probability-and-statistics-complete-course/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/5195000_e2db_2.jpg"
    },
    "Fundamentals of Responsible Artificial Intelligence/ML": {
        "Description": "Designing and mantaining AI/ML models that help data subjects, are explainable, are not biased, and are compliant.",
        "Is Paid": true,
        "Subscribers": 968,
        "Average Rating": 4.3333335,
        "Number of Reviews": 202,
        "Number of Lectures": 66,
        "Content Length": "8.5 total hours",
        "Last Update": "2023-01-25",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Vasco Patr\u00edcio"
        ],
        "Course URL": "https://www.udemy.com/course/responsible-ai-ml/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/5065894_0f92.jpg"
    },
    "Build and train a data model to recognize objects in images!": {
        "Description": "Make an image recognition model with TensorFlow & Python predictive modeling, regression analysis & machine learning!",
        "Is Paid": true,
        "Subscribers": 1487,
        "Average Rating": 4.55,
        "Number of Reviews": 202,
        "Number of Lectures": 57,
        "Content Length": "8.5 total hours",
        "Last Update": "2019-01-21",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Mammoth Interactive",
            "John Bura"
        ],
        "Course URL": "https://www.udemy.com/course/pythondatascience/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1426102_cde1_3.jpg"
    },
    "Advanced Data Science Techniques in SPSS": {
        "Description": "Hone your SPSS skills to perfection -  grasp the most high level data analysis methods available in the SPSS program.",
        "Is Paid": true,
        "Subscribers": 25339,
        "Average Rating": 4.1,
        "Number of Reviews": 200,
        "Number of Lectures": 87,
        "Content Length": "6.5 total hours",
        "Last Update": "2020-12-08",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Expert Level",
        "Authors": [
            "Bogdan Anastasiei"
        ],
        "Course URL": "https://www.udemy.com/course/advanced-data-science-techniques-in-spss/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/1424566_e0e1_2.jpg"
    },
    "Artificial Intelligence III - Deep Learning in Java": {
        "Description": "Deep Learning Fundamentals, Convolutional Neural Networks (CNNs) and Recurrent Neural Networks (RNNs) + LSTM, GRUs",
        "Is Paid": true,
        "Subscribers": 3194,
        "Average Rating": 4.642857,
        "Number of Reviews": 199,
        "Number of Lectures": 46,
        "Content Length": "4 total hours",
        "Last Update": "2021-12-17",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Holczer Balazs"
        ],
        "Course URL": "https://www.udemy.com/course/artificial-intelligence-iii-in-java/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/1462912_a4d5_2.jpg"
    },
    "Data Science for All : A Foundation Course": {
        "Description": "Learn everything you need to know about fast-growing field of Data Science without having to write a single line of code",
        "Is Paid": true,
        "Subscribers": 4921,
        "Average Rating": 4.2874017,
        "Number of Reviews": 198,
        "Number of Lectures": 25,
        "Content Length": "2 total hours",
        "Last Update": "2021-06-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Anmol Tomar"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-for-all/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4085988_3486.jpg"
    },
    "Python Pandas Library Full Tutorial": {
        "Description": "Pandas Library",
        "Is Paid": true,
        "Subscribers": 19256,
        "Average Rating": 4.4,
        "Number of Reviews": 198,
        "Number of Lectures": 32,
        "Content Length": "1 total hour",
        "Last Update": "2020-04-25",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Diptam Paul"
        ],
        "Course URL": "https://www.udemy.com/course/python-pandas-library/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3049706_4f58.jpg"
    },
    "2024 Data Visualization in Tableau & Python (2 Courses in 1)": {
        "Description": "Learn Data Visualization with Tableau &amp; Python from the basic to advanced level using Real-Life Projects",
        "Is Paid": true,
        "Subscribers": 16337,
        "Average Rating": 4.716814,
        "Number of Reviews": 197,
        "Number of Lectures": 33,
        "Content Length": "2 total hours",
        "Last Update": "2024-02-01",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Surendra Varma Pericherla"
        ],
        "Course URL": "https://www.udemy.com/course/2023-data-visualization-in-tableau-python-2-courses-in-1/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/5344042_e749_3.jpg"
    },
    "ChatGPT Masterclass: A Complete ChatGPT Zero to Hero!": {
        "Description": "ChatGPT for Beginners: Use ChatGPT to WIN in your CAREER as a professional or Make a Business Using ChatGPT & OpenAI!",
        "Is Paid": true,
        "Subscribers": 7029,
        "Average Rating": 3.8653846,
        "Number of Reviews": 195,
        "Number of Lectures": 38,
        "Content Length": "3 total hours",
        "Last Update": "2023-05-04",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Metla Sudha Sekhar"
        ],
        "Course URL": "https://www.udemy.com/course/chatgpt-masterclass-a-complete-chatgpt-zero-to-hero-openai/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/5252958_c823_4.jpg"
    },
    "Artificial Intelligence & Machine Learning from scratch": {
        "Description": "Give you a solid background in AI with MACHINE LEARNING, Deep Learning ... step-by-step to algorithms & coding exercises",
        "Is Paid": true,
        "Subscribers": 2561,
        "Average Rating": 4.214286,
        "Number of Reviews": 194,
        "Number of Lectures": 26,
        "Content Length": "6.5 total hours",
        "Last Update": "2020-12-29",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Dr. Long Nguyen",
            "TheWay2AI by Dr. Long Nguyen"
        ],
        "Course URL": "https://www.udemy.com/course/artificial-intelligence-a-complete-introduction/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/2915852_65b9_9.jpg"
    },
    "2024 Introduction to Spacy for Natural Language Processing": {
        "Description": "Kick start your Data Science career with NLP. This course is about Spacy. NLTK is not taught in this course.",
        "Is Paid": true,
        "Subscribers": 16087,
        "Average Rating": 4.05,
        "Number of Reviews": 194,
        "Number of Lectures": 26,
        "Content Length": "4 total hours",
        "Last Update": "2024-01-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Laxmi Kant | KGP Talkie"
        ],
        "Course URL": "https://www.udemy.com/course/introduction-to-for-natural-language-processing/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/3306778_f330_5.jpg"
    },
    "Deep Learning: Visual Exploration": {
        "Description": "Deep neural networks visually explained in plain english & without complex math",
        "Is Paid": true,
        "Subscribers": 11550,
        "Average Rating": 4.65,
        "Number of Reviews": 193,
        "Number of Lectures": 15,
        "Content Length": "4 total hours",
        "Last Update": "2018-04-10",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Vladimir Grankin"
        ],
        "Course URL": "https://www.udemy.com/course/deep-learning-visual-exploration-for-deep-understanding/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/1569688_dedd.jpg"
    },
    "The Ultimate Beginners Guide to Genetic Algorithms in Python": {
        "Description": "Implement genetic algorithms from scratch to solve real world problems!",
        "Is Paid": true,
        "Subscribers": 2091,
        "Average Rating": 4.56,
        "Number of Reviews": 192,
        "Number of Lectures": 35,
        "Content Length": "5 total hours",
        "Last Update": "2023-04-27",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Jones Granatyr",
            "Edson Pacholok",
            "AI Expert Academy"
        ],
        "Course URL": "https://www.udemy.com/course/the-ultimate-beginners-guide-to-genetic-algorithms-in-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4309418_eec5_2.jpg"
    },
    "Power BI Bootcamp:  Build Real World Power BI Projects": {
        "Description": "Build Real World Microsoft Power BI Desktop Projects. In This Course Learn Business Intelligence, Data Analysis.",
        "Is Paid": true,
        "Subscribers": 3081,
        "Average Rating": 4.075,
        "Number of Reviews": 192,
        "Number of Lectures": 49,
        "Content Length": "6.5 total hours",
        "Last Update": "2023-10-12",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "The Machine Learning"
        ],
        "Course URL": "https://www.udemy.com/course/build-microsoft-power-bi-projects/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4889904_4b7f_2.jpg"
    },
    "TensorFlow 101: Introduction to Deep Learning": {
        "Description": "Ready to build the future with Deep Neural Networks? Stand on the shoulder of TensorFlow and Keras for Machine Learning.",
        "Is Paid": true,
        "Subscribers": 5177,
        "Average Rating": 4.1,
        "Number of Reviews": 191,
        "Number of Lectures": 23,
        "Content Length": "4 total hours",
        "Last Update": "2020-05-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Sefik Ilkin Serengil"
        ],
        "Course URL": "https://www.udemy.com/course/tensorflow-101-introduction-to-deep-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1330246_257f_5.jpg"
    },
    "Deep Learning Mastery 2024": {
        "Description": "Learn about Complete Life Cycle of a Deep Learning Project. Implement different Neural networks using Tensorflow &amp; Keras",
        "Is Paid": true,
        "Subscribers": 34877,
        "Average Rating": 4.226415,
        "Number of Reviews": 189,
        "Number of Lectures": 34,
        "Content Length": "4.5 total hours",
        "Last Update": "2023-01-11",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Raj Chhabria"
        ],
        "Course URL": "https://www.udemy.com/course/deep-learning-masterclass/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5062314_8073.jpg"
    },
    "Python Data Science with NumPy: Over 100 Exercises": {
        "Description": "Level up Your Data Science Skills in Python - Unleash the Power of Numerical Computing and Analysis!",
        "Is Paid": true,
        "Subscribers": 61649,
        "Average Rating": 4.55,
        "Number of Reviews": 187,
        "Number of Lectures": 116,
        "Content Length": "1 total hour",
        "Last Update": "2023-10-30",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Pawe\u0142 Krakowiak"
        ],
        "Course URL": "https://www.udemy.com/course/100-exercises-python-programming-data-science-numpy/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3286770_b5d8_7.jpg"
    },
    "BigQuery ML - Machine Learning in SQL using Google BigQuery": {
        "Description": "Create Machine Learning models in Google Cloud Big Query using standard SQL. Big query ML course for ML & Data engineers",
        "Is Paid": true,
        "Subscribers": 2364,
        "Average Rating": 4.75,
        "Number of Reviews": 187,
        "Number of Lectures": 125,
        "Content Length": "11 total hours",
        "Last Update": "2023-11-17",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "J Garg - Real Time Learning"
        ],
        "Course URL": "https://www.udemy.com/course/bigquery-ml-course/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4571796_5da2.jpg"
    },
    "Artificial Intelligence Introduction for Non-Technicals": {
        "Description": "Introduction to AI, ML, Data Science , BI and Analytics for Non-Technicals, Leaders, Managers, freshers and Beginners",
        "Is Paid": true,
        "Subscribers": 549,
        "Average Rating": 4.2,
        "Number of Reviews": 185,
        "Number of Lectures": 14,
        "Content Length": "3.5 total hours",
        "Last Update": "2020-07-16",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Sudhanshu Saxena"
        ],
        "Course URL": "https://www.udemy.com/course/artificial-intelligence-for-everyone/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2855694_9261.jpg"
    },
    "Artificial Intelligence and Predictive Analysis": {
        "Description": "This course is a comprehensive understanding of AI concepts and its application using Python and iPython.",
        "Is Paid": true,
        "Subscribers": 66584,
        "Average Rating": 4.35,
        "Number of Reviews": 185,
        "Number of Lectures": 59,
        "Content Length": "6.5 total hours",
        "Last Update": "2018-12-03",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "EDUCBA Bridging the Gap"
        ],
        "Course URL": "https://www.udemy.com/course/artificial-intelligence-with-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1949472_451a_6.jpg"
    },
    "Essential Fundamentals of R": {
        "Description": "Data Types and Structures in R , Inputting & Outputting Data, Writing User-Defined Functions, and Manipulating Data Sets",
        "Is Paid": true,
        "Subscribers": 1797,
        "Average Rating": 3.95,
        "Number of Reviews": 185,
        "Number of Lectures": 46,
        "Content Length": "10.5 total hours",
        "Last Update": "2020-07-22",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Geoffrey Hubona, Ph.D."
        ],
        "Course URL": "https://www.udemy.com/course/essential-fundamentals-of-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/579018_d09b_3.jpg"
    },
    "Getting Started with Embedded AI | Edge AI": {
        "Description": "Explained a demo application to recognize fault of a small DC motor by analyzing vibrational pattern via Embedded/EdgeAI",
        "Is Paid": true,
        "Subscribers": 1235,
        "Average Rating": 3.9,
        "Number of Reviews": 183,
        "Number of Lectures": 51,
        "Content Length": "3.5 total hours",
        "Last Update": "2019-10-12",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Embedded Insider"
        ],
        "Course URL": "https://www.udemy.com/course/getting-started-with-embedded-ai-hands-on-experience/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2512366_9781.jpg"
    },
    "Python for Data Science and Data Analysis": {
        "Description": "Mastering Data Science Python Essentials: Numpy, Pandas, Matplotlib, Seaborn, Bokeh, and Scikit-Learn for Data Analysis",
        "Is Paid": true,
        "Subscribers": 820,
        "Average Rating": 3.65,
        "Number of Reviews": 184,
        "Number of Lectures": 156,
        "Content Length": "16.5 total hours",
        "Last Update": "2024-02-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "AI Sciences",
            "AI Sciences Team"
        ],
        "Course URL": "https://www.udemy.com/course/python-mastering-python-for-data-science-from-zero-to-hero/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3047350_2514_5.jpg"
    },
    "Professional Certificate in Data Mining & Machine Learning": {
        "Description": "Transform from a Beginner to a Machine Learning / Data Science Pro\u2013 Investing in Your Future Job Success [2024 Edition]",
        "Is Paid": true,
        "Subscribers": 1097,
        "Average Rating": 3.5,
        "Number of Reviews": 184,
        "Number of Lectures": 233,
        "Content Length": "29 total hours",
        "Last Update": "2024-01-21",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Academy of Computing & Artificial Intelligence"
        ],
        "Course URL": "https://www.udemy.com/course/professional-certificate-in-data-mining-machine-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3822980_c80a.jpg"
    },
    "Complete Python for data science and cloud computing": {
        "Description": "A complete & in-depth use case course taught by data science PHD & business consultants with thousand examples",
        "Is Paid": true,
        "Subscribers": 1389,
        "Average Rating": 3.3,
        "Number of Reviews": 184,
        "Number of Lectures": 361,
        "Content Length": "49 total hours",
        "Last Update": "2018-09-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Datagist INC"
        ],
        "Course URL": "https://www.udemy.com/course/complete-python-for-data-science-and-cloud-computing/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1438796_dc6c_6.jpg"
    },
    "Most Effective Tips to get your Dream Data Science Job": {
        "Description": "Get your dream role as a Data Scientist by following this go-to guide that covers all essential end to end topics.",
        "Is Paid": true,
        "Subscribers": 46371,
        "Average Rating": 4.266667,
        "Number of Reviews": 182,
        "Number of Lectures": 58,
        "Content Length": "2.5 total hours",
        "Last Update": "2022-01-04",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Prince Patni"
        ],
        "Course URL": "https://www.udemy.com/course/most-effective-tips-to-get-your-dream-data-science-job/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4435398_1d5b.jpg"
    },
    "Machine Learning & Self-Driving Cars: Bootcamp with Python": {
        "Description": "Combine the power of Machine Learning, Deep Learning and Computer Vision to make a Self-Driving Car!",
        "Is Paid": true,
        "Subscribers": 20408,
        "Average Rating": 4.551724,
        "Number of Reviews": 180,
        "Number of Lectures": 78,
        "Content Length": "8.5 total hours",
        "Last Update": "2023-10-29",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Iu Ayala"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-self-driving-cars/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4434450_9061.jpg"
    },
    "Data Visualization in Python for Machine Learning Engineers": {
        "Description": "The Third Course in a Series for Mastering Python for Machine Learning Engineers",
        "Is Paid": true,
        "Subscribers": 10261,
        "Average Rating": 4.45,
        "Number of Reviews": 181,
        "Number of Lectures": 63,
        "Content Length": "1 total hour",
        "Last Update": "2021-07-22",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Mike West"
        ],
        "Course URL": "https://www.udemy.com/course/data-visualization-in-python-for-machine-learning-engineers/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1470278_4491_2.jpg"
    },
    "Build Neural Networks In Seconds Using Deep Learning Studio": {
        "Description": "Develop Keras / TensorFlow Deep Learning Models Using A GUI And Without Knowing Python Or Machine Learning",
        "Is Paid": true,
        "Subscribers": 568,
        "Average Rating": 3.35,
        "Number of Reviews": 181,
        "Number of Lectures": 43,
        "Content Length": "3 total hours",
        "Last Update": "2019-01-04",
        "Badges": [],
        "Course Language": "English (UK)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Michael Kroeker"
        ],
        "Course URL": "https://www.udemy.com/course/build-neural-networks-in-seconds-using-deep-learning-studio/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2082540_5cf3.jpg"
    },
    "Google Bard Generative AI Masterclass : Certification Course": {
        "Description": "Unlock your creative potential and master the art of AI content creation with Google Bard in this step-by-step course",
        "Is Paid": true,
        "Subscribers": 15805,
        "Average Rating": 4.1893206,
        "Number of Reviews": 180,
        "Number of Lectures": 13,
        "Content Length": "1 total hour",
        "Last Update": "2023-05-18",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Prince Patni"
        ],
        "Course URL": "https://www.udemy.com/course/google-bard-generative-ai-masterclass-certification-course/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5328518_793a.jpg"
    },
    "50 Hrs Big Data Mastery: PySpark, AWS, Scala & Data Scraping": {
        "Description": "Comprehensive Big Data Mastery: Scala, Spark, PySpark, AWS, Data Scraping & Data Mining with Python, Mining and MongoDB",
        "Is Paid": true,
        "Subscribers": 1834,
        "Average Rating": 4.45,
        "Number of Reviews": 179,
        "Number of Lectures": 623,
        "Content Length": "54.5 total hours",
        "Last Update": "2024-02-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "AI Sciences",
            "AI Sciences Team"
        ],
        "Course URL": "https://www.udemy.com/course/big-data-with-scalasparkpyspark-and-aws-a-z-50-hours/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4388966_10db_3.jpg"
    },
    "No-Code Machine Learning with Qlik AutoML": {
        "Description": "Learn Machine Learning Concepts, Build your Model & get accurate predictions without writing any Code using Qlik AutoML",
        "Is Paid": true,
        "Subscribers": 43191,
        "Average Rating": 4.0,
        "Number of Reviews": 179,
        "Number of Lectures": 38,
        "Content Length": "2.5 total hours",
        "Last Update": "2022-03-31",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Prince Patni"
        ],
        "Course URL": "https://www.udemy.com/course/no-code-machine-learning-with-qlik-automl/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4592810_947e_2.jpg"
    },
    "Machine Learning and Statistical Modeling with R Examples": {
        "Description": "Learn how to use machine learning algorithms and statistical modeling for clustering, decision trees, etc by using R",
        "Is Paid": true,
        "Subscribers": 2300,
        "Average Rating": 4.55,
        "Number of Reviews": 178,
        "Number of Lectures": 23,
        "Content Length": "2.5 total hours",
        "Last Update": "2016-09-14",
        "Badges": [
            "Highest Rated"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "R-Tutorials Training"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-and-statistical-modeling-with-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/491640_737f.jpg"
    },
    "Machine Learning & Training Neural Network in MATLAB": {
        "Description": "Machine Learning | Learn concepts of Machine Learning and how to train a Neural Network in MATLAB on Iris data-set.",
        "Is Paid": true,
        "Subscribers": 7488,
        "Average Rating": 3.05,
        "Number of Reviews": 178,
        "Number of Lectures": 6,
        "Content Length": "1.5 total hours",
        "Last Update": "2018-04-29",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Sarthak Mishra"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-training-neural-network-in-matlab/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1600384_e655.jpg"
    },
    "Learning Path: R: Complete Machine Learning & Deep Learning": {
        "Description": "Unleash the true potential of R to unlock the hidden layers of data",
        "Is Paid": true,
        "Subscribers": 1589,
        "Average Rating": 4.45,
        "Number of Reviews": 178,
        "Number of Lectures": 213,
        "Content Length": "17.5 total hours",
        "Last Update": "2017-06-06",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Expert Level",
        "Authors": [
            "Packt Publishing"
        ],
        "Course URL": "https://www.udemy.com/course/learning-path-r-complete-machine-learning-deep-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1183326_3ace_2.jpg"
    },
    "Data Science A-Z : Machine Learning with Python & R": {
        "Description": "By Data Scientist / IITian  for Beginners . Data Science/Machine Learning with Python & R for beginners to advance",
        "Is Paid": true,
        "Subscribers": 685,
        "Average Rating": 4.15,
        "Number of Reviews": 176,
        "Number of Lectures": 90,
        "Content Length": "12.5 total hours",
        "Last Update": "2020-03-31",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Arpan Gupta"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-using-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1346692_1892_2.jpg"
    },
    "Practical Data Literacy for Leaders": {
        "Description": "Make better data-driven business-decisions. Present your data like a PRO. Learn the key data and analytics terminology",
        "Is Paid": true,
        "Subscribers": 1493,
        "Average Rating": 4.080645,
        "Number of Reviews": 175,
        "Number of Lectures": 78,
        "Content Length": "5 total hours",
        "Last Update": "2024-02-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "George Smarts"
        ],
        "Course URL": "https://www.udemy.com/course/practical-data-literacy-masterclass/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4735176_4fa1.jpg"
    },
    "ChatGPT for Data Science and Machine Learning [2024 Updated]": {
        "Description": "Learn to build Data Science and Machine Learning Projects by Leveraging the Power of ChatGPT.",
        "Is Paid": true,
        "Subscribers": 30341,
        "Average Rating": 4.189189,
        "Number of Reviews": 174,
        "Number of Lectures": 27,
        "Content Length": "3.5 total hours",
        "Last Update": "2023-03-18",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Raj Chhabria"
        ],
        "Course URL": "https://www.udemy.com/course/chatgpt-for-data-science-and-machine-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5192634_7651.jpg"
    },
    "Deep Learning: Natural Language Processing with Transformers": {
        "Description": "Use Huggingface transformers and Tensorflow to build Sentiment analysis, Translation, Q&A, Search, Speech,... projects",
        "Is Paid": true,
        "Subscribers": 1770,
        "Average Rating": 4.0875,
        "Number of Reviews": 172,
        "Number of Lectures": 120,
        "Content Length": "33.5 total hours",
        "Last Update": "2023-08-27",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Neuralearn Dot AI"
        ],
        "Course URL": "https://www.udemy.com/course/modern-natural-language-processingnlp-using-deep-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4154714_a3b8.jpg"
    },
    "Artificial Intelligence IV - Reinforcement Learning in Java": {
        "Description": "All you need to know about Markov Decision processes, value- and policy-iteation as well as about Q learning approach",
        "Is Paid": true,
        "Subscribers": 1981,
        "Average Rating": 4.55,
        "Number of Reviews": 173,
        "Number of Lectures": 39,
        "Content Length": "3 total hours",
        "Last Update": "2023-11-22",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Holczer Balazs"
        ],
        "Course URL": "https://www.udemy.com/course/artificial-intelligence-iv-reinforcement-learning-in-java/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1513950_22d6_2.jpg"
    },
    "Complete Machine Learning & Reinforcement learning 2023": {
        "Description": "Start Machine Learning & Data Science era with Python ,Math & Libraries like: SKlearn , Pandas , NumPy, Matplotlib & Gym",
        "Is Paid": true,
        "Subscribers": 1438,
        "Average Rating": 4.4,
        "Number of Reviews": 171,
        "Number of Lectures": 188,
        "Content Length": "27 total hours",
        "Last Update": "2023-07-01",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "SkyHub Academy",
            "Ahmed Attia"
        ],
        "Course URL": "https://www.udemy.com/course/complete-machine-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2032706_2e0d_11.jpg"
    },
    "Interactive python dashboards | Plotly Dash 2022| 3 Projects": {
        "Description": "Learn to create interactive Covid-19 dashboard, Retail Sales dashboard, NLP dashboard using plotly Dash and python",
        "Is Paid": true,
        "Subscribers": 986,
        "Average Rating": 4.5,
        "Number of Reviews": 171,
        "Number of Lectures": 48,
        "Content Length": "7.5 total hours",
        "Last Update": "2023-11-25",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Anmol Tomar"
        ],
        "Course URL": "https://www.udemy.com/course/plotly-dash-python-dashboards/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3252376_d522.jpg"
    },
    "LLMs with Google Cloud and Python": {
        "Description": "Learn to use Google Cloud's latest LLM models in Google Cloud Platform and with Python!",
        "Is Paid": true,
        "Subscribers": 2081,
        "Average Rating": 4.6538463,
        "Number of Reviews": 169,
        "Number of Lectures": 37,
        "Content Length": "5 total hours",
        "Last Update": "2023-11-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Jose Portilla"
        ],
        "Course URL": "https://www.udemy.com/course/llms-with-google-cloud-and-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5597124_b07c_3.jpg"
    },
    "Build Your Own Chatbot in Python": {
        "Description": "Play with your own AI Assistant",
        "Is Paid": true,
        "Subscribers": 16793,
        "Average Rating": 2.75,
        "Number of Reviews": 170,
        "Number of Lectures": 11,
        "Content Length": "2 total hours",
        "Last Update": "2021-04-21",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Kumar Rajmani Bapat"
        ],
        "Course URL": "https://www.udemy.com/course/build-your-own-chatbot-in-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3991532_a8f8_3.jpg"
    },
    "Optical Character Recognition (OCR) in Python": {
        "Description": "OpenCV, Tesseract, EasyOCR and EAST applied to images and videos! Create your own OCR from scratch using Deep Learning!",
        "Is Paid": true,
        "Subscribers": 1708,
        "Average Rating": 4.571429,
        "Number of Reviews": 169,
        "Number of Lectures": 95,
        "Content Length": "13 total hours",
        "Last Update": "2023-04-27",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Jones Granatyr",
            "Gabriel Alves",
            "AI Expert Academy"
        ],
        "Course URL": "https://www.udemy.com/course/ocr-optical-character-recognition-in-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4639122_3a09_2.jpg"
    },
    "OpenAI Assistants with OpenAI Python API": {
        "Description": "Learn to use the new OpenAI Assistants API, allowing GPT models to run code, read your files, and call functions!",
        "Is Paid": true,
        "Subscribers": 1809,
        "Average Rating": 4.665663,
        "Number of Reviews": 166,
        "Number of Lectures": 24,
        "Content Length": "4 total hours",
        "Last Update": "2023-12-13",
        "Badges": [
            "Highest Rated"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Jose Portilla"
        ],
        "Course URL": "https://www.udemy.com/course/openai-assistants-with-openai-python-api/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5700566_eda2_2.jpg"
    },
    "Optical Character Recognition (OCR) MasterClass in Python": {
        "Description": "Learn OCR in Python using OpenCV, Pytesseract, Pillow and Machine Learning",
        "Is Paid": true,
        "Subscribers": 28376,
        "Average Rating": 4.035714,
        "Number of Reviews": 168,
        "Number of Lectures": 22,
        "Content Length": "2 total hours",
        "Last Update": "2023-01-03",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Raj Chhabria"
        ],
        "Course URL": "https://www.udemy.com/course/optical-character-recognition-ocr-masterclass-in-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5045772_8171_7.jpg"
    },
    "How to easily use ANN for prediction mapping using GIS data?": {
        "Description": "First Simplified Step-by-Step Artificial Neural Network Methodology in R for Prediction Mapping using GIS Data",
        "Is Paid": true,
        "Subscribers": 844,
        "Average Rating": 4.65,
        "Number of Reviews": 167,
        "Number of Lectures": 39,
        "Content Length": "7.5 total hours",
        "Last Update": "2023-09-15",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Dr. Omar AlThuwaynee"
        ],
        "Course URL": "https://www.udemy.com/course/how-to-use-ann-for-prediction-mapping-using-gis-data/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2268034_6d58_2.jpg"
    },
    "Streamlit Bootcamp": {
        "Description": "Build beautiful web apps for your Data Science and Machine Learning projects in a fast and easy way using Streamlit.",
        "Is Paid": true,
        "Subscribers": 25322,
        "Average Rating": 4.40625,
        "Number of Reviews": 166,
        "Number of Lectures": 29,
        "Content Length": "2 total hours",
        "Last Update": "2023-01-01",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Raj Chhabria"
        ],
        "Course URL": "https://www.udemy.com/course/streamlit-bootcamp/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5021180_dbc8_2.jpg"
    },
    "Google Bard AI: The Ultimate Guide - Google Bard AI": {
        "Description": "Learn how to use Google Bard AI to generate text, Write Emails, Blog Posts, Resume, Cover Letter, and creative content!",
        "Is Paid": true,
        "Subscribers": 1083,
        "Average Rating": 4.366667,
        "Number of Reviews": 166,
        "Number of Lectures": 44,
        "Content Length": "6 total hours",
        "Last Update": "2023-11-27",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Ankit Mistry",
            "Vijay Gadhave"
        ],
        "Course URL": "https://www.udemy.com/course/google-bard-the-ultimate-guide-master-generative-ai/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5324606_f26c_3.jpg"
    },
    "PyTorch Ultimate 2024: From Basics to Cutting-Edge": {
        "Description": "Become an expert applying the most popular Deep Learning framework PyTorch",
        "Is Paid": true,
        "Subscribers": 4202,
        "Average Rating": 4.5625,
        "Number of Reviews": 166,
        "Number of Lectures": 171,
        "Content Length": "18 total hours",
        "Last Update": "2024-01-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Bert Gollnick"
        ],
        "Course URL": "https://www.udemy.com/course/pytorch-ultimate/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4684974_9c1b_3.jpg"
    },
    "Neural Networks With MATLAB: Programming For Beginners": {
        "Description": "Neural Network and Its Applications in Data Fitting Problems with MATLAB (ToolBox)",
        "Is Paid": true,
        "Subscribers": 9193,
        "Average Rating": 3.9,
        "Number of Reviews": 166,
        "Number of Lectures": 13,
        "Content Length": "33 total mins",
        "Last Update": "2020-03-31",
        "Badges": [],
        "Course Language": "English (UK)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Karthik K"
        ],
        "Course URL": "https://www.udemy.com/course/neuralnetworkmatlab/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2914498_7d93.jpg"
    },
    "Data Visualization & Data Wrangling Masterclass with Python": {
        "Description": "Master Advanced Data Visualization, Data Preprocessing, Data Wrangling in Python with Industry Level Projects",
        "Is Paid": true,
        "Subscribers": 24129,
        "Average Rating": 4.05,
        "Number of Reviews": 165,
        "Number of Lectures": 167,
        "Content Length": "9.5 total hours",
        "Last Update": "2022-03-24",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Dataisgood Academy"
        ],
        "Course URL": "https://www.udemy.com/course/data-visualization-wrangling-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4169522_f973.jpg"
    },
    "2 in 1: Python Machine Learning PLUS 30 Hour Python Bootcamp": {
        "Description": "Learn model building, algorithms, data science PLUS 30 hours of step by step coding, libraries, arguments, projects +++",
        "Is Paid": true,
        "Subscribers": 1242,
        "Average Rating": 4.3,
        "Number of Reviews": 165,
        "Number of Lectures": 394,
        "Content Length": "45 total hours",
        "Last Update": "2022-10-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Peter Alkema",
            "Regenesys Business School"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-in-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4541086_6ed8_13.jpg"
    },
    "NLP - Natural Language Processing in Python Chatbot GPT 2024": {
        "Description": "Master NLP: Create Chatbots, RASA, ChatGPT, BERT, Transformers, ChatGPT 4, OpenAI GPT - Unlock the Power of Language Pro",
        "Is Paid": true,
        "Subscribers": 1285,
        "Average Rating": 4.551282,
        "Number of Reviews": 164,
        "Number of Lectures": 115,
        "Content Length": "23 total hours",
        "Last Update": "2024-01-09",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Manifold AI Learning \u00ae"
        ],
        "Course URL": "https://www.udemy.com/course/practical-natural-language-processing-go-from-zero-to-hero/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4955494_0897_2.jpg"
    },
    "Machine Learning Projects for Beginners: Work on 10 Projects": {
        "Description": "Build 10 Real World Machine Learning Projects, Step by step guide to build any Machine Learning Project !",
        "Is Paid": true,
        "Subscribers": 1218,
        "Average Rating": 4.45,
        "Number of Reviews": 164,
        "Number of Lectures": 59,
        "Content Length": "9.5 total hours",
        "Last Update": "2023-10-03",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Vijay Gadhave"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-projects-for-beginners-in-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3837086_8d31_3.jpg"
    },
    "Beginning with Machine Learning, Data Science and Python": {
        "Description": "Fundamentals of Data Science :  Exploratory Data Analysis (EDA), Regression (Linear & logistic), Visualization, Basic ML",
        "Is Paid": true,
        "Subscribers": 7933,
        "Average Rating": 4.0,
        "Number of Reviews": 163,
        "Number of Lectures": 49,
        "Content Length": "3.5 total hours",
        "Last Update": "2018-07-01",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "UNP United Network of Professionals"
        ],
        "Course URL": "https://www.udemy.com/course/jumpstart-to-data-science-machine-learning-using-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1483624_e056_3.jpg"
    },
    "Complete Deep Learning In R With Keras & Others": {
        "Description": "Deep Learning: Master Powerful Deep Learning Tools in R Like Keras, Mxnet, H2O and Others",
        "Is Paid": true,
        "Subscribers": 1494,
        "Average Rating": 4.95,
        "Number of Reviews": 163,
        "Number of Lectures": 73,
        "Content Length": "8 total hours",
        "Last Update": "2019-12-23",
        "Badges": [
            "Highest Rated"
        ],
        "Course Language": "English (UK)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Minerva Singh"
        ],
        "Course URL": "https://www.udemy.com/course/complete-deep-learning-in-r-with-keras-others/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2088728_b418_3.jpg"
    },
    "NLTK: Build Document Classifier & Spell Checker with Python": {
        "Description": "NLP with Python - Analyzing Text with the Natural Language Toolkit (NLTK) - Natural Language Processing (NLP) Tutorial",
        "Is Paid": true,
        "Subscribers": 862,
        "Average Rating": 3.65,
        "Number of Reviews": 163,
        "Number of Lectures": 46,
        "Content Length": "5.5 total hours",
        "Last Update": "2019-02-26",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "GoTrained Academy",
            "Waqar Ahmed"
        ],
        "Course URL": "https://www.udemy.com/course/natural-language-processing-python-nltk/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1175220_543f_2.jpg"
    },
    "Deep Learning for Beginners in Python: Work On 12+ Projects": {
        "Description": "Work On 12+ Projects, Deep Learning Python, TensorFlow 2.0, Neural Networks, NLP, Data Science, Machine Learning, More !",
        "Is Paid": true,
        "Subscribers": 1535,
        "Average Rating": 4.076923,
        "Number of Reviews": 162,
        "Number of Lectures": 106,
        "Content Length": "14.5 total hours",
        "Last Update": "2024-01-03",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Vijay Gadhave"
        ],
        "Course URL": "https://www.udemy.com/course/deep-learning-for-beginners-with-tensorflow-20-and-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3330730_9597_3.jpg"
    },
    "Data Science with R - Beginners": {
        "Description": "This training is an introduction to the concept of Data science and its application using R programming language",
        "Is Paid": true,
        "Subscribers": 16284,
        "Average Rating": 3.9,
        "Number of Reviews": 162,
        "Number of Lectures": 56,
        "Content Length": "6 total hours",
        "Last Update": "2018-12-01",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "eduCode Forum"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-with-r-beginners/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2060549_454c.jpg"
    },
    "Accelerate Deep Learning on Raspberry Pi": {
        "Description": "How to Accelerate your AI Object Detection Models 5X faster on a Raspberry Pi 3, using Intel Movidius for Deep Learning",
        "Is Paid": true,
        "Subscribers": 1351,
        "Average Rating": 3.55,
        "Number of Reviews": 161,
        "Number of Lectures": 25,
        "Content Length": "2 total hours",
        "Last Update": "2019-12-01",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Augmented Startups",
            "Laszlo Benke"
        ],
        "Course URL": "https://www.udemy.com/course/accelerate-deep-learning-on-raspberry-pi-movidius/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1630654_4f9a_2.jpg"
    },
    "Get started with GIS & Remote Sensing in QGIS #Beginners": {
        "Description": "Get an overview and learn basics of GIS, QGIS and Remote Sensing with open data & tools (QGIS and Google Earth Engine)",
        "Is Paid": true,
        "Subscribers": 7501,
        "Average Rating": 4.1,
        "Number of Reviews": 161,
        "Number of Lectures": 22,
        "Content Length": "3 total hours",
        "Last Update": "2024-01-18",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Kate Alison"
        ],
        "Course URL": "https://www.udemy.com/course/basics-of-geographic-information-systems-gis-with-open-tools/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2723814_b554_3.jpg"
    },
    "Machine Learning: Beginner Reinforcement Learning in Python": {
        "Description": "How to teach a neural network to play a game using delayed gratification in 146 lines of Python code",
        "Is Paid": true,
        "Subscribers": 528,
        "Average Rating": 4.1,
        "Number of Reviews": 160,
        "Number of Lectures": 24,
        "Content Length": "2 total hours",
        "Last Update": "2020-01-13",
        "Badges": [],
        "Course Language": "English (UK)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Milo Spencer-Harper"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-beginner-reinforcement-learning-in-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2217146_d05b_4.jpg"
    },
    "Convolutional Neural Networks for Medical Images Diagnosis": {
        "Description": "CNN, Deep Learning, Medical Imaging, Transfer Learning, CNN Visualization, VGG, ResNet, Inception, Python & Keras",
        "Is Paid": true,
        "Subscribers": 640,
        "Average Rating": 4.3,
        "Number of Reviews": 157,
        "Number of Lectures": 29,
        "Content Length": "1.5 total hours",
        "Last Update": "2020-06-04",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Hussein Samma"
        ],
        "Course URL": "https://www.udemy.com/course/convolutional-neural-network-for-medical-images-diagnosis/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2978688_c821_3.jpg"
    },
    "Keras: Deep Learning in Python": {
        "Description": "Build complex deep learning algorithms easily in Python",
        "Is Paid": true,
        "Subscribers": 1066,
        "Average Rating": 3.65,
        "Number of Reviews": 157,
        "Number of Lectures": 39,
        "Content Length": "10 total hours",
        "Last Update": "2017-07-17",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Francisco Juretig"
        ],
        "Course URL": "https://www.udemy.com/course/keras-deep-learning-in-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1137212_b9ba.jpg"
    },
    "Computer Vision In Python! Face Detection & Image Processing": {
        "Description": "Learn Computer Vision With OpenCV In Python! Master Python By Implementing Face Recognition & Image Processing In Python",
        "Is Paid": true,
        "Subscribers": 16922,
        "Average Rating": 3.65,
        "Number of Reviews": 157,
        "Number of Lectures": 61,
        "Content Length": "11 total hours",
        "Last Update": "2023-11-13",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Emenwa Global",
            "Zoolord Academy"
        ],
        "Course URL": "https://www.udemy.com/course/computer-vision-in-python-face-detection-image-processing/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3474498_c48e_6.jpg"
    },
    "A to Z (NLP) Machine Learning Model building and Deployment.": {
        "Description": "Python, Docker, Flask, GitLab, Jenkins tools and technology used for deploy model in your Local server. A complete Guide",
        "Is Paid": true,
        "Subscribers": 13973,
        "Average Rating": 4.4,
        "Number of Reviews": 156,
        "Number of Lectures": 31,
        "Content Length": "5 total hours",
        "Last Update": "2023-08-19",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Mohammed Rijwan"
        ],
        "Course URL": "https://www.udemy.com/course/a-to-z-nlp-machine-learning-model-building-and-deployment/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2598110_64c8_3.jpg"
    },
    "Creating Online Dashboards & Story Maps using arcGIS Online": {
        "Description": "Master in Geospatial Data Visualization and Building Operational Dashboards plus Story Maps using ArcGIS Online",
        "Is Paid": true,
        "Subscribers": 7560,
        "Average Rating": 4.181818,
        "Number of Reviews": 154,
        "Number of Lectures": 26,
        "Content Length": "2.5 total hours",
        "Last Update": "2024-01-18",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Shoaib Shahzad Obaidi"
        ],
        "Course URL": "https://www.udemy.com/course/creating-online-dashboards-and-storymaps-using-arcgis-online/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3831676_0a0d_3.jpg"
    },
    "Pandas with Python for Data Science": {
        "Description": "Learn how to get you up and running with data analysis and visualization using Pandas",
        "Is Paid": true,
        "Subscribers": 23450,
        "Average Rating": 4.85,
        "Number of Reviews": 155,
        "Number of Lectures": 58,
        "Content Length": "6 total hours",
        "Last Update": "2021-07-12",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Exam Turf"
        ],
        "Course URL": "https://www.udemy.com/course/pandas-with-python-for-data-science-examturf/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4179758_6128.jpg"
    },
    "The Visual Guide on How Neural Networks Learn from Data": {
        "Description": "The BEST Resource for Understanding Neural Networks and How They Learn",
        "Is Paid": true,
        "Subscribers": 3273,
        "Average Rating": 4.8,
        "Number of Reviews": 155,
        "Number of Lectures": 56,
        "Content Length": "3 total hours",
        "Last Update": "2020-08-06",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Mauricio Maroto"
        ],
        "Course URL": "https://www.udemy.com/course/the-visual-guide-on-how-neural-networks-learn-from-data/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1118274_ac23_2.jpg"
    },
    "Data Science:Hands-on Diabetes Prediction with Pyspark MLlib": {
        "Description": "Diabetes Prediction using Machine Learning in Apache Spark",
        "Is Paid": true,
        "Subscribers": 11843,
        "Average Rating": 4.5,
        "Number of Reviews": 155,
        "Number of Lectures": 6,
        "Content Length": "1 total hour",
        "Last Update": "2020-09-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "School of Disruptive Innovation"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-hands-on-diabetes-prediction-with-pyspark-mllib/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3304348_f458.jpg"
    },
    "Full Stack Data Science with Python, Numpy and R Programming": {
        "Description": "Learn data science with R programming and Python. Use NumPy, Pandas to  manipulate the data and produce outcomes | R",
        "Is Paid": true,
        "Subscribers": 15477,
        "Average Rating": 4.45,
        "Number of Reviews": 155,
        "Number of Lectures": 236,
        "Content Length": "30.5 total hours",
        "Last Update": "2024-02-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Oak Academy",
            "OAK Academy Team"
        ],
        "Course URL": "https://www.udemy.com/course/full-stack-data-science-with-python-numpy-and-r-programming/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3519986_7581_6.jpg"
    },
    "Azure Open AI & Prompt Engineering Zero to Hero with Chatgpt": {
        "Description": "Become an expert in Azure Open AI, Chatgpt & Prompt Engineering from scratch with practical examples - The Master Course",
        "Is Paid": true,
        "Subscribers": 20472,
        "Average Rating": 3.8214285,
        "Number of Reviews": 155,
        "Number of Lectures": 38,
        "Content Length": "3.5 total hours",
        "Last Update": "2023-04-22",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Divyanshu Mehta"
        ],
        "Course URL": "https://www.udemy.com/course/azopenai/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5273720_22b6_3.jpg"
    },
    "Master Scientific Computing in Python with NumPy": {
        "Description": "Explore data science in Python by doing linear algebra, image processing, simple machine learning and more in NumPy!",
        "Is Paid": true,
        "Subscribers": 1168,
        "Average Rating": 4.7,
        "Number of Reviews": 153,
        "Number of Lectures": 74,
        "Content Length": "5.5 total hours",
        "Last Update": "2023-03-06",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "TM Quest"
        ],
        "Course URL": "https://www.udemy.com/course/scientific-computing-with-numpy/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3781750_ca89.jpg"
    },
    "Learn Basic Data science and Python Libraries": {
        "Description": "Covers all Essential Python topics and Libraries for Data Science or Machine Learning Beginner Such as numpy pandas etc.",
        "Is Paid": true,
        "Subscribers": 36012,
        "Average Rating": 2.7,
        "Number of Reviews": 153,
        "Number of Lectures": 9,
        "Content Length": "2.5 total hours",
        "Last Update": "2020-11-08",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Akbar Khan"
        ],
        "Course URL": "https://www.udemy.com/course/basics-data-science-with-numpy-pandas-and-matplotlib/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3433526_b925.jpg"
    },
    "Recommendation Engine Bootcamp with 3 Capstone Projects": {
        "Description": "Master recommendation systems Industry Projects using using modern recommendation techniques and methodologies",
        "Is Paid": true,
        "Subscribers": 14748,
        "Average Rating": 4.35,
        "Number of Reviews": 152,
        "Number of Lectures": 68,
        "Content Length": "4.5 total hours",
        "Last Update": "2022-03-24",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Dataisgood Academy"
        ],
        "Course URL": "https://www.udemy.com/course/recommendation-engine-machine-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4112402_8e98_8.jpg"
    },
    "2024 Master class on Data Science using Python A-Z for ML": {
        "Description": "Python NumPy, Pandas, Matplotlib and Seaborn for Data Analysis, Data Science and ML. Pre-machine learning Analysis.",
        "Is Paid": true,
        "Subscribers": 16671,
        "Average Rating": 4.7,
        "Number of Reviews": 150,
        "Number of Lectures": 87,
        "Content Length": "6.5 total hours",
        "Last Update": "2024-02-01",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Surendra Varma Pericherla"
        ],
        "Course URL": "https://www.udemy.com/course/master-class-on-datascience/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5272092_57db_3.jpg"
    },
    "Data Science: Beginners Guide to the Command Line": {
        "Description": "Master the Basics of the Command Line and Prepare for a Career in Data Science!",
        "Is Paid": true,
        "Subscribers": 8043,
        "Average Rating": 3.9,
        "Number of Reviews": 150,
        "Number of Lectures": 32,
        "Content Length": "1.5 total hours",
        "Last Update": "2017-10-28",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Ben Weinstein"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-beginners-guide-to-the-command-line/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1350136_9cf0_2.jpg"
    },
    "RA: Retail Customer Analytics and Trade Area Modeling.": {
        "Description": "EP3: Learn Python and apply Customer analytics, Churn prediction, Customer Segmentation and Trade Area Modeling.",
        "Is Paid": true,
        "Subscribers": 12977,
        "Average Rating": 4.4375,
        "Number of Reviews": 149,
        "Number of Lectures": 162,
        "Content Length": "15.5 total hours",
        "Last Update": "2022-11-09",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Haytham Omar-Ph.D"
        ],
        "Course URL": "https://www.udemy.com/course/ra-retail-customer-analytics-and-trade-area-modeling/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3877156_7789_13.jpg"
    },
    "Monitoring and Evaluation (M&E) in Development Projects": {
        "Description": "Become a Monitoring and Evaluation Specialist in 3 Hours. Project Management, M&E, PMP, LogFrame, Data Analysis",
        "Is Paid": true,
        "Subscribers": 484,
        "Average Rating": 3.975,
        "Number of Reviews": 149,
        "Number of Lectures": 34,
        "Content Length": "3 total hours",
        "Last Update": "2023-10-10",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Nhoeb Khan"
        ],
        "Course URL": "https://www.udemy.com/course/monitoring_evaluation/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4975892_f2e8_3.jpg"
    },
    "The Complete Healthcare Artificial Intelligence Course 2022": {
        "Description": "Creating powerful AI model for Real-World Healthcare applications with Data Science, Machine Learning and Deep Learning",
        "Is Paid": true,
        "Subscribers": 1323,
        "Average Rating": 4.306452,
        "Number of Reviews": 146,
        "Number of Lectures": 116,
        "Content Length": "18.5 total hours",
        "Last Update": "2021-11-09",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Hoang Quy La"
        ],
        "Course URL": "https://www.udemy.com/course/the-complete-healthcare-artificial-intelligence-course-2021/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3811732_a607_2.jpg"
    },
    "Machine Learning and Deep Learning using Tensor Flow & Keras": {
        "Description": "A-Z Course for Google's Deep Learning Framework - TensorFlow with Python! Learn to use functions and apply Codes.",
        "Is Paid": true,
        "Subscribers": 1943,
        "Average Rating": 3.25,
        "Number of Reviews": 146,
        "Number of Lectures": 99,
        "Content Length": "11 total hours",
        "Last Update": "2018-06-14",
        "Badges": [],
        "Course Language": "English (India)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Dr Aashish Dikshit, PHD(Founder of Lakshmish academy)"
        ],
        "Course URL": "https://www.udemy.com/course/dlmltensorflow/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1556050_d5e2_7.jpg"
    },
    "Python for Data Science Bootcamp 2023: From Zero to Hero": {
        "Description": "Learn Data Science with Python, Pandas, Scikit-learn, and more! | 4 Projects | 100+ exercises | ChatGPT for data science",
        "Is Paid": true,
        "Subscribers": 919,
        "Average Rating": 4.5,
        "Number of Reviews": 146,
        "Number of Lectures": 126,
        "Content Length": "17.5 total hours",
        "Last Update": "2024-01-20",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Frank Andrade"
        ],
        "Course URL": "https://www.udemy.com/course/python-for-data-science-bootcamp-2022-from-zero-to-hero/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4366618_7afe_5.jpg"
    },
    "Taming Regular Expressions (REGEX) - Complete Guide to Regex": {
        "Description": "Regular Expression (Regex) examples in Python, JavaScript, Rust, Java, C#, C++, Swift, Google Sheets, Kotlin and Ruby",
        "Is Paid": true,
        "Subscribers": 1087,
        "Average Rating": 4.714286,
        "Number of Reviews": 146,
        "Number of Lectures": 81,
        "Content Length": "8 total hours",
        "Last Update": "2023-07-18",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Paul Ogier"
        ],
        "Course URL": "https://www.udemy.com/course/taming-regex-a-complete-guide-to-regular-expressions/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2732420_bd36_7.jpg"
    },
    "Machine Learning for Beginners with 6 Real World Projects": {
        "Description": "Build Real-World Machine Learning Applications and Gain Insight on ChatGPT Technology- This Course is Meant for Everyone",
        "Is Paid": true,
        "Subscribers": 13492,
        "Average Rating": 4.45,
        "Number of Reviews": 145,
        "Number of Lectures": 24,
        "Content Length": "2 total hours",
        "Last Update": "2023-08-08",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Eshgin Guluzade"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-for-kids-and-beginners/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3715066_86b0.jpg"
    },
    "Practical Data Science: Reducing High Dimensional Data in R": {
        "Description": "In this R course, we'll see how PCA can reduce a 5000+ variable data set into 10 variables and barely lose accuracy!",
        "Is Paid": true,
        "Subscribers": 1794,
        "Average Rating": 4.45,
        "Number of Reviews": 145,
        "Number of Lectures": 11,
        "Content Length": "2.5 total hours",
        "Last Update": "2017-04-12",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Manuel Amunategui"
        ],
        "Course URL": "https://www.udemy.com/course/practical-data-science-reducing-high-dimensional-data-in-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/598848_5c4e_3.jpg"
    },
    "Professional Diploma in Python Development": {
        "Description": "Python Development Program by MTF Institute: Python at Data Science, Web Development, Machine Learning, Software",
        "Is Paid": true,
        "Subscribers": 15001,
        "Average Rating": 4.3370786,
        "Number of Reviews": 145,
        "Number of Lectures": 32,
        "Content Length": "3 total hours",
        "Last Update": "2023-11-04",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "MTF Institute of Management, Technology & Finance"
        ],
        "Course URL": "https://www.udemy.com/course/introduction-to-python-development/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5559832_e816.jpg"
    },
    "Optimization Using Pattern Search Method: MATLAB Programming": {
        "Description": "A Quick Way to Learn and Solve Optimization Problems in MATLAB. A Course for Beginners.",
        "Is Paid": true,
        "Subscribers": 19988,
        "Average Rating": 4.5,
        "Number of Reviews": 145,
        "Number of Lectures": 21,
        "Content Length": "1 total hour",
        "Last Update": "2022-07-26",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Karthik K"
        ],
        "Course URL": "https://www.udemy.com/course/directsearch/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2982260_064d_2.jpg"
    },
    "Master 3 AI Chatbots in 1 Course: ChatGPT, Bard, Bing Chat": {
        "Description": "Learn how to use ChatGPT, Google Bard, and Bing Chat to simplify your life, improve your business, create stunning image",
        "Is Paid": true,
        "Subscribers": 14178,
        "Average Rating": 3.9285715,
        "Number of Reviews": 144,
        "Number of Lectures": 43,
        "Content Length": "1.5 total hours",
        "Last Update": "2023-06-01",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Neyamul Hasan, M.Pharm"
        ],
        "Course URL": "https://www.udemy.com/course/learn-ai-chatbots-chatgpt-google-bard-bing-chat-edge-image-creator/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5264264_cf02_3.jpg"
    },
    "Professional Certificate in Data Science 2024": {
        "Description": "Learn All the Skills to Become a Data Scientist [ Machine Learning,Deep Learning, CNN, DCGAN, Python, Java, Algorithms]",
        "Is Paid": true,
        "Subscribers": 801,
        "Average Rating": 3.7142856,
        "Number of Reviews": 144,
        "Number of Lectures": 170,
        "Content Length": "26.5 total hours",
        "Last Update": "2024-01-12",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Academy of Computing & Artificial Intelligence"
        ],
        "Course URL": "https://www.udemy.com/course/professional-certificate-in-data-science/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3238375_b357_4.jpg"
    },
    "Data Science:Hands-on Covid-19 Data Analysis & Visualization": {
        "Description": "Create 45 graphs including Choropleth maps, WordCloud, Animation, Bar graphs, scatter plots & more to visualize Covid-19",
        "Is Paid": true,
        "Subscribers": 13783,
        "Average Rating": 4.05,
        "Number of Reviews": 144,
        "Number of Lectures": 15,
        "Content Length": "2 total hours",
        "Last Update": "2020-09-21",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "School of Disruptive Innovation"
        ],
        "Course URL": "https://www.udemy.com/course/hands-on-covid-19-data-visualization-using-plotly-express/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3499092_aa5f_3.jpg"
    },
    "Apache Spark with Scala By Example": {
        "Description": "Advance your Spark skills and become more valuable, confident, and productive",
        "Is Paid": true,
        "Subscribers": 1419,
        "Average Rating": 3.75,
        "Number of Reviews": 143,
        "Number of Lectures": 45,
        "Content Length": "3 total hours",
        "Last Update": "2016-05-23",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Todd McGrath"
        ],
        "Course URL": "https://www.udemy.com/course/learning-spark/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/354532_36b2_3.jpg"
    },
    "Unleash Machine Learning: Build Artificial Neuron in Python": {
        "Description": "A journey into Machine Learning concepts using your very own Artificial Neural Network: Load, Train, Predict, Evaluate",
        "Is Paid": true,
        "Subscribers": 1988,
        "Average Rating": 4.35,
        "Number of Reviews": 143,
        "Number of Lectures": 28,
        "Content Length": "3 total hours",
        "Last Update": "2017-10-09",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Razvan Pistolea"
        ],
        "Course URL": "https://www.udemy.com/course/unleash-machine-learning-build-artificial-neuron-in-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/761380_c68d_3.jpg"
    },
    "ChatGPT Prompts, Data Science & Python Coding PLUS Projects": {
        "Description": "Learn ChatGPT Prompts For Beginners & Intermediate, Maths & Stats Coding In Python, Calculus, Numpy & Matplotlib",
        "Is Paid": true,
        "Subscribers": 1566,
        "Average Rating": 3.9,
        "Number of Reviews": 143,
        "Number of Lectures": 198,
        "Content Length": "19.5 total hours",
        "Last Update": "2023-04-16",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Peter Alkema",
            "TeraVerse Instructor"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-python-maths/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4700194_0be4_5.jpg"
    },
    "Python - Data Analytics - Real World Hands-on Projects": {
        "Description": "First step towards Data Science in this competitive job market",
        "Is Paid": true,
        "Subscribers": 19254,
        "Average Rating": 4.347826,
        "Number of Reviews": 143,
        "Number of Lectures": 8,
        "Content Length": "4.5 total hours",
        "Last Update": "2024-01-11",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Data Science Lovers"
        ],
        "Course URL": "https://www.udemy.com/course/bigdata-analysis-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5231450_3ee9_4.jpg"
    },
    "SVM for Beginners: Support Vector Machines in R Studio": {
        "Description": "Learn Support Vector Machines in R Studio. Basic SVM models to kernel-based advanced SVM models of Machine Learning",
        "Is Paid": true,
        "Subscribers": 56286,
        "Average Rating": 4.45,
        "Number of Reviews": 142,
        "Number of Lectures": 50,
        "Content Length": "5 total hours",
        "Last Update": "2024-01-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Start-Tech Academy"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-adv-support-vector-machines-svm-in-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2420940_7b7b_3.jpg"
    },
    "MACHINE LEARNING MASTER CLASS, AI MADE EASY (Zero to Hero!!)": {
        "Description": "In-depth approach to ML easing you into the basics of ML and making you a pro out of it in no time. Grab this course now",
        "Is Paid": true,
        "Subscribers": 3081,
        "Average Rating": 4.25,
        "Number of Reviews": 142,
        "Number of Lectures": 313,
        "Content Length": "47 total hours",
        "Last Update": "2023-10-09",
        "Badges": [],
        "Course Language": "English (India)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Chand Sheikh",
            "StudyEasy Organisation"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-tutorial/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3329214_28bf_7.jpg"
    },
    "Mastering Chatbots with Botpress, Rasa3, RAG & LLMs Flowise": {
        "Description": "All you need to develop your next AI Chatbot using Open-Source tools like Botpress, Rasa, Transformers and FastAPI",
        "Is Paid": true,
        "Subscribers": 4482,
        "Average Rating": 4.609375,
        "Number of Reviews": 141,
        "Number of Lectures": 128,
        "Content Length": "14.5 total hours",
        "Last Update": "2024-02-01",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Abu Bakr Soliman"
        ],
        "Course URL": "https://www.udemy.com/course/mastering-chatbots-using-botpress-rasa-and-transformers/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5207544_2dc1_2.jpg"
    },
    "AWS SageMaker MasterClass": {
        "Description": "Learn Machine Learning on cloud with AWS SageMaker and No CODE Machine Learning with AWS SageMaker Canvas.",
        "Is Paid": true,
        "Subscribers": 30101,
        "Average Rating": 4.4666667,
        "Number of Reviews": 142,
        "Number of Lectures": 18,
        "Content Length": "2.5 total hours",
        "Last Update": "2022-12-30",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Raj Chhabria"
        ],
        "Course URL": "https://www.udemy.com/course/aws-sagemaker-masterclass/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5039480_5b17_2.jpg"
    },
    "Deploying machine learning models with flask for beginners": {
        "Description": "How to deploy a machine learning model. How to create an API for machine learning. #machinelearning, #datascience",
        "Is Paid": true,
        "Subscribers": 612,
        "Average Rating": 4.1,
        "Number of Reviews": 142,
        "Number of Lectures": 18,
        "Content Length": "2.5 total hours",
        "Last Update": "2023-05-03",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Dan We"
        ],
        "Course URL": "https://www.udemy.com/course/deploying-machine-learning-models-with-flask-for-beginners/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2531482_7e3d_3.jpg"
    },
    "The Fun and Easy Guide to Machine Learning using Keras": {
        "Description": "Learn 16 Machine Learning Algorithms in a Fun and Easy along with Practical Python Labs using Keras",
        "Is Paid": true,
        "Subscribers": 1859,
        "Average Rating": 3.85,
        "Number of Reviews": 141,
        "Number of Lectures": 50,
        "Content Length": "5 total hours",
        "Last Update": "2019-01-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Augmented Startups",
            "Minerva Singh"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-fun-and-easy-using-python-and-keras/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1255504_754e_3.jpg"
    },
    "ChatGPT + Bing Chat: Combined AI Masterclass (1000+ Prompts)": {
        "Description": "Complete Prompt Engineering AI Course for ChatGPT + Bing Chat. Beginner to advanced. 1000+ prompts, Templates Incl.",
        "Is Paid": true,
        "Subscribers": 7719,
        "Average Rating": 4.5108695,
        "Number of Reviews": 140,
        "Number of Lectures": 20,
        "Content Length": "1.5 total hours",
        "Last Update": "2023-10-28",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Navin B"
        ],
        "Course URL": "https://www.udemy.com/course/chatgpt-bing-chat-prompt-engineering-2023-marterclass-course/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5304338_32c3_4.jpg"
    },
    "Byte-Sized-Chunks: Recommendation Systems": {
        "Description": "Build a movie recommendation system in Python - master both theory and practice",
        "Is Paid": true,
        "Subscribers": 3228,
        "Average Rating": 4.2,
        "Number of Reviews": 140,
        "Number of Lectures": 20,
        "Content Length": "4.5 total hours",
        "Last Update": "2016-03-11",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Loony Corn"
        ],
        "Course URL": "https://www.udemy.com/course/recommendation-systems/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/783682_2611_3.jpg"
    },
    "Applied Machine Learning For Healthcare": {
        "Description": "Learn to implement machine learning algorithms to real world life sciences problems",
        "Is Paid": true,
        "Subscribers": 995,
        "Average Rating": 4.2,
        "Number of Reviews": 140,
        "Number of Lectures": 19,
        "Content Length": "5 total hours",
        "Last Update": "2018-12-03",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Eduonix Learning Solutions",
            "Eduonix-Tech ."
        ],
        "Course URL": "https://www.udemy.com/course/applied-machine-learning-for-healthcare/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1803222_f44e_2.jpg"
    },
    "Generative Adversarial Networks (GANs): Complete Guide": {
        "Description": "Deep Learning and Computer Vision to implement projects using one of the most revolutionary technologies in the world!",
        "Is Paid": true,
        "Subscribers": 2225,
        "Average Rating": 4.5833335,
        "Number of Reviews": 140,
        "Number of Lectures": 112,
        "Content Length": "17 total hours",
        "Last Update": "2023-11-19",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Jones Granatyr",
            "Gabriel Alves",
            "AI Expert Academy"
        ],
        "Course URL": "https://www.udemy.com/course/generative-adversarial-networks-gans-complete-guide/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5283810_1d96_2.jpg"
    },
    "Comprehensive Linear Modeling with R": {
        "Description": "Learn to model with R: ANOVA, regression, GLMs, survival analysis, GAMs, mixed-effects, split-plot and nested designs",
        "Is Paid": true,
        "Subscribers": 2322,
        "Average Rating": 4.5,
        "Number of Reviews": 140,
        "Number of Lectures": 104,
        "Content Length": "14.5 total hours",
        "Last Update": "2020-09-28",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Geoffrey Hubona, Ph.D."
        ],
        "Course URL": "https://www.udemy.com/course/comprehensive-linear-modeling-with-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/690278_f248_6.jpg"
    },
    "The Complete Data Science Project Management Course": {
        "Description": "Learn step by step Data Science Project Management through CRISP-DM industry standard data mining methodology",
        "Is Paid": true,
        "Subscribers": 396,
        "Average Rating": 3.15,
        "Number of Reviews": 140,
        "Number of Lectures": 39,
        "Content Length": "1.5 total hours",
        "Last Update": "2018-09-22",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "HiTech Squad"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-project-management/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1912560_d699_2.jpg"
    },
    "Statistics 2023 A-Z\u2122: For Data Science with Both Python & R": {
        "Description": "Beginner to Expert Guide for Data Science and Business Analysis with Case Studies and Hands-on Exercise Using Python & R",
        "Is Paid": true,
        "Subscribers": 1847,
        "Average Rating": 4.25,
        "Number of Reviews": 140,
        "Number of Lectures": 39,
        "Content Length": "15.5 total hours",
        "Last Update": "2023-11-17",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "MG Analytics"
        ],
        "Course URL": "https://www.udemy.com/course/practical-statistics-for-data-science-with-python-and-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4256968_1021_10.jpg"
    },
    "Azure Cloud Azure Databricks Apache Spark Machine learning": {
        "Description": "Big Data, Spark SQL, Hadoop, Kafka, Data Lake, Transfer Learning, Zeppelin Notebook, Graph, Hortonworks HDP, Cloudbreak",
        "Is Paid": true,
        "Subscribers": 764,
        "Average Rating": 2.15,
        "Number of Reviews": 139,
        "Number of Lectures": 74,
        "Content Length": "8.5 total hours",
        "Last Update": "2020-05-20",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Bigdata Engineer"
        ],
        "Course URL": "https://www.udemy.com/course/azure-cloud-azure-databricks-apache-spark-machine-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2295373_d42f_4.jpg"
    },
    "The Complete Artificial Intelligence (AI) for Professionals": {
        "Description": "Learn Google BARD [Gemini], ChatGPT along with 100+ AI tools and use them to Master Business, Ethics and Innovation!",
        "Is Paid": true,
        "Subscribers": 8914,
        "Average Rating": 4.303279,
        "Number of Reviews": 138,
        "Number of Lectures": 129,
        "Content Length": "4.5 total hours",
        "Last Update": "2024-02-02",
        "Badges": [],
        "Course Language": "English (UK)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Debayan Dey"
        ],
        "Course URL": "https://www.udemy.com/course/the-complete-artificial-intelligence-ai-for-professionals/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5352294_5f15_2.jpg"
    },
    "Text Mining and NLP using R and Python": {
        "Description": "Data Science Text Mining and NLP using R and Python",
        "Is Paid": true,
        "Subscribers": 1591,
        "Average Rating": 3.5,
        "Number of Reviews": 139,
        "Number of Lectures": 29,
        "Content Length": "3.5 total hours",
        "Last Update": "2018-08-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "ExcelR Solutions"
        ],
        "Course URL": "https://www.udemy.com/course/text-analyticstext-mining-using-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1067792_96b6_2.jpg"
    },
    "Python Programming: Machine Learning, Deep Learning | Python": {
        "Description": "Python Machine Learning and Python Deep Learning with Data Analysis,  Artificial Intelligence, OOP, and Python Projects",
        "Is Paid": true,
        "Subscribers": 10260,
        "Average Rating": 4.4,
        "Number of Reviews": 139,
        "Number of Lectures": 146,
        "Content Length": "21.5 total hours",
        "Last Update": "2024-02-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Oak Academy",
            "OAK Academy Team",
            "Ali\u0307 CAVDAR"
        ],
        "Course URL": "https://www.udemy.com/course/python-programming-machine-learning-deep-learning-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4066948_6223_4.jpg"
    },
    "The Ultimate Beginners Guide to Python Recommender Systems": {
        "Description": "Use collaborative filtering to recommend movies to users! Implementations step by step from scratch!",
        "Is Paid": true,
        "Subscribers": 13659,
        "Average Rating": 4.678571,
        "Number of Reviews": 138,
        "Number of Lectures": 30,
        "Content Length": "4 total hours",
        "Last Update": "2023-04-27",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Jones Granatyr",
            "AI Expert Academy"
        ],
        "Course URL": "https://www.udemy.com/course/the-ultimate-beginners-guide-to-python-recommender-systems/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4152368_7c04_5.jpg"
    },
    "Data science on COVID-19 / CORONA virus spread data": {
        "Description": "Analysis of CORONA / COVID-19 virus data with Python: data handling, machine learning, visualisation, spread simulations",
        "Is Paid": true,
        "Subscribers": 757,
        "Average Rating": 4.75,
        "Number of Reviews": 138,
        "Number of Lectures": 67,
        "Content Length": "7.5 total hours",
        "Last Update": "2023-05-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Frank Kienle"
        ],
        "Course URL": "https://www.udemy.com/course/applied-data-science-covid-19-prototype/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2932654_e61b_2.jpg"
    },
    "R Programming Ninja Course 2023:Data Science with 5 Projects": {
        "Description": "Complete Beginner to Expert Guide with detailed theory, challenges,Case Studies and Projects .Many courses in one!!",
        "Is Paid": true,
        "Subscribers": 1291,
        "Average Rating": 4.35,
        "Number of Reviews": 137,
        "Number of Lectures": 49,
        "Content Length": "22.5 total hours",
        "Last Update": "2023-11-17",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "MG Analytics"
        ],
        "Course URL": "https://www.udemy.com/course/r-programming-ninja-course-2021-with-5-real-world-projects/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4373744_7179_3.jpg"
    },
    "Big Data & Business Intelligence": {
        "Description": "Everything You Need To Know About Big Data and Business Intelligence for the Modern Workplace",
        "Is Paid": true,
        "Subscribers": 865,
        "Average Rating": 4.35,
        "Number of Reviews": 136,
        "Number of Lectures": 35,
        "Content Length": "4.5 total hours",
        "Last Update": "2016-12-10",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Michael McDonald"
        ],
        "Course URL": "https://www.udemy.com/course/big-data-business-intelligence/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/948584_a436_2.jpg"
    },
    "Search Algorithms in Artificial Intelligence with Java": {
        "Description": "This Artificial Intelligence Course Teaches Theory, Implementation, and Applications With Robot Path Planning",
        "Is Paid": true,
        "Subscribers": 2451,
        "Average Rating": 4.65,
        "Number of Reviews": 136,
        "Number of Lectures": 25,
        "Content Length": "10.5 total hours",
        "Last Update": "2023-11-22",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Tim Buchalka's Learn Programming Academy",
            "Seyedali Mirjalili"
        ],
        "Course URL": "https://www.udemy.com/course/search-algorithms-in-artificial-intelligence-with-java/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2002944_f024.jpg"
    },
    "Artificial General Intelligence AGI : An Introductory course": {
        "Description": "Learn the basics of Artificial General Intelligence AGI with our course, and know the next steps to be in the AI race !",
        "Is Paid": true,
        "Subscribers": 14482,
        "Average Rating": 4.0576925,
        "Number of Reviews": 136,
        "Number of Lectures": 15,
        "Content Length": "1 total hour",
        "Last Update": "2023-05-08",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Prince Patni"
        ],
        "Course URL": "https://www.udemy.com/course/artificial-general-intelligence-agi-an-introductory-course/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5315558_2d00.jpg"
    },
    "Data Science for Marketing Analytics": {
        "Description": "Achieve your marketing goals with the data analytics power of Python",
        "Is Paid": true,
        "Subscribers": 919,
        "Average Rating": 3.5,
        "Number of Reviews": 135,
        "Number of Lectures": 45,
        "Content Length": "4.5 total hours",
        "Last Update": "2019-08-22",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Packt Publishing"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-for-marketing-analytics/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/2521408_6806_2.jpg"
    },
    "Mastering Time Series Forecasting with Python": {
        "Description": "Learn Python, Time Series Model Additive, Multiplicative, AR, Moving Average, Exponential, ARIMA models",
        "Is Paid": true,
        "Subscribers": 22209,
        "Average Rating": 3.85,
        "Number of Reviews": 134,
        "Number of Lectures": 119,
        "Content Length": "11.5 total hours",
        "Last Update": "2022-01-15",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Data Science Anywhere",
            "G Sudheer",
            "Brightshine Learn"
        ],
        "Course URL": "https://www.udemy.com/course/complete-practical-time-series-forecasting-in-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3333632_5979_7.jpg"
    },
    "Master Data Mining in Data Science & Machine Learning": {
        "Description": "Learn about Data Mining Standard Processes, Survival Analysis, Clustering Analysis, Various algorithms and much more.",
        "Is Paid": true,
        "Subscribers": 16965,
        "Average Rating": 4.0,
        "Number of Reviews": 134,
        "Number of Lectures": 84,
        "Content Length": "6 total hours",
        "Last Update": "2022-03-24",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Dataisgood Academy"
        ],
        "Course URL": "https://www.udemy.com/course/data-mining-in-data-science-machine-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4219320_a0eb_2.jpg"
    },
    "KubeFlow Bootcamp": {
        "Description": "Learn how to use Kubeflow for Machine Learning at scale on Google Cloud!",
        "Is Paid": true,
        "Subscribers": 1434,
        "Average Rating": 4.321429,
        "Number of Reviews": 134,
        "Number of Lectures": 55,
        "Content Length": "8 total hours",
        "Last Update": "2023-07-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Jose Portilla"
        ],
        "Course URL": "https://www.udemy.com/course/kubeflow-bootcamp/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5358664_bd6b_2.jpg"
    },
    "Machine Learning Intro for Python Developers": {
        "Description": "Get started with Machine Learning Algorithms",
        "Is Paid": true,
        "Subscribers": 19818,
        "Average Rating": 4.107143,
        "Number of Reviews": 134,
        "Number of Lectures": 19,
        "Content Length": "1 total hour",
        "Last Update": "2019-01-22",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Frank Anemaet"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-intro-for-python-developers/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2092098_7e21_3.jpg"
    },
    "Supercharged Web Scraping with Asyncio and Python": {
        "Description": "Learn the fundamentals of asynchronous web scraping & data mining in Python to drastically improve extraction speeds.",
        "Is Paid": true,
        "Subscribers": 30607,
        "Average Rating": 4.5,
        "Number of Reviews": 134,
        "Number of Lectures": 22,
        "Content Length": "3 total hours",
        "Last Update": "2021-04-13",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Justin Mitchel"
        ],
        "Course URL": "https://www.udemy.com/course/supercharged-web-scraping-with-asyncio-and-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3412184_b4b7.jpg"
    },
    "Data Science in Python: Regression & Forecasting": {
        "Description": "Learn Python for Data Science & Machine Learning, and build regression and forecasting models with hands-on projects",
        "Is Paid": true,
        "Subscribers": 2131,
        "Average Rating": 4.5603447,
        "Number of Reviews": 133,
        "Number of Lectures": 152,
        "Content Length": "8.5 total hours",
        "Last Update": "2023-09-26",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Maven Analytics",
            "Chris Bruehl"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-in-python-regression/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5517074_ca9e.jpg"
    },
    "Data Science with R and Python | R Programming": {
        "Description": "Python and R programming! Learn data science with R &amp; Python with all in one course. You'll learn NumPy, Pandas and more",
        "Is Paid": true,
        "Subscribers": 744,
        "Average Rating": 4.1,
        "Number of Reviews": 132,
        "Number of Lectures": 167,
        "Content Length": "23.5 total hours",
        "Last Update": "2024-02-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Oak Academy",
            "OAK Academy Team"
        ],
        "Course URL": "https://www.udemy.com/course/full-stack-data-science-r-and-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3519920_e45f_8.jpg"
    },
    "Detect Fraud and Predict the Stock Market with TensorFlow": {
        "Description": "\u200bLearn how to code in Python & use TensorFlow! Make a credit card fraud detection model & a stock market prediction app.",
        "Is Paid": true,
        "Subscribers": 1206,
        "Average Rating": 4.25,
        "Number of Reviews": 131,
        "Number of Lectures": 42,
        "Content Length": "7 total hours",
        "Last Update": "2019-01-16",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Mammoth Interactive",
            "John Bura"
        ],
        "Course URL": "https://www.udemy.com/course/detect-fraud-and-predict-the-stock-market-with-tensorflow/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/1513180_1c89.jpg"
    },
    "Hands-On Machine Learning for .NET Developers": {
        "Description": "Use machine learning today without a machine learning background",
        "Is Paid": true,
        "Subscribers": 1000,
        "Average Rating": 3.84375,
        "Number of Reviews": 131,
        "Number of Lectures": 31,
        "Content Length": "3 total hours",
        "Last Update": "2020-06-30",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Packt Publishing"
        ],
        "Course URL": "https://www.udemy.com/course/hands-on-machine-learning-for-net-developers/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3280488_8c66_5.jpg"
    },
    "kickstart your journey to be Bioinformatician(A-Z Guide)2022": {
        "Description": "Updated and To the point course of bioinformatics for beginner students and Academic Professional to peruse their career",
        "Is Paid": true,
        "Subscribers": 1258,
        "Average Rating": 4.5,
        "Number of Reviews": 131,
        "Number of Lectures": 74,
        "Content Length": "4.5 total hours",
        "Last Update": "2022-01-04",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Abdul Rehman Ikram"
        ],
        "Course URL": "https://www.udemy.com/course/kickstart-your-journey-to-be-bioinformaticiana-z-guide2022/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4475512_03a6.jpg"
    },
    "Machine Learning Model Deployment with Flask, React & NodeJS": {
        "Description": "Use web development tools Node.JS, React and Flask to deploy your Data Science models to web apps!",
        "Is Paid": true,
        "Subscribers": 1257,
        "Average Rating": 4.45,
        "Number of Reviews": 131,
        "Number of Lectures": 59,
        "Content Length": "4 total hours",
        "Last Update": "2023-12-21",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Jordan Sauchuk",
            "Ligency Team",
            "Juan Pablo Mejia",
            "SuperDataScience Team"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-model-deployment-with-flask-react-nodejs/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4197696_f2a7_3.jpg"
    },
    "Basics of Artificial Intelligence for beginners (AI)": {
        "Description": "For Beginners: On AI Initiatives",
        "Is Paid": true,
        "Subscribers": 6979,
        "Average Rating": 3.7,
        "Number of Reviews": 131,
        "Number of Lectures": 17,
        "Content Length": "2 total hours",
        "Last Update": "2020-01-14",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Dr. Dheeraj Mehrotra"
        ],
        "Course URL": "https://www.udemy.com/course/basics-of-artificial-intelligence-for-beginners/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2131354_c8f5.jpg"
    },
    "Salesforce CRM Analytics: Einstein & Tableau CRM": {
        "Description": "Boost Salesforce CRM Results with Einstein & Tableau: Data Visualization, Analytics Techniques, and Best Practices",
        "Is Paid": true,
        "Subscribers": 1071,
        "Average Rating": 4.4322033,
        "Number of Reviews": 130,
        "Number of Lectures": 59,
        "Content Length": "4 total hours",
        "Last Update": "2023-10-28",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Yashad Tayal"
        ],
        "Course URL": "https://www.udemy.com/course/salesforce-crm-analytics-einstein-tableau-crm/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5136318_2c2e.jpg"
    },
    "Mastering Artificial Intelligence": {
        "Description": "Your Complete Guide to Artificial Intelligence",
        "Is Paid": true,
        "Subscribers": 539,
        "Average Rating": 4.2772727,
        "Number of Reviews": 129,
        "Number of Lectures": 37,
        "Content Length": "12.5 total hours",
        "Last Update": "2023-10-21",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Selfcode Academy"
        ],
        "Course URL": "https://www.udemy.com/course/mastering-artificial-intelligence/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5540362_0ebf.jpg"
    },
    "Guide to Careers in Data Science - Interview Hacks [2023]": {
        "Description": "An Amazing Interview Preparation guide that includes questions & answers for people with NO experience in Data Science",
        "Is Paid": true,
        "Subscribers": 24599,
        "Average Rating": 4.55,
        "Number of Reviews": 129,
        "Number of Lectures": 106,
        "Content Length": "2 total hours",
        "Last Update": "2023-01-27",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Nizamuddin Siddiqui"
        ],
        "Course URL": "https://www.udemy.com/course/complete-guide-to-crack-a-data-science-interview/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2120426_0b90_6.jpg"
    },
    "Python: Machine Learning, Deep Learning, Pandas, Matplotlib": {
        "Description": "Python, Machine Learning, Deep Learning, Pandas, Seaborn, Matplotlib, Geoplotlib, NumPy,  Data Analysis, Tensorflow",
        "Is Paid": true,
        "Subscribers": 5156,
        "Average Rating": 4.25,
        "Number of Reviews": 129,
        "Number of Lectures": 239,
        "Content Length": "36 total hours",
        "Last Update": "2024-02-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Oak Academy",
            "OAK Academy Team",
            "Ali\u0307 CAVDAR"
        ],
        "Course URL": "https://www.udemy.com/course/python-machine-learning-deep-learning-pandas-matplotlib/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4141774_d0e8_5.jpg"
    },
    "2024 R 4.0 Programming for Data Science || Beginners to Pro": {
        "Description": "Learn Latest R 4 with R-Studio &amp; Jupyter. DataFrame, Vectors, Matrix, DateTime, GGplot2, Tidyverse, Plotly, etc.",
        "Is Paid": true,
        "Subscribers": 12884,
        "Average Rating": 4.65,
        "Number of Reviews": 129,
        "Number of Lectures": 126,
        "Content Length": "14.5 total hours",
        "Last Update": "2024-01-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Laxmi Kant | KGP Talkie"
        ],
        "Course URL": "https://www.udemy.com/course/r-programming-for-data-science-beginners-to-pro/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3700300_3103.jpg"
    },
    "Databricks - Master Azure Databricks for Data Engineers": {
        "Description": "Learn Azure Databricks for professional data engineers using PySpark and Spark SQL",
        "Is Paid": true,
        "Subscribers": 929,
        "Average Rating": 4.899194,
        "Number of Reviews": 124,
        "Number of Lectures": 91,
        "Content Length": "17.5 total hours",
        "Last Update": "2024-01-15",
        "Badges": [
            "Highest Rated"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Learning Journal",
            "Prashant Kumar Pandey"
        ],
        "Course URL": "https://www.udemy.com/course/master-azure-databricks-for-data-engineers/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5733038_d495.jpg"
    },
    "Beginners Guide to Machine Learning - Python, Keras, SKLearn": {
        "Description": "Master the fundamentals of Machine Learning in 2 hours!",
        "Is Paid": true,
        "Subscribers": 2365,
        "Average Rating": 4.35,
        "Number of Reviews": 128,
        "Number of Lectures": 20,
        "Content Length": "2 total hours",
        "Last Update": "2023-01-28",
        "Badges": [],
        "Course Language": "English (UK)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "SA Programmer"
        ],
        "Course URL": "https://www.udemy.com/course/beginners-guide-to-machine-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5071186_98bb.jpg"
    },
    "Machine Learning, Deep Learning & Neural Networks in Matlab": {
        "Description": "Learn deep learning from A to Z and create a neural network in MATLAB to recognize handwritten numbers (MNIST database)",
        "Is Paid": true,
        "Subscribers": 610,
        "Average Rating": 4.2,
        "Number of Reviews": 127,
        "Number of Lectures": 22,
        "Content Length": "4 total hours",
        "Last Update": "2020-03-25",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Eliott Wertheimer",
            "Albert Nassar"
        ],
        "Course URL": "https://www.udemy.com/course/deep-learning-neural-networks-in-matlab-mnist/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2894606_ef6e.jpg"
    },
    "Data Augmentation in NLP": {
        "Description": "Augment your Dataset and Outperform",
        "Is Paid": true,
        "Subscribers": 24535,
        "Average Rating": 4.7,
        "Number of Reviews": 127,
        "Number of Lectures": 12,
        "Content Length": "1 total hour",
        "Last Update": "2020-12-06",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Prathamesh Dahale"
        ],
        "Course URL": "https://www.udemy.com/course/data-augmentation-in-nlp/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3637972_b4ee.jpg"
    },
    "Machine Learning  & Tensorflow - Google Cloud Approach": {
        "Description": "Tensors and TensorFlow",
        "Is Paid": true,
        "Subscribers": 654,
        "Average Rating": 2.75,
        "Number of Reviews": 126,
        "Number of Lectures": 30,
        "Content Length": "3 total hours",
        "Last Update": "2018-04-29",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Notez (Rent a Mind)"
        ],
        "Course URL": "https://www.udemy.com/course/hands-on-machine-learning-google-cloud-approach/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1594160_55a7_2.jpg"
    },
    "Machine Learning in R & Predictive Models | 3 Courses in 1": {
        "Description": "Supervised & unsupervised machine learning in R, clustering in R, predictive models in R by many labs, understand theory",
        "Is Paid": true,
        "Subscribers": 19900,
        "Average Rating": 4.0,
        "Number of Reviews": 126,
        "Number of Lectures": 74,
        "Content Length": "7.5 total hours",
        "Last Update": "2023-11-17",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Kate Alison",
            "Georg M\u00fcller"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-predictive-models-in-r-theory-practice/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3461018_9b07_4.jpg"
    },
    "Data Architecture for Data Scientists": {
        "Description": "Datawarehouse, Data Lake, Data Lakehouse, Data Mesh, Kafka, Lambda &amp; Kappa architecture, Feature Store, Vector DB &amp; more",
        "Is Paid": true,
        "Subscribers": 652,
        "Average Rating": 4.522059,
        "Number of Reviews": 126,
        "Number of Lectures": 36,
        "Content Length": "2 total hours",
        "Last Update": "2024-02-04",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Biju Krishnan"
        ],
        "Course URL": "https://www.udemy.com/course/data-architecture-for-data-scientists/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5295982_ca3c_2.jpg"
    },
    "Build and Deploy Machine Learning App in Cloud with Python": {
        "Description": "Develop and Deploy Machine Learning Web App and Deploy in Python Anywhere Cloud Platform using Python, Flask, Skimage",
        "Is Paid": true,
        "Subscribers": 20068,
        "Average Rating": 4.45,
        "Number of Reviews": 126,
        "Number of Lectures": 56,
        "Content Length": "6.5 total hours",
        "Last Update": "2022-03-14",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Data Science Anywhere",
            "G Sudheer",
            "Brightshine Learn"
        ],
        "Course URL": "https://www.udemy.com/course/deploy-image-classification-flask-web-app-in-pythonanywhere/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3745414_60b9_15.jpg"
    },
    "Understanding Regression Techniques": {
        "Description": "An Introduction to Predictive Analytics for Data Scientists",
        "Is Paid": true,
        "Subscribers": 3510,
        "Average Rating": 3.95,
        "Number of Reviews": 124,
        "Number of Lectures": 89,
        "Content Length": "7 total hours",
        "Last Update": "2019-06-28",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Najib Mozahem"
        ],
        "Course URL": "https://www.udemy.com/course/understanding-regression-techniques/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2344014_bb34_2.jpg"
    },
    "{ C Language } Deep Learning From Ground Up\u2122": {
        "Description": "Build Artificial Intelligence Applications in C",
        "Is Paid": true,
        "Subscribers": 1889,
        "Average Rating": 4.0,
        "Number of Reviews": 124,
        "Number of Lectures": 51,
        "Content Length": "7.5 total hours",
        "Last Update": "2022-07-14",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Israel Gbati",
            "BHM Engineering Academy"
        ],
        "Course URL": "https://www.udemy.com/course/c-language-deep-learning-from-ground-uptm/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2665668_31a2_5.jpg"
    },
    "Master Machine Learning , Deep Learning with Python": {
        "Description": "Complete course covering fundamentals of Machine learning , Deep learning with Python code",
        "Is Paid": true,
        "Subscribers": 6505,
        "Average Rating": 3.5,
        "Number of Reviews": 124,
        "Number of Lectures": 117,
        "Content Length": "5 total hours",
        "Last Update": "2023-05-27",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Vishal Kumar Singh"
        ],
        "Course URL": "https://www.udemy.com/course/demystifying-machine-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2207892_6e27_4.jpg"
    },
    "The Complete Guide to Stata": {
        "Description": "Learn how to master Stata like a professional",
        "Is Paid": true,
        "Subscribers": 810,
        "Average Rating": 4.6585364,
        "Number of Reviews": 122,
        "Number of Lectures": 304,
        "Content Length": "26 total hours",
        "Last Update": "2023-03-11",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "F. Buscha"
        ],
        "Course URL": "https://www.udemy.com/course/the-complete-guide-to-stata/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5196436_ffca_2.jpg"
    },
    "End-to-End Machine Learning: From Idea to Implementation": {
        "Description": "Build, Manage, and Deploy Machine Learning (AI) Projects with Python and MLOps",
        "Is Paid": true,
        "Subscribers": 4691,
        "Average Rating": 4.62,
        "Number of Reviews": 122,
        "Number of Lectures": 277,
        "Content Length": "36 total hours",
        "Last Update": "2024-01-28",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "K\u0131van\u00e7 Y\u00fcksel"
        ],
        "Course URL": "https://www.udemy.com/course/sustainable-and-scalable-machine-learning-project-development/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4070996_5b0b_3.jpg"
    },
    "Machine Learning with SciKit-Learn with Python": {
        "Description": "Get a practical understanding of the Scikit-Learn library and learn the ML implementation",
        "Is Paid": true,
        "Subscribers": 27664,
        "Average Rating": 4.5,
        "Number of Reviews": 121,
        "Number of Lectures": 54,
        "Content Length": "8.5 total hours",
        "Last Update": "2021-07-11",
        "Badges": [
            "Highest Rated"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Exam Turf"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-with-scikit-learn-with-python-examturf/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4177722_4562.jpg"
    },
    "Big Data Analytics in Telecommunication": {
        "Description": "Understanding the transformative nature of Big data analytics in Telecommunication service provider domain",
        "Is Paid": true,
        "Subscribers": 482,
        "Average Rating": 3.4,
        "Number of Reviews": 120,
        "Number of Lectures": 27,
        "Content Length": "1 total hour",
        "Last Update": "2017-11-12",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "RankOne Consulting"
        ],
        "Course URL": "https://www.udemy.com/course/big-data-analytics-for-telecom/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/799562_388a_4.jpg"
    },
    "R Ultimate 2024: R for Data Science and Machine Learning": {
        "Description": "R Basics, Data Science, Statistical Machine Learning models, Deep Learning, Shiny and much more (All R code included)",
        "Is Paid": true,
        "Subscribers": 1181,
        "Average Rating": 4.4333334,
        "Number of Reviews": 120,
        "Number of Lectures": 203,
        "Content Length": "22.5 total hours",
        "Last Update": "2024-01-14",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Bert Gollnick"
        ],
        "Course URL": "https://www.udemy.com/course/r-ultimate-learn-r-for-data-science-and-machine-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3372022_fb97_3.jpg"
    },
    "Experimental Machine Learning & Data Mining: Weka, MOA & R": {
        "Description": "Learn how to start your Machine Learning journey with Weka, MOA to Build your next Predicative Machine Learning Models.",
        "Is Paid": true,
        "Subscribers": 2703,
        "Average Rating": 4.3,
        "Number of Reviews": 118,
        "Number of Lectures": 83,
        "Content Length": "3.5 total hours",
        "Last Update": "2023-09-10",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Shadi Oweda"
        ],
        "Course URL": "https://www.udemy.com/course/weka-for-data-mining-and-machine-learning-for-beginners/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2829614_c8af.jpg"
    },
    "Data Wrangling in Pandas for Machine Learning Engineers": {
        "Description": "The Second Course in a Series for Mastering Python for Machine Learning Engineers",
        "Is Paid": true,
        "Subscribers": 799,
        "Average Rating": 4.15,
        "Number of Reviews": 117,
        "Number of Lectures": 89,
        "Content Length": "2 total hours",
        "Last Update": "2020-01-22",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Mike West"
        ],
        "Course URL": "https://www.udemy.com/course/data-wrangling-in-pandas-for-machine-learning-engineers/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1437428_7336_3.jpg"
    },
    "Statistical Thinking and Data Science with R.": {
        "Description": "R from A-Z!  Statistics, Advanced Regression,Visualizations, Probabilities, Inference, Simulations and Machine learning.",
        "Is Paid": true,
        "Subscribers": 17671,
        "Average Rating": 4.45,
        "Number of Reviews": 117,
        "Number of Lectures": 243,
        "Content Length": "27 total hours",
        "Last Update": "2023-08-12",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Haytham Omar-Ph.D"
        ],
        "Course URL": "https://www.udemy.com/course/statistical-thinking-for-data-science-business-analytics/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3526754_2038_22.jpg"
    },
    "Bio-inspired Artificial Intelligence Algorithms": {
        "Description": "Genetic algorithm, differential evolution, neural networks, clonal selection, particle swarm, ant colony optimization",
        "Is Paid": true,
        "Subscribers": 1487,
        "Average Rating": 4.464286,
        "Number of Reviews": 116,
        "Number of Lectures": 88,
        "Content Length": "8.5 total hours",
        "Last Update": "2023-04-27",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Jones Granatyr",
            "Guilherme Matos Passarini, phD",
            "AI Expert Academy"
        ],
        "Course URL": "https://www.udemy.com/course/bio-inspired-artificial-intelligence-algorithms-for-optimization/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4639264_b2c9.jpg"
    },
    "Mathematics for Data Science and Machine Learning using R": {
        "Description": "Learn the fundamental mathematics for Data Science, AI &ML using R",
        "Is Paid": true,
        "Subscribers": 935,
        "Average Rating": 4.45,
        "Number of Reviews": 116,
        "Number of Lectures": 65,
        "Content Length": "10.5 total hours",
        "Last Update": "2019-07-30",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Eduonix Learning Solutions",
            "Eduonix-Tech ."
        ],
        "Course URL": "https://www.udemy.com/course/mathematics-for-data-science-and-machine-learning-using-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2361054_3541.jpg"
    },
    "Unlocking the Power of ChatGPT in Data Science : A-Z Guide": {
        "Description": "Learn how to effectively use ChatGPT as a Data Scientist and make the most of this revolutionary AI tool : ChatGPT",
        "Is Paid": true,
        "Subscribers": 23805,
        "Average Rating": 4.137931,
        "Number of Reviews": 115,
        "Number of Lectures": 35,
        "Content Length": "2 total hours",
        "Last Update": "2023-02-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Prince Patni"
        ],
        "Course URL": "https://www.udemy.com/course/unlocking-the-power-of-chatgpt-in-data-science-a-z-guide/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5098388_de87_2.jpg"
    },
    "Master Deep Learning for Computer Vision in TensorFlow[2024]": {
        "Description": "Use ConvNets &amp; Vision Transformers to build projects in Image classification,generation,segmentation &amp; Object detection",
        "Is Paid": true,
        "Subscribers": 835,
        "Average Rating": 4.2647057,
        "Number of Reviews": 115,
        "Number of Lectures": 139,
        "Content Length": "45.5 total hours",
        "Last Update": "2023-07-06",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Neuralearn Dot AI"
        ],
        "Course URL": "https://www.udemy.com/course/master-deep-learning-for-computer-vision-with-tensorflow-2/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4269568_7a49_3.jpg"
    },
    "PyTorch for Deep Learning Computer Vision Bootcamp 2024": {
        "Description": "Master Computer Vision in PyTorch/Python: Beginner to Pro with Expert Tips on Convolutional Neural Networks (CNNs)",
        "Is Paid": true,
        "Subscribers": 7868,
        "Average Rating": 4.15,
        "Number of Reviews": 115,
        "Number of Lectures": 82,
        "Content Length": "10.5 total hours",
        "Last Update": "2024-01-09",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Manifold AI Learning \u00ae"
        ],
        "Course URL": "https://www.udemy.com/course/deep-learning-pytorch/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2494264_9a0d.jpg"
    },
    "Machine Learning Unleashed: Mastering Algorithms and Models": {
        "Description": "Deep dive into Machine Learning with Python Programming. Implement practical scenarios &amp; a project on Recommender System",
        "Is Paid": true,
        "Subscribers": 24757,
        "Average Rating": 3.65,
        "Number of Reviews": 114,
        "Number of Lectures": 30,
        "Content Length": "24 total hours",
        "Last Update": "2024-01-20",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Uplatz Training"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-with-python-training/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3546664_ca57_8.jpg"
    },
    "Build Chatbot using RASA 2x in 2021": {
        "Description": "Let's build a university Chatbot that will fetch attendance, marks in real-time. Also, it will be able to answer FAQs.",
        "Is Paid": true,
        "Subscribers": 947,
        "Average Rating": 3.7,
        "Number of Reviews": 113,
        "Number of Lectures": 26,
        "Content Length": "2 total hours",
        "Last Update": "2021-01-24",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Aqib Ahmed"
        ],
        "Course URL": "https://www.udemy.com/course/build-chatbot-using-rasa-2x/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3778302_5dbc_3.jpg"
    },
    "Data Science Marathon: 120 Projects To Build Your Portfolio": {
        "Description": "Build 120 Projects in 120 Days- Data Science, Machine Learning, Deep Learning (Python, Flask, Django, AWS, Heruko Cloud)",
        "Is Paid": true,
        "Subscribers": 2869,
        "Average Rating": 4.2,
        "Number of Reviews": 111,
        "Number of Lectures": 794,
        "Content Length": "132.5 total hours",
        "Last Update": "2022-11-20",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Pianalytix ."
        ],
        "Course URL": "https://www.udemy.com/course/build-real-world-data-science-projects/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4885940_14ce_2.jpg"
    },
    "Big Data Complete Course": {
        "Description": "Learn HDFS, Spark, Kafka, Machine Learning, Hadoop, Hadoop MapReduce, Cassandra, CAP, Predictive Analytics and much more",
        "Is Paid": true,
        "Subscribers": 27728,
        "Average Rating": 3.8181818,
        "Number of Reviews": 112,
        "Number of Lectures": 36,
        "Content Length": "18.5 total hours",
        "Last Update": "2021-07-15",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Edcorner Learning"
        ],
        "Course URL": "https://www.udemy.com/course/big-data-complete-course/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4184124_aa3a.jpg"
    },
    "Statistics for Data Science and Business Analysis - 2024": {
        "Description": "Statistics you need at the Project : Descriptive and Inferential statistics, Hypothesis testing, Regression analysis",
        "Is Paid": true,
        "Subscribers": 1179,
        "Average Rating": 4.340909,
        "Number of Reviews": 112,
        "Number of Lectures": 134,
        "Content Length": "23 total hours",
        "Last Update": "2024-01-09",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Manifold AI Learning \u00ae"
        ],
        "Course URL": "https://www.udemy.com/course/statistics-probability-for-data-science/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4880084_9f0b.jpg"
    },
    "More Data Mining with R": {
        "Description": "How to perform market basket analysis, analyze social networks, mine Twitter data, text, and time series data.",
        "Is Paid": true,
        "Subscribers": 2579,
        "Average Rating": 3.0,
        "Number of Reviews": 111,
        "Number of Lectures": 67,
        "Content Length": "10.5 total hours",
        "Last Update": "2020-08-01",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Geoffrey Hubona, Ph.D."
        ],
        "Course URL": "https://www.udemy.com/course/more-data-mining-with-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/586534_56fa_2.jpg"
    },
    "Business Statistics Fundamentals": {
        "Description": "Learn everything you need to know about statistics used in businesses",
        "Is Paid": true,
        "Subscribers": 1498,
        "Average Rating": 4.5,
        "Number of Reviews": 110,
        "Number of Lectures": 94,
        "Content Length": "8.5 total hours",
        "Last Update": "2023-12-27",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Rajarshi Sarma"
        ],
        "Course URL": "https://www.udemy.com/course/business-statistics-fundamentals/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1679590_f41a.jpg"
    },
    "Python ReportLab from Beginner to Winner": {
        "Description": "Generate Dynamically PDF files using Python and ReportLab",
        "Is Paid": true,
        "Subscribers": 644,
        "Average Rating": 4.45,
        "Number of Reviews": 108,
        "Number of Lectures": 21,
        "Content Length": "8.5 total hours",
        "Last Update": "2022-02-07",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Hugo Ferro"
        ],
        "Course URL": "https://www.udemy.com/course/python-reportlab-from-beginner-to-winner/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3957618_0d1f_5.jpg"
    },
    "Machine Learning Projects A-Z : Kaggle and Real World Pro": {
        "Description": "Master Machine Learning Kaggle and Real World Projects and Start Participating in Competitive Forums",
        "Is Paid": true,
        "Subscribers": 1461,
        "Average Rating": 4.0,
        "Number of Reviews": 108,
        "Number of Lectures": 59,
        "Content Length": "8 total hours",
        "Last Update": "2019-02-22",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Geekshub Pvt Ltd"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-projects-kaggle-and-real-world-pro/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2228522_e078_2.jpg"
    },
    "Data Pre-Processing for Data Analytics and Data Science": {
        "Description": "Pre-Processing for Data Analytics and Data Science",
        "Is Paid": true,
        "Subscribers": 2245,
        "Average Rating": 4.5930233,
        "Number of Reviews": 107,
        "Number of Lectures": 48,
        "Content Length": "9 total hours",
        "Last Update": "2024-02-01",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Elearning Moocs"
        ],
        "Course URL": "https://www.udemy.com/course/data-pre-processing-for-data-analytics-and-data-science/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5255106_2697_2.jpg"
    },
    "Statistics and Hypothesis Testing for Data science": {
        "Description": "\"Mastering Data Analysis and Making Informed Decisions with Statistical Hypothesis Testing in Data Science\".",
        "Is Paid": true,
        "Subscribers": 13521,
        "Average Rating": 4.609756,
        "Number of Reviews": 100,
        "Number of Lectures": 31,
        "Content Length": "4.5 total hours",
        "Last Update": "2023-12-01",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Meritshot Academy"
        ],
        "Course URL": "https://www.udemy.com/course/statistics-and-hypothesis-testing-for-data-science/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5481410_6bc1_4.jpg"
    },
    "2024 Data Science Interview Preparation Guide": {
        "Description": "Interview questions and answers in data science, statistics, machine learning, deep learning, culture fit and SQL.",
        "Is Paid": true,
        "Subscribers": 1703,
        "Average Rating": 4.15,
        "Number of Reviews": 106,
        "Number of Lectures": 156,
        "Content Length": "4 total hours",
        "Last Update": "2023-06-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Dr. Gary White"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-interview-preparation-guide/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3500298_bf51_8.jpg"
    },
    "50-Days 50-Projects: Data Science, Machine Learning Bootcamp": {
        "Description": "Build & Deploy Data Science, ML, Deep Learning Projects Course(Python, Flask, Django, AWS, Azure, GCP, Heruko Cloud)",
        "Is Paid": true,
        "Subscribers": 1606,
        "Average Rating": 3.75,
        "Number of Reviews": 106,
        "Number of Lectures": 366,
        "Content Length": "46 total hours",
        "Last Update": "2021-11-14",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Pianalytix ."
        ],
        "Course URL": "https://www.udemy.com/course/real-world-data-science-machine-learning-projects/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4329636_b65c_4.jpg"
    },
    "100 Days Data Science Bootcamp: Build 100 Real Life Projects": {
        "Description": "Build & Deploy Data Science, Machine Learning, Deep Learning (Python, Flask, Django, AWS, Azure, GCP, Heruko Cloud)",
        "Is Paid": true,
        "Subscribers": 2748,
        "Average Rating": 4.05,
        "Number of Reviews": 106,
        "Number of Lectures": 731,
        "Content Length": "105.5 total hours",
        "Last Update": "2022-09-06",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Pianalytix ."
        ],
        "Course URL": "https://www.udemy.com/course/real-world-data-science-projects/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4539674_c7e1_2.jpg"
    },
    "Machine Learning Project: Heart Attack Prediction Analysis": {
        "Description": "Data Science &amp; Machine Learning - Boost your Machine Learning, statistics skills with real heart attack analysis project",
        "Is Paid": true,
        "Subscribers": 783,
        "Average Rating": 4.428571,
        "Number of Reviews": 105,
        "Number of Lectures": 53,
        "Content Length": "7.5 total hours",
        "Last Update": "2024-02-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Oak Academy",
            "OAK Academy Team"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-project-heart-attack-prediction-analysis/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4682726_d689_4.jpg"
    },
    "Game Devs Unleash Artificial Intelligence: Flocking Agents": {
        "Description": "Artificial Intelligence for Game Devs in Unity to understand & implement the beautiful bird's natural Flocking Behavior",
        "Is Paid": true,
        "Subscribers": 1288,
        "Average Rating": 4.15,
        "Number of Reviews": 105,
        "Number of Lectures": 27,
        "Content Length": "2.5 total hours",
        "Last Update": "2017-10-09",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Razvan Pistolea"
        ],
        "Course URL": "https://www.udemy.com/course/helping-game-devs-unleash-artificial-intelligence-flocking/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/415720_a201_3.jpg"
    },
    "Optimization with Excel: Operations Research without Coding": {
        "Description": "Optimization with Gurobi, CBC, IPOPT. Linear programming, nonlinear, genetic algorithm. Using Excel, without coding",
        "Is Paid": true,
        "Subscribers": 747,
        "Average Rating": 4.85,
        "Number of Reviews": 105,
        "Number of Lectures": 81,
        "Content Length": "10 total hours",
        "Last Update": "2023-06-10",
        "Badges": [
            "Highest Rated"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Rafael Silva Pinto"
        ],
        "Course URL": "https://www.udemy.com/course/optimization-with-excel-operations-research-without-coding/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4342076_15a4_31.jpg"
    },
    "Geospatial APIs For Data Science Applications In Python": {
        "Description": "Data Science With Google Earth Engine (GEE) and Foursquare With Python Using Application Programming Interfaces (APIs)",
        "Is Paid": true,
        "Subscribers": 3571,
        "Average Rating": 4.7,
        "Number of Reviews": 105,
        "Number of Lectures": 74,
        "Content Length": "6 total hours",
        "Last Update": "2023-11-14",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Minerva Singh"
        ],
        "Course URL": "https://www.udemy.com/course/geospatial-apis-for-data-science-applications-in-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4228472_e9db.jpg"
    },
    "Artificial Intelligence #6 : LSTM Neural Networks with Keras": {
        "Description": "Learn how to create Recurrent Neural Network and LSTMs by using Keras Libraries and Python",
        "Is Paid": true,
        "Subscribers": 1595,
        "Average Rating": 2.5,
        "Number of Reviews": 105,
        "Number of Lectures": 27,
        "Content Length": "2 total hours",
        "Last Update": "2018-11-07",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Sobhan N."
        ],
        "Course URL": "https://www.udemy.com/course/artificial-intelligence-6-lstm-neural-networks-with-keras/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1764006_b82d.jpg"
    },
    "Statistics in Depth for Business Analytics and Data Science": {
        "Description": "Master the Statistics in Python and Data Science along with in-depth examples. Solid Foundation in Statistics Guaranteed",
        "Is Paid": true,
        "Subscribers": 12365,
        "Average Rating": 3.95,
        "Number of Reviews": 104,
        "Number of Lectures": 60,
        "Content Length": "6.5 total hours",
        "Last Update": "2022-03-24",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Dataisgood Academy"
        ],
        "Course URL": "https://www.udemy.com/course/statistics-for-data-science-and-business-analytics/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4219344_dc45_2.jpg"
    },
    "Learn Data Science Basics": {
        "Description": "Basics of Data Science",
        "Is Paid": true,
        "Subscribers": 9929,
        "Average Rating": 3.4,
        "Number of Reviews": 103,
        "Number of Lectures": 11,
        "Content Length": "1.5 total hours",
        "Last Update": "2023-11-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Dr. Dheeraj Mehrotra"
        ],
        "Course URL": "https://www.udemy.com/course/learn-data-science-basics/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2538340_d462.jpg"
    },
    "Linear Regression: Absolute Fundamentals": {
        "Description": "Explore COVID-19 positive case prediction with scikit-learn's Linear Regression in Python.",
        "Is Paid": true,
        "Subscribers": 10327,
        "Average Rating": 4.1,
        "Number of Reviews": 103,
        "Number of Lectures": 12,
        "Content Length": "2.5 total hours",
        "Last Update": "2023-10-25",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Sujithkumar MA"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-linear-regression-absolute-fundamentals/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3322462_f359_3.jpg"
    },
    "Learn & Deploy Data Science Web Apps with Streamlit": {
        "Description": "Learn, Develop and Deploy Streamlit web app for Data Science application using just Python",
        "Is Paid": true,
        "Subscribers": 757,
        "Average Rating": 4.6,
        "Number of Reviews": 103,
        "Number of Lectures": 74,
        "Content Length": "5.5 total hours",
        "Last Update": "2023-09-26",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "G Sudheer",
            "Data Science Anywhere",
            "Brightshine Learn"
        ],
        "Course URL": "https://www.udemy.com/course/streamlit-for-datascience/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4461858_712e_4.jpg"
    },
    "Automated Machine Learning with AutoGluon Library in Python": {
        "Description": "Discover how to easily automate entire machine learning pipelines with the extremely powerful Autogluon library from AWS",
        "Is Paid": true,
        "Subscribers": 1353,
        "Average Rating": 4.785714,
        "Number of Reviews": 103,
        "Number of Lectures": 37,
        "Content Length": "5.5 total hours",
        "Last Update": "2023-07-20",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Jose Portilla"
        ],
        "Course URL": "https://www.udemy.com/course/automated-machine-learning-with-autogluon-library-in-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5231548_b06b_4.jpg"
    },
    "Deep Learning for Image Segmentation with Python & Pytorch": {
        "Description": "Image Semantic Segmentation for Computer Vision with PyTorch & Python to Train & Deploy YOUR own Models (UNet, DeepLab)",
        "Is Paid": true,
        "Subscribers": 404,
        "Average Rating": 4.3777776,
        "Number of Reviews": 103,
        "Number of Lectures": 35,
        "Content Length": "3.5 total hours",
        "Last Update": "2023-07-14",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Mazhar Hussain",
            "AI & Computer Science School"
        ],
        "Course URL": "https://www.udemy.com/course/deep-learning-for-semantic-segmentation-with-python-pytorh/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5092818_4100_3.jpg"
    },
    "Deep Learning with Google Colab": {
        "Description": "Implementing and training deep learning models in a free, integrated environment",
        "Is Paid": true,
        "Subscribers": 7602,
        "Average Rating": 4.25,
        "Number of Reviews": 103,
        "Number of Lectures": 61,
        "Content Length": "5.5 total hours",
        "Last Update": "2020-02-06",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "BPB Online + 100 Million Books Sold"
        ],
        "Course URL": "https://www.udemy.com/course/deep-learning-with-google-colab/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2579724_2eb4.jpg"
    },
    "Artificial Intelligence for Beginners: Understand the basics": {
        "Description": "Specially designed course for a complete beginner to help clarify the basics of Artificial Intelligence.",
        "Is Paid": true,
        "Subscribers": 431,
        "Average Rating": 4.175,
        "Number of Reviews": 102,
        "Number of Lectures": 20,
        "Content Length": "5 total hours",
        "Last Update": "2022-11-27",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Nikita Aakhade"
        ],
        "Course URL": "https://www.udemy.com/course/artificial-intelligence-for-beginners-understand-the-basics/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4962846_5d6a_6.jpg"
    },
    "Full Stack Data Science Course - Become a Data Scientist": {
        "Description": "Master the four major areas of Data Science and become a Full Stack Data Scientist in 2021.",
        "Is Paid": true,
        "Subscribers": 1792,
        "Average Rating": 4.15,
        "Number of Reviews": 102,
        "Number of Lectures": 33,
        "Content Length": "2 total hours",
        "Last Update": "2021-02-04",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "The Click Reader",
            "Merishna Singh Suwal"
        ],
        "Course URL": "https://www.udemy.com/course/full-stack-data-science-course/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3512066_f3a8_5.jpg"
    },
    "Pig For Wrangling Big Data": {
        "Description": "Extract, Transform and Load data using Pig to harness the power of Hadoop",
        "Is Paid": true,
        "Subscribers": 3363,
        "Average Rating": 3.7,
        "Number of Reviews": 102,
        "Number of Lectures": 35,
        "Content Length": "5.5 total hours",
        "Last Update": "2016-11-18",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Loony Corn"
        ],
        "Course URL": "https://www.udemy.com/course/pig-for-wrangling-big-data/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/886032_0f11.jpg"
    },
    "2024 Python for Machine Learning: A Step-by-Step Guide": {
        "Description": "Data Science Projects with Linear Regression, Logistic Regression, Random Forest, SVM, KNN, KMeans, XGBoost, PCA etc",
        "Is Paid": true,
        "Subscribers": 11423,
        "Average Rating": 4.48,
        "Number of Reviews": 102,
        "Number of Lectures": 280,
        "Content Length": "32 total hours",
        "Last Update": "2024-01-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Laxmi Kant | KGP Talkie"
        ],
        "Course URL": "https://www.udemy.com/course/python-for-machine-learning-and-data-science-projects/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3435072_bfef.jpg"
    },
    "Create Analytics Dashboard with PowerBi and Tableau": {
        "Description": "Learn to create Visualization Reports on Tableau | Data Analysis | Data Science | Business Intelligence with Power BI",
        "Is Paid": true,
        "Subscribers": 7757,
        "Average Rating": 4.45,
        "Number of Reviews": 101,
        "Number of Lectures": 26,
        "Content Length": "2 total hours",
        "Last Update": "2023-01-11",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Harshit Srivastava"
        ],
        "Course URL": "https://www.udemy.com/course/create-analytics-dashboard-with-powerbi-and-tableau/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4024026_1043_5.jpg"
    },
    "Statistics for Data science": {
        "Description": "This course teaches Data Science with Maths statistics from basic to advanced level.",
        "Is Paid": true,
        "Subscribers": 3524,
        "Average Rating": 3.9,
        "Number of Reviews": 101,
        "Number of Lectures": 5,
        "Content Length": "1 total hour",
        "Last Update": "2019-07-03",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Shivprasad Koirala"
        ],
        "Course URL": "https://www.udemy.com/course/datascience-statistics/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2356514_2b1c_2.jpg"
    },
    "Artificial Intelligence and Machine Learning Fundamentals": {
        "Description": "Learn to develop real-world applications powered by the latest advances in intelligent systems",
        "Is Paid": true,
        "Subscribers": 614,
        "Average Rating": 3.9,
        "Number of Reviews": 99,
        "Number of Lectures": 53,
        "Content Length": "8 total hours",
        "Last Update": "2020-02-13",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Expert Level",
        "Authors": [
            "Packt Publishing"
        ],
        "Course URL": "https://www.udemy.com/course/artificial-intelligence-and-machine-learning-fundamentals/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2291401_cc64_3.jpg"
    },
    "Curiosity Driven Deep Reinforcement Learning": {
        "Description": "How Agents Can Learn In Environments With No Rewards",
        "Is Paid": true,
        "Subscribers": 1272,
        "Average Rating": 4.75,
        "Number of Reviews": 99,
        "Number of Lectures": 27,
        "Content Length": "4 total hours",
        "Last Update": "2023-07-09",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Expert Level",
        "Authors": [
            "Phil Tabor"
        ],
        "Course URL": "https://www.udemy.com/course/curiosity-driven-deep-reinforcement-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4332214_a904_3.jpg"
    },
    "Avaya IP Office Server": {
        "Description": "Learn Avaya IP Office Intelligent Communications and Artificial Intelligence",
        "Is Paid": true,
        "Subscribers": 347,
        "Average Rating": 3.55,
        "Number of Reviews": 98,
        "Number of Lectures": 29,
        "Content Length": "3 total hours",
        "Last Update": "2021-10-06",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Juan Sebastian Garcia"
        ],
        "Course URL": "https://www.udemy.com/course/avaya-ip-office-server-kn/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2573884_7f75_4.jpg"
    },
    "Introduction to Generative Adversarial Networks with PyTorch": {
        "Description": "A comprehensive course on GANs including state of the art methods, recent techniques, and step-by-step hands-on projects",
        "Is Paid": true,
        "Subscribers": 945,
        "Average Rating": 4.05,
        "Number of Reviews": 98,
        "Number of Lectures": 34,
        "Content Length": "6 total hours",
        "Last Update": "2021-05-14",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Mustafa Qamaruddin"
        ],
        "Course URL": "https://www.udemy.com/course/introduction-to-generative-adversarial-networks-with-pytorch/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2332450_7223_3.jpg"
    },
    "JavaScript Wizardry: The Basics Unveiled": {
        "Description": "Master the Power of JavaScript in under 10 hrs: Mastering the Inner Workings for Javascript : ChatGPT : HTML : CSS",
        "Is Paid": true,
        "Subscribers": 8130,
        "Average Rating": 4.75,
        "Number of Reviews": 97,
        "Number of Lectures": 46,
        "Content Length": "8.5 total hours",
        "Last Update": "2023-05-27",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "The Table Of Bosses",
            "Cornell Literacy",
            "Rechcel Toledo"
        ],
        "Course URL": "https://www.udemy.com/course/javascript-mastery-learn-the-ins-outs-of-javascript/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5350854_82b1_3.jpg"
    },
    "Image Processing and Computer Vision with Python & OpenCV": {
        "Description": "Learn Image Processing and Computer Vision from AI (ML & DL) professional",
        "Is Paid": true,
        "Subscribers": 582,
        "Average Rating": 3.4,
        "Number of Reviews": 97,
        "Number of Lectures": 77,
        "Content Length": "9.5 total hours",
        "Last Update": "2023-08-23",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Shiv Onkar Deepak Kumar"
        ],
        "Course URL": "https://www.udemy.com/course/image-processing-and-computer-vision-with-python-opencv/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2213906_43b2_2.jpg"
    },
    "Basics of R Software for Data Science": {
        "Description": "Descriptive Statistics using R Software",
        "Is Paid": true,
        "Subscribers": 1280,
        "Average Rating": 4.45,
        "Number of Reviews": 96,
        "Number of Lectures": 8,
        "Content Length": "4.5 total hours",
        "Last Update": "2021-07-16",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Prof R Madana Mohana"
        ],
        "Course URL": "https://www.udemy.com/course/basics-of-r-software-for-data-science/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4187446_ca25_2.jpg"
    },
    "Machine Learning For Researchers": {
        "Description": "Learn Research Methods & Machine Learning",
        "Is Paid": true,
        "Subscribers": 16850,
        "Average Rating": 4.75,
        "Number of Reviews": 96,
        "Number of Lectures": 13,
        "Content Length": "5.5 total hours",
        "Last Update": "2020-06-29",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Academy of Computing & Artificial Intelligence",
            "Kaneeka Vidanage"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-for-researchers/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3271880_6266.jpg"
    },
    "Neural Network Trading Bot": {
        "Description": "Build a Machine Learning Trading Bot from scratch",
        "Is Paid": true,
        "Subscribers": 698,
        "Average Rating": 3.8,
        "Number of Reviews": 95,
        "Number of Lectures": 41,
        "Content Length": "5 total hours",
        "Last Update": "2020-05-24",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Vinay Phadnis"
        ],
        "Course URL": "https://www.udemy.com/course/neural-network-trading-bot/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2369132_6e8d_2.jpg"
    },
    "Deep Learning with Python & Pytorch for Image Classification": {
        "Description": "Deep Learning & Computer Vision for Image Classification with PyTorch & Python.Train,Test & Deploy Models on Custom data",
        "Is Paid": true,
        "Subscribers": 3659,
        "Average Rating": 4.9565215,
        "Number of Reviews": 95,
        "Number of Lectures": 25,
        "Content Length": "2 total hours",
        "Last Update": "2023-07-17",
        "Badges": [
            "Highest Rated"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "AI & Computer Science School",
            "Mazhar Hussain"
        ],
        "Course URL": "https://www.udemy.com/course/deep-learning-with-python-for-image-classification/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4681154_ca33_2.jpg"
    },
    "Data Analytics & Visualization: Using Excel and Python": {
        "Description": "Unlocking Insights through Data: Mastering Analytics and Visualization for In-Demand Tech Proficiency",
        "Is Paid": true,
        "Subscribers": 10235,
        "Average Rating": 4.6578946,
        "Number of Reviews": 95,
        "Number of Lectures": 120,
        "Content Length": "17 total hours",
        "Last Update": "2023-12-27",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Meritshot Academy"
        ],
        "Course URL": "https://www.udemy.com/course/data-analytics-visualization-acquire-demanded-tech-skills/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5081398_e792_5.jpg"
    },
    "Essential Guide to Python Pandas": {
        "Description": "A Python Pandas crash course to teach you all the essentials to get started with data analytics",
        "Is Paid": true,
        "Subscribers": 5357,
        "Average Rating": 4.65,
        "Number of Reviews": 93,
        "Number of Lectures": 17,
        "Content Length": "1.5 total hours",
        "Last Update": "2022-11-26",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Dr. Ali Gazala",
            "Aimei Zhu"
        ],
        "Course URL": "https://www.udemy.com/course/essential-guide-to-python-pandas/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4545714_9f30.jpg"
    },
    "Data Science 4 Newbs! Skills + Basic Web Experiment Analysis": {
        "Description": "Practice basic web experiment analysis hands-on and gain the crucial data science skills of Unix, SQL, and Tableau fast!",
        "Is Paid": true,
        "Subscribers": 2205,
        "Average Rating": 4.4,
        "Number of Reviews": 93,
        "Number of Lectures": 18,
        "Content Length": "1.5 total hours",
        "Last Update": "2016-09-19",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Larry Wai"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-4-newbs/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/746320_c3c5_3.jpg"
    },
    "Neural Networks for Machine Learning From Scratch": {
        "Description": "Develop your own deep learning framework from zero to one. Hands-on Machine Learning with Python.",
        "Is Paid": true,
        "Subscribers": 592,
        "Average Rating": 4.2,
        "Number of Reviews": 93,
        "Number of Lectures": 17,
        "Content Length": "3 total hours",
        "Last Update": "2020-06-24",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Sefik Ilkin Serengil"
        ],
        "Course URL": "https://www.udemy.com/course/neural-networks-fundamentals-in-python/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/1354870_f737_3.jpg"
    },
    "Neural Radiance Fields (NeRF)": {
        "Description": "Introduction to NeRF, volumetric rendering, and 3D reconstruction",
        "Is Paid": true,
        "Subscribers": 565,
        "Average Rating": 4.3235292,
        "Number of Reviews": 92,
        "Number of Lectures": 70,
        "Content Length": "10 total hours",
        "Last Update": "2023-03-28",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Maxime Vandegar"
        ],
        "Course URL": "https://www.udemy.com/course/neural-radiance-fields-nerf/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/5041586_a8c2_3.jpg"
    },
    "Data Visualization with Python and Power BI": {
        "Description": "Learn to create Power BI reports and visual charts with Python Matplotlib and Seaborn. Power bi business intelligence",
        "Is Paid": true,
        "Subscribers": 10894,
        "Average Rating": 3.95,
        "Number of Reviews": 92,
        "Number of Lectures": 21,
        "Content Length": "1.5 total hours",
        "Last Update": "2022-12-03",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Harshit Srivastava"
        ],
        "Course URL": "https://www.udemy.com/course/data-visualization-with-python-and-power-bi/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4247260_0eb0.jpg"
    },
    "Python: Python Basics Bootcamp for Beginners in Data Science": {
        "Description": "A python basics course to kicksart your data science career with python .Learn Python for data science with ease .",
        "Is Paid": true,
        "Subscribers": 10981,
        "Average Rating": 3.85,
        "Number of Reviews": 92,
        "Number of Lectures": 59,
        "Content Length": "3 total hours",
        "Last Update": "2020-09-15",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Shepherd Mahupa"
        ],
        "Course URL": "https://www.udemy.com/course/beginners-python-basics-for-data-science-bootcamp/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/3501070_3d74.jpg"
    },
    "Machine learning with Scikit-learn": {
        "Description": "Learn the most important machine learning techniques using the best machine learning library available",
        "Is Paid": true,
        "Subscribers": 612,
        "Average Rating": 3.95,
        "Number of Reviews": 91,
        "Number of Lectures": 27,
        "Content Length": "6.5 total hours",
        "Last Update": "2017-03-11",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Francisco Juretig"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-with-scikit-learn/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/1019024_956d.jpg"
    },
    "Advanced Reinforcement Learning in Python: from DQN to SAC": {
        "Description": "Build Artificial Intelligence (AI) agents using Deep Reinforcement Learning and PyTorch: DDPG, TD3, SAC, NAF, HER.",
        "Is Paid": true,
        "Subscribers": 1571,
        "Average Rating": 4.6666665,
        "Number of Reviews": 91,
        "Number of Lectures": 116,
        "Content Length": "8 total hours",
        "Last Update": "2024-01-03",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Escape Velocity Labs"
        ],
        "Course URL": "https://www.udemy.com/course/advanced-reinforcement/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4454406_679a_4.jpg"
    },
    "Artificial Intelligence Projects with Python": {
        "Description": "Learn Artificial Intelligence by Building 14 practical Machine Learning and Deep Learning Projects with Python !",
        "Is Paid": true,
        "Subscribers": 7916,
        "Average Rating": 3.7,
        "Number of Reviews": 91,
        "Number of Lectures": 64,
        "Content Length": "6.5 total hours",
        "Last Update": "2023-08-11",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Yaz\u0131l\u0131m Teknolojileri Akademisi"
        ],
        "Course URL": "https://www.udemy.com/course/deep-learning-with-python-course/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4189844_91a4_14.jpg"
    },
    "Data Mining with Rattle": {
        "Description": "Learn to use the GUI-based comprehensive Data Miner data mining software suite implemented as the rattle package in R",
        "Is Paid": true,
        "Subscribers": 1631,
        "Average Rating": 4.4,
        "Number of Reviews": 91,
        "Number of Lectures": 82,
        "Content Length": "15 total hours",
        "Last Update": "2020-08-01",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Geoffrey Hubona, Ph.D."
        ],
        "Course URL": "https://www.udemy.com/course/data-mining-with-rattle/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/590962_b3a4_7.jpg"
    },
    "Data Mining": {
        "Description": "An introductory course about understanding patterns, process, tools of data mining. ",
        "Is Paid": true,
        "Subscribers": 655,
        "Average Rating": 3.85,
        "Number of Reviews": 90,
        "Number of Lectures": 48,
        "Content Length": "2 total hours",
        "Last Update": "2015-03-03",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "The Art Of Service"
        ],
        "Course URL": "https://www.udemy.com/course/data-mining/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/158962_9314_2.jpg"
    },
    "Machine Learning Made Easy : Beginner to Advanced using R": {
        "Description": "Learn Machine Learning Algorithms using R from experts with hands on examples and practice sessions. With 5 different pr",
        "Is Paid": true,
        "Subscribers": 4349,
        "Average Rating": 4.5,
        "Number of Reviews": 90,
        "Number of Lectures": 129,
        "Content Length": "15.5 total hours",
        "Last Update": "2018-04-13",
        "Badges": [],
        "Course Language": "English (India)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Statinfer Solutions"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-made-easy-beginner-to-advance-using-r/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/1322994_9e6c_4.jpg"
    },
    "Data Science-Forecasting/Time series Using XLMiner,R&Tableau": {
        "Description": "Forecasting Techniques-Linear,Exponential,Quadratic Seasonality models, Autoregression, Smooting, Holts, Winters Method",
        "Is Paid": true,
        "Subscribers": 1350,
        "Average Rating": 4.55,
        "Number of Reviews": 90,
        "Number of Lectures": 33,
        "Content Length": "6.5 total hours",
        "Last Update": "2018-03-01",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "ExcelR Solutions"
        ],
        "Course URL": "https://www.udemy.com/course/forecasting-time-series-using-xlminer-r-and-tableau/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/1062344_5aa6.jpg"
    },
    "Python Pandas Data Crash Course 2024 Learn by Doing.": {
        "Description": "Speed up Data Analysis & Visualization with Python Pandas library in easy & simple way also Master using it with SQL.",
        "Is Paid": true,
        "Subscribers": 28453,
        "Average Rating": 3.7333333,
        "Number of Reviews": 90,
        "Number of Lectures": 56,
        "Content Length": "4.5 total hours",
        "Last Update": "2024-02-01",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Temotec Learning Academy"
        ],
        "Course URL": "https://www.udemy.com/course/python-pandas-data-crash-course/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4242880_8446_3.jpg"
    },
    "Datascience:COVID-19 Pneumonia Classification(Deep learning)": {
        "Description": "A Practical Hands-on Data Science Guided Project on Covid-19 Pneumonia Classification through X-rays using Deep Learning",
        "Is Paid": true,
        "Subscribers": 892,
        "Average Rating": 4.1,
        "Number of Reviews": 90,
        "Number of Lectures": 9,
        "Content Length": "1.5 total hours",
        "Last Update": "2021-01-09",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "School of Disruptive Innovation"
        ],
        "Course URL": "https://www.udemy.com/course/datasciencecovid-19-pneumonia-classificationdeep-learning/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/3354932_5725.jpg"
    },
    "Data Science for Sports - Sports Analytics and Visualization": {
        "Description": "Learn how to perform sports analytics and visualization using Python.",
        "Is Paid": true,
        "Subscribers": 7582,
        "Average Rating": 3.15,
        "Number of Reviews": 90,
        "Number of Lectures": 9,
        "Content Length": "1 total hour",
        "Last Update": "2021-02-06",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "The Click Reader"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-for-sports/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/3610614_db4d_6.jpg"
    },
    "The Ultimate Beginners Guide to Fuzzy Logic in Python": {
        "Description": "Understand the basic theory and implement fuzzy systems with skfuzzy library! Step by step implementations",
        "Is Paid": true,
        "Subscribers": 839,
        "Average Rating": 4.1,
        "Number of Reviews": 89,
        "Number of Lectures": 37,
        "Content Length": "4.5 total hours",
        "Last Update": "2023-04-27",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Jones Granatyr",
            "Eduardo Alexandre Franciscon",
            "AI Expert Academy"
        ],
        "Course URL": "https://www.udemy.com/course/the-ultimate-beginners-guide-to-fuzzy-logic-in-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4772284_21c6_2.jpg"
    },
    "Machine Learning from the scratch using Python": {
        "Description": "Machines are now learning, why aren't you?",
        "Is Paid": true,
        "Subscribers": 2393,
        "Average Rating": 3.4,
        "Number of Reviews": 89,
        "Number of Lectures": 35,
        "Content Length": "15 total hours",
        "Last Update": "2020-04-23",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Saheb Singh Chaddha"
        ],
        "Course URL": "https://www.udemy.com/course/machinesarelearning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1966294_942b.jpg"
    },
    "Mastering Probability & Statistic Python (Theory & Projects)": {
        "Description": "Statistic & Probability for Machine Learning & Data Science: Learning Statistics, Probability & Bayes Classifier, Python",
        "Is Paid": true,
        "Subscribers": 1469,
        "Average Rating": 3.85,
        "Number of Reviews": 89,
        "Number of Lectures": 134,
        "Content Length": "14 total hours",
        "Last Update": "2024-02-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "AI Sciences Team",
            "AI Sciences"
        ],
        "Course URL": "https://www.udemy.com/course/mastering-probability-and-statistics-in-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3234447_ddd3_3.jpg"
    },
    "Practical Neural Networks and Deep Learning in Python": {
        "Description": "Your Complete Guide to Implementing PyTorch, Keras, Tensorflow Algorithms: Neural Networks and Deep Learning in Python",
        "Is Paid": true,
        "Subscribers": 830,
        "Average Rating": 4.2,
        "Number of Reviews": 89,
        "Number of Lectures": 85,
        "Content Length": "8.5 total hours",
        "Last Update": "2023-11-15",
        "Badges": [],
        "Course Language": "English (UK)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Minerva Singh"
        ],
        "Course URL": "https://www.udemy.com/course/practical-neural-networks-and-deep-learning-in-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2502044_4115_2.jpg"
    },
    "Scikit-learn in Python: 100+ Data Science Exercises": {
        "Description": "Master Machine Learning - Unleash the Power of Data Science for Predictive Modeling!",
        "Is Paid": true,
        "Subscribers": 39107,
        "Average Rating": 4.8,
        "Number of Reviews": 89,
        "Number of Lectures": 114,
        "Content Length": "1 total hour",
        "Last Update": "2023-10-30",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Pawe\u0142 Krakowiak"
        ],
        "Course URL": "https://www.udemy.com/course/100-exercises-python-data-science-scikit-learn/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3305776_136f_11.jpg"
    },
    "Deep Learning with TensorFlow (beginner to expert level)": {
        "Description": "TensorFlow concepts, components, pipeline, ANN, Classification, Regression, Object Identification, CNN, RNN, TensorBoard",
        "Is Paid": true,
        "Subscribers": 23878,
        "Average Rating": 3.55,
        "Number of Reviews": 88,
        "Number of Lectures": 89,
        "Content Length": "29.5 total hours",
        "Last Update": "2021-05-09",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Uplatz Training"
        ],
        "Course URL": "https://www.udemy.com/course/deep-learning-with-tensorflow-certification-training/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3708676_355e_3.jpg"
    },
    "awk tutorial": {
        "Description": "awk programming examples",
        "Is Paid": true,
        "Subscribers": 10171,
        "Average Rating": 4.55,
        "Number of Reviews": 88,
        "Number of Lectures": 13,
        "Content Length": "32 total mins",
        "Last Update": "2021-08-06",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Frank Anemaet"
        ],
        "Course URL": "https://www.udemy.com/course/awk-tutorial/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4224586_3488.jpg"
    },
    "Chatbot Building with Rasa": {
        "Description": "Rasa NLU, Rasa Core - How to build a Facebook Massenger Chatbot",
        "Is Paid": true,
        "Subscribers": 498,
        "Average Rating": 3.75,
        "Number of Reviews": 88,
        "Number of Lectures": 15,
        "Content Length": "2.5 total hours",
        "Last Update": "2019-05-23",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "GoTrained Academy",
            "Faizan Ali"
        ],
        "Course URL": "https://www.udemy.com/course/chatbot-building-rasa-dialogflow-witai-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1965542_8a50.jpg"
    },
    "No-Code and No-Math Machine Learning": {
        "Description": "Machine learning for everyone! Google Vertex AI, Data Robot AI, Obviously AI, Big ML, Microsoft Azure and Orange!",
        "Is Paid": true,
        "Subscribers": 1015,
        "Average Rating": 4.681818,
        "Number of Reviews": 87,
        "Number of Lectures": 41,
        "Content Length": "5 total hours",
        "Last Update": "2023-04-27",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Jones Granatyr",
            "AI Expert Academy"
        ],
        "Course URL": "https://www.udemy.com/course/no-code-no-math-machine-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4896784_a525_3.jpg"
    },
    "Unsupervised Machine Learning : With 2 Capstone ML Projects": {
        "Description": "Learn Complete Unsupervised ML: Clustering Analysis and Dimensionality Reduction",
        "Is Paid": true,
        "Subscribers": 13735,
        "Average Rating": 4.25,
        "Number of Reviews": 87,
        "Number of Lectures": 50,
        "Content Length": "3 total hours",
        "Last Update": "2022-03-24",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Dataisgood Academy"
        ],
        "Course URL": "https://www.udemy.com/course/unsupervised-machine-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4186170_c1fd.jpg"
    },
    "Data Science Bootcamp with Power Bi and Python": {
        "Description": "learn to create Power bi python charts. Data Visualization, Cleaning and analysis with python Powerbi bootcamp",
        "Is Paid": true,
        "Subscribers": 12207,
        "Average Rating": 4.3,
        "Number of Reviews": 87,
        "Number of Lectures": 28,
        "Content Length": "2 total hours",
        "Last Update": "2022-12-08",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Harshit Srivastava"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-bootcamp-with-power-bi-and-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4263374_6983.jpg"
    },
    "Python Machine learning & Data mining Bootcamp": {
        "Description": "Develop your own Python recommender system using Machine Learning",
        "Is Paid": true,
        "Subscribers": 17517,
        "Average Rating": 3.9,
        "Number of Reviews": 86,
        "Number of Lectures": 19,
        "Content Length": "2.5 total hours",
        "Last Update": "2023-04-07",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Mark Nielsen"
        ],
        "Course URL": "https://www.udemy.com/course/python-data-mining-and-machine-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1724378_6706_4.jpg"
    },
    "Python for Data Science: Learn Data Science From Scratch": {
        "Description": "Data Science with Python, NumPy, Pandas, Matplotlib, Data Visualization Learn with Data Science project & Python project",
        "Is Paid": true,
        "Subscribers": 396,
        "Average Rating": 4.75,
        "Number of Reviews": 86,
        "Number of Lectures": 136,
        "Content Length": "19.5 total hours",
        "Last Update": "2024-02-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Oak Academy",
            "OAK Academy Team"
        ],
        "Course URL": "https://www.udemy.com/course/python-for-data-science-learn-data-science-from-scratch/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3114550_e0d7_9.jpg"
    },
    "NLP-Natural Language Processing in Python(Theory & Projects)": {
        "Description": "Mastering Natural Language Processing with Spacy, NLTK, PyTorch, NLP Techniques, Text Data Analysis, Hands-on Projects",
        "Is Paid": true,
        "Subscribers": 963,
        "Average Rating": 4.3,
        "Number of Reviews": 86,
        "Number of Lectures": 258,
        "Content Length": "23.5 total hours",
        "Last Update": "2024-02-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "AI Sciences",
            "AI Sciences Team"
        ],
        "Course URL": "https://www.udemy.com/course/nlp-natural-language-processing-in-python-for-beginners/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4076522_ddab.jpg"
    },
    "Statistics for Data Analysts and Scientists 2023": {
        "Description": "Ultimate course to master practical and business applications of essential statistical tests and concepts",
        "Is Paid": true,
        "Subscribers": 1118,
        "Average Rating": 4.03125,
        "Number of Reviews": 86,
        "Number of Lectures": 31,
        "Content Length": "2.5 total hours",
        "Last Update": "2023-02-15",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Olanrewaju Oyinbooke"
        ],
        "Course URL": "https://www.udemy.com/course/statistics-for-data-analysts-and-scientists/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5158790_c238_2.jpg"
    },
    "Case Studies in Data Mining with R": {
        "Description": "Learn to use the \"Data Mining with R\" (DMwR) package and R software to build and evaluate predictive data mining models.",
        "Is Paid": true,
        "Subscribers": 2224,
        "Average Rating": 4.25,
        "Number of Reviews": 86,
        "Number of Lectures": 136,
        "Content Length": "22 total hours",
        "Last Update": "2020-08-01",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Geoffrey Hubona, Ph.D."
        ],
        "Course URL": "https://www.udemy.com/course/case-studies-in-data-mining-with-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/589876_e968_2.jpg"
    },
    "Python Data Science basics with Numpy, Pandas and Matplotlib": {
        "Description": "Covers all Essential Python topics and Libraries for Data Science or Machine Learning Beginner.",
        "Is Paid": true,
        "Subscribers": 1816,
        "Average Rating": 4.7,
        "Number of Reviews": 84,
        "Number of Lectures": 63,
        "Content Length": "6.5 total hours",
        "Last Update": "2019-10-16",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Abhilash Nelson"
        ],
        "Course URL": "https://www.udemy.com/course/python-data-science-basics-with-numpy-pandas-and-matplotlib/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/2560188_6899_3.jpg"
    },
    "Mastering Data Modeling Fundamentals in Power BI": {
        "Description": "Learn how to create relationships, calculated columns measures and use DAX formulas in Power BI Data Modeling",
        "Is Paid": true,
        "Subscribers": 2599,
        "Average Rating": 3.4,
        "Number of Reviews": 85,
        "Number of Lectures": 6,
        "Content Length": "41 total mins",
        "Last Update": "2021-08-11",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Ameen Khan",
            "Ameen Khan"
        ],
        "Course URL": "https://www.udemy.com/course/data-modeling-power-bi/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4237120_434e_2.jpg"
    },
    "Machine Learning with Jupyter Notebooks in Amazon AWS": {
        "Description": "A comprehensive look into Machine Learning using Dynamic Programming, Python and SageMaker service offered by Amazon AWS",
        "Is Paid": true,
        "Subscribers": 13054,
        "Average Rating": 4.3,
        "Number of Reviews": 85,
        "Number of Lectures": 46,
        "Content Length": "5.5 total hours",
        "Last Update": "2021-11-13",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Qasim Shah",
            "Syed Raza"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-with-jupyter-notebooks-in-amazon-aws/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/2195232_7a98_4.jpg"
    },
    "Statistics Fundamentals": {
        "Description": "Theory and Python",
        "Is Paid": true,
        "Subscribers": 12055,
        "Average Rating": 4.2,
        "Number of Reviews": 84,
        "Number of Lectures": 213,
        "Content Length": "14.5 total hours",
        "Last Update": "2021-12-22",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Takuma Kimura"
        ],
        "Course URL": "https://www.udemy.com/course/statistics-fundamentals-bundled/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/3969820_71af_2.jpg"
    },
    "The Big Data Developer Course": {
        "Description": "Master the most in-demand big data skills: Hadoop, Sqoop, Hive, Spark, Scala, Cassandra, HBase, NIFI, Kafka and more",
        "Is Paid": true,
        "Subscribers": 688,
        "Average Rating": 4.071429,
        "Number of Reviews": 84,
        "Number of Lectures": 197,
        "Content Length": "33.5 total hours",
        "Last Update": "2023-09-22",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Deesa Technologies"
        ],
        "Course URL": "https://www.udemy.com/course/the-big-data-developer-course/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4870802_1653_4.jpg"
    },
    "Math for Machine Learning": {
        "Description": "Learn the core topics of Machine Learning to open doors to data science and artificial intelligence.",
        "Is Paid": true,
        "Subscribers": 1098,
        "Average Rating": 3.85,
        "Number of Reviews": 84,
        "Number of Lectures": 81,
        "Content Length": "5 total hours",
        "Last Update": "2020-08-25",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Richard Han"
        ],
        "Course URL": "https://www.udemy.com/course/mathematics-for-machine-learning/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/1205086_3a72_2.jpg"
    },
    "Text Mining with Machine Learning and Python": {
        "Description": "Get high-quality information from your text using Machine Learning with Tensorflow, NLTK, Scikit-Learn, and Python",
        "Is Paid": true,
        "Subscribers": 448,
        "Average Rating": 3.8,
        "Number of Reviews": 84,
        "Number of Lectures": 31,
        "Content Length": "2.5 total hours",
        "Last Update": "2018-05-25",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Packt Publishing"
        ],
        "Course URL": "https://www.udemy.com/course/text-mining-with-machine-learning-and-python/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/1695082_80c9_2.jpg"
    },
    "ChatGPT for Everyone": {
        "Description": "Unleash Your AI Creativity with ChatGPT and Generative AI: A Beginner's Guide by a 15-Year Microsoft Veteran",
        "Is Paid": true,
        "Subscribers": 1305,
        "Average Rating": 4.15,
        "Number of Reviews": 84,
        "Number of Lectures": 9,
        "Content Length": "32 total mins",
        "Last Update": "2023-05-04",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Tatjana Nijemcevic"
        ],
        "Course URL": "https://www.udemy.com/course/course-title-chatgpt-for-everyone/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/5262164_a85f.jpg"
    },
    "Math 0-1: Linear Algebra for Data Science & Machine Learning": {
        "Description": "A Casual Guide for Artificial Intelligence, Deep Learning, and Python Programmers",
        "Is Paid": true,
        "Subscribers": 1029,
        "Average Rating": 4.9375,
        "Number of Reviews": 84,
        "Number of Lectures": 97,
        "Content Length": "19.5 total hours",
        "Last Update": "2024-02-02",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Lazy Programmer Team",
            "Lazy Programmer Inc."
        ],
        "Course URL": "https://www.udemy.com/course/linear-algebra-data-science/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/5118092_26c8_2.jpg"
    },
    "Master Reinforcement Learning and Deep RL with Python": {
        "Description": "Reinforcement Learning Mastery: Deep Q-Learning, SARSA, and Real-World Applications with Car Racing, Trading Projects",
        "Is Paid": true,
        "Subscribers": 527,
        "Average Rating": 3.95,
        "Number of Reviews": 84,
        "Number of Lectures": 165,
        "Content Length": "14.5 total hours",
        "Last Update": "2024-02-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "AI Sciences",
            "AI Sciences Team"
        ],
        "Course URL": "https://www.udemy.com/course/reinforcement-learning-deep-rl-pythontheory-projects/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4304679_e0fd_3.jpg"
    },
    "Decision Trees for Machine Learning From Scratch": {
        "Description": "Learn to build decision trees for applied machine learning from scratch in Python.",
        "Is Paid": true,
        "Subscribers": 392,
        "Average Rating": 4.3,
        "Number of Reviews": 84,
        "Number of Lectures": 21,
        "Content Length": "3 total hours",
        "Last Update": "2020-05-12",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Sefik Ilkin Serengil"
        ],
        "Course URL": "https://www.udemy.com/course/decision-trees-for-machine-learning/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/1915334_18bc_3.jpg"
    },
    "Data Science Hands On (PowerBI, SQL, Tableau, Spark, Python)": {
        "Description": "Delve Into Hands-On Data Science: Build 5 Unique Projects Using Python, SQL, Spark, PowerBI, & Tableau.",
        "Is Paid": true,
        "Subscribers": 2241,
        "Average Rating": 4.2727275,
        "Number of Reviews": 83,
        "Number of Lectures": 30,
        "Content Length": "8 total hours",
        "Last Update": "2023-05-31",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Ben Sullins",
            "Lahcen Bouya"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-hands-on/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/5351094_c3d8_2.jpg"
    },
    "Introduction to the Latest Artificial Intelligence Tools": {
        "Description": "Get More Done with Less Effort in Less Time...with A.I. Tools that Will Revolutionize Your Life & Business",
        "Is Paid": true,
        "Subscribers": 473,
        "Average Rating": 4.8,
        "Number of Reviews": 83,
        "Number of Lectures": 42,
        "Content Length": "3.5 total hours",
        "Last Update": "2024-02-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Bryan Guerra"
        ],
        "Course URL": "https://www.udemy.com/course/introduction-to-the-latest-artificial-intelligence-tools/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/5203178_8f72.jpg"
    },
    "Introductory statistics Part1: Descriptive Statistics ": {
        "Description": "Learn the concepts, calculations and applications of statistics at your own pace and comfort.",
        "Is Paid": true,
        "Subscribers": 935,
        "Average Rating": 4.35,
        "Number of Reviews": 83,
        "Number of Lectures": 29,
        "Content Length": "4.5 total hours",
        "Last Update": "2016-09-11",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Luc Zio"
        ],
        "Course URL": "https://www.udemy.com/course/introductory-statistics-part1-descriptive-statistics/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/90352_f733_7.jpg"
    },
    "Intro to Natural Language Processing in Python for AI": {
        "Description": "Learn the Technology Behind AI Tools Like ChatGPT: Understanding, Generating, and Classifying Human Language",
        "Is Paid": true,
        "Subscribers": 376,
        "Average Rating": 4.5,
        "Number of Reviews": 82,
        "Number of Lectures": 47,
        "Content Length": "3 total hours",
        "Last Update": "2023-10-11",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "365 Careers",
            "Lauren Newbould"
        ],
        "Course URL": "https://www.udemy.com/course/intro-to-natural-language-processing-in-python-for-ai/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/5533500_df21_3.jpg"
    },
    "Statistics & Probability for Data Science & Machine Learning": {
        "Description": "Know each & every concept - Descriptive, Inferential Statistics & Probability become expert in Stats for Data Science",
        "Is Paid": true,
        "Subscribers": 433,
        "Average Rating": 4.15,
        "Number of Reviews": 82,
        "Number of Lectures": 43,
        "Content Length": "29 total hours",
        "Last Update": "2021-11-22",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Rahul Tiwari"
        ],
        "Course URL": "https://www.udemy.com/course/statistics-probability-for-data-science-machine-learning/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/3279738_885a_3.jpg"
    },
    "100 Days Of Code: Real World Data Science Projects Bootcamp": {
        "Description": "Build 100 Projects in 100 Days- Data Science, Machine Learning, Deep Learning (Python, Flask, Django, AWS, Heruko Cloud)",
        "Is Paid": true,
        "Subscribers": 2698,
        "Average Rating": 4.0,
        "Number of Reviews": 82,
        "Number of Lectures": 731,
        "Content Length": "105.5 total hours",
        "Last Update": "2022-11-20",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Pianalytix ."
        ],
        "Course URL": "https://www.udemy.com/course/hands-on-data-science-build-real-world-projects/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4889834_9385_2.jpg"
    },
    "Learn Artificial Intelligence Fundamentals": {
        "Description": "Join the new smart club | Understand the fundamentals | Learn about the Industry Situation and Opportunities",
        "Is Paid": true,
        "Subscribers": 3441,
        "Average Rating": 3.8,
        "Number of Reviews": 81,
        "Number of Lectures": 22,
        "Content Length": "1 total hour",
        "Last Update": "2018-10-30",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Mahadi Hasan Meem"
        ],
        "Course URL": "https://www.udemy.com/course/learnartificialintelligence/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1809418_fb6b_2.jpg"
    },
    "Master Power BI: 30 Hands-On Projects for Data Visualization": {
        "Description": "From Data Preprocessing to Advanced Business Intelligence, Analytics\u2014Become an In-Demand Microsoft Power BI Expert!",
        "Is Paid": true,
        "Subscribers": 1314,
        "Average Rating": 4.0961537,
        "Number of Reviews": 80,
        "Number of Lectures": 139,
        "Content Length": "19.5 total hours",
        "Last Update": "2023-12-26",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Pianalytix ."
        ],
        "Course URL": "https://www.udemy.com/course/data-analysis-power-bi-projects/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5510804_53be_3.jpg"
    },
    "Python Data Science with Pandas: Over 130 Exercises": {
        "Description": "Dive into Data Manipulation and Analysis with Pandas Exercises in Python - Master the Essential Skills for Data Science!",
        "Is Paid": true,
        "Subscribers": 20202,
        "Average Rating": 4.4,
        "Number of Reviews": 81,
        "Number of Lectures": 146,
        "Content Length": "1 total hour",
        "Last Update": "2023-10-30",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Pawe\u0142 Krakowiak"
        ],
        "Course URL": "https://www.udemy.com/course/100-exercises-python-programming-data-science-pandas/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3294280_f013_5.jpg"
    },
    "Data Visualization with Python Masterclass | Python A-Z": {
        "Description": "Python Data visualization: Python data analysis and visualization, Machine Learning, Deep Learning, Pandas, Matplotlib",
        "Is Paid": true,
        "Subscribers": 2776,
        "Average Rating": 4.6,
        "Number of Reviews": 81,
        "Number of Lectures": 144,
        "Content Length": "20.5 total hours",
        "Last Update": "2024-02-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Oak Academy",
            "OAK Academy Team",
            "Ali\u0307 CAVDAR"
        ],
        "Course URL": "https://www.udemy.com/course/data-visualization-with-python-masterclass-python-a-z/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4066954_1852_5.jpg"
    },
    "Deep Learning Application for Earth Observation": {
        "Description": "Satellite Image processing using Deep Learning Neural Network",
        "Is Paid": true,
        "Subscribers": 384,
        "Average Rating": 4.5,
        "Number of Reviews": 81,
        "Number of Lectures": 65,
        "Content Length": "10 total hours",
        "Last Update": "2024-01-13",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Tek Kshetri"
        ],
        "Course URL": "https://www.udemy.com/course/deep-learning-application-for-earth-observation/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4868294_1afc.jpg"
    },
    "Machine Learning with Remote Sensing in Google Earth Engine": {
        "Description": "Learn to apply machine learning, remote sensing, big spatial data using the Google Earth Engine cloud computing",
        "Is Paid": true,
        "Subscribers": 384,
        "Average Rating": 3.6,
        "Number of Reviews": 80,
        "Number of Lectures": 14,
        "Content Length": "1.5 total hours",
        "Last Update": "2024-02-10",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Spatial eLearning",
            "Dr. Alemayehu Midekisa"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-and-earth-observation-big-data/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1936792_bdde_9.jpg"
    },
    "Artificial Intelligence Bootcamp 44 projects Ivy League pro": {
        "Description": "Be a Machine Learning, Matplotlib, NumPy, and TensorFlow pro.  Use AI for programming, business or science!",
        "Is Paid": true,
        "Subscribers": 13556,
        "Average Rating": 3.8,
        "Number of Reviews": 80,
        "Number of Lectures": 74,
        "Content Length": "13.5 total hours",
        "Last Update": "2018-06-15",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "GP Shangari"
        ],
        "Course URL": "https://www.udemy.com/course/artificial/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1750258_e459_3.jpg"
    },
    "Generative AI Unleashed: Exploring Possibilities and Future": {
        "Description": "Understanding the Power and Impact of artificial Intelligence in Generating Content",
        "Is Paid": true,
        "Subscribers": 13038,
        "Average Rating": 4.4310346,
        "Number of Reviews": 80,
        "Number of Lectures": 19,
        "Content Length": "1 total hour",
        "Last Update": "2023-06-16",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Learnsector LLP"
        ],
        "Course URL": "https://www.udemy.com/course/generative-ai-techniques-applications-and-ethics/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5366894_9d33_2.jpg"
    },
    "Master AWS with Python and Boto3": {
        "Description": "Learn to use Python to connect to AWS and launch services with Boto3, such as S3, EC2, DynamoDB, and more!",
        "Is Paid": true,
        "Subscribers": 1400,
        "Average Rating": 4.627907,
        "Number of Reviews": 79,
        "Number of Lectures": 36,
        "Content Length": "6 total hours",
        "Last Update": "2023-09-20",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Jose Portilla"
        ],
        "Course URL": "https://www.udemy.com/course/master-aws-with-python-and-boto3/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5559012_d09f.jpg"
    },
    "Artificial Intelligence:Deep Learning in Real World Business": {
        "Description": "Learn how to deploy deep learning business applications for real world purposes.",
        "Is Paid": true,
        "Subscribers": 567,
        "Average Rating": 3.7,
        "Number of Reviews": 79,
        "Number of Lectures": 26,
        "Content Length": "3.5 total hours",
        "Last Update": "2023-04-08",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Eduero Academy, Inc."
        ],
        "Course URL": "https://www.udemy.com/course/deep-learning-for-real-world-business/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1314996_bdb7.jpg"
    },
    "NumPy, Pandas and Matplotlib A-Z\u2122 for Machine Learning 2023": {
        "Description": "Python NumPy, Pandas, and Matplotlib for Data Analysis, Data Science and Machine Learning. Pre-machine learning Analysis",
        "Is Paid": true,
        "Subscribers": 518,
        "Average Rating": 3.35,
        "Number of Reviews": 79,
        "Number of Lectures": 447,
        "Content Length": "11.5 total hours",
        "Last Update": "2023-11-16",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Donatus Obomighie, PhD, MSc, PMP"
        ],
        "Course URL": "https://www.udemy.com/course/numpy-for-data-science-deep-machine-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4074236_e1cc_16.jpg"
    },
    "Face Mask Recognition: Deep Learning based Desktop App": {
        "Description": "Learn and Build Face Recognition for Face Mask Detection Desktop App using Python, TensorFlow 2, OpenCV, PyQT, Qt",
        "Is Paid": true,
        "Subscribers": 2459,
        "Average Rating": 4.6,
        "Number of Reviews": 79,
        "Number of Lectures": 68,
        "Content Length": "4.5 total hours",
        "Last Update": "2022-06-08",
        "Badges": [],
        "Course Language": "English (India)",
        "Instructional Level": "All Levels",
        "Authors": [
            "G Sudheer",
            "Data Science Anywhere",
            "Brightshine Learn"
        ],
        "Course URL": "https://www.udemy.com/course/computer-vision-face-mask-detection-with-deep-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4155042_3203_20.jpg"
    },
    "Machine Learning and Deep Learning A-Z: Hands-On Python": {
        "Description": "Python Machine Learning and Python Deep Algorithms in Python Code templates included. Python in Data Science | 2021",
        "Is Paid": true,
        "Subscribers": 2794,
        "Average Rating": 4.5,
        "Number of Reviews": 78,
        "Number of Lectures": 116,
        "Content Length": "18 total hours",
        "Last Update": "2024-02-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Oak Academy",
            "OAK Academy Team",
            "Ali\u0307 CAVDAR"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-and-deep-learning-a-z-hands-on-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4141792_2df3_4.jpg"
    },
    "Pomodoro Technique for Effective Developers and Programmers": {
        "Description": "Master the Pomodoro Technique to Boost Your Productivity and Efficiency as a Programmer or Software Developer",
        "Is Paid": true,
        "Subscribers": 11019,
        "Average Rating": 4.3235292,
        "Number of Reviews": 77,
        "Number of Lectures": 14,
        "Content Length": "1 total hour",
        "Last Update": "2023-05-08",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Prince Patni"
        ],
        "Course URL": "https://www.udemy.com/course/pomodoro-technique-for-effective-developers-and-programmers/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5315110_8381_2.jpg"
    },
    "Data Science with R": {
        "Description": "Statistical analysis with R",
        "Is Paid": true,
        "Subscribers": 7,
        "Average Rating": 1.75,
        "Number of Reviews": 2,
        "Number of Lectures": 16,
        "Content Length": "1 total hour",
        "Last Update": "2022-04-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "E-Lephant Group"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-with-r-le/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4549524_0630_3.jpg"
    },
    "A Beginner's Guide to Machine Learning (in Python)": {
        "Description": "Learn supervised learning for structured data, and implement them using Python programming",
        "Is Paid": true,
        "Subscribers": 1191,
        "Average Rating": 3.55,
        "Number of Reviews": 77,
        "Number of Lectures": 49,
        "Content Length": "3.5 total hours",
        "Last Update": "2020-08-08",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Curiosity for Data Science"
        ],
        "Course URL": "https://www.udemy.com/course/a-beginners-guide-to-data-mining/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1567490_54fb_3.jpg"
    },
    "Natural Language Processing Bootcamp in Python": {
        "Description": "Learn the fundamentals of Text Mining and NLP using Text Processing, NLTK, Sentiment Analysis and Neural Networks",
        "Is Paid": true,
        "Subscribers": 764,
        "Average Rating": 4.6666665,
        "Number of Reviews": 77,
        "Number of Lectures": 125,
        "Content Length": "18 total hours",
        "Last Update": "2023-12-31",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Ivo Bernardo"
        ],
        "Course URL": "https://www.udemy.com/course/nlp_natural_language_processing_python_beginners/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3856988_63ee_5.jpg"
    },
    "Universal Deep Learning Mastery - 2024 Edition with Updated": {
        "Description": "Transform into a Deep Learning Expert: Build Intuition from Single Neuron to Deep Neural Networks using Keras &amp; TensorFl",
        "Is Paid": true,
        "Subscribers": 579,
        "Average Rating": 4.7352943,
        "Number of Reviews": 77,
        "Number of Lectures": 104,
        "Content Length": "12 total hours",
        "Last Update": "2024-01-09",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Manifold AI Learning \u00ae"
        ],
        "Course URL": "https://www.udemy.com/course/deep-learning-101/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2345898_c175_5.jpg"
    },
    "LookML A-Z: Google Looker for Developers": {
        "Description": "Learn LookML, Google Looker's modeling language, to get complete control of the visualization process | LookML mastery",
        "Is Paid": true,
        "Subscribers": 15067,
        "Average Rating": 4.285714,
        "Number of Reviews": 77,
        "Number of Lectures": 51,
        "Content Length": "4 total hours",
        "Last Update": "2024-01-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Start-Tech Academy"
        ],
        "Course URL": "https://www.udemy.com/course/lookml-google-looker-for-developers/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4704782_2744_4.jpg"
    },
    "Looker for Beginners": {
        "Description": "Learn everything you need to get started with Looker in less than an hour!",
        "Is Paid": true,
        "Subscribers": 249,
        "Average Rating": 4.7,
        "Number of Reviews": 76,
        "Number of Lectures": 26,
        "Content Length": "1 total hour",
        "Last Update": "2021-10-06",
        "Badges": [
            "Highest Rated"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Colin Matthews"
        ],
        "Course URL": "https://www.udemy.com/course/looker-for-beginners/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4293926_6c24.jpg"
    },
    "Tensorflow for Beginners": {
        "Description": "A complete guide for building machine learning and deep learning solutions using Tensorflow",
        "Is Paid": true,
        "Subscribers": 620,
        "Average Rating": 4.0,
        "Number of Reviews": 76,
        "Number of Lectures": 20,
        "Content Length": "4 total hours",
        "Last Update": "2018-12-03",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Eduonix Learning Solutions",
            "Eduonix-Tech ."
        ],
        "Course URL": "https://www.udemy.com/course/tensorflow-for-beginners/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1583732_85fe.jpg"
    },
    "Artificial Neural Networks(ANN) Made Easy": {
        "Description": "Learn ANN Model Building and Fine-tuning ANN\u00a0hyper-parameters on Python and TensorFlow",
        "Is Paid": true,
        "Subscribers": 6973,
        "Average Rating": 3.9,
        "Number of Reviews": 76,
        "Number of Lectures": 66,
        "Content Length": "5.5 total hours",
        "Last Update": "2019-02-28",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Statinfer Solutions"
        ],
        "Course URL": "https://www.udemy.com/course/artificial-neural-networks-made-easy/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2234110_b09f.jpg"
    },
    "Imbalanced Learning (Unbalanced Data) - The Complete Guide": {
        "Description": "Learn how to handle imbalanced data in Machine Learning. Data based approaches, algorithmic approaches and more!",
        "Is Paid": true,
        "Subscribers": 836,
        "Average Rating": 4.55,
        "Number of Reviews": 76,
        "Number of Lectures": 61,
        "Content Length": "5 total hours",
        "Last Update": "2019-11-25",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Bassam Almogahed"
        ],
        "Course URL": "https://www.udemy.com/course/imbalanced-learning-the-complete-guide/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1681954_b6e4_3.jpg"
    },
    "YOLOv4 Object Detection Course": {
        "Description": "How to Implement & Train YOLOv4 for Object Detection",
        "Is Paid": true,
        "Subscribers": 4396,
        "Average Rating": 4.4,
        "Number of Reviews": 76,
        "Number of Lectures": 57,
        "Content Length": "5.5 total hours",
        "Last Update": "2021-12-21",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Augmented Startups",
            "Geeky Bee AI Private Limited"
        ],
        "Course URL": "https://www.udemy.com/course/yolov4-object-detection-nano-course/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3247268_b3a1_4.jpg"
    },
    "OpenAI | Dall E | Chat GPT | Make Flutter Siri & Alexa Clone": {
        "Description": "Learn Flutter & Open AI ChatGPT & DaleE | Build iOS & Android AI Draw Images and Intelligent Virtual Assistant App",
        "Is Paid": true,
        "Subscribers": 636,
        "Average Rating": 4.65,
        "Number of Reviews": 75,
        "Number of Lectures": 33,
        "Content Length": "3.5 total hours",
        "Last Update": "2023-11-01",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Coding Cafe"
        ],
        "Course URL": "https://www.udemy.com/course/openai-dall-e-chat-gpt-make-flutter-siri-alexa-clone/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5121002_c17e.jpg"
    },
    "Machine Learning Model Deployment with Streamlit": {
        "Description": "Deploy ML models with Streamlit and share your data science work with the world",
        "Is Paid": true,
        "Subscribers": 684,
        "Average Rating": 4.7605634,
        "Number of Reviews": 75,
        "Number of Lectures": 44,
        "Content Length": "7 total hours",
        "Last Update": "2023-09-22",
        "Badges": [
            "Highest Rated"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Marco Peixeiro"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-model-deployment-with-streamlit/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5326624_fdd2_2.jpg"
    },
    "Python Numpy: Machine Learning & Data Science Course": {
        "Description": "Learn Numpy Python and get comfortable with Python Numpy in order to start into Data Science and Machine Learning.",
        "Is Paid": true,
        "Subscribers": 7482,
        "Average Rating": 4.6,
        "Number of Reviews": 75,
        "Number of Lectures": 66,
        "Content Length": "9 total hours",
        "Last Update": "2024-02-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Oak Academy",
            "OAK Academy Team"
        ],
        "Course URL": "https://www.udemy.com/course/python-numpy-machine-learning-data-science-course/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3525856_763b_6.jpg"
    },
    "Machine Learning and Data Science with AWS- Hands On": {
        "Description": "Learn data science and machine learning services using AWS Athena, Glue, Quicksight, AWS Comprehend and Python Boto3",
        "Is Paid": true,
        "Subscribers": 6245,
        "Average Rating": 3.6,
        "Number of Reviews": 75,
        "Number of Lectures": 36,
        "Content Length": "3 total hours",
        "Last Update": "2022-11-22",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Pranjal Srivastava",
            "Harshit Srivastava"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-and-data-science-with-aws/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4451048_bbbf.jpg"
    },
    "Azure Data Engineer Workshop In A Weekend": {
        "Description": "Get a quick jumpstart in your journey of Azure Data Engineer.Create ETL pipelines using Data Factory, Data Lake & SQL DB",
        "Is Paid": true,
        "Subscribers": 965,
        "Average Rating": 4.6,
        "Number of Reviews": 75,
        "Number of Lectures": 31,
        "Content Length": "9.5 total hours",
        "Last Update": "2022-12-21",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Amit Navgire"
        ],
        "Course URL": "https://www.udemy.com/course/azuredata/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4640946_f320.jpg"
    },
    "Complete ArcGIS Pro Mastery: A Hands-On, Practical Course": {
        "Description": "Mastering ArcGIS Pro: A Hands-On Journey Through Practical Applications",
        "Is Paid": true,
        "Subscribers": 397,
        "Average Rating": 4.3977275,
        "Number of Reviews": 75,
        "Number of Lectures": 49,
        "Content Length": "8 total hours",
        "Last Update": "2024-01-18",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Shoaib Shahzad Obaidi"
        ],
        "Course URL": "https://www.udemy.com/course/complete-arcgis-pro-mastery-a-hands-on-practical-course/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5459866_581e_2.jpg"
    },
    "LaTeX for everyone 2021": {
        "Description": "LaTeX for everyone!",
        "Is Paid": true,
        "Subscribers": 561,
        "Average Rating": 4.05,
        "Number of Reviews": 75,
        "Number of Lectures": 23,
        "Content Length": "2 total hours",
        "Last Update": "2021-07-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "David Armend\u00e1riz"
        ],
        "Course URL": "https://www.udemy.com/course/latex-for-data-scientists-2020-and-for-non-data-scientists/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2719230_afbf.jpg"
    },
    "Data Science: Machine Learning and Deep Learning with Python": {
        "Description": "Learn Data Science with Data Parsing, Data Visualization, Data Processing, Supervised & Unsupervised Machine Learning",
        "Is Paid": true,
        "Subscribers": 3276,
        "Average Rating": 4.3,
        "Number of Reviews": 75,
        "Number of Lectures": 60,
        "Content Length": "14.5 total hours",
        "Last Update": "2019-09-12",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Teach Premium",
            "Teach Apex"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-machine-learning-and-deep-learning-with-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2552305_a5f0.jpg"
    },
    "The Complete GANs Bootcamp: Theory and Applications": {
        "Description": "Master Generative Adversarial Networks (GANs) in no time",
        "Is Paid": true,
        "Subscribers": 595,
        "Average Rating": 4.3,
        "Number of Reviews": 75,
        "Number of Lectures": 20,
        "Content Length": "3 total hours",
        "Last Update": "2020-12-22",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Mahmoud Elsayed"
        ],
        "Course URL": "https://www.udemy.com/course/gans_bootcamp/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/2951978_0c03_4.jpg"
    },
    "Machine Learning and Deep Learning Projects in Python": {
        "Description": "20 practical projects of Machine Learning and Deep Learning and their implementation in Python along with all the codes",
        "Is Paid": true,
        "Subscribers": 14184,
        "Average Rating": 4.240741,
        "Number of Reviews": 74,
        "Number of Lectures": 60,
        "Content Length": "5.5 total hours",
        "Last Update": "2023-11-04",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "S. Emadedin Hashemi"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-and-deep-learning-projects-in-python/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/5424444_410a_2.jpg"
    },
    "R for Data Analysis, Statistics and Data Science": {
        "Description": "Data Analysis & Data Science using R : Descriptive & Inferential Statistics, Data Visualization, Hypothesis Testing",
        "Is Paid": true,
        "Subscribers": 2444,
        "Average Rating": 3.65,
        "Number of Reviews": 74,
        "Number of Lectures": 79,
        "Content Length": "8 total hours",
        "Last Update": "2020-04-30",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Syed Mohiuddin"
        ],
        "Course URL": "https://www.udemy.com/course/statistical-data-analysis-using-r/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/2668492_9e16.jpg"
    },
    "Complete Data Science & Machine Learning Bootcamp in Python": {
        "Description": "Learn Python,NumPy,Pandas,Matplotlib,Seaborn,Scikit-learn,Dask,LightGBM,XGBoost,CatBoost,Streamlit,Power BI & much more",
        "Is Paid": true,
        "Subscribers": 860,
        "Average Rating": 4.5,
        "Number of Reviews": 74,
        "Number of Lectures": 365,
        "Content Length": "18 total hours",
        "Last Update": "2022-10-20",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Derrick Mwiti",
            "Namespace Labs"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-bootcamp-in-python/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/3240770_e715_4.jpg"
    },
    "Data Forensics Class": {
        "Description": "Data Collections",
        "Is Paid": true,
        "Subscribers": 1215,
        "Average Rating": 4.375,
        "Number of Reviews": 74,
        "Number of Lectures": 11,
        "Content Length": "1.5 total hours",
        "Last Update": "2022-05-17",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Robert Fried"
        ],
        "Course URL": "https://www.udemy.com/course/dataforensicsclass/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4678144_972d_2.jpg"
    },
    "Machine Learning for Interviews & Research and DL basics": {
        "Description": "Machine Learning, Linear Regression, PCA, Neural Networks, Hyperparameters, Deep Learning, Keras, Clustering, Case Study",
        "Is Paid": true,
        "Subscribers": 681,
        "Average Rating": 4.55,
        "Number of Reviews": 74,
        "Number of Lectures": 38,
        "Content Length": "4.5 total hours",
        "Last Update": "2023-12-12",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Learn with Amine"
        ],
        "Course URL": "https://www.udemy.com/course/ml-dl-interviews/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4536082_0709_4.jpg"
    },
    "Computer Vision - Object Detection on Videos - Deep Learning": {
        "Description": "Quick Starter on Object Detection and Image Classification on Videos using Deep Learning, OpenCV, YOLO and CNN Models",
        "Is Paid": true,
        "Subscribers": 408,
        "Average Rating": 4.4,
        "Number of Reviews": 73,
        "Number of Lectures": 82,
        "Content Length": "2.5 total hours",
        "Last Update": "2022-12-03",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Vineeta Vashistha"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-on-videos-using-python/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/3053348_c0e0_4.jpg"
    },
    "Deep learning: An Image Classification Bootcamp": {
        "Description": "Use Tensorflow to Create Image Classification models for Deep Learning applications. Beginners Level Course",
        "Is Paid": true,
        "Subscribers": 3186,
        "Average Rating": 3.9,
        "Number of Reviews": 73,
        "Number of Lectures": 15,
        "Content Length": "36 total mins",
        "Last Update": "2021-09-11",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Aditya Shankarnarayan"
        ],
        "Course URL": "https://www.udemy.com/course/deep-learning-an-image-classification-bootcamp/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/3608058_0c43_2.jpg"
    },
    "PyTorch: Deep Learning with PyTorch - Masterclass!: 2-in-1": {
        "Description": "Start your journey with PyTorch to build useful & effective models with the PyTorch Deep Learning framework from scratch",
        "Is Paid": true,
        "Subscribers": 586,
        "Average Rating": 4.1,
        "Number of Reviews": 73,
        "Number of Lectures": 65,
        "Content Length": "7.5 total hours",
        "Last Update": "2018-10-22",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Packt Publishing"
        ],
        "Course URL": "https://www.udemy.com/course/pytorch-deep-learning-with-pytorch-masterclass-2-in-1/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/1959818_ec9e_3.jpg"
    },
    "Optimization Using Genetic Algorithms : MATLAB Programming": {
        "Description": "A Quick Way to Learn and Solve Optimization Problems in MATLAB. A Course for Beginners.",
        "Is Paid": true,
        "Subscribers": 7729,
        "Average Rating": 4.15,
        "Number of Reviews": 73,
        "Number of Lectures": 23,
        "Content Length": "1 total hour",
        "Last Update": "2022-07-26",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Karthik K"
        ],
        "Course URL": "https://www.udemy.com/course/genetic-algorithm/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/2983342_b00e.jpg"
    },
    "Complete Python Machine Learning & Data Science for Dummies": {
        "Description": "Machine Learning and Data Science for programming beginners using python with  scikit-learn, SciPy, Matplotlib & Pandas",
        "Is Paid": true,
        "Subscribers": 2346,
        "Average Rating": 4.15,
        "Number of Reviews": 73,
        "Number of Lectures": 90,
        "Content Length": "10.5 total hours",
        "Last Update": "2021-07-16",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Abhilash Nelson"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-with-python-for-dummies-the-complete-guide/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/2138304_f3b0_2.jpg"
    },
    "Predictive Analytics With R": {
        "Description": "Enhance you analytics by Predictive Analytcis with R. Become an Analyst with easy programming code of R.",
        "Is Paid": true,
        "Subscribers": 331,
        "Average Rating": 4.15,
        "Number of Reviews": 72,
        "Number of Lectures": 44,
        "Content Length": "4.5 total hours",
        "Last Update": "2016-02-09",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Easylearning guru"
        ],
        "Course URL": "https://www.udemy.com/course/predictive-analytics-with-r/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/698836_ae4a.jpg"
    },
    "Data Science with R Tidyverse": {
        "Description": "Take your R programming skills to the next level with the core tidyverse packages of dplyr, tidyr, ggplot2 and magrittr",
        "Is Paid": true,
        "Subscribers": 258,
        "Average Rating": 4.45,
        "Number of Reviews": 72,
        "Number of Lectures": 26,
        "Content Length": "3.5 total hours",
        "Last Update": "2023-09-12",
        "Badges": [],
        "Course Language": "English (UK)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Adam Hayward"
        ],
        "Course URL": "https://www.udemy.com/course/efficient-r-programming-with-the-tidyverse/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/3207443_c86f_5.jpg"
    },
    "Machine Learning with Python: Data Science for Beginners": {
        "Description": "Data Science / Machine Learning is the most in-demand and Highest Paying job of 2017",
        "Is Paid": true,
        "Subscribers": 3293,
        "Average Rating": 3.4,
        "Number of Reviews": 71,
        "Number of Lectures": 67,
        "Content Length": "11 total hours",
        "Last Update": "2017-11-04",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "TELCOMA Global"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-with-python-data-science-for-beginners/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1413802_de90.jpg"
    },
    "Data Science Methodology in Action using Dataiku": {
        "Description": "Gain hands-on experience in building a Data Driven AI engagement using Dataiku",
        "Is Paid": true,
        "Subscribers": 311,
        "Average Rating": 4.15,
        "Number of Reviews": 70,
        "Number of Lectures": 38,
        "Content Length": "4 total hours",
        "Last Update": "2022-11-15",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Neena Sathi"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-methodology-in-action-using-dataiku/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4873466_5eca.jpg"
    },
    "Mastering Microsoft Power BI: From Beginner to Advanced": {
        "Description": "Unlocking the Secrets of Data Visualization and Transforming Insights into Action",
        "Is Paid": true,
        "Subscribers": 2070,
        "Average Rating": 4.521739,
        "Number of Reviews": 70,
        "Number of Lectures": 55,
        "Content Length": "9 total hours",
        "Last Update": "2023-11-21",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Sunil Kumar Gupta"
        ],
        "Course URL": "https://www.udemy.com/course/mastering-microsoft-power-bi-from-beginner-to-advanced/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5365294_7ba1.jpg"
    },
    "AI Machine Learning Complete Course: for PHP & Python Devs": {
        "Description": "Build real-world AI & machine learning apps using both PHP & Python. No prior ML knowledge required. Full Code Included.",
        "Is Paid": true,
        "Subscribers": 1881,
        "Average Rating": 4.25,
        "Number of Reviews": 70,
        "Number of Lectures": 65,
        "Content Length": "4.5 total hours",
        "Last Update": "2018-10-03",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Amr Shawqy",
            "Sameh Nabil"
        ],
        "Course URL": "https://www.udemy.com/course/ai-machine-learning-complete-course/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1929182_d767_5.jpg"
    },
    "Ultimate Neural Nets and Deep Learning Masterclass in Python": {
        "Description": "The best way to learn machine learning and AI using python: simply and fully explained concepts with practical exercises",
        "Is Paid": true,
        "Subscribers": 468,
        "Average Rating": 4.05,
        "Number of Reviews": 70,
        "Number of Lectures": 52,
        "Content Length": "6.5 total hours",
        "Last Update": "2019-02-15",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "John Harper"
        ],
        "Course URL": "https://www.udemy.com/course/neural-nets/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1379600_2500.jpg"
    },
    "Data Analysis and Statistical Modeling in R": {
        "Description": "Learn the foundation of Data Science, Analytics and Data interpretation using statistical tests with real world examples",
        "Is Paid": true,
        "Subscribers": 10079,
        "Average Rating": 4.05,
        "Number of Reviews": 70,
        "Number of Lectures": 37,
        "Content Length": "5 total hours",
        "Last Update": "2021-02-09",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Jazeb Akram"
        ],
        "Course URL": "https://www.udemy.com/course/data-analysis-and-statistical-modelling-in-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3797024_68bb_10.jpg"
    },
    "AP Computer Science A - Java Concepts and Fundamentals": {
        "Description": "Attain a high-level understanding of Java concepts and fundamentals with a focus on succeeding on the AP Exam",
        "Is Paid": true,
        "Subscribers": 356,
        "Average Rating": 4.352941,
        "Number of Reviews": 70,
        "Number of Lectures": 31,
        "Content Length": "3 total hours",
        "Last Update": "2022-03-22",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Jarrett Cornelison"
        ],
        "Course URL": "https://www.udemy.com/course/ap-computer-science-a-java-concepts-and-fundamentals/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4461212_146f_5.jpg"
    },
    "Learn OpenCV: Build # 30 Apps with OpenCV, YOLOv8 & YOLO-NAS": {
        "Description": "OpenCV, Object Detection, Object Tracking, Object Segmentation, YOLOv8, YOLO-NAS, Train Custom Dataset, Pose Estimation",
        "Is Paid": true,
        "Subscribers": 793,
        "Average Rating": 4.6896553,
        "Number of Reviews": 70,
        "Number of Lectures": 87,
        "Content Length": "24.5 total hours",
        "Last Update": "2023-11-29",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Muhammad Moin"
        ],
        "Course URL": "https://www.udemy.com/course/learn-opencv-build-30-apps-with-opencv-yolov8-yolo-nas/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5550794_4971.jpg"
    },
    "ChatGPT: Self-Publish an Amazon KDP Bestseller Book in 24hrs": {
        "Description": "ChatGPT Mastery: Supercharge Your Amazon KDP Success & Secure Passive Income in Just 24hrs!",
        "Is Paid": true,
        "Subscribers": 641,
        "Average Rating": 4.339286,
        "Number of Reviews": 70,
        "Number of Lectures": 32,
        "Content Length": "8.5 total hours",
        "Last Update": "2024-01-03",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Passive Income Gen Z"
        ],
        "Course URL": "https://www.udemy.com/course/chatgpt-self-publish-an-amazon-kdp-bestseller-book-in-24hrs-course/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5144770_69dd_4.jpg"
    },
    "Introduction to Diffusion Models": {
        "Description": "Diffusion Models from scratch using PyToch | In depth break down of Stable Diffusion and DALL\u00b7E 2",
        "Is Paid": true,
        "Subscribers": 473,
        "Average Rating": 4.45,
        "Number of Reviews": 70,
        "Number of Lectures": 56,
        "Content Length": "9.5 total hours",
        "Last Update": "2023-11-09",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Maxime Vandegar"
        ],
        "Course URL": "https://www.udemy.com/course/diffusion-models/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5334888_e69e_2.jpg"
    },
    "Semantic Search engine using Sentence BERT": {
        "Description": "Learn how to use Sentence BERT to find similar news headlines",
        "Is Paid": true,
        "Subscribers": 371,
        "Average Rating": 3.6,
        "Number of Reviews": 70,
        "Number of Lectures": 13,
        "Content Length": "2.5 total hours",
        "Last Update": "2020-04-24",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Evergreen Technologies"
        ],
        "Course URL": "https://www.udemy.com/course/semantic-search-engine-using-sentence-bert/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2818397_aa4c.jpg"
    },
    "Predictive Modeling with Python": {
        "Description": "Think with a predictive mindset and understand well the basics of the techniques used in prediction with this course",
        "Is Paid": true,
        "Subscribers": 16379,
        "Average Rating": 3.4,
        "Number of Reviews": 69,
        "Number of Lectures": 68,
        "Content Length": "9.5 total hours",
        "Last Update": "2021-06-21",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Exam Turf"
        ],
        "Course URL": "https://www.udemy.com/course/predictive-modeling-with-python-examturf/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4136520_8b9a_2.jpg"
    },
    "AI Essentials: Introduction to Artificial Intelligence": {
        "Description": "AI Essentials: A Simple Introduction to Artificial Intelligence Technologies by MTF Institute",
        "Is Paid": true,
        "Subscribers": 9683,
        "Average Rating": 4.257353,
        "Number of Reviews": 68,
        "Number of Lectures": 20,
        "Content Length": "1 total hour",
        "Last Update": "2023-12-01",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "MTF Institute of Management, Technology and Finance"
        ],
        "Course URL": "https://www.udemy.com/course/ai-essentials-introduction-to-artificial-intelligence/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5681724_5f41.jpg"
    },
    "Digital Twin": {
        "Description": "Explore the Future of Innovation - Master Digital Twins for Smart Solutions and Enhanced Decision-Making in Any Industry",
        "Is Paid": true,
        "Subscribers": 1495,
        "Average Rating": 4.536232,
        "Number of Reviews": 69,
        "Number of Lectures": 27,
        "Content Length": "2 total hours",
        "Last Update": "2024-02-01",
        "Badges": [
            "Bestseller"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Surendra Varma Pericherla"
        ],
        "Course URL": "https://www.udemy.com/course/digital-twin/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5744038_120b_2.jpg"
    },
    "Telecom Customer Churn Prediction in Apache Spark (ML)": {
        "Description": "Learn Apache Spark machine learning by creating a Telecom customer churn prediction project using Databricks Notebook",
        "Is Paid": true,
        "Subscribers": 15617,
        "Average Rating": 4.35,
        "Number of Reviews": 69,
        "Number of Lectures": 17,
        "Content Length": "2 total hours",
        "Last Update": "2023-10-27",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Bigdata Engineer"
        ],
        "Course URL": "https://www.udemy.com/course/telecom-customer-churn-prediction-in-apache-spark-ml/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2459992_8c0c_2.jpg"
    },
    "Python programming for Machine Learning , Data Analytics": {
        "Description": "Learn to create Machine Learning Algorithms in Python # Introduction to Data Science and Machine Learning [Step by Step]",
        "Is Paid": true,
        "Subscribers": 511,
        "Average Rating": 4.25,
        "Number of Reviews": 69,
        "Number of Lectures": 42,
        "Content Length": "7.5 total hours",
        "Last Update": "2020-06-27",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Academy of Computing & Artificial Intelligence"
        ],
        "Course URL": "https://www.udemy.com/course/python-programming-for-machine-learning-data-analytics/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2828518_22d1.jpg"
    },
    "Spark Machine Learning Project (House Sale Price Prediction)": {
        "Description": "Spark Machine Learning Project (House Sale Price Prediction) for beginner using Databricks Notebook (Unofficial)",
        "Is Paid": true,
        "Subscribers": 12300,
        "Average Rating": 4.2,
        "Number of Reviews": 69,
        "Number of Lectures": 16,
        "Content Length": "1.5 total hours",
        "Last Update": "2023-10-27",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Bigdata Engineer"
        ],
        "Course URL": "https://www.udemy.com/course/spark-machine-learning-project-house-sale-price-prediction/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2452496_efda_2.jpg"
    },
    "Master Azure OpenAI and ChatGPT": {
        "Description": "Create enterprise AI solutions using Microsoft Azure AI Services (ChatGPT, Cognitive Search, Bing and many others)",
        "Is Paid": true,
        "Subscribers": 363,
        "Average Rating": 4.1,
        "Number of Reviews": 68,
        "Number of Lectures": 9,
        "Content Length": "1.5 total hours",
        "Last Update": "2023-03-21",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Freddy Ayala"
        ],
        "Course URL": "https://www.udemy.com/course/azure-open-ai/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5218738_ee2f_5.jpg"
    },
    "Advanced Reinforcement Learning: policy gradient methods": {
        "Description": "Build Artificial Intelligence (AI) agents using Deep Reinforcement Learning and PyTorch: (REINFORCE, A2C, PPO, etc)",
        "Is Paid": true,
        "Subscribers": 1123,
        "Average Rating": 4.7272725,
        "Number of Reviews": 68,
        "Number of Lectures": 96,
        "Content Length": "7.5 total hours",
        "Last Update": "2024-01-01",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Escape Velocity Labs"
        ],
        "Course URL": "https://www.udemy.com/course/advanced-rl-pg/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4635836_2d12_2.jpg"
    },
    "Data Science Interview Preparation - Career Guide": {
        "Description": "Prepare for your Data Science Interview with this full guide on a career in Data Science including practice questions!",
        "Is Paid": true,
        "Subscribers": 1042,
        "Average Rating": 4.85,
        "Number of Reviews": 68,
        "Number of Lectures": 23,
        "Content Length": "4 total hours",
        "Last Update": "2019-05-10",
        "Badges": [
            "Highest Rated"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Up Degree"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-interview/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2014482_494d.jpg"
    },
    "Professional Certificate in Machine Learning 2024": {
        "Description": "Learn all the skills to become a Data Scientist &amp;  Build 500+ Artificial Intelligence Projects with source",
        "Is Paid": true,
        "Subscribers": 553,
        "Average Rating": 4.3,
        "Number of Reviews": 67,
        "Number of Lectures": 196,
        "Content Length": "24 total hours",
        "Last Update": "2023-08-23",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Academy of Computing & Artificial Intelligence"
        ],
        "Course URL": "https://www.udemy.com/course/professional-certificate-in-machine-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3840876_99a7_3.jpg"
    },
    "Data Engineering with Spark Databricks Delta Lake Lakehouse": {
        "Description": "Apache Spark  Databricks Lakehouse Delta Lake   Delta Tables  Delta Caching Scala Python Data Engineering for beginners",
        "Is Paid": true,
        "Subscribers": 1293,
        "Average Rating": 4.5384617,
        "Number of Reviews": 67,
        "Number of Lectures": 26,
        "Content Length": "2.5 total hours",
        "Last Update": "2024-01-01",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "FutureX Skills"
        ],
        "Course URL": "https://www.udemy.com/course/data-engineering-with-spark-databricks-delta-lake-lakehouse/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5133314_dd0d.jpg"
    },
    "Microsoft Power BI Practice Tests and Interview Questions": {
        "Description": "Test & Improve your Microsoft Power BI skills | All topics included | Practice Questions | Common Interview Questions",
        "Is Paid": true,
        "Subscribers": 23561,
        "Average Rating": 4.35,
        "Number of Reviews": 67,
        "Number of Lectures": 0,
        "Content Length": "90 questions",
        "Last Update": "2022-08-08",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Prince Patni"
        ],
        "Course URL": "https://www.udemy.com/course/microsoft-power-bi-practice-tests-and-interview-questions/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4821760_26ed.jpg"
    },
    "Learn to scrape any website with R": {
        "Description": "Get data from the web directly into R",
        "Is Paid": true,
        "Subscribers": 302,
        "Average Rating": 4.65,
        "Number of Reviews": 67,
        "Number of Lectures": 30,
        "Content Length": "3 total hours",
        "Last Update": "2020-07-28",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Mikkel Freltoft Krogsholm"
        ],
        "Course URL": "https://www.udemy.com/course/scrape-any-website-with-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3329252_3a10.jpg"
    },
    "High Resolution Generative Adversarial Networks (GANs)": {
        "Description": "Photorealistic image generation with Python and TensorFlow 2.0",
        "Is Paid": true,
        "Subscribers": 907,
        "Average Rating": 4.3,
        "Number of Reviews": 66,
        "Number of Lectures": 57,
        "Content Length": "7.5 total hours",
        "Last Update": "2022-01-31",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Brad Klingensmith"
        ],
        "Course URL": "https://www.udemy.com/course/high-resolution-generative-adversarial-networks/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4478692_7a04_2.jpg"
    },
    "Machine Learning & Data Science Masterclass in Python and R": {
        "Description": "Machine learning with many practical examples. Regression, Classification and much more",
        "Is Paid": true,
        "Subscribers": 721,
        "Average Rating": 4.2,
        "Number of Reviews": 66,
        "Number of Lectures": 204,
        "Content Length": "17 total hours",
        "Last Update": "2021-01-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Denis Panjuta"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-data-science-masterclass/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2295605_4aef.jpg"
    },
    "Machine Learning and Data Science Essentials with Python & R": {
        "Description": "Master Machine Learning with Python, Tensorflow & R. Data Science is the most in-demand and Highest Paying Job of 2018",
        "Is Paid": true,
        "Subscribers": 4862,
        "Average Rating": 4.35,
        "Number of Reviews": 66,
        "Number of Lectures": 24,
        "Content Length": "5.5 total hours",
        "Last Update": "2017-12-16",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "AkaSkills! 35,000+ Students"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-with-python-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1471462_10f1.jpg"
    },
    "Building Big Data Pipelines with PySpark + MongoDB + Bokeh": {
        "Description": "Build intelligent data pipelines with big data processing and machine learning technologies",
        "Is Paid": true,
        "Subscribers": 2406,
        "Average Rating": 3.85,
        "Number of Reviews": 66,
        "Number of Lectures": 25,
        "Content Length": "5 total hours",
        "Last Update": "2020-02-13",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "EBISYS R&D"
        ],
        "Course URL": "https://www.udemy.com/course/building-big-data-pipelines-with-pyspark-mongodb-bokeh/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2806989_c457.jpg"
    },
    "Accelerate Your Bioinformatic Skills with AI (prompt master)": {
        "Description": "Introduction to AI and Unlocking the Power of Chatbots (ChatGpt) in Bioinformatics Research (Prompt Engineering)",
        "Is Paid": true,
        "Subscribers": 127,
        "Average Rating": 4.625,
        "Number of Reviews": 65,
        "Number of Lectures": 16,
        "Content Length": "1.5 total hours",
        "Last Update": "2023-04-18",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Abdul Rehman Ikram"
        ],
        "Course URL": "https://www.udemy.com/course/accelerate-your-bioinformatic-skills-with-ai-prompt-master/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5251198_eeaf_2.jpg"
    },
    "Object Oriented Programming using Python + Pycharm Hands-on": {
        "Description": "Practical approach to object oriented programming using Python and Pycharm. Grow as a Python developer.",
        "Is Paid": true,
        "Subscribers": 439,
        "Average Rating": 4.2714286,
        "Number of Reviews": 64,
        "Number of Lectures": 27,
        "Content Length": "2.5 total hours",
        "Last Update": "2023-12-15",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Faisal Memon",
            "EmbarkX Official"
        ],
        "Course URL": "https://www.udemy.com/course/object-oriented-programming-using-python-pycharm-hands-on/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4302237_d1a2_2.jpg"
    },
    "Data Science: Bitcoin Data Visualization &  Price Prediction": {
        "Description": "Data Science: Hands-on & Practical Cryptocurrency Data Visualization & Bitcoin Price Forecasting using Machine Learning",
        "Is Paid": true,
        "Subscribers": 6813,
        "Average Rating": 4.25,
        "Number of Reviews": 65,
        "Number of Lectures": 14,
        "Content Length": "1.5 total hours",
        "Last Update": "2021-03-17",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "School of Disruptive Innovation"
        ],
        "Course URL": "https://www.udemy.com/course/cryptocurrency-data-visualization-bitcoin-price-prediction/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3614386_ef81_3.jpg"
    },
    "Natural Language Processing | Build LLM Web App | RNN & LSTM": {
        "Description": "Create App Using Streamlit | Sentiment Analysis | Speech to text | Spam Detection",
        "Is Paid": true,
        "Subscribers": 16182,
        "Average Rating": 4.3,
        "Number of Reviews": 65,
        "Number of Lectures": 30,
        "Content Length": "2.5 total hours",
        "Last Update": "2023-10-10",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "SeaportAi ."
        ],
        "Course URL": "https://www.udemy.com/course/nlp-natural-language-processing/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3708128_9043_4.jpg"
    },
    "Natural Language Processing [ Building Real World Projects]": {
        "Description": "Build Real World Applications of Natural Language Processing [COMPLETE PROJECT]",
        "Is Paid": true,
        "Subscribers": 19095,
        "Average Rating": 4.25,
        "Number of Reviews": 64,
        "Number of Lectures": 31,
        "Content Length": "4 total hours",
        "Last Update": "2020-08-13",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Academy of Computing & Artificial Intelligence",
            "Future AI  - Academy of Computing & Artificial Intelligence",
            "Savidu Dias"
        ],
        "Course URL": "https://www.udemy.com/course/natural-language-processing-building-real-world-projects/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3110312_7233.jpg"
    },
    "Python for Marketing Analytics: Hands-On Machine Learning": {
        "Description": "Machine Learning Algorithms | Numpy, Pandas, Sklearn, VarClusHi | 2 Real World Marketing Analytics Python Projects",
        "Is Paid": true,
        "Subscribers": 589,
        "Average Rating": 4.7272725,
        "Number of Reviews": 64,
        "Number of Lectures": 144,
        "Content Length": "25.5 total hours",
        "Last Update": "2023-10-03",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Machine Learning Express"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-with-projects-on-retail-marketing-analytics/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3751642_8d21_3.jpg"
    },
    "Data Extraction Basics for Docs and Images with OCR and NER": {
        "Description": "Become a Data Extraction Expert with Python, Pandas, OCR, NER, and Spacy : Learn to Train and Build Real-World Solutions",
        "Is Paid": true,
        "Subscribers": 311,
        "Average Rating": 4.7,
        "Number of Reviews": 64,
        "Number of Lectures": 39,
        "Content Length": "2 total hours",
        "Last Update": "2023-09-25",
        "Badges": [
            "Highest Rated"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Vineeta Vashistha"
        ],
        "Course URL": "https://www.udemy.com/course/ocr-for-smart-data-extraction-from-pdf-and-images-with-ner/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4479904_bcb5.jpg"
    },
    "Kaggle Master with Heart Attack Prediction Kaggle Project": {
        "Description": "Kaggle is Machine Learning &amp; Data Science community. Become Kaggle master with real machine learning kaggle project",
        "Is Paid": true,
        "Subscribers": 676,
        "Average Rating": 4.55,
        "Number of Reviews": 64,
        "Number of Lectures": 72,
        "Content Length": "11 total hours",
        "Last Update": "2024-02-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Oak Academy",
            "OAK Academy Team"
        ],
        "Course URL": "https://www.udemy.com/course/kaggle-master-with-heart-attack-prediction-kaggle-project/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4682720_67ba_4.jpg"
    },
    "Machine Learning A-Z\u2122: Hands-On Python & R in Data Science": {
        "Description": "Machine Learning , Python, Advanced Data Visualization, R Programming, Linear Regression, Decision Trees,  NumPy, Pandas",
        "Is Paid": true,
        "Subscribers": 10852,
        "Average Rating": 3.45,
        "Number of Reviews": 64,
        "Number of Lectures": 151,
        "Content Length": "15 total hours",
        "Last Update": "2019-11-22",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Apex Education"
        ],
        "Course URL": "https://www.udemy.com/course/data-science-and-machine-learning-bootcamp-with-python-and-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2626940_cd26.jpg"
    },
    "Databricks Certified Data Engineer Associate Exam Prep 2023": {
        "Description": "Databricks Certified Data Engineer Associate 2023 V3 Exam Guide | Databricks | Databricks Data Engineer Bootcamp",
        "Is Paid": true,
        "Subscribers": 685,
        "Average Rating": 4.3809524,
        "Number of Reviews": 62,
        "Number of Lectures": 81,
        "Content Length": "8 total hours",
        "Last Update": "2023-07-12",
        "Badges": [
            "Highest Rated"
        ],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Henry Habib",
            "The Intelligent Worker"
        ],
        "Course URL": "https://www.udemy.com/course/databricks-certified-data-engineer-associate-complete-guide/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5371304_e34a_4.jpg"
    },
    "Practical Foundations of R Programming": {
        "Description": "The basics of programming in R: R data structures; R subsetting operations; and R functions",
        "Is Paid": true,
        "Subscribers": 825,
        "Average Rating": 4.45,
        "Number of Reviews": 63,
        "Number of Lectures": 101,
        "Content Length": "8 total hours",
        "Last Update": "2017-06-20",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Geoffrey Hubona, Ph.D."
        ],
        "Course URL": "https://www.udemy.com/course/practical-foundations-of-r-programming/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/850940_920e_3.jpg"
    },
    "Artificial Intelligence Bootcamp in R Programming": {
        "Description": "Practical Neural Networks and Deep Learning in R",
        "Is Paid": true,
        "Subscribers": 770,
        "Average Rating": 3.7,
        "Number of Reviews": 63,
        "Number of Lectures": 86,
        "Content Length": "10 total hours",
        "Last Update": "2023-12-21",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Minerva Singh",
            "SuperDataScience Team",
            "Ligency Team"
        ],
        "Course URL": "https://www.udemy.com/course/artificial-intelligence-bootcamp-in-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2472836_368d.jpg"
    },
    "Python for Mastering Machine Learning and Data Science": {
        "Description": "Learn Pandas, Scikit-Learn, Seaborn, Matplotlib, Machine Learning, NLP, Dealing with practical problems and more!",
        "Is Paid": true,
        "Subscribers": 2573,
        "Average Rating": 4.65,
        "Number of Reviews": 63,
        "Number of Lectures": 93,
        "Content Length": "20 total hours",
        "Last Update": "2023-01-19",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Jifry Issadeen"
        ],
        "Course URL": "https://www.udemy.com/course/master-machine-learning-and-data-science-with-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4456438_14ac_9.jpg"
    },
    "Machine Learning for Predictive Maps in Python and Leaflet": {
        "Description": "Using the power of machine learning to build predictive map applications",
        "Is Paid": true,
        "Subscribers": 3295,
        "Average Rating": 4.5,
        "Number of Reviews": 63,
        "Number of Lectures": 32,
        "Content Length": "6 total hours",
        "Last Update": "2020-06-29",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "EBISYS R&D"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-for-predictive-maps-in-python-and-leaflet/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2769056_6a14_2.jpg"
    },
    "Learn SQL databases in a weekend": {
        "Description": "SQL crash-course with everything you need to jump into database programming projects. Learn it all in a single weekend!",
        "Is Paid": true,
        "Subscribers": 243,
        "Average Rating": 4.85,
        "Number of Reviews": 63,
        "Number of Lectures": 154,
        "Content Length": "8.5 total hours",
        "Last Update": "2021-11-01",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Girts Strazdins"
        ],
        "Course URL": "https://www.udemy.com/course/learn-sql-databases-in-a-weekend/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3758122_7d5d_2.jpg"
    },
    "Artificial Intelligence and Machine Learning: Complete Guide": {
        "Description": "Do you want to study AI and don't know where to start? You will learn everything you need to know in theory and practice",
        "Is Paid": true,
        "Subscribers": 1599,
        "Average Rating": 4.72093,
        "Number of Reviews": 63,
        "Number of Lectures": 189,
        "Content Length": "22.5 total hours",
        "Last Update": "2023-09-25",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Jones Granatyr",
            "AI Expert Academy"
        ],
        "Course URL": "https://www.udemy.com/course/artificial-intelligence-and-machine-learning-complete-guide/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5536934_acf3.jpg"
    },
    "Market Basket Analysis & Linear Discriminant Analysis with R": {
        "Description": "Master: Association rules (MBA) & it's usage, Linear Discriminant Analysis (LDA) for classification & variable selection",
        "Is Paid": true,
        "Subscribers": 416,
        "Average Rating": 4.35,
        "Number of Reviews": 63,
        "Number of Lectures": 36,
        "Content Length": "3.5 total hours",
        "Last Update": "2017-08-06",
        "Badges": [],
        "Course Language": "English (India)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Gopal Prasad Malakar"
        ],
        "Course URL": "https://www.udemy.com/course/market-basket-analysis-linear-discriminant-analysis-with-r/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1253390_c1e8_3.jpg"
    },
    "Python Data Science Fundamentals: Getting Started": {
        "Description": "Python Data Science Fundamentals: Dive into NumPy, Pandas, Matplotlib, and Scikit-learn for Powerful Data Insights",
        "Is Paid": true,
        "Subscribers": 8356,
        "Average Rating": 4.3076925,
        "Number of Reviews": 62,
        "Number of Lectures": 22,
        "Content Length": "2 total hours",
        "Last Update": "2023-08-03",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Academy of Computing & Artificial Intelligence"
        ],
        "Course URL": "https://www.udemy.com/course/python-data-science-fundamentals-getting-started/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5479158_99ce.jpg"
    },
    "Become a Data Scientist: SQL, Tableau, ML & DL [4-in-1]": {
        "Description": "4-in-1 Bundle covering the 4 essential topics for a data scientist - SQL, Tableau, Machine & Deep Learning using Python",
        "Is Paid": true,
        "Subscribers": 1515,
        "Average Rating": 4.642857,
        "Number of Reviews": 62,
        "Number of Lectures": 329,
        "Content Length": "37 total hours",
        "Last Update": "2024-01-08",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Start-Tech Academy"
        ],
        "Course URL": "https://www.udemy.com/course/become-a-data-scientist/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5254956_406a_3.jpg"
    },
    "Machine Learning in Python: From Zero to Hero in 10 Hours": {
        "Description": "Machine Learning & Data Science in Python with real life projects. Source codes included.",
        "Is Paid": true,
        "Subscribers": 402,
        "Average Rating": 4.55,
        "Number of Reviews": 62,
        "Number of Lectures": 75,
        "Content Length": "8 total hours",
        "Last Update": "2021-07-27",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Sanjay Singh"
        ],
        "Course URL": "https://www.udemy.com/course/applied-machine-learning-hands-on-course/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2540164_c299_2.jpg"
    },
    "Math 0-1: Matrix Calculus in Data Science & Machine Learning": {
        "Description": "A Casual Guide for Artificial Intelligence, Deep Learning, and Python Programmers",
        "Is Paid": true,
        "Subscribers": 1095,
        "Average Rating": 4.836066,
        "Number of Reviews": 62,
        "Number of Lectures": 37,
        "Content Length": "6.5 total hours",
        "Last Update": "2024-02-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Lazy Programmer Inc."
        ],
        "Course URL": "https://www.udemy.com/course/matrix-calculus-machine-learning/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5571740_5726.jpg"
    },
    "Anyword AI: The Best Generative Artificial Intelligence Tool": {
        "Description": "Unlock the Power of AI Content Creation with AnyWord \u2013 The Ultimate Solution for Your Marketing Needs!",
        "Is Paid": true,
        "Subscribers": 15787,
        "Average Rating": 4.193548,
        "Number of Reviews": 62,
        "Number of Lectures": 17,
        "Content Length": "1.5 total hours",
        "Last Update": "2023-05-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Prince Patni"
        ],
        "Course URL": "https://www.udemy.com/course/anyword-ai-the-best-generative-artificial-intelligence-tool/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/5302880_c6a4_2.jpg"
    },
    "Microsoft Azure Machine Learning - DP-100": {
        "Description": "Learn Microsoft Azure Machine Learning Studio and prepare your DP-100 Certification Exam",
        "Is Paid": true,
        "Subscribers": 298,
        "Average Rating": 3.85,
        "Number of Reviews": 62,
        "Number of Lectures": 45,
        "Content Length": "6.5 total hours",
        "Last Update": "2021-02-15",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Data Science Training"
        ],
        "Course URL": "https://www.udemy.com/course/azure-machine-learning-bootcamp/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/3439738_2c92_2.jpg"
    },
    "Machine Learning in Python - Complete Course & Projects": {
        "Description": "Learn Machine Learning Algorithms and their Python Implementations. Learn the core concepts in Machine Learning.",
        "Is Paid": true,
        "Subscribers": 6056,
        "Average Rating": 4.45,
        "Number of Reviews": 62,
        "Number of Lectures": 57,
        "Content Length": "5 total hours",
        "Last Update": "2023-08-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Onur Baltac\u0131"
        ],
        "Course URL": "https://www.udemy.com/course/python-machine-learning-course/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4937890_b605_5.jpg"
    },
    "Master Azure Databricks": {
        "Description": "Learn Databricks concepts, PySpark, Spark Structure Streaming, Delta lake, Databricks SQL Analytics, REST API & CLI",
        "Is Paid": true,
        "Subscribers": 448,
        "Average Rating": 4.1153846,
        "Number of Reviews": 62,
        "Number of Lectures": 152,
        "Content Length": "13 total hours",
        "Last Update": "2023-11-06",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "A. K Kumar"
        ],
        "Course URL": "https://www.udemy.com/course/master-azure-databricks/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4627006_329f.jpg"
    },
    "Learn Data Analysis with Python Pandas": {
        "Description": "Real world examples of Python Pandas to analyse large data files. Create visual representations of your data.",
        "Is Paid": true,
        "Subscribers": 5298,
        "Average Rating": 3.8,
        "Number of Reviews": 61,
        "Number of Lectures": 32,
        "Content Length": "2.5 total hours",
        "Last Update": "2018-11-05",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Tony Staunton"
        ],
        "Course URL": "https://www.udemy.com/course/python-pandas-data-manipulation-and-analysis/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/1980038_aca5_3.jpg"
    },
    "Learn Data Wrangling with Python": {
        "Description": "Perform Data Wrangling with the Python Programming Language. Practice and Solution Notebooks included.",
        "Is Paid": true,
        "Subscribers": 6694,
        "Average Rating": 4.3,
        "Number of Reviews": 61,
        "Number of Lectures": 18,
        "Content Length": "1.5 total hours",
        "Last Update": "2023-10-19",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Valentine Mwangi"
        ],
        "Course URL": "https://www.udemy.com/course/data-wrangling-with-python-in-1-hour/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/2734304_e520.jpg"
    },
    "Data Science:  Machine Learning algorithms in Matlab": {
        "Description": "A-Z Guide to Implementing Classic Machine Learning Algorithms From Scratch and with Matlab and maths.",
        "Is Paid": true,
        "Subscribers": 553,
        "Average Rating": 3.7,
        "Number of Reviews": 61,
        "Number of Lectures": 26,
        "Content Length": "2.5 total hours",
        "Last Update": "2018-04-13",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Geek Cafe"
        ],
        "Course URL": "https://www.udemy.com/course/machine-learning-step-by-step-guide/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/1112654_0088_4.jpg"
    },
    "Complete Python for Data Science & Machine Learning from A-Z": {
        "Description": "Python with Machine Learning & Data Science, Data Visulation, Numpy & Pandas for Data Analysis, Kaggle projects from A-Z",
        "Is Paid": true,
        "Subscribers": 494,
        "Average Rating": 4.75,
        "Number of Reviews": 61,
        "Number of Lectures": 318,
        "Content Length": "43.5 total hours",
        "Last Update": "2024-02-04",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Oak Academy",
            "OAK Academy Team",
            "Ali\u0307 CAVDAR"
        ],
        "Course URL": "https://www.udemy.com/course/complete-python-for-data-science-machine-learning-from-a-z/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/5289390_5cd0.jpg"
    },
    "Crash Course - R programming from Scratch & workout": {
        "Description": "Analytics / Data Science: Learn to Import, Sort, Merge, Subset, Append, Freq, Univariate, Regression, Derive variable",
        "Is Paid": true,
        "Subscribers": 540,
        "Average Rating": 3.95,
        "Number of Reviews": 61,
        "Number of Lectures": 49,
        "Content Length": "4 total hours",
        "Last Update": "2021-01-27",
        "Badges": [],
        "Course Language": "English (India)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Gopal Prasad Malakar"
        ],
        "Course URL": "https://www.udemy.com/course/introduction-to-r-programming-learn-r-syntax-by-example/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/375989_7ada_8.jpg"
    },
    "Spark SQL & Hadoop (For Data Science)": {
        "Description": "Learn HDFS commands, Hadoop, Spark SQL, SQL Queries, ETL & Data Analysis| Spark Hadoop Cluster VM | Fully Solved Qs",
        "Is Paid": true,
        "Subscribers": 5529,
        "Average Rating": 4.4,
        "Number of Reviews": 60,
        "Number of Lectures": 85,
        "Content Length": "5.5 total hours",
        "Last Update": "2022-03-21",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Matthew Barr"
        ],
        "Course URL": "https://www.udemy.com/course/spark-sql-hadoop-for-data-scientists-big-data-analysts/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4104862_c5cb.jpg"
    },
    "Introduction to R programming & RStudio for beginners": {
        "Description": "Introduction to R programming & RStudio for beginners - with practical exercises",
        "Is Paid": true,
        "Subscribers": 7213,
        "Average Rating": 3.25,
        "Number of Reviews": 60,
        "Number of Lectures": 10,
        "Content Length": "31 total mins",
        "Last Update": "2021-01-14",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "JP COURSES"
        ],
        "Course URL": "https://www.udemy.com/course/introduction-to-r-programming-rstudio-for-beginners/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/3414440_a333_2.jpg"
    },
    "Introduction to AI Governance": {
        "Description": "Learn how to measure, monitor and control your AI Models",
        "Is Paid": true,
        "Subscribers": 294,
        "Average Rating": 4.3194447,
        "Number of Reviews": 60,
        "Number of Lectures": 8,
        "Content Length": "1.5 total hours",
        "Last Update": "2022-08-26",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Neena Sathi"
        ],
        "Course URL": "https://www.udemy.com/course/introduction-to-ai-governance/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/3801630_4977_2.jpg"
    },
    "Guide to Big Data Analytics: Origination to Opportunities": {
        "Description": "Foundation in basic  big data analytic methods, technology and tools",
        "Is Paid": true,
        "Subscribers": 616,
        "Average Rating": 4.35,
        "Number of Reviews": 60,
        "Number of Lectures": 59,
        "Content Length": "2.5 total hours",
        "Last Update": "2017-12-27",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "RankOne Consulting"
        ],
        "Course URL": "https://www.udemy.com/course/big-data-analytics/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/708630_dc3f_4.jpg"
    },
    "Complete DataScience with Python and Tensorflow": {
        "Description": "Learn about machine learning, deep learning, text analytics using python and tensorflow",
        "Is Paid": true,
        "Subscribers": 339,
        "Average Rating": 3.35,
        "Number of Reviews": 60,
        "Number of Lectures": 147,
        "Content Length": "11 total hours",
        "Last Update": "2018-07-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Full Stack Datascientist"
        ],
        "Course URL": "https://www.udemy.com/course/complete-datascience-with-python-and-tensorflow/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/1706472_c928_4.jpg"
    },
    "Pyspark Foundation for Data Engineering | Beginners": {
        "Description": "Data Engineering, PySpark, Coding exercise",
        "Is Paid": true,
        "Subscribers": 781,
        "Average Rating": 4.3,
        "Number of Reviews": 59,
        "Number of Lectures": 24,
        "Content Length": "1 total hour",
        "Last Update": "2022-06-08",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Akash Sunil Pawar"
        ],
        "Course URL": "https://www.udemy.com/course/pyspark-foundation-for-data-engineering-begineers/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4724890_cf2d_3.jpg"
    },
    "2024 Advanced Machine Learning and Deep Learning Projects": {
        "Description": "Text Embedding, Clustering, Classification | Image Clustering, Classification, Text to Image Search",
        "Is Paid": true,
        "Subscribers": 15881,
        "Average Rating": 4.5,
        "Number of Reviews": 59,
        "Number of Lectures": 32,
        "Content Length": "5.5 total hours",
        "Last Update": "2024-01-02",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Laxmi Kant | KGP Talkie"
        ],
        "Course URL": "https://www.udemy.com/course/advanced-natural-language-and-image-processing-projects/",
        "Image URL": "https://img-b.udemycdn.com/course/125_H/4726808_5e8e.jpg"
    },
    "Advanced Apache Spark for Data Scientists and Developers ": {
        "Description": "Apache Spark",
        "Is Paid": true,
        "Subscribers": 515,
        "Average Rating": 3.65,
        "Number of Reviews": 59,
        "Number of Lectures": 71,
        "Content Length": "5.5 total hours",
        "Last Update": "2016-01-18",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Intermediate Level",
        "Authors": [
            "Adastra Academy"
        ],
        "Course URL": "https://www.udemy.com/course/advanced-apache-spark-for-data-scientists-and-developers/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/500160_73b7_2.jpg"
    },
    "Data Science Bootcamp in Python: 250+ Exercises to Master": {
        "Description": "Unlock the World of Data Science in Python with 250+ Engaging Exercises - Master the Art of Data Science!",
        "Is Paid": true,
        "Subscribers": 37517,
        "Average Rating": 4.25,
        "Number of Reviews": 59,
        "Number of Lectures": 65,
        "Content Length": "40 total mins",
        "Last Update": "2023-10-30",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Pawe\u0142 Krakowiak"
        ],
        "Course URL": "https://www.udemy.com/course/250-exercises-data-science-bootcamp-in-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3134370_720b_7.jpg"
    },
    "Batch Processing with Apache Beam in Python": {
        "Description": "Easy to follow, hands-on introduction to batch data processing in Python",
        "Is Paid": true,
        "Subscribers": 275,
        "Average Rating": 3.35,
        "Number of Reviews": 59,
        "Number of Lectures": 19,
        "Content Length": "1 total hour",
        "Last Update": "2020-09-29",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Alexandra Abbas"
        ],
        "Course URL": "https://www.udemy.com/course/apache-beam-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3535406_1889_2.jpg"
    },
    "TensorFlow Hub: Deep Learning, Computer Vision and NLP": {
        "Description": "Build computer vision and natural language processing projects quickly, easily and with few lines of code!",
        "Is Paid": true,
        "Subscribers": 941,
        "Average Rating": 4.7,
        "Number of Reviews": 59,
        "Number of Lectures": 46,
        "Content Length": "7 total hours",
        "Last Update": "2023-04-27",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Jones Granatyr",
            "AI Expert Academy"
        ],
        "Course URL": "https://www.udemy.com/course/tensorflow-hub-deep-learning-computer-vision-nlp/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4807418_1ece.jpg"
    },
    "R Programming: R for Data Science and Data Analytics A-Z\u2122": {
        "Description": "Learn R Programming Hands-on - Vectors and Data Frames, R Packages & Functions, R in Data Visualization, Apply R for ML",
        "Is Paid": true,
        "Subscribers": 5220,
        "Average Rating": 4.4,
        "Number of Reviews": 59,
        "Number of Lectures": 34,
        "Content Length": "7.5 total hours",
        "Last Update": "2019-12-13",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Teach Premium",
            "Apex Education"
        ],
        "Course URL": "https://www.udemy.com/course/r-programming-beginners/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2692478_ebbe_3.jpg"
    },
    "Hands-on Data Visualization With Python": {
        "Description": "Harness the power of Matplotlib, Seaborn and Plotly to boost your data visualization skills!",
        "Is Paid": true,
        "Subscribers": 850,
        "Average Rating": 3.8,
        "Number of Reviews": 58,
        "Number of Lectures": 50,
        "Content Length": "4.5 total hours",
        "Last Update": "2023-12-21",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Jordan Sauchuk",
            "Ligency Team",
            "SuperDataScience Team"
        ],
        "Course URL": "https://www.udemy.com/course/hands-on-data-visualization-with-python/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/3981144_ca8e.jpg"
    },
    "AI LAW, ETHICS, PRIVACY & LEGALITIES - DR. PAVAN DUGGAL -CLU": {
        "Description": "AN INTRODUCTION TO THE WONDERFUL WORLD OF DIFFERENT TOPICS UNDER ARTIFICIAL INTELLIGENCE LAW",
        "Is Paid": true,
        "Subscribers": 208,
        "Average Rating": 4.0,
        "Number of Reviews": 58,
        "Number of Lectures": 39,
        "Content Length": "1 total hour",
        "Last Update": "2021-02-04",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "All Levels",
        "Authors": [
            "Dr. Pavan Duggal"
        ],
        "Course URL": "https://www.udemy.com/course/ai-law-ethics-privacy-by-dr-pavan-duggal/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/2414664_56cf_5.jpg"
    },
    "Apache Spark 3 Programming | Databricks Certification Python": {
        "Description": "Become zero to hero in Apache PySpark 3.0 programming in a fun and easy way. Fastest way to prepare for Databricks exam.",
        "Is Paid": true,
        "Subscribers": 275,
        "Average Rating": 3.8,
        "Number of Reviews": 58,
        "Number of Lectures": 32,
        "Content Length": "2.5 total hours",
        "Last Update": "2021-07-07",
        "Badges": [],
        "Course Language": "English (US)",
        "Instructional Level": "Beginner Level",
        "Authors": [
            "Vivek Singh Bhadouria"
        ],
        "Course URL": "https://www.udemy.com/course/apache-pyspark-3-programming-and-databricks-certification/",
        "Image URL": "https://img-c.udemycdn.com/course/125_H/4168498_0951_8.jpg"
    },
}

class Command(BaseCommand):
    help = "Import predefined courses into the database"

    def handle(self, *args, **kwargs):
        for course_title, course_data in COURSE_DATA.items():
            # Ensure at least one author is assigned as the teacher
            teacher_name = course_data["Authors"][0]
            teacher, _ = User.objects.get_or_create(
                username=teacher_name,
                defaults={
                    "role": "teacher",
                    "email": f"{teacher_name.lower().replace(' ', '')}@example.com",
                    "password": "testpass"
                }
            )

            # Create or update the Course entry
            course, created = Course.objects.get_or_create(
                title=course_title,
                defaults={
                    "description": course_data["Description"],
                    "teacher": teacher,
                    "image_url": course_data["Image URL"],
                    "difficulty_level": course_data["Instructional Level"],
                },
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"Course added: {course.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Course already exists: {course.title}"))