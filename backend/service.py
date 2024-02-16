from sqlalchemy import JSON, create_engine, MetaData, Table, select, insert, true, update, Column, and_, or_
from sqlalchemy.orm import sessionmaker, Session
import os
from beans.tables import Task

IS_DATABASE_VERBOSE = False

def get_all(DB_name):
    '''
        Retrieve all the data for the frontend.
        Returns:
            {
                db_data
            }
    '''

    session = build_session(DB_name)
    print("########################################## BEGIN GET ALL #########################################")
    print(DB_name)

    try:
        tasks = get_all_tasks(session)
    except:
        session.close()
        print("There was a fetch problem.")
     
    res = {}
    res['tasks'] = tasks
    session.close()
    return res

def get_all_tasks(session):
    '''
        Retrieve all the data in the 'tasks' DB table.
        Parameters:
            - session: Database session.
        Returns:
            {param_name: param_value, ...}
    '''

    res = session.query(Task)

    typeArr = []
    for row in res:
        typeArr.append(
            {
            'key': row.id_task,
            'name': row.name,
            'begin_date': row.begin_date,
            'end_date': row.end_date,
            'id_parent_task': row.id_parent_task,
            }
            )
    return typeArr

def build_session(DB_name):
    '''
        Returns:
            Sqlalchemy session for given database name.
    '''
    engine = build_engine(DB_name)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def build_engine(DB_name):
    '''
        Returns:
            Sqlalchemy db engine for given database name.
    '''
    user = os.environ.get('DATABASE_USER', 'postgres')
    password = os.environ.get('DATABASE_PASSWORD', 'password').replace('@','%40')
    local = os.environ.get('DB_HOST', 'localhost')

    connect_string = 'postgresql+psycopg2://%s:%s@%s/%s' % (user, password, local, DB_name)
    print("connecting to: " + connect_string)
    if IS_DATABASE_VERBOSE:
        print("connecting to: " + connect_string)
    return create_engine(connect_string, echo=IS_DATABASE_VERBOSE)