# Assignments
## FINNISH
## T1. file `departments.ipynb`
```
Lue employees.csv ja departments.csv tiedostot kahteen erilliseen pandas dataframeen. 
Otsikot ensimm�isell� rivill�, ja erotinmerkkin� pilkku (','). 
Tutki dataframeja spyderin Variable Explorer ikkunassa.

Tutustu dataan (describe, info, isnull, unique, nlargest, nsmallest)
Huom! Aina kun luetaan csv dataa, kannattaa katsoa, onko header vai ei. 
Nyt header (otsikot) on ensimm�isell� rivill�. Kokeile: header=None. 
Tutki dataframeja ja palauta header=0.

Yhdist� kaksi dataframea yhdeksi k�ytt�en pandas merge ominaisuutta. 
K�yt� inner-liitosta (how='inner'), ja tee liitos dep:n perusteella (on='dep'). 
T�m� on dataframe, jota jatkossa k�ytet��n.

Poista image sarake dataframesta
```

# T2. `departments.ipynb`
```
-   Laske montako ty�ntekij�� on dataframessa
-   Laske montako miest� (gender=0) ja naista (gender=1) on ty�tekij�iss�
-   Laske my�s em. prosenttiosuudet yhdell� desimaalilla
-   Laske ty�tekij�iden minimi, maksimi ja keskipalkka
-   Laske 'Tuotekehitys' osaston keskipalkka
-   Laske monellako ty�ntekij�ll� ei ole kakkospuhelinta (phone2)
-   Lis�� dataframeen uusi sarake: 'age', ja laske siihen jokaisen ty�ntekij�n ik� vuosina
-   Lis�� dataframeen uusi sarake: 'age_group', ja lis�� siihen jokaisen ty�ntekij�n ik�ryhm� seuraavasti: 
    ik�ryhm�t ovat viiden vuoden v�lein 15-70. Ik�ryhm�n arvo on 'alle X vuotta'. 
    Esim. 61 vuotias kuuluu ryhm��n alle 65 vuotta, ts. ik�ryhm�n arvo on 65 (kts. alla).
         
         age age_group
          61        65
          55        60
          51        55
          41        45
          44        45
          56        60
          65        70
          42        45
          64        65
          30        35
          36        40
          46        50
          35        40
          38        40
          51        55

Tee my�s uusi dataframe, johon otat vain salary, age ja gender kent�t mukaan. 
Luo korrelaatiomatriisi k�ytt�en pandasin corr-metodia. Visualisoi matriisi k�ytt�en seabornin heatmappia (annot=True)

Vaihdetaan aineistoja.
```

# T3. `titanic.ipynb`
```
-   Lataa Titanic csv tiedostot pythoniin pandas dataframeen (Titanic_data.csv, Titanic_names.csv)
-   Tulosta ipyhon consoliin dataframien info ja describe. 
    Tee histogrammi  df_titanic_data ( bins=4) dataframesta. 
    
-   Yhdist� dataframet (df_titanic_data, df_titanic_names) uudeksi dataframeksi df. 
    K�yt� how='inner' on='id'.
    
-   Montako henkil� on aineistossa?
-   Montako miest� ja naista on aineistossa?
-   Matkustajien keski-ik�?
-   Kuinka monta nollan ik�ist� matkustajaa?
```

# T4:`titanic.ipynb`
```
-   Huomataan, ett� on paljon nollan ik�isi� matkustajia. 
    Lasketaan ei-nollan ik�isten matkustajien keski-ik�, ja p�ivitet��n nollan 
    ik�isten matkustajien i�ksi t�m� laskettu keskiarvo

-   Tulosta yksik�sitteiset PClasses arvot. Output: ['1st' '2nd' '*' '3rd']
-   Etsi, kenen PClass on: *
-   Laske selviytyneiden ja ei-selviytyneiden lukum��r�. Tulosta arvot my�s prosentteina
-   Laske selviytyminen ja ei-selviytyminen miesten ja naisten kohdalla
```

# ENGLISH

# T1. `departments.ipynb`
```
Read the employees.csv and departments.csv files into two separate pandas dataframes. 
Headers on the first line, with a comma (',') as a delimiter. 
Examine the dataframes in spyder's Variable Explorer window.

Explore the data (describe, info, isnull, unique, nlargest, nsmallest)
Note! Whenever you read csv data, you should check if there is a header or not. 
Now the header is on the first line. Try: header=None. 
Check the dataframes and return header=0.

Merge the two dataframes into one using the pandas merge feature. 
Use inner join (how='inner'), and do the join based on dep (on='dep'). 
This is the dataframe that will be used in the future.

Remove the image column from the dataframe
```
# T2.  `departments.ipynb`
```
-   Calculate the number of employees in the dataframe
-   Count how many men (gender=0) and women (gender=1) are in the workforce
-   Calculate also the above percentages to one decimal place
-   Calculate the minimum, maximum and average wages of the workers
-   Calculate the average salary for the 'Product Development' department
-   Calculate how many employees do not have a second phone (phone2)
-   Add a new column to the dataframe: 'age', and calculate the age of each employee in years

-   Add a new column to the dataframe: 'age_group', and add the age group of each employee as follows 
    the age groups are every five years from 15 to 70. The value of the age group is 'less than X years'. 
    For example, a 61 year old belongs to the group under 65, i.e. the age group value is 65 (see below).
         
         age age_group
          61 65
          55 60
          51 55
          41 45
          44 45
          56 60
          65 70
          42 45
          64 65
          30 35
          36 40
          46 50
          35 40
          38 40
          51 55

Also create a new dataframe with only the salary, age and gender fields. 
Create a correlation matrix using the corr method of pandas. Visualise the matrix using the seaborn heatmap (annot=True)

Exchange the data.
```

# T3. `titanic.ipynb`
```
-   Upload Titanic csv files to python in pandas dataframe (Titanic_data.csv, Titanic_names.csv)
-   Print the info and describe of the dataframe to ipyhon console. 
      Make a histogram of the df_titanic_data ( bins=4) dataframe. 
      
-   Combine the dataframes (df_titanic_data, df_titanic_names) into a new dataframe df. 
      Use how='inner' on='id'.
      
-   How many persons are in the data?
-   How many men and women are in the data?
-   Average age of passengers?
-   How many passengers with age zero?
```

# T4:`titanic.ipynb`
```
-   Note that there are many passengers aged zero. 
    Calculate the average age of non-zero passengers, and update to zero. 
    as the age of the zero-age passengers.

-   Print the unique PClasses values. Output: ['1st' '2nd' '*' '3rd']
-   Find whose PClass is: *
-   Calculate the number of survivors and non-survivors. Output the values also as percentages
-   Calculate the survival and non-survival for males and females
```

