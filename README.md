# Research Paper Recommendation
#### A simple NLP and ML based website which recommends the best research papers similar to your research paper.

## DISCLAIMER ⚠️
This is a POC(Proof of concept) kind-of project. The data used here comes up with no guarantee from the creator. However, this project presents the idea that how we can use NLP/ML into information retrieval if developed at large scale and with authentic and verified data.

## MOTIVATION 💪
- 1. Enhanced Search Capabilities: Traditional search systems often rely on keyword matching, which can be limited in understanding the context or nuances of queries. NLP and ML can improve the relevance of search results by understanding and processing natural language more effectively, leading to better user satisfaction and more accurate information retrieval.

- 2. Personalization: ML algorithms can analyze user behavior and preferences to personalize search results. By tailoring the information retrieval process to individual users, the system can provide more relevant content, improving engagement and user experience.

- 3. Scalability: NLP and ML techniques can handle large volumes of data and queries more efficiently than traditional methods. This scalability is crucial for systems that need to manage vast amounts of information, such as search engines, digital libraries, or customer support systems.

- 4. Innovative Applications: Combining NLP and ML opens up opportunities for innovative applications, such as question-answering systems, chatbots, and automated summarization tools. These applications can enhance user interactions and provide new ways to access and utilize information.

- 5. Competitive Advantage: Implementing cutting-edge NLP and ML techniques can give organizations a competitive edge by offering superior information retrieval capabilities compared to traditional systems. This can lead to better user retention, increased user satisfaction, and overall improved business performance.


## DATA SOURCE 📊
- [Research Papers dataset ](https://www.kaggle.com/datasets/spsayakpaul/arxiv-paper-abstracts/data)

## Useful Links
- Blog 1 : https://www.analyticsvidhya.com/blog/2021/06/part-20-step-by-step-guide-to-master-nlp-information-retrieval/
- Blog 2 : https://scikit-learn.org/stable/modules/neighbors.html


# Built with 🛠️
<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code>
<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/html/html.png"></code>
<code><img height="30" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/git/git.png"></code>
<code><img height="30" src="https://symbols.getvecta.com/stencil_80/56_flask.3a79b5a056.jpg"></code>
<code><img height="30" src="https://raw.githubusercontent.com/numpy/numpy/7e7f4adab814b223f7f917369a72757cd28b10cb/branding/icons/numpylogo.svg"></code>
<code><img height="30" src="https://raw.githubusercontent.com/pandas-dev/pandas/761bceb77d44aa63b71dda43ca46e8fd4b9d7422/web/pandas/static/img/pandas.svg"></code>
<code><img height="30" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1280px-Scikit_learn_logo_small.svg.png"></code>

## DEPLOYMENT 🚀

#### Deployment is done using [deploy](https://github.com/Nihal-Mevekari/End_to_End_Research_Paper_Recommendation_using_Information_Retrieval) branch
#### This website is deployed at [AWS](https://aws.amazon.com/)

## How to use 💻
- Crop Recommendation system ==> enter the corresponding nutrient values of your soil, state and city. Note that, the N-P-K (Nitrogen-Phosphorous-Pottasium) values to be entered should be the ratio between them. Refer [this website](https://www.gardeningknowhow.com/garden-how-to/soil-fertilizers/fertilizer-numbers-npk.htm) for more information.
Note: When you enter the city name, make sure to enter mostly common city names. Remote cities/towns may not be available in the [Weather API](https://openweathermap.org/) from where humidity, temperature data is fetched.

- Fertilizer suggestion system ==> Enter the nutrient contents of your soil and the crop you want to grow. The algorithm will tell which nutrient the soil has excess of or lacks. Accordingly, it will give suggestions for buying fertilizers.

- Disease Detection System ==> Upload an image of leaf of your plant. The algorithm will tell the crop type and whether it is diseased or healthy. If it is diseased, it will tell you the cause of the disease and suggest you how to prevent/cure the disease accordingly.
Note that, for now it only supports following crops


## How to run locally 🛠️
- Before the following steps make sure you have [git](https://git-scm.com/download), [Anaconda](https://www.anaconda.com/) or [miniconda](https://docs.conda.io/en/latest/miniconda.html) installed on your system
- Clone the complete project with `git clone https://github.com/Nihal-Mevekari/End_to_End_Research_Paper_Recommendation_using_Information_Retrieval` or you can just download the code and unzip it
  ```
  ❯ git clone -b deploy https://github.com/Nihal-Mevekari/End_to_End_Research_Paper_Recommendation_using_Information_Retrieval
  ```
- Once the project is cloned, open anaconda prompt in the directory where the project was cloned and paste the following block
  ```
  conda create -p venv python==3.11.0 -y
  conda activate venv
  pip install -r requirements.txt
  ```
- And finally run the project with
  ```
  python application.py
  ```
- Open the localhost url provided after running `application.py` and now you can use the project locally in your web browser.
## DEMO

- ### Research Paper recommendation system

![demo](https://media.giphy.com/media/90JbjdAa5nDq3TJh5u/giphy.gif)



## Usage ⚙️
You can use this project for further developing it and adding your work in it. If you use this project, kindly mention the original source of the project and mention the link of this repo in your report.

## Further Improvements 📈
This was my first big project so there are lot of things to improve upon

- Frontend can be made more nicer and more user friendly (PS: I suck at frontend development) :cry:	
- More data can be collected :monocle_face:	

## Contact 📞

#### If you have any doubt or want to contribute feel free to email me or hit me up on [LinkedIn](https://www.linkedin.com/in/nihal-mevekari/)
