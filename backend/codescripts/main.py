from utilities.db_util import get_db_connection
from utilities.general_utils import replace_dict_keys

def get_farmer_data(farmer_name):
    db = get_db_connection()
    try:
        cursor = db.cursor()
        sql_query = f"SELECT farmer_name,taluka,village,ans_q4_processed,ans_q5_processed,ans_q6_processed,ans_q7_processed,ans_q8_processed,ans_q9_processed,ans_q10_processed,ans_q13_processed,ans_q14_processed FROM farmer_data where farmer_name='{farmer_name}'"
        cursor.execute(sql_query)
        farmer_data = cursor.fetchall()[0]
        print(farmer_data)
        farmer_data = replace_dict_keys(farmer_data)
        return farmer_data
        # for e in farmer_data_1:
        #   for j in e.keys():
        #     print("'"+str(j)+"'"," : ",str(e[j]))
    finally:
        db.close()
