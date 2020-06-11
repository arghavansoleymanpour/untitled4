import mysql.connector


# import database as db1


# arguments = ('arghavan',)
# cursor.callproc('if_user_exists', arguments)

# connection.commit()

# for result in cursor.stored_results():
#     print(result.fetchall())


# def main_process(cursor, connection):
# input0 = input('1.signup or 2.login')
# if input0 == '1':
# sign_up(cursor, connection)
# elif input0 == '2':
# log_in(cursor, connection)


def sign_up(cursor, connection):
    in1 = input('enter your username:\n')
    in2 = input('enter your password:\n')
    in3 = input('enter your account_number:\n')
    in4 = input('enter your name:\n')
    in5 = input('enter your lastname:\n')
    in6 = input('enter your address:\n')
    in7 = input('enter your birthDate:\n')
    in8 = input('enter your phone_number:\n')
    in9 = input('enter your id:\n')
    in10 = input('enter your nikname:\n')

    arguments = (in1, in2, in3, in4, in5, in6, in7, in8, in9, in10)
    cursor.callproc('createnewuser', arguments)
    connection.commit()

    for result in cursor.stored_results():
        print(result.fetchall())


def log_in(cursor, connection):
    a = input('please enter username \n ')
    b = input('enter your password \n ')

    arguments = (a, b)
    cursor.callproc('Authentication', arguments)
    connection.commit()

    for result in cursor.stored_results():
        print(result.fetchall())


def main_process(cursor, connection):
    input0 = input('1.Edit or 2.createnews or3.deleteEverything or 4.insertaccount or 5.sendEmail')
    if input0 == '1':
        Edit(cursor, connection)
    elif input0 == '2':
        createnews(cursor, connection)
    elif input0 == '3':
        deleteEverything(cursor, connection)
    elif input0 == '4':
        insertaccount(cursor, connection)
    elif input0 == '5':
        SendEmail(cursor, connection)


def Edit(cursor, connection):
    input0 = input('please change your password \n')
    input1 = input('please change your account number \n')
    input2 = input('please change your name \n')
    input3 = input('please change your lastName \n')
    input4 = input('please change your address \n')
    input5 = input('please change your birthDate \n')
    input6 = input('please change your phone_number \n')
    input7 = input('please change your id  \n')
    input8 = input('please change your nikName \n')

    arguments = (input0, input1, input2, input3, input4, input5, input6, input7, input8)
    cursor.callproc('EditInformation', arguments)
    connection.commit()

    for result in cursor.stored_results():
        print(result.fetchall())


def createnews(cursor, connection):
    input1 = input('write your text \n')
    input2 = input('write yor comment \n')
    arguments = (input1, input2)
    cursor.callproc('create_news', arguments)
    connection.commit()

    for result in cursor.stored_results():
        print(result.fetchall())


def deleteEverything(cursor, connection):
    input1 = input('delete your username \n')
    arguments = (input1)
    cursor.callproc('deleteEverything', arguments)
    connection.commit()

    for result in cursor.stored_results():
        print(result.fetchall())


# def getinformation(cursor,connection):
# cursor.callproc('deleteEverything')
# connection.commit()

# for result in cursor.stored_results():
# print(result.fetchall()# )

def insertaccount(cursor, connection):
    input1 = input('please write your nameAccount \n ')
    arguments = (input1,)
    cursor.callproc('insertaccount', arguments)
    connection.commit()

    for result in cursor.stored_results():
        print(result.fetchall())


def SendEmail(cursor, connection):
    input1 = input('please write your subject \n')
    input2 = input('please write your emailgetter \n')
    input3 = input('please write your ccgetter \n')
    input4 = input('please write your textofemail \n')
    arguments = (input1, input2, input3, input4)
    cursor.callproc('sendemail', arguments)
    connection.commit()


def emailingtomany(cursor, connection):
    input1 = input('please enter emailgetter \n')
    input2 = input('please enter ccgetter \n ')
    input3 = input('please enter subject \n')
    input4 = input('please enter textOfEmail \n')

    # arguments = (input1, input2, input3, input4, input5)
    # cursor.callproc('emailingtomany', arguments)
    # connection.commit()

    input1 = input1.split(',')

    for i in range(len(input1)):
        arguments = (input3, input1[i], '0', input4)
        cursor.callproc('sendemail', arguments)
        connection.commit()

    input2=input2.split(',')
    for i in range(len(input2)):
        arguments = (input3, '0',input2[i], input4)
        cursor.callproc('sendemail', arguments)
        connection.commit()


def getnews(cursor,connection):
    arguments = ()
    cursor.callproc('getnews', arguments)
    connection.commit()

def blockuser(cursor,connection):
    input1=input('please enter usename of the person you want to block \n')
    arguments= (input1, )
    cursor.callproc('BlockUser',arguments)
    connection.commit()
def getMyinformation(cursor,connection):
    arguments= ()
    cursor.callproc('getinformation',arguments)
    connection.commit()
    for result in cursor.stored_results():
        print(result.fetchall())






if __name__ == "__main__":
    connection = mysql.connector.connect(host="localhost",
                                         user="root",
                                         db="foofle")

    cursor = connection.cursor()


    # main_process(cursor, connection)
    # emailingtomany(cursor, connection)
    # blockuser(cursor,connection)
    getMyinformation(cursor,connection)