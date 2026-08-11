import pandas as pd, os

os.mkdir('yearly_files')

def generate_year_files():

  surveys_df = pd.read_csv('surveys.csv')

  unique_years = surveys_df['year'].unique()

  for year in unique_years:

    if year >= 1990 and year <= 2000:

      yearly_data = surveys_df[surveys_df.year == year]

      file_name = 'yearly_files/survey_'+str(year)+'.csv'

      yearly_data.to_csv(file_name)

  return 'Done exporting csv files'

def display_year_file_names():

  file_names = os.listdir('yearly_files')

  for name in file_names:

    print(name)
