from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()


class Station(Base):
    __tablename__ = "stations"

    id = Column(String, primary_key=True)  # Station ID from pyhafas
    name = Column(String, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)

    # Relationship to delays
    delays = relationship("TrainDelay", back_populates="station")


class TrainDelay(Base):
    __tablename__ = "train_delays"

    id = Column(Integer, primary_key=True, autoincrement=True)
    station_id = Column(String, ForeignKey("stations.id"), nullable=False)
    train_id = Column(String, nullable=False)
    train_line = Column(String)

    scheduled_departure = Column(DateTime)
    actual_departure = Column(DateTime)
    scheduled_arrival = Column(DateTime)
    actual_arrival = Column(DateTime)

    departure_delay_minutes = Column(Integer, default=0)
    arrival_delay_minutes = Column(Integer, default=0)

    is_cancelled = Column(Boolean, default=False)
    platform = Column(String)
    reason = Column(String)  # Delay reason if available

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    station = relationship("Station", back_populates="delays")