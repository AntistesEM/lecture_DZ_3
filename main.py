import requests
import datetime


class Stackoverflow:
    host = 'https://api.stackexchange.com/2.3/questions'

    def get_questions(self, tag, days):
        date = datetime.date.today() - datetime.timedelta(days=days)
        url = self.host
        params = {
            'site': 'stackoverflow',
            'tagged': tag,
            'fromdate': date
        }
        response = requests.get(url, params=params).json()
        print(f'Вопросы с тегом {tag} в период с {date} по '
              f'{datetime.datetime.today().replace(microsecond=0)}:')
        for question in response.get('items'):
            print(
                f'Вопрос: {question["title"]} \n   Ссылка: {question["link"]}'
            )


if __name__ == '__main__':
    st = Stackoverflow()
    st.get_questions('Python', 2)
