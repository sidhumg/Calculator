import mysql.connector

class connect_db:
    def __init__(self) :
        self.db = mysql.connector.connect(
            host = '127.0.0.1',
            user = 'root',
            password = 'Schooldbms#',
            port = '3306',
            database = 'school'
        )

    def selection(self,table_name):
        print('c')
        query = f'select * from  {table_name}'
        cursor = self.db.cursor()
        cursor.execute(query)
        if table_name == 'admin':
            result=cursor.fetchall()
            return(result)
        self.db.commit()
        

    def insertions(self,table_name):
        query = f'select column_name from information_schema.columns where table_name = "{table_name}" order by ordinal_position;'
        cursor = self.db.cursor() 
        cursor.execute(query)
        column = cursor.fetchall()
        print('Enter the below data:')
        col_value=[None]*len(column)
        for i in range(len(column)):
            column[i]=str(column[i])
            column[i]=column[i][2:-3]
            print(column[i])
            col_value[i] = input()
            col_value[i]=f"'{col_value[i]}'"
        c=', '.join(map(str,column))
        cv=', '.join(map(str, col_value))
        x=f'insert into {table_name} ({c}) values ({cv})'
        print(x)
        cursor.execute(x)
        self.db.commit()
        

    def update(self,table_name):
        query = f'select column_name from information_schema.columns where table_name = "{table_name}" order by ordinal_position;'
        cursor = self.db.cursor() 
        cursor.execute(query)
        column = cursor.fetchall()
        print('Enter the data you want to update:\n ')
        for i in range(len(column)):
            column[i]=str(column[i])
            column[i]=column[i][2:-3]
            print(f' {i+1}. {column[i]}|')
        update_value=input()
        update_value=int(update_value)-1
        print('Enter new value:')
        up=str(input())
        print('Enter the condition column:')
        con=input()
        con=int(con)-1
        c=column[con]
        print('Enter the condition column value:')
        con_value=input()
        cursor.execute('SET SQL_SAFE_UPDATES = 0;')
        self.db.commit
        x=f'update {table_name} set {column[update_value]} =\'{up}\' where {c} =\'{con_value}\';'
        print(x)
        cursor.execute(x)
        self.db.commit()

        

    def delete(self,table_name):
        query = f'select column_name from information_schema.columns where table_name = "{table_name}" order by ordinal_position;'
        cursor = self.db.cursor() 
        cursor.execute(query)
        column = cursor.fetchall()
        print('Do you want to delete the entire table: y or n\n ')
        d=input()
        if d=='y':
            cursor.execute(f'delete from {table_name};' )
            self.db.commit()
        else:
            for i in range(len(column)):
               column[i]=str(column[i])
               column[i]=column[i][2:-3]
               print(f' {i+1}. {column[i]}|')
            print('Enter the condition column:')
            con=input()
            con=int(con)-1
            c=column[con]
            print('Enter the condition: > or = or <')
            co=input()
            print('Enter the condition column value:')
            con_value=input()
            cursor.execute(f'delete from {table_name} where {c}{co}\'{con_value}\';' )
            self.db.commit()
    
    def view(self,table_name):
        cursor = self.db.cursor()
        cursor.execute(f'SELECT * FROM {table_name}')
        values=cursor.fetchall()
        for row in values:
            print(row)



print('Enter the admin Username:')
admin_user = input()
print('Enter the admin password:')
admin_pass = input()
admin_data = (admin_user,admin_pass)
global x
database = connect_db()
admin_existingdata = database.selection('admin')


for i in range(len(admin_existingdata)):
    if set(admin_data).issubset(set(admin_existingdata[i])):
        x=1
        break
    else:
        x=0
if x==1:
    print('Enter the table no. you wish to select: |1. Student |2. Teacher |3.Principal')
    t = input()
    t1 = ['student','teacher','principal']
    table = t1[int(t)-1]
    print(f'Table \'{table}\' is selected.')
    if set(t).issubset(set(['1','2','3'])):
        print('Enter the operation no. you wish to perform: |1. Add |2. Update |3. Delete')
        op = input()
        if int(op)==1:
            database.insertions(table)
        if int(op)==2:
            database.update(table)
        if int(op)==3:
            database.delete(table)
else:
    print('You can only view the data.')
    print('Select the table you wish to view: |1. Student |2. Teacher |3.Principal')
    t = input()
    t1 = ['student','teacher','principal']
    table = t1[int(t)-1]
    database.view(table)

    
