
# Hate Speech Detection
XGBoost, LSTM and Transformer based approches fro predicting hate speech.  
Deployed with Python - Flask.


## Features

- Twitter Hate Speech Dataset
- Live Model Predictions on REST API
- Cross platform access

## API Reference

#### Get Traditional ML Model Prediction

```http
  GET /api/traditionalmlapi
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `text` | `string` | **Required**. Text for prediction |

#### Get Traditional LSTM Model Prediction

```http
  GET /api/lstmapi
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `text` | `string` | **Required**. Text for prediction |


#### Get Traditional Fusion Model Prediction

```http
  GET /api/fusionapi
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `text` | `string` | **Required**. Text for prediction |

## Tech Stack

#### Languages
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)


#### Machine Learning
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)

#### Web Development
![Flask](https://img.shields.io/badge/-Flask-blue?logo=flask&logoColor=black&style=for-the-badge) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)


## Deployment

To deploy the project backend run

```bash
  python main.py
```

To deploy the project frontend run

```bash
  npx tailwindcss -i ./static/input.css -o ./static/css/output.css --watch

```


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## Authors

- [Aditya R](https://www.github.com/adityarags)
- [Ayushi Indu](https://www.github.com/ayushi200116)
- [Urvashi Indu](https://www.github.com/urvashi16)
- [Palak Garg](https://www.github.com)
- [Ashish Vats](https://www.github.com)
