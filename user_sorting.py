import pandas as pd
import dbConnect as db
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
import time
   

class Sorting_User():
    def __init__(self):
        self.index = None
        self.user_id = None
        self.vektorler = None
        self.model = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased')
        self.connection = None
    

    def load_data(self):
        start = time.time()
        veri = np.load("user_vektor.npz",allow_pickle=True)
        self.user_id = veri["id"]
        self.vektorler = veri["vektor"]
        self.vektorler = self.vektorler.astype("float32")

        dimension = self.vektorler.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(self.vektorler)
        print("load_data harcana  süre", time.time() - start)


    def search(self,keyword,k=10):
        start = time.time()
        print(keyword)
        keyword_vektor = self.model.encode(keyword).astype("float32")
        D,I = self.index.search(np.expand_dims(keyword_vektor,axis=0),k)

        id_list = []
        self.connection = db.connect()
        cursor = self.connection.cursor()
        print(I)
        print(D)
        for i in range(k):
            if 1:
                user_index = I[0][i]
                cursor.execute(f"select fullname from [user] where id = '{self.user_id[user_index]}'")
                uss = cursor.fetchall()
                id_list.append(self.user_id[user_index])
                print("isim",uss)


        print("search harcana  süre", time.time() - start)
        self.connection.close()
        return id_list
    
    def update(self,userid):
        try:
            start = time.time()
            self.connection = db.connect()
            query = f"""select table1.username, table1.fullname , table2.talent, table1.id
from [user] as table1
inner join user_detail as table2 on table1.id = table2.id and table1.id = '{userid}'
"""
            df = pd.read_sql(query, self.connection)
            user_find = np.where(self.user_id ==userid)[0][0]
            new_vektor = self.model.encode(f"ÖNEMLİ İSİM : {df['fullname']}, tam ismi :{df['fullname']} yetenekleri : {df["talent"]}")
            self.vektorler[user_find]  = new_vektor
            np.savez('user_vektor.npz', id=self.user_id,vektor=self.vektorler)
            self.connection.close()
            print("update harcana  süre", time.time() - start)
            return {"code":"0x202","mess":"suceessfull"}
        except Exception as e:
            return {"code":"404","mess":f"güncellenemdi {e}"}
        


    def create(self):
        try:
            start = time.time()
            self.connection = db.connect()
            query = """select table1.username, table1.fullname , table2.talent, table1.id
 from [user] as table1
inner join user_detail as table2 on table1.id = table2.id
"""
            df = pd.read_sql(query,self.connection)
            df["text"] = df.apply( lambda row: f"kullanıcı adı:{row['username']}, ÖNEMLİ İSİM :{row['fullname']} ,yetenekleri : {row["talent"]}",axis=1)
            text_vektors = self.model.encode(df['text'].to_list())
            # normalized_vektors = normalize(text_vektors, axis=1)  

      
            self.vektorler = text_vektors

            self.user_id = df["id"].values
            np.savez("user_vektor.npz",id=self.user_id,vektor=self.vektorler)
            self.connection.close()
            self.load_data()
            print("create harcana  süre", time.time() - start)
            return {"code":"0x202","mess":"suceessfull"}
        except Exception as err:
            print(err)
            return {"code":"0x404", "mess":f"hata kodu {err}:"}
            



vektor_search = Sorting_User()
vektor_search.load_data()





