import data
from build_data import CountyDemographics





def population_total(counties:list[CountyDemographics]) -> int:
    return sum(county.population['2014 Population'] for county in counties)
#part2


def filter_by_state(county_list: list[data.CountyDemographics], state_abbr: str) -> list[data.CountyDemographics]:
        filtered_counties = [county for county in county_list if county.state == state_abbr]

        return filtered_counties

#part3
def population_by_education(county_list: list[data.CountyDemographics], education_key: str) -> float:
    total_population = 0
    for county in county_list:
        if education_key in county.education:
            total_population += county.education[education_key]
    return total_population

def population_by_ethnicity(county_list: list[data.CountyDemographics], ethnicity_key: str) -> float:
    total_population = 0
    for county in county_list:
        if ethnicity_key in county.ethnicities:
            total_population += county.ethnicities[ethnicity_key]
    return total_population

def population_below_poverty_level(counties:list[data.CountyDemographics]) -> float:
    return sum(county.population['2014 Population'] * county.income.get('Persons Below Poverty Level', 0) /100 for county in counties)

#part4
def percent_by_education(county_list: list[data.CountyDemographics], education_key: str) -> float:
    # Get the total population for the specified education level
    education_population = population_by_education(county_list, education_key)
    # Get the total population across all counties
    total_population = population_total(county_list)
    # Calculate the percentage
    if total_population == 0:
        return 0
    return (education_population / total_population) * 100

def percent_by_ethnicity(county_list: list[data.CountyDemographics], ethnicity_key: str) -> float:
    # Get the total population for the specified ethnicity
    ethnicity_population = population_by_ethnicity(county_list, ethnicity_key)
    # Get the total population across all counties
    total_population = population_total(county_list)
    # Calculate the percentage
    if total_population == 0:
        return 0
    return (ethnicity_population / total_population) * 100

def percent_below_poverty_level(county_list: list[data.CountyDemographics]) -> float:
    # Get the total population below poverty level
    poverty_population = population_below_poverty_level(county_list)
    # Get the total population across all counties
    total_population = population_total(county_list)
    # Calculate the percentage
    if total_population == 0:
        return 0
    return (poverty_population / total_population) * 100

#part5
def education_greater_than(county_list: list[data.CountyDemographics], education_key: str, threshold: float) -> list[data.CountyDemographics]:
    return [county for county in county_list if county.education.get(education_key, 0) > threshold]

def education_less_than(county_list: list[data.CountyDemographics], education_key: str, threshold: float) -> list[data.CountyDemographics]:
    return [county for county in county_list if county.education.get(education_key, 0) < threshold]

def ethnicity_greater_than(county_list: list[data.CountyDemographics], ethnicity_key: str, threshold: float) -> list[data.CountyDemographics]:
    return [county for county in county_list if county.ethnicities.get(ethnicity_key, 0) > threshold]

def ethnicity_less_than(county_list: list[data.CountyDemographics], ethnicity_key: str, threshold: float) -> list[data.CountyDemographics]:
    return [county for county in county_list if county.ethnicities.get(ethnicity_key, 0) < threshold]

def below_poverty_level_greater_than(county_list: list[data.CountyDemographics], threshold: float) -> list[data.CountyDemographics]:
    return [county for county in county_list if county.income.get('Persons Below Poverty Level', 0) > threshold]

def below_poverty_level_less_than(county_list: list[data.CountyDemographics], threshold: float) -> list[data.CountyDemographics]:
    return [county for county in county_list if county.income.get('Persons Below Poverty Level', 0) < threshold]
