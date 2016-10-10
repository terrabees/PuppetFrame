from sqlalchemy import Column, Integer, BigInteger, String, ForeignKey, DECIMAL, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

PuppetModel = declarative_base()


class Account(PuppetModel):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), nullable=False, index=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    password = Column('password_hash', String(100), nullable=False)


class Address(PuppetModel):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fk_account_id = Column(Integer, ForeignKey(Account.id), nullable=True, index=True)
    organization_name = Column(String(100), nullable=True)
    unit = Column(String(50), nullable=True)
    sub_premise = Column(String(100), nullable=True)
    premise = Column(String(100), nullable=True)
    thoroughfare = Column(String(100), nullable=True)
    postal_code = Column(String(25), nullable=True)
    dependent_locality = Column(String(100), nullable=True)
    locality = Column(String(100), nullable=True)
    sub_administrative_area = Column(String(100), nullable=True)
    administrative_area = Column(String(100), nullable=True)
    country = Column(String(2), nullable=False)

    account = relationship('Account', back_populates='addresses')
    Account.addresses = relationship('Address', order_by=id, back_populates='account')
