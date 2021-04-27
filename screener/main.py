

#  Used for launching all tasks, connects all modules of the app together, and parses data around.

from exchanges.exchanges import df_ex_baselist, extract_ex_details
from databases.database import db_conn, db_curs
from apis.apis import iex_api
import pandas as pd


#  Retrieves exchanges baselist fromm constants and stores it to the database
def store_baselist():
    df_ex_baselist().to_sql('ex_baselist', db_conn,
                            if_exists='replace', index=False)
    print('Exchanges baselist stored in database.')


#  Retrieves data from IEX Cloud for the exchanges in the baselist, and stores it in the database.
def retrieve_ex_data():
    #  Retrieves exchanges baselist from the database as a DataFrame.
    db_curs.execute('SELECT mic FROM ex_baselist')
    ex_baselist = pd.DataFrame(data=db_curs.fetchall(), columns=['mic'])

    #  Calls IEX Cloud API and retrieves their list of international exchanges details as a DataFrame.
    df_ex_details = pd.DataFrame(iex_api.internationalExchangesDF())

    #  Gets exchanges data for the baselist exchanges from the IEX Cloud exchanges data.
    extr_ex_data_df = extract_ex_details(ex_baselist, df_ex_details)

    #  Sends final IEX Cloud exchanges data for only the baselist exchanges to the database.
    extr_ex_data_df.to_sql('ex_data', db_conn,
                           if_exists='replace', index=False)

    print('Exchange data retrieved and stored.')


def run():
    choice = input('''
Choose one of the following options:

1. Refresh exchanges baselist in database.
2. Retrieve exchanges data from IEX Cloud.
3. Both of the above.
Type 1, 2, or 3.

''')
    if choice == '1':
        store_baselist()
    elif choice == '2':
        retrieve_ex_data()
    elif choice == '3':
        store_baselist()
        retrieve_ex_data()
    else:
        print('No choice was made. Terminating.')


if __name__ == "__main__":
    run()
    db_conn.close()
