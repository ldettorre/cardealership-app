# Moderna Motors - A Car Dealership App

## Fullstack Django Project
###### This project is intended for educational purposes only.


## Description

‘Moderna Motors’ is a car dealership site that resulting from my joy of building apps and my passion for cars. I noticed many independent dealerships across Ireland use a default style that comes from being associated with a popular Irish network and so I set myself the challenge to build a full stack version complete with features that would aid a running business. 

## UX and UI

Part of the challenge I set myself when building this site was to try and mimic the UX and UI that can be seen used by independent car dealerships that have their site powered by Carzone.ie. The reason I went this route was because while many have their own style or twist, they still follow a core pattern and this was something I wanted to try and replicate.

Users have everything easily accessible to them right from the beginning of the landing page. Links are self explanatory and the search feature only renders Makes, relevant Models and available Years. This means as far as the first 3 fields, Users will only see what is available and not have empty searches. However this does not expand to the rest of the search fields just yet. Something I opted to do differently over the other dealer sites was to have an in-depth search form available from the get go as opposed to just 3 or 4 fields.

Regarding the Contact page, this is fully loaded with email, address, phone number, Google Map and custom contact form but unlike the sites I was working from, I created a less congested format without sacrificing on details or readability.

The Vehicles page and single view Vehicle page were both heavily inspired from the aforementioned sites down to the image formatting with carousels and car detail grid with icons.

The Landing Page however is where I decided to take inspiration from main dealerships that invest more in advertising their services as opposed to independents. To help with this I used a template from Themeforest. 


### Technologies Used For This Project
* HTML
* CSS
* Bootstrap Version 4.5.2
* Javascript and Jquery
* Python 3.8.2
* Django 3.1.4
* Heroku - Deployment
* Postgresql Database

## Features

### Existing Features

#### Site Specific:
- The Custom Dynamic Search Function 
    - My main goal for the Search Feature was to have it only render inventory that is available on the site while also only render options that were related to the previous selection. For example, if the User chose Audi as the 'Make' then only Audi models, that were also listed on the site as an ad, would be rendered in the 'Models' field. Then upon selecting a 'Model', the Year field would perform the same process. After researching how to go about creating this from scratch, I found that is was also referred to as 'dependent' by some.

- Contact/Car Sourcing Form Notification Email
    - When the User submits either of these forms, they create an entry that can be seen in the Django dashboard however the site also emails the Admin or Owner to notify them of the new submission. Currently, the Contact Form adds the Users submitted information to help facilitate a faster response as opposed to then needing to have the admin/owner sign into the dashboard, find the entry and action it.

- Subscriber Form
    - The Subscriber Form takes the Users email, creates an entry within the dashboard and then also emails the User, using the email provided, to inform them that they are now subscribed to the site's newsletter. 

- Mobile Responsive
    - As with all modern sites, having it be mobile responsive was a must and so thanks to Bootstrap, the site looks very well right down to mobile devices with smaller screens.



#### As the Site Admin:

- Export Dashboard Data To CSV
    - The Contact app's admin file contains a custom function called 'export_data' which allows the admin/owner to download all the objects data to a CSV file. This was something I loved to create as I imagined myself as the owner and having the ability to download everything for review or processing seemed immensely valuable.

- Listing Upload
    - The Admin of the site can easily upload a new listing within minutes which includes upto 10 images.

- Featured/Publihsed Options
    - The Admin can choose which listings to promote on the landing page via the 'Featured' field. They can also choose to hide certain listings via the 'is_published' field allowing them keep in the backend but not publically available for whatever reason.

- User Creation
    - As this is a Django App, the Admin can easily create new users or Staff (not a custom model yet) via the dashboard allowing them a range of C.R.U.D. permissions.



### Features Left to Implement
- Subcriber Unsubscribe Feature
    - I'd like to try and implement a way for Users to click a link in their confirmation email allowing them to unsubscribe to the site. While I could create a way for them to enter the email in a form on the site and remove them from the listing or db entirely, this would have issues in the real world where anyone could try mass unsubscribe people. So one method of working around this could be to generate a key upon subbing and authenticate that key through an unsub view that is called via an 'unsubscribe' url.


## Deployment and Hosting
The steps provided assume that you have forked the repository to your GitHub already and have knowledge on setting up a storage bucket via AWS S3.

1. Sign into Heroku, click new in the top right hand of the page and click on create app.
2. Provide an app name, select the region relevant to you then click 'create'.
3. Within the Deploy tab of your app dashboard, locate ‘Deployment Method’ and select GitHub. You will then need to enter the app name and select it.
4. Within the Resources of the dashboard, you will need to scroll to ‘Add-ons’ and enter ‘Heroku Postgres’. Ensure that you select the ‘Hobby Dev - Free’ Tier.
5. You will then need to locate the Settings tab and scroll down to 'Config Vars' where you will enter the project ‘config vars’ or ‘environment variables’.
    - These are the AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME, DATABASE_URL, DJANGO_SETTINGS_MODULE, EMAIL_ADDRESS, EMAIL_PASSWORD, EMAIL_PORT, PGHOST, PGNAME, PGPASSWORD, PGUSER, and SECRET_KEY.
    - Regarding the email password, if you are using Gmail and have 2-factor authentication enabled then you will need to go to thr Security section of your account and generate an app password.

Note that we did not set a DEBUG config var as this will default to False as seen in the base.py file.

Once the above has been completed you can return to the Deploy tab, scroll down to ‘Manual Deploy’ and click ‘Deploy Branch’. Should you encounter any issue, I would recommend then consulting the log by returning to the app dashboard within Heroku, clicking on 'More' in the top right and selecting 'View Logs'. You may need to redeploy the app with the log opened in order to see an entire account of what happened. While you could create a config var called DEBUG and set it to True in order to receive any 'yellow page errors', please ensure you remember to remove it when you're done.





