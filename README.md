# Crimes in Atlanta in the midst of COVID-19 Pandemic

## Proposal
The purpose of this analysis is to examine crimes in Atlanta and the impact it had from COVID-19 pandemic.
### Questions to answer  
How did the COVID-19 impacted the crime rate and the different types of crimes? 

## Datasets and Limitation
### Atlanta Crime Dataset
The source for the Atlanta crime dataset is from the the Atlanta Police Department website. There were total of four datasets from the website:
  - COBRA-2009-2019 (Updated 1_9_2020)
  - COBRA-2020-OldRMS-09292020 (Corrected 11_25_20)
  - COBRA-2020 (NEW RMS 9-30 12-31)
  - COBRA-2021 (Updated 11_18_2021)

Atlanta Police Department uses Uniform Crime Report (UCR) program to report crime statistics.

The biggest limitation in these dataset were the breakdown and the inconsistent of crimes categories and codes along the datasets. 

For the consistency of all the datasets and the file size limitations, I will only be analyzing from year 2016-2021 and the crime categories I will be analyzing are the following: Aggravated assault, auto theft, burglary, homicide, larceny from vehicle, larceny from non vehicle, manslaugther, and robbery. 

Since 2021 is not over, the dataset I was able to obtain was up to November 18, 2021.

I will be using the occur date of incident rather than the report date to get a clearer representation of the COVID 19 impact on crimes.

### UCR Crime Categories Definition
These are the definitions of the crime types according to UCR.

- Aggravated assault- Attack by one person upon another with the purpose of inflicting severe or aggravated bodily injury.
- Auto theft- Attempted theft or theft of a motor vehicle.
- Burglary- Unlawful entry of a structure to commit a felony or theft. 
- Homicide- Willful killing of one human being by another.
- Larceny from vehicle- Theft of articles from a motor vehicle or the theft of any part or accessory either interior or exterior of a motor vehicle.
- Larceny from non vehicle- Attempted theft or theft of property from the possession of another such as shoplifting, pocket‐picking, purse‐snatching,  bicycle thefts, and so forth, in which no use of force, violence, or fraud occurs.
- Manslaugther- Unlawful killing through negligence or that doesn't involve malice intention.
- Robbery- Taking or attempting to take anything of value from the care, custody, or control of a person or persons by force or threat of force or violence and/or by putting the victim in fear.

### COVID-19 Pandemic in 2020
- Dec 2019 - Coronavirus disease 2019 (COVID-19) official outbreak.
- Jan 20 2020 - First confirmed case in United States in Washington state.
- Mar 2 2020 - First two confirmed cases were from two residents of culton County which Atlanta, the capital of Georgia, is under.
- Mar 15 2020 - Atlanta city-wide state of emergency
- Mar 23 2020 - Atlanta mayor Bottoms signed a 14-day stay-at-home order to direct all city residents to stay at home except for performing essential tasks
- Apr 8 2020 - GA Governor Kemp extended the statewide shelter in place order through the end of April
- Apr 24 2020 - Georgia businesses start to reopen

The COVID-19 dataset source is from Georgia Department of Public Health.

## Data Analysis and Observations

![Covid daily graph](https://user-images.githubusercontent.com/93147265/143073147-510f261d-31bc-4f80-9bae-39d35e6e7478.png)
![Covid monthly chart](https://user-images.githubusercontent.com/93147265/143072618-5d1e9f43-df5d-4e5e-a971-72b9d43e1de5.png)

Observations:
- From March 15, when city-wide state of of emergency was announced and the lockdown that followed til end of April, the cases stayed somewhat stagnant. 
- The start of a steep incline of cases was not until mid to late June and the first peak of the wave was in July.
- The start of second wave was in October and reaches new height of number of cases throughout the rest of the year.


![Crimes in 2020](https://user-images.githubusercontent.com/93147265/143081784-4b4543b0-2877-45d7-98ce-d3c9bcaab599.png)
![Total Crimes 2020 monthly bar chart](https://user-images.githubusercontent.com/93147265/142947180-e407505a-2883-4618-906e-bf0aea50310f.png)
![Total Crimes 2019 monthly bar chart](https://user-images.githubusercontent.com/93147265/143162836-2fe3c6e1-7207-4919-bf82-01bf2724f027.png)

Observations:
- The first six months of 2020, there is a downward trend of number of crimes.
- There is a sharp drop of crimes when state of emergency was announed.
- Starting May, as businesses open up, there is upward trend of crimes
- A huge outlier/peak is due to the George Floyd protest. Although the protest started peacefully, it quickly turned violent.
- According to the Atlanta Police Department, 71 arrests were made by the morning of May 30.
- The crimes flattens from June to September and the crimes increases from October til the end of the year.
- January and February 2020 crime numbers are higher than 2019, but drastically lower during the months from April til September.
- However from October to December, 2020 crime numbers are higher again than previous year.

### Comparing Crimes in 2020 with previous 4 years (2016-2019)
![Total Crimes 2016-2020 bar chart](https://user-images.githubusercontent.com/93147265/142947185-64c2605a-aa32-4387-a156-91d745da7d2d.png)

Observations:
- From this graph, we can see that the total crimes in Atlanta is decreasing every year since 2016.
- Therefore it is hard to pinpoint if COVID-19 had an impact in decreasing crimes overall but we can make a logical assumption that COVID-19 lockdown may have contributed to a steeper decrease in crimes overall.


### Comparing the types of Crimes
![image](https://user-images.githubusercontent.com/93147265/143252489-8edd1356-206d-4961-86f8-026d91da444d.png)

Observations: 
- Robbery, burglary, both larceny, and auto theft decrease in counts during March.
- Aggravated assault and homicide has risen during March.
- All crimes starts to rise in April to May.
- Homicide has an irregular pattern.



| Crime Categories | 4-year AVG (2016-2019) | 2020 | Diff | % Diff |
| --- | --- | ---| --- | ---- |
| Burglary	| 3406.75	| 2102.0	| -1304.75	| -38.298965 |
| Robbery	| 1350.75	| 884.0	| -466.75	| -34.554877 |
| Larceny non vehicle	| 6399.75	| 4722.0	| -1677.75	| -26.215868 |
| Larceny from vehicle	| 9910.00	| 8625.0	| -1285.00	| -12.966700 |
| Auto theft	| 3311.75	| 3275.0	| -36.75	| -1.109685 |
| Aggravated assault	| 2023.75	| 2340.0	| 316.25	| 15.626930 |
| Homicide	| 98.00	| 145.0	| 47.00	| 47.959184 |
| Manslaugther	| 0.75	| 2.0	| 1.25	| 166.666667 |
| Total	| 26501.50	| 22095.0	| -4406.50	| -16.627361 |

Observations:
- Most types of crime events have declined in 2020 compared to the previous 4-year.
- Burglary dropped 38%, robbery dropped 34%, larceny non vehicle dropped 26%, larceny from vehicle dropped 12%.
- There are some noticeable increases in some categories: Aggravated assault, homicide, and manslaughter increased in 2020.
- Manslaugther had increased by 166% however it is important to note that the actual number is only 2 counts in 2020.

### The big trend in Crimes from 2016-2021
![Crimes 2016-2021 Graph](https://user-images.githubusercontent.com/93147265/142972524-4bf2536d-eaf1-4d91-9b5d-2cb45914cff7.png)

Observations:
- There is a seasonality related trend to overall crimes.
- Overall crimes are lower during the first quarter of year compared to the last quarter.
- Crimes drop during the first quarter and start increasing throughout the year.
- From 2016-2021, crimes was lowest during the lockdown in 2020.
- Although the lowest point was in 2020, crimes increased after the lockdown regardless of the increased in COVID-19 cases.
- The steep drop in crime during the lockdown is followed by a steep rise in crime beginning in the summer and the winter in 2020. 

## Conclusion
How did the COVID-19 impacted the crime rate and the different types of crimes? 

It is unclear as there is no clear correlation between the number of COVID-19 cases and crimes.

Although a very reasonable explanation for the overall drop in crimes was due to the COVID-19 lockdown. 

Since all crimes dropped during the month March.

Some logical hypothesis for why the pandemic would have driven down burglary, robbery, and larceny:
- More people were are home, fewer people were on the street, and many businesses were closed during the lockdown.
- Less opportunies to commit burglaries, robberies and larcenies.

However after the end of lockdown, crimes have increased rapidly and homicides and aggravated assault is higher than previous years.

With better dataset, I would like to investigate the reasons why aggravated assault and homicide on the other hand increased. I would like to see if domestic abuse may have caused aggravated assault to increase during the lockdown.

Also once 2021 is over, I would like to compare 2021 dataset with 2020, to see how the crime trend in 2021 changed compared to 2020 and 2016-2019.
