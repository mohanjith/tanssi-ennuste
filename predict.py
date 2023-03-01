# predict score based on band and place using mathematical models
# data in data/set-1.csv
# usage: python predict.py <place> <band> <favourite dancers %>

import sys
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# main function
def main():
    place = sys.argv[1]
    band = sys.argv[2]
    favouriteDancers = sys.argv[3]

    data = pd.read_csv('data/set-1.csv')
    data = data.drop(['Date'], axis=1)

    le = LabelEncoder()
    data['Place Index'] = le.fit_transform(data['Place'])
    data['Band Index'] = le.fit_transform(data['Band'])

    data = data.sample(frac=1)

    features = ['Favourite dancers %']
    prediction = [favouriteDancers]

    bdi = data.loc[data['Band'] == band]['Band Index']
    pdi = data.loc[data['Place'] == place]['Place Index']

    if bdi.empty:
        band_index = None
    else:
        band_index = bdi.iloc[0]
        features.append('Band Index')
        prediction.append(band_index)
    if pdi.empty:
        place_index = None
    else:
        place_index = pdi.iloc[0]
        features.append('Place Index')
        prediction.append(place_index)

    target = 'Score (%)'

    model = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=0)
    model.fit(data[features].values, data[target].values)

    print("Predicted score: %d" % model.predict([prediction])[0])

if __name__ == '__main__':
    main()