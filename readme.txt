requirements:

pandas==2.1.4
numpy==1.26.0
torchvision==0.17.0
pytorch==2.2.0
scikit-learn==1.3.2
matplotlib==3.8.1
seaborn==0.12.2
skorch==0.15.0
joblib==1.3.2
imbalanced-learn==0.12.0
ucimlrepo==0.0.3


setup_instruction: 

1 - extract all files from the zip folder
2 - change directory to the extracted folder, all test data, and saved models will be there
3 - in a VS Code terminal type the following command
        - python -m venv {name of your env} 
4 - once created activate with the following command 
        - .\{name of your env}\Scripts\activate
5 - now install required packages by entering the following command
        - pip install -r requirements.txt 
6 - finall enter the final command below
        - jupyter notebook testing.ipynb


source_data:

1 - the data is accessed through the script, but can be downloaded with the following link 
        - https://archive.ics.uci.edu/dataset/2/adult