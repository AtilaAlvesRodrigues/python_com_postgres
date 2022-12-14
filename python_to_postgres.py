import psycopg2
import psycopg2.extras

#no caso o nome da minha database era teste, então altera para a sua 
hostname = 'localhost'
database = 'teste'
username = 'postgres'
pwd = 'admin'
port_id = 5432
conn = None

#alterar para a sua senha em password
try:
    with psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = senha_bem_aqui,
                port = port_id) as conn:

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:

            cur.execute('DROP TABLE IF EXISTS employee')

            create_script = ''' CREATE TABLE IF NOT EXISTS employee (
                                    id      int PRIMARY KEY,
                                    name    varchar(40) NOT NULL,
                                    salary  int,
                                    dept_id varchar(30)) '''
            cur.execute(create_script)

            insert_script  = 'INSERT INTO employee (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'
            insert_values = [(1, 'Atila', 12000, 'D1'), (2, 'Alves', 15000, 'D1'), (3, 'Rodrigues', 20000, 'D2')]
            for record in insert_values:
                cur.execute(insert_script, record)

            update_script = 'UPDATE employee SET salary = salary + (salary * 0.5)'
            cur.execute(update_script)

            delete_script = 'DELETE FROM employee WHERE name = %s'
            delete_record = ('Rodrigues',)
            cur.execute(delete_script, delete_record)

            cur.execute('SELECT * FROM EMPLOYEE')
            for record in cur.fetchall():
                print(record['name'], record['salary'])
                #se tudo der certo vai sair o nome e o salario
                
except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
