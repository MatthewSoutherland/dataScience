import numpy as np
import pandas as pd


def calculate_demographic_data():
    # Read data from file
    df = pd.read_csv("data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = len(df["race"].drop_duplicates())

    # What is the average age of men?
    avg_men = df[df["sex"] == "Male"]
    average_age_men = avg_men["age"].sum() / len(avg_men["age"])

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = len(df[df["education"] == "Bachelors"]) / len(
        df["education"]
    )

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[
        (df["education"] == "Bachelors")
        | (df["education"] == "Masters")
        | (df["education"] == "Doctorate"),
        ["education", "salary"],
    ]

    # What percentage of people without advanced education make more than 50K?
    lower_education = df.loc[
        (df["education"] != "Bachelors")
        & (df["education"] != "Masters")
        & (df["education"] != "Doctorate"),
        ["education", "salary"],
    ]
    lower_education_over = lower_education.loc[lower_education["salary"] == ">50K"]
    higher_education_over = higher_education.loc[higher_education["salary"] == ">50K"]

    # percentage with salary >50K
    higher_education_rich = len(higher_education_over) / len(higher_education)
    lower_education_rich = len(lower_education_over) / len(lower_education)
    print(higher_education_rich, lower_education_rich)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = None

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = None

    rich_percentage = None

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None

    # DO NOT MODIFY BELOW THIS LINE

    print_data = False
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
        )
        print("Country with highest percentage of rich:", highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    # return {
    #     "race_count": race_count,
    #     "average_age_men": average_age_men,
    #     "percentage_bachelors": percentage_bachelors,
    #     "higher_education_rich": higher_education_rich,
    #     "lower_education_rich": lower_education_rich,
    #     "min_work_hours": min_work_hours,
    #     "rich_percentage": rich_percentage,
    #     "highest_earning_country": highest_earning_country,
    #     "highest_earning_country_percentage": highest_earning_country_percentage,
    #     "top_IN_occupation": top_IN_occupation,
    # }

    return True


calculate_demographic_data()
