from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database import Author

def opendb():
    engine =create_engine ('sqlite://mydb.sqlite')
    session =sessionmaker(bind=engine)
    return session()


while True:
    print('_'*20)
    print('1.Add author')
    print('2.display author')
    print('3.Quit')
    print('_'*20)
    choice =input('enter your choice:')
    if choice =='1':
        pass
    elif choice =='2':
        pass
    elif choice =='3':
        break
    
