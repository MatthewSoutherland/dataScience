import numpy as np
import pandas as pd


def calculate_demographic_data():
    # Read data from file
    df = pd.read_csv("data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts().to_list()

    # What is the average age of men?
    avg_men = df[df["sex"] == "Male"]
    average_age_men = round(avg_men["age"].sum() / len(avg_men["age"]), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(
        len(df[df["education"] == "Bachelors"]) / len(df["education"]) * 100, 1
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
    higher_education_rich = round(
        len(higher_education_over) / len(higher_education) * 100, 1
    )

    lower_education_rich = round(
        len(lower_education_over) / len(lower_education) * 100, 1
    )

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df["hours-per-week"] == 1]
    num_min_work_rich = num_min_workers.loc[num_min_workers["salary"] == ">50K"]

    rich_percentage = len(num_min_work_rich) / len(num_min_workers) * 100

    # What country has the highest percentage of people that earn >50K?
    country_count = df["native-country"].value_counts()
    country_rich_count = df[df["salary"] == ">50K"]["native-country"].value_counts()

    highest_earning_country = (country_rich_count / country_count * 100).idxmax()

    highest_earning_country_percentage = round(
        (country_rich_count / country_count * 100).max(), 1
    )
    print(highest_earning_country_percentage)

    # Identify the most popular occupation for those who earn >50K in India.
    people_in_india = df[df["native-country"] == "India"]
    job_counts = people_in_india[people_in_india["salary"] == ">50K"][
        "occupation"
    ].value_counts()

    top_IN_occupation = job_counts.idxmax()
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
