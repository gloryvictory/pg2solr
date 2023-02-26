

# from src import cfg
# from src.database import database, metadata, engine
import pysolr

def try_solr():

    # Create a client instance. The timeout and authentication options are not required.
    solr = pysolr.Solr('http://localhost:8983/solr/files', always_commit=True, auth = ('solr', 'Ghbdtn123!'))     # timeout = 10,
    # solr = pysolr.Solr('http://solr:Ghbdtn123!@localhost:8983/solr/files', always_commit=True, timeout=10)

    str_tmp = solr.ping()
    print(str_tmp)
    str_tmp = solr.add(
        [
            {
                "file_path": "\\r57-vfs01.zsniigg.local\volarch\!_2019_ГПН-190900_000919_Р_048_2019-Д_01032019_СМотреть\ЗСНГП-НФ_ОтвИспРусаковПС_Межовский\2004г_Отчёт_НОВОСИБ_ТННЦ_1277_04\MAP\IZOPACH\IZOPACH_RAK_VOST\isopach_t1_b.srf",
                "file_size": "132"
            },
            {
                "file_path": "\\r57-vfs01.zsniigg.local\volarch\!_2019_ГПН-190900_000919_Р_048_2019-Д_01032019_СМотреть\ЗСНГП-НФ_ОтвИспРусаковПС_Межовский\2004г_Отчёт_НОВОСИБ_ТННЦ_1277_04\PRIL\pril_10.cdr",
                "file_size": "234"
            }
        ]
    )
    print(str_tmp)



if __name__ == "__main__":
    try_solr()
    # set_logger()
    # uvicorn.run("main:app", host=cfg.SERVER_HOST, port=cfg.SERVER_PORT, reload=True)
