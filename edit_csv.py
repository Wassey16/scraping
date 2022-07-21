import pandas as pd
# reading csv file 
df = pd.read_csv('data_file.csv')
# removing a column which has no data 
del (df['eightd_station_services'])
# renaming columns for beter under standing 
df.rename(columns = {'has_kiosk':'kiosk', 'station_id':'Station Id', 'external_id':'External Id','eightd_has_key_dispenser':'Dispenser', 'external_ielectric_bike_surcharge_waiverd':'Waiver', 'legacy_id':'Legacy Id', 'rental_uris':'Rental Uris', 'region_id':'Region Id','rental_methods':'Rental Methods', 'short_name':'Short Name','station_type':'Station Type'}, inplace = True)
# sorting and writing data into csv file 
x = df.sort_values(by=['capacity'], ascending=False)
x.to_csv('formated_csv.csv')
