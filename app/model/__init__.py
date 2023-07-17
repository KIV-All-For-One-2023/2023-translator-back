# """MariaDB Module"""
# from typing import Union

# from sqlalchemy import exc
# from sqlalchemy.dialects.mysql import insert

# from search_api.v1.model.maria.conn import create_engine_session
# from search_api.v1.core.settings import setting
# from search_api.v1.model.schema import SearchAPIInternalError
# from search_api.v1.model.maria.tables.clinic import Base as clinic_base
# from search_api.v1.model.maria.tables.images import Base as images_base

# CLINIC_ENGINE, CLINIC_SESSION_MAKER = create_engine_session(
#     setting.DATABASES.mariaDB.CLIENT.us_clinic.db_name, setting
#     )
# # clinic_base.metadata.drop_all(bind=CLINIC_ENGINE)
# clinic_base.metadata.create_all(bind=CLINIC_ENGINE, checkfirst=True)

# IMAGE_ENGINE, IMAGE_SESSION_MAKER = create_engine_session(
#     setting.DATABASES.mariaDB.CLIENT.us_image.db_name, setting
#     )
# images_base.metadata.create_all(bind=IMAGE_ENGINE, checkfirst=True)


# class BaseMariaDB:
#     """Base MySQL database class"""
#     # pylint: disable=no-member
#     def __enter__(self):
#         return self

#     def __exit__(self, *args):
#         """Shall be called when an instance dies"""
#         self.session.close()

#     def commit(self):
#         """Commit!"""
#         self.session.commit()

#     def close_session(self):
#         """Close maria session"""
#         self.session.close()

#     def get_record(self, cols: list):
#         """Get one record from db

#         Args:
#             cols (list): columns

#         Returns:
#             _type_: record
#         """
#         row = self.session.query(*cols).first()
#         if row is None:
#             return False
#         return row

#     def get_multiple_records(self, cols: list) -> list:
#         """Get bunch of records from db

#         Args:
#             cols (list): columns

#         Returns:
#             list: records
#         """
#         rows = self.session.query(*cols).all()
#         return rows if len(rows) != 0 else []

#     def execute_query(self, query: str, fetch_one: bool = False) -> tuple:
#         """Execute Raw Query"""
#         if fetch_one:
#             data = self.session.execute(query).fetchone()
#         else:
#             data = self.session.execute(query).fetchall()
#         if not data:
#             return ()
#         return data

#     def insert_record(
#             self,
#             table: object,
#             value: dict,
#             upsert_key: str = None
#             ) -> int:
#         """Insert one record to db

#         Args:
#             value (dict): data

#         Returns:
#             bool: Good or Somthing's wrong(Maybe Integrity Error)
#         """
#         try:
#             query = insert(table).values(value)
#             if upsert_key is not None:
#                 query = query.on_duplicate_key_update({upsert_key: value[upsert_key]})
#             res = self.session.execute(query)
#         except exc.OperationalError:
#             self.session.rollback()
#             raise
#         self.session.commit()
#         return res.inserted_primary_key[0]

#     def insert_bulk(
#             self,
#             table: object,
#             values: list[dict],
#             upsert_key: list[str] = None,
#             exist_ok: bool = False,
#             return_column: str = "",
#             commit_later: bool = False
#         ) -> Union[bool, list]:
#         """Insert bunch of records to db

#         Args:
#             table: should call __table__

#         Returns:
#             bool: Good or Somthing's wrong
#         # TODO: Add Some Exceptions
#         """
#         stmt = insert(table).values(values)
#         if exist_ok:
#             stmt = stmt.prefix_with("IGNORE")
#         if upsert_key is not None:
#             stmt = stmt.on_duplicate_key_update(
#                 {uk: getattr(stmt.inserted, uk) for uk in upsert_key})
#         try:
#             if return_column:
#                 stmt = stmt.returning(getattr(table, return_column))
#                 res = self.session.execute(stmt).all()
#                 if len(res) != len(values):
#                     raise SearchAPIInternalError(
#                         f"Report insertion failed: {table.fullname}", 500)
#                 if not commit_later:
#                     self.commit()
#                 return [x[0] for x in res]
#             self.session.execute(stmt)
#             if not commit_later:
#                 self.commit()
#         except exc.IntegrityError:
#             self.session.rollback()
#             raise
#         except exc.ProgrammingError:
#             self.session.rollback()
#             raise
#         finally:
#             if not commit_later:
#                 self.close_session()
#         return True


# class ClinicMariaDB(BaseMariaDB):
#     """Mysql database class for clinic db"""
#     def __init__(self):
#         super().__init__()
#         self.session_maker = CLINIC_SESSION_MAKER
#         self.session = self.session_maker()


# class ImageMariaDB(BaseMariaDB):
#     """Mysql database class for image db"""
#     def __init__(self):
#         super().__init__()
#         self.session_maker = IMAGE_SESSION_MAKER
#         self.session = self.session_maker()
