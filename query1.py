from data.users import User
from data import db_session

db_session.global_init('database/mars_explorer.db')
session = db_session.create_session()

capitan = User()
capitan.surname = 'Scott'
capitan.name = 'Ridley'
capitan.age = 21
capitan.position = 'captain'
capitan.speciality = 'research engineer'
capitan.address = 'module_1'
capitan.email = 'scott_chief@mars.org'
capitan.hashed_password = ''

capitan1 = User()
capitan1.surname = 'Sasha'
capitan1.name = 'Smirnov'
capitan1.age = 9
capitan1.position = 'helper'
capitan1.speciality = 'doctor'
capitan1.address = 'module_2'
capitan1.email = 'scott_chiefir@mars.org'
capitan1.hashed_password = ''

capitan2 = User()
capitan2.surname = 'Tommy'
capitan2.name = 'Hilfiger'
capitan2.age = 41
capitan2.position = 'chef'
capitan2.speciality = 'programmer'
capitan2.address = 'module_3'
capitan2.email = 'tommy@mars.org'
capitan2.hashed_password = ''

capitan3 = User()
capitan3.surname = 'Jdun'
capitan3.name = 'Vkino'
capitan3.age = 99
capitan3.position = 'chefir'
capitan3.speciality = 'povar'
capitan3.address = 'module_4'
capitan3.email = 'jdunvkino@mars.org'
capitan3.hashed_password = ''


session.add(capitan1)
session.add(capitan2)
session.add(capitan3)
session.add(capitan)
session.commit()