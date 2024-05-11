# PharmaSymptom Guide

#### Video Demo: https://youtu.be/W66XacPU03g

#### Description:
The idea behind my final project is a virtual assistant that can provide personalized recommendations of over-the-counter solutions for some health concerns like the flu, smoking cessation and solar burn, based on some informations the users are asked to provide.
The app.py file contains code that directs users to the pages related to the health concern that they want to know about and also allows the users to navegate between the HTML pages that have the informations (medicines and non-pharmacological measures) related to the previously chosen health concern.

Inside the templates folder is possibile to find:
- layout.html: contains the HTML code of the layout of the project as well as the link to the libraries (bootstrap) and the css stylesheet (available inside the static folder), responsabile for the desing of the project.

- index.html: contains a brief descripton of the project's aim and allows the users to choose the health concern they are interested in knowing more information about.

- symptoms.html: presents a list of some of the most common flu symptoms, allowig the users to select the symptoms that they have in order to give information about the medicines that they could take to treat those symptoms.

- apology.html: this page renders an apology if the users don't pick any symptoms from the given list in the index.html page, explaining they must choose some symptom from the list.

- medicine.html: presents a table with the symptoms previously chosen at the symptoms.html page. The table has three columns: the symptoms column, the medicine column, that has the group of medicines used to treat the respective symptom, and the contraindications column, that has a list of the contraindications of that specific medicine, alerting the users who suffer from those contraindications to not take that medicine before talking to their physician or pharmacist. At the end of the page the users can find a button that will redirect them to the page of the non-pharmacological measures.

- measures.html: contains a list of some of the most important non-pharmacological measures that are essencial for a faster recovery.

- smoking_cessation.html: this page contains information of some options of Nicotine Replacement Therapy, alongside with information on how to take or apply them. It is also possible to find a button that will direct the users to the correct dosage to take according to the number of cigarettes they smoke a day (more or less than 20 cigarettes).

- dosage_more.html: the users will find information about the correct dosage to take of every option presented in the smoking_cessation.html page, if they smoke more than 20 cigarettes a day.

- dosage_less.html: the users will find information about the correct dosage to take of every option presented in the smoking_cessation.html page, if they smoke less than 20 cigarettes a day.

- measures_smoking.html: from the dosage_more.html and dosage_less.html pages, the users will be able to go to the non-pharmacological measures page. In this page they will find measures that taken alongside the use of Nicotine Replacement Therapy will highly increase their chances of breaking this habit and quit smoking.

- solar_burn.html: the solar_burn.html page presents a table with the medicines the users should take according to the symptoms they have developed after the solar burn. As happens with the others health concerns, there will be a button allowing the users to look up some non-pharmacological measures.

- measures_solarburn.html: in this page the users will find some non-pharmacological measures used in solar burns to make the recovery faster.
