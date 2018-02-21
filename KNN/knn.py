# knn
# Created by JKChang
# 20/02/2018, 22:45
# Tag:
# Description: 
import numpy as np
import pandas as pd

features = [
    'accommodates', 'bedrooms', 'bathrooms', 'beds', 'price', 'minimum_nights',
    'maximum_nights', 'number_of_reviews'
]
dc_listings = pd.read_csv('listings.csv')[features]
dc_listings['price'] = dc_listings['price'].str.replace("\$|,", '').astype(float)

train_df = dc_listings.copy().iloc[:2792]
test_df = dc_listings.copy().iloc[2792:]


def predict_price(new_listing_value, feature_column):
    print(new_listing_value)
    temp_df = train_df
    temp_df['difference'] = np.abs(dc_listings[feature_column] - new_listing_value)  # difference
    temp_df = temp_df.sort_values('difference')  # sort according to the difference
    knn_5 = temp_df.price.iloc[:5]
    predicted_price = knn_5.mean()  # mean value of 5 nearest ones
    return (predicted_price)


test_df['predicted_price'] = test_df.accommodates.apply(predict_price, feature_column='accommodates')

