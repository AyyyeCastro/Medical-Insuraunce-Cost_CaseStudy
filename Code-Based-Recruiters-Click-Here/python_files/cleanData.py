### Import Library ###
import pandas as pd

### insert csv into the pandas dataframe
df = pd.read_csv('raw_csv\insurance.csv')


### Function Dictionary

def getAverageCostByGender():
    averages = df.groupby('gender')['charges'].mean()
    averageByGender_df = averages.reset_index()
    averageByGender_df.to_csv('manipulated_csv/average_charges_by_gender.csv', index=False)

def getAverageBMIByGender():
    averages = df.groupby('gender')['bmi'].mean()
    averageBMIByGender_df = averages.reset_index()
    averageBMIByGender_df.to_csv('manipulated_csv/average_BMI_by_gender.csv', index=False)

def getGenderRegionRate():
    regionCounts = df.groupby('gender')['region'].value_counts()
    genderRegionCounts_df = regionCounts.reset_index()
    genderRegionCounts_df.to_csv('manipulated_csv/region_count_by_gender.csv', index=False)

def getSmokerGenderRate():
    smokers_df = df[df['smoker'] == 'yes']
    genderSmokerCount = smokers_df['gender'].value_counts()
    genderSmokerCount_df = genderSmokerCount.reset_index()
    genderSmokerCount_df.to_csv('manipulated_csv/smoke_count_by_gender.csv', index=False)
    
def getSmokerRegionRate():
    smokers_df = df[df['smoker'] == 'yes']
    genderSmokerCount = smokers_df['region'].value_counts()
    genderSmokerCount_df = genderSmokerCount.reset_index()
    genderSmokerCount_df.to_csv('manipulated_csv/smoke_count_by_region.csv', index=False)

def getNonSmokerRegionRate():
    smokers_df = df[df['smoker'] == 'no']
    genderSmokerCount = smokers_df['region'].value_counts()
    genderSmokerCount_df = genderSmokerCount.reset_index()
    genderSmokerCount_df.to_csv('manipulated_csv/Non_smoker_count_by_region.csv', index=False)

def getAverageChildCountByGender(): 
    averages = df.groupby('gender')['children'].mean()
    averageByGender_df = averages.reset_index()
    averageByGender_df.to_csv('manipulated_csv/average_child_count__by_gender.csv', index=False)

def getAverageCostByChildCount(): 
    averages = df.groupby('children')['charges'].mean()
    averageByGender_df = averages.reset_index()
    averageByGender_df.to_csv('manipulated_csv/average_charges_by_child_count.csv', index=False)

def getAverageCostByRegion():
    averages = df.groupby('region')['charges'].mean()
    averageByRegion_df = averages.reset_index()
    averageByRegion_df.to_csv('manipulated_csv/average_charges_by_Region.csv', index=False)


### Run Functions 

# getAverageCostByGender()
# getAverageBMIByGender()
# getSmokerGenderRate()
# getGenderRegionRate()
# getSmokerRegionRate()
# getAverageChildCountByGender()
# getAverageCostByChildCount()
# getAverageCostByRegion()
# getNonSmokerRegionRate()