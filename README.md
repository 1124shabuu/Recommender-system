# Recommender-system
An app that will recommend you movies based on content and collaborative based filtering.The recommender recommends you on the basis of both content and collaborative based filtering and therefore is a hybrid recommender.For content based filtering ,on the basis of cast,director,overview,genres,keywords we have used cosine similarity for finding top 25 similar movies . In collaborative filtering we have used SVD algorithm to predict the ratings for a given user and after sorting returns top 5 movies for the user.
## Steps to setup the project :
1. Clone the git repository in your cmd/powershell
2. Install python
3. Install pycharm using this [link](https://www.jetbrains.com/pycharm/download/#section=windows)
4. Make a new project on  venv  using base interpreter of latest version of python and add files(indices.pkl,links.pkl,links1.pkl,main.py,matrix.pkl,movies.pkl,svd1.pkl,users.pkl to it
5. In the terminal install the streamlit package using the command:
    `pip install streamlit`
6. Install scikit surprise using the commands:
    ````
    pip install numpy cython
    git clone https://github.com/NicolasHug/surprise.git
    cd surprise
    python setup.py install
    ````
7. In the terminal now run:
   `streamlit run main.py`
   
  ** You are good to go**
  
  
