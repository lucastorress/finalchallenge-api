def convert_ISO8601_to_normal(date):
    full_date = date.split('-')
    day = full_date[2][:2]
    month = full_date[1]
    year = full_date[0]

    return f'{day}/{month}/{year}'

def convert_normal_to_ISO8601(date):
    date_ISO8601 = 'T12:00:00-03:00'
    date_input = date.split('/')
    day = date_input[0]
    month = date_input[1]
    year = date_input[2]

    return f'{year}-{month}-{day}{date_ISO8601}'

if __name__ == "__main__":
    date_ISO8601 = '2017-09-24T21:07:40-0300'
    print(convert_ISO8601_to_normal(date_ISO8601))
    date = '25/12/2017'
    print(convert_normal_to_ISO8601(date))
