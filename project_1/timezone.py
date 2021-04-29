from datetime import timedelta
import numbers
from datetime import datetime

class TimeZone:

    def __init__(self, name, offset_hours, offset_minutes):

        if name is None and len(name.strip()) == 0:
            raise ValueError("Timezone name cannot be empty.")

        self._name = name

        if not isinstance(offset_minutes, numbers.Integral):
            raise ValueError("Minutes offset must be an integer number.")


        if not isinstance(offset_hours, numbers.Integral):
            raise ValueError("Hours offset must be an integer number.")

        if offset_minutes > 59 or offset_minutes < -59:
            raise ValueError("Minutes offset must be between -59 and 59 (inclusive).")


        offset = timedelta(hours=offset_hours, minutes=offset_minutes)

        if offset < timedelta(hours=-12, minutes=0) or offset > timedelta(hours=14, minutes=0):
            raise ValueError("Offset must be between -12:00 to +14:00.")

        self._offset = offset
        self._offset_hours = offset_hours
        self._offset_minutes = offset_minutes

    @property
    def offset(self):
        return self._offset
    
    @property
    def name(self):
        return self._name


    def __eq__(self, other):
        return (isinstance(other, TimeZone) and 
         self.name == other.name and
         self._offset_hours == other._offset_hours and
         self._offset_minutes == other._offset_minutes)


    def __repr__(self):     
        return (f"TimeZone(name='{self.name}',\
                offset_hours={self._offset_hours},\
                offset_minutes={self._offset_minutes})")

        
if __name__ == "__main__":
    dt = datetime.utcnow()
    print(f"current date : {dt}")
    tz = TimeZone('ABC', 12, 0)
    print(f"Timezone : {tz}")
    print(f"Add offset : {dt + tz.offset}")
