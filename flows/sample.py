from prefect import task, Flow
from prefect.tasks.mysql.mysql import MySQLFetch
from prefect.tasks.secrets import PrefectSecret
from prefect.client import Secret

import prefect

run_mysql_query = MySQLFetch(
    db_name = Secret('MYSQL_DATABASE').get(),
    host = Secret('MYSQL_HOST').get(),
    user = Secret('MYSQL_USER').get(),
    password = Secret('MYSQL_PASSWORD').get(),
    cursor_type = 'sscursor',
    fetch = 'all',
    query = '''
        select 'adhe' as engineer
        union
        select 'bilal' as engineer
    '''
)

@task
def print_result(result):
    logger = prefect.context.get("logger")
    logger.info(result)
    print(result)


with Flow('anu') as flow:

    result = run_mysql_query()
    print_result(result)

if __name__ == '__main__':
    flow.run()