### Preprocessing of Bike Sharing Data
We got our bike sharing data from the bike sharing provider [Metro Bike Share](https://bikeshare.metro.net/), who already prepared and cleansed the data. We have to keep in mind this data preperation.  

In their [Trip Data document](https://bikeshare.metro.net/about/data/), they explain what kind of data cleansing they did: 

- Staff servicing and test trips are removed.
- Trips below 1 minute are removed.
- A "Virtual Station" listed in the checkout and return kiosks, is used by staff to check in or check out a bike remotely for a special event or in a situation in which a bike could not otherwise be checked in or out to a station.
- Trip lengths are capped at 24 hours.
- Some short round trips or long trips may be the result of system or user error, but have been kept in the dataset for completeness.

On the website of Metro Bike Share is also the [location of the stations](https://bikeshare.metro.net/stations/json/) available for download.

