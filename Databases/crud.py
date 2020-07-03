from main import db,Puppy

my_puppy = Puppy('Rufus',5)
db.session.add(my_puppy)
db.session.commit()

all_puppies = Puppy.query.all()


puppy_1 = Puppy.query.get(1)


puppy_franky = Puppy.query.filter_by(name='Franky')
print(puppy_franky.all())

#Update

puppy_1.age = 10
db.session.add(puppy_1)
db.session.commit()

print(puppy_1)

#Delete 

db.session.delete(puppy_1)
db.session.commit()