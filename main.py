import schedule
import time
import requests
import sys
import json
from thehive4py.api import TheHiveApi
from thehive4py.models import Case, CaseTask, CustomFieldHelper
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

api = TheHiveApi('https://thehive.rkomi.ru', 'q4Z/SWGO3IBXE+HtwBYyWL/9EYw36c2+', cert=False)

def job():
    tasks = [
        CaseTask(title='ЕСК-102', status='Waiting', flag=True)
    ]
    # Prepare the custom fields

    case = Case(title='Периодические работы: ЕСК-102 - Контроль наличия обычных учеток в All Computer Admins',
                tlp=3,
                flag=True,
                tags=['Periodic', 'ESK-102'],
                description='https://secmon.rk.local/wiki/%D0%95%D0%A1%D0%9A-102%E2%80%8B_-_%D0%9A%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C_%D0%BD%D0%B0%D0%BB%D0%B8%D1%87%D0%B8%D1%8F_%D0%BE%D0%B1%D1%8B%D1%87%D0%BD%D1%8B%D1%85_%D1%83%D1%87%D0%B5%D1%82%D0%BE%D0%BA_%D0%B2_All_Computer_Admins',
                tasks=tasks)

    # Create the case
    print('Create Case')
    print('-----------------------------')
    id = None
    response = api.create_case(case)
    print(response.status_code)
    if response.status_code == 201:
        print(json.dumps(response.json(), indent=4, sort_keys=True))
        print('')
        id = response.json()['id']
    else:
        print('ko: {}/{}'.format(response.status_code, response.text))
        sys.exit(0)

    # Get all the details of the created case
    print('Get created case {}'.format(id))
    print('-----------------------------')
    response = api.get_case(id)
    if response.status_code == requests.codes.ok:
        print(json.dumps(response.json(), indent=4, sort_keys=True))
        print('')
    else:
        print('ko: {}/{}'.format(response.status_code, response.text))

    print('Add a task {}'.format(id))
    print('-----------------------------')
    response = api.create_case_task(id, CaseTask(
        title='Периодические работы: ЕСК-102 - Контроль наличия обычных учеток в All Computer Admins',
        status='InProgress',
        owner='b.a.nesterov@cit.rkomi.ru',
        description='Выполнить периодическую задачу: \n\r\n '
                    'Описание по ссылке: https://secmon.rk.local/wiki/%D0%95%D0%A1%D0%9A-102%E2%80%8B_-_%D0%9A%D0%BE%D0%BD%D1%82%D1%80%D0%BE%D0%BB%D1%8C_%D0%BD%D0%B0%D0%BB%D0%B8%D1%87%D0%B8%D1%8F_%D0%BE%D0%B1%D1%8B%D1%87%D0%BD%D1%8B%D1%85_%D1%83%D1%87%D0%B5%D1%82%D0%BE%D0%BA_%D0%B2_All_Computer_Admins',
        flag=True,
        startDate=int(time.time()) * 1000))
    if response.status_code == 201:
        print(json.dumps(response.json(), indent=4, sort_keys=True))
        print('')
    else:
        print('ko: {}/{}'.format(response.status_code, response.text))
def job_day ():
    print("I'm working every day")

def main():

    schedule.every(10).seconds.do(job) # executing m
    schedule.every().day.do(job_day) # executing daily
    schedule.every().saturday.at("21:49").do(job_day)
    while True:
        schedule.run_pending()
        time.sleep(1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


