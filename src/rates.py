def CTR(df, column, value):
    '''Function to calculate click through rate using the number of clicks
    and total amount of visits'''
    
    #clicks
    clicks = df[(df[column] == value)][column].count()
    #total visits
    visits = df.shape[0]
    
    return round((clicks/visits)*100,2)