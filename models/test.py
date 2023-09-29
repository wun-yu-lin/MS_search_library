

# from sqlalchemy import  BIGINT, TIMESTAMP,create_engine, URL
# from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column
# from sqlalchemy.sql import func
# import datetime, sys
# sys.path.insert(1, "./")
# import config
# # from models.Spectrum_data_model import Spectrum_data
# # from models.Base_model import Base
# ##  sql config
# url_object = URL.create(
#     config.DIALECT_DRIVER,
#     username=config.MYSQL_USER,
#     password=config.MYSQL_PASSWORD, 
#     host=config.MYSQL_HOST, 
#     database=config.MYSQL_DATABASE,
# )


# class Base(DeclarativeBase):
#     type_annotation_map = {
#         int: BIGINT,
#         datetime.datetime: TIMESTAMP(timezone=True)
#     }

# class Spectrum_data(Base):
#     __tablename__ = "spectrum_data"
#     id:Mapped[int] = mapped_column(primary_key=True, autoincrement= True, unique=True,nullable=True)


# # spectrum_data = Spectrum_data(
# #     ms_level=1,
# #     compound_data_id=1,
# #     compound_classification_id=1,
# #     precursor_mz=1,
# #     collision_energe=1,
# #     mz_error=1,
# #     data_source="1",
# #     tool_type="1",
# #     ion_mode="1",
# #     instrument="1",
# #     exact_mass=1,
# #     precursor_type="1",
# #     ms2_spectrum="1"
# # )




# # base = Base()
# engine = create_engine(url_object)
# Base.metadata.create_all(engine)
# # # base.metadata.create_all(engine)
# # Session =sessionmaker(bind=engine)
# # # session = Session()


# # session.add(spectrum_data)
# # session.commit()
# # session.close()

# from Base_model import Session_tool

# session_tool = Session_tool()
# session = session_tool.session