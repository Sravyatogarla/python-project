#Python Project

This repository contains multiple Python exercises focusing on data analysis, Pandas, and Jupyter notebooks. Each problem statement is solved in a separate Jupyter notebook, along with real-world datasets.

Project Structure
bash
Copy
Edit
/Python_Project/

│── README.md  

│── .gitignore 

│── Dataset/

│   ├── top50spotify.csv # Dataset of 50 Spotify songs

│   ├── cereal.csv    # Dataset of cereals and manufacturers

│── Notebooks/

│   ├── Problem_1_Spotify.ipynb   # Analysis of Spotify songs dataset

│   ├── Problem_2_Pandas_Series.ipynb # Creating and manipulating Pandas series

│   ├── Problem_3_Multiples_7_17.ipynb # Generating series with multiples

│   ├── Problem_4_Cereal_Analysis.ipynb  # Cereal dataset visualization

│── requirements.txt        # Required Python libraries

│── LICENSE  # License details

Datasets
1. Spotify Songs Dataset (top50spotify.csv)
Description: Contains 50 top songs from Spotify with multiple attributes.

Columns:

SerialNo. - Serial number of the song
TrackName - Name of the track
ArtistName - Name of the artist
Genre - Genre of the song
Energy - Energy index of the song
Length - Length of the song
Popularity - Popularity score
3. Cereal Dataset (cereal.csv)
Description: Contains details of various cereal brands and their manufacturers.

Columns:
name - Brand name of the cereal
MFR - Manufacturer of the cereal
rating - Quality rating of the cereal
Notebook Descriptions
1. Problem 1 - Spotify Songs Analysis (Problem_1_Spotify.ipynb)
2. 
Objective: Analyze Spotify's top 50 songs dataset to extract insights.
Tasks Performed:

✔ Import the dataset and drop unnecessary columns

✔ Calculate the average Energy and Length of the first 10 songs

✔ Group songs by Genre and calculate total length

✔ Identify the artist with the most tracks in a single genre

3. Problem 2 - Pandas Series (Problem_2_Pandas_Series.ipynb)
4. 
Objective: Create and manipulate Pandas Series from a dictionary.

Tasks Performed:

✔ Convert the given dictionary into Pandas Series

✔ Handle missing values by replacing them with zeros

✔ Transpose the DataFrame and calculate the average for each subject

6. Problem 3 - Series of Multiples (Problem_3_Multiples_7_17.ipynb)
7. 
Objective: Generate a Pandas Series from 1 to 1000 and extract numbers divisible by 7 and 17.

Tasks Performed:

✔ Create a range of numbers from 1 to 1000

✔ Filter numbers divisible by both 7 and 17

✔ Convert the filtered values into a new Pandas Series

9. Problem 4 - Cereal Data Analysis (Problem_4_Cereal_Analysis.ipynb)
10. 
Objective: Visualize cereal quality based on manufacturer ratings.

Tasks Performed:

✔ Import the dataset and clean data if necessary

✔ Plot ratings for different manufacturers

✔ Use ticks to standardize rating range from 0-100

✔ Apply Seaborn styling for better visualization

Requirements
To run this project, install the required libraries using:

bash
Copy
Edit
pip install -r requirements.txt
Main Libraries Used:

pandas
numpy
matplotlib
seaborn
How to Use This Repository
Clone the repository:
bash
Copy
Edit
git clone https://github.com/YourUsername/Python_Project.git
Navigate to the project directory:
bash
Copy
Edit
cd Python_Project
Open Jupyter Notebook:
bash
Copy
Edit
jupyter notebook
Run the required notebook inside the Notebooks/ folder.
