from dataPreparation import data_preparation


def data_cleaning():

    df_rent, df_house_price, df_rent_price = data_preparation()

    # rename the columns
    df_house_price.rename(columns={"Unnamed: 0": "country"}, inplace=True)
    df_rent_price.rename(columns={"Unnamed: 0": "country"}, inplace=True)

    # there are NaN, we replace them with 0
    df = df_rent.fillna(0)
    df_house_price = df_house_price.fillna(0)
    df_rent_price = df_rent_price.fillna(0)

    # renaming columns
    df.rename(columns = {'textdata':'text-data', 'desktophidden2':'desktop-hidden 2', 'desktophidden4':'desktop-hidden 4',}, inplace = True)

    # create a new column with the country name by taking the last word of the column 'title'
    splitted = df['title'].str.split()
    df['country'] = splitted.str[-1]
    df['country'].replace({'Republic':'Czech Republic'}) # replace the 'Republic' with 'Czech Republic'

    # drop useless columns
    df.drop(columns=['title'], inplace=True)
    df.drop(columns=['text-data'], inplace=True)

    # rename the columns and replace 'Not specified' prices with 0
    df.rename(columns={"desktop-hidden 2": "price", "desktop-hidden 4": "surface"}, inplace=True)

    # normal replace not working so, replace the ',' with '' in the long way
    df['price'] = df['price'].astype(str)
    df['price'].replace({'0,':'0'}, regex=True, inplace=True)
    df['price'].replace({'1,':'1'}, regex=True, inplace=True)
    df['price'].replace({'2,':'2'}, regex=True, inplace=True)
    df['price'].replace({'3,':'3'}, regex=True, inplace=True)
    df['price'].replace({'4,':'4'}, regex=True, inplace=True)
    df['price'].replace({'5,':'5'}, regex=True, inplace=True)
    df['price'].replace({'6,':'6'}, regex=True, inplace=True)
    df['price'].replace({'7,':'7'}, regex=True, inplace=True)
    df['price'].replace({'8,':'8'}, regex=True, inplace=True)
    df['price'].replace({'9,':'9'}, regex=True, inplace=True)

    df['surface'].replace({'0,':'0'}, regex=True, inplace=True)
    df['surface'].replace({'1,':'1'}, regex=True, inplace=True)
    df['surface'].replace({'2,':'2'}, regex=True, inplace=True)
    df['surface'].replace({'3,':'3'}, regex=True, inplace=True)
    df['surface'].replace({'4,':'4'}, regex=True, inplace=True)
    df['surface'].replace({'5,':'5'}, regex=True, inplace=True)
    df['surface'].replace({'6,':'6'}, regex=True, inplace=True)
    df['surface'].replace({'7,':'7'}, regex=True, inplace=True)
    df['surface'].replace({'8,':'8'}, regex=True, inplace=True)
    df['surface'].replace({'9,':'9'}, regex=True, inplace=True)

    # remove not valid data
    df = df[df['price'] != "Not specified"]
    df = df[df['surface'] != 0]
    df = df[df['price'] != 0]


    #convert all the prices to € and remove the 'EUR'

    # CHF, DKK, PLN, SEK, CZK, BGN, HUF, RON, Iceland
    # create multiplier for the prices
    multiplier = {'EUR': 1, 'CHF': 1, 'DKK': 0.13, 'PLN': 0.21, 'SEK': 0.09, 'CZK': 0.04, 'BGN': 0.51, 'HUF': 0.0025, 'RON': 0.2, 'ISK': 0.0072, 'NOK': 0.096}

    prices = []
    for price in df['price']:
        if price.find('EUR') != -1:
            price = price.replace('EUR', '')
            price = float(price) * multiplier['EUR']
        elif price.find('CHF') != -1:
            price = price.replace('CHF', '')
            price = float(price) * multiplier['CHF']
        elif price.find('DKK') != -1:
            price = price.replace('DKK', '')
            price = float(price) * multiplier['DKK']
        elif price.find('PLN') != -1:
            price = price.replace('PLN', '')
            price = float(price) * multiplier['PLN']
        elif price.find('SEK') != -1:
            price = price.replace('SEK', '')
            price = float(price) * multiplier['SEK']
        elif price.find('CZK') != -1:
            price = price.replace('CZK', '')
            price = float(price) * multiplier['CZK']
        elif price.find('BGN') != -1:
            price = price.replace('BGN', '')
            price = float(price) * multiplier['BGN']
        elif price.find('HUF') != -1:
            price = price.replace('HUF', '')
            price = float(price) * multiplier['HUF']
        elif price.find('RON') != -1:
            price = price.replace('RON', '')
            price = float(price) * multiplier['RON']
        elif price.find('ISK') != -1:
            price = price.replace('ISK', '')
            price = float(price) * multiplier['ISK']
        elif price.find('NOK') != -1:
            price = price.replace('NOK', '')
            price = float(price) * multiplier['NOK']
        else:
            price = float(price)
        prices.append(price)
    df['price'] = prices

    # clean the column 'surface'
    df['surface'].replace({' m2':''}, regex=True, inplace=True)
    df['surface'] = df['surface'].astype(float)

    # calculate the index for every apartment
    df['index'] = df['price']/df['surface']

    # remove ousiders
    df = df[df['index'] < 1000]

    # write the new dataframe to a csv file
    df.to_csv('result.csv', sep='\t')

    return df, df_rent_price, df_house_price