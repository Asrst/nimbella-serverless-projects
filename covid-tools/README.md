## Covid Tools - Servelss Web App
- Provides somes tools which people can use to help themselves in times of Covid-19 panademic.

### Project file structure
The GitHub project has the file structure that Nimbella uses to intelligently deploy the project:
The [`packages`](./packages) directory contains the project's API implementations using python.
The [`web`](./web) directory contains the web content for the project.

### Notes on fact-check api:

Misinformation pertaining to COVID-19 is Rising along with confirmed cases. 
While some misinformation is related to vaccine or symptoms, there is also other irrelevant info spread by people in social media channels like FB, Insta & Youtube to increase their following.
The idea is to combat all of these by validating the information to maintain peace of mind.

It uses Google's Factcheck API in backend (still in Alpha)


### Notes on urgency-of-admission-check api:

With cases increasing day by day, High population countries like India are facing shoratages in available emergency beds.
And with private hospitals coming into play, they started money bidding on the available beds - Who can pay more money gets the admission first regardless of emergency.
Inorder to resolve, I built prototype of an automated system with help of ML Algorithm which rather classifies the urgency of admission based on their age, symptoms & gives them the preference.

Caution: ML Algorithms are only as good as data. This is just a working prototype with a small sample of aggregrated data, so dont except top-notch results.



### Notes on Covid Safety check & Help pages:

These currently work only on Indian Pincodes. They use MaymyIndia API's.

- Safety Check: Taking the pincode of your current location, it shows approx distance/nearby covid-contaminated zones.

- Help: This can show you Near by
  - Testing Labs.
  - Sample Collection Centers.
  - Quarantine Centers.
  - District hospitals.
  - Treatment Centers.