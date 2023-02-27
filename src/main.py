import asyncio

from src.database import database, metadata, engine
from datetime import datetime
import ormar
from multiprocessing import Pool

import pysolr

from src import cfg
from src.models import FILES_M



# def str2integer(s):
#     try:
#         return int(s)
#     except ValueError:
#         return 0


# def work_log(data_for_work):
#     print(" Process name is %s waiting time is %s seconds" % (data_for_work[0], data_for_work[1]))
#     time.sleep(int(data_for_work[1]))
#     print(" Process %s Executed." % data_for_work[0])


async def try_pg2():

    # p = Pool(2)
    # p.map(work_log, w)

    # time1 = datetime.now()
    # print('Starting at :' + str(time1))
    #
    # # solr_delete()
    # if not database.is_connected:
    #     await database.connect()
    # cnt = 0
    # # print(cnt)
    # files = await FILES_M.objects.all() #limit(10).all()
    # len_files = len(files)
    #
    # for file_item in files:
    #     # print(file_item.file_path)
    #     print(f"{cnt} of {len_files}. Осталось {len_files - cnt}")
    #     file_path = file_item.file_path
    #     file_size = file_item.file_size
    #     solr_add(file_path, file_size)
    #     cnt += 1
    #     # time3 = datetime.now()
    #     # print('one:' + str(time3))
    #     # print('time left: ' + str(time3 - time1))
    #     # file_path = file_item.file_path
    #
    # time2 = datetime.now()
    # print('Finishing at :' + str(time2))
    # print('Total time : ' + str(time2 - time1))
    print('DONE !!!!')


async def try_pg():
    time1 = datetime.now()
    print('Starting at :' + str(time1))

    # solr_delete()
    if not database.is_connected:
        await database.connect()
    cnt = 0
    # print(cnt)
    files = await FILES_M.objects.all() #limit(10).all()
    len_files = len(files)

    for file_item in files:
        # print(file_item.file_path)
        print(f"{cnt} of {len_files}. Осталось {len_files - cnt}")
        file_path = file_item.file_path
        file_size = file_item.file_size
        solr_add(file_path, file_size)
        cnt += 1
        # time3 = datetime.now()
        # print('one:' + str(time3))
        # print('time left: ' + str(time3 - time1))
        # file_path = file_item.file_path

    time2 = datetime.now()
    print('Finishing at :' + str(time2))
    print('Total time : ' + str(time2 - time1))
    print('DONE !!!!')


def solr_add(file_path: str = "", file_size: str = ''):
    # Create a client instance. The timeout and authentication options are not required.
    str_solr_conn = f"http://{cfg.SOLR_HOST}:{cfg.SOLR_PORT}/solr/{cfg.SOLR_COLL}"
    # print(str_solr_conn)
    solr = pysolr.Solr(str_solr_conn,
                       always_commit=True,
                       auth=(cfg.SOLR_USER, cfg.SOLR_PASS)
                       )  # timeout = 10,

    str_tmp = solr.add(
        {
            "file_path": file_path,
            "file_size": int(file_size)
        }
    )
    # print(str_tmp)


def solr_delete():
    str_solr_conn = f"http://{cfg.SOLR_HOST}:{cfg.SOLR_PORT}/solr/{cfg.SOLR_COLL}"
    solr = pysolr.Solr(str_solr_conn,
                       always_commit=True,
                       auth=(cfg.SOLR_USER, cfg.SOLR_PASS)
                       )  # timeout = 10,
    str_tmp = solr.delete(q='*:*')
    print(str_tmp)


if __name__ == "__main__":
    asyncio.run(try_pg())

    # try_solr()
    # set_logger()
    # uvicorn.run("main:app", host=cfg.SERVER_HOST, port=cfg.SERVER_PORT, reload=True)
