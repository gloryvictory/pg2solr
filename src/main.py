from src.database import database, metadata, engine
from datetime import datetime
import ormar

import pysolr

from src import cfg
from src.models import FILES_M


async def try_pg():
    cnt = 0
    files = await FILES_M.objects.all()
    # for file_item in files:
    # # async for file_item in FILES_M.objects.iterate():
    #     if cnt < 10:
    #         assert  print(file_item.file_path)
    #     else:
    #         break
    #     cnt += 1


def try_solr():
    # Create a client instance. The timeout and authentication options are not required.
    str_solr_conn = f"http://{cfg.SOLR_HOST}:{cfg.SOLR_PORT}/solr/{cfg.SOLR_COLL}"
    print(str_solr_conn)
    solr = pysolr.Solr(str_solr_conn,
                       always_commit=True,
                       auth=(cfg.SOLR_USER, cfg.SOLR_PASS)
                       )  # timeout = 10,
    # solr = pysolr.Solr('http://solr:Ghbdtn123!@localhost:8983/solr/files', always_commit=True, timeout=10)
    str_tmp = solr.ping()
    print(str_tmp)
    str_tmp = solr.delete(q='*:*')
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
    try_pg()
    # try_solr()
    # set_logger()
    # uvicorn.run("main:app", host=cfg.SERVER_HOST, port=cfg.SERVER_PORT, reload=True)
